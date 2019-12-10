class Target():
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> str:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """
    return target.request()


def get_data():
    str_return = "Client: I can work just fine with the Target objects:"
    target = Target()
    str_return += client_code(target) + '\n'
    adaptee = Adaptee()
    str_return += "Client: The Adaptee class has a weird interface. See, I don't understand it:\n"
    str_return += f"Adaptee: {adaptee.specific_request()}\n\n"

    str_return += "Client: But I can work with it via the Adapter:\n"
    adapter = Adapter(adaptee)
    return str_return + client_code(adapter) + '\n'
