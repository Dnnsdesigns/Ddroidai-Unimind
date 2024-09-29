# subordinate_agents/memory_agent.py
from shared_memory import SharedMemory

class MemoryAgent:
    def __init__(self):
        self.memory = SharedMemory()

    def store(self, key, value):
        self.memory.set_data(key, value)

    def retrieve(self, key):
        return self.memory.get_data(key)
