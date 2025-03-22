from firebase_admin import firestore

db = firestore.client()
class LaunchModel:
    COLLECTION_NAME = "launch"
    @staticmethod
    def get(id, params):
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
        data["created_at"] = firestore.SERVER_TIMESTAMP
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("launch").add(data)[1]
    
    @staticmethod
    def update(id, data):
        data["updated_at"] = firestore.SERVER_TIMESTAMP
        return db.collection("launch").document(id).update(data)

    @staticmethod
    def delete(id):
        # validar se é uma transação parcelada
        launch = db.collection("launch").document(id)
        if not launch.get().exists:
            return {"error": "Não encontrado"}, 404
        
        if launch.get().get("parcelado"):
            launches = db.collection("launch").where("transacaoRef", "==", launch.get().get("transacaoRef")).stream()
            qt = 0
            for doc in launches:
                doc.reference.delete()
                qt += 1
            return {"success": True, "message": "{amount} itens removidos".format(amount=qt)}

        launch.delete()
        return {"success": True, "message": "Removido"}
