import os
import pathlib
import sys


#PIGGIOGGIO <3
#UNSTABLE(CAN KILL A FILE mangiandosi il titolo o.o)
def redux(directory,x): #Rimuovi i primi x caratteri
    for filename in os.listdir(directory): #per ogni file name in LISTA 
        if filename == sys.argv[0]:
            continue
        if len(filename) - x >= 5 :
        #TEST
        #  48 (x.mp3)     48
        #  len(filename) -x  >= 5 ok             
            file_old_name = os.path.join(directory, filename)
            file_new_name = os.path.join(directory, filename[x:])
            os.rename(file_old_name, file_new_name)
        else :
            print("You can't cut ",filename," too much!Skip!")



def resolve_space(directory): 
    for filename in os.listdir(directory): #per ogni file name in LISTA 
        file_old_name = os.path.join(directory, filename)
        file_new_name = os.path.join(directory, filename.replace(" ", "_"))
        if file_old_name != file_new_name:
            os.rename(file_old_name, file_new_name)
    print("fixed_space")

def main():
    
    directory = pathlib.Path().parent.resolve() 
    print("Siamo in ",directory) #stampa questo pathRIN
    
    i=0
    if len(sys.argv) < 2:
        print("ERRORE: Argomenti mancanti o più di 2!(Scrivi space per eliminare il primo spazio)")
        sys.exit()
    print("Argomento:",sys.argv[1])
    if sys.argv[1] == 'space':
        resolve_space(directory)
        prfx="_"
    else:
        prfx=sys.argv[1]
    n=len(os.listdir(directory))
    for filename in os.listdir(directory): #per ogni file name in LISTA 
        file_old_name = os.path.join(directory, filename)
        file_new_name = os.path.join(directory, filename.removeprefix(prfx))
        if file_old_name != file_new_name:
            os.rename(file_old_name, file_new_name)
            print("nome vecchio file=",file_old_name,"\nnome nuovo file=",file_new_name)
        else:
            i+=1
            print("nome vecchio file=",file_old_name,"\nnome nuovo file=",file_new_name)    
    print("File non modificati:",i)    
    print("File modificati:",n-i)   

if __name__ == "__main__":
    main()
