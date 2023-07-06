from pkgs.core.transformer import Transformer
from .users import UserTransformer

class JobTransformer(Transformer):
    def transform(self, obj):
        return {
            "id": obj.get('uuid'),
            "title": obj.get('title'),
            "description": obj.get('description'),
            "created_by": obj.get('_created_by'),
            "created_at": obj.get('created_at'),
            "updated_at": obj.get('updated_at')
        }
    
    def include_created_by(self, data, include_options = {}):
        return self.item(data.get('created_by'), UserTransformer(), include_options)