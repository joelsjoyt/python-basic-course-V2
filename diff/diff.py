
def diff(a,b):
    print(f'__name__:{__name__}')
    return a+b

def main():
    print(diff(10, 20))
    
# Checks if the file is the main execution file
if __name__ == "__main__":
    main()