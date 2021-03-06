
import os
import PySide2
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication,  QMessageBox, QLineEdit, QFrame, QPlainTextEdit
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('列车故障救援-故障车救援车均处于区间-流程动态展示')
window.resize(1900,1000)
#--------------------评价变量设定（全局变量）---------------------------------
T_xs = 20;T_ddml = 8;T_sq = 20;T_dk = 2;T_gfx = 4;T_xxjh = 6;T_zylj = 8;T_ats = 1;T_fzpj = 1  # 应急场景下具体的操作类型数量
Y_01 = 0  # 0-1变量
S_xs = 2.4024;S_ddml = 1.8538;S_sq = 2.4024;S_dk = 2.4024;S_gfx = 2.4024;S_xxjh = 1.356;S_zylj = 2.4024;S_ats = 1.619;S_fzpj = 1.0888  # 各部分评价分数
# S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
S_xs_count = 0;S_ddml_count = 0;S_sq_count = 0;S_dk_count = 0;S_gfx_count = 0;S_xxjh_count = 0;S_zylj_count = 0;S_ats_count = 0;S_fzpj_count = 0;  # 普通操作正确情况计数
S_jlzb_count = 0;S_xcaqjl_count = 0;S_rcaq_count = 0;S_cdaq_count = 0  # 安全性评价操作错误情况计数0-1
#----------------------------竖线代码--------------------------
line_1 = QFrame(window)
line_1.resize(1,950)
line_1.move(1000,20)
line_1.setFrameShape(QFrame.VLine)
#-----------------故障车司机----------------------------------------
btu_1 = QPushButton(window)
btu_1.setText('故障车司机汇报')
btu_1.move(10,10)
btu_1.setStyleSheet('font-weight:bold;')
# print(btu_1.geometry().x())
# print(btu_1.geometry().y())
# global click_btu1
click_btu1 = 0 #操作逻辑关系的标记
click_btu2 = 0
click_btu3 = 0
click_btu4 = 0
click_btu5 = 0
click_btu6 = 0
#-----------------------------------------------------------
label_1 =QLabel(window)
label_1.setText('→')
label_1.move(133,20)
#-------------------1调度员---------------------------------------
btu_2 =QPushButton(window)
btu_2.setText('查看ATS面板，核对故障车车次车号及所处区间')
btu_2.move(150,10)

#-----------------2调度员--------------------------------------------
label_2 =QLabel(window)
label_2.setText('→')
label_2.move(475,20)

btu_3 = QPushButton(window)
btu_3.setText('要求故障车进入第一个三分钟排故')
btu_3.move(500,10)

##--------------3调度员---------------------------------------------
label_3 =QLabel(window)
label_3.setText('→')
label_3.move(750,20)

btu_4 = QPushButton(window)
btu_4.setText('对后续列车进行扣车')
btu_4.move(770,10)
##--------------4调度员---------------------------------------------
label_4 =QLabel(window)
label_4.setText('→')
label_4.move(10,70)

btu_5 = QPushButton(window)
btu_5.setText('通知车站、司机故障基本情况、预计晚点时间')
btu_5.move(30,60)
##--------------5调度员---------------------------------------------
label_5 =QLabel(window)
label_5.setText('→')
label_5.move(350,70)

btu_6 = QPushButton(window)
btu_6.setText('询问故障车司机能否动车')
btu_6.move(370,60)
##--------------6故障车司机回复---------------------------------------------
label_6 =QLabel(window)
label_6.setText('→')
label_6.move(550,70)

btu_7 = QPushButton(window)
btu_7.setText('故障车回复能否动车')
btu_7.move(570,60)
btu_7.setStyleSheet('font-weight:bold;')
##--------------7分支线条---------------------------------------------
label_xt_1=QLabel(window)
label_xt_1.setText('丨')
label_xt_1.move(630, 93)

label_xt_2 =QLabel(window)
label_xt_2.setText('————————————————————————————————————')
label_xt_2.move(90, 103)#左边

label_xt_3 =QLabel(window)
label_xt_3.setText('———————————————')
label_xt_3.move(642, 103)#右边

label_xt_4 =QLabel(window)
label_xt_4.setText('↓')
label_xt_4.move(80, 110)#左边

label_xt_5 =QLabel(window)
label_xt_5.setText('↓')
label_xt_5.move(861, 110)#右边
#--------------------------7右边分支：能够动车，调度员-----------------------------------------
btu_8_R = QPushButton(window)
btu_8_R.setText('安排故障车及后列车恢复正常运营')
btu_8_R.move(750,130)
#--------------------------7左边分支：不能够动车，调度员-----------------------------------------
btu_8 = QPushButton(window)
btu_8.setText('同意进行第二个三分钟排故')
btu_8.move(5,130)

##-------------------------8调度员---------------------------------------------
label_8 =QLabel(window)
label_8.setText('↓')
label_8.move(80, 163)

btu_9 = QPushButton(window)
btu_9.setText('询问故障车具体位置')
btu_9.move(15,180)
##-------------------------9故障车司机回复---------------------------------------------
label_9 =QLabel(window)
label_9.setText('↓')
label_9.move(80, 213)

btu_10 = QPushButton(window)
btu_10.setText('故障车司机回复百米标\n/参照物位置')
btu_10.move(5,230)
btu_10.setStyleSheet('font-weight:bold;')
##-------------------------10调度员---------------------------------------------
label_10 =QLabel(window)
label_10.setText('↓')
label_10.move(80, 275)

btu_11 = QPushButton(window)
btu_11.setText('向救援车司机发布运行命令')
btu_11.move(5,290)
##-------------------------11救援车司机---------------------------------------------
label_11 =QLabel(window)
label_11.setText('↓')
label_11.move(80, 323)

btu_12 = QPushButton(window)
btu_12.setText('救援车复诵调令')
btu_12.move(25,340)
btu_12.setStyleSheet('font-weight:bold;')
##-------------------------12调度员---------------------------------------------
label_12 =QLabel(window)
label_12.setText('↓')
label_12.move(80, 373)

btu_13 = QPushButton(window)
btu_13.setText('询问故障车能否动车\n并进行四确认')
btu_13.move(13,390)
##-------------------------13故障车司机---------------------------------------------
label_13 =QLabel(window)
label_13.setText('↓')
label_13.move(80, 438)

btu_14 = QPushButton(window)
btu_14.setText('故障车回复四确认完毕\n无法动车')
btu_14.move(2,455)
btu_14.setStyleSheet('font-weight:bold;')
##-------------------------14调度员---------------------------------------------
label_14 =QLabel(window)
label_14.setText('↓')
label_14.move(80, 500)

btu_15 = QPushButton(window)
btu_15.setText('要求将对讲机调至救援组')
btu_15.move(2,515)
##-------------------------15调度员---------------------------------------------
label_15 =QLabel(window)
label_15.setText('↓')
label_15.move(80, 550)

btu_16 = QPushButton(window)
btu_16.setText('向故障车发布等待救援命令')
btu_16.move(2,565)
##-------------------------16故障车司机复诵---------------------------------------------
label_16 =QLabel(window)
label_16.setText('↓')
label_16.move(80, 600)

btu_17 = QPushButton(window)
btu_17.setText('故障车司机复诵')
btu_17.move(25,615)
btu_17.setStyleSheet('font-weight:bold;')
##-------------------------17救援车司机---------------------------------------------
label_17 =QLabel(window)
label_17.setText('↓')
label_17.move(80, 650)

btu_18 = QPushButton(window)
btu_18.setText("救援车司机汇报\n已到达‘一车'位置")
btu_18.move(15,665)
btu_18.setStyleSheet('font-weight:bold;')
##-------------------------18调度员---------------------------------------------
label_18 =QLabel(window)
label_18.setText('↓')
label_18.move(80, 713)

btu_19 = QPushButton(window)
btu_19.setText("发布实施救援连挂命令")
btu_19.move(10,730)
##-------------------------19救援车司机---------------------------------------------
label_19 =QLabel(window)
label_19.setText('↓')
label_19.move(80, 765)

btu_20 = QPushButton(window)
btu_20.setText("救援车司机复诵")
btu_20.move(25,780)
btu_20.setStyleSheet('font-weight:bold;')
#------------------------线条---------------------------
label_xt_6 = QLabel(window)
label_xt_6.setText('丨\n丨\n丨')
label_xt_6.move(80,810)

label_xt_7 = QLabel(window)
label_xt_7.setText('——————————')
label_xt_7.move(85,857)

label_xt_8 = QLabel(window)
label_xt_8.setText('丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨')
label_xt_8.move(230,147)

label_xt_9 = QLabel(window)
label_xt_9.setText('——→')
label_xt_9.move(240,141)

label_xt_10 = QLabel(window)
label_xt_10.setText('丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨\n丨')
label_xt_10.move(860,162)

label_xt_11 = QLabel(window)
label_xt_11.setText('←—————————————')
label_xt_11.move(658,865)

#--------------------------20调度员-----------------------------------------
btu_21 = QPushButton(window)
btu_21.setText("传达COCC下达的黄牌信息")
btu_21.move(290,135)
##-------------------------21救援车司机---------------------------------------------
label_21 =QLabel(window)
label_21.setText('↓')
label_21.move(360, 170)

btu_22 = QPushButton(window)
btu_22.setText("救援车司机汇报救援连挂完毕")
btu_22.move(270,190)
btu_22.setStyleSheet('font-weight:bold;')
##-------------------------22调度员---------------------------------------------
label_22 =QLabel(window)
label_22.setText('↓')
label_22.move(360, 224)

btu_23 = QPushButton(window)
btu_23.setText("向前方车站发布\n故障车清客命令")
btu_23.move(310,240)
##-------------------------23调度员---------------------------------------------
label_23 =QLabel(window)
label_23.setText('↓')
label_23.move(360, 289)

btu_24 = QPushButton(window)
btu_24.setText("发布调令，令救援连挂车以切除ATP\n方式运行至前方站台清客")
btu_24.move(250,305)
##-------------------------24救援连挂列车---------------------------------------------
label_24 =QLabel(window)
label_24.setText('↓')
label_24.move(360, 354)

btu_25 = QPushButton(window)
btu_25.setText("车站、救援连挂车司机复诵")
btu_25.move(275,370)
btu_25.setStyleSheet('font-weight:bold;')
##-------------------------25故障车---------------------------------------------
label_25 =QLabel(window)
label_25.setText('↓')
label_25.move(360, 404)

btu_26 = QPushButton(window)
btu_26.setText("故障车报告清客完毕")
btu_26.move(290,420)
btu_26.setStyleSheet('font-weight:bold;')
##-------------------------26调度员---------------------------------------------
label_26 =QLabel(window)
label_26.setText('↓')
label_26.move(360, 453)

btu_27 = QPushButton(window)
btu_27.setText("发布调令，向前方车站\n发布救援车清客命令")
btu_27.move(290,470)
##-------------------------27调度员---------------------------------------------
label_27 =QLabel(window)
label_27.setText('↓')
label_27.move(360, 517)

btu_28 = QPushButton(window)
btu_28.setText("发布调令，向救援车发布清客命令")
btu_28.move(260,535)
#-----------------------------28救援车司机-------------------------------------------------
label_28 =QLabel(window)
label_28.setText('↓')
label_28.move(360, 567)

btu_29 = QPushButton(window)
btu_29.setText("车站、救援车司机复诵")
btu_29.move(285,585)
btu_29.setStyleSheet('font-weight:bold;')
#---------------------29调度员------------------------------
label_29 =QLabel(window)
label_29.setText('↓')
label_29.move(360, 617)

btu_30 = QPushButton(window)
btu_30.setText("令车站安排人员登乘救援车")
btu_30.move(280,635)
#---------------------30行车值班员------------------------------
label_30 =QLabel(window)
label_30.setText('↓')
label_30.move(360, 667)

btu_31 = QPushButton(window)
btu_31.setText("车站汇报登乘人员已到位")
btu_31.move(285,685)
btu_31.setStyleSheet('font-weight:bold;')
#---------------------31救援车司机------------------------------
label_31 =QLabel(window)
label_31.setText('↓')
label_31.move(360, 717)

btu_32 = QPushButton(window)
btu_32.setText("救援车汇报：清客完毕")
btu_32.move(285,735)
btu_32.setStyleSheet('font-weight:bold;')
#---------------------32调度员------------------------------
label_32 =QLabel(window)
label_32.setText('↓')
label_32.move(360, 765)

btu_33 = QPushButton(window)
btu_33.setText("发布调令，令救援连挂车以切除ATP\n方式运行至XX车场")
btu_33.move(255,785)
#---------------------33调度员------------------------------
label_33 =QLabel(window)
label_33.setText('↓')
label_33.move(360, 835)

btu_34 = QPushButton(window)
btu_34.setText("通知DCC运转，救援连挂车即将回库")
btu_34.move(260,855)
#---------------------34结束------------------------------
label_end =QLabel(window)
label_end.setText('——→')
label_end.move(510,865)

btu_End =QPushButton(window)
btu_End.setText('结束')
btu_End.move(560,855)
#------------以上为左半边流程逻辑的代码展示---------------------------------------------------------------------------------------
#-----------------以下为下拉框设计部分代码-------------------------------------------------------
scrollArea = QtWidgets.QScrollArea(window)#区域的设置，父类是Form
scrollArea.setGeometry(QtCore.QRect(1000,15, 900, 970))#前两个参数为区域起点的位置，后两个参数为设置区域在Form上显示的大小
scrollArea.setWidgetResizable(True)
scrollArea.setObjectName("scrollArea")
scrollAreaWidgetContents = QtWidgets.QWidget(scrollArea)
scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 2900))#设置一共有多长，原则上并不设上限
scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(100, 2900))
scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
scrollArea.setWidget(scrollAreaWidgetContents)


#------------以下为右半边评价部分代码展示-------------------------------------------------------------------
def cao_1():
    btu_1.setStyleSheet('background-color: yellow;')
    mb_1.setText('xx号车报告调度，列车故障并迫停于XX区间/XX车站')
    mb_1.open()
