#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import serial.tools.list_ports
from SerialCommunication import *    # module SerialCommunication.py
import logging
import platform
import time
from subprocess import call
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msgbox
from languages import *

FORMAT = '%(asctime)-15s %(name)s - %(levelname)s - %(message)s'
'''
Level: The level determines the minimum priority level of messages to log. 
Messages will be logged in order of increasing severity: 
DEBUG is the least threatening, 
INFO is also not very threatening, 
WARNING needs attention, 
ERROR needs immediate attention, 
and CRITICAL means “drop everything and find out what’s wrong.” 
The default starting point is INFO, 
which means that the logging module will automatically filter out any DEBUG messages.
'''
# logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

class App:
    def __init__(self):
        self.win = Tk()
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.win.geometry('530x450+260+100')
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.win.geometry('530x356+260+200')
        self.win.update()
        tk.Grid.rowconfigure(self.win, 0, weight=1)
        tk.Grid.columnconfigure(self.win, 0, weight=1)
        self.language = Language('eng')
        self.initWidgets()
        print("当前窗口的宽度为", self.win.winfo_width())
        print("当前窗口的高度为", self.win.winfo_height())
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus

    def refreshLabels(self, language):
        if self.strProduct.get() == 'Bittle':
            modeTuple = language.rbnBittleModes
        elif self.strProduct.get() == 'Nybble':
            modeTuple = language.rbnNybbleModes

        self.lanDict = {
            self.labFileDir: language.labFileDir,
            self.btnFileDir: language.btnFileDir,
            self.labPort: language.labPort,
            self.labProduct: language.labProduct,
            self.labMode: language.labMode,
            self.rbnModes[0]: modeTuple[0],
            self.rbnModes[1]: modeTuple[1],
            self.rbnModes[2]: modeTuple[2],
            self.rbnModes[3]: modeTuple[3],
            self.labFile: language.labFile,
            self.checkBnWI: language.cbnFileWI,
            self.checkBnOC: language.cbnFileMF,
            # self.labNote: language.labNote,
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
        self.strSoftwareVersion = StringVar()
        self.strSoftwareVersion.set('2.0')
        self.strBoardVersion = StringVar()
        self.strBoardVersion.set('NyBoard_V1_0')
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
        style.configure('my.TRadiobutton', font=('Arial', 15))
        style.configure('my.TCheckbutton', font=('Arial', 15))
        # style.configure('my.TEntry', background='white')

        product = ('Bittle', 'Nybble')

        # fmFileDir = ttk.Frame(self.win)
        fmFileDir = tk.Frame(self.win)
        # fmFileDir.pack(side=TOP, fill=BOTH, expand=YES)
        fmFileDir.grid(row=0, ipadx=2, padx=2, sticky=W + E + N + S)
        # self.labFileDir = ttk.Label(fmFileDir, text=self.language.labFileDir, font=('Arial', 16))
        self.labFileDir = tk.Label(fmFileDir, text=self.language.labFileDir, font=('Arial', 16))
        self.labFileDir.grid(row=0, column=0, ipadx=2, padx=2, sticky=W)
        # self.btnFileDir = ttk.Button(fmFileDir, text=self.language.btnFileDir, style='my.TButton', width=12,
        #            command=self.open_dir)  # 绑定 open_dir 方法
        if self.win.call('tk', 'windowingsystem') == 'win32':
            self.btnFileDir = tk.Button(fmFileDir, text=self.language.btnFileDir, font=('Arial', 14), foreground='blue',
                                        command=self.open_dir)  # 绑定 open_dir 方法
        elif self.win.call('tk', 'windowingsystem') == 'aqua':
            self.btnFileDir = tk.Button(fmFileDir, text=self.language.btnFileDir, font=('Arial', 14), foreground='blue',
                                        background='gray', command=self.open_dir)  # 绑定 open_dir 方法
        self.btnFileDir.grid(row=0, column=1, ipadx=5, padx=5, sticky=E)

        # self.entry = ttk.Entry(fmFileDir, textvariable=self.stFileDir,
        #                        font=('Arial', 12),
        #                        foreground='green', style='my.TEntry')
        # if self.win.call('tk', 'windowingsystem') == 'win32':
        #     self.entry = tk.Entry(fmFileDir, textvariable=self.stFileDir,
        #                        font=('Arial', 16), foreground='green', background='white')
        # elif self.win.call('tk', 'windowingsystem') == 'aqua':
        self.entry = tk.Entry(fmFileDir, textvariable=self.stFileDir,
                                  font=('Arial', 16), foreground='green', background='white')
        self.entry.grid(row=1, columnspan=2, ipadx=5, padx=5, sticky=E + W)
        
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
            if len(port_list) == 1:
                cb.set(port_list[0][0])
            for each_port in port_list:
                port_list_number.append(each_port[0])
        # 为 Combobox 设置列表项
        cb['values'] = port_list_number
        cb.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmSoftwareVersion = ttk.Frame(self.win)
        fmSoftwareVersion.grid(row=2, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labSoftwareVersion = ttk.Label(fmSoftwareVersion, text=self.language.labSoftwareVersion, font=('Arial', 16))
        self.labSoftwareVersion.grid(row=0, ipadx=5, padx=5, sticky=W)
        cbSoftwareVersion = ttk.Combobox(fmSoftwareVersion, textvariable=self.strSoftwareVersion, width=20, font=12)
        cbSoftwareVersion.bind("<<ComboboxSelected>>",self.chooseSoftwareVersion)

        # list of board version
        software_version_list = ['1.0', '2.0']
        # 为 Combobox 设置默认项
        cbSoftwareVersion.set(software_version_list[1])
        # 为 Combobox 设置列表项
        cbSoftwareVersion['values'] = software_version_list
        cbSoftwareVersion.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmBoardVersion = ttk.Frame(self.win)
        fmBoardVersion.grid(row=3, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labBoardVersion = ttk.Label(fmBoardVersion, text=self.language.labBoardVersion, font=('Arial', 16))
        self.labBoardVersion.grid(row=0, ipadx=5, padx=5, sticky=W)
        cbBoardVersion = ttk.Combobox(fmBoardVersion, textvariable=self.strBoardVersion, width=20, font=12)

        # list of board version
        board_version_list = ['NyBoard_V1_0', 'NyBoard_V1_1']
        # 为 Combobox 设置默认项
        cbBoardVersion.set(board_version_list[0])
        # 为 Combobox 设置列表项
        cbBoardVersion['values'] = board_version_list
        cbBoardVersion.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmProduct = ttk.Frame(self.win)
        fmProduct.grid(row=4, ipadx=2, padx=2, sticky=W + E + N + S)
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
        fmMode.grid(row=5, ipadx=2, padx=2, sticky=W + E + N + S)
        self.labMode = ttk.Label(fmMode, text=self.language.labMode, font=('Arial', 16))
        self.labMode.grid(row=0, column=0, ipadx=5, padx=5, sticky=W)
        c = 0
        self.rbnModes = []
        if self.strProduct.get() == 'Bittle':
            modeTuple = self.language.rbnBittleModes
        elif self.strProduct.get() == 'Nybble':
            modeTuple = self.language.rbnNybbleModes

        for i in range(len(modeTuple)):
            rbMode = ttk.Radiobutton(fmMode, text=modeTuple[i], value=i, style='my.TRadiobutton',
                                     variable=self.intMode, state=NORMAL, command=self.chooseMode)
            rbMode.grid(row=1, column=c, ipadx=5, padx=5, sticky=W)
            self.rbnModes.append(rbMode)
            c += 1
        self.strMode.set('Standard')
        self.strFileName.set("OpenCat" + self.strMode.get() + ".ino.hex")

        fmUploadFile = ttk.Frame(self.win)
        fmUploadFile.grid(row=6, ipadx=2, padx=2, sticky=W + E + N + S)
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

        # fmNote = ttk.Frame(self.win)
        # fmNote.grid(row=5, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        # self.labNote = ttk.Label(fmNote, text=self.language.labNote, font=('Arial', 12), foreground='red')
        # self.labNote.grid(row=0, ipadx=5, padx=5, sticky=W)

        # fmUpload = ttk.Frame(self.win)
        fmUpload = tk.Frame(self.win)
        fmUpload.grid(row=7, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
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
        fmStatus.grid(row=8, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        self.statusBar = ttk.Label(fmStatus, textvariable=self.stStatus, font=('Arial', 16), relief=SUNKEN)
        self.statusBar.grid(row=0, ipadx=5, padx=5, sticky=W + E + N + S)
        fmStatus.columnconfigure(0, weight=1)  # 尺寸适配
        fmStatus.rowconfigure(0, weight=1)  # 尺寸适配


    def about(self):
        self.msgbox = msgbox.showinfo(self.language.titleVersion, self.language.msgVersion)
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus


    def chooseSoftwareVersion(self, event):
        if self.strSoftwareVersion.get() == '1.0':
            stt = DISABLED
            self.intMode.set(0)
            self.strMode.set('Standard')
            print(self.strMode.get())
            self.strFileName.set("OpenCat" + self.strMode.get() + ".ino.hex")
            print(self.strFileName.get())
        else:
            stt = NORMAL
        for i in range(1,4):
            self.rbnModes[i].configure(state=stt)


    def chooseProduct(self):
        print("self.strProduct is " + self.strProduct.get())
        
        if self.strProduct.get() == 'Bittle':
            modeTuple = self.language.rbnBittleModes
        elif self.strProduct.get() == 'Nybble':
            modeTuple = self.language.rbnNybbleModes

        for i in range(len(modeTuple)):
            self.rbnModes[i].configure(text=modeTuple[i])

        if (self.strProduct.get() == 'Bittle' and self.strMode.get() == "Ultrasonic") \
            or (self.strProduct.get() == 'Nybble' and self.strMode.get() == "Camera"):
            msgbox.showwarning(self.language.titleWarning, self.language.msgMode)
            self.intMode.set(0)
            self.strMode.set('Standard')
            print(self.strMode.get())
            self.strFileName.set("OpenCat" + self.strMode.get() + ".ino.hex")
            print(self.strFileName.get())
            self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus


    def chooseMode(self):
        # if self.intMode.get() == 0:
        #     self.strMode.set("Standard")
        # elif self.intMode.get() == 1:
        #     self.strMode.set("Ultrasonic")
        # elif self.intMode.get() == 2:
        #     self.strMode.set("Camera")
        if self.strProduct.get() == 'Bittle':
            mode = "Camera"
        elif self.strProduct.get() == 'Nybble':
            mode = "Ultrasonic"
        switcher = {
            0 : "Standard",
            1 : "Random_Mind",
            2 : "Voice",
            3 : mode
        }
        self.strMode.set(switcher.get(self.intMode.get(), "Invalid num of selection"))
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
        logger.debug(f"{self.stFileDir.get()}")
        if (self.stFileDir.get()).find('./release') != -1:
            dirpath = filedialog.askdirectory(title=self.language.titleFileDir,
                                          initialdir=r'./release')    # 初始目录
        else:
            dirpath = filedialog.askdirectory(title=self.language.titleFileDir,
                                              initialdir=self.stFileDir)  # 用户自定目录

        if dirpath:
            self.formalize(dirpath)
            with open('./defaultpath.txt', 'w') as f:  # 设置文件对象
                f.write(self.stFileDir.get())  # 将字符串写入文件中
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus


    def changeSelect(self):
        print("self.intVarWI:" + str(self.intVarWI.get()))
        print("self.intVarOC:" + str(self.intVarOC.get()))


    def encode(self, in_str, encoding='utf-8'):
        if isinstance(in_str, bytes):
            return in_str
        else:
            return in_str.encode(encoding)


    def WriteInstinctProcess(self, port):
        ser = Communication(port, 115200, 0.5)
        logger.info(f"Connect to usb serial port: {port}.")
        strSoftwareVersion = self.strSoftwareVersion.get()
        bRest = False
        bCalibrate = False
        bUploadInst = False
        while True:
            time.sleep(0.01)
            if ser.main_engine.in_waiting > 0:
                x = str(ser.main_engine.readline())
                logger.debug(f"{x}")
                if x != "":
                    questionMark = "Y/n"
                    if x.find(questionMark) != -1:
                        if x.find("Calibrate") != -1:
                            if strSoftwareVersion == '2.0':
                                if bRest == True:
                                    self.stStatus.set(self.language.labStatusRest22)
                                elif bRest == False:
                                    self.stStatus.set(self.language.labStatusUploadInst12)
                            elif strSoftwareVersion == '1.0':
                                if bUploadInst == True:
                                    self.stStatus.set(self.language.labStatusUploadInst12)
                            self.statusBar.update()
                            retMsg = msgbox.askyesno(self.language.titleWarning, self.language.msgCalibrateIMU)
                        elif x.find("Reset") != -1:
                            retMsg = msgbox.askyesno(self.language.titleWarning, self.language.msgRstOffsets)
                        else:
                            if bRest == True:
                                self.stStatus.set(self.language.labStatusRest12)
                                self.statusBar.update()
                            retMsg = msgbox.askyesno(self.language.titleWarning, x[2:-5])
                        self.win.update()
                        if retMsg == True:
                            ser.Send_data(self.encode("Y"))
                            if strSoftwareVersion == '1.0':
                                if x.find("Reset") != -1:
                                    bRest = True
                                    self.stStatus.set(self.language.labStatusRest1)
                                elif x.find("Calibrate") != -1:
                                    bCalibrate = True
                                    self.stStatus.set(self.language.labStatusCalibrate)
                                else:
                                    bUploadInst = True
                                    self.stStatus.set(self.language.labStatusUploadInst1)
                                self.statusBar.update()
                            else:
                                if x.find("Reset") != -1:
                                    bRest = True
                                    self.stStatus.set(self.language.labStatusRest2)
                                elif x.find("Calibrate") != -1:
                                    bCalibrate = True
                                    self.stStatus.set(self.language.labStatusCalibrate)
                                self.statusBar.update()

                        elif retMsg == False:
                            ser.Send_data(self.encode("n"))
                            if x.find("Reset") != -1 and strSoftwareVersion == '2.0':
                                self.stStatus.set(self.language.labStatusUploadInst1)
                                self.statusBar.update()
                            if x.find("Calibrate") != -1:
                                break
                    elif x.find("sent to mpu.setXAccelOffset") != -1 or x.find("Ready!") != -1:
                        if retMsg == True and bCalibrate == True:
                            self.stStatus.set(self.language.labStatusCalibrate2)
                            self.statusBar.update()
                        break
        ser.Close_Engine()
        logger.info("close the serial port.")
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus


    def autoupload(self):
        strProd = self.strProduct.get()
        strSoftwareVersion = self.strSoftwareVersion.get()
        strBoardVersion = self.strBoardVersion.get()

        strFileName = self.strFileName.get()
        fnWriteI = self.stFileDir.get() + "/" + strSoftwareVersion + "/" + strBoardVersion + "/" + strProd + "/WriteInstinct.ino.hex"
        fnOpenCat = self.stFileDir.get() + "/" + strSoftwareVersion + "/" + strBoardVersion + "/" + strProd + "/" + strFileName
        filename = [fnWriteI, fnOpenCat]
        print(filename)
        port = self.stPort.get()
        print(self.stPort.get())

        if self.stFileDir.get() == '' or self.stFileDir.get() == ' ':
            msgbox.showwarning(self.language.titleWarning, self.language.msgFileDir)
            self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus
            return False

        if port == ' ' or port == '':
            msgbox.showwarning(self.language.titleWarning, self.language.msgPort)
            self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus
            return False

        if (self.intVarWI.get() == 0) and (self.intVarOC.get() == 0):
            msgbox.showwarning(self.language.titleWarning, self.language.msgFirmware)
            self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus
            return False 

        ret = 0
        for file in filename:
            if (self.intVarWI.get() == 0) and (file == fnWriteI):
                continue
            if (self.intVarOC.get() == 0) and (file == fnOpenCat):
                continue

            if file == fnWriteI:
                self.stStatus.set(self.language.labStatus1 + self.language.cbnFileWI + '...' )
            elif file == fnOpenCat:
                self.stStatus.set(self.language.labStatus1 + self.language.cbnFileMF + '...')
            self.statusBar.update()

            if platform.system()=="Darwin" or platform.system()=="Linux":
                ret = call('./avrdude -C./avrdude.conf -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                           (port, file), shell=True)
            else:
                ret = call('./avrdude -C./avrdude.conf -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                            (port, file), shell=False)
            print("ret = " + str(ret))

            if ret == 0:
                if file == fnWriteI:
                    self.stStatus.set(self.language.cbnFileWI + ' ' + self.language.labStatus3)
                    self.statusBar.update()
                    time.sleep(5)
                    self.WriteInstinctProcess(port)
                    time.sleep(3)
                elif file == fnOpenCat:
                    self.stStatus.set(self.language.cbnFileMF + ' ' + self.language.labStatus3)
                    self.statusBar.update()
            else:
                if file == fnWriteI:
                    self.stStatus.set(self.language.cbnFileWI + ' ' + self.language.labStatus2)
                    self.statusBar.update()
                elif file == fnOpenCat:
                    self.stStatus.set(self.language.cbnFileMF + ' ' + self.language.labStatus2)
                    self.statusBar.update()
                return False

        print('Finish!')
        msgbox.showinfo(title=None, message=self.language.msgFinish)
        self.win.after(1, lambda: self.win.focus_force())  # 强制主界面获取focus
        return True


app = App()
app.win.mainloop()
