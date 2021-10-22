import random
from PyQt6 import QtWidgets
import main_window
import settings


class PasswordGenerator(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btns_functions()

    def btns_functions(self):
        self.generate_button.clicked.connect(lambda: self.generate_button_clicked())

    def generate_button_clicked(self):
        result = self.collect_set(settings.final_set)
        if len(result) > 0:
            print_result = '\n'.join(self.generate_password(result))
            self.password_browser.setText(print_result)  # запись в поле с паролем
        else:
            self.password_browser.setText('Выберите хотя бы 1 параметр')
        self.update_design()

    # Формируем итоговый набор символов для пароля
    def collect_set(self, result_set):
        if self.check_box1.isChecked():
            result_set += settings.set1
        if self.check_box2.isChecked():
            result_set += settings.set2
        if self.check_box3.isChecked():
            result_set += settings.set3
        if self.check_box4.isChecked():
            result_set += settings.set4
        if self.check_box5.isChecked():
            result_set += settings.set5
        if self.check_box6.isChecked():
            result_set += settings.set6
        return result_set

    # Генерируем пароли в зависимости от их кол-ва и длины
    def generate_password(self, final_set):
        res = []
        number_quantity = int(self.comboBox.currentText())
        length = int(self.comboBox_2.currentText())
        for i in range(number_quantity):
            result = ''
            while len(result) < length:
                result += random.choice(final_set)
            res.append(result)
        return res

    def update_design(self):
        if int(self.comboBox.currentText()) > 1:
            self.label8.setText('Ваши пароли: ')
        else:
            self.label8.setText('Ваш пароль: ')
