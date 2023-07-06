import pytest
from unittest import TestCase
from unittest.mock import patch
from api_dao import Artistas

class myapitest(TestCase):
    def setup(self):
        self.api = Artistas()

@patch('api_dao.Artistas.cria_artistas')
def test_criar_artista(self, mock_artistas):
   
    mock_artistas.return_value = "teste"
    
    resultado = self.api.cria_artistas()
    
    self.assertEqual(resultado, "teste")

 