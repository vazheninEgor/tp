from abc import ABC, abstractmethod

# Продукты
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows Button")

class MacButton(Button):
    def render(self):
        print("Rendering Mac Button")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering Windows Checkbox")

class MacCheckbox(Checkbox):
    def render(self):
        print("Rendering Mac Checkbox")

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Клиентский код
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()

# Пример использования
client_code(WindowsFactory())
client_code(MacFactory())