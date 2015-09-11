import pdfkit
import easygui
import tkFileDialog
from Tkinter import *
import os
import urllib2
#Made by Will Beddow for a client on  fiverr.com
#For more information about me go to http://willbeddow.com
#To hire Will, go to http://fiverr.com/willcbeddow
root = Tk()
root.withdraw()
def overmain():
	def convert(filetype, fileobject):
		if filetype=="url":
			finalname=(fileobject.replace(fileobject.split("://")[0], '').replace('://', '')+'.pdf')
			easygui.msgbox("Saving "+fileobject+" as "+finalname)
			pdfkit.from_url(fileobject, finalname)
			overmain()
		elif filetype=="file":
			finalname=(fileobject.replace(fileobject.split('.')[1], 'pdf'))
			easygui.msgbox("Saving "+fileobject+" as "+finalname)
			pdfkit.from_file(fileobject, finalname)
			overmain()
		elif filetype=="dir":
			os.chdir(fileobject)
			for i in os.listdir(fileobject):
				if ".html" in i or ".htm" in i:
					finalname=(i.replace(i.split('.')[1], 'pdf'))
					pdfkit.from_file(i, fileobject+finalname)
				else:
					pass
			overmain()
	def get_file(filetype):
		if filetype=="dir":
			filename = tkFileDialog.askdirectory()
			return filename
		elif filetype=="file":
			filename = tkFileDialog.askopenfilename()
			return filename
	def main():
		urlchoice = "Supply a url to turn into a pdf"
		filechoice = "Pick a single file to turn into a pdf"
		dirchoice = "Pick a directory, all .html or .htm files within will be converted to pdf"
		mainchoices=[urlchoice,filechoice,dirchoice]
		choice=easygui.choicebox(title="Options", msg="Please select an option", choices=mainchoices)
		if choice==urlchoice:
			filetype="url"
			fileobject=easygui.enterbox("Please enter a url")
			try:
				if "http://" in fileobject or "https://" in fileobject:
					html = urllib2.urlopen(fileobject).read()
					convert(filetype, fileobject)
				else:
					fileobject="http://"+fileobject
					html = urllib2.urlopen(fileobject).read()
					convert(filetype, fileobject)
			except urllib2.HTTPError:
				easygui.msgbox("Invalid url")
				main()
		elif choice==filechoice:
			filetype="file"
			fileobject=get_file(filetype)
			convert(filetype, fileobject)
		elif choice==dirchoice:
			filetype="dir"
			fileobject=get_file(filetype)
			convert(filetype, fileobject)
	main()
overmain()
