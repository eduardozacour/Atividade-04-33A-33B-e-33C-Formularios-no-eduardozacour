from django.db import models


# Create your models here.
class Distros(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    launch_date = models.DateField()


class Machines(models.Model):
    name = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    launch_date = models.DateField()
    available = models.CharField(max_length=50)


class Features(models.Model):
    STATUS = [
        ("WIP",
         "O desenvolvimento da funcionalidade está em progresso ativo, mas ainda não está pronto para testes mais amplos, uso ou distribuição"
         ),
        ("linux-asahi",
         "a funcionalidade é (relativamente) estável e disponível para uso no linux-asahi"
         ),
        ("TBA",
         "Não está sendo realizado trabalho ativo nesta funcionalidade no momento"
         )
    ]

    VERSIONS = [("v1", "1.0"), ("v2", "2.0"), ("v3", "3.0")]

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    version = models.CharField(max_length=50, choices=VERSIONS)

    launch_date = models.DateField()
