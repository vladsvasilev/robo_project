from django import forms

from robo_project.robot_factory.models import AppMassages
from robo_project.robots.mixins.form_mixins import DisabledFormMixin


class AppMessagesForm(forms.ModelForm):
    class Meta:
        model = AppMassages
        fields = ['first_name', 'last_name', 'email', 'message']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'message': 'Message',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'message': forms.TextInput(
                attrs={
                    'placeholder': 'Message',
                }
            ),
        }


class DeleteMessagesForm(DisabledFormMixin, AppMessagesForm):
    disabled_fields = ('first_name', 'last_name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