mb_1 = QMessageBox(window)
mb_1.setWindowTitle('消息提示')

label_input = QLabel(scrollAreaWidgetContents)
label_input.setText('调度操作内容记录')
label_input.setStyleSheet('font-weight:bold;')
label_input.move(500,65)

label_czpj = QLabel(scrollAreaWidgetContents)
label_czpj.setText('调度操作评价')
label_czpj.setStyleSheet('font-weight:bold;')
label_czpj.move(220,65)

label_dxdfqk = QLabel(scrollAreaWidgetContents)
label_dxdfqk.setText('单项得分情况')
label_dxdfqk.setStyleSheet('font-weight:bold;')
label_dxdfqk.move(730,65)

btu_R_1 = QPushButton(scrollAreaWidgetContents)
btu_R_1.setText('开始模拟')
btu_R_1.move(450,10)
btu_R_1.pressed.connect(cao_1)
##----------------------------操作1------------------------------------------------------------------------
#------------------1调度员弹窗输入-----------------------------------------
#弹窗设计，标签，QlineEdit
Newwindow_1 =QWidget()
Newwindow_1.setWindowTitle('消息提示')
Newwindow_1.resize(400, 200)
label_tc1 = QLabel(Newwindow_1)
label_tc1.setText('请输入操作内容')
label_tc1.move(10,10)
LineEdit_1 =QLineEdit(Newwindow_1)
LineEdit_1.resize(380,30)
LineEdit_1.move(10, 50)
btu_tc1 =QPushButton(Newwindow_1)
btu_tc1.setText('确定')
btu_tc1.move(150,100)

def Get_Input_1():
    global dict_Input_1, T_xs , T_ddml, T_sq , T_dk , T_gfx , T_xxjh , T_zylj , T_ats , T_fzpj #应急场景下具体的操作类型数量
    global Y_01 #0-1变量
    global S_xs , S_ddml , S_sq , S_dk ,S_gfx , S_xxjh, S_zylj , S_ats , S_fzpj #各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count , S_ddml_count , S_sq_count,S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count ,S_ats_count , S_fzpj_count #普通操作正确情况计数
    global S_jlzb_count , S_xcaqjl_count, S_rcaq_count, S_cdaq_count #安全性评价操作错误情况计数0-1
    dxzf_1 = S_xs + S_sq + S_gfx
    dxdf_1 = 0
    Input_1 = LineEdit_1.text()
    Result_1 = []
    plainTextEdit_czjl_1.setPlainText(Input_1)
    Input_1_list = Input_1.split('，')#先转成列表
    #限速=无，授权=无，作业环节规范性=鼠标移至故障车所在位置 --固定格式
    dict_Input_1 = {}
    for i in range(len(Input_1_list)):
        dict_Input_1[Input_1_list[i].split('=')[0]] = Input_1_list[i].split('=')[1]
    print(dict_Input_1)
    #-----------将input转换成字典类型
    if dict_Input_1['限速']=='无':
        S_xs_count += 1
        dxdf_1 += S_xs
    else:
        Result_1.append('限速错误，错误限速为：'+ dict_Input_1['限速'])
        plainTextEdit_czpj_1.setStyleSheet('color:red;')
        btu_2.setStyleSheet('background-color: red;')
    if dict_Input_1['授权']=='无':
        S_sq_count += 1
        dxdf_1 += S_sq
    else:
        Result_1.append('授权错误，错误授权为：'+ dict_Input_1['授权'])
        plainTextEdit_czpj_1.setStyleSheet('color:red;')
        btu_2.setStyleSheet('background-color: red;')
    if dict_Input_1['作业环节规范性']=='鼠标移至故障车所在位置':
        S_gfx_count += 1
        dxdf_1 += S_gfx
    else:
        Result_1.append('作业规范性错误，错误作业规范性为：'+ dict_Input_1['作业规范性'])
        plainTextEdit_czpj_1.setStyleSheet('color:red;')
        btu_2.setStyleSheet('background-color: red;')
    if dict_Input_1['限速']=='无' and dict_Input_1['授权']=='无' and dict_Input_1['作业环节规范性']=='鼠标移至故障车所在位置':
        Result_1.append('处置正确√')
        plainTextEdit_czpj_1.setStyleSheet('background-color: lime;')
    plainTextEdit_czpj_1.setPlainText(str(Result_1))
    plainTextEdit_dxdfqk_1.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_1,dxdf_1, str(dxzf_1 - dxdf_1)))
    #plainTextEdit_czjl_1.setEnabled(False)
    Newwindow_1.close()
btu_tc1.pressed.connect(Get_Input_1)

def cao_2():
    global click_btu2
    click_btu2 = 1  # 点击后标记变成1，在下一个btu中做判断
    btu_2.setStyleSheet('background-color: yellow;')
    label_1.setStyleSheet('background-color: yellow;')
    Newwindow_1.show()
    btu_R_2.setEnabled(False)

plainTextEdit_czpj_1 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_1.resize(250, 70)
plainTextEdit_czpj_1.move(150, 95)

plainTextEdit_czjl_1 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_1.resize(250, 70)
plainTextEdit_czjl_1.move(430, 95)

plainTextEdit_dxdfqk_1 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_1.resize(160, 70)
plainTextEdit_dxdfqk_1.move(700, 95)


btu_R_2 = QPushButton(scrollAreaWidgetContents)
btu_R_2.setText('   操作1   ')
btu_R_2.move(15,100)
btu_R_2.pressed.connect(cao_2)
##----------------------------操作2------------------------------------------------------------------------
#---------------------2调度员弹窗----------------------------------------
##按钮三的弹窗设置
Newwindow_2 =QWidget()
Newwindow_2.setWindowTitle('消息提示')
Newwindow_2.resize(400, 200)
label_tc2 = QLabel(Newwindow_2)
label_tc2.setText('请输入操作内容')
label_tc2.move(10,10)
LineEdit_2 =QLineEdit(Newwindow_2)
LineEdit_2.resize(380,30)
LineEdit_2.move(10, 50)
btu_tc2 =QPushButton(Newwindow_2)
btu_tc2.setText('确定')
btu_tc2.move(150,100)

def Get_Input_2():
    global dict_Input_2, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_2 = S_xxjh + S_sq + S_xs
    dxdf_2 = 0
    Input_2 = LineEdit_2.text()
    Result_2 = []
    plainTextEdit_czjl_2.setPlainText(Input_2)
    plainTextEdit_czjl_2.setPlainText(Input_2)
    Input_2_list = Input_2.split('，')#先转成列表
    #信息交互=进入第一个三分钟排故，限速=无，授权=无
    dict_Input_2 = {}
    for i in range(len(Input_2_list)):
        dict_Input_2[Input_2_list[i].split('=')[0]] = Input_2_list[i].split('=')[1]
    print(dict_Input_2)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_2['信息交互']=='进入第一个三分钟排故':
        S_xxjh_count += 1
        dxdf_2 += S_xxjh
    else:
        Result_2.append('信息交互错误，错误信息交互为：' + dict_Input_2['信息交互'])
        plainTextEdit_czpj_2.setStyleSheet('color:red;')
        btu_3.setStyleSheet('background-color: red;')
    if dict_Input_2['限速']=='无':
        S_xs_count += 1
        dxdf_2 += S_xs
    else:
        Result_2.append('限速错误，错误限速为：' + dict_Input_2['限速'])
        plainTextEdit_czpj_2.setStyleSheet('color:red;')
        btu_3.setStyleSheet('background-color: red;')
    if dict_Input_2['授权']=='无':
        S_sq_count += 1
        dxdf_2 += S_sq
    else:
        Result_2.append('授权错误，错误授权为：'+ dict_Input_2['授权'])
        btu_3.setStyleSheet('background-color: red;')
    if dict_Input_2['限速'] == '无' and dict_Input_2['授权'] == '无' and dict_Input_2['信息交互'] == '进入第一个三分钟排故':
        Result_2.append('处置正确√')
        plainTextEdit_czpj_2.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_2.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_2,dxdf_2, str(dxzf_2 - dxdf_2)))
    plainTextEdit_czpj_2.setPlainText(str(Result_2))
    Newwindow_2.close()
btu_tc2.pressed.connect(Get_Input_2)
##错误流程变红，且终端显示具体的错误
#----------------------------判断过程-------------------------------------------------------
def cao_3():
    btu_3.setStyleSheet('background-color: yellow;')
    label_2.setStyleSheet('background-color: yellow;')
    Newwindow_2.show()
    btu_R_3.setEnabled(False)

plainTextEdit_czpj_2 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_2.resize(250, 70)
plainTextEdit_czpj_2.move(150, 180)

plainTextEdit_czjl_2 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_2.resize(250, 70)
plainTextEdit_czjl_2.move(430, 180)

plainTextEdit_dxdfqk_2 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_2.resize(160, 70)
plainTextEdit_dxdfqk_2.move(700, 180)

btu_R_3 = QPushButton(scrollAreaWidgetContents)
btu_R_3.setText('   操作2   ')
btu_R_3.move(15,185)
btu_R_3.pressed.connect(cao_3)
##----------------------------操作3（存在作业间逻辑关系）------------------------------------------------------------------------
##按钮三的弹窗设置---------------------------------------------------------------
Newwindow_3 =QWidget()
Newwindow_3.setWindowTitle('消息提示')
Newwindow_3.resize(400, 200)
label_tc3 = QLabel(Newwindow_3)
label_tc3.setText('请输入操作内容')
label_tc3.move(10,10)
LineEdit_3 =QLineEdit(Newwindow_3)
LineEdit_3.resize(380,30)
LineEdit_3.move(10, 50)
btu_tc3 =QPushButton(Newwindow_3)
btu_tc3.setText('确定')
btu_tc3.move(150,100)

def Get_Input_3():
    global dict_Input_3, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_3 = S_xs + S_sq + S_ats + S_zylj
    dxdf_3 = 0
    Input_3 = LineEdit_3.text()
    Result_3 = []
    plainTextEdit_czjl_3.setPlainText(Input_3)
    Input_3_list = Input_3.split('，')#先转成列表
    #授权=无，限速=无，ATS基本操作=选中相邻列车前方站台右击扣车按钮，各作业间逻辑=查看故障车位置之后
    dict_Input_3 = {}
    for i in range(len(Input_3_list)):
        dict_Input_3[Input_3_list[i].split('=')[0]] = Input_3_list[i].split('=')[1]
    print(dict_Input_3)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_3['ATS基本操作']=='选中相邻列车前方站台右击扣车按钮':
        S_ats_count += 1
        dxdf_3 += S_ats
    else:
        Result_3.append('ATS基本操作错误，错误ATS基本操作为：'+ dict_Input_3['ATS基本操作'])
        plainTextEdit_czpj_3.setStyleSheet('color:red;')
        btu_4.setStyleSheet('background-color: red;')
    if dict_Input_3['限速']=='无':
        S_xs_count += 1
        dxdf_3 += S_xs
    else:
        Result_3.append('限速错误，错误限速为：'+ dict_Input_3['限速'])
        plainTextEdit_czpj_3.setStyleSheet('color:red;')
        btu_4.setStyleSheet('background-color: red;')
    if dict_Input_3['授权']=='无':
        S_sq_count += 1
        dxdf_3 += S_sq
    else:
        Result_3.append('授权错误，错误授权为：'+ dict_Input_3['授权'])
        plainTextEdit_czpj_3.setStyleSheet('color:red;')
        btu_4.setStyleSheet('background-color: red;')
    if click_btu2 == 1:
        S_zylj_count += 1
        dxdf_3 += S_zylj
    else:
        Result_3.append('操作顺序错误:未执行查看ATS面板操作')
        plainTextEdit_czpj_3.setStyleSheet('color:red;')
        btu_4.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_3['限速'] == '无' and dict_Input_3['授权'] == '无' and dict_Input_3['ATS基本操作'] == '选中相邻列车前方站台右击扣车按钮'and click_btu2==1:
        Result_3.append('处置正确√')
        plainTextEdit_czpj_3.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_3.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_3,dxdf_3, str(dxzf_3 - dxdf_3)))
    plainTextEdit_czpj_3.setPlainText(str(Result_3))
    Newwindow_3.close()
btu_tc3.pressed.connect(Get_Input_3)

def cao_4():
    btu_4.setStyleSheet('background-color: yellow;')
    label_3.setStyleSheet('background-color: yellow;')
    Newwindow_3.show()
    btu_R_4.setEnabled(False)

mb_2 = QMessageBox(window)
mb_2.setWindowTitle('消息提示')

plainTextEdit_czpj_3 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_3.resize(250, 70)
plainTextEdit_czpj_3.move(150, 265)

plainTextEdit_czjl_3 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_3.resize(250, 70)
plainTextEdit_czjl_3.move(430, 265)

plainTextEdit_dxdfqk_3 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_3.resize(160, 70)
plainTextEdit_dxdfqk_3.move(700, 265)

btu_R_4 = QPushButton(scrollAreaWidgetContents)
btu_R_4.setText('   操作3   ')
btu_R_4.move(15,270)
btu_R_4.pressed.connect(cao_4)
##----------------------------操作4------------------------------------------------------------------------
Newwindow_4 =QWidget()
Newwindow_4.setWindowTitle('消息提示')
Newwindow_4.resize(400, 200)
label_tc4 = QLabel(Newwindow_4)
label_tc4.setText('请输入操作内容')
label_tc4.move(10,10)
LineEdit_4 =QLineEdit(Newwindow_4)
LineEdit_4.resize(380,30)
LineEdit_4.move(10, 50)
btu_tc4 =QPushButton(Newwindow_4)
btu_tc4.setText('确定')
btu_tc4.move(150,100)

