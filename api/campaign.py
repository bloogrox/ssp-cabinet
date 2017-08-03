from rest_framework import mixins
from rest_framework import generics
from rest_framework import serializers

from campaigns.models import Campaign, CampaignFilter


class CampaignFilterSerializer(serializers.ModelSerializer):

    field = serializers.StringRelatedField()
    values = serializers.ListField(source='value_as_list', read_only=True)

    class Meta:
        model = CampaignFilter
        fields = ('field', 'values')


class CampaignSerializer(serializers.ModelSerializer):

    targetings = CampaignFilterSerializer(
        source='get_targetings',
        many=True,
        read_only=True
    )

    class Meta:
        model = Campaign
        fields = ('id', 'name', 'targetings')


class CampaignList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Campaign.objects.filter(active=True)
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
