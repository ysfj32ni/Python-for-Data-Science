ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

try:
    ft_list[-1] = "World!"
except IndexError as e:
    print("Error:", e)
try:
    tmp_Tuple = list(ft_tuple)
    tmp_Tuple.remove("toto!")
    ft_tuple = tuple(tmp_Tuple)
    ft_tuple = ft_tuple + ("Morocco!",)
except TypeError as e:
    print("Error:", e)
try:
    ft_set.remove("tutu!")
    ft_set.add("Benguerire!")
except KeyError as e:
    print("Error:", e)

try:
    ft_dict["Hello"] = "1337-BG!"
except KeyError as e:
    print("Error:", e)
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
