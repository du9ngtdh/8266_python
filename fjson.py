import json
class FJson:
    def __init__(self, data: str):
        self.__json = json.loads(data)

    def toString(self):
        return json.dumps(self.__json)

    def value(self, key: str):
        return self.__json[key]

    def keys(self):
        listKeys = []
        keys = self.__json.keys()
        for k in keys:
            listKeys.append(k)

        return listKeys
