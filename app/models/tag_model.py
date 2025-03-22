from firebase_admin import firestore

db = firestore.client()

class TagModel:
    @staticmethod
    def get(id):
        return db.collection("tags").stream()

    @staticmethod
    def create(data):
        ## add timestamp
        data["created_at"] = firestore.SERVER_TIMESTAMP
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("tags").add(data)
    
    @staticmethod
    def update(id, data):
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("tags").document(id).update(data)
    
    @staticmethod
    def delete(id):
        ## valida se documento existe
        doc = db.collection("tags").document(id)
        if not doc.get().exists:
            return {"error": "Não encontrado"}, 404
        
        doc.delete()
        return {"success": True, "message": "Removido"}
