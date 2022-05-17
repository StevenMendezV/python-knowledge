def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "David", "lastname": "Soler"},
        {"firstname": "Steven", "lastname": "Ruiz"},
        {"firstname": "Esteban", "lastname": "Murcia"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "interger_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

# IMPRESION DEL DICCIONARIO DE LISTAS /////////////////
    # for key, value in super_dict.items():
    #     print(f'{key} tiene como conjunto {value}') 

# IMPRESION DE LA LISTA DE DICCIONARIOS ////////////////////
    for i in super_list:
        print(f'{i["firstname"]} tiene de apellido {i["lastname"]}')


if __name__ == "__main__":
    run()