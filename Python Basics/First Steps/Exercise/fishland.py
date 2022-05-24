price_per_kilo_skumria = float(input())
price_per_kilo_caca = float(input())
kilos_palamud = float(input())
kilos_safrid = float(input())
kilos_midi = int(input())

midi = kilos_midi * 7.50
palamud = (price_per_kilo_skumria + price_per_kilo_skumria * 0.60) * \
          kilos_palamud
safrid = (price_per_kilo_caca + price_per_kilo_caca * 0.80) * \
         kilos_safrid
total = midi + palamud+ safrid

print (f'{total:.2f}')