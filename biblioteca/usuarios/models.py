from django.db import models

#user: Connor
#email: crellan345@gmail.com
#senha: teste1234

class Usuario(models.Model):
    nome = models.CharField(max_length= 50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome
