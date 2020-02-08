from django.shortcuts import render,redirect
from  django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#注销
def logout_view(request):
    '''注销用户'''
    logout(request)
    return  redirect(reverse('blog:index'))
#注册页面
def register(request):
    '''注册新用户'''
    if request.method !='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return redirect(reverse('blog:index'))
    context={'form':form}
    return render(request,'users/register.html',context)