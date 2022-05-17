# PRIMER EJEMPLO DE DICCIONARIOS //////////////

# def run():
#     mi_dict = {
#         "llave1": 1,
#         "llave2": 2,
#         "llave3": 3,   
#     }
#     print(mi_dict["llave1"])
#     print(mi_dict["llave2"])
#     print(mi_dict["llave3"])


# if __name__ == "__main__":
#     run()

# SEGUNDO EJEMPLO DE DICCIONARIOS //////////////

# def run():
#     mi_dict = {
#         "llave1": 1,
#         "llave2": 2,
#         "llave3": 3,   
#     }

#     population_countries = {
#         "Argentina": 44938712,
#         "Brasil": 210147125,
#         "Colombia": 50372424
#     }

#     print(population_countries["Argentina"])



# if __name__ == "__main__":
#     run()

# TERCER EJEMPLO DE DICCIONARIOS TRAYENDO KEYS //////////////

# def run():
#     mi_dict = {
#         "llave1": 1,
#         "llave2": 2,
#         "llave3": 3,   
#     }

#     population_countries = {
#         "Argentina": 44938712,
#         "Brasil": 210147125,
#         "Colombia": 50372424
#     }

#     for country in population_countries.keys():
#         print(country)



# if __name__ == "__main__":
#     run()

# CUARTO EJEMPLO DE DICCIONARIOS TRAYENDO VALUES //////////////

# def run():
#     mi_dict = {
#         "llave1": 1,
#         "llave2": 2,
#         "llave3": 3,   
#     }

#     population_countries = {
#         "Argentina": 44938712,
#         "Brasil": 210147125,
#         "Colombia": 50372424
#     }

#     for country in population_countries.values():
#         print(country)



# if __name__ == "__main__":
#     run()

# QUINTO EJEMPLO DE DICCIONARIOS TRAYENDO KEYS Y VALUES //////////////

def run():
    mi_dict = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,   
    }

    population_countries = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    for country, population in population_countries.items():
        print("El país " + country + " tiene una población de " + str(population) + " habitantes.")



if __name__ == "__main__":
    run()
    