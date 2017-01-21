f = open('pos_tags.txt','r')
line = f.read()
lines = line.split('\n')

pos_dict = {}
for line in lines:
    key_val = line.split('\t')
    pos_dict[key_val[0]] = key_val[1]

