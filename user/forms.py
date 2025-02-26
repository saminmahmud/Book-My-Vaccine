from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms import ModelForm
from django import forms

User = get_user_model()

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            'email', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'date_of_birth', 
            'gender', 
            'photo',
            'identity_document_type',
            'identity_document_number',
        ]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = "__all__"


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = "__all__"


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        required=True, 
        label='New Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        required=True, 
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'new_password1', 'new_password2']

class ProfileUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            'first_name', 
            'middle_name', 
            'last_name', 
            'date_of_birth', 
            'gender', 
            'photo',
            'identity_document_type',
            'identity_document_number',
        ]