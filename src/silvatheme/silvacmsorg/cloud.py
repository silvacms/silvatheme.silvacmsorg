
from five import grok
from zope import interface, schema
from z3c.schema.email import RFC822MailAddress
from zeam.form import silva as silvaforms
from silva.core.interfaces import IContainer
from Products.Silva.mail import sendmail
from silva.translations import translate as _
from zope.traversing.browser import absoluteURL

TEMPLATE = u"""
You have a new cloud request!

From: {name}
Company: {company_name}
Subdomain: {subdomain_name}
Email: {email}
Telephone: {telephone}

{comment}
"""


class IContactFields(interface.Interface):
    """Describe a comment.
    """
    name = schema.TextLine(title=u"Your name", required=True)
    company_name = schema.TextLine(
        title=u"Company", required=False, default=u'')
    subdomain_name = schema.TextLine(
        title=u"Subdomain", required=True, default=u'')
    email = RFC822MailAddress(title=u"Email", required=True)
    telephone = schema.TextLine(
        title=u"Telephone", required=False, default=u'')
    comment = schema.Text(
        title=u"Comment", required=False)


class CloudForm(silvaforms.PublicForm):
    """Cloud form.
    """
    grok.name('cloud.html')
    grok.context(IContainer)

    label = _(u'Cloud instance')
    description = _(u"""You can request a cloud instance using this form.
                        The instance will usually
                        be setup in less than a business day.
                        Once your instance is setup you'll be sent a URL,
                        e.g.: http://yourname.silvacms.org/.
                        Then you'll have your own Silva sandbox
                        and you can give Silva an extensive test drive.""")
    fields = silvaforms.Fields(IContactFields)

    @silvaforms.action(_(u"Get your cloud instance!"),
                       identifier='cloud', accesskey='c')
    def cloud(self):
        data, errors = self.extractData()
        if errors:
            self.status = _(u'Please correct the errors.')
            return silvaforms.FAILURE
        sendmail(self.context, TEMPLATE.format(**data.getDictWithDefault()),
                 mto='sales@infrae.com', mfrom='sales@infrae.com',
                 subject='Cloud instance request from silvacms.org')
        success = self.context.get_root()._getOb('success', None)
        if success is not None:
            self.response.redirect(absoluteURL(success, self.request))
        else:
            self.status = _(u'Thank you for your request.')
        return silvaforms.SUCCESS
