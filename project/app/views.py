from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>Homepage</h1>")


def view_b(request):
    return HttpResponse("<h1>View B</h1>")


def view_c(request):
    return HttpResponse("<h1>View C</h1>")
