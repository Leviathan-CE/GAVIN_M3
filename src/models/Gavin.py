
from src.api.Exceptions import ApiKeyNotFoundException
from src.api.EventHandler import OnTextChanged,EventHandlerPushMessages
from src.data.profiles import (
            ROLE,
            TOKEN_MULTIPLYER,
            TOKEN_LIMIT,
            USER_NAME,
            OPENAI_KEY_NAME
)

MODEL_FOUNDATION = "gpt-3.5"
MODEL_GAVIN_MI = "GAVIN_M1"


class FoundationModel(OnTextChanged):
    
    active_model = MODEL_FOUNDATION
    def __init__(self):
       self.eventhandler = EventHandlerPushMessages()
       self.eventhandler.sub_event(listeners=self)
    
    def On_text_input_changed(self,text:str, event):
        print(f"{text} + it worked")
    
    def invoke_on_push_message(self, text: str, event):
        self.eventhandler.invoke_on_push_message(text, event)

    def text_to_prompt(self,text) ->dict:
        return {"role": "user", "content": text}


class GavinMarkI(FoundationModel):
    
    MODEL = "GAVIN_M1"
    def __init__(self):
        import openai
        import os
        super().__init__()
        try:
             openai.api_key = os.getenv(OPENAI_KEY_NAME)
             print(openai.api_key)

        except:
            print("eorors alll the errors") 
            raise ApiKeyNotFoundException("open ai key not found")
        
        if openai.api_key == None:
                print("api not found")
                raise ApiKeyNotFoundException
            
            
    def On_text_input_changed(self, text: str, event):
        print(type(self))
        if self.active_model == self.MODEL and not isinstance(event,GavinMarkI):
            self.invoke_on_push_message(text, event)
            response = self.generate(text=text)
            from src.data.DataBase import DataBase
            db = DataBase()
            db.insert(self.MODEL,response)
            db.close()
            self.invoke_on_push_message(response, self)

    
    
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
        max_tokens= TOKEN_LIMIT*TOKEN_MULTIPLYER, #max 4096
        user=USER_NAME,
        frequency_penalty= .1, #.2
        presence_penalty=.1) #.2
        #--------consumed------------------
        print(response)

        #format gpt response
        response = {"role": "assistant", "content":response.choices[0].message.content} # type: ignore

        #return only the content
        return response["content"]