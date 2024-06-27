survival_data_male = [
    100000, 99919, 99863, 99827, 99805, 99791, 99781, 99772, 99763, 99754,
    99745, 99735, 99725, 99714, 99701, 99684, 99662, 99632, 99594, 99548,
    99495, 99436, 99374, 99308, 99241, 99173, 99107, 99042, 98979, 98916,
    98850, 98783, 98715, 98646, 98575, 98502, 98426, 98344, 98256, 98159,
    98052, 97936, 97810, 97673, 97525, 97366, 97194, 97005, 96798, 96569,
    96319, 96045, 95746, 95423, 95076, 94704, 94305, 93873, 93403, 92893,
    92339, 91736, 91079, 90364, 89589, 88751, 87850, 86884, 85850, 84741,
    83548, 82258, 80858, 79333, 77667, 75845, 73845, 71646, 69224, 66557,
    63631, 60445, 57016, 53366, 49505, 45457, 41286, 37047, 32799, 28609,
    24545, 20677, 17068, 13776, 10844, 8304.0, 6166.6, 4426.3, 3059.5, 2028.2,
    1283.7, 771.73, 438.26, 233.66, 116.15, 53.420, 22.543, 8.6471, 2.9838, 0.9156
]

death_data_male = [
    81, 56, 36, 22, 14, 10, 9, 9, 9, 9,
    10, 10, 11, 13, 17, 23, 30, 38, 46, 53,
    59, 63, 66, 68, 67, 66, 64, 63, 63, 65,
    67, 68, 69, 71, 73, 76, 82, 89, 97, 107,
    116, 126, 137, 147, 159, 172, 189, 208, 228, 250,
    275, 299, 323, 347, 372, 400, 432, 469, 510, 555,
    603, 657, 715, 775, 838, 901, 966, 1034, 1109, 1193,
    1290, 1400, 1525, 1665, 1822, 2000, 2199, 2422, 2667, 2926,
    3185, 3429, 3650, 3861, 4048, 4171, 4240, 4248, 4190, 4064,
    3868, 3609, 3292, 2931, 2540.4, 2137.4, 1740.3, 1366.7, 1031.3, 744.6,
    511.94, 333.46, 204.61, 117.51, 62.726, 30.877, 13.8961, 5.6633, 2.0682, 0.9156
]

survival_data_female = [
    100000, 99922, 99869, 99836, 99817, 99806, 99798, 99790, 99782, 99775,
    99768, 99761, 99754, 99746, 99736, 99724, 99710, 99694, 99675, 99655,
    99632, 99607, 99581, 99554, 99526, 99497, 99468, 99438, 99408, 99376,
    99342, 99305, 99266, 99222, 99173, 99120, 99061, 98997, 98927, 98850,
    98768, 98681, 98590, 98492, 98390, 98279, 98160, 98027, 97880, 97717,
    97539, 97347, 97141, 96923, 96689, 96441, 96181, 95908, 95620, 95317,
    94995, 94650, 94282, 93892, 93482, 93054, 92604, 92127, 91616, 91064,
    90462, 89802, 89071, 88258, 87353, 86346, 85233, 84004, 82640, 81120,
    79415, 77498, 75345, 72938, 70269, 67283, 63997, 60415, 56555, 52440,
    48108, 43607, 38995, 34344, 29733, 25250, 20983, 17016, 13425, 10269,
    7586.6, 5389.6, 3663.8, 2370.1, 1450.0, 833.14, 446.05, 220.55, 99.723,
    40.772, 14.884, 4.7833, 1.3318, 0.3155
]

death_data_female = [
    78, 53, 33, 19, 11, 8, 8, 8, 7, 7, 7, 7, 8, 10, 12, 14, 16, 19, 21, 23, 25,
    26, 27, 28, 29, 29, 30, 31, 32, 34, 37, 40, 44, 49, 54, 58, 64, 70, 76, 82,
    87, 92, 98, 102, 110, 120, 133, 147, 163, 178, 192, 205, 219, 234, 248, 260,
    273, 288, 303, 322, 345, 368, 390, 409, 428, 450, 477, 510, 552, 602, 660,
    731, 812, 906, 1006, 1113, 1230, 1363, 1521, 1704, 1917, 2153, 2407, 2669,
    2986, 3287, 3581, 3861, 4114, 4332, 4502, 4612, 4651, 4610, 4483, 4268, 3967,
    3591, 3156, 2682.5, 2197.0, 1725.8, 1293.7, 920.1, 616.89, 387.10, 225.50,
    120.830, 58.951, 25.888, 10.1008, 3.4515, 1.0162, 0.3155
]

while True:
    input_line = input("性別を入力してください(男性:1,女性:2)")
    try:
        gender = int(input_line)
        if gender == 1 or gender == 2:
            break
    except ValueError:
        continue

if gender == 1:
    d = death_data_male
    l = survival_data_male
    max_age = 109
    pgender = "男性"
elif gender == 2:
    d = death_data_female
    l = survival_data_female
    max_age = 113
    pgender = "女性"

while True:
    input_line = input("保険金を入力してください")
    try:
        B = int(input_line)
        break
    except ValueError:
        continue

while True:
    input_line = input("年齢を入力してください")
    try:
        x = int(input_line)
        if 0 <= x <= max_age:
            break
    except ValueError:
        continue

while True:
    input_line = input("保険期間を入力してください")
    try:
        n = int(input_line)
        break
    except ValueError:
        continue

while True:
    input_line = input("利率を入力してください")
    try:
        rate = float(input_line)
        break
    except ValueError:
        continue

while True:
    input_line = input("保険料を入力してください")
    try:
        P = int(input_line)
        break
    except ValueError:
        continue    

if x + n > max_age:
    n = max_age - x

future_expence = 0
future_income = 0


v = 1 / (1 + rate)

print(f"性別:{pgender} 保険金：{B:,}円 保険料：{P:,}円 年齢：{x}歳 保険期間：{n}年 利率：{rate:.6f}")

P = P / B

y = []
for t in range(n):
    d_sum = 0
    l_sum = 0
    for i in range(t,n):
        d_sum += v ** (i + 1/2) * d[x + t + i]
        l_sum += v ** i * l[x + t + i]
    future_expence = d_sum
    funter_income = P * l_sum
    V = (future_expence - future_income) / l[x + t]
    print(f"{t=} {V=:,.5f}")
    y.append(V)

x = list(range(n))

import matplotlib.pyplot as plt

fig,ax = plt.subplots()

ax.set_title('Reserve')
ax.set_xlabel('t')
ax.set_ylabel('V')
ax.plot(x,y)

plt.show()
