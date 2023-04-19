from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models import contact, home_info
from .filters import searchFilter
from .forms import contactForm
from django.contrib import messages
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView
from django.views import View
from .models import *

#########################

class AjaxMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        def is_ajax(self):
            return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
        request.is_ajax = is_ajax.__get__(request)
        response = self.get_response(request)
        return response

def ajaxForm(request):
	if request.is_ajax():
		form = contactForm(request.POST or None, request.FILES or None)

		if form.is_valid():	
			response = {
				'result': 'success',
				'message': 'Thank you! We have received your message, we will contact you as soon as possible.',
			}
			form.save()
			return JsonResponse(response, status=200)

		else:
			response = {
	            'result': 'error',
	            'message': 'Error! Enter the fields properly',
       		}
			return JsonResponse(response, status = 400)
	
	else:
		return HttpResponse('Eror, not ajax request!')


########################

class index(FormView):
	template_name = 'home/templates/index.html'
	form_class = contactForm	

	def get(self, request):
		home = home_info.objects.order_by('home_number')	


		myFilter = searchFilter(request.GET, queryset=home)
		home = myFilter.qs

		form = self.form_class()

		args = {'home': home, 'myFilter': myFilter, 'form': form}
		return render(request, self.template_name, args)

		
########################

class whoAreWe(FormView):
	template_name = 'home/templates/whoAreWe.html'
	form_class = contactForm	

########################


class clientView(FormView):
	template_name = 'home/templates/client_property.html'
	form_class = contactForm

########################

class buyingView(FormView):
	template_name = 'home/templates/buying.html'
	form_class = contactForm


	def get(self, request):
		home = home_info.objects.order_by('home_number')	


		myFilter = searchFilter(request.GET, queryset=home)
		home = myFilter.qs

		form = self.form_class()

		args = {'home': home, 'myFilter': myFilter, 'form': form}
		return render(request, self.template_name, args)

		

	# inserting the data to the database 
	'''description1 = home_description(description='Ankara apartment for sale, Affordable Ankara investment.')
	description2 = home_description(description='Istanbul amazing villa for sale, wise Istanbul investment.')
	description3 = home_description(description='Izmir villa for rent, wonderful Izmir neighborhood.')
	description4 = home_description(description='Istanbul luxury apartment for sale,  Istanbul investment.')
	description5 = home_description(description='Istanbul nice apartment for sale, Affordable Istanbul investment.')
	description6 = home_description(description='Aydin apartment for rent, Affordable Aydin Apartment.')
	description1.save()
	description2.save()
	description3.save()
	description4.save()
	description5.save()
	description6.save()'''

	'''address1 = home_address(address ='1233. Sk. Ostim Osb/Yenimahalle/Ankara' , zip_code='2245', location = 'https://goo.gl/maps/os2MpeXLmVGiatXG7')
	address2 = home_address(address='European Side Esentepe 34265 Sultangazi/İstanbul', zip_code='34265', location='https://goo.gl/maps/sAXGQcNyx99CnpaBA')
	address3 = home_address(address='Hüseyin Yurttaş Sk. 34-52 Bostanlı 35590 Karşıyaka/İzmir', zip_code='35590', location='https://goo.gl/maps/avv3ZQtDGviECphS9')
	address4 = home_address(address='Anatolian Side Selimiye 34668 Üsküdar/İstanbul', zip_code='34668', location='https://goo.gl/maps/2ERpHFsCnd4rdb2a8')
	address5 = home_address(address='Ataşehir Atatürk 34758 Ataşehir/İstanbul', zip_code='34758', location='	')
	address6 = home_address(address='2120. Sk. No:13 Girne 09100 Aydın Merkez/Aydın', zip_code='09100', location='https://goo.gl/maps/NrhbxPCRdSS8Y1wK7')
	address1.save()
	address2.save()
	address3.save()
	address4.save()
	address5.save()
	address6.save()'''

	#description1_id = home_description.objects.get(pk = 1)
	#address1_id = home_address.objects.get(pk = 1)

	#home1 = home_info(home_number = '101', title='Home in Istanbul', city='Istanbul', Type='For Sale', price='150000', bedrooms='3', bathrooms='2', description = description1_id, address = address1_id)
	#home2 = home_info(home_number = '102', title='', cities='', Type='', price='', bedrooms='', bathrooms='', image= , description='', address='')
	'''home3 = home_info(home_number = '103', title='', cities='', Type='', price='', bedrooms='', bathrooms='', image= , description='', address='')
	home4 = home_info(home_number = '104', title='', cities='', Type='', price='', bedrooms='', bathrooms='', image= , description='', address='')
	home5 = home_info(home_number = '105', title='', cities='', Type='', price='', bedrooms='', bathrooms='', image= , description='', address='')
	home6 = home_info(home_number = '106', title='', cities='', Type='', price='', bedrooms='', bathrooms='', image= , description='', address='')
	home1.save()
	home2.save()
	home3.save()
	home4.save()
	home5.save()
	home6.save()'''
	#home1.save()


#########################


'''def buying(request):
	home = home_info.objects.all()		

	myFilter = searchFilter(request.GET, queryset=home)
	home = myFilter.qs


	if request.is_ajax():
		form = contactForm(request.POST or None, request.FILES or None)
		if form.is_valid():	
			message = 'Thank you! We have received your message, we will contact you as soon as possible'
			form.save()
			return JsonResponse({'message': message}, status=200)

		else:
			return JsonResponse({'message': 'Error! Enter the field properly'})
	
	else:
		args = {'home': home, 'myFilter': myFilter, 'form': form}
		return render(request, 'home/templates/buying.html', args) '''
	

'''def client_property(request):

	form = contactForm(request.POST or None, request.FILES or None)

	if form.is_valid():
	  form.save()
	  form = contactForm()

	args = {'form': form}
	return render(request, 'home/templates/client_property.html', args)'''


#####################

''' def contactView(request):
	context = {}
	if request.method == 'POST':
		name = request.POST['userName']
		email = request.POST['userEmail']
		Message = request.POST['message']'''

	#form = contactForm(request.POST or None, request.FILES or None)

'''new = contact(name = name, email = email, message = Message) '''
'''new.save()'''
'''if form.is_valid():
  form.save()

	context['form'] = form

	return render(request, 'home/templates/index.html', context)

	else:
		return render(request, 'home/templates/index.html', {})'''
