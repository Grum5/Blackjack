from src.models.player import Player


class Dealer(Player):

    def __init__(self) -> None:
        super().__init__(name="dealer")

    @property
    def should_hit(self) -> bool:
        '''
            El dealer se plantea al tener 17
        '''

        return self.get_score() < 17
