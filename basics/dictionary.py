chai_type = {"Masala":"Spicy","Ginger":"Zesty","Mint":"Healty"}
print(chai_type)
print(chai_type["Masala"]) #if wrong key then error
print(chai_type.get("Masala")) #if wrong key then no error

chai_type["Mint"] = "Sour"
print(chai_type)

for chai in chai_type:
    print(chai,"chai is",chai_type[chai])

for key,value in chai_type.items():
    print(key,value)

if "Masala" in chai_type:
    print("i have masala cai")

print(len(chai_type))

chai_type["Green"] = "Fresh"
print(chai_type)

chai_type.pop("Mint")
print(chai_type)

chai_type.popitem()
chai_type["Mint"]='Sour'
print(chai_type)

del chai_type['Masala']
print(chai_type)

chai_type_copy = chai_type.copy() #same as list

# nested dict
tea_shop= {
    "chai":{"Masala":"spicy","ginger":"zesty"},
    "worker":{ "raju":100,"ramu":200}
}

print(tea_shop)
print(tea_shop["chai"]["Masala"])
print(tea_shop["worker"]["raju"])

squared_num = {x:x**2 for x in range(1,6)}

print(squared_num)
squared_num.clear()
print(squared_num)

keys = ["masala",'mint']
default_value ="Top"

new_dict = dict.fromkeys(keys,default_value)

print(new_dict)

