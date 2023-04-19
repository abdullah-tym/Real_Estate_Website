from django.db import models
from django.db.models import CharField


class contact(models.Model):
	name = models.CharField(max_length = 40, null = False)
	email = models.CharField(max_length = 40, null = False)
	message = models.TextField(max_length = 100, null = False)
	
	def __str__(self):
		return str(self.name)

# one to one attriubute:	
class home_description(models.Model):
	description = models.CharField(max_length = 100)	

	def __str__(self):
		return str(self.description)

# one to one attriubute:	
class home_address(models.Model):
	address = models.CharField(max_length = 100)
	zip_code = models.IntegerField()
	location = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.address)

class home_info(models.Model):
	home_number = models.IntegerField() #(NOT PRIMARY KEY)
	title = models.CharField(max_length = 40)

	cities = (
		('Ankara', 'Ankara'),
		('Istanbul', 'Istanbul'),
		('Izmir', 'Izmir'),
		('Mersin', 'Mersin'),
		('Aydin', 'Aydin'),
		)
	city = models.CharField(max_length = 40, choices = cities)

	options = (
		('For Sale', 'For Sale'),
		('For Rent', 'For Rent'),
		)
	Type = models.CharField(max_length = 40, choices=options)

	price = models.IntegerField()

	numbers = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('5+','5+'),	
	)
	bedrooms = models.CharField(max_length = 40, choices=numbers)
	bathrooms = models.CharField(max_length = 40, choices=numbers)
	image = models.ImageField(upload_to='home_images')		

	description = models.OneToOneField(home_description, on_delete=models.CASCADE)
	address = models.OneToOneField(home_address,  related_name = 'addressName', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.home_number)



