from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<page>', views.page),
    path('<category>/<page>', views.products)
    # path('about', views.about),
]