from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import Event, Participant


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "events_home.html")


def lesson_view(request):
    if not Event.objects.exists():
        context = {'all_events': None}
    else:
        all_events = Event.objects.all()
        all_participants = Participant.objects.all()

        # for event in all_events:
        #     print(event)
        #     for participant in all_participants:
        #         if participant.event_key == event:
        #             print(participant)
        #             event.participants[event] = participant
        #                 # .append(participant.name)
        #     for participant in event.participants[event]:
        #         print(participant)

        context = {'all_events': all_events, 'all_participants': all_participants}

    return render(request, "events_view.html", context)


# TODO
def lesson_filter(request, name):
    if not Event.objects.exists():
        context = {'all_events': None}
    else:
        all_events = Event.objects.all()
        all_participants = Participant.objects.all()
        all_events = all_events.filter(name=name)
        context = {'all_events': all_events, 'all_participants': all_participants}

    return render(request, "events_view.html", context)


def adder(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "adder_home.html")


def add_lesson(request):
    if not Event.objects.exists():
        return render(request, "events_add_new.html")
    else:
        all_events = Event.objects.all()
        event_count = Event.objects.all().count()
        context = {'all_events': all_events, 'event_count': event_count}
        return render(request, "events_add.html", context)


def add_participant(request):
    if not Event.objects.exists():
        return render(request, "participants_add_new.html")
    else:
        all_participants = Participant.objects.all()
        participants_count = Participant.objects.all().count()
        context = {'all_participants': all_participants, 'participants_count': participants_count}
        return render(request, "participants_add.html", context)


def add(request):
    the_values = {
        "key": "the_values"
    }
    for key, value in request.POST.items():
        the_values[key] = value

    new_lesson = Event(name=the_values["event"])

    new_lesson.save()
    return redirect('events:view_events')


# TODO
def add_p(request):
    the_values = {
        "key": "the_values"
    }
    for key, value in request.POST.items():
        the_values[key] = value
        print(key + " " + value)

    # new_lesson = Event(name=the_values["event"])

    # new_lesson.save()
    return redirect('events:view_events')


def clearer(request):
    # return HttpResponse('Hello from Python!')
    if not request:
        return render("down.html")

    return render(request, "clearer_home.html")


def lesson_wipe(request):
    if not Event.objects.exists():
        raise Http404("Event does not exist")
    else:
        all_events = Event.objects.all()

    event_count = Event.objects.all().count()
    context = {'all_events': all_events, 'event_count': event_count}
    return render(request, "events_delete.html", context)


def delete(request):
    name = request.POST.get("name")
    lessons = Event.objects.all()
    lesson = lessons.filter(name=name)
    lesson.delete()
    return redirect('events:view_events')


def delete_participant(request):
    if not Participant.objects.exists():
        raise Http404("Participant does not exist")
    else:
        all_participants = Participant.objects.all()

    participant_count = Participant.objects.all().count()
    context = {'all_participants': all_participants, 'participant_count': participant_count}
    return render(request, "participant_delete.html", context)


def delete_p(request):
    name = request.POST.get("name")
    participants = Participant.objects.all()
    participant = participants.filter(name=name)
    participant.delete()
    return redirect('events:view_events')
