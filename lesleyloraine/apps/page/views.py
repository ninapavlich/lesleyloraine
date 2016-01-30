from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.utils.decorators import method_decorator

from carbon.compounds.form.views import CreateFormEntryMixin
from carbon.compounds.page.views import PageDetail as BasePageDetail
from carbon.compounds.page.views import PageBlockView as BasePageBlockView

from carbon.compounds.form.views import signal_form_error, signal_form_entry_created

from .models import Page
from lesleyloraine.apps.form.forms import FormEntryForm
from lesleyloraine.apps.form.models import Form, FormEntry


class PageDetail(BasePageBlockView, CreateFormEntryMixin, BasePageDetail):

    model = Page
    form_class = FormEntryForm

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(PageDetail, self).dispatch(*args, **kwargs)

    def get_form_schema(self):
        if not self.object:
            self.object = self.get_object()
        if self.object:
            return self.object.form
        return None


    def get_success_url(self):
        return self.object.get_absolute_url()


@receiver(signal_form_error, sender=Form)
def on_form_error(sender, **kwargs):
    form = kwargs['form_schema']
    #pass...

@receiver(signal_form_entry_created, sender=FormEntry)
def on_form_created(sender, **kwargs):
    form_entry = kwargs['form_entry']
    #pass...  