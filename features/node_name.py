
def HandleNodeName(name):
    if ((name == None) | (name == '')):
        return name
    elif ((name[0] == '_') | (name.isalpha())):
        return name
    else:
        for i in range(0, len(name)):
            if (not name[0:i+1].isalpha()):
                return name[0:i]