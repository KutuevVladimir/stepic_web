from django.core.paginator import Paginator, EmptyPage
from django.http.response import Http404


def paginate(request, objects):
    # try:
    #     limit = int(request.GET.get('limit', 10))
    # except ValueError:
    #     limit = 10
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(objects, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return {'paginator': paginator,
            'page': page}
