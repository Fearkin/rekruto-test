from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "GET":
        name = request.GET.get("name", "")
        message = request.GET.get("message", "")
        context = {"name": name, "message": message}
        return render(request, "hello_service/index.html", context)
    return HttpResponse("Should be GET request")