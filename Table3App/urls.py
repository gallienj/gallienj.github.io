from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Table3App.models import toxin

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=toxin.objects.all(),
                                    template_name="table3/table3.html")),

		url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = toxin,
                                    template_name="table3/detail.html")),
            ]
