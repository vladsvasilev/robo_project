from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, login
from robo_project.robots.forms import RobotCreateForm, RobotTypeForm, RobotTypeEditForm, RobotTypeCreateForm, \
    RobotTypeDeleteForm
from robo_project.robots.models import RobotTypes, AppRobots


@login_required
def add_robot_type(request):
    if request.method == "GET":
        form = RobotTypeCreateForm
    else:
        form = RobotTypeForm(request.POST)
        if form.is_valid():
            robot = form.save(commit=False)
            robot.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form
    }
    return render(
        request,
        'robots/add_robot_type.html',
        context
    )


@login_required
def details_robot_types(request, pk):
    robot_type = RobotTypes.objects.filter(pk=pk)\
        .get()
    context = {
        'robot_type': robot_type,
    }
    return render(
        request,
        'robots/details_robot_type.html',
        context,
    )

@login_required
def edit_robot_type(request, pk):
    robot_type = RobotTypes.objects \
        .filter(pk=pk) \
        .get()

    if request.method == "GET":
        form = RobotTypeEditForm(instance=robot_type)
    else:
        form = RobotTypeEditForm(request.POST, instance=robot_type)
        if form.is_valid():
            form.save()
            return redirect('robot types list')

    context = {
        'form': form,
        'robot_type': robot_type,
    }
    return render(
        request,
        'robots/edit_robot_type.html',
        context,
    )

@login_required
def delete_robot_type(request, pk):
    robot_type = RobotTypes.objects \
        .filter(pk=pk) \
        .get()

    if request.method == "GET":
        form = RobotTypeDeleteForm(instance=robot_type)
    else:
        form = RobotTypeDeleteForm(request.POST, instance=robot_type)
        if form.is_valid():
            form.save()
            return redirect('robot types list')

    context = {
        'form': form,
        'robot_type': robot_type,
    }
    return render(
        request,
        'robots/delete_robot_type.html',
        context,
    )

class RobotTypesListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = RobotTypes
    paginate_by = 5
    ordering = ['pk']
    template_name = "robots/robot_types_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


#@login_required
#def add_robot(request):
#    if request.method == "GET":
#        form = RobotCreateForm()
#    else:
#        form = RobotCreateForm(request.POST)
#        if form.is_valid():
#            robot = form.save(commit=False)
#            robot.save()
#            return redirect('robots list')

#    context = {
#        'form': form
#    }
#    return render(
#        request,
#        'robots/add_robot.html',
#        context
#    )


class RobotCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'robots/add_robot.html'
    form_class = RobotCreateForm
    success_url = reverse_lazy('robots list')


class RobotDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = AppRobots
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class RobotEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'robots/edit_robot.html'
    model = AppRobots
    fields = ('description', 'available_quantity', 'image_url', 'type')
    success_url = reverse_lazy('robots list')


class RobotDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'robots/delete_robot.html'
    model = AppRobots
    success_url = reverse_lazy('robots list')


class RobotsListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = AppRobots
    paginate_by = 5
    ordering = ['pk']
    template_name = "robots/robots_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context




