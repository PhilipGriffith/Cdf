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
        print('Banker:', banker_deal)
        print('Punter:', punter_deal)

        banker = int(str(banker_deal[:2].sum())[-1])
        punter = int(str(punter_deal[:2].sum())[-1])

        banker2 += banker_deal[-1]
        banker2 = int(str(banker2)[-1])
        punter2 += punter_deal[-1]
        punter2 = int(str(punter2)[-1])

        print('Initial Banker hand:', banker)
        print('Initial Punter hand:', punter)

        result = 'Banker: {} vs Punter: {}\n{{}} wins'.format(banker,
                                                              punter)

        if banker > 7 or punter > 7:
            if banker > punter:
                print(result.format('Banker'))
            elif banker < punter:
                print(result.format('Punter'))
            else:
                print(result.format('Nobody'))
        else:
            if punter < 5:
                punter = punter2
            elif punter == 5:
                if npr.random(1) > 0.220504:
                    punter = punter2

c = Chemin()
c.play()
