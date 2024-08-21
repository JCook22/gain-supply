from django.shortcuts import render


def handler404(request, exception):
    """
    Custom 404 page to be displayed to users
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Custom 500 page to be displayed to users
    """
    return render(request, "errors/500.html", status=500)


def handler403(request):
    """
    Custom 403 page to be displayer to users
    """
    return render(request, "errors/403.html", status=403)


def handler405(request):
    """
    Custom 405 page to be displayed to users
    """
    return render(request, "errors/405.html", status=405)