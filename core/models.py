from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100, default="")  # Valor padrão para nome
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=100, default="")  # Valor padrão para especialidade

    def __str__(self):
        return f'{self.nome} - {self.crm}'

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome  # Exibir apenas o nome do paciente

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateField()  # Campo para a data
    hora = models.TimeField()  # Campo para a hora
    status = models.CharField(max_length=20, choices=[
        ('Agendada', 'Agendada'),
        ('Realizada', 'Realizada'),
        ('Faltou', 'Faltou'),
    ])

    def __str__(self):
        # Exibir o nome do paciente, a data e a hora da consulta
        return f'{self.paciente.nome} - {self.data.strftime("%d/%m/%Y")} às {self.hora.strftime("%H:%M")}'
