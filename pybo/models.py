from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # 사용자 모델, 회원 가입시 데이터 저장에 사용했던 모델.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)# 제한된 글자시 CharFiled 사용
    content = models.TextField()# 글자 제한 없을 시 TextFiled() 사용.
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()

    def __str__(self): # Question.objects.all() 에서 제목으로 볼 수 있게해줌.
        return self.subject


class Answer(models.Model):
    # 무조건 있어야 함으로 강제로 임의값을 주입.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #질문에 대한 답변이므로 ForeignKey를 통해 질문과 연결.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE를 통해 질문 삭제시 응답도 삭제.
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
