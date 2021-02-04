def pal(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

