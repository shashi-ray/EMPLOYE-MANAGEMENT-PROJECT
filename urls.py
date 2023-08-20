from django.contrib import admin
from django.urls import path
from .views import UPDATE_EMPLOYE,HOME_VIEW,ABOUT_VIEW,CONTACT_VIEW,VIEW_ALL,ADD_EMPLOYE,UPDATE_EMP,REMOVE_EMP,FILTER_EMP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HOME_VIEW,name='home'),
    path('about/',ABOUT_VIEW,name='about'),
    path('contact/',CONTACT_VIEW,name='contact'),
    path('view_all/',VIEW_ALL,name='view_all'),
    path('add_emp/',ADD_EMPLOYE,name='add_employe'),
    path('update_emp/<int:id>/',UPDATE_EMP,name='update_employe'),
    path('update_employe/<int:id>/',UPDATE_EMPLOYE,name='update_employe'),
    path('remove_emp/',REMOVE_EMP,name='remove_employe'),
    path('remove_emp/<int:id>/',REMOVE_EMP,name='remove_employe'),
    path('filter_emp/',FILTER_EMP,name='filter_employe'),

























































]
