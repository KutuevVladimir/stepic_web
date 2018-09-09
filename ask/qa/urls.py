from django.conf.urls import url
from qa.views import main, question_by_id
from qa.views import popular

urlpatterns = [
    url(r'^$', main, name='main-page'),
    url(r'^popular/$', popular, name='popular-questions'),
    url(r'question/(?P<id>\d+)/', question_by_id, name='question')
]