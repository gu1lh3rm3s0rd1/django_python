from django.views.generic import DetailView, ListView

from .models import Dashboard

# Create your views here.

class DashboardListView(ListView):
    model = Dashboard


class DashboardDetailView(DetailView):
    model = Dashboard