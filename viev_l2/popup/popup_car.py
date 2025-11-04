import PyQt5.QtWidgets as q

from controllers.carController import create_car
from viev_l2.popup.popup_car_abstract import PopupCarAbstract


class PopupCar(PopupCarAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.car_data = (False, False, False, False, False, False, False, False)
        self.setWindowTitle("Add new car to the Database")
        self.main_content = self._create_main_content()
        self.layout.insertWidget(0, self.main_content)
        self.save_btn.clicked.connect(self._on_save)

    def _on_save(self):
        try:
            create_car((False, self.model_input.text(), self.year_input.text(), self.color_input.text(),
                        self.licen_input.text(), self.price_input.text(), self.insur_input.text(),
                        self.rad_group.checkedId()))
            self.parent().on_text_changed('')
            self.close()
        except Exception as e:
            q.QMessageBox.critical(self, "Error", str(e))

