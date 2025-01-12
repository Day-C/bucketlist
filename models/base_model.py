#!/usr/bin/python3
"""describe base attributes which will be inherited by all other models"""

from datetime import datetime
import models
import uuid

t_format = "%Y-%m-%dT%H:%M:%S:%f"


class Base_mod():
    """Define base attributes for all models"""

    def __init__(self, **kwargs):
        """initialize all instance attributes"""

        if kwargs:
            #craate instance from kwargs keys/values
            for key, value in kwargs.items():
                if key != "_sa_instance_state":
                    setattr(self, key, value)

            # check the time to update from string to correct type
            if kwargs.get('craated_at', None) and type('created_at') is str:
                self.created_at = datetime.strptime(self.created_at, t_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) and type('updated_at') is str:
                self.updated_at = datetime.strptime(self.updated_at, t_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()
            self.id = str(uuid.uuid4())

    def to_dict(self):
        """create a ductionary representation of an model instance."""

        inst_dict = self.__dict__
        if 'craated_at' in inst_dict and type(inst_dict['created_at']) is not str:
            inst_dict['created_at'] = inst_dict['created_at'].strftime(t_format)
        if 'updated_at' in inst_dict and type(inst_dict['updated_at']) is not str:
            inst_dict['updated_at'] = inst_dict['updated_at'].strftime(t_format)

        return inst_dict

    def __str__(self):
        """display string type information about an instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save a new inatance of a models to storage"""

        self.updated_at = datetime.utcnow()
        print('saving')
        models.file_storage.new(self)
        models.file_storage.save()

    def delete(self):
        """remove an exsting instance of a model from storage."""

        models.file_storage.delete(self)
        print('bye bye')

