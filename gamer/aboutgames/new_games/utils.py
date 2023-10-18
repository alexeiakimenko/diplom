from django.core.paginator import Paginator


def page_list(request, object_list, page):
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get('page', int(page))
    return paginator, page_number


def calculate_rating(sum_evaluations, length_evaluations):
    rating = round(float(sum_evaluations / length_evaluations), 2)
    return rating
