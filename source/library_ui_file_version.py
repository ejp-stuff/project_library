from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QComboBox, 
QLineEdit, QInputDialog, QFileDialog, QMessageBox, QCheckBox)
from PySide2 import QtGui, QtCore, QtUiTools, QtWidgets
from PySide2.QtGui import QFont, QPixmap, QIcon
import hou, os

"""
---------------------------------------------------------------                                                        
 _____     _           _     _    _____                         
|     |___| |_ ___ ___|_|___| |  |     |___ ___ ___ ___ ___ ___ 
| | | | .'|  _| -_|  _| | .'| |  | | | | .'|   | .'| . | -_|  _|
|_|_|_|__,|_| |___|_| |_|__,|_|  |_|_|_|__,|_|_|__,|_  |___|_|  
                                                   |___|       
---------------------------------------------------------------
"""

class material_manager_ui(QtWidgets.QWidget):


    def __init__(self, *args, **kwargs):
        super(material_manager_ui, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Material Manager")
        self.setGeometry(600, 250, 1320, 950)
        
        ui_file = "C:/Dev/git/py/prj/material_library/ui/material_manager_ui_v001.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
          
        self.main_thumbnail = self.ui.px_main_thumbnail
        self.snapshot       = self.ui.snapshot_button
        self.info_box       = self.ui.information_group
        self.load_material  = self.ui.load_button
        self.material_types = self.ui.type_tree
        self.search         = self.ui.shader_search
        self.add_shader     = self.ui.add_button
        self.remove_shader  = self.ui.remove_button
        self.shader_library = self.ui.shader_list
        
        self.main_thumbnail.setPixmap(QPixmap("C:/Users/ewanp/Downloads/material.png"))
        self.main_thumbnail.setStyleSheet("QLabel { border: 5px solid rgb(40, 40, 40); }")
        
        self.snapshot.setIcon(QIcon("C:/Dev/git/py/prj/material_library/icons/snapshot_img.jpg"))
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.ui)
        
        self.setStyleSheet("QWidget { background-color: rgb(50, 50, 50); }")
        self.setLayout(main_layout)

win = material_manager_ui()
win.show()

        
