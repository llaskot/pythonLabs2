import PyQt5.QtWidgets as q

from controllers.carController import create_car
from viev_l2.popup.popup_abstract import PopupAbstract


class PopupCar(PopupAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_content = self._create_main_content()
        self.layout.insertWidget(0, self.main_content)
        self.save_btn.clicked.connect(self._on_save)

    def _create_main_content(self):
        form = q.QWidget()
        # form.setFixedSize(300, 250)
        form_layout = q.QFormLayout(form)

        self.model_input, model = self.create_text_input("Car model")

        self.year_input, year = self.create_int_input("Car year")

        self.color_input, color = self.create_text_input("Car color")

        self.licen_input, licen = self.create_text_input("License plate")

        self.price_input, price = self.create_float_input("Daily price")

        self.insur_input, insur = self.create_float_input("Insurance price")

        self.rad_group, availability = self.create_radio_btns("Availability")

        horizont_group = q.QWidget()
        hor_layout = q.QHBoxLayout(horizont_group)
        hor_layout.addWidget(year)
        hor_layout.addWidget(color)

        horizont_group2 = q.QWidget()
        hor_layout2 = q.QHBoxLayout(horizont_group2)
        hor_layout2.addWidget(price)
        hor_layout2.addWidget(insur)
        hor_layout2.addWidget(availability)

        form_layout.addWidget(model)
        form_layout.addWidget(horizont_group)
        form_layout.addWidget(licen)
        form_layout.addWidget(horizont_group2)
        return form

    def _on_save(self):
        print(self.parent().search_func)
        try:
            create_car((False, self.model_input.text(), self.year_input.text(), self.color_input.text(),
                        self.licen_input.text(), self.price_input.text(), self.insur_input.text(),
                        self.rad_group.checkedId()))
            self.parent().on_text_changed('')
            self.close()
        except Exception as e:
            q.QMessageBox.critical(self, "Error", str(e))

    def create_radio_btns(self, name: str, val: bool = True):
        availability = q.QGroupBox(name)
        rad_yes = q.QRadioButton("yes")
        rad_yes.setChecked(val)
        rad_no = q.QRadioButton("no")
        rad_no.setChecked(not val)
        rad_group = q.QButtonGroup()
        rad_group.addButton(rad_yes, 1)
        rad_group.addButton(rad_no, 0)
        availability_layout = q.QHBoxLayout(availability)
        availability_layout.addWidget(rad_yes)
        availability_layout.addWidget(rad_no)
        return rad_group, availability
