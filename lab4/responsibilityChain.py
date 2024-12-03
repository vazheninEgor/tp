from abc import ABC, abstractmethod

class RequestHandler(ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next_handler(self, handler):
        self.next_handler = handler
    
    @abstractmethod
    def handle_request(self, request):
        pass

# Обработчик на этапе проверки заявки
class ApplicationCheckHandler(RequestHandler):
    def handle_request(self, request):
        if request.get_stage() == "CHECK":
            print("Checking the application...")
            request.set_stage("ANALYZE")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Обработчик на этапе анализа проблемы
class ProblemAnalysisHandler(RequestHandler):
    def handle_request(self, request):
        if request.get_stage() == "ANALYZE":
            print("Analyzing the problem...")
            request.set_stage("ESTIMATE")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Обработчик на этапе оценки стоимости
class CostEstimationHandler(RequestHandler):
    def handle_request(self, request):
        if request.get_stage() == "ESTIMATE":
            print("Estimating the repair cost...")
            request.set_stage("APPROVE")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Обработчик на этапе утверждения ремонта
class ApprovalHandler(RequestHandler):
    def handle_request(self, request):
        if request.get_stage() == "APPROVE":
            print("Approving the repair request...")
            request.set_stage("COMPLETED")
        elif self.next_handler:
            self.next_handler.handle_request(request)

class Request:
    def __init__(self, stage):
        self.stage = stage
    
    def get_stage(self):
        return self.stage

    def set_stage(self, stage):
        self.stage = stage

if __name__ == "__main__":
    request = Request("CHECK")
    
    # Создание цепочки обработчиков
    handler1 = ApplicationCheckHandler()
    handler2 = ProblemAnalysisHandler()
    handler3 = CostEstimationHandler()
    handler4 = ApprovalHandler()

    handler1.set_next_handler(handler2)
    handler2.set_next_handler(handler3)
    handler3.set_next_handler(handler4)

    # Обработка запроса
    handler1.handle_request(request)