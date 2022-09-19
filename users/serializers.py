from .models import Vendor, Consumer
from rest_framework import serializers


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"

    # def validate(self, value):
    #     if not value.endswith('@fastapp.com'):
    #         raise serializers.ValidationError("Email must andswith @fastapp,com")
        
    #     return value


class ConsumerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = "__all__"

    def validate(self, attrs):
        nm = attrs.get("name")
        ag = attrs.get("age")

        if len(nm) <= 4:
            raise serializers.ValidationError(f"{nm} must more then 4 character")
        
        if not ag > 18:
            raise serializers.ValidationError(f"{ag} age not allowed, Only above 18+")

        return attrs