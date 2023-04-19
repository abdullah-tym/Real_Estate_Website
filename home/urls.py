from django.urls import path 

from . import views

urlpatterns = [

	path('', views.index.as_view(), name='index'),
	path('about/', views.whoAreWe.as_view(), name='whoAreWe'),
	path('clientView/', views.clientView.as_view(), name='clientView'),
	path('buying/', views.buyingView.as_view(), name = 'buying'),
	path('ajax/', views.ajaxForm, name='ajaxForm'),

]