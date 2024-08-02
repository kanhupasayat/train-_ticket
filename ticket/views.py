from django.shortcuts import render,HttpResponse

from .models import Ticket

# Create your views here.


def ticket_from(request):
    if request.method == 'POST':
        train=request.POST.get('train')
        passenger=request.POST.get('passenger')
        state_depart=request.POST.get('state_depart')
        state_arrive=request.POST.get('state_arrive')
        carriage=request.POST.get('carriage')
        print(passenger)
        print(state_arrive)
        print(state_depart)
        data=Ticket.objects.create(train=train,passenger=passenger,state_depart=state_depart,state_arrive=state_arrive,carriage=carriage)
        data.save()
        data=Ticket.objects.latest('id')
        print(data)

        return render (request,"confirm_ticket.html",{'data':data})
    
    return render (request,"from.html")