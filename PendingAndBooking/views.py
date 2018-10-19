from django.http import HttpResponse
from django.shortcuts import render, redirect
from Property import models
from PendingAndBooking import models as Pmodels
from PendingAndBooking import forms
from django.db.models import Q
import re

# Create your views here.
def booking(request):
    pid = request.POST.get('pid')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    contact_name = request.POST.get('name_booking')
    contact_phone = request.POST.get('Phone_booking')

    pid = int(pid)
    if not check_in:
        print("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)

    print("pid {}, check_in {}, check_out {}, contact_name {}, contact_phone {}".format(pid,check_in,check_out,contact_name,contact_phone))

    booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                              Q(end_time__gt=check_in)
                                                              ).values_list('pid', flat=True).distinct()
    # for x in booked_properties:
    #     print('booked id is ',x)

    if pid not in booked_properties:
        tr = Pmodels.TransAndReview()
        tr.user_ID = request.user
        tr.start_time = check_in
        tr.end_time = check_out
        tr.pid = models.Property.objects.get(id= pid)
        tr.contact_name = contact_name
        tr.contact_phone = contact_phone
        tr.save()
        trans_id = tr.id
        print(trans_id)
        return HttpResponse(trans_id)
    else:
        return HttpResponse('failed')


def paynow(request,trip_id):
    print(trip_id)
    # print("this is here")
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    total_money = (trip.end_time-trip.start_time).days * trip.pid.price
    # print (total_money)
    return render(request,'paynow.html',{'total_money':total_money, 'trip_id':trip_id})

def trips(request):
    template = 'my_trips.html'
    user_ID = request.user
    trip_list = Pmodels.TransAndReview.objects.filter(Q(user_ID__exact=user_ID)).distinct()
    # trip_property_list = []
    # for trip in trip_list:
    #     property = models.Property.objects.filter(pk=trip.pid_id)
    my_trips = sorted(trip_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trips':my_trips})

def payment(request,trip_id):
    template = 'my_trips.html'
    print('here')
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    trip.status = 'C'
    trip.save()
    user_ID = request.user
    trip_list = Pmodels.TransAndReview.objects.filter(Q(user_ID__exact=user_ID)).distinct()
    my_trips = sorted(trip_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trips': my_trips})

def my_trans(request):
    template = 'my_trans.html'
    user_ID = request.user
    property_list = models.Property.objects.filter(Q(user_ID__exact=user_ID)).values_list('id', flat=True).distinct()
    trans_list = Pmodels.TransAndReview.objects.filter(Q(pid__in=property_list)).distinct()
    my_trans = sorted(trans_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trans':my_trans})

def confirm(request,tran_id):
    tran = Pmodels.TransAndReview.objects.get(pk=tran_id)
    tran.status = 'S'
    tran.save()
    template = 'my_trans.html'
    user_ID = request.user
    property_list = models.Property.objects.filter(Q(user_ID__exact=user_ID)).values_list('id', flat=True).distinct()
    trans_list = Pmodels.TransAndReview.objects.filter(Q(pid__in=property_list)).distinct()
    my_trans = sorted(trans_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trans': my_trans})

def pending(request):
    pid = request.POST.get('pid')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    contact_name = request.POST.get('name_booking')
    contact_phone = request.POST.get('Phone_booking')

    pid = int(pid)
    if not check_in:
        print("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)

    print("pid {}, check_in {}, check_out {}, contact_name {}, contact_phone {}".format(pid, check_in, check_out,
                                                                                        contact_name, contact_phone))

    booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                              Q(end_time__gt=check_in)
                                                              ).values_list('pid', flat=True).distinct()
    for x in booked_properties:
        print('booked id is ', x)

    if pid not in booked_properties:
        tr = Pmodels.TransAndReview()
        tr.user_ID = request.user
        tr.start_time = check_in
        tr.end_time = check_out
        tr.pid = models.Property.objects.get(id=pid)
        tr.contact_name = contact_name
        tr.contact_phone = contact_phone
        tr.status = 'P'
        tr.save()
        trans_id = tr.id
        print(trans_id)
        return HttpResponse(trans_id)
    else:
        return HttpResponse('failed')

def pending_request(request,trip_id):
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    return render(request, 'pending_request.html', {'trip_id':trip_id,'property':trip.pid})

def add_pending(request):
    trip_id = request.POST.get('trip_id')
    price = request.POST.get('price')
    capacity = request.POST.get('capacity')
    party = request.POST.get('party',False)
    pet = request.POST.get('pet',False)
    smoking = request.POST.get('smoking',False)
    couple = request.POST.get('couple',False)



    print(price,capacity,party,pet,smoking,couple)

    pending_tr = Pmodels.PendingAndTrans()
    pending_tr.price = price
    pending_tr.capacity = capacity
    pending_tr.party = party
    pending_tr.pet = pet
    pending_tr.smoking = smoking
    pending_tr.couple = couple
    pending_tr.trans_ID = Pmodels.TransAndReview.objects.get(id=trip_id)
    pending_tr.save()

    template = 'my_trips.html'
    user_ID = request.user
    trip_list = Pmodels.TransAndReview.objects.filter(Q(user_ID__exact=user_ID)).distinct()
    my_trips = sorted(trip_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trips': my_trips})

def show_pending(request, tran_id):
    pending_trans = Pmodels.PendingAndTrans.objects.get(trans_ID_id=tran_id)
    print('pending id is {}'.format(pending_trans.id))
    trip = Pmodels.TransAndReview.objects.get(id=tran_id)
    print(trip.id)
    print('property id is {}'.format(trip.pid.id))
    return render(request, 'show_pending.html', {'pending_trans':pending_trans,'pending_id':pending_trans.id,'trip_id':trip.id,'trip':trip,'property':trip.pid})

def finish_pending(request):
    agree = request.POST.get('agree')
    print('finish agree is {}'.format(agree))
    trip_id = request.POST.get('trip_id')
    print('finish trip id is {}'.format(trip_id))
    pending_id = request.POST.get('pending_id')
    print('finish pending id is {}'.format(pending_id))
    trip = Pmodels.TransAndReview.objects.get(id=trip_id)
    pending_trans = Pmodels.PendingAndTrans.objects.get(id=pending_id)

    if agree == 'Disagree':
        pending_trans.delete()
        trip.delete()
    else:
        trip.status = 'PB'
        trip.save()

    template = 'my_trans.html'
    user_ID = request.user
    property_list = models.Property.objects.filter(Q(user_ID__exact=user_ID)).values_list('id', flat=True).distinct()
    trans_list = Pmodels.TransAndReview.objects.filter(Q(pid__in=property_list)).distinct()
    my_trans = sorted(trans_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trans': my_trans})

def pending_paynow(request,trip_id):
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    pending_trans = Pmodels.PendingAndTrans.objects.get(trans_ID_id=trip_id)
    total_money = (trip.end_time - trip.start_time).days * pending_trans.price
    # print (total_money)
    return render(request, 'paynow.html', {'total_money': total_money, 'trip_id': trip_id})
