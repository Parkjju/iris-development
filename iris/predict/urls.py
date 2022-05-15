
from django.urls import path
from . import views

app_name = 'preict'

urlpatterns = [
    path('', views.predict, name='predict'),
    path('predict/', view.predict_chances, name='submit_prediction'),
]