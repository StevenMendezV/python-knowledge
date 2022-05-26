class voting_booth:

    def __init__(self, id, country, permitted_areas):
        self.__id = id 
        self.__country = country
        self.__permitted_areas = permitted_areas
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__permitted_areas:
            self.__region = region

        else:
            raise ValueError(f"La región {region} no pertenece a {self.__permitted_areas}")


if __name__ == "__main__":

    voting = voting_booth("123", "Colombia", ("Quindio", "Amazonas", "Medellin", "Choco"))
    # vol = voting_booth("123", "Colombia", ("Quindio", "Amazonas", "Medellin", "Choco"))
    print(voting.region)
    voting.region = "jalisco"
    # print(voting.region)




    