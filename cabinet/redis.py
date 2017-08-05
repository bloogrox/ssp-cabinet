import redis

from django.conf import settings


REDIS_POOL = redis.ConnectionPool.from_url(settings.REDIS_URI)
