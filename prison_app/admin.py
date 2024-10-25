from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Login)
admin.site.register(PoliceReg)
admin.site.register(Prisoner)
admin.site.register(Remarks)
admin.site.register(Duty)
admin.site.register(Visitor)
admin.site.register(Parole)