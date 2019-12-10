from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и связаны
    темой или концепцией высокого уровня. Продукты одного семейства обычно могут
    взаимодействовать между собой. Семейство продуктов может иметь несколько
    вариаций, но продукты одной вариации несовместимы с продуктами другой.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
    время как внутри метода создается экземпляр конкретного продукта.
    """

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
    Все вариации продукта должны реализовывать этот интерфейс.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Конкретные продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
    друг с другом, но правильное взаимодействие возможно только между продуктами
    одной и той же конкретной вариации.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Продукт B способен работать самостоятельно...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...а также взаимодействовать с Продуктами Б той же вариации.

        Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совместимы.
        """
        pass


"""
Конкретные Продукты создаются соответствующими Конкретными Фабриками.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    Продукт B1 может корректно работать только с Продуктом A1. Тем не менее, он
    принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return "The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        Продукт B2 может корректно работать только с Продуктом A2. Тем не менее,
        он принимает любой экземпляр Абстрактного Продукта А в качестве
        аргумента.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> str:
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    str_return = f"{product_b.useful_function_b()}\n"
    return str_return + f"{product_b.another_useful_function_b(product_a)}\n"


def get_data():
    str_return = "Client: Testing client code with the first factory type:"
    str_return += client_code(ConcreteFactory1()) + '\n'
    str_return += "Client: Testing the same client code with the second factory type:\n"
    return str_return + client_code(ConcreteFactory2()) + '\n'
