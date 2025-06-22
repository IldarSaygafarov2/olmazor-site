from django.shortcuts import render


def render_home_page(request):
    """
    Render the home page of the application.
    """
    return render(request, "apps/main/index.html")
