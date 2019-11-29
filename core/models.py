from django.db import models

# Create your models here.
class Pesquisa(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=2)
    telefone = models.CharField(max_length=13)
    responsavel = models.CharField(max_length=150)
    pesquisador = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nome

class Tele(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=2)
    telefone = models.CharField(max_length=13)
    responsavel = models.CharField(max_length=150)
    pesquisador = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    nome_do_telemarketing = models.CharField(max_length=150)
    parentesco = models.CharField(max_length=50)
    escola = models.CharField(max_length=200)
    turno = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    Endereco = models.CharField(max_length=300)
    CEP = models.CharField(max_length=8)
    Cidade = models.CharField(max_length=60)
    ESTADO = (

        ('AC', 'Acre'),

        ('AL', 'Alagoas'),

        ('AP', 'Amapá'),

        ('AM', 'Amazonas'),

        ('BA', 'Bahia'),

        ('CE', 'Ceará'),

        ('DF', 'Distrito Federal'),

        ('ES', 'Espírito Santo'),

        ('GO', 'Goiás'),

        ('MA', 'Maranhão'),

        ('MT', 'Mato Grosso'),

        ('MS', 'Mato Grosso do Sul'),

        ('MG', 'Minas Gerais'),

        ('PA', 'Pará'),

        ('PB', 'Paraíba'),

        ('PR', 'Paraná'),

        ('PE', 'Pernambuco'),

        ('PI', 'Piauí'),

        ('RJ', 'Rio de Janeiro'),

        ('RS', 'Rio Grande do Sul'),

        ('RO', 'Rondônia'),

        ('RR', 'Roraima'),

        ('SC', 'Santa Catarina'),

        ('SP', 'São Paulo'),

        ('SE', 'Sergipe'),

        ('TO', 'Tocantins'),

    )

    Estado = models.CharField(max_length=60, choices=ESTADO)

    codigo_telemarketing = models.CharField(max_length=30)
    data_agendamento = models.DateField(auto_now=True)

    observacoes = models.TextField()

    STATUS_CHOICES = [
        ['A', 'Atendeu'],
        ['N', 'Não Atendeu'],
        ['C', 'Caixa de Mensagens']
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome

