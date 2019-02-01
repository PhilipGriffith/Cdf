import numpy.random as npr

class Chemin():

    def __init__(self, num_decks=6):
        
        self.num_decks = num_decks
        self.shoe = []
        
        self._build_shoe()

        

    def _build_shoe(self):

        for i in range(self.num_decks):
            standard_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]*4
            self.shoe.extend(standard_deck)

    def _deal(self, num=6):

        return npr.choice(self.shoe, num, replace=False)

    def play(self):

        hand = self._deal()
        banker_deal = hand[:3]
        punter_deal = hand[3:]
        punter_card = punter_deal[-1]

        banker1 = int(str(banker_deal[:2].sum())[-1])
        punter1 = int(str(punter_deal[:2].sum())[-1])

        banker2 = int(str(banker1 + banker_deal[-1])[-1])
        punter2 = int(str(punter1 + punter_card)[-1])

        print('Banker:', banker_deal)
        print('Punter:', punter_deal)

        if banker1 > 7 or punter1 > 7:
            self.result(banker1, punter1)
        else:
            if punter1 < 5 or (punter1 == 5 and npr.randint(0, 2)):
                print('Player hits')
                punter1 = punter2
                if banker1 < 3:
                    banker1 = banker2
                    print('Banker hits')
                elif banker1 == 3 and (punter_card < 8 or (punter_card == 9 and npr.randint(0, 2))):
                    banker1 = banker2
                    print('Banker hits')
                elif banker1 == 4 and (1 < punter_card < 8):
                    banker1 = banker2
                    print('Banker hits')
                elif banker1 == 5 and ((4 < punter_card < 8) or (punter_card == 4 and npr.randint(0, 2))):
                    banker1 = banker2
                    print('Banker hits')
                elif banker1 == 6 and (5 < punter_card < 8):
                    banker1 = banker2
                    print('Banker hits')
            else:
                print('Player stands')
                if banker1 < 6 or (banker1 == 6 and npr.randint(0, 2)):
                    banker1 = banker2
                    print('Banker hits')

            self.result(banker1, punter1)

    @staticmethod
    def result(banker, punter):

        result = 'Banker: {} vs Punter: {}\n{{}} wins'.format(banker, punter)
        if banker > punter:
            print(result.format('Banker'))
        elif banker < punter:
            print(result.format('Punter'))
        else:
            print(result.format('Nobody'))


c = Chemin()
c.play()
