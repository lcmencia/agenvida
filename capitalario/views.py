from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from .models import Purpose
from .forms import PurposeForm
from django.contrib import messages
# Create your views here.


class PurposeContributeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get("id")
        print(id)
        obj = get_object_or_404(Purpose, id=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.contributions.all():
                obj.contributions.remove(user)
            else:
                obj.contributions.add(user)
        return url_


def authentication(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            action = request.POST.get('action', None)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            if action == 'signup':
                user = User.objects.create_user(username=username, password=password)
                user.save()
            elif action == 'login':
                user = authenticate(username=username, password=password)
                login(request, user)
            return redirect('/')
        return render(request, 'login.html', {})


@login_required()
def purpose_list(request):
    queryset = Purpose.objects.all().order_by('-creado')
    context = {
        "object_list": queryset,
        "title": "My user List" 
    }
    return render(request,"list.html", context)
    

@login_required()
def purpose_detail(request, id):
    instance = get_object_or_404(Purpose, id=id)
    context = {
        "instance": instance,
    }
    return render(request,"detail.html", context)


@login_required()
def purpose_add(request):
    form = PurposeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
        context = {
        "form": form,
        }
        return render(request,"add.html", context)
   

@login_required()
def purpose_edit(request, id=None):
    instance = get_object_or_404(Purpose, id=id)
    form = PurposeForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved", extra_tags='edit-success')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.nombre,
        "instance": instance,
        "form": form,
    }
    return render(request,"add.html", context)
    

@login_required()
def purpose_delete(request, id=None):
    instance = get_object_or_404(Purpose, id=id)
    instance.delete()
    messages.success(request, "Deleted", extra_tags='delete-success')
    return redirect("list")
    
