from django.contrib import admin
from .models import Machines, Features, Distros
# Register your models here.

admin.site.register(Machines)
admin.site.register(Features)
admin.site.register(Distros)