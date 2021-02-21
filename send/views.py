from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction, Users


# Create your views here.
def transfer(request):
    t = Users.objects.all()
    if request.method == 'POST':
        amt = request.POST['amt'] 
        response = render(request,'send/second.html', {'user':t})
        response.set_cookie('amt',amt)
        uid1 = request.COOKIES['uid1']
        user1 = Users.objects.get(pk=uid1) 
        if user1.amount>amt: 
            return response
        else:
            return render(request,'send/first.html',{'user':t})

    if 'flag' in request.COOKIES:
        uid1 = request.COOKIES['uid1']
        uid2 = request.COOKIES['uid2']
        amountt = request.COOKIES['amt']
        user1 = Users.objects.get(pk=uid1)
        user2 = Users.objects.get(pk=uid2)
        tr = Transaction ( sender=user1.name, receiver=user2.name, amt=amountt ) 
        tr.save()
        user1.amount = user1.amount - int(amountt) 
        user2.amount = user2.amount + int(amountt)
        user1.save()
        user2.save()
        t = Transaction.objects.all()
        return render(request,'send/allrecords.html',{'transactions':t})
    return render(request, 'send/first.html', {'user':t})

 
def view(request):
    t = Transaction.objects.all()
    return render(request,'send/allrecords.html',{'transactions':t})

