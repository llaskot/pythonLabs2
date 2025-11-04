from PyQt5.QtWidgets import QWidget, QFormLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup

from viev_l2.popup.popup_abstract import PopupAbstract


class PopupCarAbstract(PopupAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.car_data = None

    def _create_main_content(self) -> QWidget:
        form = QWidget()
        # form.setFixedSize(300, 250)
        form_layout = QFormLayout(form)

        self.model_input, model = self.create_text_input("Car model", self.car_data[1] if self.car_data[1] else '')

        self.year_input, year = self.create_int_input("Car year", self.car_data[2] if self.car_data[2] else '')

        self.color_input, color = self.create_text_input("Car color", self.car_data[3] if self.car_data[3] else '')

        self.licen_input, licen = self.create_text_input("License plate", self.car_data[4] if self.car_data[4] else '')

        self.price_input, price = self.create_float_input("Daily price", self.car_data[5] if self.car_data[5] else '')

        self.insur_input, insur = self.create_float_input("Insurance price",
                                                          self.car_data[6] if self.car_data[6] else '')

        self.rad_group, availability = self.create_radio_btns("Availability",
                                                              self.car_data[7] if self.car_data else True)

        horizont_group = QWidget()
        hor_layout = QHBoxLayout(horizont_group)
        hor_layout.addWidget(year)
        hor_layout.addWidget(color)

        horizont_group2 = QWidget()
        hor_layout2 = QHBoxLayout(horizont_group2)
        hor_layout2.addWidget(price)
        hor_layout2.addWidget(insur)
        hor_layout2.addWidget(availability)

        form_layout.addWidget(model)
        form_layout.addWidget(horizont_group)
        form_layout.addWidget(licen)
        form_layout.addWidget(horizont_group2)
        return form

    def create_radio_btns(self, name: str, val: bool = True) -> (QButtonGroup, QGroupBox):
        availability = QGroupBox(name)
        rad_yes = QRadioButton("yes")
        rad_yes.setChecked(val)
        rad_no = QRadioButton("no")
        rad_no.setChecked(not val)
        rad_group = QButtonGroup()
        rad_group.addButton(rad_yes, 1)
        rad_group.addButton(rad_no, 0)
        availability_layout = QHBoxLayout(availability)
        availability_layout.addWidget(rad_yes)
        availability_layout.addWidget(rad_no)
        return rad_group, availability
