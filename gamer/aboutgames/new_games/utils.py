from django.core.paginator import Paginator


def page_list(request, object_list):
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get('page', 1)
    return paginator, page_number
