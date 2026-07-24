import threading
import time


class ThreadSafeCacheDemo:
    def __init__(self):
        self._lock = threading.Lock()
        self._cache = {} #key = userid , value =(count, time)

    def run(self):
        print("Starting ThreadSafeCacheDemo...")
        print("Type your name and the cache time to set(seconds) seperated by comma")
        prompt = input()
        data = prompt.split(",")
        name = data[0]
        cache_time = float(data[1])
        self.start_time = time.perf_counter()
        with self._lock:
            self._cache[name] = (0, cache_time)
        print("Cache time set for your user Id")
        print("accessing cache")
        with self._lock:
            if cache_time > (time.perf_counter() - self.start_time):
                print(self._cache[name])
            else:
                print("cache cleared!")
        print("Checking the rate limit which is set to 5 ")
        for i in range(71):
            print(f"making call {i+1} time")
            res = self.ratelimitvalidator(name, i, self._cache[name])
            print(res)


    def ratelimitvalidator(self, user, request_count, value):
        max_count = 5
        with self._lock:
            access_count, ctime = value
            if user in self._cache.keys():
                if ctime > (time.perf_counter() - self.start_time):
                    access_count, ctime = self._cache[user]
                    if access_count < max_count:
                        self._cache[user] = (access_count + 1, ctime)
                        return self._cache[user]
                    else:
                        return "Max requests reached!"
                else:
                    return "Timeout reached!"