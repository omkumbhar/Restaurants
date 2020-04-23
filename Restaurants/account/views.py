from django.shortcuts import render ,redirect
from django.contrib.auth import  login, authenticate ,logout
from .forms import AccountRegistrationForm , LoginForm

def accountRegistarationView(request):
    context = {}
    if request.POST:
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-home')
        else:
            context['form'] = form
    else:
        form = AccountRegistrationForm()
    context['register_form'] = form
    return  render(request, 'account/accountRegister.html', context)


def logoutUser(request):
    logout(request)
    return redirect('restaurant-home')


def loginForm(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email       = form.cleaned_data.get("email")
            password    = form.cleaned_data.get("password")
            user = authenticate(request, email = email,password = password)
            if user is not None:
                login(request,user)
                if user.is_admin :
                    return redirect('manager-home')
                else:
                    return redirect('restaurant-home')
            else:
                form = LoginForm()
                context['error_message'] = "Login Failed! Enter the username and password correctly"
                context['login_form'] = form
                return render(request, 'account/accountLogin.html',  context)
                print("Error ssss")
    else:
        form = LoginForm()
        context['login_form'] = form
    return render(request, 'account/accountLogin.html', context)



