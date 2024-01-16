from unittest import TestCase
from fastapi.testclient import TestClient
from app.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('app', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:app:Starting up ...',
                              'INFO:app:Shutting down ...'])
