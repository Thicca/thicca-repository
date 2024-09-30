# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.font

class WIDGET():
    def __init__(self):
        self.entry_name = ""
        self.entry_name_list = []
        self.delete_num = 1000
        self.insert_num = 1000
    
    def gen_window(self):
        # create window
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.title(u"Room Match Order")
        root.geometry("400x300")
        font = tk.font.Font(size = 20)
        
        self.entry_name = tk.Message(width = 360, font = font)
        
        # register
        ## text
        self.label_entry = tk.Label(text = u"名前")
        self.label_entry.place(x = 20, y = 10, width = 30, height = 20)
        
        ## text box & process by enter
        self.entry = tk.Entry(root)
        self.entry.bind("<Return>", self.name_register)
        self.entry.place(x = 60, y = 10, width = 250, height = 20)
        
        ## button
        self.button_register = tk.Button(root, text = u"登録")
        self.button_register.bind("<Button-1>", self.name_register)
        self.button_register.place(x = 330, y = 10, width = 50, height = 20)
        
        # delete
        ## text box & process by enter
        self.entry_del = tk.Entry(root)
        self.entry_del.bind("<Return>", self.name_delete)
        self.entry_del.place(x = 20, y = 40, width = 30, height = 20)
        
        ## text
        self.label_delete = tk.Label(text = u"番目を")
        self.label_delete.place(x = 60, y = 40, width = 40, height = 20)
        
        ## button
        self.button_register = tk.Button(root, text = u"削除")
        self.button_register.bind("<Button-1>", self.name_delete)
        self.button_register.place(x = 110, y = 40, width = 50, height = 20)
        
        # insert
        ## text box & process by enter
        self.entry_ins_name = tk.Entry(root)
        self.entry_ins_name.bind("<Return>", self.name_insert)
        self.entry_ins_name.place(x = 20, y = 70, width = 150, height = 20)
        
        ## text
        self.label_insert = tk.Label(text = u"を")
        self.label_insert.place(x = 170, y = 70, width = 30, height = 20)
        
        ## text box & process by enter
        self.entry_ins_num = tk.Entry(root)
        self.entry_ins_num.bind("<Return>", self.name_insert)
        self.entry_ins_num.place(x = 200, y = 70, width = 30, height = 20)
        
        ## text
        self.label_insert2 = tk.Label(text = u"番目に")
        self.label_insert2.place(x = 240, y = 70, width = 40, height = 20)
        
        ## button
        self.button_register = tk.Button(root, text = u"挿入")
        self.button_register.bind("<Button-1>", self.name_insert)
        self.button_register.place(x = 290, y = 70, width = 50, height = 20)
        
        root.mainloop()
    
    def name_register(self, event):
        if self.entry.get():
            self.entry_name_list.append(self.entry.get())
            self.entry.delete(0, tk.END)
            
            self.entry_name["text"] = self.get_list_to_str(self.entry_name_list)
        
            self.entry_name.place(x = 20, y = 100)
    
    def name_delete(self, event):
        try:
            self.delete_num = int(self.entry_del.get())
            if self.delete_num >= 1:
                self.entry_name_list.pop(self.delete_num - 1)
                self.entry_del.delete(0, tk.END)
            
                if self.entry_name:
                    self.entry_name["text"] = self.get_list_to_str(self.entry_name_list)
            else:
                self.entry_del.delete(0, tk.END)
                
            self.entry_name.place(x = 20, y = 100)
        except ValueError:
            self.entry_del.delete(0, tk.END)
        except IndexError:
            self.entry_del.delete(0, tk.END)
        else:
            return True
    
    def name_insert(self, name):
        if self.entry_ins_name.get() and self.entry_ins_num.get():
            try:
                self.insert_num = int(self.entry_ins_num.get())
                if self.insert_num >= 1:
                    self.entry_name_list.insert(self.insert_num - 1, self.entry_ins_name.get())
                    self.entry_ins_name.delete(0, tk.END)
                    self.entry_ins_num.delete(0, tk.END)
                    
                    self.entry_name["text"] = self.get_list_to_str(self.entry_name_list)
                    
                    self.entry_name.place(x = 20, y = 100)
                else:
                    self.entry_ins_name.delete(0, tk.END)
                    self.entry_ins_num.delete(0, tk.END)
            except ValueError:
                self.entry_ins_name.delete(0, tk.END)
                self.entry_ins_num.delete(0, tk.END)
            except IndexError:
                self.entry_ins_name.delete(0, tk.END)
                self.entry_ins_num.delete(0, tk.END)
            else:
                return True
        else:
            self.entry_ins_name.delete(0, tk.END)
            self.entry_ins_num.delete(0, tk.END)
        
    def get_list_to_str(self, arg_list):
        str_list = ""
        for i in range(len(arg_list)):
            str_list += str(i + 1) + ":" + arg_list[i] + " "
        return str_list

widget = WIDGET()
widget.gen_window()