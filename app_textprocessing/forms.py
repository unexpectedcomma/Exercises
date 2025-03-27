from django import forms
from django.core.exceptions import ValidationError

def validate_txt_file(value):
    if not value.name.endswith('.txt'):
        raise ValidationError('Only .txt files are allowed.')


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file', validators=[validate_txt_file])