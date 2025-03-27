from django.shortcuts import render
from .forms import DocumentForm
import random

def upload_text_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["docfile"]
            content = file.read().decode("utf-8")
            result = scramble(content)
            context = {
                "result": result,
            }
            return render(request, "processingresult.html", context)
        else:
            context = {
                "form": form
            }
            return render(request, "textprocessing.html", context)
    context = {
        "form": DocumentForm()
    }
    return render(request, "textprocessing.html", context)

def scramble(content):
    words = content.split()
    scrambled_words = []
    for word in words:
        if not len(word) <= 3:
            first, middle, last = word[0], list(word[1:-1]), word[-1]
            random.shuffle(middle)
            scrambled_word = first + "".join(middle) + last  # Reconstruct word
        else:
            scrambled_word = word  # Keep short words unchanged

        scrambled_words.append(scrambled_word)  # Store the modified word

    return " ".join(scrambled_words)  # Reconstruct sentence


