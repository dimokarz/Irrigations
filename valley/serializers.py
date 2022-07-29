from rest_framework import serializers
from .models import Journal


class JournalSerializer(serializers.ModelSerializer):
    journal_date = serializers.CharField(max_length=30)
    journal_valley = serializers.CharField(max_length=30)

    class Meta:
        model = Journal
        fields = '__all__'
