def daorne(filePath):
    try:
        with open(f'{filePath}.txt', 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
if daorne(max) == False:
    p = open('max.txt','w')
    p.write('0')
    p.close()
