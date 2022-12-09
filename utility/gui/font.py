from PyQt6.QtGui import *
import utility.constants as const

class Font():
  # * Properties
  _bold_style = None
  _regular_style = None
  _code_style = None
  _size = 0
  
  # * Constructor
  def __init__(self, size: int):
    # Configure the typography styles.
    fid = QFontDatabase.addApplicationFont(const.STATIC_FOLDER + "Quicksand-Bold.ttf")
    self._bold_style = QFontDatabase.applicationFontFamilies(fid)

    fid = QFontDatabase.addApplicationFont(const.STATIC_FOLDER + "Quicksand-Medium.ttf")
    self._regular_style = QFontDatabase.applicationFontFamilies(fid)

    fid = QFontDatabase.addApplicationFont(const.STATIC_FOLDER + "FiraCode-Medium.ttf")
    self._code_style = QFontDatabase.applicationFontFamilies(fid)

    # Set the size.
    self._size = size
    
  # * Getters
  @property
  def bold(self) -> QFont:
    return QFont(self._bold_style[0], self._size, 700)
  
  @property
  def regular(self) -> QFont:
    return QFont(self._regular_style[0], self._size, 500)

  @property
  def mono(self) -> QFont:
    return QFont(self._code_style[0], self._size, 500)