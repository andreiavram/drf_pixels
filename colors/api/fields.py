from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers


@extend_schema_field(OpenApiTypes.OBJECT)
class ColorField(serializers.Field):
    def to_representation(self, instance):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(instance[i:i + 2], 16)
            rgb.append(decimal)

        representation = {
            "red": rgb[0],
            "green": rgb[1],
            "blue": rgb[2],
        }
        return representation

    def to_internal_value(self, data):
        return '{:02x}{:02x}{:02x}'.format(data['red'], data['green'], data['blue'])

