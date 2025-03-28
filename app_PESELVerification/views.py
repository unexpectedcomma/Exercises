from django.shortcuts import render
from .forms import PeselForm

def verify_pesel_view(request):
    if request.method == 'POST':
        form = PeselForm(request.POST)
        validity = 'is-invalid'
        if form.is_valid():
            validity = 'is-valid'
            pesel = form.cleaned_data['peselField']
            sex = form.cleaned_data['sexField']
        else:
            pesel = request.POST['peselField']
            sex = request.POST['sexField']
            print(pesel, sex)
        context = {
            'form': form,
            'validity': validity,
            'pesel': pesel,
            'sex': sex,
        }
        return render(request, "verification.html", context)


    context = {
        "form": PeselForm()
    }
    return render(request, "verification.html", context)