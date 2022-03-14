class Allergies:
    death = [] 

    def __init__(self, score):
        self.s = score

    def allergic_to(self, item):
        self.i = item
        # allergens = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16, "chocolate": 32, "pollen": 64, "cats": 128 }
        allergens = {"cats": 128, "pollen": 64, "chocolate": 32, "tomatoes": 16, "strawberries": 8, "shellfish": 4, "peanuts": 2, "eggs": 1}
        all_key = [] 
        all_val = []
        death = []
        counter = self.s
        for n, (key, value) in enumerate(allergens.items()): 
            if counter >= value:
                counter -= value
                death.append(key)
            all_key.append(key)
            all_val.append(value)
        print(death)
        Allergies.death = death
        for i in self.i:
            if not self.i in death: return False 
        return True
        # return self.i in death



    @property
    def lst(self):
        print(Allergies.death)
        return Allergies.death


def main():
    # print(Allergies(80).allergic_to("chocolate"))
    print(Allergies(3).lst(["eggs", "peanuts"]))

if __name__ == '__main__':
    main()