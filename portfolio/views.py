from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def projects(request):
    return render(request, 'projects.html', locals())

def resume(request):
    return render(request,'resume.html', locals())