import pandas as pd
import unittest
import dataframe_quiz1 as quiz_script  

class TestQuizMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'Experience': [5, 3, 7, 4, 6],
            'Monthly Salary': [5000, 4500, 5500, 4800, 5200],
            'Department': ['HR', 'Finance', 'IT', 'HR', 'Marketing'],
            'Location': ['New York', 'London', 'Paris', 'London', 'Berlin']
        }, index = ['Elena', 'Aiden', 'Grace', 'Michael', 'Lucas'])

    def test_get_department(self):
        expected_output = pd.Series(['HR', 'Finance', 'IT', 'HR', 'Marketing'], name="Department", index = ['Elena', 'Aiden', 'Grace', 'Michael', 'Lucas'])
        result = quiz_script.get_department(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_second_record(self):
        expected_output = pd.Series(['Aiden', 3, 4500, 'Finance', 'London'], index=self.df.columns, name=1)
        result = quiz_script.get_second_record(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_info_grace(self):
        expected_data = {'Experience': 7, 'Monthly Salary': 5500, 'Department': 'IT', 'Location': 'Paris'}
        expected_output = pd.Series(expected_data, name = "Grace")
        result = quiz_script.get_info_grace(self.df)
        pd.testing.assert_series_equal(result, expected_output)

    def test_get_experience_location(self):
        expected_data = {'Experience': [5, 3, 7, 4, 6], 'Location': ['New York', 'London', 'Paris', 'London', 'Berlin']}
        expected_output = pd.DataFrame(expected_data, index = ['Elena', 'Aiden', 'Grace', 'Michael', 'Lucas'])
        result = quiz_script.get_experience_location(self.df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_get_experience_salary_third_to_end(self):
        expected_data = {'Experience': [7, 4, 6], 'Monthly Salary': [5500, 4800, 5200]}
        expected_output = pd.DataFrame(expected_data, index=["Grace","Michael","Lucas"])
        result = quiz_script.get_experience_salary_third_to_end(self.df)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_get_department_elena_aiden(self):
        expected_output = pd.Series(['HR', 'Finance'], name="Department", index=["Elena","Aiden"])
        result = quiz_script.get_department_elena_aiden(self.df)
        pd.testing.assert_series_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()
