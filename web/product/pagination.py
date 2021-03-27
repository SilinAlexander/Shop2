from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'