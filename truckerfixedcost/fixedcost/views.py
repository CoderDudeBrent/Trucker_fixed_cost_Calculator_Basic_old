from django.shortcuts import render
from django.http import HttpResponse


def calculate_cost(request):
    if request.method == 'POST':
        # Get the values of the input fields
        truck_payment = request.POST.get('truck_payment')
        insurance_cost = request.POST.get('insurance_cost')
        license_plates = request.POST.get('license_plates')
        permits = request.POST.get('permits')
        total_miles_driven = request.POST.get('total_miles_driven')

        # Calculate the total cost and cost per mile
        total_cost = int(truck_payment) + int(insurance_cost) + int(license_plates) + int(permits)
        cost_per_mile = total_cost / int(total_miles_driven)

        # Pass the results to the template
        context = {
            'total_cost': total_cost,
            'cost_per_mile': cost_per_mile,
        }
        return render(request, 'fixedcost.html', context)


def fixedcost(request):
    return render(request, 'fixedcost.html')
