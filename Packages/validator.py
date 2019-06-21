import re
def phonenumvalid(num):
    pattern = '^[06789][0-9]{9}$|^[+91][6-9][0-9]{9}$'
    if re.match(pattern,str(num)):
        return True
    return False
phonenumvalid(9565033528)

import re
def emailvalid(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,13}[@][a-z0-9]{3,18}[.][a-z]{2,4}$|^[0-9a-z][0-9a-z_.]{4,13}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,str(email)):
        return True
    return False
emailvalid("re_12345@gmail.com")