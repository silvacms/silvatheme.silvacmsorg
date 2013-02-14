
from five import grok
from zope import interface, schema
from z3c.schema.email import RFC822MailAddress
from zeam.form import silva as silvaforms
from silva.core.interfaces import IContainer
from Products.Silva.mail import sendmail
from silva.translations import translate as _
from zope.traversing.browser import absoluteURL

TEMPLATE="""
You have a new contact request!

From: {name}
Company: {company_name}
Email: {email}
Telephone: {telephone}

{comment}
"""


class IContactFields(interface.Interface):
    """Describe a comment.
    """
    name = schema.TextLine(title=u"Your name", required=True)
    company_name = schema.TextLine(title=u"Company", required=False, default=u'')
    email = RFC822MailAddress(title=u"Email", required=True)
    telephone = schema.TextLine(title=u"Telephone", required=False, default=u'')
    comment = schema.Text(title=u"Comment", required=True)


class ContactForm(silvaforms.PublicForm):
     """Contact form.
     """
     grok.name('contact.html')
     grok.context(IContainer)

     label = _(u'Contact')
     description = _(u'You can contact us using this form')
     fields = silvaforms.Fields(IContactFields)

     @silvaforms.action(_(u"Contact us!"), identifier='contact', accesskey='c')
     def contact(self):
         data, errors = self.extractData()
         if errors:
             self.status = _(u'Please correct the errors.')
             return silvaforms.FAILURE
         sendmail(self.context, TEMPLATE.format(**data.getDictWithDefault()),
                  mto='info@infrae.com', mfrom='info@infrae.com',
                  subject='Contact request from silvacms.org')
         success = self.context.get_root()._getOb('success', None)
         if success is not None:
             self.response.redirect(absoluteURL(success, self.request))
         else:
             self.status = _(u'Thank you for your request.')
         return silvaforms.SUCCESS
