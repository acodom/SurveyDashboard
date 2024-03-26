from django.test import TestCase
from .models import Question, Choice
from .forms import SurveyForm
from django.urls import reverse
from django.test import Client

class YourAppTestCase(TestCase):
    def setUp(self):
        # Create test data for your models
        self.question_1 = Question.objects.create(question_text="What is your favorite animal?")
        self.question_2 = Question.objects.create(question_text="What is your favorite color?")
        
        # Create choices for the first question
        self.choice_tiger = Choice.objects.create(question=self.question_1, choice_text="Tiger", votes=0)

        # Create choices for the second question
        self.choice_blue = Choice.objects.create(question=self.question_2, choice_text="Blue", votes=0)
        self.choice_red = Choice.objects.create(question=self.question_2, choice_text="Red", votes=0)
        self.choice_red = Choice.objects.create(question=self.question_1, choice_text="Tiger", votes=0)

    def test_model(self):
        # Test your models
        self.assertEqual(self.question_1.question_text, "What is your favorite animal?")
        self.assertEqual(self.question_2.question_text, "What is your favorite color?")


    def test_form(self):
        # Test your forms
        
        # Get choices for the first question
        choices_question_1 = [(choice.id, choice.choice_text) for choice in self.question_1.choice_set.all()]

        # Get choices for the second question
        choices_question_2 = [(choice.id, choice.choice_text) for choice in self.question_2.choice_set.all()]
        
        # Test data for the form
        form_data = {
            'question_1': str(self.question_1.choice_set.first().id),  # Assuming the first choice for question 1 is selected
            'question_2': str(self.choice_blue.id),  # Selecting the Blue choice for question 2
        }
        
        questions_data = {'questions': [self.question_1, self.question_2]}  # Pass the list of Question objects
        
        # Instantiate the SurveyForm with the provided data
        form = SurveyForm(data=form_data, **questions_data)

        # Check if the form is valid
        if not form.is_valid():
            print(form.errors)  # Print out the form errors for debugging

        # Assert that the form is valid
        self.assertTrue(form.is_valid())

    def test_view(self):
        # Test your views
        client = Client()
        
        # Test survey view
        response = client.get(reverse('survey'))
        self.assertEqual(response.status_code, 200)
        
        # Test survey_success view
        response = client.get(reverse('survey_success'))
        self.assertEqual(response.status_code, 200)
