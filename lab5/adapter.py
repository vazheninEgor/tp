from abc import ABC, abstractmethod

# Target
class KeyboardInput(ABC):
    @abstractmethod
    def read_input(self):
        pass

# Adaptee
class USBKeyboard:
    def get_key_press(self):
        return "Key pressed: A"

# Adapter
class USBKeyboardAdapter(KeyboardInput):
    def __init__(self, usb_keyboard):
        self.usb_keyboard = usb_keyboard

    def read_input(self):
        return self.usb_keyboard.get_key_press()

# Usage
if __name__ == "__main__":
    usb_keyboard = USBKeyboard()
    adapter = USBKeyboardAdapter(usb_keyboard)
    print(adapter.read_input())  # Outputs: Key pressed: A