from django.conf.urls import patterns, url
from carpooling import views

urlpatterns = patterns('',url(r'^$', views.loginuser, name='loginuser'),
							url(r'^register/$', views.register, name='register'),
							url(r'^loginverify/$', views.loginverify, name='loginverify'),
							url(r'^registration/$', views.registration, name='registration'),	
							url(r'^logoutuser/$', views.logoutuser, name='logoutuser'),
							
							url(r'^menu/$', views.menu, name='menu'),
							url(r'^viewvehicles/$', views.viewvehicles, name='viewvehicles'),
							url(r'^addvehicle/$', views.addvehicle, name='addvehicle'),	
							url(r'^notifications/$', views.notifications, name='notifications'),	
							#url(r'^contact/$', views.contact, name='contact'),
							
							url(r'^requests/$', views.requests, name='requests'),
							url(r'^addcheck/$', views.addcheck, name='addcheck'),
							url(r'^availablevehicles/$', views.availablevehicles, name='availablevehicles'),
							url(r'^(?P<vehicle_id>\d+)/(?P<seats>\d+)/makeRequest/$', views.makeRequest, name='makeRequest'),
							
							url(r'^(?P<request_id>\d+)/accept/$', views.accept, name='accept'),
						    url(r'^(?P<request_id>\d+)/reject/$', views.reject, name='reject'),
						    
						   url(r'^acceptedusers/$', views.acceptedusers, name='acceptedusers'),
						   
						   url(r'^(?P<user_id>\d+)/requestlocation/$', views.requestlocation, name='requestlocation'),
							url(r'^(?P<user_id>\d+)/userlocation/$', views.userlocation, name='userlocation'),
							url(r'^(?P<user_id>\d+)/allowlocation/$', views.allowlocation, name='allowlocation'),
							)

