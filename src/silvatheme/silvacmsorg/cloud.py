
from Products.Silva.mail import sendmail
from five import grok
from silva.core.interfaces import IContainer
from silva.core.views import views as silvaviews
from silva.translations import translate as _
from z3c.schema.email import RFC822MailAddress
from zeam.form import silva as silvaforms
from zope import interface, schema
from zope.traversing.browser import absoluteURL

grok.templatedir('templates_silvacmsorg')

TEMPLATE = u"""
You have a new cloud request!

From: {name}
Company: {company_name}
Subdomain: {subdomain_name}
Email: {email}
Telephone: {telephone}

{comment}
"""


class InvalidDomain(Exception):

    def __init__(self, msg):
        self.msg = msg

    def doc(self):
        return self.msg


def validate_subdomain(value):
    value = value.strip()
    if not value:
        return True
    if '.' in value or ' ' in value or '\t' in value:
        raise InvalidDomain("The subdomain cannot contain dots or spaces.")
    if value.startswith('manage_'):
        raise InvalidDomain("The subdomain cannot start with manage_.")
    if not value[0].isalnum():
        raise InvalidDomain("The subdomain need to start with a letter or a digit.")
    if value in ('silva', 'test', 'silvacms', 'infrae'):
        raise InvalidDomain("This subdomain is reserved and cannot be used.")
    return True


class IContactFields(interface.Interface):
    """Describe a comment.
    """
    name = schema.TextLine(
        title=u"Your name",
        description=u"Valid contact informations are required and will " \
            "verified manually before the creation of your site. We reserve " \
            "ourself the right not to create or delete the created site in case " \
            "of invalid information or abuse.",
        required=True)
    company_name = schema.TextLine(
        title=u"Company",
        default=u'',
        required=False)
    email = RFC822MailAddress(
        title=u"Email",
        required=True)
    telephone = schema.TextLine(
        title=u"Telephone",
        default=u'',
        required=False)
    subdomain_name = schema.TextLine(
        title=u"Subdomain",
        description=u"The subdomain will used in front of cloud.silvacms.org " \
            "in order to create the domain name of your site.",
        default=u'',
        constraint=validate_subdomain,
        required=True,)
    comment = schema.Text(
        title=u"Comment",
        required=False)


class CloudForm(silvaforms.PublicForm):
    """Cloud form.
    """
    grok.name('cloud.html')
    grok.context(IContainer)

    label = _(u'Cloud instance')
    description = _(u"""You can request a cloud site using this form.
         The site will usually be setup in less than a business
         day. Once it is done you'll be sent a URL, e.g.:
         http://subdomain.cloud.silvacms.org, a user and password to
         access your site. Then you'll have your own Silva sandbox and
         you can give Silva an extensive test drive. There is no
         guarantee of service on this hosting.""")
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
        self.response.redirect(
            absoluteURL(self.context, self.request) + '/cloud-booked.html')
        return silvaforms.SUCCESS


class CloudBooked(silvaviews.Page):
    grok.name('cloud-booked.html')
    grok.context(IContainer)
