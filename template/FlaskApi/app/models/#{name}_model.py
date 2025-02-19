from firebase_admin import firestore

db = firestore.client()

class #{nameUp}Model:
    @staticmethod
    def get(id):
        return db.collection("#{name}s").where("id", "==", id).stream()

    @staticmethod
    def create(data):
        return db.collection("#{name}s").add(data)

    @staticmethod
    def delete(id):
        return db.collection("#{name}s").document(id).delete()
