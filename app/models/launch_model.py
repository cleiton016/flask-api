from firebase_admin import firestore


class LaunchModel:
    COLLECTION_NAME = "launch"
    @staticmethod
    def get(id, params):
        db = firestore.client()
        query = db.collection("launch")\
            .where("accountRef", "==", id )\
            .limit(params.get("limit", 10)).offset(params.get("offset", 0))\
            .order_by('numeroParcela')
        
        last_doc_id = params.get("last_doc_id", None)

        if last_doc_id:
            last_doc = db.collection(LaunchModel.COLLECTION_NAME).document(last_doc_id).get()
            if last_doc.exists:
                query = query.start_after(last_doc)

        return query.stream()

    @staticmethod
    def create(data):
        db = firestore.client()
        return db.collection("launch").add(data)[1]

    @staticmethod
    def delete(id):
        db = firestore.client()
        return db.collection("launch").document(id).delete()
