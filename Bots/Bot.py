from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

<<<<<<< HEAD
    def __init__(self,nome):
=======
    def __init__(self,nome):
>>>>>>> 2de4ee66feb7d098367a46f27c5d9bcca5b568f4
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    @abstractmethod
    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass