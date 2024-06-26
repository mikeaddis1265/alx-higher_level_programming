#!/usr/bin/python3

"""
    Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation -
    TestBase_to_json_string -
    TestBase_save_to_file - 
    TestBase_from_json_string
    TestBase_create 
    TestBase_load_from_file 
    TestBase_save_to_file_csv 
    TestBase_load_from_file_csv 
"""


import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id,  b2.id - 1)
    
    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1, b3.id - 2)
    
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
    
    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)
    
    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
    
    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)
    
    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
    
    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)
    
    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
    
    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
