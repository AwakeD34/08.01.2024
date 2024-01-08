from django.urls import path
from myapp.views import index, itemsid, contact

app_name = 'myapp'

urlpatterns = [
    path('index/', index),
    path('index/<int:my_id>/', itemsid, name='detail'),
    path('contact/', contact)

]
