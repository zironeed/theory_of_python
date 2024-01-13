from django.urls import path
from tester_app.apps import TesterAppConfig
from tester_app.views import QuestionListView

app_name = TesterAppConfig.name


urlpatterns = [
    path('list/', QuestionListView.as_view(), name='question_list'),
]