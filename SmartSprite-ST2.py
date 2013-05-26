import sublime
import sublime_plugin
import re


class SublimeOnSaveBuild(sublime_plugin.EventListener):
    def on_post_save(self, view):
        view.window().run_command('build')
