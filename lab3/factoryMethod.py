from abc import ABC, abstractmethod

# Продукт
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Конкретные продукты
class FileLogger(Logger):
    def log(self, message: str):
        print(f"Logging to file: {message}")

class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Logging to console: {message}")

# Создатель
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

# Конкретные создатели
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()

# Пример использования
def client_code(factory: LoggerFactory):
    logger = factory.create_logger()
    logger.log("Factory Method Example")

client_code(FileLoggerFactory())  # Logging to file
client_code(ConsoleLoggerFactory())  # Logging to console