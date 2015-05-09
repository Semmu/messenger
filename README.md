# Messenger
A headless browser window for Facebook's [Messenger.com](https://messenger.com).
![Screenshot](screenshot.png)

## Why?
[Messenger.com](https://messenger.com) is really great if you use mostly only the chat functionality of Facebook. Giving it a headless browser opens a lot of possibilities, like native notifications and better OS integration. That is the main goal of this project.

## Requirements
* python3
* gtk3
* wekbit

## Features
* headless browser
* saves cookies, remembers login credentials (if you check it)
* launcher icon

## TODO
* allow only one instance running (via dbus or GtkApplication)
* native desktop notifications
* inject smooth scrolling and don't break the current javascript scroll events
* attachment download support
* memory leak (?) fix
* Gtk headerbar support

## Installation
Clone this repository into /opt/messenger (filenames are hardcoded currently)
Optional: copy /opt/messenger/messenger.desktop to /usr/share/applications/ and make it executable.

## License
GPLv3
