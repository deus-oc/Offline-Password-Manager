import tkinter as tk
from tkinter import PhotoImage, scrolledtext
from tkinter.constants import TOP
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame
from Database.PDatabase import siteData


class HomeFrame(tk.Frame):
	def __init__(self, parent, controller):
		from Frames.loginFrame import LoginFrame
		tk.Frame.__init__(self, parent)
		#colors
		self.primaryColor = '#4479ff'
		self.backgroundColor = '#aac2ff'
		self.surface1Color = '#ffffff'
		self.surface2Color = '#212121'
		self.successColor = '#03dac6'
		self.errorColor = '#cf6679'
		self.priTextColor = '#000000'
		self.secTextColor = '#000000'
		#fonts
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12, "bold")

		# frame components
		self.homeFrame = tk.LabelFrame(self, text="Home - Saved Credentials", bg=self.backgroundColor, fg=self.secTextColor, bd=5)
		self.homeFrame.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.homeBoxFrame = tk.Frame(self.homeFrame, bd=5, bg=self.backgroundColor)
		self.homeBoxFrame.place(relx=0.05, rely=0.025, relwidth=0.9, relheight=0.8)
		#datatable
		self.viewData = scrolledtext.ScrolledText(self.homeBoxFrame, font=self.labelFont, bg=self.surface1Color)
		self.viewData.place(relheight=1, relwidth=1)
		#button
		self.refreshBtn = tk.Button(self.homeFrame, command=self.insertScrolledText, bg=self.successColor)
		self.refreshBtn.place(relx=0.96, rely=0.045, relwidth=0.029, relheight=0.025)
		self.logoutBtn = tk.Button(self.homeFrame, command=lambda:[controller.show_frame(LoginFrame)], bg=self.errorColor)
		self.logoutBtn.place(relx=0.96, rely=0.095, relwidth=0.029, relheight=0.025)
		self.newPassBtn = tk.Button(self.homeFrame, text = "Add New Password", bg=self.primaryColor, fg=self.secTextColor, command=lambda:[controller.show_frame(AddPassFrame)], font = self.labelFont)
		self.newPassBtn.place(relx=0.15, rely=0.855, relwidth=0.3, relheight=0.08)
		self.searchPassBtn = tk.Button(self.homeFrame, text = "Retrive Password", bg=self.primaryColor, fg=self.secTextColor, command=lambda:[controller.show_frame(SearchPassFrame)], font = self.labelFont)
		self.searchPassBtn.place(relx=0.55, rely=0.855, relwidth=0.3, relheight=0.08)
		
		self.insertScrolledText()

	def insertScrolledText(self):
		self.viewData.config(state='normal')
		self.viewData.delete(1.0, 'end')
		VObj = siteData()
		allPass = VObj.viewData()
		heading = "\tSiteName \t\t | \t Username\n"
		heading += "-"*90+"\n"
		self.viewData.insert('insert', heading, 'head')
		for d in allPass:
			info ="\t"+d[0]+" \t\t | \t "+d[1]+"\n"
			info+="-"*90+"\n"
			self.viewData.insert('insert', info, 'data')
		self.viewData.tag_config('head', background=self.primaryColor, foreground=self.secTextColor)
		self.viewData.tag_config('data', foreground=self.secTextColor)
		self.viewData.config(state='disabled')