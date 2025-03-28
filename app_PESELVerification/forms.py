from django import forms
from datetime import datetime


class PeselForm(forms.Form):
    peselField = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please input your PESEL'}),
        label='PESEL'
    )
    sexField = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Sex', required=False)
    dateOfBirth = forms.DateField(required=False)

    def clean_peselField(self):
        pesel = self.cleaned_data.get('peselField')
        weights = '1379137913'

        if len(pesel) != 11:
            self.add_error('peselField', 'PESEL must be 11 digits long.')

        if not pesel.isnumeric():
            self.add_error('peselField', 'PESEL must only contain digits.')
        else:

            control_digit = 0
            for index, digit in enumerate(pesel[:-1]):
                control_digit += int(digit) * int(weights[index])
            if 10 - control_digit % 10  != int(pesel[10]):
                self.add_error('peselField', 'PESEL is not valid.')

        return pesel

    def clean(self):

        cleaned_data = super().clean()

        pesel = cleaned_data.get('peselField')
        if not self.errors and pesel:
            sex = self.get_sex_from_pesel(pesel)
            cleaned_data['sexField'] = sex
            cleaned_data['dateOfBirth'] = self.get_bday_from_pesel(pesel)

        return cleaned_data

    def get_sex_from_pesel(self, pesel):
        if int(pesel[9]) % 2 == 0:
            return 'F'
        else:
            return 'M'
    def get_bday_from_pesel(self, pesel):
        day = int(pesel[4:6])
        month = int(pesel[2:4])
        year = int(pesel[0:2])

        if 1 <= month <= 12:
            year += 1900
        elif 13 <= month <= 32:
            year += 2000
            month -= 20
        elif 40 <= month <= 42:
            year += 2100
            month -= 40
        elif 60 <= month <= 72:
            year += 2200
            month -= 60
        elif 80 <= month <= 92:
            year += 1800
            month -= 80

        return datetime(year, month, day).date()
