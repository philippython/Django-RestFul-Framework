from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class ViewPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 10


class WatchListPaginatorLO(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10