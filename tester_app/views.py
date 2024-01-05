from django.views.generic import DetailView, ListView
from tester_app.models import Question


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question
