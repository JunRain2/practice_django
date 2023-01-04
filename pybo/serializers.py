from rest_framework import serializers
from pybo.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Question
        fields = ['subject', 'content']
        widgets = {
            'subject': serializers.TextInput(attrs={'class': 'form-control'}),
            'content': serializers.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }