
import math

#level configuration: little_one, medium_one, bombar    r, big_one

def create_list_level(max_level):
    list_type_enemies = ["little", "lit_med", "medium", "big", "huge"]
    list_level = []
    for i in range(max_level):
        list_nb_ennemies = []
        level = []

        list_nb_ennemies.append(30 + math.floor(i*1))
        list_nb_ennemies.append(5  + 2*i)
        list_nb_ennemies.append(2*i)
        list_nb_ennemies.append(round(2*1.5))
        list_nb_ennemies.append(2*math.floor(i/5))

        if i < 5:
            list_nb_ennemies[2],list_nb_ennemies[3] , list_nb_ennemies[4] = 0, 0, 0
        for j in range(5):
            tmp = [list_type_enemies[j]]*list_nb_ennemies[j]
            level += tmp
        list_level.append(level)
    return list_level
