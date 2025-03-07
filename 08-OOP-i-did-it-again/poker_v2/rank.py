class Rank:
    def __init__(self, rank: str) -> None:
        self.RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.rank = self._check_valid(rank)

    def _check_valid(self, rank: str) -> str:
        if not isinstance(rank, str):
            raise TypeError('Sorry, that is an invalid type. It should be a string type.')
        elif rank not in self.RANKS:
            raise ValueError('Sorry, that is not a valid rank')
        return rank
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return self.rank == other.rank
        else:
            raise NotImplementedError()
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)
        else:
            raise NotImplementedError()
        
    def __hash__(self) -> int:
        return self.rank.__hash__()
    
    def __sub__(self, other: object) -> int:
        if isinstance(other, Rank):
            return self.RANKS.index(self.rank) - self.RANKS.index(other.rank)
        else:
            raise NotImplementedError()
    