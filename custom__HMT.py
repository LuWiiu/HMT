import sys

class error():
    versionError = "The version of HMT you are is not the most recent! | verion: {}"
    guiTypeError = "Please pip insall the gui you plan to use | guiName: {}"

class dummyGUIfuncs():
    def makeMain(): 
        """
        DearPyGui | titel = "", geometry = [200, 200]
        ... | None
        """
    def startMain(): """None"""
    def endMain(): ...
    def makeWin(): """titel = "", geometry = [200, 200]"""
    def makeButton(): """holder, titel = "", x = 0, y = 0, command = lambda: ..."""
    def makeEntry(): """holder, x = 0, y = 0"""
    def makeListBox(): """holder, contents, x = 0, y = 0, others = []"""

    ###################################################
    ###################################################
    ###################################################
    ###################################################
    ###################################################

    def getEntryText(): 
        """
        TK  | target: _TKINTER.Entry
        CTK | target: _CTK.CTkEntry
        DPG | target: int
        """
    def makeCheckBox(): """holder, x = 0, y = 0, command = lambda: ..."""
    def getCheckBoxState(): 
        """
        TK  | target: _TKINTER.Checkbutton
        CTK | target: _CTK.CTkCheckBox
        DPG | target: int
        """
    def getListBoxItem(): 
        """
        TK  | target: _TKINTER.Checkbutton
        CTK | target: _CTK.CTkEntry
        DPG | target: int
        """

