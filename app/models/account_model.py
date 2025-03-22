from firebase_admin import firestore
db = firestore.client()
class AccountModel:
    @staticmethod
    def get(id):
        return db.collection("accounts").where("userRef", "==", id).stream()

    @staticmethod
    def create(data):
        data["created_at"] = firestore.SERVER_TIMESTAMP
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("accounts").add(data)
    
    @staticmethod
    def update(id, data):
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("accounts").document(id).update(data)

    @staticmethod
    def delete(id):
        return db.collection("accounts").document(id).delete()
