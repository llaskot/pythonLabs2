from PyQt5.QtWidgets import QWidget, QFormLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup

from viev_l2.popup.popup_abstract import PopupAbstract


class PopupClientAbstract(PopupAbstract):
    def __init__(self, parent):
        super().__init__(parent)
        self.client_data = None

    def _create_main_content(self) -> QWidget:
        form = QWidget()
        form.setMinimumWidth(400)
        form_layout = QFormLayout(form)

        self.name_input, name = self.create_text_input("Client fullname",
                                                       self.client_data[1] if self.client_data[1] else '')

        self.license_input, license_el = self.create_text_input("License number",
                                                                self.client_data[2] if self.client_data[2] else '')

        form_layout.addWidget(name)
        form_layout.addWidget(license_el)
        return form
