my_dict={"Sasha":1999, "Ilya":2004, "Masha":2000, "Nastya":2019}
print(my_dict)
print(my_dict["Sasha"])
print(my_dict.get("Petya"))
my_dict.update({"Oksana":1988,"Misha":2020})
lie=my_dict.pop("Masha")
print(lie)
print(my_dict)
my_set={"Weather",1,2.5,1,(0,3,4,),"Weather",2.5}
print(my_set)
my_set.add("Magic")
my_set.add(52)
my_set.remove(2.5)
print(my_set)