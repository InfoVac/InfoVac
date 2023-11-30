from django.db import models

# Create your models here.

class Tabela_Disponibilidade(models.Model):
    UBS = (
        ('Anita Ferraz', 'Anita Ferraz'),
        ('Cacimba Velha', 'Cacimba Velha'),
        ('Campestre Norte', 'Campestre Norte'),
        ('Cidade Jardim', 'Cidade Jardim'),
        ('Coroatá', 'Coroatá'),
        ('Ininga', 'Ininga'),
        ('Parque Universitário', 'Parque Universitário'),
        ('Piçarreira', 'Piçarreira'),
        ('Planalto Uruguai', 'Planalto Uruguai'),
        ('Santa Bárbara', 'Santa Bárbara'),
        ('Santa Isabel', 'Santa Isabel'),
        ('Santa Luz', 'Santa luz'),
        ('Santa Teresa', 'Santa teresa'),
        ('São João', 'São João'),
        ('Satélite', 'Satélite'),
        ('Soinho', 'Soinho'),
        ('Taquari', 'Taquari'),
        ('Vale do Gavião', 'Vale do Gavião'),
        ('Vila Bandeirantes', 'Vila Bandeirantes'),
        ('Vila União', 'Vila união'),
    )
    VACINA = (
        ('Dupla Adulto (Difteria e Tétano)', 'Dupla Adulto (Difteria e Tétano)'),
        ('Febre Amarela', 'Febre Amarela'),
        ('Hepatite A', 'Hepatite A'),
        ('Hepatite B', 'Hepatite B'),
        ('Inativada Poliomielite', 'Inativada Poliomielite'),
        ('Meningocócica ACWY', 'Meningocócica ACWY'),
        ('Meninocócica C', 'Meninocócica C'),
        ('Oral Poliomielite', 'Oral Poliomielite'),
        ('Oral Rotavírus humano', 'Oral Rotavírus Humano'),
        ('Papiloma Vírus Humano Quadrivalente', 'Papiloma Vírus Humano Quadrivalente'),
        ('Pentavalente (DTP/HB/Hib)', 'Pentavalente (DTP/HB/Hib)'),
        ('Pneumocócica 10 Valente', 'Pneumocócica 10 Valente'),
        ('DTP - Tríplice Bacteriana(Difteria, Tétano, Coqueluche)', 'DTP - Tríplice Bacteriana(Difteria, Tétano, Coqueluche)'),
        ('SCR - Tríplice Viral(Sarampo, Caxumba e Rubéola)', 'SCR - Tríplice Viral(Sarampo, Caxumba e Rubéola)'),
        ('Varicela', 'Varicela'),
    )
    STATUS = (
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível'),
    )
    nome_ubs = models.CharField(
        max_length = 30,
        choices = UBS,
    )
    nome_vacina = models.CharField(
        max_length = 70,
        choices = VACINA,
    )
    disponibilidade = models.CharField(
        max_length =15,
        choices = STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['nome_ubs', 'nome_vacina']
    def __str__(self):
        return "{} da UBS {}".format(self.nome_vacina, self.nome_ubs)

class Tabela_Funcionamento(models.Model):
    UBS = (
        ('Anita Ferraz', 'Anita Ferraz'),
        ('Cacimba Velha', 'Cacimba Velha'),
        ('Campestre Norte', 'Campestre Norte'),
        ('Cidade Jardim', 'Cidade Jardim'),
        ('Coroatá', 'Coroatá'),
        ('Ininga', 'Ininga'),
        ('Parque Universitário', 'Parque Universitário'),
        ('Piçarreira', 'Piçarreira'),
        ('Planalto Uruguai', 'Planalto Uruguai'),
        ('Santa Bárbara', 'Santa Bárbara'),
        ('Santa Isabel', 'Santa Isabel'),
        ('Santa Luz', 'Santa luz'),
        ('Santa Teresa', 'Santa teresa'),
        ('São João', 'São João'),
        ('Satélite', 'Satélite'),
        ('Soinho', 'Soinho'),
        ('Taquari', 'Taquari'),
        ('Vale do Gavião', 'Vale do Gavião'),
        ('Vila Bandeirantes', 'Vila Bandeirantes'),
        ('Vila União', 'Vila união'),
    )
    
    nome_ubs = models.CharField(
        max_length = 30,
        choices = UBS,
    )
    horario = models.CharField(
        max_length = 70,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['nome_ubs']
    def __str__(self):
        return "Funcionamento da UBS do(a) {} é {}".format(self.nome_ubs, self.horario)