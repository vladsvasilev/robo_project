
from django.urls import path, include

from robo_project.accounts.views import SignUpView, SignInView, SignOutView, UserEditView, ProfileDetailsView, \
    ProfileDeleteView, UsersListView, DeleteUserRobot, AddUserRobot

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('', UsersListView.as_view(), name='users list'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', UserEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
        path('urobots/', include([
            path('', AddUserRobot.as_view(), name='add user robots'),
            path('add/', AddUserRobot.as_view(), name='add user robot'),
            path('delete/<int:pk>/', DeleteUserRobot.as_view(), name='delete user robot'),
        ])),
    ])),
]
