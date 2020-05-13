def hashcount(string):
    sum=0;
    for i in string:
        sum=sum+(ord(i)-96)
    return str(sum)

def encode_pwd(string):
    rstring=''
    for i in string:
        rstring=rstring+chr(ord(i)+3)
    return str(rstring)

def decode_pwd(string):
    if '\n' in string:
        string=string.replace('\n','')
    rstring=''
    for i in string:
        rstring=rstring+chr(ord(i)-3)
    return str(rstring)
    