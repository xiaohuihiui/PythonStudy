import win32com.client as win32
word=win32.Dispatch("Word.Application")
word.DisplayAlerts = False
cs=win32.constants

