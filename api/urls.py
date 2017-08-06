from django.conf.urls import url

from .campaign import CampaignList
from .general import general


urlpatterns = [
    url(r'^campaigns/$', CampaignList.as_view()),
    url(r'^general/$', general),
]
