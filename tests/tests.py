import unittest
import pygematria
from pygematria import conv


class TestClient(unittest.TestCase):

    sample_letters_string = "Test."
    sample_letters_list = ['This', 'is', 'a', 'test.']
    sample_numbers_string = '100 + 8 + 9 + 90'
    sample_numbers_list = ['100 + 8 + 9 + 90', '9 + 90']
    sample_numbers_list_no_plus = [100, 8, 9, 90]
    sample_numbers_string_list = ['100', '8l', '9l', '90l']
        
    def test_nums_to_list_string(self):
        assert pygematria.conv.nums_to_list(TestClient.sample_numbers_string) == ['100', '8', '9', '90']

    def test_nums_to_list_list(self):
        assert pygematria.conv.nums_to_list(TestClient.sample_numbers_list) == ['100', '8', '9', '90', 'space', '9', '90']

    def test_lets_to_nums_string(self):
        assert pygematria.conv.lets_to_nums(TestClient.sample_letters_string) == ['100', '5l', '90l', '100l', '.']

    def test_lets_to_nums_list(self):
         assert pygematria.conv.lets_to_nums(TestClient.sample_letters_list) == ['100', '8l', '9l', '90l', '9l', '90l', '1l', '100l', '5l', '90l', '100l', '.']

    def test_nums_to_lets_string(self):
          assert pygematria.conv.nums_to_lets(TestClient.sample_numbers_string) == 'THIS'
    
    def test_nums_to_lets_list(self):
         assert pygematria.conv.nums_to_lets(TestClient.sample_numbers_string) == 'THIS'
    
    def test_nums_to_lets_list(self):
         assert pygematria.conv.nums_to_lets(TestClient.sample_numbers_string) == 'THIS'
    
    def test_string_and_num_values_string(self):
         assert pygematria.conv.string_and_num_values(TestClient.sample_letters_string) == [('T', '100'), ('e', '5'), ('s', '90'), ('t', '100')]
    
    def test_string_and_num_values_list(self):
         assert pygematria.conv.string_and_num_values(TestClient.sample_letters_list) == [('This', '207'), ('is', '99'), ('a', '1'), ('test.', '295')]
    
    def test_num_list_to_words(self):
        assert pygematria.conv.num_list_to_words(TestClient.sample_numbers_string_list) == 'This'
    
    def test_string_to_nums(self):
         assert pygematria.conv.string_to_nums(TestClient.sample_letters_string) == ['100', '5l', '90l', '100l', '.']
     
    def test_string_values(self):
         assert pygematria.conv.string_values(TestClient.sample_letters_list) == [207, 99, 1, 295]
         

if __name__ == "__main__":
     unittest.main()