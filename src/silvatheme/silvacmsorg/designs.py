
from five import grok

from silva.app.page.interfaces import IPage
from silva.core.contentlayout import Design, Slot
from silva.fanstatic import need
from silva.core import conf as silvaconf

from .interfaces import ISilvaCmsOrg, IAboutResources


grok.templatedir('templates_silvacmsorg')
silvaconf.layer(ISilvaCmsOrg)


class Home(Design):
   grok.name('home')
   grok.title('Home')
   grok.context(IPage)

   slots = {
       'homecontent': Slot(css_class='about-content'),
       'screenshots': Slot(css_class='screenshots'),
       'boxfirst': Slot(css_class='box'),
       'boxsecond': Slot(css_class='box'),
       'boxthird': Slot(css_class='box')}

   def update(self):
       self.title = self.content.get_title_or_id()
       need(IAboutResources)


class About(Design):
   grok.name('about')
   grok.title('About')
   grok.context(IPage)

   slots = {
       'aboutcontent': Slot(css_class='about-content'),
       'featurescontent': Slot(css_class='features-content'),
       'involvedcontent': Slot(css_class='involved-content'),
       'democontent': Slot(css_class='demo-content'),
       'news': Slot(css_class='silva-news')}

   def update(self):
       self.title = self.content.get_title_or_id()
       need(IAboutResources)


class Support(Design):
   grok.name('support')
   grok.title('Support')
   grok.context(IPage)

   slots = {
       'supportcontent': Slot(css_class='support-content'),
       'introshort': Slot(css_class=''),
       'introsupport': Slot(css_class='support-intro'),
       'boxfirst': Slot(css_class=''),
       'boxsecond': Slot(css_class=''),
       'boxthird': Slot(css_class='')}

   def update(self):
       self.title = self.content.get_title_or_id()


class Documentation(Design):
   grok.name('documentation')
   grok.title('Documentation')
   grok.context(IPage)

   slots = {
       'one': Slot(css_class='slot-one'),
       'two': Slot(css_class='slot-two'),
       'three': Slot(css_class='slot-three'),
       'four': Slot(css_class='slot-four'),
       'five': Slot(css_class='slot-five'),
       'six': Slot(css_class='slot-six')}

   def update(self):
       self.title = self.content.get_title_or_id()


class Download(Design):
   grok.name('download')
   grok.title('Download')
   grok.context(IPage)

   slots = {
       'downloadcontent': Slot(css_class='download-content'),
       'boxfirst': Slot(css_class=''),
       'boxsecond': Slot(css_class=''),
       'boxthird': Slot(css_class=''),
       'releasescontent': Slot(css_class='')}

   def update(self):
       self.title = self.content.get_title_or_id()
