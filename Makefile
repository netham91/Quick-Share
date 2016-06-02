# Puts a copy of the file under /usr/local/bin
# Commands must be run under sudo.

install:
	cp quickshare.py /usr/local/bin/quickshare
	chmod +x /usr/local/bin/quickshare

uninstall:
	rm /usr/local/bin/quickshare