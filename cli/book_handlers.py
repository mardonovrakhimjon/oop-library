from repositories.book_repository import BookRepository
from repositories.borrow_repository import BorrowRepository


class BookHandler:
    def show_all_book(self):
        books = BookRepository.get_all_book()
        for book in books:
            print(book['id'], book['title'])

    def search_book(self):
        serach = input('Search: ')
        books = BookRepository.get_all_book()
        for book in books:
            if serach == book['title']:
                print(book['id'], book['title'])

    def borrow_book(self, user):
        book_id = input('Book id: ')
        BorrowRepository.create_borrow(user, book_id)
    
    def return_book(self, user):
        
        book_id  = input("Qaytarmoqchi bo'lgan kitob ID si: ")
        success = BorrowRepository.delete_borrow(user.id, book_id)

        if success:
            print(f"ID: {book_id} bo'lgan kitob muvaffaqiyatli qaytarildi.")
        else:
            print("Xato: Siz bu kitobni ijaraga olmagansiz yoki ID noto'g'ri.")