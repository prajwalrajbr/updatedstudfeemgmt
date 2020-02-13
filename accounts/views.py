from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from entry.models import Faculty
from .forms import LoginForm
# Create your views here.
def login_view(request):
    msg=None
    if request.method == 'POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            faculty=Faculty.objects.get(Username=user)
            if faculty.Working_Status==True:
                if faculty.Dept=='Office':
                    login(request,user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('details:list')
                else:
                    msg="Access Denied!!!"
                    return render(request,'accounts/login.html',{'form':form,'msg':msg})
            else:
                msg="Access Denied!!!"
                return render(request,'accounts/login.html',{'form':form,'msg':msg})
    else:
        form=LoginForm()
        msg=None
    return render(request,'accounts/login.html',{'form':form,'msg':msg})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')