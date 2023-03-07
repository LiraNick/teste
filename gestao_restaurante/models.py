from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

class Mesa(models.Model):
    numero = models.IntegerField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Garcon(models.Model):
    nome = models.CharField(max_length=100)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    garcon = models.ForeignKey(Garcon, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    encerrada = models.BooleanField(default=False)

class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

class Menu(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='pedidos')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='pedidos')
    quantidade = models.IntegerField(default=1)

    def total(self):
        return self.menu.preco * self.quantidade