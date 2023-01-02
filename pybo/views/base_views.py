# 기본관리
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


# 질문 목록 화면
def index(request):
    page= request.GET.get('page',1) # 페이지, GET으로 호출 됐을경우, page 디폴트 값이 1 을 의미
    # 질문 목록 출력.
    question_list = Question.objects.order_by('-create_date') # order_by -> 조회 결과를 정렬, '-' 유 : 역방향 정렬/무 : 순방향 정렬
    paginator =  Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) # 요청된 페이지에 해당된 객체
    context = {'question_list': page_obj}
    # render 는 pyhon 데이터를 템플릿에 적용해 HTML로 반환. 'pybo/question_list.html' --> 템플릿 : HTML과 유사하지만 파이썬 데이터를 읽을 수 있는 파일.
    return render(request, 'pybo/question_list.html', context)

# 질문 선택시 화면
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #pk : Question 모델의 기본키
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
