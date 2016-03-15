#!/usr/bin/python3

import os
import sys
import webbrowser
from gi.repository import Gtk, Gdk, WebKit, Soup

class Messenger(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(Messenger, self).__init__(*args, **kwargs)

		self.connect("destroy", Gtk.main_quit)
		self.connect("key-press-event", self.key_pressed)
		self.set_size_request(800, 600)
		self.set_icon_from_file("/opt/messenger/messenger.svg")

		if not os.path.exists(os.path.expanduser("~/.messenger")) or not os.path.isdir(os.path.expanduser("~/.messenger")):
			os.makedirs(os.path.expanduser("~/.messenger"))
			open(os.path.expanduser("~/.messenger/cookies.txt"), "a").close()

		cookiejar = Soup.CookieJarText.new(os.path.expanduser("~/.messenger/cookies.txt"), False)
		cookiejar.set_accept_policy(Soup.CookieJarAcceptPolicy.ALWAYS)
		session = WebKit.get_default_session()
		session.add_feature(cookiejar)

		self.webview = WebKit.WebView()
		self.webview.get_settings().set_property("enable-smooth-scrolling", True)
		self.webview.get_settings().set_property("enable-default-context-menu", False)

		self.webview.connect("title-changed", self.title_changed)
		self.webview.connect("load-finished", self.load_finished)
		self.webview.connect("new-window-policy-decision-requested", self.link_clicked)

		self.scrolled_window = Gtk.ScrolledWindow()

		self.webview.load_uri("https://messenger.com/login")

		self.scrolled_window.add(self.webview)
		self.add(self.scrolled_window)

		self.show_all()

	def title_changed(self, view, frame, title):
		self.set_title(self.webview.get_title())

	def console_message(self, view, msg, n, something):
		print("MSGMSGMSG")
		print(msg)

	def load_finished(self, view, frame):
		pass
		# self.webview.execute_script(open("/opt/messenger/inject.js", "r").read())

	def key_pressed(self, widget, event):
		if (event.keyval == Gdk.KEY_F5):
			self.webview.reload()

	def link_clicked(self, view, frame, req, nav, pol):
		webbrowser.open(req.get_uri())

if __name__ == "__main__":
	Gtk.init(sys.argv)

	messenger = Messenger()

	Gtk.main()