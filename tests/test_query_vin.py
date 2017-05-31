# -*- coding: utf-8 -*-

from unittest import TestCase
from QueryVin import QueryVinService


class TestQueryVin(TestCase):

    def test_query_vin_by_return_one_result(self):
        left_vin = 'LSVAL218'
        right_vin = 'B2366933'
        res = QueryVinService.run(left_vin, right_vin)
        self.assertEqual(len(res), 1, 'success')

    def test_query_vin_by_return_ten_results(self):
        left_vin = 'lsja24u6'
        right_vin = 'fs037618'
        res = QueryVinService.run(left_vin, right_vin)
        self.assertEqual(len(res), 10, 'success')

    def test_query_vin_by_return_two_results(self):
        left_vin = 'lbvnu790'
        right_vin = '9sb81546'
        res = QueryVinService.run(left_vin, right_vin)
        self.assertEqual(len(res), 2, 'success')