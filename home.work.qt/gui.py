from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import sys
from collections import Counter


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Анализ текста")
        self.setMinimumSize(600, 400)

        # центральный виджет и главный лейаут
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        # поле ввода текста
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Введите текст для анализа...")
        # скроллбар уже есть по умолчпнию
        main_layout.addWidget(self.text_edit)

        # кнопка
        self.analyze_btn = QPushButton("Анализ")
        self.analyze_btn.clicked.connect(self.run_analysis)
        self.analyze_btn.setFixedHeight(40)
        main_layout.addWidget(self.analyze_btn, alignment=Qt.AlignHCenter)

        # блок результата
        result_layout = QHBoxLayout()
        main_layout.addLayout(result_layout)
        label_result = QLabel("Результат:")
        result_layout.addWidget(label_result, alignment=Qt.AlignTop)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setPlaceholderText("Здесь будет анализ текста...")
        result_layout.addWidget(self.result_box)

    def run_analysis(self):
        text = self.text_edit.toPlainText()
        if not text.strip():
            self.result_box.setPlainText("Текст пустой, анализировать нечего.\n")
            return

        # нормализуем: в нижний регистр и заменяем разделители пробелами
        symbols = ",.!?;:\"'()[]{}\n\t\r"
        normalized = text.lower()
        for ch in symbols:
            normalized = normalized.replace(ch, " ")

        words = [w for w in normalized.split()]
        total_words = len(words)
        unique_words = len(set(words))
        chars = len(text)

        # частоты слов
        count = Counter([w for w in words if len(w) > 2])
        top_n = 10
        most_common = count.most_common(top_n)

        # доля уникальных слов
        diversity = unique_words / total_words if total_words > 0 else 0

        # текст результата
        lines = [f"Количество символов: {chars}", f"Количество слов: {total_words}", f"Уникальных слов: {unique_words}",
                 f"Лексическое разнообразие (уникальные/все): {diversity:.2f}",
                 f"Вот {top_n} самых частых слов (если длина > 2):"]

        if most_common:
            for word, cnt in most_common:
                percent = (cnt / total_words) * 100
                lines.append(f"  {word} — {cnt} раз ({percent:.1f}%)")
        else:
            lines.append("Нет достаточно длинных слов для анализа")

        result_text = "\n".join(lines) + "\n"

        self.result_box.setPlainText(result_text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

main()



