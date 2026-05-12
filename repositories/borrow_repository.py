import json
from uuid import uuid1


class BorrowRepository:
    @staticmethod
    def read_file():
        with open("data/borrow.json") as f:
            return json.loads(f.read())
        
    @staticmethod
    def save_file(borrows):
        with open("data/borrow.json", "w") as f:
            f.write(json.dumps(borrows, indent=4))

    @staticmethod
    def create_borrow(user, book_id):
        borrows = BorrowRepository.read_file()
        borrows.append({
            'id': str(uuid1()),
            'user_id': user.id,
            'book_id': book_id
        })
        BorrowRepository.save_file(borrows)
        
    @staticmethod
    def delete_borrow(user_id, book_id):
        borrows = BorrowRepository.read_file()
        
        new_borrows = [
            b for b in borrows 
            if not (str(b['user_id']) == str(user_id) and str(b['book_id']) == str(book_id))
        ]
        
        if len(new_borrows) < len(borrows):
            BorrowRepository.save_file(new_borrows)
            return True
        
        return False