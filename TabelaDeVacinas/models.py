from django.db import models

class UBS(models.Model):
    nome_ubs = models.CharField(max_length=22)

    def __str__(self):
        return self.nome_ubs

class Vacinas(models.Model):
    nome_vacina = models.CharField(max_length=60)

    def __str__(self):
        return self.nome_vacina

class UBSVacinas(models.Model):
    DISPONIBILIDADE_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Não Disponível', 'Não Disponível'),
    ]
    ubs = models.ForeignKey(UBS, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacinas, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=DISPONIBILIDADE_CHOICES, default='Não Disponível')

    def __str__(self):
        return f"{self.ubs} - {self.vacina} - {self.status}"

class Tabela_Disponibilidade(models.Model):
    DISPONIBILIDADE_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Não Disponível', 'Não Disponível'),
    ]
    ubs = models.ForeignKey(UBS, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacinas, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=DISPONIBILIDADE_CHOICES, default='Não Disponível')

    def __str__(self):
        return f"{self.ubs} - {self.vacina} - {self.status}" 

class Tabela_Funcionamento(models.Model):
    ubs = models.ForeignKey(UBS, on_delete=models.CASCADE)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    def __str__(self):
        return f"{self.ubs} - {self.horario_abertura} às {self.horario_fechamento}"
