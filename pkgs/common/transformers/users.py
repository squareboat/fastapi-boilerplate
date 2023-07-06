from pkgs.core.transformer import Transformer

class UserTransformer(Transformer):
    def transform(self, obj):
        return {
            "id": obj.get('uuid'),
            "name": obj.get('name'),
            "email": obj.get('email'),
            "created_at": obj.get('created_at'),
            "updated_at": obj.get('updated_at')
        }