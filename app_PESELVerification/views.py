from django.shortcuts import render
from .forms import PeselForm
from datetime import datetime

def verify_pesel_view(request):
    if request.method == 'POST':
        form = PeselForm(request.POST)
        validity = 'is-invalid'
        if form.is_valid():
            validity = 'is-valid'
            pesel = form.cleaned_data['peselField']
            sex = form.cleaned_data['sexField']
            dateOfBirth = form.cleaned_data['dateOfBirth']
            print("valid", pesel, sex, dateOfBirth)
            dateOfBirth = dateOfBirth.strftime('%Y-%m-%d')
        else:
            pesel = request.POST['peselField']
            sex = request.POST['sexField']
            dateOfBirth = request.POST['dateOfBirth']
        context = {
            'form': form,
            'validity': validity,
            'pesel': pesel,
            'sex': sex,
            'dateOfBirth': dateOfBirth
        }
        return render(request, "verification.html", context)


    context = {
        "form": PeselForm()
    }
    return render(request, "verification.html", context)