from django.shortcuts import render

# Create your views here.
from event_manager.models import event


def get_main(request):
    return


def get_filtered(request):
    return


def get_participants(request):
    return


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):
    greeting = event
    greeting.save()

    greetings = event.objects.all()

    return render(request, "db.html", {"greetings": greetings})
