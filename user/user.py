class User:
    def __init__(self, name = None, id = None):
        self.name = name
        self.id = id
    
    def show_user(self):
        print(f'User name: {self.name}, user_id: {self.id}')

def main():
    user1 = User("Test",10)
    user1.show_user()
    
# Checks if the file is the main execution file 
if __name__ == "__main__":
    main()