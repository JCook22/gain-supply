from django.utils.translation import gettext_lazy as _
from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    input_text = _('')
    initial_text = _('Current Image')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html')
