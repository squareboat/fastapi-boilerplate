from pkgs.core.transformer import Transformer

class JobTransformer(Transformer):
    def transform(self, obj):
        return {
            "id": obj.get('uuid'),
            "title": obj.get('title'),
            "description": obj.get('description'),
            "created_by": obj.get('created_by'),
            "created_at": obj.get('created_at'),
            "updated_at": obj.get('updated_at')
        }