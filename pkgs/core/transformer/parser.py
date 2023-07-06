def parse_includes(exp: str):
    o = {}
    p = []
    inArray = False
    parsed_obj = []
    final = {}

    length = len(exp)
    i = 0
    while (i < length):
        last_char = None if i < 0 else ord(exp[i - 1])
        ch = ord(exp[i])
        if (ch == 91):
            o['name'] = ''.join(p)
            o['args'] = []
            p = []
            inArray = True
        elif (inArray and ch == 44):
            o['args'].append(''.join(p))
            p = [];
        elif (ch == 93):
            o['args'].append(''.join(p))
            parsed_obj.append(o)
            o = {}
            p = []
            inArray = False
        elif (last_char != 93 and ch == 44):
            o['name'] = ''.join(p)
            parsed_obj.append(o)
            o = {}
            p = []
        elif (ch != 93 and length - i == 1):
            p.append(chr(ch))
            o['name'] = ''.join(p)
            parsed_obj.append(o)
        elif (ch != 44):
            p.append(chr(ch))

        i+=1

        for p in parsed_obj:
            final[p['name']] = p.get('args')

    return final