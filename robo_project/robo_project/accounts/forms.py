from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from robo_project.accounts.models import UserRobots
from robo_project.robots.mixins.form_mixins import DisabledFormMixin

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'first_name', 'last_name', 'city', 'address')




class SignUpForm(auth_forms.UserCreationForm):

    # Remove help_text from sign-up form on password fields
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in [UserModel.USERNAME_FIELD, 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'city', 'address',)
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'label': "Email",
                    'class': 'form-control',
                    'placeholder': 'Enter email',

                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'label': "Password",
                    'class': 'form-control',
                    'placeholder': 'Enter password',

                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'label': "Password",
                    'class': 'form-control',
                    'placeholder': 'Confirm password',
                }
            ),
            'first_name': forms.TextInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),

            'city': forms.DateInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Enter City',
                }
            ),
            'address': forms.DateInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Enter Address',
                }
            )
         }


class AddUserRobotForm(forms.ModelForm):
    class Meta:
        model = UserRobots
        fields = ('user', 'robot_name', 'user_robots_quantity',)
        exclude = ('last_login',)



class DeleteUserRobotForm(DisabledFormMixin, AddUserRobotForm):
    disabled_fields = ('user_robots_quantity', 'user', 'robot_name')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
