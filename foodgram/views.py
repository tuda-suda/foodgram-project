from django.shortcuts import render


def page_not_found(request, exception):
    """
    Handle HTTP 404 Not Found.
    """
    return render(request, 'error/404.html', status=404)


def server_error(request):
    """
    Handle HTTP 500 Server Error.
    """
    return render(request, 'error/500.html', status=500)


def page_bad_request(request, exception):
    """
    Handle HTTP 400 Bad Request.
    """
    return render(request, 'error/400.html', status=400)
