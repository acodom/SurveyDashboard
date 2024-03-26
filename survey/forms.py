# forms.py

from django import forms
from .models import Question

class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(SurveyForm, self).__init__(*args, **kwargs)
        if questions:
            for question in questions:
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.question_text,
                    choices=[(choice.id, choice.choice_text) for choice in question.choice_set.all()],
                    widget=forms.RadioSelect,
                    required=True
                )