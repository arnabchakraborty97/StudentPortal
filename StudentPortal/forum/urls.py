from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [

	# forum/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# forum/posts
	url(r'^posts/$', views.IndexView.as_view(), name='index'),

	# posts/72
	url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetailView.as_view(), name='post-detail'),

	# posts/create
	url(r'^posts/create$', views.PostCreateView.as_view(), name='post-create'),

	# posts/edit/74
	url(r'^posts/edit/(?P<pk>[0-9]+)$', views.PostUpdateView.as_view(), name='post-update'),

	# posts/delete/74
	url(r'^posts/delete/(?P<pk>[0-9]+)$', views.PostDeleteView.as_view(), name='post-delete'),

]