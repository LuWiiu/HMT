import sys
from BetterPY.wrappers import deprecatedFunc

class error():
    versionError = "The version of HMT you are is not the most recent! | verion: {}"
    guiTypeError = "Please pip install the gui you plan to use | guiName: {}"

class gui():
    """
    An "simple" interface to make GUIs that can be translated into any GUI framework that it supports

    Currently supported GUI:
        tk
        cutsomtkenter
        dearpygui
    
    You can modify this code how you want but just know I'm not the best and this is probably bad code to most standards,
    if you do please just give some credit.
    """
    modernVersion = "0.1.4"
    guiType = None
    TKcboxvars = {}
    ANYhelperText = {}
    customFrameInsert = {}
    frame = None
    TK = None
    CTK = None

    def __init__(s, guiType, version, customFrameInsert: dict = {}):

        """

        customFrameInsert is an dict that lets you define your own functions;
        if you are brave enough to make your own equivalent to each function...

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
            "getButtonName": None,
            "setFunc": None,
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
            s.frame = gTK
        elif guiType == "ctk":
            global _TK
            global _CTK
            from tkinter import Tk as _TK
            import customtkinter as _CTK
            s.frame = gCTK
        elif guiType == "dear" or "dpg":
            s.guiType = "dpg"
            global _DPG
            import dearpygui.dearpygui as _DPG
            s.frame = gDPG
        else: print(f"Invalid guiType | {guiType}"); sys.exit()
        GUIcontext.guiSelf = s

    @deprecatedFunc
    def makeMain(s, *args): return s.frame.makeMain(*args)
    @deprecatedFunc
    def startMain(s, *args): return s.frame.startMain(*args)
    @deprecatedFunc
    def endMain(s, *args): return s.frame.endMain(*args)
    @deprecatedFunc
    def makeWin(s, *args): return s.frame.makeWin(*args)
    @deprecatedFunc
    def makeButton(s, *args): return s.frame.makeButton(*args)
    @deprecatedFunc
    def makeEntry(s, *args): return s.frame.makeEntry(*args)
    @deprecatedFunc
    def getEntryText(s, *args): return s.frame.getEntryText(*args)
    @deprecatedFunc
    def getCheckBoxState(s, *args): return s.frame.getCheckBoxState(*args)
    @deprecatedFunc
    def makeCheckBox(s, *args): return s.frame.makeCheckBox(*args)
    @deprecatedFunc
    def getCheckBoxState(s, *args): return s.frame.getCheckBoxState(*args)
    @deprecatedFunc
    def makeListBox(s, *args): return s.frame.makeListBox(*args)
    @deprecatedFunc
    def getListBoxItem(s, *args): return s.frame.getListBoxItem(*args)
    @deprecatedFunc
    def makeText(s, *args): return s.frame.makeText(*args)
    @deprecatedFunc
    def makeHelperInfo(s, *args): return s.frame.makeHelperInfo(*args)

################################################
################################################
################################################
################################################

class GUIcontext:
    guiSelf: gui
class gTK:
    def makeMain(titel = "", geometry = [200, 200]):
        win = _TK()
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        win.withdraw()
        GUIcontext.guiSelf.TK = win
    def startMain():
        GUIcontext.guiSelf.TK.mainloop()
    def endMain():
        GUIcontext.guiSelf.TK.destroy()
    def makeWin(titel = "", geometry = [200, 200]):
            win = _TKINTER.Toplevel(GUIcontext.guiSelf.TK)
            win.title(titel)
            win.geometry(f"{geometry[0]}x{geometry[1]}")
            return win
    def makeButton(holder, titel = "", x = 0, y = 0, command = lambda: ..., *useless):
            button = _TKINTER.Button(holder, text = titel, command = command)
            button.place(x = x, y = y)
            return button
    def makeEntry(holder, x = 0, y = 0, *useless):
            entry = _TKINTER.Entry(holder)
            entry.place(x = x, y = y)
            return entry
    def getEntryText(target):
        return target.get()
    def makeCheckBox(holder, x = 0, y = 0, label = "", command = lambda: ..., *useless):
        var = _TKINTER.IntVar()
        checkBox = _TKINTER.Checkbutton(holder, text = label, command = command, variable = var)
        checkBox.place(x = x, y = y)
        GUIcontext.guiSelf.TKcboxvars[checkBox] = var
        return checkBox
    def getCheckBoxState(target):
        return bool(GUIcontext.guiSelf.TKcboxvars[target].get())
    def makeListBox(holder, contents, x = 0, y = 0, *useless):
        _list = _TTK.Combobox(holder, values = contents)
        _list.place(x = x, y = y)
        return _list
    def getListBoxItem(target):
        return target.selection_get()
    def makeText(holder, text = "", x = 0, y = 0, others = []):
        _text = _TKINTER.Label(holder, text = text)
        _text.place(x = x, y = y)
        if "helperInfo" in others: GUIcontext.guiSelf.ANYhelperText[holder] = _text
        return _text
    def makeHelperInfo(target, info):
        target.bind("<Enter>", lambda a: GUIcontext.guiSelf.frame.makeText(target.master, info, 20, target.master.winfo_height() - 30, ["helperInfo"]))
        target.bind("<Leave>", lambda a: GUIcontext.guiSelf.ANYhelperText[target.master].destroy())
    def getButtonName(target): return target.config('text')[-1]
    def setFunc(target, func): return target.configure(command = func)





class gCTK:
    def makeMain(titel = "", geometry = [200, 200]):
        win = _CTK.CTk()
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        win.withdraw()
        GUIcontext.guiSelf.CTK = win
    def startMain():
        GUIcontext.guiSelf.CTK.mainloop()
    def endMain():
        GUIcontext.guiSelf.CTK.destroy()
    def makeWin(titel = "", geometry = [200, 200]):
        win = _CTK.CTkToplevel(GUIcontext.guiSelf.CTK)
        win.title(titel)
        win.geometry(f"{geometry[0]}x{geometry[1]}")
        return win
    def makeButton(holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []):
        if "offsetY" in others: y += 15
        if "offsetX" in others: x += 120
        button = _CTK.CTkButton(holder, text = titel, command = command)
        button.place(x = x, y = y)
        return button
    def makeEntry(holder, x = 0, y = 0, *useless):
        entry = _CTK.CTkEntry(holder)
        entry.place(x = x, y = y)
        return entry
    def getEntryText(target):
        return target.get()
    def makeCheckBox(holder, x = 0, y = 0, label = "", command = lambda: ..., *useless):
        entry = _CTK.CTkCheckBox(holder, text = label ,command = command)
        entry.place(x = x, y = y + 10)
        return entry
    def getCheckBoxState(target):
        return bool(target.get())
    def makeListBox(holder, contents, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 20
        for i in range(len(contents)): contents[i] = str(contents[i])
        _list = _CTK.CTkOptionMenu(holder, values = contents)
        _list.place(x = x, y = y)
        return _list
    def getListBoxItem(target):
        return target.get()
    def makeText(holder, text = "", x = 0, y = 0, others = []):
        _text = _CTK.CTkLabel(holder, text = text)
        _text.place(x = x, y = y)
        if "helperInfo" in others: GUIcontext.guiSelf.ANYhelperText[holder] = _text
        return _text
    def makeHelperInfo(target, info):
        target.bind("<Enter>", lambda a: GUIcontext.guiSelf.frame.makeText(target.master, info, 20, target.master.winfo_height() - 30, ["helperInfo"]))
        target.bind("<Leave>", lambda a: GUIcontext.guiSelf.ANYhelperText[target.master].destroy())
    def getButtonName(target): return target.cget("text")
    def setFunc(target, func): return target.configure(command = func)




class gDPG:
    def makeMain(titel = "", geometry = [200, 200]):
        _DPG.create_context()
        _DPG.create_viewport(title = titel, width = geometry[0], height = geometry[1])
    def startMain():
        _DPG.setup_dearpygui()
        _DPG.show_viewport()
        _DPG.start_dearpygui()
    def endMain():
        _DPG.destroy_context()
    def makeWin(titel = "", geometry = [200, 200]):
        return _DPG.add_window(label = titel, width = geometry[0], height = geometry[1])
    def makeButton(holder, titel = "", x = 0, y = 0, command = lambda: ..., others = []):
        if "offsetY" in others: y += 25
        return _DPG.add_button(parent = holder, label = titel, pos = [x, y+20], callback = command)
    def makeEntry(holder, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 10
        return _DPG.add_input_text(parent = holder, pos = [x, y+20])
    def getEntryText(target):
        return _DPG.get_value(target)
    def makeCheckBox(holder, x = 0, y = 0, label = "", command = lambda: ..., others = []):
        if "offsetY" in others: y += 20
        return _DPG.add_checkbox(parent = holder, pos = [x, y+20], label = label, callback = command)
    def getCheckBoxState(target):
        return _DPG.get_value(target)
    def makeListBox(holder, contents, x = 0, y = 0, others = []):
        if "offsetY" in others: y += 20
        return _DPG.add_listbox(parent = holder, items = contents, pos = [x, y+20])
    def getListBoxItem(target):
        return _DPG.get_value(target)
    def makeText(holder, text = "", x = 0, y = 0, others = []):
        if "offsetY" in others: y += 20
        _text = _DPG.add_text(text, parent = holder, pos = [x, y+20])
        if "helperInfo" in others: GUIcontext.guiSelf.ANYhelperText = _text
        _DPG.show_item(_text)
        return _text
    def makeHelperInfo(target, info):
        parent = _DPG.get_item_parent(target)
        GUIcontext.guiSelf.ANYhelperText[target] = _DPG.add_text(info, parent = parent, show = False, pos = [20, _DPG.get_item_height(parent) - 30])
        def SHOWorHIDEitem(t):
            if _DPG.is_item_hovered(t): _DPG.show_item(GUIcontext.guiSelf.ANYhelperText[target])
            else: _DPG.hide_item(GUIcontext.guiSelf.ANYhelperText[target])
        with _DPG.handler_registry(): _DPG.add_mouse_move_handler(callback = lambda: SHOWorHIDEitem(t = target), user_data = target)
    def getButtonName(target): _DPG.get_item_label(target)
    def setFunc(target, func): return _DPG.set_item_callback(taget, func)