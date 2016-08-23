class NotesApplication(object):
    notes_id=0
    
    def __init__(self,author="Author"):
        self.author=author
        self.note_list=[]
        NotesApplication.notes_id+=1
        self.id=NotesApplication.notes_id
        
    def create(self, note_content=""):
        if note_content:
            self.note_list.append(note_content)
            return

        note_content=input("What do you have in mind!!!!???  :   ")
        self.note_list.append(note_content)
    
    def list(self):
        count=1
        for item in self.note_list:
            print("Note ID","  ",str(self.id) +"\n")
            print(count,"  ",item +"\n")
            print("By Author","  ", self.author)
            print("="*30 +"\n")
            count+=1

    
    def get(self, note_id):
        return str(self.note_list[note_id])
    
    def search(self, search_text):
        notes_index_list=[]
        for item in self.note_list:
            item=str(item)
            if search_text in item:
                print("Showing results for search ", search_text)
                self.list()
            else:
                return "Not in my notes notes, please check in the net, lol"
                
            
    def delete(self, note_id):
        self.note_list.pop(note_id)
    
    def edit(self, note_id, new_content=""):
        if new_content:
            self.note_list[note_id]=new_content
            return
            
        new_content = input("Write you edit text here  :   ")
        self.note_list[note_id]=new_content
    
#s=NotesApplication("Emmanuel")
#s.create("MMamamams rrdididid")
#s.create("Usdsdsd sajsd dddfdfdfd")
#s.create("Dadadsdf sdd sdsdfsf sfsfsds")
#print (s.search("rrdididd"))
#print (s.get(1))
#s.edit(1,"Oooh my code")
#s.delete(2)
#s.list()




    
