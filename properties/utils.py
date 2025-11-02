from django.core.cache import cache
from .models import Property


def get_all_properties():
    """Get all properties, caching the queryset in Redis for 1 hour."""
    # Try fetching from cache
    properties = cache.get('all_properties')

    if properties is None:
        print("Cache miss — fetching from database")
        # Fetch from DB if not in cache
        properties = list(Property.objects.values())
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)
    else:
        print("Cache hit — fetched from Redis")

    return properties
