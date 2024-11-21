from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks=[]

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request,"task/index.html",{
        "tasks":tasks
    })
def add(request):
    if request.method == "POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            form.cleaned_data["tasks"]
            tasks.append(tasks)
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request,"task/add.html",{
                "form":form
            })
    return render(request,"task/add.html",{
        "form":NewTaskForm()
    })