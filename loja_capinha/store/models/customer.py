from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField (max_length=50, null=True)
    telefone = models.CharField(max_length=25)
    email=models.EmailField()
    senha = models.CharField(max_length=100)
    
    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Cliente.objects.get(email= email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Cliente.objects.get(id= id)
        except:
            return False


    def isExists(self):
        if Cliente.objects.filter(email = self.email):
            return True

        return False