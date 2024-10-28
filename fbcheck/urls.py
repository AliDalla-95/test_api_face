from django.urls import path
from .views import check_user_membership

urlpatterns = [
    path('check_membership/', check_user_membership, name='check_membership'),
]
