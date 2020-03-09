from django.urls import path
from .views import (
    homeView, 
    postDetailView,
    hvacView,
    hvacDetailView,
    doorView,
    doorDetailView,
    equipmentView,
    equipmentDetailView,
    metalView,
    metalDetailView,
)


app_name = 'intellect'

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('hvac/', hvacView.as_view(), name='hvac'),
    path('door/', doorView.as_view(), name='door'),
    path('equipment/', equipmentView.as_view(), name='equipment'),
    path('metal/', metalView.as_view(), name='metal'),
    path('metalDetail/<slug>/', metalDetailView.as_view(), name='metalDetail'),
    path('equipmentDetail/<slug>/', equipmentDetailView.as_view(), name='equipmentDetail'),
    path('doorDetail/<slug>/', doorDetailView.as_view(), name='doorDetail'),
    path('product/<slug>/', postDetailView.as_view(), name='product'),
    path('hvacDetail/<slug>/', hvacDetailView.as_view(), name='hvacDetail'),
]