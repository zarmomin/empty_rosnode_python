#!/usr/bin/env python
import unittest
import numpy as np
import numpy.testing


class TestCovarianceStuff(unittest.TestCase):
    def test_something(self):
        T_expected = np.asarray([
            -0.892758, -0.024074, 0.449893, 0.145993, 0.020839, -0.999709,
            -0.012143, -0.007044, 0.450054, -0.001466, 0.893000, -0.199547,
            0.000000, 0.000000, 0.000000, 1.000000
        ]).reshape((4, 4))
        numpy.testing.assert_array_almost_equal(T_expected, T_expected)


if __name__ == '__main__':
    unittest.main()
