from django import forms
from translate.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['email', 'title', 'file', 'check1', 'check2']
        labels = {
            'email': '이메일',
            'title': '게임 타이틀',
            'file': '번역파일',
            'check1': '개인정보 수집 및 이용 동의',
            'check2': '이벤트 등 프로모션 알림 수신 동의',
        }
