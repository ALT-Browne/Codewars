class User(object):
    def __init__(self, rank=-8):
        assert (rank in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]), "Not a valid user rank"
        self.rank = rank
        self.progress = 0

    def inc_progress(self, rank):
        assert (rank in [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]), "Not a valid activity rank"
        if self.rank > 0:
            user_rank = self.rank - 1
        else:
            user_rank = self.rank
        if rank > 0:
            act_rank = rank - 1
        else:
            act_rank = rank
        if act_rank - user_rank == -1:
            self.progress += 1
        if act_rank - user_rank == 0:
            self.progress += 3
        if act_rank - user_rank > 0:
            self.progress += 10 * ((act_rank - user_rank) ** 2)
        rank_inc = self.progress // 100
        self.progress %= 100
        if self.rank < 0 and (self.rank + rank_inc) >= 0:
            self.rank = self.rank + rank_inc + 1
        else:
            self.rank += rank_inc
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
