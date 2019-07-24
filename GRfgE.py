#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.2 on Wed Apr 10 16:48:31 2019
#

import wx
import pylab
import math

import G
import GRMain
import WelcomePage

import numpy as np

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


# end wxGlade


class MyFrame(wx.Frame):
    Parent = None

    def __init__(self, *args, **kwds):
        # begin wxGlade: GRfgE.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1300, 700))
        self.Panel = wx.Panel(self, wx.ID_ANY)
        self.panel1 = wx.Panel(self.Panel, wx.ID_ANY)
        figure1 = self.matplotlib_figure = Figure()
        self.matplotlib_axes1 = figure1.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure1 = FigureCanvas(self.panel1, wx.ID_ANY, figure1)
        self.checkbox1 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn1 = wx.RadioButton(self.Panel, wx.ID_ANY, "Iteration")
        self.panel4 = wx.Panel(self.Panel, wx.ID_ANY)
        figure4 = self.matplotlib_figure = Figure()
        self.matplotlib_axes4 = figure4.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure4 = FigureCanvas(self.panel4, wx.ID_ANY, figure4)
        self.checkbox4 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn4 = wx.RadioButton(self.Panel, wx.ID_ANY, "Local Thresholding")
        self.panel2 = wx.Panel(self.Panel, wx.ID_ANY)
        figure2 = self.matplotlib_figure = Figure()
        self.matplotlib_axes2 = figure2.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure2 = FigureCanvas(self.panel2, wx.ID_ANY, figure2)
        self.checkbox2 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn2 = wx.RadioButton(self.Panel, wx.ID_ANY, "Homogeneity")
        self.panel5 = wx.Panel(self.Panel, wx.ID_ANY)
        figure5 = self.matplotlib_figure = Figure()
        self.matplotlib_axes5 = figure5.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure5 = FigureCanvas(self.panel5, wx.ID_ANY, figure5)
        self.checkbox5 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn5 = wx.RadioButton(self.Panel, wx.ID_ANY, "Otsu")
        self.panel3 = wx.Panel(self.Panel, wx.ID_ANY)
        figure3 = self.matplotlib_figure = Figure()
        self.matplotlib_axes3 = figure3.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure3 = FigureCanvas(self.panel3, wx.ID_ANY, figure3)
        self.checkbox3 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn3 = wx.RadioButton(self.Panel, wx.ID_ANY, "The maximum distance \nbetween classes")
        self.panel6 = wx.Panel(self.Panel, wx.ID_ANY)
        figure6 = self.matplotlib_figure = Figure()
        self.matplotlib_axes6 = figure6.add_subplot(111)  # 1x1 grid, first subplot
        self.matplotlib_canvas6 = FigureCanvas(self.panel6, wx.ID_ANY, figure6)
        self.Figure6 = FigureCanvas(self.panel6, wx.ID_ANY, figure6)
        self.checkbox6 = wx.CheckBox(self.Panel, wx.ID_ANY, "")
        self.radio_btn6 = wx.RadioButton(self.Panel, wx.ID_ANY, "The maximum entropy")
        self.panel7 = wx.Panel(self.Panel, wx.ID_ANY)
        figure7 = self.matplotlib_figure = Figure()
        self.matplotlib_axes7 = figure7.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure7 = FigureCanvas(self.panel7, wx.ID_ANY, figure7)
        self.OriginImBtn = wx.Button(self.Panel, wx.ID_ANY, "The Original Image")
        self.fgExtratBtn = wx.Button(self.Panel, wx.ID_ANY, "Foreground Extraction")
        self.fgConfirmBtn = wx.Button(self.Panel, wx.ID_ANY, "Foreground Confirm")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OriginImShow, self.OriginImBtn)
        self.Bind(wx.EVT_BUTTON, self.fgCalculate, self.fgExtratBtn)
        self.Bind(wx.EVT_BUTTON, self.fgConfirm, self.fgConfirmBtn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: GRfgE.__set_properties
        self.SetTitle("Foreground Extract")
        self.Figure1.SetMinSize((200, 300))
        self.panel1.SetMinSize((200, 300))
        self.checkbox1.SetMinSize((20, 40))
        self.radio_btn1.SetMinSize((180, 40))
        self.Figure4.SetMinSize((200, 300))
        self.panel4.SetMinSize((200, 300))
        self.checkbox4.SetMinSize((20, 40))
        self.radio_btn4.SetMinSize((180, 40))
        self.Figure2.SetMinSize((200, 300))
        self.panel2.SetMinSize((200, 300))
        self.checkbox2.SetMinSize((20, 40))
        self.radio_btn2.SetMinSize((180, 40))
        self.Figure5.SetMinSize((200, 300))
        self.panel5.SetMinSize((200, 300))
        self.checkbox5.SetMinSize((20, 40))
        self.radio_btn5.SetMinSize((180, 40))
        self.Figure3.SetMinSize((200, 300))
        self.panel3.SetMinSize((200, 300))
        self.checkbox3.SetMinSize((20, 40))
        self.radio_btn3.SetMinSize((180, 40))
        self.Figure6.SetMinSize((200, 300))
        self.panel6.SetMinSize((200, 300))
        self.checkbox6.SetMinSize((20, 40))
        self.radio_btn6.SetMinSize((180, 40))
        self.Figure7.SetMinSize((300, 450))
        self.panel7.SetMinSize((300, 500))
        self.OriginImBtn.SetMinSize((300, 40))
        self.fgExtratBtn.SetMinSize((300, 40))
        self.fgComfirmBtn.SetMinSize((300, 40))
        self.Panel.SetMinSize((1300, 700))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: GRfgE.__do_layout
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.VERTICAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.BoxSizer(wx.VERTICAL)
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_27 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8.Add(self.Figure1, 1, wx.EXPAND, 0)
        self.panel1.SetSizer(sizer_8)
        sizer_6.Add(self.panel1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_7.Add(self.checkbox1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_7.Add(self.radio_btn1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_6.Add(sizer_7, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_27.Add(sizer_6, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_13.Add(self.Figure4, 1, wx.EXPAND, 0)
        self.panel4.SetSizer(sizer_13)
        sizer_12.Add(self.panel4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_14.Add(self.checkbox4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_14.Add(self.radio_btn4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_12.Add(sizer_14, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_27.Add(sizer_12, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_26.Add(sizer_27, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_10.Add(self.Figure2, 1, wx.EXPAND, 0)
        self.panel2.SetSizer(sizer_10)
        sizer_9.Add(self.panel2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_15.Add(self.checkbox2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_15.Add(self.radio_btn2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_9.Add(sizer_15, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_28.Add(sizer_9, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_20.Add(self.Figure5, 1, wx.EXPAND, 0)
        self.panel5.SetSizer(sizer_20)
        sizer_19.Add(self.panel5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_21.Add(self.checkbox5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_21.Add(self.radio_btn5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_19.Add(sizer_21, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_28.Add(sizer_19, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_26.Add(sizer_28, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_17.Add(self.Figure3, 1, wx.EXPAND, 0)
        self.panel3.SetSizer(sizer_17)
        sizer_16.Add(self.panel3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_18.Add(self.checkbox3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_18.Add(self.radio_btn3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_16.Add(sizer_18, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_29.Add(sizer_16, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_23.Add(self.Figure6, 1, wx.EXPAND, 0)
        self.panel6.SetSizer(sizer_23)
        sizer_22.Add(self.panel6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_24.Add(self.checkbox6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_24.Add(self.radio_btn6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        sizer_22.Add(sizer_24, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_29.Add(sizer_22, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_26.Add(sizer_29, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_25.Add(self.Figure7, 1, wx.EXPAND, 0)
        self.panel7.SetSizer(sizer_25)
        sizer_3.Add(self.panel7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_3.Add(self.OriginImBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_3.Add(self.fgExtratBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_3.Add(self.fgComfirmBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_26.Add(sizer_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_1.Add(sizer_26, 1, wx.EXPAND, 0)
        self.Panel.SetSizer(sizer_1)
        sizer_11.Add(self.Panel, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.SetSizer(sizer_11)
        self.Layout()
        # end wxGlade

    def OriginImShow(self, event):  # wxGlade: GRfgE.<event_handler>
        #print("Event handler 'OriginImShow' not implemented!")
        #event.Skip()

        G.fore = np.copy(G.HyperDataAve)
        # print(fore.shape)

        self.matplotlib_axes7.imshow(G.fore, cmap='jet')
        self.matplotlib_axes7.set_xticks([])
        self.matplotlib_axes7.set_yticks([])
        self.Figure7.draw()

    def fgConfirm(self, event):  # wxGlade: GRfgE.<event_handler>
        print("Event handler 'fgComfirm' not implemented!")
        event.Skip()

        if self.radio_btn1.GetValue():
            G.foreP = np.copy(G.iteration)
        elif self.radio_btn2.GetValue():
            G.foreP = np.copy(G.homogeneity)
        elif self.radio_btn3.GetValue():
            G.foreP = np.copy(G.distance)
        elif self.radio_btn4.GetValue():
            G.foreP = np.copy(G.local)
        elif self.radio_btn5.GetValue():
            G.foreP = np.copy(G.Otsu)
        elif self.radio_btn6.GetValue():
            G.foreP = np.copy(G.comentropy)
        else:
            pass

        G.fore = np.multiply(G.fore, G.foreP)

        print(self.Parent)

        self.Parent.matplotlib_axes3.imshow(G.fore, cmap='jet')
        self.Parent.matplotlib_axes3.set_xticks([])
        self.Parent.matplotlib_axes3.set_yticks([])
        self.Parent.Figure3.draw()

        self.Destroy()
        self.Parent.Show()

    def fgCalculate(self, event):  # wxGlade: GRfgE.<event_handler>
        #print("Event handler 'fgCalculate' not implemented!")
        #event.Skip()

        # CN~点击次数?
        #G.CN = 0

        #print(self.checkbox1.GetValue())
        #print(self.radio_btn1.GetValue())
        # print(G.HyperDataAve.min())

        # Iteration算法
        try:
            if self.checkbox1.GetValue():
                # G.CN = G.CN+1
                G.iteration = G.Iteration(G.HyperDataAve, 0.3, 0.5, 0.0001)
                # 绘图
                self.matplotlib_axes1.imshow(G.iteration, cmap='jet')
                self.matplotlib_axes1.set_xticks([])
                self.matplotlib_axes1.set_yticks([])
                self.Figure1.draw()

        except Exception as err:
            pass

        # homogeneity
        # 算法有点慢
        # 求d的过程采用遍历，有无其它方案？
        try:
            if self.checkbox2.GetValue():
                G.homogeneity = G.Homogeneity(G.HyperDataAve, 1000)
                # 绘图
                self.matplotlib_axes2.imshow(G.homogeneity, cmap='jet')
                self.matplotlib_axes2.set_xticks([])
                self.matplotlib_axes2.set_yticks([])
                self.Figure2.draw()

        except Exception as err:
            pass

        # The maximum distance between classes
        try:
            if self.checkbox3.GetValue():
                G.distance = G.Distance(G.HyperDataAve, 1000)
                # 绘图
                self.matplotlib_axes3.imshow(G.distance, cmap='jet')
                self.matplotlib_axes3.set_xticks([])
                self.matplotlib_axes3.set_yticks([])
                self.Figure3.draw()

        except Exception as err:
            pass

        # Local Threshold
        try:
            if self.checkbox4.GetValue():
                G.local = G.LocalThreshold(G.HyperDataAve, 5, 3)
                # 子区域划分数，ee=行，kk=列
                #ee, kk = 5, 3  # 考虑界面上输入
                # 绘图
                self.matplotlib_axes4.imshow(G.local, cmap='jet')
                self.matplotlib_axes4.set_xticks([])
                self.matplotlib_axes4.set_yticks([])
                self.Figure4.draw()

        except Exception as err:
            pass

        # Otsu
        try:
            if self.checkbox5.GetValue():
                G.Otsu = G.otsu_(G.HyperDataAve)
                # 绘图
                self.matplotlib_axes5.imshow(G.Otsu, cmap='jet')
                self.matplotlib_axes5.set_xticks([])
                self.matplotlib_axes5.set_yticks([])
                self.Figure5.draw()

        except Exception as err:
            pass

        # maximum entropy
        try:
            if self.checkbox6.GetValue():
                G.comentropy = G.Comentropy(G.HyperDataAve, 256)
                # 绘图
                self.matplotlib_axes6.imshow(G.comentropy, cmap='jet')
                self.matplotlib_axes6.set_xticks([])
                self.matplotlib_axes6.set_yticks([])
                self.Figure6.draw()

        except Exception as err:
            pass

# end of class GRfgE

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()


