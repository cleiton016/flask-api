from firebase_admin import firestore
class AccountModel:
    @staticmethod
    def get(id):
        db = firestore.client()
        return db.collection("accounts").where("userRef", "==", id).stream()

    @staticmethod
    def create(data):
        db = firestore.client()
        return db.collection("accounts").add(data)

    @staticmethod
    def delete(id):
        db = firestore.client()
        return db.collection("accounts").document(id).delete()
