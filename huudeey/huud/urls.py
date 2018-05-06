
from django.urls import path
from django.conf.urls import url
from . import views
from . models import Prodsale


urlpatterns = [
    path('', views.index, name='index'),
    path('sales/', views.ProdsaleListView.as_view(model=Prodsale), name='sales'),
    path('saledate/', views.prodsale, name='saledate'),
    url(r'^results/(?P<content_all>.+)/', views.results, name='results'),
    path('searchdatesale/', views.searchdatesale, name='searchdatesale'),
<<<<<<< HEAD
    url(r'^searchdresults/(?P<b_result>.+)/(?P<e_result>.+)/', views.searchdresults, name='searchdresults'),
    path('searchcost/', views.searchcost, name='searchcost'),
    url(r'^costresults/(?P<b_result>.+)/', views.costresults, name='costresults'),


=======
    url(r'^searchdresults/(?P<b_result>.+)/', views.searchdresults, name='searchdresults'),
>>>>>>> 216a4bb38ccbaad1f656463f8a37f6a95f916389
]
