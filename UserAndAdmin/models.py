from django.db import models
from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name=None, last_name=None, password=None, date_of_birth=None, is_active=True):
        if not email:
            raise ValueError("empty email! ")

        if not password:
            raise ValueError("empty password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.set_date_of_birth(date_of_birth)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, first_name=None, last_name=None, password=None):

        staff = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name

        )
        staff.staff = True
        staff.save(using=self._db)
        return staff

    def create_superuser(self, email, first_name=None, last_name=None, password=None):
        admin = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name

        )
        admin.staff = True
        admin.admin = True
        admin.save(using=self._db)
        return admin


class User(AbstractBaseUser, PermissionsMixin):
    # 登陆 为用户名登陆
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True)
    USERNAME_FIELD = "email"

    '''
     AbstractBaseUser 内部实现了  密码 和 登陆时间
    password = models.CharField(_('password'), max_length=128)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
 
    staff 工作人员
    admin 管理员 
    
    '''
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    '''
    必填项
    
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    # required_fileds /  创建createsuperuser
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = UserManager()

    '''
    方法
    
    '''

    def set_date_of_birth(self, raw_date_of_birth = None):
        if not raw_date_of_birth:
            raw_date_of_birth = datetime.now()
        self.date_of_birth = raw_date_of_birth

    # long /short 用户标识别
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def set_active(self):
        self.active = True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    # 权限

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        return False

    def has_module_perms(self, app_label):
        return True



class UserProfile(models.Model):
    '''
    个人信息
    性别
    用户自我介绍
    用户手机
    '''

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unknown"),
    )
    user = models.OneToOneField(User, models.CASCADE)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default="U")
    language = models.CharField(max_length = 10,default = 'English')
    image = models.ImageField(null=True,blank=None)
    user_description = models.TextField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length =50,default='U')



# NEIGHNOURHOOD_CHOICES=(
# 'Ashfield',
# 'Auburn',
# 'Bankstown',
# 'Blacktown',
# 'Botany',
# 'Bay',
# 'Burwood',
# 'Camden',
# 'Campbelltown',
# 'Canada',
# 'Bay',
# 'Canterbury',
# 'City',
# 'Of',
# 'Kogarah',
# 'Fairfield',
# 'Holroyd',
# 'Hornsby',
# 'Hunters',
# 'Hill',
# 'Hurstville',
# 'Ku - Ring - Gai',
# 'Lane',
# 'Cove',
# 'Leichhardt',
# 'Liverpool',
# 'Manly',
# 'Marrickville',
# 'Mosman',
# 'North',
# 'Sydney',
# 'Parramatta',
# 'Penrith',
# 'Pittwater',
# 'Randwick',
# 'Rockdale',
# 'Ryde',
# 'Strathfield',
# 'Sutherland',
# 'Shire',
# 'Sydney',
# 'The',
# 'Hills',
# 'Shire',
# 'Warringah',
# 'Waverley',
# 'Willoughby',
# 'Woollahra')
