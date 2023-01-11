from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Activity
        fields = ('id', 'activity', 'type', 'participants', 'price', 'link', 'key', 'accessibility', 'done', 'user')