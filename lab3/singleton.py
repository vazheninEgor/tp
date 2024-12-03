class APIConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Создание нового подключения к API")
            cls._instance = super(APIConnection, cls).__new__(cls, *args, **kwargs)
        else:
            print("Использование существующего подключения к API")
        return cls._instance

    def connect(self):
        print("Подключение к API...")

# Использование
conn1 = APIConnection()
conn1.connect()

conn2 = APIConnection()
conn2.connect()

# Проверка, что это один и тот же объект
print(conn1 is conn2)