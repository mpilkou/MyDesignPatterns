import unittest
import pickle as pic
import os

from multiprocessing.pool import ThreadPool as Pool
from singleton import Singleton, ChildSingleton

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")

"""Help fun"""
def help_threat_get_singleton():
    return Singleton()

def help_threat_read_singleton():
    with open("singleton","rb") as f:
        return pic.load(f)


class SingletonTest(unittest.TestCase):
    """Singleton"""

    def test_is_singleton(self):
        singleton_1 = Singleton()
        self.assertEqual(singleton_1.__class__.__name__,"Singleton")

    def test_is_same_singleton(self):
        singleton_1 = Singleton()
        singleton_2 = Singleton()
        self.assertEqual(singleton_1.get_instanse() is singleton_2.get_instanse(), True)

    def test_thread_save(self):
        try:
            pool1 = Pool(processes=1)
            pool2 = Pool(processes=1)
            self.assertEqual(pool1.apply_async(help_threat_get_singleton()).get(), pool2.apply_async(help_threat_get_singleton()).get())
        except:
            print ("Error") 
    
    """Inheritanse"""
    def test_is_different_singleton_inheritanse(self):
        singleton_1 = Singleton()
        singleton_2 = ChildSingleton()
        self.assertFalse(singleton_1.get_instanse() is singleton_2.get_instanse())

    def test_is_same_singleton_child_inheritanse(self):
        singleton_1 = ChildSingleton()
        singleton_2 = ChildSingleton()
        self.assertTrue(singleton_1.get_instanse() is singleton_2.get_instanse())

    """Serialisation"""
    def test_is_serialize(self):
        
        with open("singleton","wb") as f:
            pic.dump(Singleton(),f)

        try:
            pool1 = Pool(processes=1)
            pool2 = Pool(processes=1)
            self.assertEqual(pool1.apply_async(help_threat_read_singleton()).get(), pool2.apply_async(help_threat_read_singleton()).get())
        except:
            print ("Error in test")

        try:
            os.remove("singleton")
        except OSError:
            print ("Error in remove")

if __name__ == '__main__':
    unittest.main()