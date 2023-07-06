import pytest
from unittest import mock
from api_dao import Artistas


def test_criar_artista(mocker):
   
    mock_bd= mock.Mock()
    
    
    mock_bd.criar_artista.return_value = {'nome': 'Artista Teste', 'gravadora_id':1}
    
    api = Artistas(mock_bd)
    
    artista = Artistas.cria_artista(api, 'Artista Teste')
    
    
    assert artista['nome'] == 'Artista Teste'
    mock_bd.criar_artista.assert_called_once_with('Artista Teste')
    
def test_get_artistas(mocker):
    
    mock_bd= mock.Mock()
    
   
    mock_bd.get_artistas.return_value = [
        {'nome': 'Artista 1', 'gravadora_id': 1},
        {'nome': 'Artista 2', 'gravadora_id': 2},
        {'nome': 'Artista 3', 'gravadora_id': 3}
    ]
    
    
    artistas = Artistas.get_artistas(mock_bd)
    
    
    assert len(artistas) == 3
    assert artistas[0]['nome'] == 'Artista 1'
    assert artistas[1]['nome'] == 'Artista 2'
    assert artistas[2]['nome'] == 'Artista 3'
    mock_bd.get_artistas.assert_called_once()
    