from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def posts_create(reqeust):
    return HttpResponse("<h1>Create</h1>")
def posts_detail(reqeust):
    return HttpResponse("<h1>detail</h1>")
def posts_list(reqeust):
    return render(reqeust,"index.html",{})
def posts_update(reqeust):
    return HttpResponse("<h1>update</h1>")
def posts_delete(reqeust):
    return HttpResponse("<h1>delete</h1>")

