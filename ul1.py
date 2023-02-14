with open('sammud.txt', 'r') as f:
    sammud = [(line) for line in f]

kokku = sum(sammud)
print(f"Nädala kokku sammud: {kokku}")

keskmised = [sammud[i:i+1] for i in range(0, len(sammud), 1)]
keskmised = [sum(p)/len(p) for p in keskmised]
print(f"Päeva keskmised sammud: {keskmised}")

suurim = max(sammud)
suurima_indeks = sammud.index(suurim)
vaikseim = min(sammud)
vaikseima_indeks = sammud.index(vaikseim)
print(f"Kõige suurem sammude arv oli {suurim} päeval {suurima_indeks+1}")
print(f"Kõige väiksem sammude arv oli {vaikseim} päeval {vaikseima_indeks+1}")
