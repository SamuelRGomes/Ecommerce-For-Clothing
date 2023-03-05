from django.db import models

class Categoria(models.Model):
    nome= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Categoria.objects.all()

    def __str__(self):
        return self.nome
