def decodeHuff(root, s):
    d = ''
    cur = root
    for i in s:
        if i == '1':
            cur = cur.right
        elif i == '0':
            cur = cur.left
        if cur.right == None and cur.right == None:
            d+=cur.data
            cur = root
    print(d)
            