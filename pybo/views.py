from django.shortcuts import render

# 제네릭 뷰 : 늘 비슷한 내용을 패턴화 해서 보여주는것 --> 여기서 사용 X
# 링크타고 들어와서 띄울 창을 모아두는 함수들.
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed


# 질문 목록 화면
def index(request):
    # 질문 목록 출력.
    question_list = Question.objects.order_by('-create_date') # order_by -> 조회 결과를 정렬, '-' 유 : 역방향 정렬/무 : 순방향 정렬
    context = {'question_list':question_list}
    # render 는 pyhon 데이터를 템플릿에 적용해 HTML로 반환. 'pybo/question_list.html' --> 템플릿 : HTML과 유사하지만 파이썬 데이터를 읽을 수 있는 파일.
    return render(request, 'pybo/question_list.html', context)

# 질문 선택시 화면
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #pk : Question 모델의 기본키
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

# 질문 추가 함수
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST': # POST시 실행
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # commit=False => 임시저장
            question.create_date=timezone.now()
            question.save()
            return redirect('pybo:index')
    else: # GET일떄 실행
        form = QuestionForm
    context = {'form': form}
    return render(request,'pybo/question_form.html', context)



