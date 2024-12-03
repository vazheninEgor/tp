from abc import ABC, abstractmethod

# Интерфейс для продукта (уведомление)
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Конкретный продукт: SMS уведомление
class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Отправка SMS: {message}")

# Конкретный продукт: Email уведомление
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Отправка Email: {message}")

# Фабрика уведомлений
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

# Фабрика для SMS уведомлений
class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

# Фабрика для Email уведомлений
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

# Клиентский код
def send_notification(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    notification.send(message)

# Использование
send_notification(SMSNotificationFactory(), "Это тестовое SMS сообщение.")
send_notification(EmailNotificationFactory(), "Это тестовое Email сообщение.")