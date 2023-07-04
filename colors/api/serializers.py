from rest_framework import serializers

from colors.api.fields import ColorField
from colors.models import ColorBox


class ColorBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorBox
        fields = ["id", "color"]
        read_only_fields = ["id", ]
