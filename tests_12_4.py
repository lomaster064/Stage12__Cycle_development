import logging
import unittest
import runner3

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s | %(filename)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run = runner3.Runner('Ilya', speed=-5)
            for i in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run = runner3.Runner(123)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = runner3.Runner('Anton')
        run2 = runner3.Runner('Alena')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1, run2)

if __name__ == '__main__':
    unittest.main()
