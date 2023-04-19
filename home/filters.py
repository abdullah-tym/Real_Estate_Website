import django_filters 
from django_filters import CharFilter, ChoiceFilter, NumberFilter
from .models import home_info, home_address 

class searchFilter(django_filters.FilterSet):
	price = django_filters.NumberFilter()
	price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
	price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

	addressName = CharFilter(field_name='address__address', lookup_expr = 'icontains')

	cities = (
		('Ankara', 'Ankara'),
		('Istanbul', 'Istanbul'),
		('Izmir', 'Izmir'),
		('Mersin', 'Mersin'),
		('Aydin', 'Aydin'),
		)
	city = ChoiceFilter(field_name ='city', choices = cities, empty_label='City')

	options = (
		('For Sale', 'For Sale'),
		('For Rent', 'For Rent'),
		)
	Type = ChoiceFilter(field_name ='Type', choices = options, empty_label='Property type')

	numbers = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('5+','5+'),	
		)
	bedrooms = ChoiceFilter(field_name ='bedrooms', choices = numbers, empty_label='Bedrooms')

	bathrooms = ChoiceFilter(field_name ='bathrooms', choices = numbers, empty_label='Bathrooms')

	class Meta:
		model = home_info
		fields = '__all__'
		exclude = ['image', 'description'] 
