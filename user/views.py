from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login as user_login, logout as user_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.forms import ChangePasswordForm, LoginForm, ProfileUpdateForm, ResetPasswordForm, SignupForm
from user.emails import send_email_verification
from user.utils import EmailVerificationTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

User = get_user_model()


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('index'))
        messages.error(request, 'Please enter valid data')
        return render(request, 'user/signup.html', {'form': form})
    context = {
        'form': SignupForm()
    }
    return render(request, 'user/signup.html', context)


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                user_login(request, user)
                messages.success(request, 'Login successful')
                return HttpResponseRedirect(reverse('index'))
            messages.error(request, 'Please enter valid credentials')
            return render(request, 'user/login.html', {'form': form})
        messages.error(request, 'Please enter valid credentials')
        return render(request, 'user/login.html', {'form': form})
    context = {
        'form': LoginForm()
    }
    return render(request, 'user/login.html', context)


@login_required
def Logout(request):
    if request.user.is_authenticated:
        user_logout(request)
        messages.info(request, 'Logout successful')
    else:
        messages.warning(request, 'You are not logged in')

    return HttpResponseRedirect(reverse('user:login'))


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
            return HttpResponseRedirect(reverse('index'))
        messages.error(request, 'Please enter valid data')
        return render(request, 'user/change_password.html', {'form': form})
    context = {
        'form': ChangePasswordForm(request.user)
    }   
    return render(request, 'user/change-password.html', context)


@login_required
def Profile_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'user/profile-view.html', context)


@login_required
def Profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(reverse('user:profile-view'))
        messages.error(request, 'Please enter valid data')
        return render(request, 'user/profile-update.html', {'form': form})
    context = {
        'form': ProfileUpdateForm(instance=request.user)
    }
    return render(request, 'user/profile-update.html', context)


@login_required
def email_verification_request(request):
    if not request.user.is_email_verified:
        send_email_verification(request, request.user.pk)
        return HttpResponse('Email verification link sent to your email')
    return HttpResponseForbidden('Email already verified')


@login_required
def email_verifier(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    if user == request.user:
        if EmailVerificationTokenGenerator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            messages.success(request, 'Email verified successfully')
            return HttpResponseRedirect(reverse('user:profile-view'))
        return HttpResponseBadRequest('Invalid request')
    return HttpResponseForbidden('You dont have permission to access this link')


def ResetPassword(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            
            if new_password1 != new_password2:
                messages.error(request, 'The passwords do not match.')
                return render(request, 'user/reset-password.html', {'form': form})
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "No user found with this email address.")
                return HttpResponseRedirect(reverse('user:reset-password'))

            user.set_password(new_password1)
            user.save()

            update_session_auth_hash(request, user)

            messages.success(request, 'Password reset successfully')
            return HttpResponseRedirect(reverse('user:login'))

        else:
            messages.error(request, 'Please enter valid data')
            return render(request, 'user/reset-password.html', {'form': form})

    else:
        form = ResetPasswordForm()

    return render(request, 'user/reset-password.html', {'form': form})