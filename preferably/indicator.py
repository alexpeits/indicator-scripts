import os
import signal
from fnmatch import fnmatch
from collections import defaultdict
from subprocess import call

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

from preferably.resources import ICON_PATH, TOP_DIR, SCRIPT_TEMPLATE

APP_NAME = 'indicator-scripts'

ENV = os.environ.copy()
ENV['DISPLAY'] = ':0'


class ScriptsIndicator(object):

    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            APP_NAME,
            ICON_PATH,
            AppIndicator3.IndicatorCategory.OTHER
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

    def build_menu(self):
        menu = self.make_menus(TOP_DIR, Gtk.Menu())

        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        item_reload = Gtk.MenuItem('Reload')
        item_reload.connect('activate', self.reload)
        menu.append(item_reload)

        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()

        return menu

    def make_menus(self, path, menu):
        gen = os.walk(path)
        root, dirs, files = next(gen)
        for f in files:
            item = Gtk.MenuItem(f)
            item.abspath = os.path.abspath(os.path.join(root, f))
            item.connect('activate', self.run)
            menu.append(item)
        for d in dirs:
            item = Gtk.MenuItem(d)
            submenu = Gtk.Menu()
            item.set_submenu(self.make_menus(os.path.join(root, d), submenu))
            menu.append(item)

        return menu

    def reload(self, item):
        # TODO
        self.indicator.set_menu(self.build_menu())

    def run(self, item):
        # TODO
        call([SCRIPT_TEMPLATE, item.abspath], env=ENV)

    def stop(self, source):
        Gtk.main_quit()


def main():
    ScriptsIndicator()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == "__main__":
    main()
