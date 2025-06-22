from django.shortcuts import render

from django.http import HttpRequest
from .models import Employee


def render_employees_page(request: HttpRequest):
    """
    Render the employees page.
    """
    employees = Employee.objects.all()
    context = {
        "employees": employees,
    }
    return render(request, "apps/employees/index.html", context=context)
