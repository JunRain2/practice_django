from django.urls import path

from . import views

# 서로 다른 앱 동일한 별칭 사용시 중복을 방지하기 위함.
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'), # path에 'pybo/'가 생략된 것.
    path('<int:question_id>/', views.detail, name='detail'), # 질문 링크를 타면 들어가는 링크.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), #답변 등록
    path('question/create/', views.question_create, name='question_create'), #질문 등록
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), # 질문 변경
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문 삭제
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'), # 답변 변경
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'), # 답변 삭제
]

# name : 수정될 수 있는 url 하드코딩을 별칭을 부여.