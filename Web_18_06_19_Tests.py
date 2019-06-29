# Методы:
# ●SetUp - запускается перед выполнением каждого теста в классе
# ●TearDown - запускается после каждого теста в классе
# ●SetUpClass - перед запуском тестового класса
# ●TearDownClass — по завершению всех тестов в классе
# ●skipTest(reason) — вызывается что бы пропустить текущий тест
# Функции:
# ●SetUpModule — перед запуском каких либо тестов в модуле
# ●TearDownModule — по завершению всех тестов в модуле
# Декораторы:
# ●skipIf /skipUnless — пропустить тест по условию

import unittest
from random import randint
from Web2_18_06_19_Tests import BuildingStack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = BuildingStack()

    def test_push_build(self):
        self.assertEquals(len(self.stack.order), 0)
        self.stack.push(randint(1, 100))
        self.assertEquals(len(self.stack.order), 1)
        # self.assertNotEqual(len(self.stack.order), 0)

    def test_pop_build(self):
        self.stack.push(randint(1, 100))
        self.assertEquals(len(self.stack.order), 1)
        self.stack.pop()
        self.assertEquals(len(self.stack.order), 0)
        self.assertIsNotNone(self.stack.order)

    def test_not_index_error(self):
        self.stack.push(randint(1, 100))
        self.assertEquals(len(self.stack.order), 1)
        self.stack.pop()

        self.assertIsNone(self.stack.head)

    def test_type_push(self):
        self.assertRaises(ValueError, self.stack.push, 'asd')

        with self.assertRaises(ValueError):
            self.stack.push('zdf')