def Get_Input_4():
    global dict_Input_4, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_4 = S_xs + S_sq + S_xxjh
    dxdf_4 = 0
    Input_4 = LineEdit_4.text()
    Result_4 = []
    plainTextEdit_czjl_4.setPlainText(Input_4)
    Input_4_list = Input_4.split('，')#先转成列表
    #授权=无，限速=无，信息交互=xx号车在xx站上/下行发生列车故障预计晚点时间xxmin
    dict_Input_4 = {}
    for i in range(len(Input_4_list)):
        dict_Input_4[Input_4_list[i].split('=')[0]] = Input_4_list[i].split('=')[1]
    print(dict_Input_4)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_4['信息交互']=='xx号车在xx站上/下行发生列车故障预计晚点时间xxmin':
        S_xxjh_count += 1
        dxdf_4 += S_xxjh
    else:
        Result_4.append('信息交互错误，错误信息交互为：'+ dict_Input_4['信息交互'])
        plainTextEdit_czpj_4.setStyleSheet('color:red;')
        btu_5.setStyleSheet('background-color: red;')
    if dict_Input_4['限速']=='无':
        S_xs_count += 1
        dxdf_4 += S_xs
    else:
        Result_4.append('限速错误，错误限速为：'+ dict_Input_4['限速'])
        plainTextEdit_czpj_4.setStyleSheet('color:red;')
        btu_5.setStyleSheet('background-color: red;')
    if dict_Input_4['授权']=='无':
        S_sq_count += 1
        dxdf_4 += S_sq
    else:
        Result_4.append('授权错误，错误授权为：'+ dict_Input_4['授权'])
        plainTextEdit_czpj_4.setStyleSheet('color:red;')
        btu_5.setStyleSheet('background-color: red;')
    if dict_Input_4['限速'] == '无' and dict_Input_4['授权'] == '无' and dict_Input_4['信息交互'] == 'xx号车在xx站上/下行发生列车故障预计晚点时间xxmin':
        Result_4.append('处置正确√')
        plainTextEdit_czpj_4.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_4.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_4,dxdf_4, str(dxzf_4 - dxdf_4)))
    plainTextEdit_czpj_4.setPlainText(str(Result_4))
    Newwindow_4.close()
btu_tc4.pressed.connect(Get_Input_4)

def cao_5():
    btu_5.setStyleSheet('background-color: yellow;')
    label_4.setStyleSheet('background-color: yellow;')
    Newwindow_4.show()
    btu_R_5.setEnabled(False)

plainTextEdit_czpj_4 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_4.resize(250, 70)
plainTextEdit_czpj_4.move(150, 350)

plainTextEdit_czjl_4 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_4.resize(250, 70)
plainTextEdit_czjl_4.move(430, 350)

plainTextEdit_dxdfqk_4 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_4.resize(160, 70)
plainTextEdit_dxdfqk_4.move(700, 350)

btu_R_5 = QPushButton(scrollAreaWidgetContents)
btu_R_5.setText('   操作4   ')
btu_R_5.move(15,355)
btu_R_5.pressed.connect(cao_5)
##------------------------------操作5------------------------------------------------
Newwindow_5 =QWidget()
Newwindow_5.setWindowTitle('消息提示')
Newwindow_5.resize(400, 200)
label_tc5 = QLabel(Newwindow_5)
label_tc5.setText('请输入操作内容')
label_tc5.move(10,10)
LineEdit_5 =QLineEdit(Newwindow_5)
LineEdit_5.resize(380,30)
LineEdit_5.move(10, 50)
btu_tc5 =QPushButton(Newwindow_5)
btu_tc5.setText('确定')
btu_tc5.move(150,100)

def Get_Input_5():
    global dict_Input_5, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_5 = S_xs + S_sq + S_xxjh
    dxdf_5 = 0
    Input_5 = LineEdit_5.text()
    Result_5 = []
    plainTextEdit_czjl_5.setPlainText(Input_5)
    Input_5_list = Input_5.split('，')#先转成列表
    #授权=无，限速=无，信息交互=xx号车能否动车？
    dict_Input_5 = {}
    for i in range(len(Input_5_list)):
        dict_Input_5[Input_5_list[i].split('=')[0]] = Input_5_list[i].split('=')[1]
    print(dict_Input_5)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_5['信息交互']=='xx号车能否动车？':
        S_xxjh_count += 1
        dxdf_5 += S_xxjh
    else:
        Result_5.append('信息交互错误，错误信息交互为：'+ dict_Input_5['信息交互'])
        plainTextEdit_czpj_5.setStyleSheet('color:red;')
        btu_6.setStyleSheet('background-color: red;')
    if dict_Input_5['限速']=='无':
        S_xs_count += 1
        dxdf_5 += S_xs
    else:
        Result_5.append('限速错误，错误限速为：'+ dict_Input_5['限速'])
        plainTextEdit_czpj_5.setStyleSheet('color:red;')
        btu_6.setStyleSheet('background-color: red;')
    if dict_Input_5['授权']=='无':
        S_sq_count += 1
        dxdf_5 += S_sq
    else:
        Result_5.append('授权错误，错误授权为：'+ dict_Input_5['授权'])
        plainTextEdit_czpj_5.setStyleSheet('color:red;')
        btu_6.setStyleSheet('background-color: red;')
    if dict_Input_5['限速'] == '无' and dict_Input_5['授权'] == '无' and dict_Input_5['信息交互'] == 'xx号车能否动车？':
        Result_5.append('处置正确√')
        plainTextEdit_czpj_5.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_5.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_5,dxdf_5, str(dxzf_5 - dxdf_5)))
    plainTextEdit_czpj_5.setPlainText(str(Result_5))
    Newwindow_5.close()
btu_tc5.pressed.connect(Get_Input_5)

def cao_6():
    btu_6.setStyleSheet('background-color: yellow;')
    label_5.setStyleSheet('background-color: yellow;')
    Newwindow_5.show()
    btu_R_6.setEnabled(False)

plainTextEdit_czpj_5 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_5.resize(250, 70)
plainTextEdit_czpj_5.move(150, 435)

plainTextEdit_czjl_5 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_5.resize(250, 70)
plainTextEdit_czjl_5.move(430, 435)

plainTextEdit_dxdfqk_5 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_5.resize(160, 70)
plainTextEdit_dxdfqk_5.move(700, 435)

btu_R_6 = QPushButton(scrollAreaWidgetContents)
btu_R_6.setText('   操作5   ')
btu_R_6.move(15,450)
btu_R_6.pressed.connect(cao_6)
##------------------------------操作6 故障车司机回复（决策点按钮）------------------------------------------------
def cao_7():
    answer_1 = np.random.randint(0, 2, 1)  # 随机生成0,1
    global Answer_1
    Answer_1 = str(answer_1)
    if '1' in Answer_1:
        btu_7.setStyleSheet('background-color: yellow;')
        label_6.setStyleSheet('background-color: yellow;')
        label_xt_1.setStyleSheet('background-color: yellow;')
        label_xt_2.setStyleSheet('background-color: yellow;')
        label_xt_4.setStyleSheet('background-color: yellow;')
        mb_3.setText('无法动车，申请进入第二个三分钟排故')
        mb_3.open()
        plainTextEdit_sjhf_1.setPlainText("司机回复：'无法动车，申请进入第二个三分钟排故'")
    if '0' in Answer_1:
        btu_7.setStyleSheet('background-color: yellow;')
        label_6.setStyleSheet('background-color: yellow;')
        label_xt_1.setStyleSheet('background-color: yellow;')
        label_xt_3.setStyleSheet('background-color: yellow;')
        label_xt_5.setStyleSheet('background-color: yellow;')
        mb_3.setText('排故完成，列车恢复正常，可以动车')
        mb_3.open()
        plainTextEdit_sjhf_1.setPlainText("司机回复：'排故完成，列车恢复正常，可以动车'")

mb_3 = QMessageBox(window)
mb_3.setWindowTitle('消息提示')

plainTextEdit_sjhf_1 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_1.resize(715, 30)
plainTextEdit_sjhf_1.move(150, 530)

btu_R_7 = QPushButton(scrollAreaWidgetContents)
btu_R_7.setText('故障车司机\n自动回复')
btu_R_7.move(15,525)
btu_R_7.setStyleSheet("color:blue")
btu_R_7.pressed.connect(cao_7)
##------------------------------操作6无法动车后------------------------------------------------
Newwindow_6 =QWidget()
Newwindow_6.setWindowTitle('消息提示')
Newwindow_6.resize(400, 200)
label_tc6 = QLabel(Newwindow_6)
label_tc6.setText('请输入操作内容')
label_tc6.move(10,10)
LineEdit_6=QLineEdit(Newwindow_6)
LineEdit_6.resize(380,30)
LineEdit_6.move(10, 50)
btu_tc6 =QPushButton(Newwindow_6)
btu_tc6.setText('确定')
btu_tc6.move(150,100)

def Get_Input_6():
    global dict_Input_6, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_6 = S_xs + S_sq + S_xxjh
    dxdf_6 = 0
    Input_6 = LineEdit_6.text()
    Result_6 = []
    plainTextEdit_czjl_6.setPlainText(Input_6)
    Input_6_list = Input_6.split('，')#先转成列表
    #授权=无，限速=无，信息交互=同意进入第二个三分钟排故
    dict_Input_6 = {}
    for i in range(len(Input_6_list)):
        dict_Input_6[Input_6_list[i].split('=')[0]] = Input_6_list[i].split('=')[1]
    print(dict_Input_6)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_6['信息交互']=='同意进入第二个三分钟排故':
        S_xxjh_count += 1
        dxdf_6 += S_xxjh
    else:
        Result_6.append('信息交互错误，错误信息交互为：'+ dict_Input_6['信息交互'])
        plainTextEdit_czpj_6.setStyleSheet('color:red;')
        btu_8.setStyleSheet('background-color: red;')
    if dict_Input_6['限速']=='无':
        S_xs_count += 1
        dxdf_6 += S_xs
    else:
        Result_6.append('限速错误，错误限速为：'+ dict_Input_6['限速'])
        plainTextEdit_czpj_6.setStyleSheet('color:red;')
        btu_8.setStyleSheet('background-color: red;')
    if dict_Input_6['授权']=='无':
        S_sq_count += 1
        dxdf_6 += S_sq
    else:
        Result_6.append('授权错误，错误授权为：'+ dict_Input_6['授权'])
        plainTextEdit_czpj_6.setStyleSheet('color:red;')
        btu_8.setStyleSheet('background-color: red;')
    if dict_Input_6['限速'] == '无' and dict_Input_6['授权'] == '无' and dict_Input_6['信息交互'] == '同意进入第二个三分钟排故':
        Result_6.append('处置正确√')
        plainTextEdit_czpj_6.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_6.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_6,dxdf_6, str(dxzf_6 - dxdf_6)))
    plainTextEdit_czpj_6.setPlainText(str(Result_6))
    Newwindow_6.close()
btu_tc6.pressed.connect(Get_Input_6)

def cao_7():
    global Answer_1
    if '1' in Answer_1:
        btu_8.setStyleSheet('background-color: yellow;')
        Newwindow_6.show()
        btu_R_8.setEnabled(False)
    else:
        mb_4.open()

plainTextEdit_czpj_6 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_6.resize(250, 70)
plainTextEdit_czpj_6.move(150, 590)

plainTextEdit_czjl_6 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_6.resize(250, 70)
plainTextEdit_czjl_6.move(430, 590)

plainTextEdit_dxdfqk_6 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_6.resize(160, 70)
plainTextEdit_dxdfqk_6.move(700, 590)

btu_R_8 = QPushButton(scrollAreaWidgetContents)
btu_R_8.setText('   操作6   ')
btu_R_8.move(15,605)
btu_R_8.pressed.connect(cao_7)
mb_4 = QMessageBox(window)
mb_4.setWindowTitle('消息提示')
mb_4.setText('     判断错误     ')


##------------------------------操作7排故成功，可以动车------------------------------------------------
Newwindow_7 =QWidget()
Newwindow_7.setWindowTitle('消息提示')
Newwindow_7.resize(400, 200)
label_tc7 = QLabel(Newwindow_7)
label_tc7.setText('请输入操作内容')
label_tc7.move(10,10)
LineEdit_7=QLineEdit(Newwindow_7)
LineEdit_7.resize(380,30)
LineEdit_7.move(10, 50)
btu_tc7 =QPushButton(Newwindow_7)
btu_tc7.setText('确定')
btu_tc7.move(150,100)

def Get_Input_7():
    global dict_Input_7, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_7 = S_xs + S_sq + S_xxjh
    dxdf_7 = 0
    Input_7 = LineEdit_7.text()
    Result_7 = []
    plainTextEdit_czjl_7.setPlainText(Input_7)
    Input_7_list = Input_7.split('，')#先转成列表
    #授权=无，限速=无，信息交互=列车运行至前方站台正常载客运营
    dict_Input_7 = {}
    for i in range(len(Input_7_list)):
        dict_Input_7[Input_7_list[i].split('=')[0]] = Input_7_list[i].split('=')[1]
    print(dict_Input_7)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_7['信息交互']=='列车运行至前方站台正常载客运营':
        S_xxjh_count += 1
        dxdf_7 += S_xxjh
    else:
        Result_7.append('信息交互错误，错误信息交互为：'+ dict_Input_7['信息交互'])
        plainTextEdit_czpj_7.setStyleSheet('color:red;')
        btu_8_R.setStyleSheet('background-color: red;')
    if dict_Input_7['限速']=='无':
        S_xs_count += 1
        dxdf_7 += S_xs
    else:
        Result_7.append('限速错误，错误限速为：'+ dict_Input_7['限速'])
        plainTextEdit_czpj_7.setStyleSheet('color:red;')
        btu_8_R.setStyleSheet('background-color: red;')
    if dict_Input_7['授权']=='无':
        S_sq_count += 1
        dxdf_7 += S_sq
    else:
        Result_7.append('中授权错误，错误授权为：'+ dict_Input_7['授权'])
        plainTextEdit_czpj_7.setStyleSheet('color:red;')
        btu_8_R.setStyleSheet('background-color: red;')
    if dict_Input_7['限速'] == '无' and dict_Input_7['授权'] == '无' and dict_Input_7['信息交互'] == '同意进入第二个三分钟排故':
        Result_7.append('处置正确√')
        plainTextEdit_czpj_7.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_7.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_7,dxdf_7, str(dxzf_7 - dxdf_7)))
    plainTextEdit_czpj_7.setPlainText(str(Result_7))
    Newwindow_7.close()
    btu_End.setStyleSheet('background-color: yellow;')
