from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.DashboardListView.as_view(), name='List'),
    path('', views.DashboardDetailView.as_view(), name='Detail'),
]