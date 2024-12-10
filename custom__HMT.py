import sys

class error():
    versionError = "The version of HMT you are is not the most recent! | verion: {}"
    guiTypeError = "Please pip insall the gui you plan to use | guiName: {}"

class gui():
    """
    An "simpel" interface to make GUIs that can be translated into any GUI framework that it supports

    Currently supported GUI:
        tk
        cutsomtkenter
        dearpygui
    
    You can moddify this code how you want but just know I'm not the best and this is probbaly bad code to most standards,
    if you do please just give some credit.
    """
    modernVersion = "0.1.1"
    guiType = None
    TKcboxvars = {}
    ANYhelperText = {}
    customFrameInsert = {}

    def __init__(s, guiType, version, customFrameInsert: dict = {}):

        """

        customFrameInsert is an dict that lets you define your own functions;
        if you are brave enough to make your own equivlent to each function...

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
            "makeHelperInfo": None,
            "makeText": None,
        """

        s.customFrameInsert = customFrameInsert
        s.guiType = guiType
        if version != s.modernVersion: print(error.versionError.format(s.modernVersion))
        if not guiType or guiType == "tk": 
            s.guiType = "tk"
            global _TKINTER
            global _TK
            global _TTK
            import tkinter as _TKINTER
            from tkinter import Tk as _TK
            from tkinter import ttk as _TTK
        elif guiType == "ctk":
            global _TK
            global _CTK
            from tkinter import Tk as _TK
            import customtkinter as _CTK
        elif guiType == "dear" or "dpg":
            s.guiType = "dpg"
            global _DPG
            import dearpygui.dearpygui as _DPG
        else: print(f"Invalid guiType | {guiType}"); sys.exit()

    ###################################################
    ###################################################
    ###################################################
    ###################################################
    ###################################################

    def makeMain(s, titel = "", geometry = [200, 200]):
        match s.guiType:
            case "tk":
                win = _TK()
                win.title(titel)
                win.geometry(f"{geometry[0]}x{geometry[1]}")
                win.withdraw()
                s.TK = win
            case "ctk":
                win = _CTK.CTk()
                win.title(titel)
                win.geometry(f"{geometry[0]}x{geometry[1]}")
                win.withdraw()
                s.CTK = win
            case "dpg":
                _DPG.create_context()
                _DPG.create_viewport(title = titel, width = geometry[0], height = geometry[1])
            case "$custom": return s.customFrameInsert["makeMain"]()

    def startMain(s):
        match s.guiType:
            case "tk": s.TK.mainloop()
            case "ctk": s.CTK.mainloop()
            case "dpg":
                _DPG.setup_dearpygui()
                _DPG.show_viewport()
                _DPG.start_dearpygui()
            case "$custom": return s.customFrameInsert["startMain"]()

    def endMain(s):
        match s.guiType:
            case "tk":  s.TK.destroy()
            case "ctk": s.CTK.destroy()
            case "dpg": _DPG.destroy_context()
            case "$custom": return s.customFrameInsert["endMain"]()

    def makeWin(s, titel = "", geometry = [200, 200]):
        match s.guiType:
            case "tk": 
                win = _TKINTER.Toplevel(s.TK)
                win.title(titel)
                win.geometry(f"{geometry[0]}x{geometry[1]}")
                return win
            case "ctk":
                win = _CTK.CTkToplevel(s.CTK)
                win.title(titel)
                win.geometry(f"{geometry[0]}x{geometry[1]}")
                return win
            case "dpg": return _DPG.add_window(label = titel, width = geometry[0], height = geometry[1])
            case "$custom": return s.customFrameInsert["makeWin"]()

    def makeButton(s, holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []):
        match s.guiType:
            case "tk":
                button = _TKINTER.Button(holder, text = titel, command = command)
                button.place(x = x, y = y)
                return button
            case "ctk":
                if "offsetY" in others: y += 15
                button = _CTK.CTkButton(holder, text = titel, command = command)
                button.place(x = x, y = y)
                return button
            case "dpg":
                if "offsetY" in others: y += 5
                return _DPG.add_button(parent = holder, label = titel, pos = [x, y+20], callback = command)
            case "$custom": return s.customFrameInsert["makeButton"]()

    def makeEntry(s, holder, x = 0, y = 0, others = []):
        match s.guiType:
            case "tk":
                entry = _TKINTER.Entry(holder)
                entry.place(x = x, y = y)
                return entry
            case "ctk":
                entry = _CTK.CTkEntry(holder)
                entry.place(x = x, y = y)
                return entry
            case "dpg":
                if "offsetY" in others: y += 10
                return _DPG.add_input_text(parent = holder, pos = [x, y+20])
            case "$custom": return s.customFrameInsert["makeEntry"]()

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

    def makeListBox(s, holder, contents, x = 0, y = 0, others = []):
        match s.guiType:
            case "tk":
                _list = _TTK.Combobox(holder, values = contents)
                _list.place(x = x, y = y)
                return _list
            case "ctk":
                if "offsetY" in others: y += 20
                for i in range(len(contents)): contents[i] = str(contents[i])
                _list = _CTK.CTkOptionMenu(holder, values = contents)
                _list.place(x = x, y = y)
                return _list
            case "dpg":
                if "offsetY" in others: y += 20
                return _DPG.add_listbox(parent = holder, items = contents, pos = [x, y+20])
            case "$custom": return s.customFrameInsert["makeListBox"]()

    def makeText(s, holder, text = "", x = 0, y = 0, others = []):
        match s.guiType:
            case "tk":
                _text = _TKINTER.Label(holder, text = text)
                _text.place(x = x, y = y)
                if "helperInfo" in others: s.ANYhelperText[holder] = _text
                return _text
            case "ctk":
                _text = _CTK.CTkLabel(holder, text = text)
                _text.place(x = x, y = y)
                if "helperInfo" in others: s.ANYhelperText[holder] = _text
                return _text
            case "dpg":
                if "offsetY" in others: y += 20
                _text = _DPG.add_text(text, parent = holder, pos = [x, y+20])
                if "helperInfo" in others: s.ANYhelperText = _text
                _DPG.show_item(_text)
                return _text
            case "$custom": return s.customFrameInsert["makeText"]()

    def makeHelperInfo(s, target, info):
        match s.guiType:
            case "tk":
                target.bind("<Enter>", lambda a: s.makeText(target.master, info, 20, target.master.winfo_height() - 30, ["helperInfo"]))
                target.bind("<Leave>", lambda a: s.ANYhelperText[target.master].destroy())
            case "ctk":
                target.bind("<Enter>", lambda a: s.makeText(target.master, info, 20, target.master.winfo_height() - 30, ["helperInfo"]))
                target.bind("<Leave>", lambda a: s.ANYhelperText[target.master].destroy())
            case "dpg":
                parent = _DPG.get_item_parent(target)
                s.ANYhelperText[target] = _DPG.add_text(info, parent = parent, show = False, pos = [20, _DPG.get_item_height(parent) - 30])
                def SHOWorHIDEitem(t):
                    if _DPG.is_item_hovered(t): _DPG.show_item(s.ANYhelperText[target])
                    else: _DPG.hide_item(s.ANYhelperText[target])
                with _DPG.handler_registry(): _DPG.add_mouse_move_handler(callback = lambda: SHOWorHIDEitem(t = target), user_data = target)
            case "$custom": return s.customFrameInsert["makeHelperInfo"]()

    ###################################################
    ###################################################
    ###################################################
    ###################################################
    ###################################################

    def getEntryText(s, target):
        match s.guiType:
            case "tk": return target.get()
            case "ctk":return target.get()
            case "dpg":return _DPG.get_value(target)
            case "$custom": return s.customFrameInsert["getEntryText"]()

    def getCheckBoxState(s, target):
        match s.guiType:
            case "tk": return bool(s.TKcboxvars[target].get())
            case "ctk": return bool(target.get())
            case "dpg": return _DPG.get_value(target)
            case "$custom": return s.customFrameInsert["getCheckBoxState"]()

    def getListBoxItem(s, target):
        match s.guiType:
            case "tk": return target.selection_get()
            case "ctk": return target.get()
            case "dpg": return _DPG.get_value(target)
            case "$custom": return s.customFrameInsert["getListBoxItem"]()
