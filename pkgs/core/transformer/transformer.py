from abc import ABC, abstractmethod
class Transformer(ABC):

    @abstractmethod
    def transform():
        pass

    def collection(self, data):
        result = []
        for datum in data:
            result.append(self.transform(datum))
        
        return result

    def work(self, data):
        result = { k: v for k, v in self.transform(data).items() if v is not None }

        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")]

        return result