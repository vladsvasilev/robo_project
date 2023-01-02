from django import forms


from robo_project.robots.mixins.form_mixins import DisabledFormMixin
from robo_project.robots.models import AppRobots, Types, RobotTypes


# TODO add forms for RobotType and AppRobots

class RobotTypeForm(forms.ModelForm):
    class Meta:
        model = RobotTypes
        fields = ('name', 'description', 'image_url')
        labels = {
            'name': 'Select type',
            'description': 'Add Description',
            'image_url': 'Link to image',
        }
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Robot Type'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Add Robot Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }


class RobotTypeCreateForm(RobotTypeForm):
    pass


class RobotTypeEditForm(DisabledFormMixin, RobotTypeForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class RobotTypeDeleteForm(DisabledFormMixin, RobotTypeForm):
    disabled_fields = ('name', 'description', 'image_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class RobotBaseForm(forms.ModelForm):
    class Meta:
        model = AppRobots
        fields = ('robot_name', 'description', 'available_quantity', 'image_url', 'type')
        labels = {
            'robot_name': 'Robot Name',
            'description': 'Add Description',
            'available_quantity': 'Add quantity',
            'image_url': 'Link to image',
            'type': 'Select type',
        }
        widgets = {
            'robot_name': forms.TextInput(
                attrs={
                    'placeholder': 'Robot Name'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Add Robot Description',
                }
            ),
            'available_quantity': forms.TextInput(
                attrs={
                    'placeholder': 'Add quantity',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Type',
                }
            ),
        }


class RobotCreateForm(RobotBaseForm):
    pass


class RobotEditForm(DisabledFormMixin, RobotBaseForm):
    disabled_fields = ('robot_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class RobotDeleteForm(DisabledFormMixin, RobotBaseForm):
    disabled_fields = ('name', 'description', 'available_quantity', 'image_url', 'type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
