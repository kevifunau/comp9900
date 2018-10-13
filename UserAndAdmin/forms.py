from django import forms
from UserAndAdmin.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


'''

处理 HTML 接收到的 from 表单

所有的表单类都要继承forms.Form类

每个表单字段都有自己的字段类型 (比如CharField) 它们分别对应一种HTML语言中的<form>元素中的表单元素

每个Django表单的实例都有一个内置的is_valid()方法，用来验证接收的数据是否合法
如果所有数据都合法，那么该方法将返回True，并将所有的表单数据转存到它的一个叫做cleaned_data的属性中，该属性是以个字典类型数据。

'''

class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class RegisterForm(forms.Form):
    """
    注册一个新用户
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

class editprofileForm(forms.Form):
    '''
    更新一个人的信息
    '''
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    language = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    user_description = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))




class passwordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    new_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]