import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, "3 - Arrays"))
sys.path.insert(0, os.path.join(BASE_DIR, "4 - Linked List"))
sys.path.insert(0, os.path.join(BASE_DIR, "5 - Sorting"))

from binary_search import binary_search
from exponential_search import exponential_search
from linked import DoublyLinkedList
from bubble_sort import bubble


def collect_forward(dll, limit=20):
    values = []
    node = dll.head
    while node is not None and len(values) < limit:
        values.append(node.value)
        node = node.next
    return values


def collect_backward(dll, limit=20):
    values = []
    node = dll.tail
    while node is not None and len(values) < limit:
        values.append(node.value)
        node = node.prev
    return values


class TestBinarySearch(unittest.TestCase):
    def test_acha_elemento(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13], 9, 0, 7), 4)

    def test_respeita_intervalo_lo_hi(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 2, 3, 5), -1)

    def test_nao_encontrado(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4, 0, 4), -1)


class TestExponentialSearch(unittest.TestCase):
    def test_acha_elemento(self):
        self.assertEqual(exponential_search(list(range(1, 101)), 32), 31)

    def test_maior_que_todos_nao_crashes(self):
        self.assertEqual(exponential_search([1, 2, 3], 10), -1)

    def test_lista_vazia(self):
        self.assertEqual(exponential_search([], 5), -1)

    def test_lista_de_um_elemento(self):
        self.assertEqual(exponential_search([5], 3), -1)


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
        self.dll.add_to_front(3)
        self.dll.add_to_front(2)
        self.dll.add_to_front(1)
        self.dll.add_to_end(4)
        self.dll.add_to_end(5)

    def test_percorre_frente_e_tras(self):
        self.assertEqual(collect_forward(self.dll), [1, 2, 3, 4, 5])
        self.assertEqual(collect_backward(self.dll), [5, 4, 3, 2, 1])

    def test_remove_pelas_pontas(self):
        self.assertEqual(self.dll.remove_from_front(), 1)
        self.assertEqual(self.dll.remove_from_end(), 5)
        self.assertEqual(collect_forward(self.dll), [2, 3, 4])


class TestBubbleSort(unittest.TestCase):
    def test_ordena_dois_tres_um(self):
        arr = [2, 3, 1]
        bubble(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_ordena_invertido(self):
        arr = [5, 4, 3, 2, 1]
        bubble(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_ja_ordenado(self):
        arr = [1, 2, 3, 4, 5]
        bubble(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
