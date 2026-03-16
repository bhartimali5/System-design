class DBConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


### Mutlithreading example: If multiple threads check for instance at the same time, they might create multiple instances. 
# To prevent this, we can use a lock. But this can reduce the performance due to locking overhead, 
# so we can use double-checked locking to minimize the locking overhead.
import threading

class ThreadSafeDBConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    


## Double-checked locking example
class DoubleCheckedDBConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:    ## First check without locking for better performance
            with cls._lock:          ## For the first time only lock is acquired, subsequent calls will skip the lock and return the instance directly
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
