#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Language():
    '''Internationalization'''

    def __init__(self, language):
        if language == 'chi':
            self.resourceLagChi()
        elif language == 'eng':
            self.resourceLagEng()

    def resourceLagChi(self):
        self.title = '烧录工具'
        self.labTrans = '切换语言'
        self.labChi = '中文'
        self.labEng = '英文'
        self.labHelp = '帮助'
        self.labAbout = '关于'
        self.labExit = '退出'
        self.labFileDir = 'release文件夹位置:'
        self.btnFileDir = '选择文件夹...'
        self.titleFileDir = '请选择release文件夹'
        self.labPort = '选择串口:'
        self.labSoftwareVersion = '选择软件版本:'
        self.labBoardVersion = '选择主板型号:'
        self.labProduct = '选择产品:'
        self.labMode = '选择模式:'
        # self.rbnModes = ('标准', '随机动作', '语音控制', '超声波', '摄像头')
        self.rbnBittleModes = ('标准', '随机动作', '语音控制', '摄像头')
        self.rbnNybbleModes = ('标准', '随机动作', '语音控制', '超声波')
        # self.labFile = '请选择需要烧录的固件:'
        self.cbnFileWI = '写入常数固件'
        self.cbnFileMF = '主功能固件'
        # self.labNote = '''注意：写入常数固件烧录完成后，程序将自动校准IMU，
        #     因此在烧录写入常数固件前，请确保将 Bittle / Nybble 保持水平放置。'''
        self.btnUpload = '烧录'
        self.titleWarning = "警告"
        self.msgFileDir = '请选择release文件夹!'
        self.msgPort = '请选择正确的串口!'
        # self.msgFirmware = '请至少选择一个固件!'
        self.labStatus1 = '烧录 '
        self.labStatus2 = '烧录失败！'
        self.labStatus3 = '烧录成功！'
        self.titleVersion = '版本信息'
        self.msgVersion = '''版本：1.0.0 
        机器人固件烧录工具
        (C) 版权所有 2018-2022 派拓艺（深圳）科技有限责任公司
        https://www.petoi.com
        20/05/2022
        '''
        self.msgRstOffsets = '舵机校准参数清零? (Y/N)'
        self.msgCalibrateIMU = '''校准 IMU? (Y/N)
        注意: 请务必将 Bittle / Nybble 保持水平放置!'''
        self.instinctFinish = '参数初始化完成！'
        self.msgFinish = '固件烧录完成!'
        self.msgMode = '无效模式，请选择其他模式!'
        self.labStatusRest1 = '舵机校准参数清零......'
        self.labStatusRest12 = '舵机校准参数清零完成!'
        self.labStatusUploadInst1 = '上传配置参数......'
        self.labStatusUploadInst12 = '上传配置参数完成!'
        self.labStatusRest2 = '舵机校准参数清零并上传配置参数......'
        self.labStatusRest22 = '舵机校准参数清零并上传配置参数完成!'
        self.labStatusCalibrate = '校准 IMU......'
        self.labStatusCalibrate2 = 'IMU 校准完成!'

    def resourceLagEng(self):
        self.title = 'Flash uploader'
        self.labTrans = 'Change Language'
        self.labChi = 'Chinese'
        self.labEng = 'English'
        self.labHelp = 'Help'
        self.labAbout = 'About'
        self.labExit = 'Exit'
        self.labFileDir = 'The directory of release folder:'
        self.btnFileDir = 'Choose folder...'
        self.titleFileDir = 'Please choose the release folder'
        self.labPort = 'Select serial port:'
        self.labSoftwareVersion = 'Select software version:'
        self.labBoardVersion = 'Select board version:'
        self.labProduct = 'Select product:'
        self.labMode = 'Select mode:'
        # self.rbnModes = ('Standard', 'Random_Mind', 'Voice', 'Ultrasonic', 'Camera')
        self.rbnBittleModes = ('Standard', 'Random_Mind', 'Voice', 'Camera')
        self.rbnNybbleModes = ('Standard', 'Random_Mind', 'Voice', 'Ultrasonic')
        self.rbnWalk = 'Walk'
        self.rbnUltrasonic = 'Ultrasonic'
        self.rbnCamera = 'Camera'
        # self.labFile = 'Select firmware:'
        self.cbnFileWI = 'Parameters'
        self.cbnFileMF = 'Main function'
        # self.labNote = '''Note: The program will calibrate IMU automatically 
        #   after the Write constant firmware is uploaded.
        #   So please make sure to keep Bittle / Nybble horizontal, 
        #   before uploading the Writing constant firmware.'''
        self.btnUpload = 'Upload'
        self.titleWarning = 'Warning'
        self.labStatus1 = 'Uploading '
        self.labStatus2 = 'firmware uploaded failed.'
        self.labStatus3 = 'firmware uploaded successfully.'
        self.msgFileDir = 'Please choose the release folder!'
        self.msgPort = 'Please choose the correct serial port!'
        # self.msgFirmware = 'Please Select at least one firmware!'
        self.titleVersion = 'Version information'
        self.msgVersion = '''Version: 1.0.0 
        Flash upload tool for robot.
        (C) Copyright 2018-2022 Petoi LLC. All rights reserved.
        https://www.petoi.com
        20/05/2022
        '''
        self.msgRstOffsets = 'Reset joint offsets? (Y/N)'
        self.msgCalibrateIMU = '''Calibrate IMU? (Y/N)
        Note: Lay the robot FLAT on a table!'''
        self.instinctFinish = 'Parameters initialized!'
        self.msgFinish = 'Firmware upload complete!'
        self.msgMode = 'Invalide, please select another mode!'
        self.labStatusRest1 = 'Reset joint offsets...'
        self.labStatusRest12 = 'Reset joint offsets complete!'
        self.labStatusUploadInst1 = 'Uploading parameters...'
        self.labStatusUploadInst12 = 'Uploading parameters complete!'
        self.labStatusRest2 = 'Reset joint offsets and upload parameters...'
        self.labStatusRest22 = 'Reset joint offsets and upload parameters complete!'
        self.labStatusCalibrate = 'Calibrating IMU...'
        self.labStatusCalibrate2 = 'Calibrate IMU complete!'
