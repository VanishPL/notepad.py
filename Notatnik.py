
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class Example(QMainWindow):
    
    def __init__(self):
        self.textEdit = QTextEdit('Pole Tekstowe')
        super().__init__()
        self.initUI()

    

    def initUI(self):
        hbox = QHBoxLayout()
        panel= QWidget()
        panel.setLayout(hbox)
        self.setCentralWidget(panel)

        menu = self.menuBar() 
        files = menu.addMenu('Plik')
        edit = menu.addMenu('Edit')

        open = QAction('Otwórz', self)
        open.setShortcut('Ctrl+O')
        open.setStatusTip('Otwórz plik')
        open.triggered.connect(self.openFile)

        save = QAction('Zapisz', self)
        save.setShortcut('Crtl+S')

        load = QAction('Wczytaj', self)
        load.setShortcut('Ctrl+L')

        saveAs = QAction('Zapisz jako...', self)
        exitMenu = QAction('Koniec', self)
        exitMenu.setShortcut('Ctrl+Q')

        files.addAction(open)   
        files.addAction(save)
        files.addAction(load)
        files.addAction(saveAs)
        files.addAction(exitMenu)

        cut = QAction('Wytnij', self)
        cut.setShortcut('Ctrl+X')
        copy = QAction('Kopiuj', self)
        copy.setShortcut('Ctrl+C')
        paste = QAction('Wklej', self)
        paste.setShortcut('Ctrl+V')
        selectall = QAction('Zaznacz wszystko', self)
        selectall.setShortcut('Ctrl+A')

        edit.addAction(cut)
        edit.addAction(copy)
        edit.addAction(paste)
        edit.addAction(selectall)

        newAct = QAction(QIcon('file.png'), 'Nowy', self)

        openAct = QAction(QIcon('open.png'), 'Otwórz', self)
        openAct.triggered.connect(self.openFile)

        findAct = QAction(QIcon('search.png'), 'Szukaj', self)

        saveAct = QAction(QIcon('save.png'), 'Zapisz', self)

        undoAct = QAction(QIcon('undo.png'), 'Do ty³u', self)

        redoAct = QAction(QIcon('redo.png'), 'Do przodu', self)

        cutAct = QAction(QIcon('cut.png'), 'Wytnij', self)

        copyAct = QAction(QIcon('copy.png'), 'Kopiuj', self)

        pasteAct = QAction(QIcon('paste.png'), 'Wklej', self)

        self.toolbar = self.addToolBar('ToolBar')
        self.toolbar.addAction(newAct)
        self.toolbar.addAction(openAct)
        self.toolbar.addAction(findAct)
        self.toolbar.addAction(saveAct)
        self.toolbar.addAction(undoAct)
        self.toolbar.addAction(redoAct)
        self.toolbar.addAction(cutAct)
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        self.toolbar.setMovable(0)

        #reloadAct = QAction(QIcon('exit24.png'), 'Reload', self)
        
        vbox = QVBoxLayout()
        hbox.addLayout(vbox)
        
        textSize = QSpinBox()
        textSize.setMinimum(1)
        textSize.setMaximum(100)
        textSize.valueChanged[int].connect(self.sizeChanged)
        vbox.addWidget(textSize)
        

        textFont = QButtonGroup(self)
        TNR = QRadioButton('Times New Roman')
        textFont.addButton(TNR)
        TNR.toggled.connect(self.Times)
        

        arial = QRadioButton('Arial')
        textFont.addButton(arial)
        arial.toggled.connect(self.arial)

        courier = QRadioButton('Courier New')
        textFont.addButton(courier)
        courier.toggled.connect(self.courier)

        vbox.addWidget(TNR)
        vbox.addWidget(arial)
        vbox.addWidget(courier)
        vbox.addLayout(self.paleta(), 0)


        vbox.addStretch(1)
        hbox.stretch(1)
        self.textEdit.setTextColor(QColor(0,234,1))
        hbox.addWidget(self.textEdit)
        TNR.setChecked(1)

        self.move(300, 150)
        self.setWindowTitle('Notepad - EXTREME EDITON')
        self.show()

    def sizeChanged(self, value):
        self.textEdit.setFontPointSize(value)

    def stes(self, color):
        self.textEdit.setTextColor(color)

    def paleta(self):
        g = QGridLayout();
        positions = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4)]
        colors = ["#000000", "#7E7E7E", "#870114", "#EC1C24", "#FE7E29",
                  "#FEFEFE", "#C2C2C2", "#B87957", "#FEAEC8", "#FEC81D",
                  "#FEF11D", "#1EB04E", "#09A2E6", "#4049CA", "#A349A2",
                  "#EEE3B0", "#B3E529", "#98D8E9", "#7091BD", "#C8BFE6"]
        for position, colors in zip(positions, colors):
            button = QPushButton("")
            button.setMinimumHeight(20)
            button.setMinimumWidth(20)
            button.setMaximumHeight(20)
            button.setMaximumWidth(20)
            button.setStyleSheet("QPushButton { background-color: " + colors + " }")
            g.addWidget(button, *position)
            col = QColor("7E7E7E")
            button.toggled.connect(self.stes)
        g.setAlignment(Qt.AlignTop)
        return g
    
    

    def openFile(self):
            self.statusBar().showMessage('Otwieranie pliku...')
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

            if fname[0]:
                f = open(fname[0], 'rt')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                self.statusBar().showMessage('Plik otworzony')

    def Times(self):
        self.statusBar().showMessage('Zmiana czcionki na Times New Roman')
        self.textEdit.setFont(QFont("Times New Roman"))
        
    def arial(self):
        self.statusBar().showMessage('Zmiana czcionki na Arial')
        self.textEdit.setFont(QFont("Arial"))

    def courier(self):
        self.statusBar().showMessage('Zmiana czcionki na Courier')
        self.textEdit.setFont(QFont("Courier"))
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.resize(800,600)
    exit(app.exec_())