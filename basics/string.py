chai  = "Lemon Chai"
print(chai)

print(chai[0])
print(chai[-1])

slice_chai = chai[0:6]
print(slice_chai)

numList = '0123456789'

print(numList[0:9:2]) # third param hop
print(numList[:])
print(numList[:-4])
print(numList[2:])

print(chai.upper())
print(chai.lower())
strips = "    AMOGH     "
print(strips)
print(strips.strip())

print(chai.replace("Lemon","Ginger"))
chai = 'Lemon, Ginger, Masala, Mint'

print(chai.split(", "))

chai = "Masalala chai"
print(chai.find("chai")) #if found return index else -1
print(chai.count('la')) 

quantity =2
order = "I ordered {} cups of {} "
print(order.format(quantity,chai))

chai_variety = ["lemon","masala","ginger"]

print(" ".join(chai_variety)) #list to string
print(len(chai))

for letter in chai:
    print(letter)

chai = "He said, \"Masala chai is awesome\" "
print(chai)

chai = "Masala\nchai"
print(chai)
chai =r"Masala\nchai" #raw string
print(chai)

print('\\n' in chai)


