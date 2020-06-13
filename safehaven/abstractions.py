from abc import ABC, abstractmethod

class CreateConnection(ABC):
    @abstractmethod
    def create_client(self):
        pass

class Listings(ABC):
    @abstractmethod
    def list_objects(self):
        pass  

class Uploader(ABC):
    @abstractmethod
    def upload_objects(self):
        pass

class Downloader(ABC):
    @abstractmethod
    def download_objects(self):
        pass