class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def double_values(self, valid_card):
        list_double = []
        list_single = []
        if len(valid_card) % 2 == 0:
            for i, value in enumerate(valid_card):
                i += 1
                if i % 2 == 0:
                    list_single.append(value)
                else:
                    list_double.append(value)
        else:
            for i, value in enumerate(valid_card):
                i += 1
                if i % 2 == 0:
                    list_double.append(value)
                else:
                    list_single.append(value)
        list_single = [int(x) for x in list_single]
        list_double = [int(x) * 2 if int(x) * 2 < 9 else (int(x) * 2) - 9 for x in list_double]
        return list_single, list_double

    def valid(self):
        _temp = self.card_num
        valid_card = self.card_num.replace(" ", "")
        if len(valid_card) <= 1 or not valid_card.isnumeric():
            return False

        list_double, list_single = self.double_values(valid_card)

        return (sum(list_single) + sum(list_double)) % 10 == 0
        
