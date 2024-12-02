class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    ADVANTAGE = 1
    WINNING = 2

    SCORES = {
        LOVE: "Love",
        FIFTEEN: "Fifteen",
        THIRTY: "Thirty",
        FORTY: "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        self.scores[player_name] += 1

    def get_score(self):
        player1_score = self.scores[self.player1_name]
        player2_score = self.scores[self.player2_name]

        if player1_score == player2_score:
            return self.get_tied_score(player1_score)
        if player1_score >= 4 or player2_score >= 4:
            return self.get_end_score(player1_score, player2_score)
        return self.get_other_score(player1_score, player2_score)
        
    def get_tied_score(self, score):
        if score < self.FORTY:
            return f"{self.SCORES[score]}-All"
        return "Deuce"

    def get_end_score(self, player1_score, player2_score):
        score_difference = player1_score - player2_score

        if score_difference == self.ADVANTAGE:
            return f"Advantage {self.player1_name}"
        if score_difference == -self.ADVANTAGE:
            return f"Advantage {self.player2_name}"
        if score_difference >= self.WINNING:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def get_other_score(self, player1_score, player2_score):
        return f"{self.SCORES[player1_score]}-{self.SCORES[player2_score]}"
