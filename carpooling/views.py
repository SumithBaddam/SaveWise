from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader	#not required
from django.contrib.auth import authenticate, login, logout
from carpooling.models import *
import datetime
import json
import unicodedata

# Create your views here.

#####REGISTRATION	
def register(request):
	usernames = User.objects.all()
	l = []
	for i in usernames:
		l.append(str(i.username))
	for i in l:
		i = i[2:]
	context = {}
	context['usernames'] = json.dumps(l)
	context['number'] = len(l)
	return render(request,'carpooling/register.html',context)


def registration(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		em = request.POST['email']
		usn = request.POST['username']
		pwd = request.POST['password']
		User.objects.create_user(username=usn,email=em,password=pwd,first_name=fname,last_name=lname)
		return redirect(loginuser)
	else:
		print request.method
		return redirect(registration)

#####LOGIN LOGOUT
def loginuser(request):
	logout(request)	
	return render(request,'carpooling/login.html')

def loginverify(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_authenticated():
				login(request,user)
				return 1
	return 0

def menu(request):
	if(request.user.is_authenticated()):
		context ={'name': request.user.first_name + " "+request.user.last_name}
		return render(request, 'carpooling/menu.html',context)
	else:
		if loginverify(request) == 1:
			context ={'name': request.user.first_name +  " "+request.user.last_name}
			return render(request, 'carpooling/menu.html',context)
		else:
			return redirect(loginuser)

def logoutuser(request):
	return redirect(loginuser)

#####ADDING A VEHICLE
def addvehicle(request):
	return render(request, 'carpooling/addvehicle.html')

def addcheck(request):
	u= request.user
	Vehicle.objects.create(user=u,name=request.POST['name'], vehicle_number=request.POST['vehicle_number'], seats=request.POST['seats'], source=request.POST['source'],destination=request.POST['destination'], date = request.POST['time'], price=request.POST['price'])
	return redirect(addvehicle)


#####VIEW AVAILABLE VEHICLES
def viewvehicles(request):
	vehicles = Vehicle.objects.all()
	sources = []
	destinations = []
	for i in vehicles:
		if i.source not in sources:
			sources.append(i.source)
		if i.destination not in destinations:
			destinations.append(i.destination)
	sources.sort()
	destinations.sort()
	context = {'sources':sources,'destinations':destinations}
	return render(request, 'carpooling/viewvehicles.html',context)

def availablevehicles(request):
	src = request.POST['source']
	dest = request.POST['destination']
	s = request.POST['seats']
	req = Request.objects.all()
	vid = []
	for i in req:
		if (i.user.username==request.user.username and i.vehicle.source==src and i.vehicle.destination==dest and i.status!=0):
			vid.append(i.vehicle.id) # removing vehicle he already requested
	now=datetime.datetime.now()
	vehicles2=Vehicle.objects.filter(source=src,destination=dest,seats__gte=s).exclude(id__in=vid)
	# Remove his own vehicles
	for v in vehicles2:
		if v.user.id == request.user.id:
			vid.append(v.id)
	vehicles = Vehicle.objects.filter(source=src,destination=dest,seats__gte=s,date__gte=now).exclude(id__in=vid) # all vehicles which he not requested
	context = {'vehicles':vehicles, 'seats':s}
	return render(request,'carpooling/availablevehicles.html',context)

def makeRequest(request,vehicle_id,seats):
	v = Vehicle.objects.get(id=vehicle_id)
	r=Request.objects.create(user=request.user,vehicle=v,seats=seats,status=1)
	r.save()
	return redirect(viewvehicles)


#####NOTIFICATIONS
def notifications(request):
	# Send him all the info about the person(driver) who accepted it.
	# Send him the option to view driver's current location.
	l1=[]
	l2=[]
	l3=[]
	requests = Request.objects.filter(user = request.user)
	print request.user.username
	print requests
	for r in requests:
		print r.status
		if(r.status == 2):
			l1.append(r)
		elif(r.status == 3):
			l2.append(r)
		else:
			print "Not yet Approved"
	f=find_request.objects.filter(user = request.user, status=1)
	print request.user.username
	for fr in f:
		l3.append(fr)
	print l3
	context = {'accepted': l1, 'rejected': l2, 'location': l3}
	return render(request, 'carpooling/notifications.html', context)

#####VIEW REQUESTS AND ACCEPT OR REJECT
def requests(request):
	req=Request.objects.all()
	re = []
	for r in req:
		if (r.vehicle.user.id == request.user.id and r.status == 1):
			re.append(r)
	context = {'requests':re}
	return render(request, 'carpooling/requests.html', context)
	
def accept(request,request_id):
	r=Request.objects.get(id=request_id)
	r.status=2
	vid=r.vehicle.id
	r.save()
	#Update vehicle seats...
	update_vehicle = Vehicle.objects.get(id=vid)
	update_vehicle.seats -= r.seats
	update_vehicle.save()
	print update_vehicle.name
	r1=Request.objects.get(id=request_id)
	return redirect(requests)
	

def reject(request,request_id):
	r=Request.objects.get(id=request_id)
	r.status=3
	vid=r.vehicle.id
	r.save()
	#Update vehicle seats...
	return redirect(requests)


#####	
def acceptedusers(request):
	v=Vehicle.objects.filter(user=request.user)
	req = Request.objects.filter(status=2, vehicle__in = v)
	#find_request()...get lat and long and send it to form and plot the map if they are not 0...
	#print find_request.objects.all()
	context = {'request':req,'message':""}
	return render(request,'carpooling/acceptedusers.html',context) 

def userlocation(request, user_id):
	U=User.objects.get(id=user_id)
	i=0
	u=find_request.objects.filter(user = U, user_requesting = request.user)

	for q in u:
		i=i+1
	if i == 0:
		v=Vehicle.objects.filter(user=request.user)
		req = Request.objects.filter(status=2, vehicle__in = v)
		print "\nNothing\n"
		context = {'request':req,'message': "User location not shared"}
		return render(request, 'carpooling/acceptedusers.html', context)
	else:
		lat = u[0].latLocation
		lon = u[0].lonLocation
		context={'lat': lat, 'lon': lon}
		print lat, lon
		return render(request, 'carpooling/view_location.html', context)

def requestlocation(request,user_id):
	find_request.objects.create(user_requesting=request.user,user=User.objects.get(id=user_id),status=1)
	return redirect(acceptedusers)

def allowlocation(request, user_id):
	loc_req=find_request.objects.filter(user=request.user, status=1, user_requesting=user_id)
	print request.POST['latitude']
	print request.POST['longitude']	
	for lr in loc_req:
		lr.latLocation = request.POST['latitude']
		lr.lonLocation = request.POST['longitude']
		lr.status=2
		print type(lr.latLocation)
		lr.save()
	return redirect(notifications)
