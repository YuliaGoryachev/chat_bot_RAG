from unittest import TestCase
from fastapi.testclient import TestClient
from rag_api.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('rag_api', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:rag_api:Starting up ...',
                              'INFO:rag_api:Shutting down ...'])
