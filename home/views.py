from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>مرحبًا بك في موقعي!</h1>")
