from django.shortcuts import render, HttpResponse
from users.fomrs import UserForm



# Create your views here.
def login(request):
    return render(
        request,
        'form.html',
        {
            'title': 'Login 🖐',        
            'form': UserForm()
        }
    )

def signup(rquest):
    pass