btu_tc7.pressed.connect(Get_Input_7)

def cao_8():
    global Answer_1
    if '0' in Answer_1:
        label_xt_10.setStyleSheet('background-color: yellow;')
        label_xt_11.setStyleSheet('background-color: yellow;')
        btu_8_R.setStyleSheet('background-color: yellow;')
        Newwindow_7.show()
        btu_R_9.setEnabled(False)
    else:
        mb_4.open()

plainTextEdit_czpj_7 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_7.resize(250, 70)
plainTextEdit_czpj_7.move(150, 680)

plainTextEdit_czjl_7 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_7.resize(250, 70)
plainTextEdit_czjl_7.move(430, 680)

plainTextEdit_dxdfqk_7 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_7.resize(160, 70)
plainTextEdit_dxdfqk_7.move(700, 680)

btu_R_9 = QPushButton(scrollAreaWidgetContents)
btu_R_9.setText('   ※操作7   ')
btu_R_9.move(15,700)
btu_R_9.pressed.connect(cao_8)
##----------------------操作8-----------------------------------------------------------------------
Newwindow_8 =QWidget()
Newwindow_8.setWindowTitle('消息提示')
Newwindow_8.resize(400, 200)
label_tc8 = QLabel(Newwindow_8)
label_tc8.setText('请输入操作内容')
label_tc8.move(10,10)
LineEdit_8 =QLineEdit(Newwindow_8)
LineEdit_8.resize(380,30)
LineEdit_8.move(10, 50)
btu_tc8 =QPushButton(Newwindow_8)
btu_tc8.setText('确定')
btu_tc8.move(150,100)

def Get_Input_8():
    global dict_Input_8, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_8 = S_xs + S_sq + S_xxjh
    dxdf_8 = 0
    Input_8 = LineEdit_8.text()
    Result_8 = []
    plainTextEdit_czjl_8.setPlainText(Input_8)
    Input_8_list = Input_8.split('，')#先转成列表
    #授权=无，限速=无，信息交互=xx号故障车汇报百米标具体位置
    dict_Input_8 = {}
    for i in range(len(Input_8_list)):
        dict_Input_8[Input_8_list[i].split('=')[0]] = Input_8_list[i].split('=')[1]
    print(dict_Input_8)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_8['信息交互']=='xx号故障车汇报百米标具体位置':
        S_xxjh_count += 1
        dxdf_8 += S_xxjh
    else:
        Result_8.append('信息交互错误，错误信息交互为：'+ dict_Input_8['信息交互'])
        plainTextEdit_czpj_8.setStyleSheet('color:red;')
        btu_9.setStyleSheet('background-color: red;')
    if dict_Input_8['限速']=='无':
        S_xs_count += 1
        dxdf_8 += S_xs
    else:
        Result_8.append('限速错误，错误限速为：'+ dict_Input_8['限速'])
        plainTextEdit_czpj_8.setStyleSheet('color:red;')
        btu_9.setStyleSheet('background-color: red;')
    if dict_Input_8['授权']=='无':
        S_sq_count += 1
        dxdf_8 += S_sq
    else:
        Result_8.append('授权错误，错误授权为：'+ dict_Input_8['授权'])
        plainTextEdit_czpj_8.setStyleSheet('color:red;')
        btu_9.setStyleSheet('background-color: red;')
    if dict_Input_8['限速'] == '无' and dict_Input_8['授权'] == '无' and dict_Input_8['信息交互'] == 'xx号故障车汇报百米标具体位置':
        Result_8.append('处置正确√')
        plainTextEdit_czpj_8.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_8.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_8,dxdf_8, str(dxzf_8 - dxdf_8)))
    plainTextEdit_czpj_8.setPlainText(str(Result_8))
    Newwindow_8.close()
btu_tc8.pressed.connect(Get_Input_8)

def cao_9():
    btu_9.setStyleSheet('background-color: yellow;')
    label_8.setStyleSheet('background-color: yellow;')
    Newwindow_8.show()
    btu_R_9.setEnabled(False)

plainTextEdit_czpj_8 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_8.resize(250, 70)
plainTextEdit_czpj_8.move(150, 770)

plainTextEdit_czjl_8 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_8.resize(250, 70)
plainTextEdit_czjl_8.move(430, 770)

plainTextEdit_dxdfqk_8 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_8.resize(160, 70)
plainTextEdit_dxdfqk_8.move(700, 770)

btu_R_9 = QPushButton(scrollAreaWidgetContents)
btu_R_9.setText('   操作8   ')
btu_R_9.move(15,785)
btu_R_9.pressed.connect(cao_9)
##------------------------操作9-故障车司机回复百米标位置-----------------------------------------------------
def cao_10():
    btu_10.setStyleSheet('background-color: yellow;')
    label_9.setStyleSheet('background-color: yellow;')
    mb_5.setText('xx号故障车于百米标260m处')
    mb_5.open()
    plainTextEdit_sjhf_2.setPlainText("司机回复：'xx号故障车于百米标260m处'")

mb_5 = QMessageBox(window)
mb_5.setWindowTitle('消息提示')

plainTextEdit_sjhf_2 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_2.resize(715, 30)
plainTextEdit_sjhf_2.move(150, 866)

btu_R_10 = QPushButton(scrollAreaWidgetContents)
btu_R_10.setText('故障车司机\n自动回复')
btu_R_10.move(15,860)
btu_R_10.setEnabled(False)
btu_tc8.pressed.connect(cao_10)
btu_R_10.setStyleSheet('font-weight:bold;')
##---------------操作10向救援车发布运行命令-------------------------------------------------------------
Newwindow_9 =QWidget()
Newwindow_9.setWindowTitle('消息提示')
Newwindow_9.resize(400, 200)
label_tc9 = QLabel(Newwindow_9)
label_tc9.setText('请输入操作内容')
label_tc9.move(10,10)
LineEdit_9 =QLineEdit(Newwindow_9)
LineEdit_9.resize(380,30)
LineEdit_9.move(10, 50)
btu_tc9 =QPushButton(Newwindow_9)
btu_tc9.setText('确定')
btu_tc9.move(150,100)

def Get_Input_9():
    global dict_Input_9, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_9 = S_xs + S_sq + S_ddml
    dxdf_9 = 0
    Input_9 = LineEdit_9.text()
    Result_9 = []
    plainTextEdit_czjl_9.setPlainText(Input_9)
    Input_9_list = Input_9.split('，')#先转成列表
    #授权=值班调度长，限速=20km/h，调度命令=命令号xxx令xxx号车以/close-in/授权/RMO/RMF模式运行至距故障车“一车位置”停车故障车xxx号在xxx站至xxx站上/下行xxx处，进路准备=进路开通正确
    dict_Input_9 = {}
    for i in range(len(Input_9_list)):
        dict_Input_9[Input_9_list[i].split('=')[0]] = Input_9_list[i].split('=')[1]
    print(dict_Input_9)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_9['调度命令']=='命令号xxx令xxx号车以/close-in/授权/RMO/RMF模式运行至距故障车“一车位置”停车故障车xxx号在xxx站至xxx站上/下行xxx处':
        S_ddml_count += 1
        dxdf_9 += S_ddml
    else:
        Result_9.append('调度命令错误，错误调度命令为：'+ dict_Input_9['调度命令'])
        plainTextEdit_czpj_9.setStyleSheet('color:red;')
        btu_11.setStyleSheet('background-color: red;')
    if dict_Input_9['限速']=='20km/h':
        S_xs_count += 1
        dxdf_9 += S_xs
    else:
        Result_9.append('限速错误，错误限速为：'+ dict_Input_9['限速'])
        plainTextEdit_czpj_9.setStyleSheet('color:red;')
        btu_11.setStyleSheet('background-color: red;')
    if dict_Input_9['授权']=='值班调度长':
        S_sq_count += 1
        dxdf_9 += S_sq
    else:
        Result_9.append('授权错误，错误授权为：'+ dict_Input_9['授权'])
        plainTextEdit_czpj_9.setStyleSheet('color:red;')
        btu_11.setStyleSheet('background-color: red;')
    if dict_Input_9['进路准备']=='进路开通正确':
        pass
    else:
        S_jlzb_count += 1
        Result_9.append('进路准备错误，错误进路准备为：'+ dict_Input_9['进路准备'])
        plainTextEdit_czpj_9.setStyleSheet('color:red;')
        btu_11.setStyleSheet('background-color: red;')
    if dict_Input_9['限速'] == '20km/h' and dict_Input_9['授权'] == '值班调度长' and dict_Input_9['进路准备'] == '进路开通正确' and dict_Input_9['调度命令'] == '命令号xxx令xxx号车以/close-in/授权/RMO/RMF模式运行至距故障车“一车位置”停车故障车xxx号在xxx站至xxx站上/下行xxx处':
        Result_9.append('处置正确√')
        plainTextEdit_czpj_9.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_9.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_9,dxdf_9, str(dxzf_9 - dxdf_9)))
    plainTextEdit_czpj_9.setPlainText(str(Result_9))
    Newwindow_9.close()
btu_tc9.pressed.connect(Get_Input_9)

def cao_11():
    btu_11.setStyleSheet('background-color: yellow;')
    label_10.setStyleSheet('background-color: yellow;')
    Newwindow_9.show()
    btu_R_10.setEnabled(False)

plainTextEdit_czpj_9 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_9.resize(250, 70)
plainTextEdit_czpj_9.move(150, 915)

plainTextEdit_czjl_9 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_9.resize(250, 70)
plainTextEdit_czjl_9.move(430, 915)

plainTextEdit_dxdfqk_9 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_9.resize(160, 70)
plainTextEdit_dxdfqk_9.move(700, 915)

btu_R_10 = QPushButton(scrollAreaWidgetContents)
btu_R_10.setText('   操作10   ')
btu_R_10.move(15,940)
btu_R_10.pressed.connect(cao_11)
##---------------------------------操作11救援车复诵调令---------------------------------------------------
def cao_11():
    btu_12.setStyleSheet('background-color: yellow;')
    label_10.setStyleSheet('background-color: yellow;')
    mb_5.setText("救援车司机回复：" + dict_Input_9['调度命令'])
    mb_5.open()
    plainTextEdit_sjhf_3.setPlainText("救援车司机回复：" + dict_Input_9['调度命令'] )

mb_5 = QMessageBox(window)
mb_5.setWindowTitle('消息提示')

plainTextEdit_sjhf_3 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_3.resize(715, 50)
plainTextEdit_sjhf_3.move(150, 1010)

btu_R_11 = QPushButton(scrollAreaWidgetContents)
btu_R_11.setText('救援车司机\n自动回复')
btu_R_11.move(15,1020)
btu_R_11.setEnabled(False)
btu_R_11.setStyleSheet('font-weight:bold;')
btu_tc9.pressed.connect(cao_11)

##---------------------------------操作12 确认是否能动车及四确认情况-------------------------------------------
Newwindow_11 =QWidget()
Newwindow_11.setWindowTitle('消息提示')
Newwindow_11.resize(400, 200)
label_tc11 = QLabel(Newwindow_11)
label_tc11.setText('请输入操作内容')
label_tc11.move(10,10)
LineEdit_11 =QLineEdit(Newwindow_11)
LineEdit_11.resize(380,30)
LineEdit_11.move(10, 50)
btu_tc11 =QPushButton(Newwindow_11)
btu_tc11.setText('确定')
btu_tc11.move(150,100)

def Get_Input_11():
    global dict_Input_11, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_11 = S_xs + S_sq + S_gfx
    dxdf_11 = 0
    Input_11 = LineEdit_11.text()
    Result_11 = []
    plainTextEdit_czjl_11.setPlainText(Input_11)
    Input_11_list = Input_11.split('，')#先转成列表
    #授权=无，限速=无，作业环节规范性=四确认是否完毕？能否动车？
    dict_Input_11 = {}
    for i in range(len(Input_11_list)):
        dict_Input_11[Input_11_list[i].split('=')[0]] = Input_11_list[i].split('=')[1]
    print(dict_Input_11)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_11['作业环节规范性']=='四确认是否完毕？能否动车？':
        S_gfx_count += 1
        dxdf_11 += S_gfx
    else:
        Result_11.append('作业环节规范性错误，错误作业环节规范性为：'+ dict_Input_11['作业环节规范性'])
        plainTextEdit_czpj_11.setStyleSheet('color:red;')
        btu_13.setStyleSheet('background-color: red;')
    if dict_Input_11['限速']=='无':
        S_xs_count += 1
        dxdf_11 += S_xs
    else:
        Result_11.append('限速错误，错误限速为：'+ dict_Input_11['限速'])
        plainTextEdit_czpj_11.setStyleSheet('color:red;')
        btu_13.setStyleSheet('background-color: red;')
    if dict_Input_11['授权']=='无':
        S_sq_count += 1
        dxdf_11 += S_sq
    else:
        Result_11.append('授权错误，错误授权为：'+ dict_Input_11['授权'])
        plainTextEdit_czpj_11.setStyleSheet('color:red;')
        btu_13.setStyleSheet('background-color: red;')
    if dict_Input_11['限速'] == '无' and dict_Input_11['授权'] == '无' and dict_Input_11['作业环节规范性'] == '四确认是否完毕？能否动车？':
        Result_11.append('处置正确√')
        plainTextEdit_czpj_11.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_11.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_11,dxdf_11, str(dxzf_11 - dxdf_11)))
    plainTextEdit_czpj_11.setPlainText(str(Result_11))
    Newwindow_11.close()
btu_tc11.pressed.connect(Get_Input_11)

def cao_12():
    global click_btu3
    click_btu3 = 1
    btu_13.setStyleSheet('background-color: yellow;')
    label_12.setStyleSheet('background-color: yellow;')
    Newwindow_11.show()
    btu_R_12.setEnabled(False)

