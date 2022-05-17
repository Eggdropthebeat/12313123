from rest_framework import serializers
from DATA_APP.models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        field = ('test', 'id')









