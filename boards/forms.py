from django import forms
from boards.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['title', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # } 
        labels = {
            'title': '제목',
            'content': '내용',
        } 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 사용할 모델
        fields = ['content']
        labels = {
            'content': '댓글',
        }   