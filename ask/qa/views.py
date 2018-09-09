from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_GET

from qa.model_func import paginate
from qa.models import Question, Answer


@require_GET
def main(request):
    questions = Question.objects.new()[:]
    paginator = paginate(request, questions)
    page = paginator['page']
    paginator = paginator['paginator']
    paginator.baseurl = reverse('main-page')
    return render(request, 'main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


@require_GET
def popular(request):
    questions = Question.objects.popular()[:]
    paginator = paginate(request, questions)
    page = paginator['page']
    paginator = paginator['paginator']
    paginator.baseurl = reverse('popular-questions')
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


@require_GET
def question_by_id(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)[:]
    # try:
    #     pass
    # except Answer.DoesNotExist:
    #     answers = None
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })

