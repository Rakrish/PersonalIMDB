from django.shortcuts import render
from application.models import User
from application.models import UserPreference
from application.models import Items
from application.models import Subscribers
# Create your views here.

def login(request):
	subscribed_list=[]
	if request.method == 'POST':
		data=request.POST
		name=data["name"]
		email=data["email"]
		request.session['email']=email
		qset=Q()
		qset = Q(email__icontains=email)
		user=User.objects.get(qset)
		if user and request.session['email']==email:
			qset1 = Q(useridid_id_icontains=user.id)
			isSubscriber=Subscribers.objects.filter(qset1)
			if isSubscriber:
				sub=name+'_list.html'	
				itemlist=isSubscriber.values_list("item_id",flat=True)	
				for j in itemlist:
					qset2 = Q(id__icontains=j)
					items=Items.objects.get(qset2)
					subscribed_list.append(items)
				return render(request, sub, {"sublist":subscribed_list})						
			else:
				return render(request, 'pref_form.html', {"name":name});
		
def savePreferences(request):
	#TODO
	#Save preferences for a particular user
	pass

def getPreferences(request):
	#TODO
	#View preferences for a particular user
	pass

def getItemList(request):
	#Get all item list
	#TODO
	pass

def getItemDetails(request):
	#Get particular item details
	#TODO
	pass

def unsubscribe(request):
	#TODO
	#Unsubscribe list of shows for the user
	pass

def subscribe(request):
	#TODO
	#Subscribe list of shows for the user
	pass

def home(request):
	#TODO
	#View subscribed details
	pass
			
