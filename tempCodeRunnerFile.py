name = ['sakib' , 'Mushfiq', 'Mashrafi']
age = [35, 37 , 38]
player = []
for nam in name:
    print("the player names : ", nam)
    for ages in age:
        print(nam, ages)
        player.append([nam, ages])
print(player)
