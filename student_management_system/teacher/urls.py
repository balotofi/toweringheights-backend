from django.conf.urls import url
from teacher.views import dashboard

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
]