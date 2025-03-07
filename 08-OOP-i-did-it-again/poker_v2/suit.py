class Suit:
    def __init__(self, suit: str) -> None:
        self.suit = self._check_valid(suit)

    def _check_valid(self, suit: str) -> str:
        if not isinstance(suit, str):
            raise TypeError('Sorry, that is invalid input. A string is required')
        elif suit not in ['H', 'D', 'S', 'C']:
            raise ValueError('This is not a valid suit')
        return suit
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Suit):
            return self.suit == other.suit
        else:
            raise NotImplementedError()
