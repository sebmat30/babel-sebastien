import year
import unittest


t_year = year.validate_year(1987)
print(t_year)
# expected output : 1987

t_year = year.validate_year("essai")
print(t_year)
# expected output : None


class TestSimple(unittest.TestCase):

    def test_validate_year(self):
        t_year = year.validate_year("1987")
        self.assertEqual(t_year, 1987)

        t_year = year.validate_year("13")
        self.assertEqual(t_year, 2013)

        t_year = year.validate_year("sdfghj")
        self.assertEqual(t_year, None)

        t_year = year.validate_year("2020")
        self.assertEqual(t_year, None)

        
if __name__ == '__main__':
    unittest.main()