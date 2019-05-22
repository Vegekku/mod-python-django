from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignUpForm


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return render_template_with_form(request, 'login', form)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
            else:
                login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        return render_template_with_form(request, 'login', form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('home')


class SignUpView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignUpForm()

        return render_template_with_form(request, 'signup', form)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

        return render_template_with_form(request, 'signup', form)


class ListView(View):

    def get(self, request):
        users = User.objects.filter(is_active=True).order_by('username')

        context = {'users': users}

        html = render(request, 'users/list.html', context)

        return HttpResponse(html)


def render_template_with_form(request, template, form):
    context = {'form': form}
    return render(request, 'users/{0}.html'.format(template), context)
