from django.db import models

class UBS(models.Model):
    nome_ubs = models.CharField(max_length=22)

    def __str__(self):
        return self.nome_ubs


class Vacina(models.Model):  # Alterado de "Vacinas" para "Vacina" para manter a convenção de singular
    nome_vacina = models.CharField(max_length=60)

    def __str__(self):
        return self.nome_vacina


class UBSVacina(models.Model):  # Alterado para singular e mantida a lógica de relacionamento
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Não Disponível', 'Não Disponível'),
    ]

    ubs = models.ForeignKey(UBS, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='Não Disponível',
    )
    
    class Meta:
        db_table = 'ubsvacina'  # Nome da tabela em letras minúsculas

    def __str__(self):
        return f"{self.ubs} - {self.vacina} ({self.status})"


class TabelaFuncionamento(models.Model):  # Alterado para remover sublinhados e padronizar
    ubs = models.ForeignKey(UBS, on_delete=models.CASCADE)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    def __str__(self):
        return f"{self.ubs} - {self.horario_abertura} às {self.horario_fechamento}"
