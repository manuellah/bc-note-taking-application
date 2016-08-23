import unittest
from NotesApplication import  NotesApplication

class TestNotesApp(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_notesapp_instance(self):
        myApp=NotesApplication('Emmanuel')
        self.assertIsInstance(myApp, NotesApplication, msg="The object should be an instance of the `NotesApplication` class" )
    def test_notesApp_type(self):    
        myApp=NotesApplication('Emmanuel')
        self.assertTrue(type(myApp) is NotesApplication)
        
    def test_notesApp_no_argument(self):
        myApp=NotesApplication()
        self.assertEqual(myApp.author, "Author")
        
    def test_notesApp_with_argument(self):
        myApp=NotesApplication("Emmanuel")
        self.assertEqual(myApp.author, "Emmanuel")
        
    def test_create(self):
        myApp=NotesApplication("Emmanuel")
        myApp.create("Andela bt-p")
        self.assertIn("Andela bt-p",myApp.note_list)
    
    def test_get(self):
        myApp=NotesApplication("Emmanuel")
        myApp.create("Andela bt-p")
        self.assertEqual(myApp.get(0), "Andela bt-p")
        
    def test_search(self):
        myApp=NotesApplication("Emmanuel")
        myApp.create("Andela bt-p")
        self.assertEqual(myApp.search("something x"),"Not in my notes notes, please check in the net, lol")
        
    def test_search_none(self):
        myApp=NotesApplication("Emmanuel")
        self.assertIsNone(myApp.search("something x"))
        
    def test_delete(self):
        myApp=NotesApplication("Emmanuel")
        myApp.create('Notes for class 1')
        myApp.create('Notes for class 2')
        x=len(myApp.note_list)
        myApp.delete(0)
        y=len(myApp.note_list)
        self.assertEqual(x,y+1)

    def test_edit(self):
        pass
        

    
if __name__ == "__main__":  
    unittest.main()

    