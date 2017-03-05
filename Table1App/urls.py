from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Table1App.models import fasta

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=fasta.objects.all(),
                                    template_name="table1/table1.html")),

		url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = fasta,
                                    template_name="table1/detail.html")),
            ]
