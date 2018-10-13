from django.db import models

# Create your models here.

class Property(models.Model):
    user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    TYPE_PROPERTY_CHOICES = (
        ('H', 'House'),
        ('A', 'Apartment'),
        ('S', 'Studio'),
        ('O', 'others'),
    )
    types_property = models.CharField(max_length=1, choices=TYPE_PROPERTY_CHOICES, default='others')

    '''
    address
    '''
    province = models.CharField(max_length=20, blank=False, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    state = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    postcode = models.IntegerField(default=0, blank=False, null=False)

    capacity = models.PositiveIntegerField(default=0)
    num_bathrooms = models.PositiveIntegerField(default=0)
    num_bedrooms = models.PositiveIntegerField(default=0)
    num_double_bed = models.PositiveIntegerField(default=0)
    num_single_bed = models.PositiveIntegerField(default=0)
    num_sofa_bed = models.PositiveIntegerField(default=0)
    area = models.FloatField(default=0.0)

    kitchen = models.BooleanField(default=False)
    in_unit_washer = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    blower = models.BooleanField(default=False)
    bathtub = models.BooleanField(default=False)

    parking = models.BooleanField(default=False)
    gyms = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)

    party = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)

    longitude = models.FloatField(default=0.0)  # 经度
    latitude = models.FloatField(default=0.0)  # 纬度

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=False)


# class Address(models.Model):
#     pid = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='Property.pid+')
#     province = models.CharField(max_length=20)
#     city = models.CharField(max_length=20)
#     state = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)
#     postcode = models.IntegerField(default=0)


class Images(models.Model):
    pid = models.ForeignKey(Property,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=100,blank=True, null=True)

    # def __unicode__(self):
    #     return '%s %s' % (self.pid, self.image)
