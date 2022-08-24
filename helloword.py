from logging import raiseExceptions


def ini(nama):
    if nama == 'Hello Words!':
        lanjutan(nama)
    else: raise SyntaxError
    
    
def lanjutan(nama):
    if len(nama) < 2 :
        raise SyntaxError
    else: rakit(nama)
    
    
def rakit(nama):
    nama_asli = []
    
    for j in nama:
        nama_asli.append(j)
    printer(nama_asli)
        
        
def printer(nama):
    namas = ''.join(nama)
    print(namas)




nama = 'Hello Words!'
ini(nama)