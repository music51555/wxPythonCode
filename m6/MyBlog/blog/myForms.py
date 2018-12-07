from django import forms
from django.forms import widgets


class UserForm(forms.Form):
    username=forms.CharField(
        min_length=4,
        label='用户名',
        widget=widgets.TextInput(attrs={'class':'form-control'})
    )
    password=forms.CharField(
        min_length=6,
        label='密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )
    r_password=forms.CharField(
        min_length=6,
        label='确认密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )
    email=forms.EmailField(
        label='邮箱',
        widget=widgets.EmailInput(attrs={'class':'form-control'})
    )
