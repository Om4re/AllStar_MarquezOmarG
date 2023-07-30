from django.contrib import admin
from .models import Clases, Instructores, Entregable, Alumno

# Register your models here.
admin.site.register(Clases)
admin.site.register(Instructores)
admin.site.register(Entregable)
admin.site.register(Alumno)