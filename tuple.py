tupleFruits = ("apple","banana","cherry") #Tuple
listFruts = ["apple","banana","cherry"] #List
print("original tuple:",tupleFruits)
print("original list:",listFruts)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงเป็นlistแล้วเก็บไว้ในตัวแปรx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าtuple:",tupleFruits)
#เพิ่มค่าในtuple
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple:",tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("เพิ่มค่าtuple:",tupleFruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitVage=tupleFruits+vege
print("join tuple:",fruitVage)
X = range(3,6)
for n in x:
    print("range x:",n)
y = range(3,20,2)    
for m in y:
     print("range y:",m)
#นายธนกฤต ธนาสุวานนท์ เลขที่ 8 6/11