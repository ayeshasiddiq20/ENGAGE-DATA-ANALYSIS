from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    
    path('gen_hist', views.gen_hist, name="gen_hist"),
    path('gen_val_counts', views.gen_val_counts, name="gen_val_counts"),
    path('gen_top_ten', views.gen_top_ten, name="gen_top_ten"),
    path('gen_year_plot', views.gen_year_plot, name="gen_year_plot"),
    path('gen_fuel_type', views.gen_fuel_type, name="gen_fuel_type"),
    path('gen_scatter', views.gen_scatter, name="gen_scatter"),
    path('gen_violin', views.gen_violin, name="gen_violin"),
    path('gen_cat', views.gen_cat, name="gen_cat"),
    path('gen_diesel_car', views.gen_diesel_car, name="gen_diesel_car"),
    path('gen_suv_year', views.gen_suv_year, name="gen_suv_year"),
    path('gen_brand_car', views.gen_brand_car, name="gen_brand_car"),
    path('gen_heat_map', views.gen_heat_map, name="gen_heat_map"),

] 
