with open('sammud.txt', 'r') as f:
    sammud = [int(line) for line in f]

kokku = sum(sammud)
print(f"Nädala kokku sammud: {kokku}")

keskmised = [sum(sammud[i:i+1])/1 for i in range(len(sammud))]
print(f"Päeva keskmised sammud: {keskmised}")

suurim = max(sammud)
suurima_indeks = sammud.index(suurim) + 1
vaikseim = min(sammud)
vaikseima_indeks = sammud.index(vaikseim) + 1
print(f"Kõige suurem sammude arv oli {suurim} päeval {suurima_indeks}")
print(f"Kõige väiksem sammude arv oli {vaikseim} päeval {vaikseima_indeks}")
