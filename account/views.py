from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            if not user_form.username and user_form.email in User.objects.all():
            # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
            # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
                new_user.save()
                return render(request, 'account/register_done.html', {'new_user': new_user})
            else:
                user_form = UserRegistrationForm()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
