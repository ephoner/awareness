from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
#    PrependedText, FormActions
# )
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginFrom(forms.Form):
    username = forms.CharField(label='用户名',)
    password = forms.CharField(widget=forms.PasswordInput, label='密码')

    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.form_method = 'POST'
    # helper.label_class = 'hidden'
    #
    # helper.layout = Layout(
    #
    #     PrependedText('username', '帐号'),
    #     PrependedText('password', '密码'),
    #     FormActions(Submit('login', '登陆', css_class='btn-primary btn-block btn-lg'))
    # )



    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("用户名不存在。")
            if not user.check_password(password):
                raise forms.ValidationError("用户密码错误。")
            if not user.is_active:
                raise forms.ValidationError("帐号已被禁用，请联系管理员。")
        return super(UserLoginFrom, self).clean(*args, **kwargs)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(max_length=120, label='用户名')
    email = forms.EmailField(label='邮箱')
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码 ', widget=forms.PasswordInput)

    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.form_method = 'POST'
    # helper.label_class = 'hidden'
    #
    # helper.layout = Layout(
    #     PrependedText('username', '帐号'),
    #     PrependedText('email', '邮箱'),
    #     PrependedText('password1', '密码'),
    #     PrependedText('password2', '确认密码'),
    #
    #     FormActions(Submit('login', '注册', css_class='btn-primary  btn-block btn-lg'))
    # )



    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致。")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user





