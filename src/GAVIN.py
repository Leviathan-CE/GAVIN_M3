

from src.api.EventHandler import OnTextChanged, EventObserver


class ModelFoundation(OnTextChanged, EventObserver):
    
    def __init__(self):
        EventObserver.sub_event(self,listeners=self)
    
    def On_text_input_changed(self,text:str, event):
        print(f"{text} + it worked")