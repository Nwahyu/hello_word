import gambar
import random




def mainin(player,bot):
    if player == 'g' or player == 'k' or player == 'b' :
        if bot == 'g' and player == 'k' or bot == 'k' and player == 'b' or bot == 'b' and player == 'g' :
            gambar.botwin()
        elif player == bot :
            print('draw')
        else: gambar.playerwin()
    else: masukan()
        
        
def masukan():
    player = str(input('''
                       masukan pilihan :
                       g = Gunting
                       k = Kertas
                       b = Batu
                        -> ''')).lower()
    bot = random.choice(['g','k','b'])
    
    mainin(player,bot)
    
masukan()