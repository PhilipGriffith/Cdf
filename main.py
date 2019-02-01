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

        punter_hits = False

        hand = self._deal()
        banker_deal = hand[:3]
        punter_deal = hand[3:]

        banker1 = int(str(banker_deal[:2].sum())[-1])
        punter1 = int(str(punter_deal[:2].sum())[-1])

        banker2 = int(str(banker1 + banker_deal[-1])[-1])
        punter2 = int(str(punter1 + punter_deal[-1])[-1])

        print('Banker:', banker_deal)
        print('Punter:', punter_deal)

        print('Initial Banker hand:', banker1)
        print('Initial Punter hand:', punter1)

        print('Second Banker hand:', banker2)
        print('Second Punter hand:', punter2)

        result = 'Banker: {} vs Punter: {}\n{{}} wins'.format(banker1,
                                                              punter1)

        if banker1 > 7 or punter1 > 7:
            if banker1 > punter1:
                print(result.format('Banker'))
            elif banker1 < punter1:
                print(result.format('Punter'))
            else:
                print(result.format('Nobody'))
        else:
            if punter1 < 6:
                # Player hits
                punter1 = punter2
                if banker1
                    pass
            else:
                # Player stands
                if banker1 < 6:
                    banker1 = banker2



c = Chemin()
c.play()
