from view import View

class ViewMain(View.View):
    def show(self):
        print("teste main")
        pass

        
def main():
    user = input("Usuario:")
    password = md5(getpass().encode()).hexdigest()
    print(user)
    print(password)
    pass 
    
if __name__ == "__main__":
    main()   