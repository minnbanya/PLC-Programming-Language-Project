import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

from components.lexica import MyLexer
from components.parsers import ASTParser
from components.memory import Memory
from components.ast.statement import PrintStatement

class StreamRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.append(text)  # Appends text to the QTextEdit widget

    def flush(self):
        pass  # Necessary for compatibility with sys.stdout


class MainWindow(QMainWindow):
    button_run: QPushButton
    button_clear: QPushButton
    # button_history: QPushButton
    input_text: QTextEdit
    output_log: QTextEdit  # Assuming you have a QTextEdit for logs or results
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("components/IDE.ui", self)

        self.memory = Memory()  # Persistent memory across runs
        self.button_run.clicked.connect(self.push_run)
        self.button_clear.clicked.connect(self.push_clear)
        # self.button_history.clicked.connect(self.push_history)
        # self.history = []

         # Redirect stdout to the QTextEdit
        sys.stdout = StreamRedirector(self.output_log)

    def closeEvent(self, event):
        super().closeEvent(event)
        sys.stdout = sys.__stdout__  # Reset stdout when the window closes


    def push_run(self):
        # if self.input_text and self.output_log:
        #     self.history.append([f"Code:{self.input_text.toPlainText()}\nOutput:{self.output_log.toPlainText()}"])
        lexer = MyLexer()
        parser = ASTParser(self.memory)
        input_text = self.input_text.toPlainText()
        result = parser.parse(lexer.tokenize(input_text))
        
        # self.push_clear()
        # print(self.memory)
        if result:
            for stmt in result:
                try:
                    stmt.run(self.memory)
                except ValueError as e:
                    print(e)
                    break
                # print(self.memory)

        else:
            print("No valid commands to execute.")

    def push_clear(self):
        self.output_log.clear()

    # def push_history(self):
    #     print(self.history)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
