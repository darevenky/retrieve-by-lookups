from django.shortcuts import render

# Create your views here.

from app.models import *

from django.db.models.functions import Length
from django.db.models import Q

def display_topics(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'display_topics.html',d)

def display_web(request):

    #lookup conditions

    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[0::2]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())


    d={'LWO':LWO}

    return render(request,'display_web.html',d)

def display_access(request):


    #lookup conditions


    LAO=Access.objects.all()
    LAO=Access.objects.filter(author__startswith='r')
    LAO=Access.objects.filter(author__endswith='l')
    LAO=Access.objects.filter(url__endswith='.com')
    LAO=Access.objects.filter(url__contains='.')
    LAO=Access.objects.filter(Q(name='Sunil Chetri') and Q(author='Sunil'))
    LAO=Access.objects.filter(author__regex='[a-zA-Z]{6}')




    d={'LAO':LAO}

    return render(request,'display_access.html',d)