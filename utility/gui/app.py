from api.lexer import Lexer

from utility.gui.font import Font
from utility.gui import helper

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import easygui_qt
import utility.constants as const

class App(QMainWindow):
  # * Properties
  _root = None # The primary layout
  _editor = None # Code editor
  _terminal = None

  _lexeme_table = None
  _lookup_table = None

  _lexeme_cols = []
  _lookup_cols = []

  # * Constructor
  def __init__(self):
    # Configure the main window.
    super().__init__()
    self._root = QVBoxLayout()
    self._root.setContentsMargins(const.MARGIN, const.MARGIN, const.MARGIN, const.MARGIN)

    widget = QWidget()
    self.configure()

    # Add the layouts for each component.
    self._root.addLayout(self.render_header()) # Header
    self._root.addLayout(self.init_editor()) # First Row
    self._root.addLayout(self.button_group()) # Button Group

    # Render the terminal.
    self._terminal = helper.codearea(True)
    self._root.addWidget(self._terminal)

    widget.setLayout(self._root)
    self.setCentralWidget(widget)
  
  # Set the default configurations
  # for the app.
  def configure(self):
    # Configure the main window.
    self.setWindowIcon(QIcon(const.ASSETS_FOLDER + "logo.png"))
    self.setWindowTitle("<lmao>code")
    self.setFixedSize(const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
    self.setStyleSheet(
      f"background-color: {const.PRIMARY}; color: {const.BLACK}"
    )

    # Move the app to the center.
    qr = self.frameGeometry()
    cp = self.screen().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())
  
  # Render the header in the program.
  def render_header(self) -> QVBoxLayout:
    col_root = QVBoxLayout()
    col_root.setContentsMargins(0, 8, 0, 36)
    col_root.setSpacing(2)

    # Add the header title.
    title_root = QHBoxLayout()
    title_root.setContentsMargins(0, 0, 0, 0)
    title_root.setSpacing(20)

    icon_lbl = QLabel()
    icon_lbl.setPixmap(QPixmap(f"{const.ASSETS_FOLDER}logo.png").scaled(40, 40))

    header = QLabel("<lmao>code")
    header.setStyleSheet(f"color: {const.ORANGE}")
    header.setFont(Font(24).bold)
    
    # Add the icon label to the layout.
    title_root.addWidget(icon_lbl)
    title_root.addWidget(header)

    title_root.setAlignment(Qt.AlignmentFlag.AlignCenter)
    col_root.addLayout(title_root)

    # Add the description.
    description = QLabel("An esoteric programming interpreter")
    description.setFont(Font(14).regular)
    description.setAlignment(Qt.AlignmentFlag.AlignCenter)
    description.setStyleSheet(f"color: {const.GREY}")
    col_root.addWidget(description)

    return col_root
  
  # Initialize the code editor as well as the
  # lexeme and lookup tables.
  def init_editor(self) -> QHBoxLayout:
    row_root = QHBoxLayout()
    row_root.setSpacing(const.MARGIN - 20)

    # Add the code editor.
    self._editor = helper.codearea()
    row_root.addWidget(self._editor)

    # Add the lexeme table.
    self._lexeme_cols = ["Lexeme", "Type", "Line"]
    self._lexeme_table = helper.table(self._lexeme_cols)
    row_root.addWidget(self._lexeme_table)
    
    # Add the lookup table.
    self._lookup_cols = ["Variable", "Value", "Type"]
    self._lookup_table = helper.table(self._lookup_cols)
    row_root.addWidget(self._lookup_table)

    return row_root
  
  # Render the button group.
  def button_group(self) -> QHBoxLayout:
    row_root = QHBoxLayout()
    row_root.setContentsMargins(0, const.MARGIN - 20, 0, const.MARGIN - 8)
    row_root.setSpacing(16)

    # Execute Button
    execute_btn = helper.button("Execute", "flash.png", "#1e3a8a")
    row_root.addWidget(execute_btn)
    execute_btn.clicked.connect(lambda s: self.execute())

    # Clear Button
    clear_btn = helper.button("Clear", "cancel.png", "#b91c1c")
    row_root.addWidget(clear_btn)
    clear_btn.clicked.connect(lambda s: self.clear())

    # Upload Button
    upload_btn = helper.button("Upload Program", "upload.png", "#365314")
    row_root.addWidget(upload_btn)
    upload_btn.clicked.connect(lambda s: self.upload_program())

    return row_root

  # Upload a LOLCODE program and place
  # the code in the editor area.
  def upload_program(self):
    try:
      # Get the program via file dialog.
      filepath = QFileDialog.getOpenFileName(self, "Upload LOLCODE Program", ".","LOLCODE Programs (*.lol)")
      code = []

      # Set the code in the editor area.
      with open(filepath[0], "r") as infile:
        for line in infile.readlines():
          code.append(line[:-1])
      self.clear()
      self._editor.setText("\n".join(code))
    except Exception as e:
      return
  
  # Execute the code and display the
  # output in the terminal.
  def execute(self):
    try:
      # Get the code from the editor.
      data = self._editor.toPlainText()
      code = [d.strip() for d in data.split("\n") if d != ""]

      # Clear all tables and the terminal.
      self._terminal.setText("")
      self._lexeme_table.setRowCount(0);
      self._lookup_table.setRowCount(0);

      # * Lexical Analysis
      lexer = Lexer(code)
      lexer_result = lexer.analyze()
      if not lexer_result[0]:
        raise Exception(lexer_result[1])

      # Morph the table rows.
      rows = []
      for row in lexer_result[1].items():
        for subrow in row[1]:
          rows.append([subrow[0], subrow[1], str(row[0])])
      self._lexeme_table.setRowCount(len(rows))

      # Display the item for each row.
      for i in range(len(rows)):
        for j in range(len(self._lexeme_cols)):
          item = QTableWidgetItem(rows[i][j])
          item.setFont(Font(11).regular)
          self._lexeme_table.setItem(i, j, item)
      
      # Resize the rows & columns based on values.
      self._lexeme_table.resizeColumnsToContents()
      self._lexeme_table.resizeRowsToContents()

      # * Syntax Analysis

      # * Semantic Analysis

      # * Uncomment this block for input.
      # # Sample Input
      # temp = easygui_qt.get_string(message="", title="GIMMEH")
      # print(f"Input: {temp}")
    except Exception as e:
      self._terminal.setText(str(e))
    
  # Clear everything in the interface.
  def clear(self):
    self._editor.setText("")
    self._terminal.setText("")
    self._lexeme_table.setRowCount(0);
    self._lookup_table.setRowCount(0);