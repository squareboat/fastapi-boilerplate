from tortoise.models import Model

class BaseModel(Model):
    def to_dict(self):
        unwanted_keys = ['_partial', '_saved_in_db', '_custom_generated_pk']
        print(self.__dict__)
        result = self.__dict__
        for key in unwanted_keys:
            result.pop(key)
        
        return result
