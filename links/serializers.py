from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)

    class Meta:
        model = Link
        fields = ["url_address", "key"]
