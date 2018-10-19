from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404


from Property import forms, models
from Property import forms
from .models import Property, Images
from .forms import PropertyForm, ImageForm
from PendingAndBooking.models import TransAndReview
from UserAndAdmin.models import User
import time
import datetime

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def add_property(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    if request.method == "POST":
        property_form = forms.PropertyForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if property_form.is_valid() and formset.is_valid():
            # user_ID = property_form.cleaned_data['user_ID']

            price = property_form.cleaned_data['price']
            types_property = property_form.cleaned_data['types_property']

            province = property_form.cleaned_data['province']
            city = property_form.cleaned_data['city']
            state = property_form.cleaned_data['state']
            address = property_form.cleaned_data['address']
            postcode = property_form.cleaned_data['postcode']

            capacity = property_form.cleaned_data['capacity']
            num_bathrooms = property_form.cleaned_data['num_bathrooms']
            num_bedrooms = property_form.cleaned_data['num_bedrooms']
            num_double_bed = property_form.cleaned_data['num_double_bed']
            num_single_bed = property_form.cleaned_data['num_single_bed']
            num_sofa_bed = property_form.cleaned_data['num_sofa_bed']
            area = property_form.cleaned_data['area']

            kitchen = property_form.cleaned_data['kitchen']
            in_unit_washer = property_form.cleaned_data['in_unit_washer']
            elevator = property_form.cleaned_data['elevator']
            heating = property_form.cleaned_data['heating']
            ac = property_form.cleaned_data['ac']
            tv = property_form.cleaned_data['tv']
            wifi = property_form.cleaned_data['wifi']
            blower = property_form.cleaned_data['blower']
            bathtub = property_form.cleaned_data['bathtub']

            parking = property_form.cleaned_data['parking']
            gyms = property_form.cleaned_data['gyms']
            swimming_pool = property_form.cleaned_data['swimming_pool']

            party = property_form.cleaned_data['party']
            pet = property_form.cleaned_data['pet']
            smoking = property_form.cleaned_data['smoking']
            couple = property_form.cleaned_data['couple']
            status = property_form.cleaned_data['status']

            # new_property = models.Property()
            new_property = property_form.save(commit=False)
            new_property.user_ID = request.user
            new_property.price = price
            new_property.types_property = types_property

            new_property.province = province
            new_property.city = city
            new_property.state = state
            new_property.address = address
            new_property.postcode = postcode
            #yguyguyguyg

            new_property.capacity = capacity
            new_property.num_bathrooms = num_bathrooms
            new_property.num_bedroom = num_bedrooms
            new_property.num_double_bed = num_double_bed
            new_property.num_single_bed = num_single_bed
            new_property.num_sofa_bed = num_sofa_bed
            new_property.area = area

            new_property.kitchen = kitchen
            new_property.in_unit_washer = in_unit_washer
            new_property.elevator = elevator
            new_property.heating = heating
            new_property.ac = ac
            new_property.tv = tv
            new_property.wifi = wifi
            new_property.blower = blower
            new_property.bathtub = bathtub

            new_property.parking = parking
            new_property.gyms = gyms
            new_property.swimming_pool = swimming_pool

            new_property.party = party
            new_property.pet = pet
            new_property.smoking = smoking
            new_property.couple = couple
            new_property.status = status

            new_property.created_at = time.asctime(time.localtime(time.time()))  #
            new_property.updated_at = time.asctime(time.localtime(time.time()))
            new_property.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(pid=new_property, image=image)
                photo.save()
            return render(request, 'detail_of_myProperty.html', {'property': new_property})
    else:
        property_form = forms.PropertyForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'add_property.html', {'property_form': property_form, 'formset': formset})

def delete_property(request,property_id):
    property = get_object_or_404(Property, pk=int(property_id))
    property.delete()
    properties = Property.objects.filter(user_ID = request.user)
    return render(request,'list_property.html',{'properties':properties})

def release_property(request,property_id):
    property = Property.objects.get(pk=int(property_id))
    property.status = True
    property.save()
    properties = Property.objects.filter(user_ID = request.user)
    return render(request,'list_property.html',{'properties':properties})

def cancel_release(request,property_id):
    property = Property.objects.get(pk=int(property_id))
    property.status = False
    property.save()
    properties = Property.objects.filter(user_ID = request.user)
    return render(request,'list_property.html',{'properties':properties})



