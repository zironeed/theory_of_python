from django.views.generic import DetailView, ListView
from tester_app.models import Question


class MainView(ListView):
    model = Question
    template_name = 'tester_app/main.html'


class QuestionListView(ListView):
    model = Question
    template_name = 'tester_app/question_list.html'


class QuestionDetailView(DetailView):
    model = Question
