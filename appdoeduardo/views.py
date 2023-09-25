from django.shortcuts import render, redirect
from .models import Machines, Features, Distros
from .forms import DistrosForm, MachinesForm, FeaturesForm


# Create your views here.
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
