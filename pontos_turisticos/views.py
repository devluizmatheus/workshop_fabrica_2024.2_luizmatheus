from django.shortcuts import render

# Create your views here.
def inicialPage(request):
    return render(
        request,
        'inicial.html'
    )