from firebase_admin import firestore


class LaunchModel:
    @staticmethod
    def get(id):
        db = firestore.client()

        return db.collection("launch").where("accountRef", "==", id).stream()

    @staticmethod
    def create(data):
        db = firestore.client()

        return db.collection("launch").add(data)

    @staticmethod
    def delete(id):
        db = firestore.client()

        return db.collection("launch").document(id).delete()
