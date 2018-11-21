from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [

	# dashboard/
	url(r'^$', views.IndexView.as_view(), name='index'),

]