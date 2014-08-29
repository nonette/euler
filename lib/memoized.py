
def memoized(f):
    cache = {}
    def cachedf(*args):
        if args not in cache:
            cache[args]=f(*args)
        return cache[args]
    return cachedf

