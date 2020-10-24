from django.urls import path

from django.contrib import admin
import events.views

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

app_name = 'events'
urlpatterns = [
    path("", events.views.index, name="index"),
    path("view_lesson", events.views.lesson_view, name="view_events"),

    path("clearer", events.views.clearer, name="clearer"),
    path("delete_lesson", events.views.lesson_wipe, name="clear_event"),
    path("delete", events.views.delete, name="delete"),
    path("delete_participant", events.views.delete_participant, name="clear_participant"),
    path("delete_p", events.views.delete_p, name="delete_p"),

    path("adder", events.views.adder, name="adder"),
    path("add_lesson", events.views.add_lesson, name="add_event"),
    path("add", events.views.add, name="add"),
    path("add_participant", events.views.add_participant, name="add_participant"),
    path("add_p", events.views.add_p, name="add_p"),



]
