# 질문 관리
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from pybo.forms import QuestionForm
from pybo.models import Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST': # POST시 실행
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # commit=False => 임시저장
            question.author = request.user # author 속성에 로그인 계정 저장.
            question.create_date=timezone.now()
            question.save()
            return redirect('pybo:index')
    else: # GET일떄 실행
        form = QuestionForm
    context = {'form': form}
    return render(request,'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request,'수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST" :
        form = QuestionForm(request.POST, instance=question) # instance 기준으로 수정해 POST로 덮어 씌움.
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date=timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else :
        form = QuestionForm(instance=question) # 폼의 속성이 instance 값으로 채워짐
    context={'form':form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')