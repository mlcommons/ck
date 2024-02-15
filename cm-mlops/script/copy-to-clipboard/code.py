import os
import pyperclip as pc

text = os.environ.get('CM_COPY_TO_CLIPBOARD_TEXT', '')

add_quotes = os.environ.get('CM_COPY_TO_CLIPBOARD_TEXT_ADD_QUOTES', '') in [True,'True','yes']

if add_quotes:
    text = '"' + text + '"'

pc.copy(text)
