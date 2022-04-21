#!/usr/bin/python
# -*- coding: UTF-8 -*-

import serial.tools.list_ports
import platform
import time
from subprocess import call
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msgbox
from languages import *

class App:
    def __init__(self):
        self.win = Tk()
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.win.geometry('720x360+260+200')
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.win.geometry('720x306+260+200')
        self.win.update()
        tk.Grid.rowconfigure(self.win, 0, weight=1)
        tk.Grid.columnconfigure(self.win, 0, weight=1)
        self.language = Language('eng')
        self.initWidgets()
        print("当前窗口的宽度为", self.win.winfo_width())
        print("当前窗口的高度为", self.win.winfo_height())
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus

    def refreshLabels(self, language):
        self.lanDict = {
            self.labFileDir: language.labFileDir,
            self.btnFileDir: language.btnFileDir,
            self.labPort: language.labPort,
            self.labProduct: language.labProduct,
            self.labMode: language.labMode,
            self.rbnModes[0]: language.rbnModes[0],
            self.rbnModes[1]: language.rbnModes[1],
            self.rbnModes[2]: language.rbnModes[2],
            self.labFile: language.labFile,
            self.checkBnWI: language.cbnFileWI,
            self.checkBnOC: language.cbnFileMF,
            self.labNote: language.labNote,
            self.btnUpload: language.btnUpload
        }

        self.win.title(language.title)

        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.win.iconbitmap(r'./images/Petoi.ico')
            self.menuBar = Menu(self.win)
            self.win.configure(menu=self.menuBar)
            self.LanguageMenu = Menu(self.menuBar, tearoff=0)
            self.menuBar.add_cascade(label=language.labTrans, menu=self.LanguageMenu)
            self.LanguageMenu.add_command(label=language.labEng, command=self._eng)
            self.LanguageMenu.add_command(label=language.labChi, command=self._chi)
            self.menuBar.add_command(label=language.labAbout, command=self.about)
            self.menuBar.add_command(label=language.labExit, command=self.win.quit)
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            menubar = Menu(self.win, background='#ff8000', foreground='black', activebackground='white',
                           activeforeground='black')
            lan = Menu(menubar, tearoff=0)
            lan.add_command(label=language.labEng, command=self._eng)
            lan.add_command(label=language.labChi, command=self._chi)
            menubar.add_cascade(label=language.labTrans, menu=lan)
            help = Menu(menubar, tearoff=1)
            help.add_command(label=language.labAbout, command=self.about)
            menubar.add_cascade(label=language.labAbout, menu=help)
            ext = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
            ext.add_command(label=language.labExit, command=self.win.quit)
            menubar.add_cascade(label=language.labExit, menu=ext)
            self.win.config(menu=menubar)

        for key in self.lanDict:
            key.configure(text=self.lanDict[key])

    def _chi(self):
        self.language = Language('chi')
        self.refreshLabels(self.language)

    def _eng(self):
        self.language = Language('eng')
        self.refreshLabels(self.language)

    def initWidgets(self):
        self.win.title(self.language.title)

        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.win.iconbitmap(r'./images/Petoi.ico')
            self.menuBar = Menu(self.win)
            self.win.configure(menu=self.menuBar)
            self.LanguageMenu = Menu(self.menuBar, tearoff=0)
            self.menuBar.add_cascade(label=self.language.labTrans, menu=self.LanguageMenu)
            self.LanguageMenu.add_command(label=self.language.labEng, command=self._eng)
            self.LanguageMenu.add_command(label=self.language.labChi, command=self._chi)
            self.menuBar.add_command(label=self.language.labAbout, command=self.about)
            self.menuBar.add_command(label=self.language.labExit, command=self.win.quit)
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.win.iconbitmap(r'./logo.icns')
            self.win.option_add('*tearOff', FALSE)
            menubar = Menu(self.win, background='#ff8000', foreground='black', activebackground='white',
                           activeforeground='black')
            lan = Menu(menubar, tearoff=0)
            lan.add_command(label=self.language.labEng, command=self._eng)
            lan.add_command(label=self.language.labChi, command=self._chi)
            menubar.add_cascade(label=self.language.labTrans, menu=lan)
            help = Menu(menubar, tearoff=1)
            help.add_command(label=self.language.labAbout, command=self.about)
            menubar.add_cascade(label=self.language.labAbout, menu=help)
            ext = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
            ext.add_command(label=self.language.labExit, command=self.win.quit)
            menubar.add_cascade(label=self.language.labExit, menu=ext)
            self.win.config(menu=menubar)

        self.stFileDir = StringVar()
        self.stPort = StringVar()
        self.stStatus = StringVar()
        self.stStatus.set(' ')
        self.strProduct = StringVar()
        self.strProduct.set('Bittle')
        self.intMode = IntVar()
        self.strMode = StringVar()
        self.strFileName = StringVar()

        f = open("./defaultpath.txt", "r")  # 设置文件对象
        strDefaultPath = f.read()  # 将txt文件的所有内容读入到字符串str中
        print(strDefaultPath)
        f.close()  # 将文件关闭
        self.stFileDir.set(strDefaultPath)

        # 设置 Button 字体
        style = ttk.Style()
        # style.configure('my.TButton', font=('Arial', 14), background='gray')
        style.configure('my.TRadiobutton', font=('Arial', 12))
        style.configure('my.TCheckbutton', font=('Arial', 12))
        # style.configure('my.TEntry', background='white')

        product = ('Bittle', 'Nybble')

        # fmFileDir = ttk.Frame(self.win)
        fmFileDir = tk.Frame(self.win)
        # fmFileDir.pack(side=TOP, fill=BOTH, expand=YES)
        fmFileDir.grid(row=0, ipadx=2, padx=2, sticky=W + E + N + S)
        # self.labFileDir = ttk.Label(fmFileDir, text=self.language.labFileDir, font=('Arial', 16))
        self.labFileDir = tk.Label(fmFileDir, text=self.language.labFileDir, font=('Arial', 16))
        self.labFileDir.grid(row=0, columnspan=2, ipadx=2, padx=2, sticky=W)

        # self.entry = ttk.Entry(fmFileDir, textvariable=self.stFileDir,
        #                        font=('Arial', 12),
        #                        foreground='green', style='my.TEntry')
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.entry = tk.Entry(fmFileDir, textvariable=self.stFileDir,
                               font=('Arial', 16), foreground='green', background='white')
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.entry = tk.Entry(fmFileDir, textvariable=self.stFileDir,
                                  font=('Arial', 12), foreground='green', background='white')
        self.entry.grid(row=1, column=0, ipadx=5, padx=5, sticky=E + W)
        # self.btnFileDir = ttk.Button(fmFileDir, text=self.language.btnFileDir, style='my.TButton', width=12,
        #            command=self.open_dir)  # 绑定 open_dir 方法
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.btnFileDir = tk.Button(fmFileDir, text=self.language.btnFileDir, font=('Arial', 14), foreground='blue',
                                        command=self.open_dir)  # 绑定 open_dir 方法
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.btnFileDir = tk.Button(fmFileDir, text=self.language.btnFileDir, font=('Arial', 14), foreground='blue',
                                        background='gray', command=self.open_dir)  # 绑定 open_dir 方法
        self.btnFileDir.grid(row=1, column=1, ipadx=5, padx=5, sticky=E + W)
        fmFileDir.columnconfigure(0, weight=8)  # 尺寸适配
        fmFileDir.columnconfigure(1, weight=1)  # 尺寸适配
        fmFileDir.rowconfigure(1, weight=1)  # 尺寸适配

        fmSerial = ttk.Frame(self.win)
        fmSerial.grid(row=1, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labPort = ttk.Label(fmSerial, text=self.language.labPort, font=('Arial', 16))
        self.labPort.grid(row=0, ipadx=5, padx=5, sticky=W)
        cb = ttk.Combobox(fmSerial, textvariable=self.stPort, width=20, font=12)

        # list of serial port number
        port_list_number = []
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            port_list_number = [' ']
            print("The Serial port can't find!")
        else:
            for each_port in port_list:
                port_list_number.append(each_port[0])
        # 为 Combobox 设置列表项
        cb['values'] = port_list_number
        cb.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmProduct = ttk.Frame(self.win)
        fmProduct.grid(row=2, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labProduct = ttk.Label(fmProduct, text=self.language.labProduct, font=('Arial', 16))
        self.labProduct.grid(row=0, column=0, ipadx=5, padx=5, sticky=W)
        c = 1
        for p in product:
            rbProduct = ttk.Radiobutton(fmProduct, text=p, value=p, style='my.TRadiobutton',
                                     variable=self.strProduct, command=self.chooseProduct)
            rbProduct.grid(row=0, column=c, ipadx=5, padx=5, sticky=W) # pack(side=LEFT, padx=5)
            c += 1
        self.strProduct.set('Bittle')

        fmMode = ttk.Frame(self.win)
        fmMode.grid(row=3, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labMode = ttk.Label(fmMode, text=self.language.labMode, font=('Arial', 16))
        self.labMode.grid(row=0, column=0, ipadx=5, padx=5, sticky=W)
        c = 1
        self.rbnModes = []
        for i in range(len(self.language.rbnModes)):
            rbMode = ttk.Radiobutton(fmMode, text=self.language.rbnModes[i], value=i, style='my.TRadiobutton',
                                     variable=self.intMode, command=self.chooseMode)
            rbMode.grid(row=0, column=c, ipadx=5, padx=5, sticky=W)
            self.rbnModes.append(rbMode)
            c += 1
        self.strMode.set('Walk')
        self.strFileName.set("OpenCat" + self.strMode.get() + ".ino.hex")

        fmUploadFile = ttk.Frame(self.win)
        fmUploadFile.grid(row=4, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labFile = ttk.Label(fmUploadFile, text=self.language.labFile, font=('Arial', 16))
        self.labFile.grid(row=0, column=0, padx=5, sticky=W)

        self.intVarWI = IntVar()
        self.intVarWI.set(1)
        self.checkBnWI = ttk.Checkbutton(fmUploadFile, text=self.language.cbnFileWI, style='my.TCheckbutton',    # font=('Arial', 12),
                                 variable=self.intVarWI, onvalue=1, offvalue=0,    # 默认选中
                                 command=self.changeSelect)    # 将选中事件绑定到self.changeSelect方法
        self.checkBnWI.grid(row=0, column=1,  sticky=W)
        self.intVarOC = IntVar()
        self.intVarOC.set(1)
        self.checkBnOC = ttk.Checkbutton(fmUploadFile, text=self.language.cbnFileMF, style='my.TCheckbutton',     # font=('Arial', 12),
                                    variable=self.intVarOC, onvalue=1, offvalue=0,  # 默认选中
                                    command=self.changeSelect)  # 将选中事件绑定到self.changeSelect方法
        self.checkBnOC.grid(row=0, column=2, ipadx=5, padx=5, sticky=W)

        fmNote = ttk.Frame(self.win)
        fmNote.grid(row=5, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        self.labNote = ttk.Label(fmNote, text=self.language.labNote, font=('Arial', 12), foreground='red')
        self.labNote.grid(row=0, ipadx=5, padx=5, sticky=W)

        # fmUpload = ttk.Frame(self.win)
        fmUpload = tk.Frame(self.win)
        fmUpload.grid(row=6, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        # self.btnUpload = ttk.Button(fmUpload, text=self.language.btnUpload, style='my.TButton',  command=self.autoupload)    # 绑定 autoupload 方法
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.btnUpload = tk.Button(fmUpload, text=self.language.btnUpload, font=('Arial', 14), foreground='blue',
                                       command=self.autoupload)  # 绑定 autoupload 方法
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.btnUpload = tk.Button(fmUpload, text=self.language.btnUpload, font=('Arial', 14), foreground='blue',
                                       background='gray', command=self.autoupload)    # 绑定 autoupload 方法
        self.btnUpload.grid(row=0, ipadx=5, padx=5, sticky=W + E + N + S)
        fmUpload.columnconfigure(0, weight=1)  # 尺寸适配
        fmUpload.rowconfigure(0, weight=1)  # 尺寸适配

        fmStatus = ttk.Frame(self.win)
        fmStatus.grid(row=7, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        self.statusBar = ttk.Label(fmStatus, textvariable=self.stStatus, font=('Arial', 16), relief=SUNKEN)
        self.statusBar.grid(row=0, ipadx=5, padx=5, sticky=W + E + N + S)
        fmStatus.columnconfigure(0, weight=1)  # 尺寸适配
        fmStatus.rowconfigure(0, weight=1)  # 尺寸适配


    def about(self):
        self.msgbox = msgbox.showinfo(self.language.titleVersion, self.language.msgVersion)


    def chooseProduct(self):
        print("self.strProduct is " + self.strProduct.get())

    def chooseMode(self):
        if self.intMode.get() == 0:
            self.strMode.set("Walk")
        elif self.intMode.get() == 1:
            self.strMode.set("Ultrasonic")
        elif self.intMode.get() == 2:
            self.strMode.set("Camera")
        print(self.strMode.get())
        self.strFileName.set("OpenCat" + self.strMode.get() + ".ino.hex")
        print(self.strFileName.get())

    def formalize(self, strdir=' '):
        sep = "/"
        listDir = strdir.split("/")
        print("listDir:" + str(listDir))
        if (listDir[-1] == "FlashUploader"):
            strdir = sep.join(listDir) + '/release'
        else:
            if (listDir[-1].find("release") == -1) and len(listDir) >= 2:
                while listDir[-1].find("release") == -1 and len(listDir) >= 2:
                    listDir = listDir[:-1]
                if listDir[-1] != "release":
                    strdir = " "
                else:
                    strdir = sep.join(listDir)
        print("strdir: " + strdir)
        self.stFileDir.set(strdir)
        print("self.stFileDir:" + self.stFileDir.get())

    def open_dir(self):
        # 调用 askdirectory 方法打开目录
        dirpath = filedialog.askdirectory(title=self.language.titleFileDir,
                                          initialdir=self.stFileDir)    # 初始目录
        if dirpath:
            self.formalize(dirpath)
            with open('./defaultpath.txt', 'w') as f:  # 设置文件对象
                f.write(self.stFileDir.get())  # 将字符串写入文件中
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus


    def changeSelect(self):
        print("self.intVarWI:" + str(self.intVarWI.get()))
        print("self.intVarOC:" + str(self.intVarOC.get()))

    def autoupload(self):
        strProd = self.strProduct.get()
        strFileName = self.strFileName.get()
        fnWriteI = self.stFileDir.get() + "/" + strProd + "/WriteInstinct.ino.hex"
        fnOpenCat = self.stFileDir.get() + "/" + strProd + "/" + strFileName
        filename = [fnWriteI, fnOpenCat]
        print(filename)
        port = self.stPort.get()
        print(self.stPort.get())

        if self.stFileDir.get() == '' or self.stFileDir.get() == ' ':
            msgbox.showwarning(self.language.titleWarning, self.language.msgFileDir)
            return False

        if port == ' ' or port == '':
            msgbox.showwarning(self.language.titleWarning, self.language.msgPort)
            return False

        self.stStatus.set(self.language.labStatus1)
        self.statusBar.update()

        ret = 0
        for file in filename:
            if (self.intVarWI.get() == 0) and (file == fnWriteI):
                continue
            if (self.intVarOC.get() == 0) and (file == fnOpenCat):
                continue
            if platform.system()=="Darwin" or platform.system()=="Linux":
                ret = call('./avrdude -C./avrdude.conf -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                           (port, file), shell=True)
            else:
                ret = call('./avrdude -C./avrdude.conf -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                            (port, file), shell=False)
            print("ret = " + str(ret))

            if ret != 0 and file == fnWriteI:
                self.stStatus.set(self.language.cbnFileWI + self.language.labStatus2)
                self.statusBar.update()
                return
            elif ret != 0 and file == fnOpenCat:
                self.stStatus.set(self.language.cbnFileMF + self.language.labStatus2)
                self.statusBar.update()
                return

            if ret == 0 and file == fnWriteI and self.intVarOC.get() == 1:
                time.sleep(10)

        if ret == 0:
            self.stStatus.set(self.language.labStatus3)
            self.statusBar.update()

        print('Finish!')
        return True


app = App()
app.win.mainloop()
