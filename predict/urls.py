from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('scatter_plot/', views.view_visual, name='scatter_plot'),
    path('box_plot/', views.view_boxplot, name='box_plot'),

]
