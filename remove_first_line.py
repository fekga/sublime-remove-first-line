import sublime
import sublime_plugin


class RemoveFirstLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        span = region.begin(),region.end()
        if span == (0,0):
            self.view.erase(edit,self.view.full_line(sublime.Region(0,1)))
