import sys
import note

if len(sys.argv)>1:
    if(sys.argv[1]=='list'):
        note.list_note(sys.argv[1],sys.argv[2])
    elif(sys.argv[1] == 'add'):
        note.write_note(sys.argv[2],sys.argv[3])
    elif(sys.argv[1] == 'remove'):
        note.remove_note(sys.argv[2],sys.argv[3])
    else:
        raise ValueError
else:
    print('Bad Command Line')
    print('Note.py expects at least 1 argument.')
    
    

