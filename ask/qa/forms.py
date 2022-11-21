from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer

class CreateUser(forms.Form):
    username = forms.CharField(max_length=30, min_length=3)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,min_length=3, max_length=20)

    def save(self):
        user = User.objects.create_user(self.cleaned_data.get('username'), self.cleaned_data.get('email'), self.cleaned_data.get('password'))
        return user



class LoginUser(forms.Form):
    username = forms.CharField(max_length=30, min_length=3)
    password = forms.CharField(widget=forms.PasswordInput,min_length=3, max_length=20)




class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    title.label = 'Заголовок'
    text.label = 'Текст вопроса'
    title.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})

    def clean_title(self):
        data = self.cleaned_data["title"]
        if len(data) == 0:
            raise forms.ValidationError(_('Заголовок не должен быть пустым'), code='invalid')
        return data

    def clean_text(self):
        data = self.cleaned_data["text"]
        if len(data) == 0:
            raise forms.ValidationError(_('Вопрос не должен быть пустым'), code='invalid')
        if data is None:
            raise forms.ValidationError(_('Вопрос не должен быть пустым'), code='invalid')
        return data
    

    def save(self):
        if self._user:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question




class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(min_value=0)
    text.label = 'Текст ответа'
    text.widget.attrs.update({'class': 'form-control'})

    def clean_text(self):
        data = self.cleaned_data["text"]
        if len(data) == 0:
            raise forms.ValidationError(_('Вопрос не должен быть пустым'), code='invalid')
        if data is None:
            raise forms.ValidationError(_('Вопрос не должен быть пустым'), code='invalid')
        return data
    
    def clean_question(self):
        data = self.cleaned_data["question"]
        if not Question.objects.filter(id = data).exists():
            raise forms.ValidationError(_('Вопроса не существует'), code='invalid')        
        return data
    

    def save(self):
        if self._user:
            self.cleaned_data['author'] = self._user
        quest = Question.objects.get(id = self.cleaned_data['question'])
        answer = Answer(text = self.cleaned_data['text'], question = quest, author = self.cleaned_data['author'] )
        answer.save()
        return answer