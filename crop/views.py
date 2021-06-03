from django.shortcuts import render, redirect
from .models import Crop

# Create your views here.

def addcrop(request,farm_id):
	if request.method == 'POST':
		Crop_Name = request.POST['cropname']
		Crop_Variety = request.POST['variety']
		Date_Of_Planting = request.POST['dop']
		Expected_Date_of_Havest = request.POST['edoh']
		Quantity_Of_Seeds = request.POST['qos']
		Cost_Of_Seeds = request.POST['price']
		Description = request.POST['description']
		Email_Address = request.POST['useremail']
		Farm_name = request.POST['farm_id']

		addcrop = Crop()

		addcrop.save()
		
		return redirect('/dashboard/') 
	else:

		land = request.GET.get('farm_id')
		context = {"choose_farm":farm_id}
		return render(request, 'addcrop.html',context)
	#return render(request, 'addcrop.html')

def insertcrop(request):

	Crop_Name = request.POST['cropname']
	Crop_Variety = request.POST['variety']
	Date_Of_Planting = request.POST['dop']
	Expected_Date_of_Havest = request.POST['edoh']
	Quantity_Of_Seeds = request.POST['qos']
	Cost_Of_Seeds = request.POST['price']
	Description = request.POST['description']
	Email_Address = request.POST['useremail']
	Farm_name = request.POST['farm_id']

	#set session
	#request.session['farmname'] = Farm_name

	addcrop = Crop()
	addcrop.Crop_Name = Crop_Name
	addcrop.Crop_Variety = Crop_Variety
	addcrop.Date_Of_Planting = Date_Of_Planting
	addcrop.Expected_Date_of_Havest = Expected_Date_of_Havest
	addcrop.Quantity_Of_Seeds = Quantity_Of_Seeds
	addcrop.Cost_Of_Seeds = Cost_Of_Seeds
	addcrop.Description = Description
	addcrop.Email_Address = Email_Address
	addcrop.Farm_name = Farm_name
	
	addcrop.save()
	
	
	

	return redirect('/cropoptions/'+Farm_name) 


def cropoptions(request,farm_id):
	land = request.GET.get('farm_id')
	request.session['farmname'] = farm_id
	context = {"choose_farm":farm_id}
	return render(request,'cropoptions.html',context)


def listcrop(request):
	
	data = Crop.objects.filter(Farm_name=request.session['farmname'])
	choose_crops = {
    "Crop_Name": data
}

	return render(request,"listcrop.html", choose_crops)

	