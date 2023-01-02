from django import forms
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from robo_project.accounts.forms import SignUpForm, AddUserRobotForm
from robo_project.accounts.models import UserRobots

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profile details')
    #success_url = reverse_lazy('profile details')  # redirect to specific url

     # Logva user ako e uspeshno registriraneto
    #def post(self, request, *args, **kwargs):

    #    response = super().post(request, *args, **kwargs)
    #    login(request, self.object)
    #    return response

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.object.pk,
        })


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    # Showing results only for the current user. Prevent viewing other users by change of url.
    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        if not self.request.user == self.object:
            return reverse_lazy('index')
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['my_robots'] = UserRobots.objects.filter(user_id=self.object.pk).select_related().all()
        return context


class UserEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):

    template_name = 'accounts/profile_edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'city', 'address')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class ChangeUserPasswordView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'
    success_url = reverse_lazy('profile details')  # redirect to specific url

    def get_success_url(self):

        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class SignOutView(auth_views.LogoutView):
    success_url = reverse_lazy('sign in')


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile_delete.html'
    model = UserModel
    success_url = reverse_lazy('sign up')


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    paginate_by = 5
    ordering = ['pk']
    template_name = "accounts/users_list.html"

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.request
        context['my_robots'] = UserRobots.objects.all().order_by("user_id")
        #test = self.object_list
        #print(type(test))
        #for test_user in test:
        #    context['my_robots'].append(len(UserRobots.objects.filter(user_id=test_user.pk)))
        return context


class AddUserRobot(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'accounts/add_user_robot.html'
    form_class = AddUserRobotForm
    success_url = reverse_lazy('profile details')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class DeleteUserRobot(views.DeleteView):
    pass

# TODO Delete additional data in accounts/profile_details.html