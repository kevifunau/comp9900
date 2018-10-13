from django.shortcuts import render, redirect
from Property import forms, models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re



def simple_search(request):
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
        print ("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print ("no check_out")
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


    print('check_in: {},check_out: {},type: {},capacity: {},city: {},price: {}'.format(check_in,check_out,type,capacity,city,price),sep='\n')

    if not check_in and not check_out:
        booked_properties = []
    elif not check_in:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out)
                                                             ).values_list('pid',flat=True).distinct()
    elif not check_out:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(end_time__gt=check_in)
                                                             ).values_list('pid',flat=True).distinct()
    else:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                                 Q(end_time__gt=check_in)
                                                                 ).values_list('pid',flat=True).distinct()

    for x in booked_properties:
        print('booked id is ',x)


    property_list = models.Property.objects.filter(Q(city__icontains=city) &
                                                   Q(types_property__icontains=type) &
                                                   Q(price__gte=price) &
                                                   Q(capacity__gte=capacity)
                                                   ).distinct().exclude(id__in=booked_properties)



    # ====================== sort part====================================

    property_list = sorted(property_list, key=lambda x: x.price, reverse=False)

    # ====================== end sort part =================================

    # 分页-----------------
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)



    context = {
        'properties': properties,
        'city': city,
        'check_in': check_in,
        'check_out': check_out,
        'capacity': capacity,
        'price': price,
        'type': type,
    }
    return render(request, template, context)


def multi_search(request):
    template = 'multi_search_list.html'

    search_form = forms.SearchForm(request.POST)
    # if search_form.is_valid():
    price = search_form.cleaned_data['price']
    types_property = search_form.cleaned_data['types_property']

    province = search_form.cleaned_data['province']
    city = search_form.cleaned_data['city']
    state = search_form.cleaned_data['state']
    address = search_form.cleaned_data['address']
    postcode = search_form.cleaned_data['postcode']

    capacity = search_form.cleaned_data['capacity']
    num_bathrooms = search_form.cleaned_data['num_bathrooms']
    num_bedrooms = search_form.cleaned_data['num_bedrooms']
    num_double_bed = search_form.cleaned_data['num_double_bed']
    # num_single_bed = search_form.cleaned_data['num_single_bed']
    # num_sofa_bed = search_form.cleaned_data['num_sofa_bed']
    # area = search_form.cleaned_data['area']

    # kitchen = search_form.cleaned_data['kitchen']
    # in_unit_washer = search_form.cleaned_data['in_unit_washer']
    # elevator = search_form.cleaned_data['elevator']
    # heating = search_form.cleaned_data['heating']
    # ac = search_form.cleaned_data['ac']
    # tv = search_form.cleaned_data['tv']
    wifi = search_form.cleaned_data['wifi']
    # blower = search_form.cleaned_data['blower']
    # bathtub = search_form.cleaned_data['bathtub']
    #
    # parking = search_form.cleaned_data['parking']
    # gyms = search_form.cleaned_data['gyms']
    # swimming_pool = search_form.cleaned_data['swimming_pool']
    #
    # party = search_form.cleaned_data['party']
    # pet = search_form.cleaned_data['pet']
    # smoking = search_form.cleaned_data['smoking']
    # couple = search_form.cleaned_data['couple']
    status = search_form.cleaned_data['status']

    property_list = models.Property.objects.filter(Q(province__iexact=province) &
                                                   Q(city__iexact=city) &
                                                   Q(price__exact=price) &
                                                   Q(types_property__iexact=types_property) &
                                                   Q(state__iexact=state) &
                                                   Q(address__iexact=address) &
                                                   Q(postcode__exact=postcode) &
                                                   Q(capacity__gte=capacity) &
                                                   Q(num_bathrooms__gte=num_bathrooms) &
                                                   Q(num_bedrooms__gte=num_bedrooms)&
                                                   Q(num_double_bed__gte=num_double_bed)&
                                                   # Q(num_single_bed__gte=num_single_bed)&
                                                   # Q(num_sofa_bed__gte=num_sofa_bed)&
                                                   # Q(area__exact=area)&
                                                   # Q(kitchen__exact=kitchen)&
                                                   # Q(in_unit_washer__exact=in_unit_washer)&
                                                   # Q(elevator__exact=elevator)&
                                                   # Q(heating__exact=heating)&
                                                   # Q(ac__exact=ac)&
                                                   # Q(tv__exact=tv)&
                                                   Q(wifi__exact=wifi)&
                                                   # Q(blower__exact=blower)&
                                                   # Q(bathtub__exact=bathtub)&
                                                   # Q(parking__exact=parking)&
                                                   # Q(gyms__exact=gyms)&
                                                   # Q(swimming_pool__exact=swimming_pool)&
                                                   # Q(party__exact=party)&
                                                   # Q(pet__exact=pet)&
                                                   # Q(smoking__exact=smoking)&
                                                   # Q(couple__exact=couple)&
                                                   Q(status__exact=status)
                                                   ).distinct()

    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    # index = properties.number - 1
    # max_index = len(paginator.page_range)
    # start_index = index - 5 if index >= 5 else 0
    # end_index = index + 5 if index <= max_index else max_index
    # page_range = paginator.page_range[start_index:end_index]

    search_form = forms.SearchForm()

    context = {
        'properties': properties,
        'search_form': search_form
        # 'page_range': page_range
    }
    print("valid")

    return render(request, template, context)
    # else:
    #     print("unvalied")
    #     return render(request, template, {'search_form': search_form})


