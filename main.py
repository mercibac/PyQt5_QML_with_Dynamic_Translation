# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from app_modules import *

class MyEngine(QQmlApplicationEngine):
    def __int__(self):
        #QApplication.__init__(self)
        super().__init__(self)


if __name__ == "__main__":

    app = QGuiApplication(sys.argv)

    #    Instatiate the Translator
    #    translator = QTranslator()
    #    translator.load('translation/tr_fr')
    #    app.installTranslator(translator)

    engine = MyEngine()

    # Get context
    qmlTranslator = QmlTranslator()
    engine.rootContext().setContextProperty("qmlTranslator", qmlTranslator)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    # engine.retranslate() ==> For a new language

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
