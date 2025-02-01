from rest_framework.pagination import LimitOffsetPagination

class NewsPagination(LimitOffsetPagination):
    default_limit = 5  # Number of items per request by default
    max_limit = 20  # Maximum number of items a client can request
    limit_query_param = 'limit'  # Allow clients to set the limit (e.g., ?limit=10)
    offset_query_param = 'offset'  # Allow clients to set the offset (e.g., ?offset=5)
