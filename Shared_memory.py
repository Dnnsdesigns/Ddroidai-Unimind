# shared_memory.py
import redis
import json

class SharedMemory:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def set_data(self, key, value):
        self.r.set(key, json.dumps(value))

    def get_data(self, key):
        data = self.r.get(key)
        return json.loads(data) if data else None

    def append_to_list(self, key, value):
        self.r.rpush(key, json.dumps(value))

    def get_list(self, key):
        return [json.loads(item) for item in self.r.lrange(key, 0, -1)]
