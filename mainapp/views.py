from django.shortcuts import render
import time

doctors = {"Smith": "Anesthesiologist", 'Johnson': 'Cardiologist', "Williams":"Dermatologist", "Jones":"Neurologist"}
timing =  ['9.00am', '9.30am', '10.00am','10.30am','11.00am','11.30am','12.00pm','12.30pm','1.00pm','3.00pm','3.30pm','4.00pm','4.30pm','5.00pm','5.30pm','6.00pm', '6.30pm', '7.00pm','7.30pm','8.00pm']

def index(request):
    return render(request,"patient/index.html")