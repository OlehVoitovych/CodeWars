import unittest
4
import main
from main import *


class TestClass(unittest.TestCase):
	def test_1(self):
		(self.assertEqual(main.decode_morse('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'), 'HEY JUDE'))
	def test_2(self):
		(self.assertEqual(main.decode_morse('11'), 'E'))