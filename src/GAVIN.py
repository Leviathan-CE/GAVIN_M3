

from src.api.EventHandler import OnTextChanged, EventObserver
from src.data.profiles import (
            ROLE,
            TOKEN_MULTIPLYER,
            TOKEN_LIMIT,
            USER_NAME
)

MODEL_FOUNDATION = "gpt-3.5"
MODEL_GAVIN_MI = "GAVIN_M1"


class FoundationModel(OnTextChanged):
    
    active_model = MODEL_FOUNDATION
    def __init__(self):
       self.eventhandler = EventObserver()
       self.eventhandler.sub_event(listeners=self)
    
    def On_text_input_changed(self,text:str, event):
        print(f"{text} + it worked")
    
    def invoke_On_text_loaded(self, text: str, event):
        self.eventhandler.invoke_On_text_loaded(text, event)

    def text_to_prompt(self,text) ->dict:
        return {"role": "user", "content": text}


class GavinMarkI(FoundationModel):
    
    MODEL = "GAVIN_M1"
    def __init__(self):
        import openai
        import os
        super().__init__()
        try:
             openai.api_key = os.getenv("OPEN_AI_KEY")
        except:
            print("OPEN_AI_KEY  Not Found")
        
        try:
            openai.organization = os.getenv("OPENAI_ORG")
        except:
            print("ORGANIZATION Not Found")
    
    def On_text_input_changed(self, text: str, event):
        print(type(self))
        if self.active_model == self.MODEL:
            self.invoke_On_text_loaded(text, event)
            self.invoke_On_text_loaded(f"{self.generate(text=text)}",self)

    
    
    def generate(self,text:str) -> str:
        import openai
        '''
        base model genration, to get response from GAVIN as text
        '''
        #tansform text to prompt
        pmt = self.text_to_prompt(text)         

        #attach it to the prompt
        pmt2 = {'role': "system", 'content': f"your role: {ROLE}"}        
        
        #generate response with context history
        #---------the chat-----------------
        response = openai.chat.completions.create( # type: ignore
        model="gpt-3.5-turbo",
        messages = [pmt2,pmt],
        #top_p= 1,  
        temperature=.45, #.6
        max_tokens= TOKEN_LIMIT*TOKEN_MULTIPLYER,
        user=USER_NAME,
        frequency_penalty= .1, #.2
        presence_penalty=.1) #.2
        #--------consumed------------------
        print(response)

        #format gpt response
        response = {"role": "assistant", "content":response.choices[0].message.content} # type: ignore
       
        #return only the content
        return response["content"]