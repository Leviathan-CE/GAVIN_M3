from src.data import WindowHints


class Event():

    def invoke(self, event):
       pass


class OnTextChanged(Event):
 '''
 listener extendable any class wishing to rercive
 text from possible observers must override the method
 '''

 def On_text_input_changed(self, text: str, event):
    raise NotImplementedError("missing Override of this function")


class OnPushMessageToDisplay(Event):

 def on_push_message(self, text: str, event):
    raise NotImplementedError("missing Override of this function")


class OnWindowResized(Event):

    '''
    called when window is minimized maximized returns to normal
    or other window changing style chioces.
    '''

    def on_window_resize(self, hint: WindowHints, event):
        raise NotImplementedError("missing Override of this function")
