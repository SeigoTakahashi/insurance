rate = float(input("利率を入力してください"))
origin = float(input("元本を入力してください"))

print('年','単利計算','複利計算','現価計算','死亡率','生存率','生命年金')
for i in range(1,31):
    die_rate = input("死亡率を入力してください")
    if die_rate == '':
        break
    die_rate = float(die_rate)
    self_rate = 1 - die_rate
    tanri = origin * (1 + i * rate)
    fukuri = origin * (1 + rate) ** i
    genkakeisan = origin / (1 + rate) ** i
    seimeinenkingenka = genkakeisan * self_rate
    print(i,end='|')
    print(round(tanri),end='|')
    print(round(fukuri),end='|')
    print(round(genkakeisan),end='|')
    print(die_rate,end='|')
    print(self_rate,end='|')
    print(round(seimeinenkingenka),end='|')
    print()