from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.role == 'admin':
            return reverse_lazy('admin_dashboard')

        elif user.role == 'pelanggan':
            return reverse_lazy('pelanggan_dashboard')

        elif user.role == 'mekanik':
            return reverse_lazy('mekanik_dashboard')

        elif user.role == 'kasir':
            return reverse_lazy('kasir_dashboard')

        return reverse_lazy('login')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(request,
                  'accounts/edit_profile.html',
                  {
                      'form': form
                  })