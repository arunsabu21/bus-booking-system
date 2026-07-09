from django.core.cache import cache

def get_cache(key):
    return cache.get(key)


def set_cache(key, value, timeout):
    cache.set(
        key=key,
        value=value,
        timeout=timeout,
    )


def delete_cache(key):
    cache.delete(key)