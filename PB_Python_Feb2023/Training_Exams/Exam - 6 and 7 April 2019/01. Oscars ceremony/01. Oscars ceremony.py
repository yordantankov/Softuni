rent = int(input())

statuetki = rent - (rent * 0.30)
ketaring = statuetki -(statuetki * 0.15)
music = ketaring / 2

total = rent + statuetki + ketaring + music

print(f'{total :.2f}')