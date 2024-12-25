from abc import ABC, abstractmethod

# Implementor
class ControlSystem(ABC):
    @abstractmethod
    def control(self, vehicle_type, action):
        pass

# ConcreteImplementor
class ManualControl(ControlSystem):
    def control(self, vehicle_type, action):
        print(f"Manually controlling the {vehicle_type} to {action}.")

class AutomaticControl(ControlSystem):
    def control(self, vehicle_type, action):
        print(f"Automatically controlling the {vehicle_type} to {action}.")

# Abstraction
class Vehicle(ABC):
    def __init__(self, control_system):
        self.control_system = control_system

    @abstractmethod
    def operate(self):
        pass

# RefinedAbstraction
class Car(Vehicle):
    def operate(self):
        self.control_system.control("car", "drive forward")

class Train(Vehicle):
    def operate(self):
        self.control_system.control("train", "move along the tracks")

# Usage
if __name__ == "__main__":
    manual_control = ManualControl()
    automatic_control = AutomaticControl()

    manual_car = Car(manual_control)
    automatic_train = Train(automatic_control)

    manual_car.operate()  # Outputs: Manually controlling the car to drive forward.
    automatic_train.operate()  # Outputs: Automatically controlling the train to move along the tracks.
