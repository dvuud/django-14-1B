from django.contrib import admin
from django.contrib.auth.models import User, Group
from apps.secondary.models import InfoUser
from apps.secondary.models import Resume
from apps.secondary.models import Experience
from apps.secondary.models import Blogs

# Register your models here.
admin.site.register(Experience)
admin.site.register(InfoUser)
admin.site.register(Resume)
admin.site.register(Blogs)
admin.site.unregister(User)
admin.site.unregister(Group)


