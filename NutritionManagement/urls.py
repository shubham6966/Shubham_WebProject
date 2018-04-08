from django.conf.urls import url
from . import views
app_name = 'NutritionManagement'
urlpatterns = [
    url(r'^breakfast/$',views.breakfast,name="breakfast"),
    url(r'^nutrientsInBreakfast',views.NutrientsCalc,name="NutrientsCalc"),
    url(r'^update/([0-9]+)/$', views.breakfast_edit, name="breakfast_edit"),
    url(r'^delete/([0-9]+)/$',views.breakfast_delete,name="breakfast_delete")
]