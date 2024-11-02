from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required    
def user_ehr_view(request):
    username = request.user.username
    first_name = request.user.first_name

    try:
        patient = Patient.objects.get(first_name=first_name)

        if patient.first_name == username:
            return render(request, 'patients/user_ehr_detail.html', {'patient': patient})
        else:
            return HttpResponse("No matching EHR found.")
    
    except Patient.DoesNotExist:
        return HttpResponse("No matching EHR found in the database.")

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required    
def patient_list(request):
    patients = Patient.objects.all()
    if request.user.is_authenticated and request.user.is_superuser: 
        return render(request, 'patients/patient_list.html', {'patients': patients})
    else:
        return HttpResponse(f"Sorry, {request.user.first_name}, you are not authorized to view this record.")

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if (request.user.first_name == patient.first_name and request.user.last_name == patient.last_name) or request.user.is_superuser:
        return render(request, 'patients/patient_detail.html', {'patient': patient})
    else:
         return HttpResponse(f"Sorry, {request.user.first_name}, you are not authorized to view this record.")

def patient_create(request):

    if request.user.is_superuser == False:
         return HttpResponse(f"Sorry, {request.user.first_name}, you are not authorized to view this record.")

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})


def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')     
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})
