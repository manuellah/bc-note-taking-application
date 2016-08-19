class NotesApplication(object):
    note_content=raw_input("What do you have in mind!!!!???")
    
    notes_id=0
    def __init__(self,author="Author"):
        self.author=author
        self.note_list=[]
        NotesApplication.notes_id+=1
        self.id=NotesApplication.notes_id
        
    def create(self, note_content):
        self.note_list.append(note_content)
    
    def list(self):
        for item in self.note_list:
            print("Note ID","  ",self.id)
            print(item)
            print()
            print("By Author","  ", self.author)
            
    
    def get(self, note_id):
        return str(self.note_list[note_id])
    
    def search(self, search_text):
        notes_index_list=[]
        print("Showing results for search ", search_text)
        for item in self.note_list:
            item=str(item)
            if search_text in item:
                print
                self.list()
                print("==============================================")
            
    def delete(self, note_id):
        self.note_list.pop(note_id)
    
    def edit(self, note_id, new_content):
        note_content = raw_input("Write you edit text here") 
        self.note_list[note_id]=new_content
    
        