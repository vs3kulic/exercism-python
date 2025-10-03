"""This module implements the HighScores class for managing game scores."""

class HighScores:
    """A class to manage a list of game scores."""
    def __init__(self, scores: list[int]):
        self.scores = scores

    def latest(self) -> int | None:
        """Return the latest score."""
        return self.scores[-1] if self.scores else None

    def personal_best(self) -> int | None:
        """Return the highest score."""
        return max(self.scores) if self.scores else None

    def personal_top_three(self) -> list[int]:
        """Return the top three scores in descending order."""
        if not self.scores:
            return []
        sorted_scores = sorted(self.scores, reverse=True)
        return sorted_scores[:3] if len(sorted_scores) >= 3 else sorted_scores

    @classmethod
    def scores_from_string(cls, score_string: str):
        """Return just the scores list from string."""
        scores = [int(x.strip()) for x in score_string.split(',')]
        return scores

def main():
    """Main function to demonstrate the HighScores class."""
    scores = HighScores.scores_from_string("30, 50, 20, 70, 10")
    high_scores = HighScores(scores)
    print("All scores:", high_scores.scores)
    print("Latest score:", high_scores.latest())
    print("Personal best:", high_scores.personal_best())
    print("Top three scores:", high_scores.personal_top_three())

if __name__ == "__main__":
    main()