plainTextEdit_czpj_11 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_11.resize(250, 70)
plainTextEdit_czpj_11.move(150, 1090)

plainTextEdit_czjl_11 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_11.resize(250, 70)
plainTextEdit_czjl_11.move(430, 1090)

plainTextEdit_dxdfqk_11 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_11.resize(160, 70)
plainTextEdit_dxdfqk_11.move(700, 1090)

btu_R_12 = QPushButton(scrollAreaWidgetContents)
btu_R_12.setText('   操作12   ')
btu_R_12.move(15,1100)
btu_R_12.pressed.connect(cao_12)
##---------------操作13 故障车回复四确认情况---------------------------------------
def cao_13():
    btu_14.setStyleSheet('background-color: yellow;')
    label_13.setStyleSheet('background-color: yellow;')
    mb_6.setText('四确认完毕，仍无法动车')
    mb_6.open()
    plainTextEdit_sjhf_12.setPlainText('四确认完毕，仍无法动车')

mb_6 = QMessageBox(window)
mb_6.setWindowTitle('消息提示')

plainTextEdit_sjhf_12 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_12.resize(715, 40)
plainTextEdit_sjhf_12.move(150, 1180)

btu_R_13 = QPushButton(scrollAreaWidgetContents)
btu_R_13.setText('故障车司机\n回复四确认')
btu_R_13.move(15,1180)
btu_R_13.setEnabled(False)
btu_R_13.setStyleSheet('font-weight:bold;')
btu_tc11.pressed.connect(cao_13)
##-------------------------------操作14将对讲机调至救援组----------------------------------
Newwindow_13 =QWidget()
Newwindow_13.setWindowTitle('消息提示')
Newwindow_13.resize(400, 200)
label_tc13 = QLabel(Newwindow_13)
label_tc13.setText('请输入操作内容')
label_tc13.move(10,10)
LineEdit_13 =QLineEdit(Newwindow_13)
LineEdit_13.resize(380,30)
LineEdit_13.move(10, 50)
btu_tc13 =QPushButton(Newwindow_13)
btu_tc13.setText('确定')
btu_tc13.move(150,100)

def Get_Input_13():
    global dict_Input_11, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_13 = S_xs + S_sq + S_gfx + S_zylj
    dxdf_13 = 0
    Input_13 = LineEdit_13.text()
    Result_13 = []
    plainTextEdit_czjl_13.setPlainText(Input_13)
    Input_13_list = Input_13.split('，')#先转成列表
    #授权=无，限速=无，作业环节规范性=要求故障车、救援车将对讲机调至救援组;作业逻辑-四确认
    dict_Input_13 = {}
    for i in range(len(Input_13_list)):
        dict_Input_13[Input_13_list[i].split('=')[0]] = Input_13_list[i].split('=')[1]
    print(dict_Input_13)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_13['作业环节规范性']=='要求故障车、救援车将对讲机调至救援组':
        S_gfx_count += 1
        dxdf_13 += S_gfx
    else:
        Result_13.append('作业环节规范性错误，错误作业环节规范性为：'+ dict_Input_13['作业环节规范性'])
        plainTextEdit_czpj_13.setStyleSheet('color:red;')
        btu_15.setStyleSheet('background-color: red;')
    if dict_Input_13['限速']=='无':
        S_xs_count += 1
        dxdf_13 += S_xs
    else:
        Result_13.append('限速错误，错误限速为：'+ dict_Input_13['限速'])
        plainTextEdit_czpj_13.setStyleSheet('color:red;')
        btu_15.setStyleSheet('background-color: red;')
    if dict_Input_13['授权']=='无':
        S_sq_count += 1
        dxdf_13 += S_sq
    else:
        Result_13.append('授权错误，错误授权为：'+ dict_Input_13['授权'])
        plainTextEdit_czpj_13.setStyleSheet('color:red;')
        btu_15.setStyleSheet('background-color: red;')
    if click_btu3 == 1:
        S_zylj_count += 1
        dxdf_13 += S_zylj
    else:
        Result_13.append('操作顺序错误:未与司机确认四确认情况')
        plainTextEdit_czpj_13.setStyleSheet('color:red;')
        btu_15.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_13['限速'] == '无' and dict_Input_13['授权'] == '无' and dict_Input_13['作业环节规范性'] == '要求故障车、救援车将对讲机调至救援组' and click_btu3==1:
        Result_13.append('处置正确√')
        plainTextEdit_czpj_13.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_13.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_13,dxdf_13, str(dxzf_13 - dxdf_13)))
    plainTextEdit_czpj_13.setPlainText(str(Result_13))
    Newwindow_13.close()
btu_tc13.pressed.connect(Get_Input_13)

def cao_14():
    btu_15.setStyleSheet('background-color: yellow;')
    label_14.setStyleSheet('background-color: yellow;')
    Newwindow_13.show()
    btu_R_14.setEnabled(False)

plainTextEdit_czpj_13 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_13.resize(250, 70)
plainTextEdit_czpj_13.move(150, 1250)

plainTextEdit_czjl_13 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_13.resize(250, 70)
plainTextEdit_czjl_13.move(430, 1250)

plainTextEdit_dxdfqk_13 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_13.resize(160, 70)
plainTextEdit_dxdfqk_13.move(700, 1250)

btu_R_14 = QPushButton(scrollAreaWidgetContents)
btu_R_14.setText('   操作14   ')
btu_R_14.move(15,1260)
btu_R_14.pressed.connect(cao_14)

##------------------------------操作15-发布等待救援命令--------------------------------------------
Newwindow_14 =QWidget()
Newwindow_14.setWindowTitle('消息提示')
Newwindow_14.resize(400, 200)
label_tc14 = QLabel(Newwindow_14)
label_tc14.setText('请输入操作内容')
label_tc14.move(10,10)
LineEdit_14 =QLineEdit(Newwindow_14)
LineEdit_14.resize(380,30)
LineEdit_14.move(10, 50)
btu_tc14 =QPushButton(Newwindow_14)
btu_tc14.setText('确定')
btu_tc14.move(150,100)

def Get_Input_14():
    global dict_Input_14, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_14 = S_xs + S_sq + S_ddml +S_zylj
    dxdf_14 = 0
    Input_14 = LineEdit_14.text()
    Result_14 = []
    plainTextEdit_czjl_14.setPlainText(Input_14)
    Input_14_list = Input_14.split('，')#先转成列表
    #授权=无，限速=无，调度命令=命令号xxx令xxx号车等待救援救援车为xxx站开来的xxx号车
    dict_Input_14 = {}
    for i in range(len(Input_14_list)):
        dict_Input_14[Input_14_list[i].split('=')[0]] = Input_14_list[i].split('=')[1]
    print(dict_Input_14)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_14['调度命令']=='命令号xxx令xxx号车等待救援救援车为xxx站开来的xxx号车':
        S_ddml_count += 1
        dxdf_14 += S_ddml
    else:
        Result_14.append('调度命令错误，错误调度命令为：'+ dict_Input_14['调度命令'])
        plainTextEdit_czpj_14.setStyleSheet('color:red;')
        btu_16.setStyleSheet('background-color: red;')
    if dict_Input_14['限速']=='无':
        S_xs_count += 1
        dxdf_14 += S_xs
    else:
        Result_14.append('限速错误，错误限速为：'+ dict_Input_14['限速'])
        plainTextEdit_czpj_14.setStyleSheet('color:red;')
        btu_16.setStyleSheet('background-color: red;')
    if dict_Input_14['授权']=='无':
        S_sq_count += 1
        dxdf_14 += S_sq
    else:
        Result_14.append('授权错误，错误授权为：'+ dict_Input_14['授权'])
        plainTextEdit_czpj_14.setStyleSheet('color:red;')
        btu_16.setStyleSheet('background-color: red;')
    if click_btu3 == 1:
        S_zylj_count += 1
        dxdf_14 += S_zylj
    else:
        Result_14.append('操作顺序错误:未与司机确认四确认情况')
        plainTextEdit_czpj_13.setStyleSheet('color:red;')
        btu_16.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_14['限速'] == '无' and dict_Input_14['授权'] == '无' and dict_Input_14['调度命令'] == '命令号xxx令xxx号车等待救援救援车为xxx站开来的xxx号车' and click_btu3 == 1:
        Result_14.append('处置正确√')
        plainTextEdit_czpj_14.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_14.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_14,dxdf_14, str(dxzf_14 - dxdf_14)))
    plainTextEdit_czpj_14.setPlainText(str(Result_14))
    Newwindow_14.close()
btu_tc14.pressed.connect(Get_Input_14)

def cao_15():
    btu_16.setStyleSheet('background-color: yellow;')
    label_15.setStyleSheet('background-color: yellow;')
    Newwindow_14.show()
    btu_R_15.setEnabled(False)

plainTextEdit_czpj_14 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_14.resize(250, 70)
plainTextEdit_czpj_14.move(150, 1330)

plainTextEdit_czjl_14 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_14.resize(250, 70)
plainTextEdit_czjl_14.move(430, 1330)

plainTextEdit_dxdfqk_14 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_14.resize(160, 70)
plainTextEdit_dxdfqk_14.move(700, 1330)

btu_R_15 = QPushButton(scrollAreaWidgetContents)
btu_R_15.setText('   操作15   ')
btu_R_15.move(15,1340)
btu_R_15.pressed.connect(cao_15)
##---------------------------------操作16故障车复诵调令---------------------------------------------------
def cao_16():
    btu_17.setStyleSheet('background-color: yellow;')
    label_16.setStyleSheet('background-color: yellow;')
    mb_7.setText("故障车司机回复：" + dict_Input_14['调度命令'])
    mb_7.open()
    plainTextEdit_sjhf_15.setPlainText("故障车司机回复：" + dict_Input_14['调度命令'] )

mb_7 = QMessageBox(window)
mb_7.setWindowTitle('消息提示')

plainTextEdit_sjhf_15 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_15.resize(715, 50)
plainTextEdit_sjhf_15.move(150, 1410)

btu_R_16 = QPushButton(scrollAreaWidgetContents)
btu_R_16.setText('故障车司机\n自动回复')
btu_R_16.move(15,1410)
btu_R_16.setEnabled(False)
btu_R_16.setStyleSheet('font-weight:bold;')
btu_tc14.pressed.connect(cao_16)

##--------------------------------操作17到达'一车'位置----------------------------------
def cao_17():
    btu_18.setStyleSheet('background-color: yellow;')
    label_17.setStyleSheet('background-color: yellow;')
    mb_8.setText("救援车司机报告：XX号车已到达'一车'位置")
    mb_8.open()
    plainTextEdit_sjhf_16.setPlainText("救援车司机报告：XX号车已到达'一车'位置")

mb_8 = QMessageBox(window)
mb_8.setWindowTitle('消息提示')

plainTextEdit_sjhf_16 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_16.resize(715, 50)
plainTextEdit_sjhf_16.move(150, 1480)

btu_R_17 = QPushButton(scrollAreaWidgetContents)
btu_R_17.setText('救援车司机报告')
btu_R_17.move(15,1490)
btu_R_17.setStyleSheet('font-weight:bold;')
btu_R_17.pressed.connect(cao_17)
##---------------------------------------操作18发布救援连挂命令-------------------------------------------
Newwindow_17 =QWidget()
Newwindow_17.setWindowTitle('消息提示')
Newwindow_17.resize(400, 200)
label_tc17 = QLabel(Newwindow_17)
label_tc17.setText('请输入操作内容')
label_tc17.move(10,10)
LineEdit_17 =QLineEdit(Newwindow_17)
LineEdit_17.resize(380,30)
LineEdit_17.move(10, 50)
btu_tc17 =QPushButton(Newwindow_17)
btu_tc17.setText('确定')
btu_tc17.move(150,100)

def Get_Input_17():
    global dict_Input_17, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_17 = S_xs + S_sq + S_ddml +S_zylj
    dxdf_17 = 0
    Input_17 = LineEdit_17.text()
    Result_17 = []
    plainTextEdit_czjl_17.setPlainText(Input_17)
    Input_17_list = Input_17.split('，')#先转成列表
    #授权=无，限速=5km/h，调度命令=命令号***令***号车与故障车实施救援作业;作业逻辑
    dict_Input_17 = {}
    for i in range(len(Input_17_list)):
        dict_Input_17[Input_17_list[i].split('=')[0]] = Input_17_list[i].split('=')[1]
    print(dict_Input_17)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_17['调度命令']=='命令号***令***号车与故障车实施救援作业':
        S_ddml_count += 1
        dxdf_17 += S_ddml
    else:
        Result_17.append('调度命令错误，错误调度命令为：'+ dict_Input_17['调度命令'])
        plainTextEdit_czpj_17.setStyleSheet('color:red;')
        btu_19.setStyleSheet('background-color: red;')
    if dict_Input_17['限速']=='5km/h':
        S_xs_count += 1
        dxdf_17 += S_xs
    else:
        Result_17.append('限速错误，错误限速为：'+ dict_Input_17['限速'])
        plainTextEdit_czpj_17.setStyleSheet('color:red;')
        btu_19.setStyleSheet('background-color: red;')
    if dict_Input_17['授权']=='无':
        S_sq_count += 1
        dxdf_17 += S_sq
    else:
        Result_17.append('授权错误，错误授权为：'+ dict_Input_17['授权'])
        plainTextEdit_czpj_17.setStyleSheet('color:red;')
        btu_19.setStyleSheet('background-color: red;')
    if click_btu3 == 1:
        S_zylj_count += 1
        dxdf_17 += S_zylj
    else:
        Result_17.append('操作顺序错误:未与司机确认四确认情况')
        plainTextEdit_czpj_17.setStyleSheet('color:red;')
        btu_19.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_17['限速'] == '5km/h' and dict_Input_17['授权'] == '无' and dict_Input_17['调度命令'] == '命令号***令***号车与故障车实施救援作业' and click_btu3 == 1:
        Result_17.append('处置正确√')
        plainTextEdit_czpj_17.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_17.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_17,dxdf_17, str(dxzf_17 - dxdf_17)))
    plainTextEdit_czpj_17.setPlainText(str(Result_17))
    Newwindow_17.close()
