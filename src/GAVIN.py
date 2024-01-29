

from src.api.EventHandler import OnTextChanged, EventObserver


class GAVIN_MODEL_M3(OnTextChanged, EventObserver):
    
    def __init__(self):
        EventObserver.sub_event(self)
    
    def On_text_input_changed(self,text:str, event):
        print(f"{text} + it worked")
        

class GAVIN_MODEL_M1(OnTextChanged, EventObserver):
    '''
    openai gpt 3.5 and davinci combined models
    '''
    def __init__(self):
        EventObserver.sub_event(self)

    def On_text_input_changed(self, text: str, event):
        print(f"{text} + it worked")


class GAVIN_MODEL_M2(OnTextChanged, EventObserver):
    '''
    openai gpt 4 and davinci combined models
    '''

    def __init__(self):
        EventObserver.sub_event(self)

    def On_text_input_changed(self, text: str, event):
        print(f"{text} + it worked")
