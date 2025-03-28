from django.shortcuts import render
from .forms import PeselForm

def verify_pesel_view(request):
    context = {
        "form": PeselForm()
    }
    return render(request, "verification.html", context)