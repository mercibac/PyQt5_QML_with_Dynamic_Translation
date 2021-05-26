import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: root
    width: 640
    height: 480
    visible: true

    Rectangle {
        anchors.fill: parent

        Row {
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.topMargin: 35

            spacing: 20

            Text {
                id: lblLanguage
                anchors.verticalCenter: comboBox.verticalCenter
            }

            ComboBox {
                id: comboBox
                model: ["English", "French", "Swahili"]

                // If you change the text, initialize the translation unit via C++ Layer
                onCurrentTextChanged: {
                    qmlTranslator.setTranslation(comboBox.currentText)
                }
            }
        }

        Text {
            id: text
            anchors.centerIn: parent
            font.pixelSize: 20
        }
    }

    // Connect to an interpreter object
    Connections {
        target: qmlTranslator // was registered in main.cpp
        function onLanguageChanged() {
            retranslateUi()
        }
    }

    // Interface translation function\
    function retranslateUi() {
        root.title = qsTr("Hello World")
        lblLanguage.text = qsTr("Language")
        text.text = qsTr("Thank you")
    }

    Component.onCompleted: {
        retranslateUi()
    }
}