def edit_property(request,property_id):
    if request.method == "POST":
        property = get_object_or_404(Property, pk=int(property_id))
        property.types_property = request.POST.get('types_property')
        property.price = request.POST.get('price')

        property.types_property = request.POST.get('types_property')
        property.province = request.POST.get('province')
        property.city = request.POST.get('city')
        property.state = request.POST.get('state')
        property.address = request.POST.get('address')
        property.postcode = request.POST.get('postcode')

        property.capacity = request.POST.get('capacity')
        property.num_bathrooms = request.POST.get('num_bathrooms')
        property.num_bedroom = request.POST.get('num_bedroom')
        property.num_double_bed = request.POST.get('num_double_bed')
        property.num_single_bed = request.POST.get('num_single_bed')
        property.num_sofa_bed = request.POST.get('num_sofa_bed')
        property.area = request.POST.get('area')

        property.kitchen = request.POST.get('kitchen',False)
        property.in_unit_washer = request.POST.get('in_unit_washer',False)
        property.elevator = request.POST.get('elevator',False)
        property.heating = request.POST.get('heating',False)
        property.ac = request.POST.get('ac',False)
        property.tv = request.POST.get('tv',False)
        property.wifi = request.POST.get('wifi',False)
        property.blower = request.POST.get('blower',False)
        property.bathtub = request.POST.get('bathtub',False)

        property.parking = request.POST.get('parking',False)
        property.gyms = request.POST.get('gyms',False)
        property.swimming_pool = request.POST.get('swimming_pool',False)

        property.party = request.POST.get('party',False)
        property.pet = request.POST.get('pet',False)
        property.smoking = request.POST.get('smoking',False)
        property.couple = request.POST.get('couple',False)
        property.status = request.POST.get('status',False)
        
        property.updated_at = time.asctime(time.localtime(time.time()))
        property.save()

        return render(request, 'detail_of_myProperty.html', {'property': property})
    else:
        property = get_object_or_404(Property, pk=int(property_id))
        return render(request, 'edit_property.html', {'property_form': property})

def list_property(request):
    properties = Property.objects.filter(user_ID = request.user)
    return render(request,'list_property.html',{'properties':properties})

def look_detail_of_myProperty(request,property_id):
    property = get_object_or_404(Property, pk=int(property_id))
    return render(request, 'detail_of_myProperty.html', {'property': property})


def add_review(request):
    if request.method=="POST":
        reviewForm = forms.AddReviewForm(request.POST)
        print(reviewForm.errors)
        if reviewForm.is_valid():
            trip_id = reviewForm.cleaned_data["trip_id"]
            position_review = reviewForm.cleaned_data["position_review"]
            comfort_review  = reviewForm.cleaned_data["comfort_review"]
            price_review = reviewForm.cleaned_data["price_review"]
            quality_review = reviewForm.cleaned_data["quality_review"]
            comment_content = reviewForm.cleaned_data["comment_content"]


            print('trip_id here is {}'.format(trip_id))


            #  get trip
            tr = TransAndReview.objects.get(id=trip_id)

            # add comment
            tr.comment_content = comment_content
            tr.position_review = position_review
            tr.comfort_review = comfort_review
            tr.price_review = price_review
            tr.quality_review = quality_review


            tr.ratings = round((position_review + comfort_review + price_review + quality_review)/4)

            tr.save()
            return HttpResponse(1)
        else:
            return HttpResponse(2)


def property_detail(request, property_id, trip_id):

    tr_list = TransAndReview.objects.filter(pid=property_id,status='S')

    _sum_rating = []
    ############ 评论列表
    review_lists=[]
    for tr in tr_list:
        review_list={}
        review_list['name'] = User.object.filter(email=tr.user_ID)[0].first_name
        review_list['time'] = tr.end_time
        if tr.comment_content == 'danjieniubi':
            continue
        review_list['review'] = tr.comment_content
        _sum_rating.append(tr.ratings)
        review_list['ratings_p'] = ["1"]*tr.ratings
        review_list['ratings_n'] = ["1"]*(5 - tr.ratings)
        review_lists.append(review_list)

    review_lists = sorted(review_lists,key=lambda x: x["time"],reverse=True)
    ############# 评论概况
    review_summary = {}
    review_summary["num_review"] = len(_sum_rating)
    if len(_sum_rating):
        review_summary["average_rating"] = round(sum(_sum_rating) / len(_sum_rating),1)
    else:
        review_summary["average_rating"] = 0

    property = Property.objects.get(id=property_id)
    property_id = property_id
    # print(property_id)
    return render(request, 'property_detail.html', {'property_id':property_id,'property': property,'review_lists': review_lists,'review_summary':review_summary,'trip_id':trip_id})


