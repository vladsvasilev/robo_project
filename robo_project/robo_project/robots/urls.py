
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from robo_project.robot_factory.views import shop, ShopListView
from robo_project.robots.views import add_robot_type, details_robot_types, edit_robot_type, \
    delete_robot_type, RobotsListView, RobotEditView, RobotDeleteView, RobotCreateView, RobotTypesListView

urlpatterns = [
    path('', ShopListView.as_view(), name='shop'),
    path('add_robot_type/', add_robot_type, name='add robot type'),
    path('typelist/', RobotTypesListView.as_view(), name='robot types list'),
    path('type/<int:pk>/', include([
         path('', details_robot_types, name='robot types details'),
         path('edit/', edit_robot_type, name='robot types edit'),
         path('delete/', delete_robot_type, name='robot types delete'),
    ])),
    path('add_robot/', RobotCreateView.as_view(), name='add robot'),
    path('list/', include([
        path('', RobotsListView.as_view(), name='robots list'),
        path('edit/<int:pk>/', RobotEditView.as_view(), name='edit robot'),
        path('delete/<int:pk>/', RobotDeleteView.as_view(), name='delete robot'),
    ])),
]
