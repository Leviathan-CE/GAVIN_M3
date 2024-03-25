'''
constainst constantants and path variables for managing files 
locations and imports
'''

import os
# NOTE: only runnable code must be places in the root GAVIN
# and all imports should start with src, turn avoid import errors
# as imports are relitive and thus the exicution location matters
# essepcailly ture for making a biuld exicutable

# options if not working
# export vai comand line python path
# export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
# for windows
# set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\

# ---------------------
# use these lines of code if you run into import errors
# they will allow you to run code and import in the same file

# import os, sys
# # Get the root directory path
# root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # Add the root directory to sys.path
# sys.path.append(root_dir)

# ---------------------
'''
ROOT
'''
import sys
print(sys.path)

# note ROOT should always be 'some path\GAVIN\src'
ROOT:str = os.path.abspath('src').replace("\\","/")
#ROOT:str = os.path.dirname(__file__)

# Combine the script directory with 'src'
#src_dir = os.path.join(ROOT, 'src')
print(f"{ROOT} : root")


DATA:str = f"{ROOT}/data"


GUI:str = f"{ROOT}/gui"
GUI_IMGS:str = f"{GUI}/imgs"
GUI_STYLES:str = f"{GUI}/styles"

MD_CONTENT:str = f"{DATA}/markdowntext.md"

