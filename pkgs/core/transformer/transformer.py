from abc import ABC, abstractmethod

class Transformer(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._includes = {}

    @abstractmethod
    def transform():
        pass

    def set_includes(self, includes):
        self._includes = includes

    def item(self, data, transformer, includes = {}):
        transformer.set_includes(includes)
        return transformer.work(data)

    def collection(self, data, transformer, includes = {}):
        transformer.set_includes(includes)
        result = []
        for datum in data:
            result.append(transformer.work(datum))
        
        return result

    def work(self, data):
        result = { k: v for k, v in self.transform(data).items() if v is not None }


        for include in self._includes:
            include_method = f'include_{include}'
            nested_includes = self._includes[include]
            if(getattr(self, include_method, None)):
                result[include] = getattr(self, include_method)(data)


        return result