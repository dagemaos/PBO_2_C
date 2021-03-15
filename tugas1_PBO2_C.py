# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class formFrame
###########################################################################

class formFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HELLO WX", pos = wx.DefaultPosition, size = wx.Size( 552,451 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		formPage = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.m_panel5.SetMaxSize( wx.Size( -1,100 ) )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.hellowx = wx.StaticText( self.m_panel5, wx.ID_ANY, u"HELLO WX", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.hellowx.Wrap( -1 )

		self.hellowx.SetFont( wx.Font( 50, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Felix Titling" ) )
		self.hellowx.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		fgSizer6.Add( self.hellowx, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( fgSizer6 )
		self.m_panel5.Layout()
		fgSizer6.Fit( self.m_panel5 )
		formPage.Add( self.m_panel5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer4.SetMinSize( wx.Size( 250,500 ) )
		self.nama = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		fgSizer4.Add( self.nama, 0, wx.ALL, 5 )

		self.inp_nama = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inp_nama.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer4.Add( self.inp_nama, 0, wx.ALL, 5 )

		self.nim = wx.StaticText( self.m_panel1, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nim.Wrap( -1 )

		fgSizer4.Add( self.nim, 0, wx.ALL, 5 )

		self.inp_nim = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inp_nim.SetMaxLength( 12 )
		self.inp_nim.SetMinSize( wx.Size( 150,-1 ) )

		fgSizer4.Add( self.inp_nim, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_ok = wx.Button( self.m_panel1, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btn_ok, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer4 )
		self.m_panel1.Layout()
		fgSizer4.Fit( self.m_panel1 )
		formPage.Add( self.m_panel1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( formPage )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


