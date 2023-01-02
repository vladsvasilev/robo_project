from django.urls import path, include

from robo_project.robot_factory.views import index, about, contact, faq, shop, MessagesListView, MessagesDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('messages/', include([
        path('', MessagesListView.as_view(), name='messages'),
        path('<int:pk>/delete/', MessagesDeleteView.as_view(), name='delete messages'),
    ])),
    #path('messages/', MessagesListView.as_view(), name='messages'),
    path('faq/', faq, name='faq'),
    #path('shop', shop, name='shop'),
]
