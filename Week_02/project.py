import time

class TODO:
    
    todos=[]
    
    def add_todo(self, desc):
        ## 1. Take the description from the user.
        ## 2. We have to create one dictionary in which we will add the todo desc.
        ## 3. We have to append that dictionary inside todos.

        dict={
            'id':int(time.time()),
            'description':desc,
            'is_completed':False
        }
        self.todos.append(dict)
        print(f"---->{desc}; Added Successfully")

    def remove_todo(self, id):
        for i in self.todos:
            if i['id']==id:
                self.todos.remove(i)
    
    def display_todos(self):
        if len(self.todos)==0: return
        for i in self.todos:
            print(f"ID:{i['id']}, Task:{i['description']}, is_completed:{i['is_completed']}")
    
    def update_todo(self, id, new_desc):
        for i in self.todos:
            if i['id']==id:
                i['description']=new_desc
    
    def toggle_mark_as_completed(self, id):
        for i in self.todos:
            if i['id']==id:
                if i['is_completed']:
                    i['is_completed']=False
                    break
                else:
                    i['is_completed']=True

    def completed_todos(self):
        if len(self.todos)==0: return

        for i in self.todos:
            if i['is_completed']:
                print(f"-->{i['description']}")
    
    def incompleted_todos(self):
        if len(self.todos)==0: return

        for i in self.todos:
            if i['is_completed']==False:
                print(f"-->{i['description']}")

obj=TODO()
