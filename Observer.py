from abc import ABC, abstractmethod

# Interface
class Observer(ABC):
    @abstractmethod
    def update(self, other):
        pass