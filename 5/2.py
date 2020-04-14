with open('text2.txt', 'r') as f:
    content = f.readlines()
    print('Total  :', len(content), 'lines')
    print('------')
    for i in range(len(content)):
        print('Line', i+1, ':', len(content[i].split()), 'words')