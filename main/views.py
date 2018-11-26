from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={},
    )


#from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import MyUserCreate as UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request,user)
            return redirect('/main/')
    else:
        form = UserCreationForm()
    return render(request, 'main/user_form.html', {'form': form})