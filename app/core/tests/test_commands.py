'''
Test custom Django management commmands
'''

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')

class CommandTests(SimpleTestCase):
    '''
    Test custom Django management commmands
    '''
    def test_wait_for_db_ready(self, patched_checked):
        '''
        Test waiting for db when db is available
        '''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            patched_checked.return_value = True
            call_command('wait_for_db')
            patched_checked.assert_called_once_with(database=['default'])
    