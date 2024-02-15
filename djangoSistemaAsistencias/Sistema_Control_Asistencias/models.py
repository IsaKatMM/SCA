from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    email = models.EmailField()
    cedula = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True

class Profesor(Persona):
    pass

class Estudiante(Persona):
    pass

class Ciclo(models.Model):
    materia = models.CharField(max_length=50)
    numero_ciclo = models.IntegerField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.materia} - Ciclo {self.numero_ciclo}'


class Horario(models.Model):
    materia = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='horarios_materia')
    dia_semana = models.CharField(max_length=10)
    hora_laboral = models.TimeField()
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='horarios_ciclo')

    def __str__(self):
        return str(self.materia)

class ControlAsistencias(models.Model):
    estado = models.BooleanField()
    fecha = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    # Método para registrar
    def registrar(self):
        pass

