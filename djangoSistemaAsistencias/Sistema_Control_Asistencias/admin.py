from django.contrib import admin
from .models import Estudiante, Profesor, Ciclo, Horario, ControlAsistencias

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Ciclo)
admin.site.register(Horario)
admin.site.register(ControlAsistencias)

