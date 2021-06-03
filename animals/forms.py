from django import forms

class FormGeneralInfo(forms.Form):

	calvedChoices = [('calved','Calved'),('purchased','Purchased')]


    category = forms.CharField(max_length=100,label="Category")
    typeofanimal = forms.CharField(max_length=100,label="Type of animal")
    animaltag = forms. CharField(max_length=100,label="Animal tag/name")
    breed = forms.CharField(max_length=100,label="Breed")
    calved = forms.ChoiceField(choices=calvedChoices, widget=forms.RadioSelect,label="Was the animal calved or purchased")
    

class FormCalved(forms.Form):
    profilepic = forms.FileField(label="Profile picture",required=False)
    

class FormPurchased(forms.Form):
    datepurchased = forms.​DateField(label='What is the date of purchase?', widget=forms.SelectDateWidget)

    buyingprice = MoneyField(
        decimal_places=0,
        default=0,
        default_currency='KE',
        max_digits=11,
        label="Buying price",
    )

    numberofanimals = forms.IntegerField(label="Number of animals bought")

    comments = forms.CharField(widget=forms.Textarea,label="Description")


def if_purchased(self):
	if self.cleaned_data.get('calved',None) == 'purchased'
	   if self.cleaned_data.get('calved',None) is not

	   pass


   