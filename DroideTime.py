import sublime
import sublime_plugin
import datetime
import sqlite3 
import os

class DroidetimeCommand(sublime_plugin.WindowCommand):

	def run(self):

		#dt_init = str(datetime.datetime.now().strftime('%d/%m/%y, %H:%M'))
		#self.window.status_message(dt_init)

		#/home/andre/.config/sublime-text-3/Packages/User
		# dir_path = os.path.dirname(os.path.realpath(__file__))
		# filedata = dir_path+'/data/DroideTime.db'
		
		# conn = sqlite3.connect(filedata)
		# cursor = conn.cursor()

		# cursor.execute("""CREATE TABLE IF NOT EXISTS registerdata
        #         (id integer not null primary key AUTOINCREMENT, projeto text not null, 
        #         dt_init text not null, dt_end text not null )
        #      """)

		win = sublime.active_window()
		view = win.active_view()
		projectdata = win.project_data()
		

		print(projectdata)

