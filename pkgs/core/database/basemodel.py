from tortoise.models import Model

class BaseModel(Model):
    def to_dict(self):
        unwanted_keys = ['_partial', '_saved_in_db', '_custom_generated_pk']
        base_dict = self.__dict__
        result = {}
        
        for k, v in base_dict.items():
            if k in unwanted_keys:
                continue
            elif isinstance(v, BaseModel):
                result[k[1:]] = v.to_dict()
            else:
                result[k] = v
            
        
        return result
