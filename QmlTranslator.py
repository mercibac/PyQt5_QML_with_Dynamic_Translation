# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QTranslator
from PyQt5.QtWidgets import qApp
from main import *


class QmlTranslator(QObject):
    def __init__(self):
        QObject.__init__(self)
        
        # Instatiate QTranslator
        self.m_translator = QTranslator()

    languageChanged = pyqtSignal()

    # Temporary slot
    @pyqtSlot(str, result=str)
    def getLangage(self, lang):
        print(lang)

    #Slot to set translation
    @pyqtSlot(str)
    def setTranslation(self, lang):
        self.m_translator.load(lang)
        qApp.installTranslator(self.m_translator)
        self.languageChanged.emit()


