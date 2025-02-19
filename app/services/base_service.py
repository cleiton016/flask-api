class BaseService:
    @staticmethod
    def serialize(data):
        list = []
        for item in data:
            obj = item.to_dict()
            obj["id"] = item.id
            list.append(obj)
        return list