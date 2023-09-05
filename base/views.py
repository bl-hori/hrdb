from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("base/home.html")
    ctx = {"title": "Django Home"}
    return HttpResponse(template.render(ctx, request))
