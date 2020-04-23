from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, first_name,middle_name,last_name,phone,password=None ):
		if not email:
			raise ValueError('Users must have an email address')
		"""if not username:
			raise ValueError('Users must have a username')"""

		user = self.model(

			email			= self.normalize_email(email),
			first_name		= first_name,
			middle_name 	= middle_name,
			last_name	 	= last_name,
			phone 		 	= phone
		)

		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, first_name, middle_name, last_name, phone, password):
		user = self.create_user(

			email=self.normalize_email(email),
			first_name=first_name,
			middle_name=middle_name,
			last_name=last_name,
			phone=phone,
			password = password,
		)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	cust_id 				= models.AutoField(primary_key=True)
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name 				= models.CharField(max_length=30)
	middle_name 			= models.CharField(max_length=30)
	last_name 				= models.CharField(max_length=30)
	phone 					= models.IntegerField()
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','middle_name','last_name','phone',]

	objects = MyAccountManager()

	def __str__(self):
		return str(self.cust_id)

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
