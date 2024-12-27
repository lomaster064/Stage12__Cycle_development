import unittest
import tests_12_3


RunnerSuite = unittest.TestSuite()

RunnerSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunnerSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity = 2)
runner.run(RunnerSuite)

