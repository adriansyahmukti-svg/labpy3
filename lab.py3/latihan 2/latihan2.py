modal = 10000000
total_laba = 0

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <=4:
        laba = modal * 0.01
    elif bulan <=7:
        laba = modal * 0.05
    else:
        laba = modal * 0.03

    total_laba += laba
    print(f"laba bulan ke- {bulan} sebesar:{int(laba)}")
    print(f"total laba adalah: {int(total_laba)}")



