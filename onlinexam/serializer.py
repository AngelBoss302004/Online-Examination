from rest_framework import serializers
from onlinexam.models import QuestionDb


class OnlineExaminationSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionDb
        fields='__all__'
    