# Продукт
class Report:
    def __init__(self):
        self.title = ""
        self.content = ""
        self.notes = ""

    def __str__(self):
        return f"Отчёт: {self.title}\n{self.content}\nПримечания: {self.notes}"

# Интерфейс строителя
class ReportBuilder:
    def build_title(self, title: str):
        pass

    def build_content(self, content: str):
        pass

    def build_notes(self, notes: str):
        pass

    def get_result(self) -> Report:
        pass

# Конкретный строитель для отчёта
class SimpleReportBuilder(ReportBuilder):
    def __init__(self):
        self.report = Report()

    def build_title(self, title: str):
        self.report.title = title

    def build_content(self, content: str):
        self.report.content = content

    def build_notes(self, notes: str):
        self.report.notes = notes

    def get_result(self) -> Report:
        return self.report

# Директор
class ReportDirector:
    def __init__(self, builder: ReportBuilder):
        self.builder = builder

    def construct_report(self, title, content, notes):
        self.builder.build_title(title)
        self.builder.build_content(content)
        self.builder.build_notes(notes)

# Использование
builder = SimpleReportBuilder()
director = ReportDirector(builder)

director.construct_report("Отчёт по проекту", "Содержание отчёта...", "Необходимы дополнительные исследования.")
report = builder.get_result()

print(report)