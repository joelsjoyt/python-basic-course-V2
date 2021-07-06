class Department:
    def __init__(self, name = None, authority = None ):
        self.department_name = name
        self.authority = authority
    
    def show_department(self):
        print(f'Department name: {self.name} || Authority: {self.authority}')


class User(Department):
    def __init__(self, name = None, id = None):
        super().__init__("ADS", "Classified")
        self.name = name
        self.id = id
    
    def show_user(self):
        print(f'User name: {self.name}, user_id: {self.id}')
        print(f'Deparment name: {self.department_name}, Authority: {self.authority}')

def main():
    user1 = User("Test",10)
    user1.show_user()
    
# Checks if the file is the main execution file 
if __name__ == "__main__":
    main()