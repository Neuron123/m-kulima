from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from .models import Hasianda

# Create your views here.
def homepage(request):
	return render(request, 'home.html')


def register(request):
	if request.method == 'POST':

	   		username = request.POST['uname']
	   		email = request.POST['email']
	   		passw = request.POST['pass']
	   		cpassw = request.POST['pass2']

	   		if passw == cpassw:

	   			user = User.objects.create_user(username=username,password=passw,email=email)
	   			user.save()
	   			print('User created')

	   			user = auth.authenticate(request,username=username,password=passw)

	   			if user is not None:
	   				auth.login(request,user)
	   				return redirect('/dashboard')
	   		else:
	   			return redirect('/register')

	else:
	   return render(request, 'register.html')


def login(request):
	if request.method == 'POST':
			username = request.POST['uname']
			passw = request.POST['pass']

			user = auth.authenticate(request,username=username,password=passw)
			if user is not None:
				auth.login(request,user)
				#if request.user.is_authenticated():
				#username = request.user.username
				return redirect('/dashboard/')
			else:
				return redirect('/login')

	else:

		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/login/')

def dashboard(request):
	num_farms = Hasianda.objects.filter(user_id=request.user).count()

	choose_farm = Hasianda.objects.filter(user_id=request.user).values_list("Farm_Name", flat=True)

	context = {"num_farms": num_farms,"choose_farm":choose_farm}
	return render(request,'index.html',  context)



def addfarm(request):
	if request.method == 'POST':
		Farm_Name = request.POST['farmname']
		County = request.POST['county']
		Address = request.POST['address']
		Size = request.POST['size']
		Description = request.POST['description']
		Email_Address = request.POST['useremail']

		addfarm = Hasianda()
		addfarm.Farm_Name = Farm_Name
		addfarm.County = County
		addfarm.Address = Address
		addfarm.Size = Size
		addfarm.Description = Description
		addfarm.Email_Address = Email_Address
		addfarm.save()
		request.user.farmlist.add(addfarm)
		return redirect('/dashboard/') 
	else:
		return render(request, 'addfarm.html')

def options(request):
	return render(request,'options.html')


def listfarm(request):	
	
	return render(request,'list.html', {})

def choosefarm(request):
	

	choose_farm = Hasianda.objects.filter(user_id=request.user).values_list("Farm_Name", flat=True)
	
	return render(request, 'index.html',{'choose_farm':choose_farm})
	

