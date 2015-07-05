class Memcache:
    def __init__(self):
        self.CACHE = {} # empty dict for Cache

    def set(self, key, value):
        self.CACHE[key] = value
        return True

    def get(self, key):
        return self.CACHE.get(key)

    def delete(self, key):
        del self.CACHE[key]
        return True

    def flush(self):
        self.CACHE.clear()

def test_memcache():
    m = Memcache()
    print(m.set('a', '1'))
    print(m.set('b', '2'))
    print(m.CACHE)
    print(m.get('b'))
    print(m.get('d'))
    m.delete('b')
    print(m.CACHE)
    m.flush()
    print(m.CACHE)

if __name__ == '__main__':
    test_memcache()


