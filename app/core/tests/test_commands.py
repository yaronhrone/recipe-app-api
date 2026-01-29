"""
Test custom Django management commands.
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_getitem):
        """Test wating for db when db is available."""
        patched_getitem.return_value = True

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)
    @patch('time.sleep')
    def test_wait_for_db_deplay(self, patched_sleep, patched_getitem):
        """Test waiting for db when getting OperationalError."""
        patched_getitem.side_effect = [Psycopg2Error] + \
            [OperationalError] * 5 + [True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)
        