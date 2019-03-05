from django import forms
from django.forms import widgets

class UserForms(forms.Form):
    username = forms.CharField(
        min_length=4, label='用户名', widget = widgets.TextInput(attrs = {'class':'form-control'})
    )
    password = forms.CharField(
        min_length=4, label='密码', widget = widgets.PasswordInput(attrs = {'class':'form-control'})
    )
    email = forms.EmailField(
        error_messages={'invalid': '邮箱格式错误'},
        widget = widgets.EmailInput(attrs = {'class':'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
