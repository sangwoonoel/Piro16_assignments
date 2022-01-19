from django.shortcuts import render,redirect, get_object_or_404
from .models import Idea, Devtool
from .form import IdeaForm, DevtoolForm
from django.http import JsonResponse
from . import models
import json

def plus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest += 1
    idea.save()
    context = {'plus_interest': idea.interest}
    return JsonResponse(context)


def minus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest -= 1
    idea.save()
    context = {'minus_interest': idea.interest}
    return JsonResponse(context)

def idea_list(request):
    ideas = Idea.objects.all()
    ctx = {'ideas': ideas}

    return render(request, template_name='idea_list.html', context=ctx)


def idea_detail(request, pk):
    ideas = Idea.objects.get(id=pk)
    
    # review.image = poster
    ctx = {'ideas' : ideas}

    return render(request, template_name='idea_detail.html', context= ctx)

# def idea_create(request):
#     if request.method == 'POST':
#         title = request.POST('title')
#         content = request.POST('content')
#         poster = request.FILES.get('poster')
#         image = poster
#         idea = models.idea(
#             title = title,
#             content = content,
#             image = image
#         )
#         idea.save()

#     ideas = models.idea.objects.all()

#     return render(request, template_name='form.html', context = {
#         "ideas": ideas
#     })

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("idea:idea_list")

            
    else:
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, template_name='form.html', context=ctx)
# def idea_create(request):
#     if request.method == 'POST':
#         form = IdeaForm(request.POST)
#         if form.is_valid():
#             poster = request.FILES.get('poster')
#             Idea.image = poster
#             review = form.save()
#             return redirect("idea:idea_list")

            
#     else:
#         form = IdeaForm()
#         ctx = {'form': form}
#         return render(request, template_name='form.html', context=ctx)

def idea_edit(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect('idea:idea_detail', pk)
    else:
        form = IdeaForm(instance=idea)
    ctx = {
        'form': form,
    }
    return render(request, template_name='form.html', context=ctx)


def idea_delete(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    idea.delete()
    return redirect("idea:idea_list")

def dev_list(request):
    devs = Devtool.objects.all()
    ctx = {'devs': devs}

    return render(request, template_name='dev_list.html', context=ctx)

def dev_detail(request, pk):
    devs = Devtool.objects.get(id=pk)
    # idea = Devtool.idea_set.objects.filter(devtool='')
    
    ideas = Idea.objects.filter(devtool=pk)
    
    ctx = {'devs' : devs, 'ideas': ideas}

    return render(request, template_name='dev_detail.html', context= ctx)

def dev_create(request):
    if request.method == "POST":
        form = DevtoolForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('idea:dev_list')
    else:
        form = DevtoolForm()
    ctx = {
        'form': form
    }
    return render(request, template_name='form.html', context=ctx)

def dev_edit(request, pk):
    dev = get_object_or_404(Devtool, id=pk)
    if request.method == "POST":
        form = DevtoolForm(request.POST, instance=dev)
        if form.is_valid():
            dev = form.save()
            return redirect('idea:dev_detail', pk)
    else:
        form = DevtoolForm(instance=dev)
    ctx = {
        'form': form,
    }
    return render(request, template_name='form.html', context=ctx)


def dev_delete(request, pk):
    dev = get_object_or_404(Devtool, id=pk)
    dev.delete()
    return redirect("idea:dev_list")
