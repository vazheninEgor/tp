# Интерфейс обработчика
class Handler(ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next_handler(self, handler):
        self.next_handler = handler
    
    @abstractmethod
    def handle_request(self, request):
        pass

# Конкретный обработчик A
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request.get_type() == "TYPE_A":
            print("ConcreteHandlerA handled the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Конкретный обработчик B
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request.get_type() == "TYPE_B":
            print("ConcreteHandlerB handled the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Запрос
class Request:
    def __init__(self, req_type):
        self.req_type = req_type
    
    def get_type(self):
        return self.req_type

# Пример использования
if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    handler_a.set_next_handler(handler_b)

    request_a = Request("TYPE_A")
    request_b = Request("TYPE_B")

    handler_a.handle_request(request_a)
    handler_a.handle_request(request_b)