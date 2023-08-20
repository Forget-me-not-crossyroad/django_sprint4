from django.shortcuts import render


def internal_server_error(request, exception=None):
    """Функция возврата 500 ошибки ."""
    return render(request, "pages/500.html", status=500)


def page_not_found(request, exception):
    """Функция возврата 404 ошибки."""
    return render(request, "pages/404.html", status=404)


def csrf_failure(request, reason=""):
    """Функция возврата 403 ошибки."""
    return render(request, "pages/403csrf.html", status=403)
