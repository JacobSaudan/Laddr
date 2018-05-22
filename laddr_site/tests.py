# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .utility import update_average

# Create your tests here.

class RunningAverage(TestCase):

	def test_one_value(self):
		self.assertTrue(2, update_average(0,0,2))

	def test_second_value(self):
		self.assertTrue(3, update_average(1, 1, 5))

	def test_many_values(self):
		self.assertTrue(101, update_average(100, 100, 201))
