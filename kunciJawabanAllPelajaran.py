import random
jwb = ["A", "B", "C", "D", "E"]
a = input("Banyak Soal: ")

for x in range(1, (int(a)+1)):
	print("{}. {}".format(x, random.choice(jwb)))