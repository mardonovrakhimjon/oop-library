from cli.menu import Menu
from cli.auth_handlers import AuthHandler
from cli.book_handlers import BookHandler


class Library:
    def __init__(self):
        self.menu = Menu()
        self.auth_handler = AuthHandler()
        self.book_handler = BookHandler()

    def run(self):
        print("----Library`ga xush kelibsiz----")

        while True:
            if self.auth_handler.current_user:
                self.menu.print_user_menu()

                option = input("> ")
                if option == "0":
                    self.auth_handler.logout()
                elif option == "1":
                    self.book_handler.search_book()
                elif option == "2":
                    self.book_handler.show_all_book()
                elif option == "3":
                    self.book_handler.borrow_book(self.auth_handler.current_user)
                elif option == "4":
                    self.book_handler.return_book(self.auth_handler.current_user)
                else:
                    print("Bunday menu yo'q")
            else:
                self.menu.print_main_menu()

                option = input("> ")
                if option == "1":
                    self.auth_handler.register()
                elif option == "2":
                    self.auth_handler.login()
                elif option == "0":
                    print("Dasturdan chiqildi.")
                    break
                else:
                    print("Bunday menu yo'q")