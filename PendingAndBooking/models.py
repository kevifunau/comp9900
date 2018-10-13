from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class TransAndReview(models.Model):
    user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    pid = models.ForeignKey('Property.Property', verbose_name='owner', on_delete=models.CASCADE, related_name='TransAndReview.pid+')
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_content = models.CharField(max_length=500, default='')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status_choies = (
        ('C', 'Comfirming'),
        ('S', 'Success'),
    )
    status = models.CharField(max_length=20, choices=status_choies, default='Booking')

    #### review
    position_review =  models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False,default=5)
    comfort_review = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False,default = 5)
    price_review= models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False,default=5)
    quality_review= models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], null=False,default=5)




class PendingTrans(models.Model):
    user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    pid = models.ForeignKey('Property.Property', verbose_name='owner', on_delete=models.CASCADE, related_name='PendingTrans.pid+')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField(default=0)
    smoking = models.BooleanField(default=False)
    party = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)
    blower = models.BooleanField(default=False)
    bathtub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

