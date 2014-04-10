from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from forms import RegistrationForm, RecordForm
from .models import Record


def Index(request):
    return render(request, 'Checkpoint/index.html')

def contacts(request):
    return render(request, 'Checkpoint/contacts.html')

def registrationPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
        return render( request, 'registration/register.html', {'form': form,} )
    else:
        form = RegistrationForm()
        return render( request, 'registration/register.html', {'form': form,} )

def table(request):
    Records = Record.objects.all()
    return render(request, 'Checkpoint/table.html', {'Records': Records})

def searchDriver(request):
    if request.method == 'POST':
        Records = Record.objects.filter(driver__icontains = request.POST['driver'])
        return render(request, 'Checkpoint/table.html', {'Records': Records})

def statistics(request):
    Records = Record.objects.all()
    for r in Records:
        print r.driver
    return render(request, 'Checkpoint/Statistics.html')

@login_required
def recordCreate(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = Record.objects.create(
                vehicleNumber = form.cleaned_data['vehicleNumber'],
                driver = form.cleaned_data['driver'],
                cargo = form.cleaned_data['cargo'],
                recordedBy = request.user
            )
            return HttpResponseRedirect(reverse('table'))
        return render(request, 'Checkpoint/record_create_form.html', {'form': form})
    else:
        form = RecordForm()
        return render(request, 'Checkpoint/record_create_form.html', {'form': form})

@login_required
def recordDelete(request, id):
    Record.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('table'))
