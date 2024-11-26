from pywinauto.application import Application
# Run a target application
app = Application().start("notepad.exe")
# Select a menu item
# UntitledNotepad - название элемента по английски без пробелов
#app.UntitledNotepad.menu_select("Справка->О программе")
# Но можно обращаться к элементу по имени (заголовку, надписи), как элементу словаря
app["Безымянный - блокнот"].menu_select("Справка->О программе")
# Click on a button
app["Блокнот:сведения"].ОК.click()
# Type a text string
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)