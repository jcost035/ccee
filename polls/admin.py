from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Staff)
admin.site.register(Event)
admin.site.register(Program)
admin.site.register(News)