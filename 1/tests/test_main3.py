from unittest import TestCase
from mains.main3 import main as main3

success_result = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'



class testMain1(TestCase):

    def test_result_equal(self):

        # 1 вариант входных данных
        ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
        # Правильный результат
        success_result = "Уникальные гео-ids: [98, 35, 15, 213, 54, 119]"

        self.assertEqual(main3(ids), success_result)

    def test_result_equal2(self):
        
        # 2 вариант входных данных
        ids2 = {'user1': [88, 22, 19, 75, 75],
       'user2': [89, 24, 24, 100, 100],
       'user3': [54, 98, 98, 35]}
        # Правильный результат
        success_result = 'Уникальные гео-ids: [98, 35, 100, 75, 19, 22, 54, 88, 89, 24]'
        
        self.assertEqual(main3(ids2), success_result)
