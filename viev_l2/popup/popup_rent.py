from PyQt5.QtCore import QDate, QLocale
from PyQt5.QtWidgets import  QWidget, QFormLayout, QMessageBox, QGroupBox, QVBoxLayout, QHBoxLayout

from controllers.rentController import get_users_list, get_cars_list, prepare_data, save_rent
from viev_l2.filter_combo import FilterCombo
from viev_l2.popup.popup_abstract import PopupAbstract
import PyQt5.QtWidgets as q


class PopupRent(PopupAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.client_data = None

        self.setWindowTitle("Rent the car")
        self.main_content = self._create_main_content()
        self.layout.insertWidget(0, self.main_content)
        self.save_btn.clicked.connect(self._on_save)

    def _create_main_content(self) -> QWidget:
        form = QWidget()
        form.setMinimumWidth(400)
        form_layout = QFormLayout(form)

        box = QGroupBox("Client License")
        layout = QVBoxLayout(box)
        self.select_user = FilterCombo(get_users_list)
        layout.addWidget(self.select_user)

        box2 = QGroupBox("Car License Plate")
        layout2 = QHBoxLayout(box2)
        self.select_car = FilterCombo(get_cars_list)
        layout2.addWidget(self.select_car)

        self.date_edit = q.QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.date_edit.setDate(QDate.currentDate())

        box3 = QGroupBox("Select Date")
        layout3 = QHBoxLayout(box3)
        layout3.addWidget(self.date_edit)

        self.days, line = self.create_int_input("Days number")
        line.setMaximumWidth(150)

        horizontal = QWidget()
        horizontal_layout = QHBoxLayout(horizontal)
        horizontal_layout.addWidget(box3)
        horizontal_layout.addWidget(line)

        form_layout.addWidget(box)
        form_layout.addWidget(box2)
        form_layout.addWidget(horizontal)
        return form

    def _on_save(self):
        try:
            dock = prepare_data(self.select_car.get_id(),
                                self.select_user.get_id(),
                                self.date_edit.date().toPyDate(),
                                self.days.text())
            QMessageBox.question(self, "Confirm!", "\n".join(f"{key}: {value}" for key, value in dock.items()))
            save_rent(self.select_car.get_id(),
                      self.select_user.get_id(),
                      self.days.text(),
                      dock['rent_total'],
                      self.date_edit.date().toPyDate()
                      )
            self.parent().on_text_changed('')
            self.close()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", str(e))
