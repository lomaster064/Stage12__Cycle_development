import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = runner.Runner('Ilya')
        for i in range(10):
            run.walk()

        # Failure test
        # for i in range(11):
        #     run.walk()

        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner('Mariya')
        for i in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Anton')
        run2 = runner.Runner('Alena')

        for i in range(10):
            run1.walk()
            run2.run()

        self.assertNotEqual(run1, run2)


if __name__ == '__main__':
    unittest.main()
