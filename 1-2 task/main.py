
import pprint

with open("Recipes.txt", "r", encoding="UTF-8") as f:
    line = f.read().split("\n\n") #удаляем пустые строки из списка
    recipes = dict()
    for smt in line: # проходим циклом по каждому рецепту в списке
        val = [] 
        key = smt.split("\n")[0] # используем первый элемент в качестве ключа
        x = smt.split("\n")[2:] # отделяем все ингридиенты в переменную x
        for lst in x: # циклом создаем отдельный словарь для каждого блюда
             ingr_dict = dict()
             lst = lst.split("|")
             ingr_dict.update({"ingredient_name":lst[0]}) # и наполняем его 
             ingr_dict.update({"quantity":lst[1]})
             ingr_dict.update({"measure":lst[2]})
             val.append(ingr_dict)
        recipes.update({key:val}) # наполняем наш словарь, значением которого является список с словарями
        


def get_shop_list_by_dishes(dishes, person_count):
    needed_ingr_dict = dict()
    for dish in dishes: 
        for recipte in recipes[dish]: # циклом создаем словарь с индридиентами для каждого рецепта
            ingr_dict = dict()
            ingr_dict["measure"] = recipte["measure"] #заполняем 
            if recipte["ingredient_name"] in needed_ingr_dict: #если ингридиент уже есть, увеличиваем его значение
                val = needed_ingr_dict[recipte["ingredient_name"]]["quantity"]
                x = int(recipte["quantity"]) * int(person_count) + val 
                ingr_dict["quantity"] = x
            else:
                ingr_dict["quantity"] = int(recipte["quantity"]) * int(person_count) 
            needed_ingr_dict[recipte["ingredient_name"]] = ingr_dict
    pprint.pprint(needed_ingr_dict)


get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
# pprint.pprint(recipes)
