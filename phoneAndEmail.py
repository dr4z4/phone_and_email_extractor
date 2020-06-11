#! python3
# This program is modified program from https://automatetheboringstuff.com.
# to check functionality of your regex, you can use https://regex101.com/
# before running this program press ctrl+A, ctrl+C on document from which you want to extract

import re, pyperclip

# Create a regex for phone numbers
# phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
# ((\d{3}|\(\d{3}\))?                # area code (optional)
# (\s|-|\.)?                        # fist separator (optional) 
# (\d{3})                           # first 3 digits
# (\s|-|\.)                         # separator
# (\d{4})                           # last 4 digits
# (\s*(ext|x|ext.)\s*(\d{2,5}))?)   # extension (optional)
# ''', re.VERBOSE)

# option for czech numbers:
phoneRegex = re.compile(r'''
# +420 475 858 012, (+420) 475 858 012,  +420475858012
((\+\d{3}|\(\+\d{3}\))            # area code 
(\s*\d{3}){3})                    # space (optional) and 3 digits - 3x                       
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_2thing@some.+_2thing.com 
[a-zA-Z0-9_.+]+         # name part
@                       # @ symbol
[a-zA-Z0-9_.+]+         # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results) # now you can paste the result into your document/email etc.
# print(results)
