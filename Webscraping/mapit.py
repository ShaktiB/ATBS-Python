#import pandas as pd
import webbrowser, sys
import pyperclip as clip

inp = sys.argv # THis will break the command like input into a list

if len(inp) > 1:
    adrs = ' '.join(inp[1:])
else:
    adrs = clip.paste() # Returns the last thing copied in you clipboard

webbrowser.open('https://www.google.ca/maps/place/' + adrs)
