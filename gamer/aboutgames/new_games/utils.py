from django.core.paginator import Paginator


def page_list(request, object_list, page):
    paginator = Paginator(object_list, 2)
    page_number = request.GET.get('page', int(page))
    return paginator, page_number


def calculate_rating(summa, sum_len):
    rating = round(float(summa / sum_len), 2)
    return rating
