#1. taking the task 
#2. storing the task
#3. show the list
#4. delete a task
class Todo:
    def __init__(self) -> None:
        self.__storage = []
        if len(self.__storage) == 0:
            print("Currently your all work is done\nAdd your daily task\n======================================================================================")
        else:
            self.show()
        n = True
        while n == True:
            try:
                self.task = int(input('\n\npress "1" : add your daily task\npress "2" : mark complete your completed task\npress "3" : show my list \npress "4" : Close application\npress "5" : delete your complete list\n\n'))
            except ValueError:
                self.task = int(input('\n\npress "1" : add your daily task\npress "2" : mark complete your completed task\npress "3" : show my list \npress "4" : Close application\npress "5" : delete your complete list\n\n'))
            if self.task == 1:
                self.take_task()
            elif self.task == 2:
                self.delete_task()
            elif self.task == 3:
                self.show()
            elif self.task == 4:
                self.show()
                break
            elif self.task == 4:
                del self
                break
            else:
                print("INVALID COMMAND\Try again")   
    def take_task(self):
        # self.__index_count = len(self.__storage)+1
        self.__input_values = str(input("Enter your task: "))
        self.__storage.append(self.__input_values)
    def show(self):
        j = 1
        for i in self.__storage:
            print(f"{j}) {i}")
    def delete_task(self):
        self.__deleted_task = int(input("Enter the completed task Sr no.:"))
        del self.__storage[self.__deleted_task]
        self.show() 
             
my = Todo()