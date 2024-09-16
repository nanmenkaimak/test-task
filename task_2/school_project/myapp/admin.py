from django.contrib import admin
from .models import User, Class, Subject, Grade

admin.site.register(User)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Grade)
