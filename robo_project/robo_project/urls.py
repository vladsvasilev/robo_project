from django.contrib import admin
from django.urls import path, include
from robo_project.robot_factory.views import handle_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('robo_project.robot_factory.urls')),
    path('accounts/', include('robo_project.accounts.urls')),
    path('robots/', include('robo_project.robots.urls')),
]

handler404 = handle_not_found
