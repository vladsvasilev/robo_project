from django.contrib.auth import views as auth_views, authenticate, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from robo_project.robot_factory.forms import AppMessagesForm
from robo_project.robot_factory.models import AppMassages
from robo_project.robots.models import RobotTypes, AppRobots

UserModel = get_user_model()


def index(request):
    robot_types = RobotTypes.objects.all()

    context = {
        'robot_types': robot_types,
        'home_intro': True,
    }
    return render(
        request,
        'common/index.html',
        context
    )


def about(request):
    return render(
        request,
        'common/about.html',
    )


def contact(request):
    if request.method == 'GET':
        form = AppMessagesForm()
    else:
        form = AppMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(
        request,
        'common/contact.html',
        context,
    )


def faq(request):
    return render(
        request,
        'common/faq.html'
    )


class ShopListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = AppRobots
    paginate_by = 4
    ordering = ['pk']
    template_name = "common/shop.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

@login_required
def shop(request):
    robots = AppRobots.objects.all().order_by('pk')
    context = {
        'robots': robots
    }
    return render(
        request,
        'common/shop.html',
        context,
    )


class MessagesListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = AppMassages
    paginate_by = 5
    ordering = ['pk']
    template_name = "common/contact_messages.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class MessagesDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'common/message_delete.html'
    model = AppMassages
    success_url = reverse_lazy('messages')


def handle_not_found(request, exception):
    return render(request, 'common/page_not_found_404.html')