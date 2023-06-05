from django.shortcuts import render
from .models import CreditApplication


def display_manufacturer(request, contract_id):
    credit_app = CreditApplication.objects.get(contract_id=contract_id)
    manufacturer = credit_app.products.all().values_list("manufacturer__id", flat=True).distinct()

    context = {
        "manufacturer": manufacturer
    }

    return render(request, "manufacture.html", context=context)
