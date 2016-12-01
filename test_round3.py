from __future__ import print_function, division, absolute_import
import unittest

from round3 import round


class Round3Test(unittest.TestCase):

	def test_second_argument_type(self):
		# any type with an __index__ method should be permitted as
		# a second argument
		self.assertAlmostEqual(round(12.34, True), 12.3)

		class MyIndex(object):
			def __index__(self): return 4
		self.assertAlmostEqual(round(-0.123456, MyIndex()), -0.1235)
		# but floats should be illegal
		self.assertRaises(TypeError, round, 3.14159, 2.0)

	def test_halfway_cases(self):
		self.assertAlmostEqual(round(0.125, 2), 0.12)
		self.assertAlmostEqual(round(0.375, 2), 0.38)
		self.assertAlmostEqual(round(0.625, 2), 0.62)
		self.assertAlmostEqual(round(0.875, 2), 0.88)
		self.assertAlmostEqual(round(-0.125, 2), -0.12)
		self.assertAlmostEqual(round(-0.375, 2), -0.38)
		self.assertAlmostEqual(round(-0.625, 2), -0.62)
		self.assertAlmostEqual(round(-0.875, 2), -0.88)

		self.assertAlmostEqual(round(0.25, 1), 0.2)
		self.assertAlmostEqual(round(0.75, 1), 0.8)
		self.assertAlmostEqual(round(-0.25, 1), -0.2)
		self.assertAlmostEqual(round(-0.75, 1), -0.8)

		self.assertEqual(round(-6.5, 0), -6.0)
		self.assertEqual(round(-5.5, 0), -6.0)
		self.assertEqual(round(-1.5, 0), -2.0)
		self.assertEqual(round(-0.5, 0), 0.0)
		self.assertEqual(round(0.5, 0), 0.0)
		self.assertEqual(round(1.5, 0), 2.0)
		self.assertEqual(round(2.5, 0), 2.0)
		self.assertEqual(round(3.5, 0), 4.0)
		self.assertEqual(round(4.5, 0), 4.0)
		self.assertEqual(round(5.5, 0), 6.0)
		self.assertEqual(round(6.5, 0), 6.0)

		# same but without an explicit second argument; in 2.x these
		# will give floats
		self.assertEqual(round(-6.5), -6)
		self.assertEqual(round(-5.5), -6)
		self.assertEqual(round(-1.5), -2.0)
		self.assertEqual(round(-0.5), 0)
		self.assertEqual(round(0.5), 0)
		self.assertEqual(round(1.5), 2)
		self.assertEqual(round(2.5), 2)
		self.assertEqual(round(3.5), 4)
		self.assertEqual(round(4.5), 4)
		self.assertEqual(round(5.5), 6)
		self.assertEqual(round(6.5), 6)

		# no ndigits and input is already an integer: output == input
		rv = round(1)
		self.assertEqual(rv, 1)
		self.assertTrue(isinstance(rv, int))
		rv = round(1.0)
		self.assertEqual(rv, 1)
		self.assertTrue(isinstance(rv, int))

		self.assertEqual(round(-25.0, -1), -20.0)
		self.assertEqual(round(-15.0, -1), -20.0)
		self.assertEqual(round(-5.0, -1), 0.0)
		self.assertEqual(round(5.0, -1), 0.0)
		self.assertEqual(round(15.0, -1), 20.0)
		self.assertEqual(round(25.0, -1), 20.0)
		self.assertEqual(round(35.0, -1), 40.0)
		self.assertEqual(round(45.0, -1), 40.0)
		self.assertEqual(round(55.0, -1), 60.0)
		self.assertEqual(round(65.0, -1), 60.0)
		self.assertEqual(round(75.0, -1), 80.0)
		self.assertEqual(round(85.0, -1), 80.0)
		self.assertEqual(round(95.0, -1), 100.0)
		self.assertEqual(round(12325.0, -1), 12320.0)
		self.assertEqual(round(0, -1), 0.0)

		self.assertEqual(round(350.0, -2), 400.0)
		self.assertEqual(round(450.0, -2), 400.0)

		self.assertAlmostEqual(round(0.5e21, -21), 0.0)
		self.assertAlmostEqual(round(1.5e21, -21), 2e21)
		self.assertAlmostEqual(round(2.5e21, -21), 2e21)
		self.assertAlmostEqual(round(5.5e21, -21), 6e21)
		self.assertAlmostEqual(round(8.5e21, -21), 8e21)

		self.assertAlmostEqual(round(-1.5e22, -22), -2e22)
		self.assertAlmostEqual(round(-0.5e22, -22), 0.0)
		self.assertAlmostEqual(round(0.5e22, -22), 0.0)
		self.assertAlmostEqual(round(1.5e22, -22), 2e22)


if __name__ == "__main__":
	unittest.main()
