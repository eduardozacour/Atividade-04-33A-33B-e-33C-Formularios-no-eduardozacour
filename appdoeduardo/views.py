from django.shortcuts import render, redirect, get_object_or_404
from .models import Machines, Features, Distros
from .forms import DistrosForm, MachinesForm, FeaturesForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
@login_required
def home(request):
    machines = Machines.objects.all()
    features = Features.objects.all()
    distros = Distros.objects.all()

    if request.method == 'POST':
        form = DistrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DistrosForm()

    return render(
        request, 'home.html', {
            'form': form,
            "machines": machines,
            "features": features,
            "distros": distros
        })


@login_required
def create_machine(request):
    if request.method == 'POST':
        form = MachinesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MachinesForm()

    return render(request, 'machine.html', {
        'action': "Adicionar",
        'form': form
    })


@login_required
def update_machine(request, id):
    machine = Machines.objects.get(id=id)
    if request.method == 'POST':
        form = MachinesForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DistrosForm(instance=machine)

    return render(request, 'machine.html', {
        'action': "Atualizar",
        'form': form,
        "machine": machine
    })


@login_required
def create_feature(request):
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeaturesForm()

    return render(request, 'feature.html', {
        'action': "Adicionar",
        'form': form
    })


@login_required
def update_feature(request, id):
    feature = Features.objects.get(id=id)
    if request.method == 'POST':
        form = FeaturesForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeaturesForm(instance=feature)

    return render(request, 'feature.html', {
        'action': "Atualizar",
        'form': form,
        "feature": feature
    })


@login_required
def create_distro(request):
    if request.method == 'POST':
        form = DistrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DistrosForm()

    return render(request, 'distro.html', {
        'action': "Adicionar",
        'form': form
    })


@login_required
def update_distro(request, id):
    distro = Distros.objects.get(id=id)
    if request.method == 'POST':
        form = DistrosForm(request.POST, instance=distro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DistrosForm(instance=distro)

    return render(request, 'distro.html', {
        'action': "Atualizar",
        'form': form,
        "distro": distro
    })


@login_required
def delete_machine(request, id):
    machine = Machines.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            machine.delete()

        return redirect("home")
    return render(request,
                  "are_you_sure.html",
                  context={
                      "type": "Máquina",
                      "item": machine.name
                  })


@login_required
def delete_distro(request, id):
    distro = Distros.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            distro.delete()

        return redirect("home")
    return render(request,
                  "are_you_sure.html",
                  context={
                      "type": "Distribuição",
                      "item": distro.name
                  })


@login_required
def delete_feature(request, id):
    feature = Features.objects.get(id=id)
    if request.method == "POST":
        if "confirm" in request.POST:
            feature.delete()

        return redirect("home")
    return render(request,
                  "are_you_sure.html",
                  context={
                      "type": "Funcionalidade",
                      "item": feature.name
                  })


def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/listusers')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {
        'form': form,
        'action': 'Adicionar'
    })


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Login bem sucedido!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciais Inválidas')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def list_users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('/listusers')
    else:
        form = CreateUserForm(instance=user)
    return render(request, 'update.html', {'form': form, 'action': 'Update'})


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('/listusers')
    return render(request, 'are_you_sure.html', {
        'item': user,
        'type': 'Usuário'
    })