class gui(dummyGUIfuncs):
    """
    An "simpel" interface to make GUIs that can be translated into any GUI framework that it supports

    Currently supported GUI:
        tk
        cutsomtkenter
        dearpygui
    
    You can moddify this code how you want but just know I'm not the best and this is probbaly bad code to most standards,
    if you do please just give some credit.
    """
    modernVersion = "0.0"
    guiType = None
    TKcboxvars = {}

    def __init__(s, guiType, version, customFrameInsert: dict = {}):

        """
        customFrameInsert:
            "makeMain": None,
            "startMain": None,
            "endMain": None,
            "makeWin": None,
            "makeButton": None,
            "makeEntry": None,
            "getEntryText": None,
            "makeCheckBox": None,
            "getCheckBoxState": None,
            "makeListBox": None,
            "getListBoxItem": None,
        """

        s.guiType = guiType
        if version != s.modernVersion: print(error.versionError.format(s.modernVersion))
        if not guiType or guiType == "tk": 
            global _TKINTER
            global _TK
            global _TTK
            import tkinter as _TKINTER
            from tkinter import Tk as _TK
            from tkinter import ttk as _TTK
            s.makeMain = s._TKmakeMain
            s.startMain = s._TKstartMain
            s.endMain = s._TKendMain
            s.makeWin = s._TKmakeWin
            s.makeButton = s._TKmakeButton
            s.makeEntry = s._TKmakeEntry
            s.getEntryText = s._TKgetEntryText
            s.makeCheckBox = s._TKmakeCheckBox
            s.getCheckBoxState = s._TKgetCheckBoxState
            s.makeListBox = s._TKmakeList
            s.getListBoxItem = s._TKgetListBoxItem
        elif guiType == "ctk":
            global _TK
            global _CTK
            from tkinter import Tk as _TK
            import customtkinter as _CTK
            s.makeMain = s._CTKmakeMain
            s.startMain = s._CTKstartMain
            s.endMain = s._CTKendMain
            s.makeWin = s._CTKmakeWin
            s.makeButton = s._CTKmakeButton
            s.makeEntry = s._CTKmakeEntry
            s.getEntryText = s._CTKgetEntryText
            s.makeCheckBox = s._CTKmakeCheckBox
            s.getCheckBoxState = s._CTKgetCheckBoxState
            s.makeListBox = s._CTKmakeList
            s.getListBoxItem = s._CTKgetListBoxItem
        elif guiType == "dear" or "dpg":
            global _DPG
            import dearpygui.dearpygui as _DPG
            s.makeMain = s._DPGmakeMain
            s.startMain = s._DPGstartMain
            s.endMain = s._DPGendMain
            s.makeWin = s._DPGmakeWin
            s.makeButton = s._DPGmakebutton
            s.makeEntry = s._DPGmakeEntry
            s.getEntryText = s._DPGgetEntryText
            s.makeCheckBox = s._DPGmakeCheckBox
            s.getCheckBoxState = s._DPGgetCheckBoxState
            s.makeListBox = s._DPGmakeList
            s.getListBoxItem = s._DPGgetListBoxItem
        elif guiType == "$custom":
            s.makeMain = customFrameInsert["makeMain"]
            s.startMain = customFrameInsert["startMain"]
            s.endMain = customFrameInsert["endMain"]
            s.makeWin = customFrameInsert["makeWin"]
            s.makeButton = customFrameInsert["makeButton"]
            s.makeEntry = customFrameInsert["makeEntry"]
            s.getEntryText = customFrameInsert["getEntryText"]
            s.makeCheckBox = customFrameInsert["makeCheckBox"]
            s.getCheckBoxState = customFrameInsert["getCheckBoxState"]
            s.makeListBox = customFrameInsert["makeListBox"]
            s.getListBoxItem = customFrameInsert["getListBoxItem"]
        else: print(f"Invalid guiType | {guiType}"); sys.exit()

    ###################################################
    ###################################################
    ###################################################
    ###################################################
    ###################################################

    def _TKmakeMain(s, titel = "", geometry = [200, 200]):
        win = _TK()
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        win.withdraw()
        s.TK = win
    def _CTKmakeMain(s, titel = "", geometry = [200, 200]):
        win = _CTK.CTk()
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        win.withdraw()
        s.CTK = win
    def _DPGmakeMain(s, titel = "", geometry = [200, 200]):
        _DPG.create_context()
        _DPG.create_viewport(title = titel, width = geometry[0], height = geometry[1])

    def _TKstartMain(s): s.TK.mainloop()
    def _CTKstartMain(s): s.CTK.mainloop()
    def _DPGstartMain(s):
        _DPG.setup_dearpygui()
        _DPG.show_viewport()
        _DPG.start_dearpygui()



    def _TKendMain(s): s.TK.destroy()
    def _CTKendMain(s): s.CTK.destroy()
    def _DPGendMain(s): _DPG.destroy_context()



    def _TKmakeWin(s, titel = "", geometry = [200, 200]): 
        win = _TKINTER.Toplevel(s.TK)
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        return win
    def _CTKmakeWin(s, titel = "", geometry = [200, 200]): 
        win = _CTK.CTkToplevel(s.CTK)
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        return win
    def _DPGmakeWin(s, titel = "", geometry = [200, 200]):
        return _DPG.add_window(label = titel, width = geometry[0], height = geometry[1])



    def _TKmakeButton(s, holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []): 
        button = _TKINTER.Button(holder, text = titel, command = command)
        button.place(x = x, y = y)
        return button
    def _CTKmakeButton(s, holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []): 
        if "offsetY" in others: y += 15

        button = _CTK.CTkButton(holder, text = titel, command = command)
        button.place(x = x, y = y)
        return button
    def _DPGmakebutton(s, holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []):
        if "offsetY" in others: y += 5

        return _DPG.add_button(parent = holder, label = titel, pos = [x, y+20], callback = command)



    def _TKmakeEntry(s, holder, x = 0, y = 0): 
        entry = _TKINTER.Entry(holder)
        entry.place(x = x, y = y)
        return entry
    def _CTKmakeEntry(s, holder, x = 0, y = 0): 
        entry = _CTK.CTkEntry(holder)
        entry.place(x = x, y = y)
        return entry
    def _DPGmakeEntry(s, holder, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 10

        return _DPG.add_input_text(parent = holder, pos = [x, y+20])



    def _TKmakeCheckBox(s, holder, x = 0, y = 0, label = "", command = lambda: ...):
        var = _TKINTER.IntVar()
        entry = _TKINTER.Checkbutton(holder, text = label, command = command, variable = var)
        entry.place(x = x, y = y)
        s.TKcboxvars[entry] = var
        return entry
    def _CTKmakeCheckBox(s, holder, x = 0, y = 0, label = "", command = lambda: ...):
        entry = _CTK.CTkCheckBox(holder, text = label ,command = command)
        entry.place(x = x, y = y + 10)
        return entry
    def _DPGmakeCheckBox(s, holder, x = 0, y = 0, label = "", command = lambda: ..., others = []):
        if "offsetY" in others: y += 20
        return _DPG.add_checkbox(parent = holder, pos = [x, y+20], label = label, callback = command)



    def _TKmakeList(s, holder, contents, x = 0, y = 0, others = []):
        _list = _TTK.Combobox(holder, values = contents)
        _list.place(x = x, y = y)
        return _list
    def _CTKmakeList(s, holder, contents, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 20

        for i in range(len(contents)): contents[i] = str(contents[i])
        _list = _CTK.CTkOptionMenu(holder, values = contents)
        _list.place(x = x, y = y)
        return _list
    def _DPGmakeList(s, holder, contents, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 20

        return _DPG.add_listbox(parent = holder, items = contents, pos = [x, y+20])

    ###################################################
    ###################################################
    ###################################################
    ###################################################
    ###################################################

    def _TKgetEntryText(s, target): """target: _TKINTER.Entry"""; return target.get()
    def _CTKgetEntryText(s, target): """target: _CTK.CTkEntry""" ;return target.get()
    def _DPGgetEntryText(s, target: int): return _DPG.get_value(target)

    def _TKgetCheckBoxState(s, target): """target: _TKINTER.Checkbutton"""; return bool(s.TKcboxvars[target].get())
    def _CTKgetCheckBoxState(s, target): """target: _CTK.CTkCheckBox"""; return bool(target.get())
    def _DPGgetCheckBoxState(s, target: int): return _DPG.get_value(target)

    def _TKgetListBoxItem(s, target): """target: _TKINTER.Listbox"""; return target.selection_get()
    def _CTKgetListBoxItem(s, target): """target: _CTK.CTkOptionMenu"""; return target.get()
    def _DPGgetListBoxItem(s, target: int): return _DPG.get_value(target)