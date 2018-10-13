from django.http import HttpResponse
from django.shortcuts import render, redirect
from Property import models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
import re

# Create your views here.
def booking(request):
    template = 'property_list.html'
    if request.method == "POST":
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        type = request.POST.get('type')
        capacity = request.POST.get('adults')
        city = request.POST.get('city')
        price = request.POST.get('price')
    else:
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        type = request.GET.get('type')
        capacity = request.GET.get('adults')
        city = request.GET.get('city')
        price = request.GET.get('price')

    if not check_in:
        print("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)
    if not capacity:
        capacity = 0
    else:
        capacity = int(capacity)
    if not price:
        price = 0
    else:
        price = int(price)
    if not city:
        city = ''
    if type == 'ALL':
        type = ''

    print('check_in: {},check_out: {},type: {},capacity: {},city: {},price: {}'.format(check_in, check_out, type,
                                                                                       capacity, city, price), sep='\n')

    booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                              Q(end_time__gt=check_in)
                                                              ).values_list('pid', flat=True).distinct()

    for x in booked_properties:
        print('booked id is ', x)

    property_list = models.Property.objects.filter(Q(city__icontains=city) &
                                                   Q(types_property__icontains=type) &
                                                   Q(price__gte=price) &
                                                   Q(capacity__gte=capacity)
                                                   ).distinct().exclude(id__in=booked_properties)

    property_list = sorted(property_list, key=lambda x: x.price, reverse=False)

    return HttpResponse("paynow")
