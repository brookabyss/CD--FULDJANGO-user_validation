from django.shortcuts import render, redirect
from .models import Users
# Create your views here.
def index(request):
    return render(request,'user_val/index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['user_name']
        if Users.objects.check_length(username):
            Users.objects.create(username=username)

            users=Users.objects.all()
            context={
                'username': username,
                'users':users
            }
            return render(request,'user_val/show.html', context)
        else:
            context={
                'error': 'Username is not valid!'
            }
            return render(request,'user_val/index.html', context)

    return redirect('/')
