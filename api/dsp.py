from rest_framework import serializers

from campaigns.models import Dsp


class DspSerializer(serializers.ModelSerializer):

    ext_fields = serializers.StringRelatedField(many=True)

    class Meta:
        model = Dsp
        fields = ('id', 'name', 'bid_url', 'active', 'ext_fields')
