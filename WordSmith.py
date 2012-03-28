import wx

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(400,400))
		self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
		self.CreateStatusBar() # A status bar at the bottom of the window

		# Setting up the menu
		filemenu = wx.Menu()
		helpmenu = wx.Menu()

		# wx.ID_ABOUT and wx>ID_EXIT are standard ID's provided by wxWidgets.
		# filemenu.AppendSeparator()
		# Filemenu:
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Termenita the program")

		# Helpmenu:
		menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", " Information about this program")


		# Creating the menubar.
		menuBar = wx.MenuBar()
		# Add the items to the menu:
		menuBar.Append(filemenu, "&File")
		menuBar.Append(helpmenu, "&Help")
		self.SetMenuBar(menuBar) # Adding the MenuBar to the Fram content.

		# Set the events.
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

		self.Show(True)

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