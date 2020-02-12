from django.contrib import admin

from . models import Register, Doctor,Problem,News

# Register your models here.

admin.site.register(Register)
admin.site.register(Doctor)
admin.site.register(Problem)
admin.site.register(News)
