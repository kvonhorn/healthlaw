# Keywords to search a law for

import re

keywords = '(?i)disabl(ed|ity)|health|primary care|(insurance|prominent) carrier'

# Returns True if the title_or_text contains a healthcare related keyword, False if not
def isInterestingLaw(title_or_text):
    return None != re.search(keywords, title_or_text)

