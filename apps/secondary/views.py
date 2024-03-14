from django.shortcuts import render
from apps.secondary.models import InfoUser
from apps.secondary.models import Resume
from apps.secondary.models import Experience
from apps.secondary.models import Blogs
from apps.secondary.models import Portfolio
# Create your views here.

def index(request):
    infouser = InfoUser.objects.latest("id")
    resume = Resume.objects.latest("id")
    experience = Experience.objects.latest("id")
    blogs = Blogs.objects.all()
    portfolio = Portfolio.objects.latest("id")
    return render(request, "index.html", locals())