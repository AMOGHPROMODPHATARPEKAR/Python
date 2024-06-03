chai_variety = ["lemon","masala","ginger"]

print(chai_variety)
print(chai_variety[0])
print(chai_variety[:2])

chai_variety[2] = "mint"
print(chai_variety)

chai_variety[1:2]=["lemon"] #bcz when sliced it is coverted nto array so expects array
print(chai_variety)

chai_variety[1:3] = ["green","masala"] 
print(chai_variety)
print(chai_variety[1:1])

chai_variety[1:1] = ["test","test"] #like splice
print(chai_variety)

chai_variety[1:3] = [] #delet or insert nothing
print(chai_variety)

for chai in chai_variety:
    print(chai,end="-")

if 'mint' in chai_variety:
    print("I have lemon tea")
else:
    chai_variety.append('mint')#add at end

print('\n')
print(chai_variety)

print(chai_variety.pop())#remove last and give
chai_variety.remove('green') #remove ele but not echos

print(chai_variety)

chai_variety.insert(1,"green")
print(chai_variety)

chai_copy = chai_variety #create a refrence so both will change
chai_variety.pop()
print(chai_copy)
print(chai_variety)
chai_copy.append("Mint")
print(chai_copy)
print(chai_variety)
chai_copy = chai_variety.copy() #makes a copy and assign
chai_copy.append("masala")
print(chai_copy)
print(chai_variety)


#list comprihension

square_num = [x**2 for x in range(10)]

print(square_num)

x=[1,2,"aofj"]
print(x)

