import runner
import runner2
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = runner.Runner('Ilya')
        for i in range(10):
            run.walk()

        # Failure test
        # for i in range(11):
        #     run.walk()

        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner.Runner('Mariya')
        for i in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = runner.Runner('Anton')
        run2 = runner.Runner('Alena')

        for i in range(10):
            run1.walk()
            run2.run()

        self.assertNotEqual(run1, run2)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = runner2.Runner("Usain", 10)
        self.andrei = runner2.Runner("Andrei", 9)
        self.nick = runner2.Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nick(self):
        tournament = runner2.Tournament(90, self.usain, self.nick)

        res = {}
        results = tournament.start()
        for i in results:
            res[i] = str(results[i])

        self.__class__.all_results[1] = res
        self.assertTrue(results[max(results)] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrei_nick(self):
        tournament = runner2.Tournament(90, self.andrei, self.nick)

        res = {}
        results = tournament.start()
        for i in results:
            res[i] = str(results[i])
        self.__class__.all_results[2] = res
        self.assertTrue(results[max(results)] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
