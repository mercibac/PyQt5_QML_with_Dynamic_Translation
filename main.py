# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from app_modules import *


if __name__ == "__main__":

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    # Get context
    qmlTranslator = QmlTranslator()
    engine.rootContext().setContextProperty("qmlTranslator", qmlTranslator)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
