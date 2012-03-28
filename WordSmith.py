import wx
import os

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800,600))
		self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
		self.CreateStatusBar() # A status bar at the bottom of the window

		# Setting up the menu
		filemenu = wx.Menu()
		editmenu = wx.Menu()
		toolsmenu = wx.Menu()
		helpmenu = wx.Menu()

		# wx.ID_ABOUT and wx>ID_EXIT are standard ID's provided by wxWidgets.
		
		# Filemenu:
		menuNew = filemenu.Append(wx.ID_NEW, "&New", " Open a new file")
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open an existing file")
		menuSave = filemenu.Append(wx.ID_SAVE, "&Save", " Save the file to disk")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Termenita the program")

		# Editmenu

		# Tools menu

		# Helpmenu:
		menuHelp = helpmenu.Append(wx.ID_HELP, "&Help", " Show help about this program")
		menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", " Information about this program")


		# Creating the menubar.
		menuBar = wx.MenuBar()
		# Add the items to the menu:
		menuBar.Append(filemenu, "&File")
		menuBar.Append(editmenu, "&Edit")
		menuBar.Append(toolsmenu, "&Tools")
		menuBar.Append(helpmenu, "&Help")
		self.SetMenuBar(menuBar) # Adding the MenuBar to the Fram content.

		# Set the events.
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

		self.Show(True)

	def OnOpen(self, e):
		""" Open a file """
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
		dlg.Destroy()

	def OnSave(self, e):
		""" Save a file """
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a save location", self.dirname, "", "*.*", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'w')
			f.write(self.control.GetValue())
		dlg.Destroy()

	def OnAbout(self, e):
		# A message dialog box with an OK button. wxOk is a standard ID in wxWidgets
		dlg = wx.MessageDialog( self, "A small text editor", "About WordSmith", wx.OK)
		dlg.ShowModal() # Show it
		dlg.Destroy() # And destroy it when its finished

	def OnExit (self, e):
		self.Close(True)  # Close the frame

app = wx.App(False)
frame = MainWindow(None, "WordSmith")
app.MainLoop()