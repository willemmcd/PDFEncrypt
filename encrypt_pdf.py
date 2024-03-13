import sys
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLabel, QLineEdit, QVBoxLayout, \
    QFileDialog, QMessageBox


class PDFEncryptor(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PDF Encryptor')
        self.resize(400, 200)

        self.encrypt_button = QPushButton('Encrypt PDF', self)
        self.encrypt_button.clicked.connect(self.encrypt_pdf)

        layout = QVBoxLayout()
        layout.addWidget(self.encrypt_button)
        self.setLayout(layout)

    def encrypt_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Choose PDF File to Encrypt', '', 'PDF Files (*.pdf)')
        if not file_path:
            return

        password, ok = QInputDialog.getText(self, 'Enter Password', 'Enter password:', QLineEdit.Password)
        if not ok:
            return

        dest_file_path, _ = QFileDialog.getSaveFileName(self, 'Save Encrypted PDF As', '', 'PDF Files (*.pdf)')
        if not dest_file_path:
            return

        encrypt_pdf_file(file_path, dest_file_path, password)

        QMessageBox.information(self, "Encryption Complete", "PDF encryption completed successfully.")


def encrypt_pdf_file(input_path, output_path, password):
    reader = PdfReader(input_path)

    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(password)

    with open(output_path, "wb") as out_file:
        writer.write(out_file)


if __name__ == '__main__':
    print("Starting app..")
    app = QApplication(sys.argv)
    pdf_encryptor = PDFEncryptor()
    pdf_encryptor.show()
    sys.exit(app.exec_())
