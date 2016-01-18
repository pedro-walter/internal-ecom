from django.contrib.auth.models import User
from django import forms

# from .models import Role, UserRole

class RegistrationForm(forms.ModelForm):
    """
    new user register
    """
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,
                                required=True,
                                label="Confirm password ")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'password1']

    def clean_password1(self):
        try:
            password1 = self.cleaned_data["password"]
            password2 = self.cleaned_data["password1"]
            if password1 == '' or password2 == '':
                raise forms.ValidationError("You must enter password")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return self.cleaned_data
        except:
            raise forms.ValidationError(
                ("Password doesn't match."))


# class UserRoleForm(forms.ModelForm):

#     class Meta:
#         model = UserRole
#         exclude = []

#     def __init__(self, *args, **kwargs):
#         super(UserRoleForm, self).__init__(*args, **kwargs)
#         self.fields["role"].widget = forms.CheckboxSelectMultiple(
#             attrs={'max-height': '100px'})
#         self.fields["role"].queryset = Role.objects.all()