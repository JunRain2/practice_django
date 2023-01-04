# Create your models here.
from djongo import models
from django.contrib.auth.models import User # 사용자 모델, 회원 가입시 데이터 저장에 사용했던 모델.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)# 제한된 글자시 CharFiled 사용
    content = models.TextField()# 글자 제한 없을 시 TextFiled() 사용.
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 추가, User를 둘다 사용함으로 User모델로 접근할 때 author 기준인지 voter 기준인지 모호해짐 -->related_name 인수 추가
    # ManyToMany 함수가 같은 사용자가 같은 게시물에 많은 추천을 누를 시 오류도 발생하지 않고, 추가도 되지않게 한다.
    def __str__(self): # Question.objects.all() 에서 제목으로 볼 수 있게해줌.
        return self.subject


class Answer(models.Model):
    # 무조건 있어야 함으로 강제로 임의값을 주입.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    #질문에 대한 답변이므로 ForeignKey를 통해 질문과 연결.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE를 통해 질문 삭제시 응답도 삭제.
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name = 'voter_answer')

