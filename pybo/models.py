from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)# 제한된 글자시 CharFiled 사용
    content = models.TextField()# 글자 제한 없을 시 TextFiled() 사용.
    create_date = models.DateTimeField()

    def __str__(self): # Question.objects.all() 에서 제목으로 볼 수 있게해줌.
        return self.subject


class Answer(models.Model):
    #질문에 대한 답변이므로 ForeignKey를 통해 질문과 연결.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE를 통해 질문 삭제시 응답도 삭제.
    content = models.TextField()
    create_date = models.DateTimeField()