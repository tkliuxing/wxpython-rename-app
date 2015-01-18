# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"wxRename"), pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0|wx.TAB_TRAVERSAL )
		self.menu_file = wx.Menu()
		self.menu_opendir = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Open folder"), wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.menu_opendir )
		
		self.menu_file.AppendSeparator()
		
		self.menu_opencfg = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Open configure file"), wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.menu_opencfg )
		
		self.menu_savecfg = wx.MenuItem( self.menu_file, wx.ID_ANY, _(u"Save configure file"), wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.menu_savecfg )
		
		self.m_menubar1.Append( self.menu_file, _(u"file") ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		top_layout_flex = wx.FlexGridSizer( 2, 0, 0, 0 )
		top_layout_flex.AddGrowableCol( 0 )
		top_layout_flex.AddGrowableRow( 0 )
		top_layout_flex.SetFlexibleDirection( wx.BOTH )
		top_layout_flex.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		data_grid = wx.GridSizer( 1, 1, 0, 0 )
		
		self.data_view = self.ex_TestListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_EDIT_LABELS|wx.LC_HRULES|wx.LC_REPORT|wx.LC_SORT_ASCENDING|wx.LC_VRULES )
		data_grid.Add( self.data_view, 0, wx.EXPAND, 5 )
		
		
		top_layout_flex.Add( data_grid, 1, wx.EXPAND, 5 )
		
		bottom_flex = wx.FlexGridSizer( 0, 2, 0, 0 )
		bottom_flex.AddGrowableCol( 0 )
		bottom_flex.SetFlexibleDirection( wx.BOTH )
		bottom_flex.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.notebook.SetMinSize( wx.Size( 590,-1 ) )
		
		self.pan_num = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		pan_num_box = wx.FlexGridSizer( 3, 4, 0, 0 )
		pan_num_box.AddGrowableCol( 1 )
		pan_num_box.AddGrowableCol( 3 )
		pan_num_box.SetFlexibleDirection( wx.BOTH )
		pan_num_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.label1 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Start"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		pan_num_box.Add( self.label1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_start = wx.SpinCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TAB_TRAVERSAL, 0, 2147483647, 0 )
		pan_num_box.Add( self.num_start, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label2 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Prefix"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )
		pan_num_box.Add( self.label2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_prefix = wx.TextCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		pan_num_box.Add( self.num_prefix, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label3 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Length"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )
		pan_num_box.Add( self.label3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_length = wx.SpinCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TAB_TRAVERSAL, 0, 10, 0 )
		pan_num_box.Add( self.num_length, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label4 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Sufix"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label4.Wrap( -1 )
		pan_num_box.Add( self.label4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_sufix = wx.TextCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		pan_num_box.Add( self.num_sufix, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label5 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Match"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label5.Wrap( -1 )
		pan_num_box.Add( self.label5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_match = wx.TextCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		pan_num_box.Add( self.num_match, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label6 = wx.StaticText( self.pan_num, wx.ID_ANY, _(u"Exclude"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label6.Wrap( -1 )
		pan_num_box.Add( self.label6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.num_exclude = wx.TextCtrl( self.pan_num, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		pan_num_box.Add( self.num_exclude, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pan_num.SetSizer( pan_num_box )
		self.pan_num.Layout()
		pan_num_box.Fit( self.pan_num )
		self.notebook.AddPage( self.pan_num, _(u"Number"), False )
		self.pan_rep = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.notebook.AddPage( self.pan_rep, _(u"Replace"), False )
		
		bottom_flex.Add( self.notebook, 1, wx.EXPAND, 5 )
		
		self.pan_bottom = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pan_bottom.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		button_box = wx.GridBagSizer( 10, 0 )
		button_box.SetFlexibleDirection( wx.BOTH )
		button_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		button_box.AddSpacer( ( 0, 13 ), wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.btn_reset = wx.Button( self.pan_bottom, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		button_box.Add( self.btn_reset, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.RIGHT, 5 )
		
		self.btn_preview = wx.Button( self.pan_bottom, wx.ID_ANY, _(u"Preview"), wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		button_box.Add( self.btn_preview, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.RIGHT, 5 )
		
		self.btn_rename = wx.Button( self.pan_bottom, wx.ID_ANY, _(u"Rename"), wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.btn_rename.SetDefault() 
		button_box.Add( self.btn_rename, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.RIGHT, 5 )
		
		
		self.pan_bottom.SetSizer( button_box )
		self.pan_bottom.Layout()
		button_box.Fit( self.pan_bottom )
		bottom_flex.Add( self.pan_bottom, 1, wx.EXPAND, 5 )
		
		
		top_layout_flex.Add( bottom_flex, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( top_layout_flex )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

