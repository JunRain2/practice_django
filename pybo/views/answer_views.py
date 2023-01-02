from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone

from pybo.forms import AnswerForm
from pybo.models import Answer, Question


@login_required(login_url='common:login') # 로그인이 필요한 함수를 의미., 로그아웃시 자동으로 로그인 페이지로 이동.
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id
            ))# 앵커를 포함, resolbe_url => 실제로 호출되는 URL 문자열을 리턴하는 장고함수.
    else:
        # 답변등록 URL인 /answer/create가 GET 방식으로 호출 --> HttpResponseNotAllowed의 405 오류 발생 --> 따라서 그냥 AnswerForm으로 이동하게 수정.
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error('수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method ==  "POST" :
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
              resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else :
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form':form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error('삭제권한이 없습니다')
    else :
        answer.delete()
    return redirect('{}#answer_{}'.format(
        resolve_url('pybo:detail', question_id = answer.question.id), answer.id))