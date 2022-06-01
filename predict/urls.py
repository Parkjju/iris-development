from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "predict"

urlpatterns = [
    path('predict/', views.predict, name='prediction_page'),
    # path('', views.user_create, name='user_create'),
    path('predict/<int:user_id>', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('scatter_plot/', views.view_visual, name='scatter_plot'),
    path('box_plot/', views.view_boxplot, name='box_plot'),
    path('pie_chart/', views.view_piechart, name='pie_chart'),
    path('bar_chart/', views.view_barchart, name='bar_chart'),

    # path('profile/', views.update_profile, name='profile'),
]
