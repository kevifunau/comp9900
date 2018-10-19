from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class TransAndReview(models.Model):
    user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    pid = models.ForeignKey('Property.Property', verbose_name='owner', on_delete=models.CASCADE, related_name='TransAndReview.pid+')
    # comment_time = models.DateTimeField(null=True)
    comment_content = models.CharField(max_length=500, default='danjieniubi')
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=False)
    ratings = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],null=True, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status_choies = (
        ('B', 'Booking'),
        ('P', 'Pending'),
        ('PB', 'Pending paying'),
        ('C', 'Comfirming'),
        ('S', 'Success'),
    )
    status = models.CharField(max_length=20, choices=status_choies, default='B')

    #### review
    position_review = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],null=True, default=5)
    comfort_review = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],null=True, default = 5)
    price_review= models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],null=True, default=5)
    quality_review= models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],null=True, default=5)

    ### booking
    contact_name = models.CharField(max_length=500, default='',null=True)
    contact_phone = models.CharField(max_length=10, default='',null=True)







class PendingAndTrans(models.Model):
    price = models.FloatField(default=0.0)
    capacity = models.IntegerField(default=0)
    smoking = models.BooleanField(default=False)
    party = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)
    trans_ID = models.ForeignKey('PendingAndBooking.TransAndReview', on_delete=models.CASCADE,null=True)

