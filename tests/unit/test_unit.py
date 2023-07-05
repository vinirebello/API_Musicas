from api_dao import Artistas

def test_cria_artista(mocker):
    mocker.patch("Artistas.cria_artista", return_value="Artista criado: teste")
    resultado = Artistas.cria_artista("teste")
    assert resultado == "Artista criado: teste"
    