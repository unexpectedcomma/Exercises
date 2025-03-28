from django import forms


class PeselForm(forms.Form):
    peselField = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please input your PESEL'}),
        label='PESEL'
    )
    sexField = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Sex')