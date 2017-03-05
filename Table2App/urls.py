from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Table2App.models import architectures

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=architectures.objects.all(),
                                    template_name="table2/table2.html")),

		url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = architectures,
                                    template_name="table2/detail.html")),
            ]
