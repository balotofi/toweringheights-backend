from django.urls import path
from users.views import dashboard

urlpatterns = [
    path(r"dashboard/", dashboard, name="dashboard"),
]