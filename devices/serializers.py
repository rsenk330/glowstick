from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    id = serializers.Field()
    ip = serializers.Field()
    copyright = serializers.Field()
    features = serializers.Field()
    hw_model = serializers.Field(source="hwmodel")
    model = serializers.Field()
    tuner_count = serializers.Field()
    version = serializers.Field()
