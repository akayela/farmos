from django.shortcuts import render

# Create your views here.

def register_view(request):
    return render(request, 'userauths/sign-up.html')
