from django.shortcuts import render, redirect
from .models import Estabelecimento, Mesa, Garcon, Menu, Comanda, ItemComanda, Pedido
from .forms import EstabelecimentoForm, MesaForm, GarconForm, MenuForm, ComandaForm

#views referente a Cadastro de Estabelecimento

def lista_estabelecimentos(request):
    estabelecimentos = Estabelecimento.objects.all()
    return render(request, 'lista_estabelecimentos.html', {'estabelecimentos': estabelecimentos})

def adiciona_estabelecimento(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estabelecimentos')
    else:
        form = EstabelecimentoForm()
    return render(request, 'adiciona_estabelecimento.html', {'form': form})

def edita_estabelecimento(request, id):
    estabelecimento = Estabelecimento.objects.get(id=id)
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect('lista_estabelecimentos')
    else:
        form = EstabelecimentoForm(instance=estabelecimento)
    return render(request, 'edita_estabelecimento.html', {'form': form})

def exclui_estabelecimento(request, id):
    estabelecimento = Estabelecimento.objects.get(id=id)
    estabelecimento.delete()
    return redirect('lista_estabelecimentos')

#views referente a Cadastro de Mesas

def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'lista_mesas.html', {'mesas': mesas})

def adiciona_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm()
    return render(request, 'adiciona_mesa.html', {'form': form})

def edita_mesa(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('lista_mesas')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'edita_mesa.html', {'form': form})

def exclui_mesa(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect('lista_mesas')

#views referente a Cadastro de Garçons

def lista_garcons(request):
    garcons = Garcon.objects.all()
    return render(request, 'lista_garcons.html', {'garcons': garcons})

def adiciona_garcon(request):
    if request.method == 'POST':
        form = GarconForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_garcons')
    else:
        form = GarconForm()
    return render(request, 'adiciona_garcon.html', {'form': form})

def edita_garcon(request, id):
    garcon = Garcon.objects.get(id=id)
    if request.method == 'POST':
        form = GarconForm(request.POST, instance=garcon)
        if form.is_valid():
            form.save()
            return redirect('lista_garcons')
    else:
        form = GarconForm(instance=garcon)
    return render(request, 'edita_garcon.html', {'form': form})

def exclui_garcon(request, id):
    garcon = Garcon.objects.get(id=id)
    garcon.delete()
    return redirect('lista_garcons')

#views referente a Cadastro de Menu

def lista_menus(request):
    menus = Menu.objects.all()
    return render(request, 'lista_menus.html', {'menus': menus})

def adiciona_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_menus')
    else:
        form = MenuForm()
    return render(request, 'adiciona_menu.html', {'form': form})

def edita_menu(request, id):
    menu = Menu.objects.get(id=id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('lista_menus')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'edita_menu.html', {'form': form})

def exclui_menu(request, id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    return redirect('lista_menus')

#calculo total das mesas

def calcula_total_mesa(request, mesa_id):
    comanda = Comanda.objects.filter(mesa=mesa_id).first()
    pedidos = Pedido.objects.filter(comanda=comanda)
    total = sum(pedido.valor_total for pedido in pedidos)
    return render(request, 'total_mesa.html', {'comanda': comanda, 'pedidos': pedidos, 'total': total})

#entrega de recibo

def entrega_recibo(request, mesa_id):
    comanda = Comanda.objects.filter(mesa=mesa_id).first()
    pedidos = Pedido.objects.filter(comanda=comanda)
    total = sum(pedido.valor_total for pedido in pedidos)
    return render(request, 'recibo.html', {'comanda': comanda, 'pedidos': pedidos, 'total': total})