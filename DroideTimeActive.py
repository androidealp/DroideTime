import sublime
import sublime_plugin
import datetime
import sqlite3 
import os

class DroidetimeactiveCommand(sublime_plugin.EventListener):

	def on_activated(self, view):

		
		print(view.window().project_data())

