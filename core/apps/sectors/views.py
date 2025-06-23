from django.http import HttpRequest
from django.shortcuts import render

from .models import Sector


def render_sectors_page(request: HttpRequest):
    """
    Render the sectors page with a list of all sectors.
    """
    sectors = Sector.objects.all()
    context = {
        "sectors": sectors,
    }
    return render(request, "apps/sectors/index.html", context)
