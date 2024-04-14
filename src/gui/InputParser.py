"""_summary_
functions for parsing text into persepctive blocks of organized text while perserving the order.
"""

def get_text_blocks(text:str ) -> list[dict[str, str]]:
        '''
        parses the text into dict reprasentation for text and code
        '''
        code_blocks: list = _parse_text(text=text)
        dicts_txt_blocks: list = []
        if len(code_blocks) != 0:

            prev_end = 0
            for block in code_blocks: 
                start, end = block
                if start > prev_end:
                    # Add a text block if there's text before the code block
                    dicts_txt_blocks.append(
                        {"type": "text", "content": text[prev_end:start]})
                # Add the code block
                dicts_txt_blocks.append(
                    {"type": "code", "content": text[start:end]})
                prev_end = end

            # if thier still stuff at the end thats not code
            if len(text.split("```")) > len(dicts_txt_blocks):
                if len(text[prev_end:]) > 0:
                    dicts_txt_blocks.append(dicts_txt_blocks.append(
                        {"type": "text", "content": text[prev_end:]}))

        else:
            dicts_txt_blocks.append({"type": "text", "content": text})
        return dicts_txt_blocks

def _parse_text(text:str) -> list:
        '''
        parses the text to find locations of markdown code blocks
        '''
        code_blocks_indices: list = []

        in_code = False
        start = 0
        for i, char in enumerate(text):
            if not in_code and text[i:i+3] in ["```"]:
                in_code = True
                start = i  # Skip the ``` characters
            elif in_code and text[i:i+3] in ["```"]:
                in_code = False
                code_blocks_indices.append((start, i+3))

        # If the text ends with an open code block, add it to the list
        if in_code:
            code_blocks_indices.append((start, len(text)))

        return code_blocks_indices