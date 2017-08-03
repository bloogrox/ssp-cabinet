from django.conf.urls import url

from .campaign import CampaignList


urlpatterns = [
    url(r'^campaigns/$', CampaignList.as_view()),
]
