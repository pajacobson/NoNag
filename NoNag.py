import sublime_plugin


class NoNagCloseCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()

        if view.is_primary():
            return

        pv = view.buffer().primary_view()

        # Sublime does not prompt to save if a buffer is marked as scratch
        pv.set_scratch(True)
        view.close()
        pv.set_scratch(False)
