import unittest


#Wyatt
#RM

class monkey(unittest.TestCase):
    def __init__(self,name,fruit):
      self.name = name
      self.fruit = fruit


    def collectfruit(self):
        return f"{self.name} collects {self.fruit}"
      
      
    
class chimp(monkey):
   def swing(self):
        return f"{self.name} swings from branch to branch"

class capuchin(monkey):
    def howl(self):
        return f"{self.name} Howls loudly!"
        
        
class testmonkey(unittest.TestCase):
    def test_collect_fruit(self):
        m = monkey("George", "banana")
        self.assertEqual(m.collectfruit(), "George collects banana")
        
        
class TestChimp(unittest.TestCase):
    def test_collect_fruit(self):
        c = chimp("Mordecai", "apple")
        self.assertEqual(c.collectfruit(), "Mordecai collects apple")
    
    def test_swing(self):
        c = chimp("Mordecai", "apple")
        self.assertEqual(c.swing(), "Mordecai swings from branch to branch")
        
class TestCapuchinMonkey(unittest.TestCase):
    def test_collect_fruit(self):
        testCap = capuchin("Julien", "lemon")
        self.assertEqual(testCap.collectfruit(), "Julien collects lemon")
    
    def test_howl(self):
        testCap2 = capuchin("Mort", "Orange")
        self.assertEqual(testCap2.howl(), "Mort Howls loudly!")


if __name__ == '__main__':
    unittest.main()



