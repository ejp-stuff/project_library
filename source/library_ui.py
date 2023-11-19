from PySide2.QtCore import Qt
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QTreeWidget, QLineEdit, QPushButton, QScrollArea, QLabel, QComboBox, QGroupBox, QSizePolicy
from PySide2 import QtGui, QtCore, QtUiTools, QtWidgets
from PySide2.QtGui import QFont, QPixmap, QIcon

import hou
import os

"""
---------------------------------------------------------------                                                        
 _____     _           _     _    _____                         
|     |___| |_ ___ ___|_|___| |  |     |___ ___ ___ ___ ___ ___ 
| | | | .'|  _| -_|  _| | .'| |  | | | | .'|   | .'| . | -_|  _|
|_|_|_|__,|_| |___|_| |_|__,|_|  |_|_|_|__,|_|_|__,|_  |___|_|  
                                                   |___|       
---------------------------------------------------------------
"""

class project_ui(QWidget):
    def __init__(self):
            super(project_ui, self).__init__()
            self.setWindowTitle("Material Library")
            self.setGeometry(600, 250, 1500, 950)
            
            # layouts
            drop_down_layout   = QVBoxLayout()
            library_layout     = QVBoxLayout()
            search_layout      = QHBoxLayout()
            information_layout = QVBoxLayout() 
            snapshot_layout    = QHBoxLayout()
            
            # widgets
            self.material_dropdown    = QTreeWidget()
            
            self.search_bar           = QLineEdit()
            self.add_material         = QPushButton('+')
            self.remove_material      = QPushButton('-')
            self.library              = QScrollArea()
            
            self.material_preview     = QLabel('')
            self.snapshot             = QPushButton()
            self.load_thumbnail       = QPushButton()
            self.material_info_box    = QGroupBox("Material Information")
            self.dcc_select           = QComboBox()
            self.engine_select        = QComboBox()
            self.load_material        = QPushButton()
            
            # widget settings
            self.search_bar.setFixedHeight(30)
            self.search_bar.setPlaceholderText("Search...")
            self.search_bar.setStyleSheet ( """
            QLineEdit {
                border: 2px solid rgb(50, 50, 50);
                border-radius: 15px;
                background-color: rgb(40, 40, 40);
                padding-left: 10px;
                color: rgb(150, 150, 150);
                font-family: Open Sans;
            }
            """ )
            
            for mat_widg in [self.add_material, self.remove_material]:
                mat_widg.setFixedHeight(30)
                mat_widg.setFixedWidth(30)
                mat_widg.setStyleSheet ( """
                QPushButton {
                    border: 2px solid rgb(50, 50, 50);
                    border-radius: 10px;
                    background-color: rgb(40, 40, 40);
                    color: rgb(150, 150, 150);
                    font-family: Open Sans;
                }
                QPushButton:hover {
                    background-color: rgb(96, 157, 212);   
                    color: rgb(50, 50, 50)
                }
                QPushButton:pressed {
                    background-color: rgb(30, 30, 30);   
                }
                """ )
            
            # setting layouts
            drop_down_layout.addWidget(self.material_dropdown)
            
            search_layout.addWidget(self.search_bar)
            search_layout.addWidget(self.add_material)
            search_layout.addWidget(self.remove_material)
            library_layout.addLayout(search_layout, 3)
            library_layout.addWidget(self.library, 6)
            
            snapshot_layout.addWidget(self.snapshot)
            snapshot_layout.addWidget(self.load_thumbnail)
            information_layout.addWidget(self.material_preview)
            information_layout.addLayout(snapshot_layout)
            information_layout.addWidget(self.material_info_box)
            information_layout.addWidget(self.dcc_select)
            information_layout.addWidget(self.engine_select)
            information_layout.addWidget(self.load_material)
            
            # qwidget class settings
            main_layout = QHBoxLayout()
            main_layout.addSpacing(15)
            main_layout.addLayout(drop_down_layout, 1)
            main_layout.addSpacing(30)
            main_layout.addLayout(library_layout, 3)
            main_layout.addSpacing(30)
            main_layout.addLayout(information_layout, 2)
            main_layout.addSpacing(15)
            
            main_vertical_layout = QVBoxLayout()
            main_vertical_layout.addSpacing(15)
            main_vertical_layout.addLayout(main_layout)
            main_vertical_layout.addSpacing(15)
            
            self.setLayout(main_vertical_layout)
            self.setStyleSheet (""" QWidget { background-color: rgb(50, 50, 50); } """)
            
            
win = project_ui()
win.show()
