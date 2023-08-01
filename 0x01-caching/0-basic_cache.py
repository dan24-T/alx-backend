#!/usr/bin/python3
"""Basic Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    cache implementaion 
    """
    def put(self, key, item):
        """ Add an item
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get
        """
        return self.cache_data.get(key, None)
