def action_note(a,file,m):
    if(a=='add'):
        write_note(file,m)
    elif(a=='list'):
        list_note(a,file)
    elif(a=='remove'):
        remove_note(file,m)
    else:
        print('Unknown Command called. Use add, remove or list')
        

def write_note(file,m):
    with open(file,'a') as f:
        print(m,file=f)

def list_note(a,file):
    c=1
    with open(file) as f:
        l=[]
        try:
            for line in f:
                l.append(line.strip())
        except FileNotFoundError:
            print('File name does not exist')
    
    if(a=='list'):
        for x in l:
            print(f'{c}. {x}')
            c+=1
    else:
        return l

def remove_note(file,m):
    l=list_note('',file)
    del l[int(m)-1]
    with open(file,'w') as f:
        for x in l:
            print(x,file=f)
    
    
#write_note('hello.txt','kill me')
#list_note('list','hello.txt')
#remove_note('hello.txt',3)
#list_note('list','hello.txt')
