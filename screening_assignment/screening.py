def screening():
    x = 'placement'
    y = 'screening'
    with open('example.txt','r') as f:
        replacement = f.read().replace(x,y)
    with open('example.txt', 'w') as f:
        f.write(replacement)

screening()