from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def move(self):
        pass

a = Animal()