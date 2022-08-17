"""Test gui.

Test gui application will be reutilised somewhere else or file renamed

"""
import os
import pathlib
import sys

from PyQt5 import QtCore, QtWidgets

from report_generator.report_generator_cli.create_report import create_report


class Ui_MainWindow(object):
    """UI Mainwindow object."""

    def setupUi(self, MainWindow):
        """UI Setup."""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 230)
        self.mainwin = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 421, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.reportNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.reportNameLabel.setObjectName("reportNameLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.reportNameLabel
        )
        self.reportNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reportNameLineEdit.setObjectName("reportNameLineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.reportNameLineEdit
        )
        self.reportAuthorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.reportAuthorLabel.setObjectName("reportAuthorLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.reportAuthorLabel
        )
        self.reportAuthorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reportAuthorLineEdit.setObjectName("reportAuthorLineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.reportAuthorLineEdit
        )
        self.universityNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.universityNameLabel.setObjectName("universityNameLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.universityNameLabel
        )
        self.universityNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.universityNameLineEdit.setObjectName("universityNameLineEdit")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.universityNameLineEdit
        )
        self.universitySchoolLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.universitySchoolLabel.setObjectName("universitySchoolLabel")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.universitySchoolLabel
        )
        self.universitySchoolLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.universitySchoolLineEdit.setObjectName("universitySchoolLineEdit")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.universitySchoolLineEdit
        )
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(267, 150, 161, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 20))
        self.menubar.setObjectName("menubar")
        self.menuReport_Generator = QtWidgets.QMenu(self.menubar)
        self.menuReport_Generator.setObjectName("menuReport_Generator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuReport_Generator.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.create_report_button)
        # self.pushButton.clicked.connect(lambda:MainWindow.close())

    def retranslateUi(self, MainWindow):
        """Retranslate UI."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Generator"))
        self.reportNameLabel.setText(_translate("MainWindow", "Report Name"))
        self.reportAuthorLabel.setText(_translate("MainWindow", "Report Author"))
        self.universityNameLabel.setText(_translate("MainWindow", "University Name"))
        self.universitySchoolLabel.setText(
            _translate("MainWindow", "University School")
        )
        self.pushButton.setText(_translate("MainWindow", "Create Report"))
        self.menuReport_Generator.setTitle(_translate("MainWindow", "Report Generator"))

    def clicked(self):
        """Click button message."""
        print("clicked")

    def create_report_button(self, MainWindow):
        """Create report button."""
        title = self.reportNameLineEdit.text()
        author = self.reportAuthorLineEdit.text()
        university = self.universityNameLineEdit.text()
        school = self.universitySchoolLineEdit.text()

        args = [title, author, university, school]
        source = os.path.join(
            (pathlib.Path(os.path.dirname(os.path.realpath(__file__)))).parent.parent,
            "examples",
            "example_output_excel",
            "output_1.xlsx",
        )
        # create_report(source, title, author,university, school)

        if all(args):
            print(f"Args: {title}, {author}, {university}, {school}")
            create_report(source, title, author, university, school)
            self.mainwin.close()
        else:
            print("All fields must be filled")


def main():
    """Application ui main."""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
