import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_if_player_found(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)

        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_search_if_player_not_found(self):
        player = self.stats.search("Empty")
        self.assertIsNone(player)

    def test_team_if_players_found(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)

        self.assertEqual(team_players[0].name, "Semenko")
        self.assertEqual(team_players[1].name, "Kurri")
        self.assertEqual(team_players[2].name, "Gretzky")

    def test_team_if_players_not_found(self):
        team_players = self.stats.team("Empty")
        self.assertEqual(len(team_players), 0)

    def test_top_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)

        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_if_top_players_none(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 0)

    def test_top_sort_by_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)

        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_sort_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)

        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_sort_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)

        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")