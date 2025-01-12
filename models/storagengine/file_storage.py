#!/usr/bin/python3
"""storage system"""

import json
from models.user import User
from models.comment import Comment
from models.post import Post

classes = {User: "user", Comment: "comment", Post: "post"}



class FileStorage():
    """define storage attributes for file storage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """retrieve all objects"""

        if cls != None:
            if cls in classes:
                all_data = self.reload()
                clss = {}
                for key in all_data.keys():
                    #splitkey to know the class and if the same as cls ass to list
                    key_split = key.split('.')
                    cls_split = str(cls).split('.')
                    cls_name = cls_split[2][:-2]
                    if key_split[0] == cls_name:
                        print("inside")
                        clss[key] = all_data[key]
                return clss
            return "Invalid class"
        return self.reload()


    def new(self, obj):
        """set __object"""

        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serialize __objects to json"""

        print(self.__objects)
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects, default=str))
    
    def delete(self, obj):
        """remove a models instance from stroage"""

        all_models = self.reload()
        for key in all_models.keys():
            if all_models[key]['id'] == obj.id:
                del all_models[key]
                self.save()
                break

    def reload(self):
        """deserialize the json file to __on=bjects"""

        try:
            with open(self.__file_path, 'r') as f:
              data = f.read()
              self.__objects = json.loads(data)
              #print(self.__objects)
              return self.__objects
        except FileNotFoundError:
            return {}


    def get(self, cls=None, id=None):
        """Find a models by its class name and id"""

        if cls != None:
            if cls in classes:
                if id != None:
                    all_models = self.reload()
                    for key in all_models.keys():
                        #split key to compare ids
                        key_split = key.split('.')
                        if key_split[1] == id:
                            return all_models[key]
        return None

    def count(self, cls=None):
        """Count the number if instances of a models exist"""

        all_models = self.reload()
        i = 0
        if cls == None:
            for key in all_models.keys():
                i += 1
            return 1
        else:
            if cls in classes:
                for key in all_models.keys():
                    #split key to get all coresponding classes
                    key_split = key.split('.')
                    if key_split[0] == cls:
                        i += 1
                return 1


