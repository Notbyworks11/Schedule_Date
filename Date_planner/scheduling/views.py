from django.shortcuts import render

# Create your views here.
def home (request):
    if request.POST:
        word = request.POST
        print(word)
    return render(request, "base.html")