btu_tc17.pressed.connect(Get_Input_17)

def cao_18():
    btu_19.setStyleSheet('background-color: yellow;')
    label_18.setStyleSheet('background-color: yellow;')
    Newwindow_17.show()
    btu_R_18.setEnabled(False)

plainTextEdit_czpj_17 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_17.resize(250, 70)
plainTextEdit_czpj_17.move(150, 1550)

plainTextEdit_czjl_17 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_17.resize(250, 70)
plainTextEdit_czjl_17.move(430, 1550)

plainTextEdit_dxdfqk_17 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_17.resize(160, 70)
plainTextEdit_dxdfqk_17.move(700, 1550)

btu_R_18 = QPushButton(scrollAreaWidgetContents)
btu_R_18.setText('   操作18   ')
btu_R_18.move(15,1560)
btu_R_18.pressed.connect(cao_18)
##---------------------------------操作19救援车复诵调令---------------------------------------------------
def cao_19():
    btu_20.setStyleSheet('background-color: yellow;')
    label_19.setStyleSheet('background-color: yellow;')
    mb_8.setText("救援车司机回复：" + dict_Input_17['调度命令'])
    mb_8.open()
    plainTextEdit_sjhf_18.setPlainText("救援车司机回复：" + dict_Input_17['调度命令'] )

mb_8 = QMessageBox(window)
mb_8.setWindowTitle('消息提示')

plainTextEdit_sjhf_18 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_18.resize(715, 50)
plainTextEdit_sjhf_18.move(150, 1630)

btu_R_19 = QPushButton(scrollAreaWidgetContents)
btu_R_19.setText('救援车司机\n自动回复')
btu_R_19.move(15,1630)
btu_R_19.setEnabled(False)
btu_R_19.setStyleSheet('font-weight:bold;')
btu_tc17.pressed.connect(cao_19)

##---------------------------------------操作20 传达COCC黄牌信息-----------------------------------------------
Newwindow_19 =QWidget()
Newwindow_19.setWindowTitle('消息提示')
Newwindow_19.resize(400, 200)
label_tc19 = QLabel(Newwindow_19)
label_tc19.setText('请输入操作内容')
label_tc19.move(10,10)
LineEdit_19 =QLineEdit(Newwindow_19)
LineEdit_19.resize(380,30)
LineEdit_19.move(10, 50)
btu_tc19 =QPushButton(Newwindow_19)
btu_tc19.setText('确定')
btu_tc19.move(150,100)

def Get_Input_19():
    global dict_Input_19, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_19 = S_xs + S_sq + S_fzpj + S_zylj
    dxdf_19 = 0
    Input_19 = LineEdit_19.text()
    Result_19 = []
    plainTextEdit_czjl_19.setPlainText(Input_19)
    Input_19_list = Input_19.split('，')#先转成列表
    #授权=无，限速=无，其他辅助评价=传达COCC下发的黄牌信息
    dict_Input_19 = {}
    for i in range(len(Input_19_list)):
        dict_Input_19[Input_19_list[i].split('=')[0]] = Input_19_list[i].split('=')[1]
    print(dict_Input_19)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_19['其他辅助评价']=='传达COCC下发的黄牌信息':
        S_fzpj_count += 1
        dxdf_19 += S_fzpj
    else:
        Result_19.append('作业环节规范性错误，错误作业环节规范性为：'+ dict_Input_19['作业环节规范性'])
        plainTextEdit_czpj_19.setStyleSheet('color:red;')
        btu_21.setStyleSheet('background-color: red;')
    if dict_Input_19['限速']=='无':
        S_xs_count += 1
        dxdf_19 += S_xs
    else:
        Result_19.append('限速错误，错误限速为：'+ dict_Input_19['限速'])
        plainTextEdit_czpj_19.setStyleSheet('color:red;')
        btu_21.setStyleSheet('background-color: red;')
    if dict_Input_19['授权']=='无':
        S_sq_count += 1
        dxdf_19 += S_sq
    else:
        Result_19.append('授权错误，错误授权为：'+ dict_Input_19['授权'])
        plainTextEdit_czpj_19.setStyleSheet('color:red;')
        btu_21.setStyleSheet('background-color: red;')
    if click_btu3 == 1:
        S_zylj_count += 1
        dxdf_19 += S_zylj
    else:
        Result_19.append('操作顺序错误:未与司机确认四确认情况')
        plainTextEdit_czpj_19.setStyleSheet('color:red;')
        btu_21.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_19['限速'] == '无' and dict_Input_19['授权'] == '无' and dict_Input_19['其他辅助评价'] == '传达COCC下发的黄牌信息' and click_btu3==1:
        Result_19.append('处置正确√')
        plainTextEdit_czpj_19.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_19.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_19,dxdf_19, str(dxzf_19 - dxdf_19)))
    plainTextEdit_czpj_19.setPlainText(str(Result_19))
    Newwindow_19.close()
btu_tc19.pressed.connect(Get_Input_19)

def cao_20():
    btu_21.setStyleSheet('background-color: yellow;')
    label_xt_6.setStyleSheet('background-color: yellow;')
    label_xt_7.setStyleSheet('background-color: yellow;')
    label_xt_8.setStyleSheet('background-color: yellow;')
    label_xt_9.setStyleSheet('background-color: yellow;')
    Newwindow_19.show()
    btu_R_19.setEnabled(False)

plainTextEdit_czpj_19 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_19.resize(250, 70)
plainTextEdit_czpj_19.move(150, 1700)

plainTextEdit_czjl_19 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_19.resize(250, 70)
plainTextEdit_czjl_19.move(430, 1700)

plainTextEdit_dxdfqk_19 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_19.resize(160, 70)
plainTextEdit_dxdfqk_19.move(700, 1700)

btu_R_20 = QPushButton(scrollAreaWidgetContents)
btu_R_20.setText('   操作20   ')
btu_R_20.move(15,1710)
btu_R_20.pressed.connect(cao_20)
##---------------------------------------------操作21 救援车回复连挂完毕----------------------------------------
def cao_21():
    global click_btu4
    click_btu4 = 1
    btu_22.setStyleSheet('background-color: yellow;')
    label_21.setStyleSheet('background-color: yellow;')
    mb_9.setText("救援车司机报告：救援连挂完毕，可以动车")
    mb_9.open()
    plainTextEdit_sjhf_20.setPlainText("救援车司机报告：救援连挂完毕，可以动车")

mb_9 = QMessageBox(window)
mb_9.setWindowTitle('消息提示')

plainTextEdit_sjhf_20 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_20.resize(715, 50)
plainTextEdit_sjhf_20.move(150, 1780)

btu_R_21 = QPushButton(scrollAreaWidgetContents)
btu_R_21.setText('救援车司机报告')
btu_R_21.move(15,1780)
btu_R_21.setStyleSheet('font-weight:bold;')
btu_R_21.pressed.connect(cao_21)
##-----------------------------操作22 发布调令 车站 切ATP运行--------------------------------------------------
Newwindow_21 =QWidget()
Newwindow_21.setWindowTitle('消息提示')
Newwindow_21.resize(400, 200)
label_tc21 = QLabel(Newwindow_21)
label_tc21.setText('请输入操作内容')
label_tc21.move(10,10)
LineEdit_21 =QLineEdit(Newwindow_21)
LineEdit_21.resize(380,30)
LineEdit_21.move(10, 50)
btu_tc21 =QPushButton(Newwindow_21)
btu_tc21.setText('确定')
btu_tc21.move(150,100)

def Get_Input_21():
    global dict_Input_21, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_21 = S_xs + S_sq + S_ddml +S_zylj
    dxdf_21 = 0
    Input_21 = LineEdit_21.text()
    Result_21 = []
    plainTextEdit_czjl_21.setPlainText(Input_21)
    Input_21_list = Input_21.split('，')#先转成列表
    #授权=无，限速=无，调度命令=发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客;作业逻辑
    dict_Input_21 = {}
    for i in range(len(Input_21_list)):
        dict_Input_21[Input_21_list[i].split('=')[0]] = Input_21_list[i].split('=')[1]
    print(dict_Input_21)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_21['调度命令']=='发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客':
        S_ddml_count += 1
        dxdf_21 += S_ddml
    else:
        Result_21.append('调度命令错误，错误调度命令为：'+ dict_Input_21['调度命令'])
        plainTextEdit_czpj_21.setStyleSheet('color:red;')
        btu_23.setStyleSheet('background-color: red;')
    if dict_Input_21['限速']=='无':
        S_xs_count += 1
        dxdf_21 += S_xs
    else:
        Result_21.append('限速错误，错误限速为：'+ dict_Input_21['限速'])
        plainTextEdit_czpj_21.setStyleSheet('color:red;')
        btu_23.setStyleSheet('background-color: red;')
    if dict_Input_21['授权']=='无':
        S_sq_count += 1
        dxdf_21 += S_sq
    else:
        Result_21.append('授权错误，错误授权为：'+ dict_Input_21['授权'])
        plainTextEdit_czpj_21.setStyleSheet('color:red;')
        btu_23.setStyleSheet('background-color: red;')
    if click_btu4 == 1:
        S_zylj_count += 1
        dxdf_21 += S_zylj
    else:
        Result_21.append('操作顺序错误:未确认救援连挂车动车条件')
        plainTextEdit_czpj_21.setStyleSheet('color:red;')
        btu_23.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_21['限速'] == '无' and dict_Input_21['授权'] == '无' and dict_Input_21['调度命令'] == '发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客' and click_btu4 == 1:
        Result_21.append('处置正确√')
        plainTextEdit_czpj_21.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_21.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_21,dxdf_21, str(dxzf_21 - dxdf_21)))
    plainTextEdit_czpj_21.setPlainText(str(Result_21))
    Newwindow_21.close()
btu_tc21.pressed.connect(Get_Input_21)

def cao_22():
    btu_23.setStyleSheet('background-color: yellow;')
    label_22.setStyleSheet('background-color: yellow;')
    Newwindow_21.show()
    btu_R_22.setEnabled(False)

plainTextEdit_czpj_21 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_21.resize(250, 70)
plainTextEdit_czpj_21.move(150, 1854)

plainTextEdit_czjl_21 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_21.resize(250, 70)
plainTextEdit_czjl_21.move(430, 1854)

plainTextEdit_dxdfqk_21 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_21.resize(160, 70)
plainTextEdit_dxdfqk_21.move(700, 1854)

btu_R_22 = QPushButton(scrollAreaWidgetContents)
btu_R_22.setText('   操作22   ')
btu_R_22.move(15,1864)
btu_R_22.pressed.connect(cao_22)
##-----------------------------------操作23 发布调令 救援连挂车  切ATP运行---------------------------------------
Newwindow_22 =QWidget()
Newwindow_22.setWindowTitle('消息提示')
Newwindow_22.resize(400, 200)
label_tc22 = QLabel(Newwindow_22)
label_tc22.setText('请输入操作内容')
label_tc22.move(10,10)
LineEdit_22 =QLineEdit(Newwindow_22)
LineEdit_22.resize(380,30)
LineEdit_22.move(10, 50)
btu_tc22 =QPushButton(Newwindow_22)
btu_tc22.setText('确定')
btu_tc22.move(150,100)

def Get_Input_22():
    global dict_Input_22, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_22 = S_xs + S_sq + S_ddml +S_dk
    dxdf_22 = 0
    Input_22 = LineEdit_22.text()
    Result_22 = []
    plainTextEdit_czjl_22.setPlainText(Input_22)
    Input_22_list = Input_22.split('，')#先转成列表
    #授权=值班调度长，限速=25km/h，调度命令=发布对象救援连挂车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客，进路准备=进路准备正确，行车安全距离=一站一区间，盯控=是
    dict_Input_22 = {}
    for i in range(len(Input_22_list)):
        dict_Input_22[Input_22_list[i].split('=')[0]] = Input_22_list[i].split('=')[1]
    print(dict_Input_22)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_22['调度命令']=='发布对象救援连挂车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客':
        S_ddml_count += 1
        dxdf_22 += S_ddml
    else:
        Result_22.append('调度命令错误，错误调度命令为：'+ dict_Input_22['调度命令'])
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['限速']=='25km/h':
        S_xs_count += 1
        dxdf_22 += S_xs
    else:
        Result_22.append('限速错误，错误限速为：'+ dict_Input_22['限速'])
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['授权']=='值班调度长':
        S_sq_count += 1
        dxdf_22 += S_sq
    else:
        Result_22.append('授权错误，错误授权为：'+ dict_Input_22['授权'])
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['进路准备'] == '进路准备正确':
        pass
    else:
        S_jlzb_count += 1
        Result_22.append('进路准备错误，错误进路准备为：' + dict_Input_22['进路准备'])
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['行车安全距离'] == '一站一区间':
        pass
    else:
        S_xcaqjl_count += 1
        Result_22.append('行车安全距离错误，错误行车安全距离为：' + dict_Input_22['行车安全距离'])
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['盯控'] == '是':
        S_dk_count += 1
        dxdf_22 += S_sq
    else:
        Result_22.append('未对救援连挂车进行盯控')
        plainTextEdit_czpj_22.setStyleSheet('color:red;')
        btu_24.setStyleSheet('background-color: red;')
    if dict_Input_22['限速'] == '25km/h' and dict_Input_22['授权'] == '值班调度长' and dict_Input_22['调度命令'] == '发布对象救援连挂车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对故障车进行清客' and dict_Input_22['进路准备'] == '进路准备正确' and dict_Input_22['行车安全距离'] == '一站一区间' and dict_Input_22['盯控'] == '是':
        Result_22.append('处置正确√')
        plainTextEdit_czpj_22.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_22.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_22,dxdf_22, str(dxzf_22 - dxdf_22)))
    plainTextEdit_czpj_22.setPlainText(str(Result_22))
    Newwindow_22.close()
btu_tc22.pressed.connect(Get_Input_22)

