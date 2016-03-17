def body_mass_index(weight, height):
    return weight / height ** 2

def shape_of(weight, height):
    if body_mass_index(weight, height) <= 15:
        return 'тежко недохранване'
    elif body_mass_index(weight, height) <=16:
        return 'средно недохранване'
    elif body_mass_index(weight, height) <= 18.5:
        return 'леко недохранване'
    elif body_mass_index(weight, height) <=25:
        return 'нормално тегло'
    elif body_mass_index(weight, height) <=30:
        return 'наднормено тегло'
    elif body_mass_index(weight, height) <=35:
        return 'затлъстяване I степен'
    elif body_mass_index(weight, height) <=40:
        return 'затлъстяване II степен'
    else:
        return 'затлъстяване III степен'
