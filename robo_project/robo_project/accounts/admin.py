from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.models import User

from robo_project.accounts.forms import UserEditForm, SignUpForm
from robo_project.accounts.models import UserRobots

"""
1234Qwer@
"""

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = SignUpForm
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('email',)
    search_fields = ("first_name", "last_name", "email")
    exclude = ('password1', 'password2',)
    readonly_fields = ('date_joined',)

    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password1',
                    'password2',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'city',
                    'address',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (

                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)