def cao_23():
    btu_24.setStyleSheet('background-color: yellow;')
    label_23.setStyleSheet('background-color: yellow;')
    Newwindow_22.show()
    btu_R_23.setEnabled(False)

plainTextEdit_czpj_22 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_22.resize(250, 70)
plainTextEdit_czpj_22.move(150, 1935)

plainTextEdit_czjl_22 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_22.resize(250, 70)
plainTextEdit_czjl_22.move(430, 1935)

plainTextEdit_dxdfqk_22 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_22.resize(160, 70)
plainTextEdit_dxdfqk_22.move(700, 1935)

btu_R_23 = QPushButton(scrollAreaWidgetContents)
btu_R_23.setText('   操作23   ')
btu_R_23.move(15,1940)
btu_R_23.pressed.connect(cao_23)

##---------------------------------操作24 调令回复------------------------------------------------------------
def cao_24():
    btu_25.setStyleSheet('background-color: yellow;')
    label_24.setStyleSheet('background-color: yellow;')
    mb_10.setText("救援车司机回复：" + dict_Input_22['调度命令'])
    mb_10.open()
    plainTextEdit_sjhf_23.setPlainText("救援车司机、车站调令复诵：" + dict_Input_22['调度命令'])

mb_10 = QMessageBox(window)
mb_10.setWindowTitle('消息提示')

plainTextEdit_sjhf_23 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_23.resize(715, 50)
plainTextEdit_sjhf_23.move(150, 2010)

btu_R_24 = QPushButton(scrollAreaWidgetContents)
btu_R_24.setText('救援车司机、车站\n自动回复')
btu_R_24.move(7,2010)
btu_R_24.setEnabled(False)
btu_R_24.setStyleSheet('font-weight:bold;')
btu_tc22.pressed.connect(cao_24)
##----------------------------------------操作25--故障车清客完毕-----------------------------------------------
def cao_25():
    btu_26.setStyleSheet('background-color: yellow;')
    label_25.setStyleSheet('background-color: yellow;')
    mb_11.setText("故障车司机报告：清客完毕")
    mb_11.open()
    plainTextEdit_sjhf_24.setPlainText("故障车司机报告：清客完毕")

mb_11 = QMessageBox(window)
mb_11.setWindowTitle('消息提示')

plainTextEdit_sjhf_24 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_24.resize(715, 50)
plainTextEdit_sjhf_24.move(150, 2075)

btu_R_25 = QPushButton(scrollAreaWidgetContents)
btu_R_25.setText('故障车司机报告')
btu_R_25.move(15,2080)
btu_R_25.setStyleSheet('font-weight:bold;')
btu_R_25.pressed.connect(cao_25)
##----------------------操作26 发布救援车清客命令 车站--------------------------------------------------------------------
Newwindow_25 =QWidget()
Newwindow_25.setWindowTitle('消息提示')
Newwindow_25.resize(400, 200)
label_tc25 = QLabel(Newwindow_25)
label_tc25.setText('请输入操作内容')
label_tc25.move(10,10)
LineEdit_25 =QLineEdit(Newwindow_25)
LineEdit_25.resize(380,30)
LineEdit_25.move(10, 50)
btu_tc25 =QPushButton(Newwindow_25)
btu_tc25.setText('确定')
btu_tc25.move(150,100)

def Get_Input_25():
    global dict_Input_25, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_25 = S_xs + S_sq + S_ddml
    dxdf_25 = 0
    Input_25 = LineEdit_25.text()
    Result_25 = []
    plainTextEdit_czjl_25.setPlainText(Input_25)
    Input_25_list = Input_25.split('，')#先转成列表
    #授权=无，限速=无，调度命令=发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客
    dict_Input_25 = {}
    for i in range(len(Input_25_list)):
        dict_Input_25[Input_25_list[i].split('=')[0]] = Input_25_list[i].split('=')[1]
    print(dict_Input_25)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_25['调度命令']=='发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客':
        S_ddml_count += 1
        dxdf_25 += S_ddml
    else:
        Result_25.append('调度命令错误，错误调度命令为：'+ dict_Input_25['调度命令'])
        plainTextEdit_czpj_25.setStyleSheet('color:red;')
        btu_27.setStyleSheet('background-color: red;')
    if dict_Input_25['限速']=='无':
        S_xs_count += 1
        dxdf_25 += S_xs
    else:
        Result_25.append('限速错误，错误限速为：'+ dict_Input_25['限速'])
        plainTextEdit_czpj_25.setStyleSheet('color:red;')
        btu_27.setStyleSheet('background-color: red;')
    if dict_Input_25['授权']=='无':
        S_sq_count += 1
        dxdf_25 += S_sq
    else:
        Result_25.append('授权错误，错误授权为：'+ dict_Input_25['授权'])
        plainTextEdit_czpj_25.setStyleSheet('color:red;')
        btu_27.setStyleSheet('background-color: red;')
    if dict_Input_25['限速'] == '无' and dict_Input_25['授权'] == '无' and dict_Input_25['调度命令'] == '发布对象车站命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客' :
        Result_25.append('处置正确√')
        plainTextEdit_czpj_25.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_25.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_25,dxdf_25, str(dxzf_25 - dxdf_25)))
    plainTextEdit_czpj_25.setPlainText(str(Result_25))
    Newwindow_25.close()
btu_tc25.pressed.connect(Get_Input_25)

def cao_26():
    btu_27.setStyleSheet('background-color: yellow;')
    label_26.setStyleSheet('background-color: yellow;')
    Newwindow_25.show()
    btu_R_26.setEnabled(False)

plainTextEdit_czpj_25 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_25.resize(250, 70)
plainTextEdit_czpj_25.move(150, 2150)

plainTextEdit_czjl_25 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_25.resize(250, 70)
plainTextEdit_czjl_25.move(430, 2150)

plainTextEdit_dxdfqk_25 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_25.resize(160, 70)
plainTextEdit_dxdfqk_25.move(700, 2150)

btu_R_26 = QPushButton(scrollAreaWidgetContents)
btu_R_26.setText('   操作26   ')
btu_R_26.move(15,2160)
btu_R_26.pressed.connect(cao_26)
###---------------------------------------------操作27 救援车清客---------------------------------------------
Newwindow_26 =QWidget()
Newwindow_26.setWindowTitle('消息提示')
Newwindow_26.resize(400, 200)
label_tc26 = QLabel(Newwindow_26)
label_tc26.setText('请输入操作内容')
label_tc26.move(10,10)
LineEdit_26 =QLineEdit(Newwindow_26)
LineEdit_26.resize(380,30)
LineEdit_26.move(10, 50)
btu_tc26 =QPushButton(Newwindow_26)
btu_tc26.setText('确定')
btu_tc26.move(150,100)

def Get_Input_26():
    global dict_Input_26, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_26 = S_xs + S_sq + S_ddml
    dxdf_26 = 0
    Input_26 = LineEdit_26.text()
    Result_26 = []
    plainTextEdit_czjl_26.setPlainText(Input_26)
    Input_26_list = Input_26.split('，')#先转成列表
    #授权=无，限速=无，调度命令=发布对象救援车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客
    dict_Input_26 = {}
    for i in range(len(Input_26_list)):
        dict_Input_26[Input_26_list[i].split('=')[0]] = Input_26_list[i].split('=')[1]
    print(dict_Input_26)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_26['调度命令']=='发布对象救援车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客':
        S_ddml_count += 1
        dxdf_26 += S_ddml
    else:
        Result_26.append('调度命令错误，错误调度命令为：'+ dict_Input_26['调度命令'])
        plainTextEdit_czpj_26.setStyleSheet('color:red;')
        btu_28.setStyleSheet('background-color: red;')
    if dict_Input_26['限速']=='无':
        S_xs_count += 1
        dxdf_26 += S_xs
    else:
        Result_26.append('限速错误，错误限速为：'+ dict_Input_26['限速'])
        plainTextEdit_czpj_26.setStyleSheet('color:red;')
        btu_28.setStyleSheet('background-color: red;')
    if dict_Input_26['授权']=='无':
        S_sq_count += 1
        dxdf_26 += S_sq
    else:
        Result_26.append('授权错误，错误授权为：'+ dict_Input_26['授权'])
        plainTextEdit_czpj_26.setStyleSheet('color:red;')
        btu_28.setStyleSheet('background-color: red;')
    if dict_Input_26['限速'] == '无' and dict_Input_26['授权'] == '无' and dict_Input_26['调度命令'] == '发布对象救援车命令号xxx令救援连挂车开999次以切除ATP方式推进至xx站对救援车进行清客' :
        Result_26.append('处置正确√')
        plainTextEdit_czpj_26.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_26.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_26,dxdf_26, str(dxzf_26 - dxdf_26)))
    plainTextEdit_czpj_26.setPlainText(str(Result_26))
    Newwindow_26.close()
btu_tc26.pressed.connect(Get_Input_26)

def cao_27():
    global click_btu5
    click_btu5 = 1
    btu_28.setStyleSheet('background-color: yellow;')
    label_27.setStyleSheet('background-color: yellow;')
    Newwindow_26.show()
    btu_R_27.setEnabled(False)

plainTextEdit_czpj_26 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_26.resize(250, 70)
plainTextEdit_czpj_26.move(150, 2230)

plainTextEdit_czjl_26 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_26.resize(250, 70)
plainTextEdit_czjl_26.move(430, 2230)

plainTextEdit_dxdfqk_26 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_26.resize(160, 70)
plainTextEdit_dxdfqk_26.move(700, 2230)

btu_R_27 = QPushButton(scrollAreaWidgetContents)
btu_R_27.setText('   操作27   ')
btu_R_27.move(15,2240)
btu_R_27.pressed.connect(cao_27)
##------------------------------------操作28  调令复诵--------------------------------------------------------
def cao_28():
    btu_29.setStyleSheet('background-color: yellow;')
    label_27.setStyleSheet('background-color: yellow;')
    mb_12.setText("救援车司机回复：" + dict_Input_26['调度命令'])
    mb_12.open()
    plainTextEdit_sjhf_27.setPlainText("救援车司机、车站调令复诵：" + dict_Input_26['调度命令'])

mb_12 = QMessageBox(window)
mb_12.setWindowTitle('消息提示')

plainTextEdit_sjhf_27 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_27.resize(715, 50)
plainTextEdit_sjhf_27.move(150, 2320)

btu_R_28 = QPushButton(scrollAreaWidgetContents)
btu_R_28.setText('救援车司机、车站\n自动回复')
btu_R_28.move(7,2320)
btu_R_28.setEnabled(False)
btu_R_28.setStyleSheet('font-weight:bold;')
btu_tc26.pressed.connect(cao_28)
##-----------------------------------------------操作29 派人登乘救援车-----------------------------------------
Newwindow_28 =QWidget()
Newwindow_28.setWindowTitle('消息提示')
Newwindow_28.resize(400, 200)
label_tc28 = QLabel(Newwindow_28)
label_tc28.setText('请输入操作内容')
label_tc28.move(10,10)
LineEdit_28 =QLineEdit(Newwindow_28)
LineEdit_28.resize(380,30)
LineEdit_28.move(10, 50)
btu_tc28 =QPushButton(Newwindow_28)
btu_tc28.setText('确定')
btu_tc28.move(150,100)

def Get_Input_28():
    global dict_Input_28, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_28 = S_xs + S_sq + S_gfx + S_zylj
    dxdf_28 = 0
    Input_28 = LineEdit_28.text()
    Result_28 = []
    plainTextEdit_czjl_28.setPlainText(Input_28)
    Input_28_list = Input_28.split('，')#先转成列表
    #授权=无，限速=无，作业环节规范性=要求车站派人登乘救援车
    dict_Input_28 = {}
    for i in range(len(Input_28_list)):
        dict_Input_28[Input_28_list[i].split('=')[0]] = Input_28_list[i].split('=')[1]
    print(dict_Input_28)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_28['作业环节规范性']=='要求车站派人登乘救援车':
        S_gfx_count += 1
        dxdf_28 += S_gfx
    else:
        Result_28.append('作业环节规范性错误，错误作业环节规范性为：'+ dict_Input_28['作业环节规范性'])
        plainTextEdit_czpj_28.setStyleSheet('color:red;')
        btu_30.setStyleSheet('background-color: red;')
    if dict_Input_28['限速']=='无':
        S_xs_count += 1
        dxdf_28 += S_xs
    else:
        Result_28.append('限速错误，错误限速为：'+ dict_Input_28['限速'])
        plainTextEdit_czpj_28.setStyleSheet('color:red;')
        btu_30.setStyleSheet('background-color: red;')
    if dict_Input_28['授权']=='无':
        S_sq_count += 1
        dxdf_28 += S_sq
    else:
        Result_28.append('授权错误，错误授权为：'+ dict_Input_28['授权'])
        plainTextEdit_czpj_28.setStyleSheet('color:red;')
        btu_30.setStyleSheet('background-color: red;')
    if click_btu5 == 1 and click_btu6 == 0:
        S_zylj_count += 1
        dxdf_28 += S_zylj
    else:
        Result_28.append('操作顺序错误:未及时派人登乘救援车')
        plainTextEdit_czpj_28.setStyleSheet('color:red;')
        btu_30.setStyleSheet('background-color: red;')
        mb_2.setText('操作顺序存在错误')
        mb_2.open()
    if dict_Input_28['限速'] == '无' and dict_Input_28['授权'] == '无' and dict_Input_28['作业环节规范性'] == '要求车站派人登乘救援车' and click_btu5==1 and click_btu6==0:
        Result_28.append('处置正确√')
        plainTextEdit_czpj_28.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_28.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_28,dxdf_28, str(dxzf_28 - dxdf_28)))
    plainTextEdit_czpj_28.setPlainText(str(Result_28))
    Newwindow_28.close()
btu_tc28.pressed.connect(Get_Input_28)

def cao_29():
    btu_30.setStyleSheet('background-color: yellow;')
    label_29.setStyleSheet('background-color: yellow;')
    Newwindow_28.show()
    btu_R_29.setEnabled(False)

