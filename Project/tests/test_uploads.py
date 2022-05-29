from includes import*
from app import*

class TestUploads:

    def setup_method(self):
        self.app = CreateApp()
        self.client = self.app.test_client()

    def test_TitleIndex(self):
        response = self.client.get('/')
        print(response, response.data)
        assert b'<title>Upload File</title>' in response.data