PREFIX=/usr
MANDIR=$(PREFIX)/share/man
BINDIR=$(PREFIX)/bin

.PHONY: all install uninstall

all:
	@echo "Run 'make install' for installation."
	@echo "Run 'make uninstall' for uninstallation."

install:
	[ ! -d /lib/systemd/system ] || install -Dm644 awr_web.service $(DESTDIR)$(PREFIX)/lib/systemd/system/awr_web.service
	systemctl daemon-reload

uninstall:
	rm -f $(DESTDIR)$(BINDIR)/awr_web
	rm -f $(DESTDIR)$(PREFIX)/lib/systemd/system/awr_web.service
