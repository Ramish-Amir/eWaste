from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .forms import LoginForm, RegisterForm


# Create your views here.
def homepage(request):
    return render(request, 'Homepage.html', {})


def dashboard(request):
    return render(request, 'Dashboard.html', {})


def log_ride(request):
    return render(request, 'RideLogPage.html', {})


def profile(request):
    render(request, '', {})


def register(request):
    print(request)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'login.html', {'form': form})


def login(request):
    return auth_views.LoginView.as_view(template_name='Login.html', redirect_authenticated=True)(request)


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'Login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return redirect('homepage')
        return render(request, self.template_name, {'form': form})
