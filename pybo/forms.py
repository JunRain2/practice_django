''' 페이지 요청시 전달되는 피라미터들을 쉽게 관리하기위한 클래스,
필수 파라미터의 값이 누락되지 않았는지, 파라미터의 형식은 적절한지 등을 검증할 목적으로 사용,
HTML을 자동으로 생성하거나 폼에 연결된 모델을 이용하여 데이터를 저장하는 기능'''

from django import forms
from pybo.models import Question, Answer

# form.ModelForm, form.Form 존재
# forms.ModelForm : 모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할수 있는 폼
class QuestionForm(forms.ModelForm):
    class Meta: # Meta 클래스 반드시 필요/ 사용할 모델, 모델의 속성을 명시.
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
