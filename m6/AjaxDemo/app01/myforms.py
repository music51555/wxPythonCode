from django import forms
from django.forms import widgets
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from app01.models import *

class UserForm(forms.Form):
    username=forms.CharField(
        label='用户名',
        widget=widgets.TextInput(),
    )
    password=forms.CharField(
        label='密码',
        widget=widgets.PasswordInput()
    )
    r_password=forms.CharField(
        label='确认密码',
        widget=widgets.PasswordInput()
    )