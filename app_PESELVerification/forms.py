from django import forms


class PeselForm(forms.Form):
    peselField = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please input your PESEL'}),
        label='PESEL'
    )
    sexField = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Sex')

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

        return cleaned_data

    def get_sex_from_pesel(self, pesel):
        if int(pesel[9]) % 2 == 0:
            return 'F'
        else:
            return 'M'