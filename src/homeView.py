import mariadb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from Users.View.UserView import UserView
from src.Items.View.ItemView import ItemView


class HomeView(QMainWindow):

    def __init__(self, widget):
        super(HomeView, self).__init__()
        loadUi("../designer/Home view/HomeView.ui", self)
        self.widget = widget
        self.setup()

    def setup(self):
        # Menu Button
        self.userButton.clicked.connect(lambda: self.gouserview())
        self.catolgingButton.clicked.connect(lambda: self.goinventoryview())
        # self.statsButton.clicked.connect(self.gostatsview())
        # self.reportButton.clicked.connect(self.goreportview())
        # self.serviceButton.clicked.connect(self.goserviceview())
        # self.commButton.clicked.connect(self.gocomunicationview())
        # self.movementButton.clicked.connect(self.gomovemetview())
        # Shortcut Button
        # self.newloanButton.clicked.connect(self.newloan())
        # self.newreservButton.clicked.connect(self.newreservation())
        # self.newuserButton.clicked.connect(self.newuser())
        # Setting Button
        # self.settingButton.clicked.connect(self.setting())
        pass

    # region Collegamenti View
    def gouserview(self):
        view = UserView(self.widget)
        self.widget.addWidget(view)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def gostatsview(self):
        pass

    def goinventoryview(self):
        view = ItemView(self.widget)
        self.widget.addWidget(view)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def goreportview(self):
        pass

    def goserviceview(self):
        pass

    def gomovemetview(self):
        pass

    def gocomunicationview(self):
        pass

    # endregion

    # region Shortcut function
    def newloan(self):
        pass

    def newreservation(self):
        pass

    def newuser(self):
        pass

    def setting(self):
        pass
    # end region
