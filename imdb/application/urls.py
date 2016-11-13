from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [ 
	url(r'^$',TemplateView.as_view(template_name='signin.html')),
	url(r'^login/$',views.login,name="login"),
	url(r'^savepreference/$',views.savePreferences,name="savePreferences"),
	url(r'^getpref/$',views.getPreferences,name="getpref"),
	url(r'^getallitems/$',views.getItemList,name="getallitems"),
	]
