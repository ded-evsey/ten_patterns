from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    Интферфейс издателя объявляет набор методов для управлениями подпискичами.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class ConcreteSubject(Subject):
    """
    Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
    изменениях.
    """

    _state: int = None
    """
    Для удобства в этой переменной хранится состояние Издателя, необходимое всем
    подписчикам.
    """

    _observers: List[Observer] = []
    """
    Список подписчиков. В реальной жизни список подписчиков может храниться в
    более подробном виде (классифицируется по типу события и т.д.)
    """

    def attach(self, observer: Observer) -> str:
        self._observers.append(observer)
        return "Subject: Attached an observer.\n"

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Методы управления подпиской.
    """

    def notify(self) -> str:
        """
        Запуск обновления в каждом подписчике.
        """

        for observer in self._observers:
            observer.update(self)
        return "Subject: Notifying observers...\n"

    def some_business_logic(self) -> str:
        """
        Обычно логика подписки – только часть того, что делает Издатель.
        Издатели часто содержат некоторую важную бизнес-логику, которая
        запускает метод уведомления всякий раз, когда должно произойти что-то
        важное (или после этого).
        """

        self._state = randrange(0, 10)
        self.notify()
        return "\nSubject: I'm doing something important.\n"+f"Subject: My state has just changed to: {self._state}"


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Получить обновление от субъекта.
        """
        pass


"""
Конкретные Наблюдатели реагируют на обновления, выпущенные Издателем, к которому
они прикреплены.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> str:
        if subject._state < 3:
            return "ConcreteObserverA: Reacted to the event"


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> str:
        if subject._state == 0 or subject._state >= 2:
            return "ConcreteObserverB: Reacted to the event"


def get_data():
    # Клиентский код.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    str_return = subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    str_return += subject.attach(observer_b)

    str_return += subject.some_business_logic()
    str_return += subject.some_business_logic()

    subject.detach(observer_a)

    str_return += subject.some_business_logic()
    return str_return
