# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 20:52:18 2015

@author: ronald
"""

import os
import sys
import wx
import glob

import images
import wx.lib.mixins.listctrl as listmix
from layout import MainFrame

import gettext

_ = gettext.gettext


class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):

    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)


class MyFrame(MainFrame, listmix.ColumnSorterMixin):

    def __init__(self, *args, **kwargs):
        self.ex_TestListCtrl = TestListCtrl
        super(MyFrame, self).__init__(*args, **kwargs)
        self.il = wx.ImageList(16, 16)
        self.sm_up = self.il.Add(images.SmallUpArrow.GetBitmap())
        self.sm_dn = self.il.Add(images.SmallDnArrow.GetBitmap())
        self.itemDataMap = {}  # ColumnSorterMixin 依赖
        self._init__data_view()
        self.data_view.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        listmix.ColumnSorterMixin.__init__(self, 3)  # ColumnSorterMixin 依赖
        self.folder = os.getcwd()
        self.Bind(wx.EVT_MENU, self.OnOpen, self.menu_opendir)
        self.Bind(wx.EVT_BUTTON, self.get_active_tag, self.btn_preview)

    def _init__data_view(self):
        self.data_view.InsertColumn(0, "Before")
        self.data_view.InsertColumn(1, "After")
        self.data_view.InsertColumn(2, "Status")
        self.data_view.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.data_view.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.data_view.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)

    def _auto_data_view_size(self, num=1):
        if num > 3:
            num = 3
        for i in range(0, num):
            self.data_view.SetColumnWidth(i, wx.LIST_AUTOSIZE)
        for i in range(num, 2):
            self.data_view.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER)

    # ColumnSorterMixin 依赖
    def GetListCtrl(self):
        return self.data_view

    # ColumnSorterMixin 依赖
    def GetSortImages(self):
        return (self.sm_dn, self.sm_up)

    def OnOpen(self, event):
        dlg = wx.DirDialog(self, "Open directory...",
                           os.getcwd(),
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.folder = dlg.GetPath()
            self.show_files(True)
        dlg.Destroy()

    def get_active_tag(self, event):
        panel = self.notebook.GetSelection()
        panel_dict = {-1: "Error", 0: "number", 1: "replace"}
        return panel_dict[panel]

    def get_files(self):
        """Read file list from self.folder"""
        files = glob.glob(os.path.join(self.folder, "*"))
        datas = [(filename, "", "") for filename in map(
            lambda x:os.path.split(x)[1], files) if filename]
        self.itemDataMap = dict(zip(range(0, len(datas)), datas))

    def show_files(self, flush_data=False):
        """Display self.itemDataMap to ListControl"""
        self.data_view.DeleteAllItems()
        if flush_data:
            self.get_files()
        for key, val in self.itemDataMap.items():
            index = self.data_view.InsertStringItem(sys.maxint, val[0])
            self.data_view.SetStringItem(index, 1, val[1])
            self.data_view.SetStringItem(index, 1, val[1])
            self.data_view.SetItemData(index, key)
        self._auto_data_view_size()


class RenameApp(wx.App):

    def OnInit(self):
        main_frame = MyFrame(None)
        self.SetTopWindow(main_frame)
        main_frame.Show()
        return 1


if __name__ == "__main__":
    gettext.install("appTest")  # replace with the appropriate catalog name

    appTest = RenameApp(0)
    appTest.MainLoop()
