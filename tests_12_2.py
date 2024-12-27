import runner2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner2.Runner("Usain", 10)
        self.andrei = runner2.Runner("Andrei", 9)
        self.nick = runner2.Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(value)


    def test_usain_nick(self):
        tournament = runner2.Tournament(90, self.usain, self.nick)

        res = {}
        results = tournament.start()
        for i in results:
            res[i] = str(results[i])

        self.__class__.all_results[1] = res
        self.assertTrue(results[max(results)] == self.nick)


    def test_andrei_nick(self):
        tournament = runner2.Tournament(90, self.andrei, self.nick)

        res = {}
        results = tournament.start()
        for i in results:
            res[i] = str(results[i])
        self.__class__.all_results[2] = res
        self.assertTrue(results[max(results)] == self.nick)


    def test_usain_andrei_nick(self):
        tournament = runner2.Tournament(90, self.usain, self.andrei, self.nick)

        res = {}
        results = tournament.start()
        for i in results:
            res[i] = str(results[i])
        self.__class__.all_results[3] = res
        self.assertTrue(results[max(results)] == self.nick)

if __name__ == '__main__':
    unittest.main()