# views.py

from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Question, Choice

def survey_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Save each response to the database
            for question in questions:
                choice_text = form.cleaned_data.get(f'question_{question.id}')
                # Create a Choice object and save it to the database
                Choice.objects.create(question=question, choice_text=choice_text)
            return redirect('survey_success')
    else:
        form = SurveyForm()  # No need to pass questions here since they're not used in the form
    return render(request, 'survey/survey.html', {'form': form})

def survey_success(request):
    return render(request, 'survey/survey_success.html')
