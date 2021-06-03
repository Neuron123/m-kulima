from django.shortcuts import render
from hasianda.models import Hasianda
from crop.models import Crop
from django.contrib.auth.models import User
from .fusioncharts import FusionCharts
from django.http import HttpResponse

# Create your views here.

def reports(request):
	dataSource = {}
	dataSource['chart']={
	"caption":"Farm name Details",
	"theme":"ocean",
	"numberSuffix":"ha",
	"subCaption":"Farm name vs Farm size"

	}

	dataSource['data']=[]

	data = Hasianda.objects.filter(user_id=request.user)

	for Farmreport in data:
		data = {}
		data['label'] = Farmreport.Farm_Name
		data['value'] = Farmreport.Size
		dataSource['data'].append(data)

	cropdataSource = {}
	cropdataSource['chart'] = {

	"caption":"Crop details",
	"theme":"ocean",
	"subCaption":"Crops details of various farms"
	}
	cropdataSource['data']=[]

	cropdata = Crop.objects.filter(Farm_name="Mars")

	for Cropreport in Crop.objects.raw('SELECT * FROM crop_crop WHERE Email_Address = "brike@yahoo.com"'):
		data = {}
		data['label'] = Cropreport.Farm_name
		data['value'] = Cropreport.Crop_Name
		cropdataSource['data'].append(data)

	
	chart1 = FusionCharts("column2d","ex1","800","500","chart-1","json",dataSource)

	cropchart = FusionCharts("column2d","ex2","800","500","chart-2","json",cropdataSource)



	# returning complete JavaScript and HTML code, 
	# which is used to generate chart in the browsers.
	return  render(request, 'reports.html', {'output' : chart1.render(),'output_2' : cropchart.render()})

