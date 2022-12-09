from utility.gui.app import App
import PyQt6.QtWidgets as qt
import sys

if __name__ == '__main__':
  # Initialize the app.
  app = qt.QApplication(sys.argv)
  window = App()

  # Display the app.
  window.show()
  sys.exit(app.exec())