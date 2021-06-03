from django.shortcuts import render,redirect

from .models import Animal

# Create your views here.
def addanimal(request,farm_id):
	if request.method == 'POST':
		date_Of_Purchase = request.POST['dop']
		category = request.POST['category']
		animaltype = request.POST['animaltype']
		breed = request.POST['breed']
		number = request.POST['number']
		calved = request.POST['calved']
		buyingprice = request.POST['buyingprice']
		currency = request.POST['currency']
		description = request.POST['description']
		profilepic = request.POST['profilepic']
		Email_Address = request.POST['useremail']
		Farm_name = request.POST['farm_id']

		addanimal = Animal()
		addanimal.save()

		return redirect('/dashboard/') 
	else:

		land = request.GET.get('farm_id')
		context = {"choose_farm":farm_id}
		return render(request, 'addanimal.html',context)


def insertanimal(request):
	date_Of_Purchase = request.POST['dop']
	category = request.POST['category']
	animaltype = request.POST['animaltype']
	breed = request.POST['breed']
	number = request.POST['number']
	calved = request.POST['calved']
	buyingprice = request.POST['buyingprice']
	currency = request.POST['currency']
	description = request.POST['description']
	profilepic = request.POST['profilepic']
	Email_Address = request.POST['useremail']
	Farm_name = request.POST['farm_id']

	addanimal = Animal()
	addanimal.date_Of_Purchase = date_Of_Purchase
	addanimal.category = category
	addanimal.animaltype = animaltype
	addanimal.breed = breed
	addanimal.number = number
	addanimal.calved = calved
	addanimal.buyingprice = buyingprice
	addanimal.currency = currency
	addanimal.description = description
	addanimal.profilepic = profilepic
	addanimal.Email_Address = Email_Address
	addanimal.Farm_Name = Farm_name

	addanimal.save()

	return redirect('/animaloptions/'+Farm_name) 




def animaloptions(request,farm_id):
	land = request.GET.get('farm_id')
	request.session['farmname'] = farm_id
	context = {"choose_farm":farm_id}
	return render(request,'animaloptions.html',context)
	

def listanimal(request):
	datalist = Animal.objects.filter(Farm_Name=request.session['farmname'])
	choose_animals = {
	"animaltype":datalist
	}
	return render(request,'listanimal.html',choose_animals)
