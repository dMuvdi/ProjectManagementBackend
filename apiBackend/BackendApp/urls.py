from django.urls import re_path as url
from django.urls import path as url2
from BackendApp import views
from .views import StatesView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^project/$', views.projectApi), #returns all projects
    url(r'^project/([0-9]+)$', views.projectApi), #works for the put and delete methods
    url(r'^project/savefile',views.SaveFile), #saves the project photo
    url2('project/<str:searchTitle>', views.projectSearch), #returns the search passing a string

    url(r'^user$',views.userApi), #returns all users
    url(r'^user/([0-9]+)$',views.userApi), #works for the put and delete methods
    url(r'^user/active',views.userApi), #returns the active user
    url2('user/myproject/<int:id>', views.userMyProject), #returns the project info related to that user
    url2('user/<str:email>/<str:password>', views.userLogIn), #updates user active field to true
    url2('user/<str:email>', views.userLogOff), #updates user active field to false
    

    url(r'state/(?P<pk>[0-9]+)/$', StatesView.as_view(), name="StatesView"), #returns the state json


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)