plainTextEdit_czpj_28 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_28.resize(250, 70)
plainTextEdit_czpj_28.move(150, 2390)

plainTextEdit_czjl_28 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_28.resize(250, 70)
plainTextEdit_czjl_28.move(430, 2390)

plainTextEdit_dxdfqk_28 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_28.resize(160, 70)
plainTextEdit_dxdfqk_28.move(700, 2390)

btu_R_29 = QPushButton(scrollAreaWidgetContents)
btu_R_29.setText('   操作29   ')
btu_R_29.move(15,2400)
btu_R_29.pressed.connect(cao_29)
##---------------------------------------操作30 回复登乘人员已到位----------------------------------------------
def cao_30():
    btu_31.setStyleSheet('background-color: yellow;')
    label_30.setStyleSheet('background-color: yellow;')
    mb_12.setText("车站报告：登乘人员已到位")
    mb_12.open()
    plainTextEdit_sjhf_29.setPlainText("车站报告：登乘人员已到位")

mb_12 = QMessageBox(window)
mb_12.setWindowTitle('消息提示')

plainTextEdit_sjhf_29 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_29.resize(715, 50)
plainTextEdit_sjhf_29.move(150, 2470)

btu_R_30 = QPushButton(scrollAreaWidgetContents)
btu_R_30.setText('车站报告')
btu_R_30.move(15,2470)
btu_R_30.setStyleSheet('font-weight:bold;')
btu_R_30.setEnabled(False)
btu_tc28.pressed.connect(cao_30)
##----------------------------------操作31  救援车请客完毕-----------------------------------------------------
def cao_31():
    btu_32.setStyleSheet('background-color: yellow;')
    label_31.setStyleSheet('background-color: yellow;')
    mb_13.setText("救援车报告：清客完毕")
    mb_13.open()
    plainTextEdit_sjhf_30.setPlainText("救援车报告：清客完毕")

mb_13 = QMessageBox(window)
mb_13.setWindowTitle('消息提示')

plainTextEdit_sjhf_30 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_sjhf_30.resize(715, 50)
plainTextEdit_sjhf_30.move(150, 2540)

btu_R_31 = QPushButton(scrollAreaWidgetContents)
btu_R_31.setText('救援车报告')
btu_R_31.move(15,2540)
btu_R_31.setStyleSheet('font-weight:bold;')
btu_R_31.pressed.connect(cao_31)
##-----------------------------操作32 调度命令 切ATP回车场-----------------------------------------------------
Newwindow_31 =QWidget()
Newwindow_31.setWindowTitle('消息提示')
Newwindow_31.resize(400, 200)
label_tc31 = QLabel(Newwindow_31)
label_tc31.setText('请输入操作内容')
label_tc31.move(10,10)
LineEdit_31 =QLineEdit(Newwindow_31)
LineEdit_31.resize(380,30)
LineEdit_31.move(10, 50)
btu_tc31 =QPushButton(Newwindow_31)
btu_tc31.setText('确定')
btu_tc31.move(150,100)

def Get_Input_31():
    global dict_Input_31, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_31 = S_xs + S_sq + S_ddml +S_dk
    dxdf_31 = 0
    Input_31 = LineEdit_31.text()
    Result_31 = []
    plainTextEdit_czjl_31.setPlainText(Input_31)
    Input_31_list = Input_31.split('，')#先转成列表
    #授权=值班调度长，限速=30km/h，调度命令=命令号xxx令救援连挂车开999次以切除ATP方式推进至xx处，进路准备=进路准备正确，行车安全距离=一站一区间，盯控=是
    dict_Input_31 = {}
    for i in range(len(Input_31_list)):
        dict_Input_31[Input_31_list[i].split('=')[0]] = Input_31_list[i].split('=')[1]
    print(dict_Input_31)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_31['调度命令']=='命令号xxx令救援连挂车开999次以切除ATP方式推进至xx处':
        S_ddml_count += 1
        dxdf_31 += S_ddml
    else:
        Result_31.append('调度命令错误，错误调度命令为：'+ dict_Input_31['调度命令'])
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['限速']=='30km/h':
        S_xs_count += 1
        dxdf_31 += S_xs
    else:
        Result_31.append('限速错误，错误限速为：'+ dict_Input_31['限速'])
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['授权']=='值班调度长':
        S_sq_count += 1
        dxdf_31 += S_sq
    else:
        Result_31.append('授权错误，错误授权为：'+ dict_Input_31['授权'])
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['进路准备'] == '进路准备正确':
        pass
    else:
        S_jlzb_count += 1
        Result_31.append('进路准备错误，错误进路准备为：' + dict_Input_31['进路准备'])
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['行车安全距离'] == '一站一区间':
        pass
    else:
        S_xcaqjl_count += 1
        Result_31.append('行车安全距离错误，错误行车安全距离为：' + dict_Input_31['行车安全距离'])
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['盯控'] == '是':
        S_dk_count += 1
        dxdf_31 += S_sq
    else:
        Result_31.append('未对救援连挂车进行盯控')
        plainTextEdit_czpj_31.setStyleSheet('color:red;')
        btu_33.setStyleSheet('background-color: red;')
    if dict_Input_31['限速'] == '30km/h' and dict_Input_31['授权'] == '值班调度长' and dict_Input_31['调度命令'] == '命令号xxx令救援连挂车开999次以切除ATP方式推进至xx处' and dict_Input_31['进路准备'] == '进路准备正确' and dict_Input_31['行车安全距离'] == '一站一区间' and dict_Input_31['盯控'] == '是':
        Result_31.append('处置正确√')
        plainTextEdit_czpj_31.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_31.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_31,dxdf_31, str(dxzf_31 - dxdf_31)))
    plainTextEdit_czpj_31.setPlainText(str(Result_31))
    Newwindow_31.close()
btu_tc31.pressed.connect(Get_Input_31)

def cao32():
    btu_33.setStyleSheet('background-color: yellow;')
    label_32.setStyleSheet('background-color: yellow;')
    Newwindow_31.show()
    btu_R_32.setEnabled(False)

plainTextEdit_czpj_31 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_31.resize(250, 70)
plainTextEdit_czpj_31.move(150, 2615)

plainTextEdit_czjl_31 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_31.resize(250, 70)
plainTextEdit_czjl_31.move(430, 2615)

plainTextEdit_dxdfqk_31 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_31.resize(160, 70)
plainTextEdit_dxdfqk_31.move(700, 2615)

btu_R_32 = QPushButton(scrollAreaWidgetContents)
btu_R_32.setText('   操作33   ')
btu_R_32.move(15,2625)
btu_R_32.pressed.connect(cao32)
##-----------------------------------------------操作33 通知DCC运转-------------------------------------------
Newwindow_32 =QWidget()
Newwindow_32.setWindowTitle('消息提示')
Newwindow_32.resize(400, 200)
label_tc32 = QLabel(Newwindow_32)
label_tc32.setText('请输入操作内容')
label_tc32.move(10,10)
LineEdit_32 =QLineEdit(Newwindow_32)
LineEdit_32.resize(380,30)
LineEdit_32.move(10, 50)
btu_tc32 =QPushButton(Newwindow_32)
btu_tc32.setText('确定')
btu_tc32.move(150,100)

def Get_Input_32():
    global dict_Input_32, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    #-----------------------------------------------------------------------------------------------------------------
    dxzf_32 = S_xs + S_sq + S_xxjh
    dxdf_32 = 0
    Input_32 = LineEdit_32.text()
    Result_32 = []
    plainTextEdit_czjl_32.setPlainText(Input_32)
    Input_32_list = Input_32.split('，')#先转成列表
    #授权=无，限速=无，信息交互=通知DCC运转救援连挂车即将回库
    dict_Input_32= {}
    for i in range(len(Input_32_list)):
        dict_Input_32[Input_32_list[i].split('=')[0]] = Input_32_list[i].split('=')[1]
    print(dict_Input_32)
    #-----------将input转换成字典类型-----------------------------------------------------
    if dict_Input_32['信息交互']=='通知DCC运转救援连挂车即将回库':
        S_xxjh_count += 1
        dxdf_32 += S_xxjh
    else:
        Result_32.append('信息交互错误，错误信息交互为：'+ dict_Input_32['信息交互'])
        plainTextEdit_czpj_32.setStyleSheet('color:red;')
        btu_34.setStyleSheet('background-color: red;')
    if dict_Input_32['限速']=='无':
        S_xs_count += 1
        dxdf_32 += S_xs
    else:
        Result_32.append('限速错误，错误限速为：'+ dict_Input_32['限速'])
        plainTextEdit_czpj_32.setStyleSheet('color:red;')
        btu_34.setStyleSheet('background-color: red;')
    if dict_Input_32['授权']=='无':
        S_sq_count += 1
        dxdf_32 += S_sq
    else:
        Result_32.append('授权错误，错误授权为：'+ dict_Input_32['授权'])
        plainTextEdit_czpj_32.setStyleSheet('color:red;')
        btu_34.setStyleSheet('background-color: red;')
    if dict_Input_32['限速'] == '无' and dict_Input_32['授权'] == '无' and dict_Input_32['信息交互'] == '通知DCC运转救援连挂车即将回库':
        Result_32.append('处置正确√')
        plainTextEdit_czpj_32.setStyleSheet('background-color: lime;')
    plainTextEdit_dxdfqk_32.setPlainText('单项总分：{}\n单项得分：{}\n单项扣分：{} '.format(dxzf_32,dxdf_32, str(dxzf_32 - dxdf_32)))
    plainTextEdit_czpj_32.setPlainText(str(Result_32))
    Newwindow_32.close()
btu_tc32.pressed.connect(Get_Input_32)

def cao_33():
    btu_34.setStyleSheet('background-color: yellow;')
    label_33.setStyleSheet('background-color: yellow;')
    Newwindow_32.show()
    btu_R_33.setEnabled(False)

plainTextEdit_czpj_32 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czpj_32.resize(250, 70)
plainTextEdit_czpj_32.move(150, 2700)

plainTextEdit_czjl_32 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_czjl_32.resize(250, 70)
plainTextEdit_czjl_32.move(430, 2700)

plainTextEdit_dxdfqk_32 = QPlainTextEdit(scrollAreaWidgetContents)
plainTextEdit_dxdfqk_32.resize(160, 70)
plainTextEdit_dxdfqk_32.move(700, 2700)

btu_R_33 = QPushButton(scrollAreaWidgetContents)
btu_R_33.setText('   操作34   ')
btu_R_33.move(15,2710)
btu_R_33.pressed.connect(cao_33)

##---------#模拟结束按钮，def所有控件的得分结果-------------------------------------------------------------------
def Result():
    global dict_Input_2, T_xs, T_ddml, T_sq, T_dk, T_gfx, T_xxjh, T_zylj, T_ats, T_fzpj  # 应急场景下具体的操作类型数量
    global Y_01  # 0-1变量
    global S_xs, S_ddml, S_sq, S_dk, S_gfx, S_xxjh, S_zylj, S_ats, S_fzpj  # 各部分评价分数
    # S_jlzb = 0; S_xcaqjl = 0; S_rcaq = 0; S_cdaq = 0
    global S_xs_count, S_ddml_count, S_sq_count, S_dk_count, S_gfx_count, S_xxjh_count, S_zylj_count, S_ats_count, S_fzpj_count  # 普通操作正确情况计数
    global S_jlzb_count, S_xcaqjl_count, S_rcaq_count, S_cdaq_count  # 安全性评价操作错误情况计数0-1
    global T_xs ,T_ddml ,T_sq,T_dk ,T_gfx ,T_xxjh,T_zylj,T_ats ,T_fzpj #操作总数量
    if S_jlzb_count + S_xcaqjl_count + S_rcaq_count + S_cdaq_count != 0:
        Y_01 = 1
    else:
        Y_01 = 0
    S_max = S_sq*T_sq + S_ddml*T_ddml + S_xs*T_xs + S_dk*T_dk + S_gfx*T_gfx + S_xxjh*T_xxjh + S_zylj*T_zylj + S_ats*T_ats + S_fzpj*T_fzpj
    S = S_sq*S_sq_count + S_ddml*S_ddml_count + S_xs*S_xs_count + S_dk*S_dk_count + S_gfx*S_gfx_count + S_xxjh*S_xxjh_count + S_zylj*S_zylj_count + S_ats*S_ats_count + S_fzpj*S_fzpj_count - Y_01*S_max*2/5
    #------------------------------------------------------------------------------------------------
    False_xs = T_xs - S_xs_count
    False_ddml=T_ddml - S_ddml_count
    False_sq = T_sq - S_sq_count
    False_dk = T_dk - S_dk_count
    False_gfx = T_gfx - S_gfx_count
    False_xxjh = T_xxjh - S_xxjh_count
    False_zylj = T_zylj - S_zylj_count
    False_ats = T_ats - S_ats_count
    False_fzpj = T_fzpj - S_fzpj_count
    mb_End.setText('\n限速执行错误数量：' + str(False_xs) + '\n调度命令执行错误数量：'+str(False_ddml)
                   + '\n授权执行错误数量：'+str(False_sq) + '\n盯控执行错误数量：'+str(False_dk) + '\n作业环节规范性执行错误数量：'+str(False_gfx)
                + '\n信息交互执行错误数量：'+str(False_xxjh) + '\n作业逻辑执行错误数量：'+ str(False_zylj) + '\nats操作执行错误数量：'+ str(False_ats)
                + '\n辅助评价执行错误数量：'+str(False_fzpj) + '\n满分为：' + str(S_max)+'\n总得分为：' + str(S) + '\n总扣分为：'+ str(S_max-S))
    btu_End.setStyleSheet('background-color: yellow;')
    mb_End.open()
mb_End = QMessageBox(window)
mb_End.setWindowTitle('模拟结束')

btu_R_End =QPushButton(scrollAreaWidgetContents)
btu_R_End.setText('模拟结束')
btu_R_End.move(420,2800)
btu_R_End.pressed.connect(Result)

window.setWindowIcon(QIcon('logo1.png'))
window.show()
sys.exit(app.exec_())
