
from django.urls import path
from . import views


urlpatterns = [
    path("",views.ticket_from,name="from_page")

]