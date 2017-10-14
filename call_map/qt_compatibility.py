'''
The qt_compatibility module is to make it easy to switch between different Qt/Python bridge implementations.

'''


from PySide2 import QtCore, QtGui, QtWidgets, Qt

# The following monkey patching already occurs when importing
# qtconsole.pygments_highlighter, however that should not be relied upon.
QtCore.Signal = QtCore.pyqtSignal
