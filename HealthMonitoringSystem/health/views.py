import csv
from django.shortcuts import render

def display_data(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        with open('static/patient.csv', 'r') as file:
            csv_data = csv.DictReader(file)
            data = [patient for patient in csv_data if patient['PatientID'] == patient_id]
        if data:
            return render(request, 'health/index.html', {'data': data[0]})
    return render(request, 'health/home.html')


