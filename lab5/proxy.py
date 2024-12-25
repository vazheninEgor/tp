from abc import ABC, abstractmethod

# Subject
class APIService(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

# RealSubject
class RealAPIService(APIService):
    def fetch_data(self):
        print("Fetching data from the real API...")
        return {"data": "Real API data"}

# Proxy
class CachedAPIService(APIService):
    def __init__(self):
        self._real_service = RealAPIService()
        self._cache = None

    def fetch_data(self):
        if self._cache is None:
            print("Cache is empty. Fetching from real service...")
            self._cache = self._real_service.fetch_data()
        else:
            print("Returning data from cache.")
        return self._cache

# Usage
if __name__ == "__main__":
    service = CachedAPIService()
    print(service.fetch_data())  # Fetches from real service
    print(service.fetch_data())  # Fetches from cache