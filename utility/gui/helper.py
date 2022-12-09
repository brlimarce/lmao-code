from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from utility.gui.font import Font
from utility import constants as const

# Render a code area in the interface.
def codearea(disabled=False) -> QTextEdit:
  textarea = QTextEdit()
  textarea.setStyleSheet(f"background-color: {const.BLACK}; color: {const.WHITE}; padding: 20px")
  textarea.setFont(Font(12).mono)
  textarea.setDisabled(disabled)
  textarea.setTabStopDistance(8) # 2 spaces for 1 tab.
  
  # Return the component.
  return textarea

# Render a table based on the given data.
def table(colnames: list) -> QTableWidget:
  # Set the properties for the table.
  table = QTableWidget()
  table.setShowGrid(False)
  table.setStyleSheet("QTableView::section { border: none } QHeaderView::section { border: none; background-color: #ffedd5; color: " + const.ORANGE + "; }")

  # Set the table headers.
  table.setColumnCount(len(colnames))
  table.setFixedWidth(108 * len(colnames))
  table.setHorizontalHeaderLabels(colnames)
  table.horizontalHeader().setStyleSheet(f"background-color: #ffedd5; color: {const.ORANGE}; border: none")
  table.horizontalHeader().setFont(Font(12).bold)

  # Display the table
  table.show()

  # Return the component.
  return table

# Render a button with an icon.
def button(label: str, icon_file: str, color = const.ORANGE) -> QPushButton:
  button = QPushButton(f"\t{label.upper()}")
  button.setStyleSheet("QPushButton { background-color: transparent; border: 1px solid " + color + ";" + "color:"  + color + "; border-radius: 3 } QPushButton:hover { color: #fefefe; background-color: " + color + "; }")
  
  button.setIcon(QIcon(f"{const.ASSETS_FOLDER}{icon_file}"))
  button.setFont(Font(10).bold)
  button.setFixedHeight(32)
  
  # Return the component.
  return button