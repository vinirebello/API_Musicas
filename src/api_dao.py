from database import Database
from flask import  request, jsonify

class Artistas:
 
    def cria_artista():

        banco = Database.connection
    
        cursor = banco.cursor()

        data = request.json

        nome = data.get('nome')
        gravadora_id = data.get('gravadora_id')

        insert = ('INSERT INTO artistas '
                '(nome, gravadoras_id)'
                ' VALUES ("' + nome + '" ,' + str(gravadora_id) + ');'
                    )
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert

    def get_artistas():
            banco = Database.connection
            cursor = banco.cursor()
            
            select = ('select * from artistas')
            
            #select = ('select a.nome as "nome do artista", m.nome as "nome da musica", g.nome as "nome da gravadora" '
                        # ' from musicas_has_artistas ma '
                        # ' join musicas as m on ma.musicas_id = m.id'
                        # ' join artistas as a on ma.artistas_id = a.id'
                        # ' join gravadoras as g on a.gravadoras_id = g.id order by a.nome asc;')
            
            cursor.execute(select)
            linhas = cursor.fetchall()
            
            resultados = []
            for linha in linhas:
                resultado = {
                'nome da musica': linha[0],
                'nome do artista': linha[1],
                'nome da gravadora': linha[2],
                'created': linha[3],
                'modified': linha[4],
                }
                resultados.append(resultado)
            
            cursor.close()
            return jsonify(resultados)

    def get_artista_id(artista_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _artista = artista_id
        select = ('SELECT artistas.nome AS "Nome do Artista", musicas.nome AS "Nome da Música", gravadoras.nome AS "Nome da Gravadora"'
                    ' FROM musicas'
                    ' INNER JOIN musicas_has_artistas AS mha ON musicas.id = mha.musicas_id'
                    ' INNER JOIN artistas ON artistas.id = mha.artistas_id'
                    ' INNER JOIN gravadoras ON gravadoras.id = artistas.gravadoras_id'
                    ' where artistas.id = '+ str(_artista) + ';')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'nome do Artista': linha[0],
            'nome da musica': linha[1],
            'nome da gravadora': linha[2],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

    def atualiza_artista( artista_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _artista = artista_id
        
        data = request.json
        
        nome = data.get('nome')
        gravadora_id = data.get('gravadora_id')
    
        update = ('UPDATE artistas as a '
                'SET a.nome = "' + nome + '", a.gravadoras_id = ' + str(gravadora_id) + ' WHERE a.id = ' + str(_artista) + ';')
    
        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update

    def delete_artista(artista_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _artista = artista_id
    
        delete = ('DELETE FROM artistas '
                        'WHERE id = ' + str(_artista) + ';')
        
    
        cursor.execute(delete)
        banco.commit()
        cursor.close()
        
        return delete
        
class Clientes:
    
    def cria_cliente():
        
        banco= Database.connection
        cursor = banco.cursor()

        data = request.json

        login = data.get('login')
        senha = data.get('senha')
        planos_id = data.get('plano_id')
        email = data.get('email')

        insert = ('INSERT INTO clientes '
                '(login, senha, planos_id, email)'
                ' VALUES '
                '("' + login +'", "' + senha + '", ' + str(planos_id) + ', "' + email +'");'
                    )
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert, Database.status
        
    def get_clientes():
        banco = Database.connection
        cursor = banco.cursor()
        
        data = request.json
        
        select = ('select id, login, senha, planos_id'
                   ' from clientes'
                    )
                    
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'user_id': linha[0],
            'login': linha[1],
            'senha': linha[2],
            'plano_id': linha[3],
            'email': linha[4]
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

    def pega_cliente_por_id(cliente_id):  
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id
        
        select = ('select id, login, senha, planos_id, email'
                   ' from clientes where id = ' + str(_cliente) + ';')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'user_id': linha[0],
            'login': linha[1],
            'senha': linha[2],
            'plano_id': linha[3],
            'email': linha[4]
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

    def atualiza_cliente(cliente_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id
        
        data = request.json
        
        login = data.get('login')
        senha = data.get('senha')
        planos_id = data.get('plano_id')
        email = data.get('email')
        
        
        update = ('UPDATE clientes as c '
    'SET c.login = "' + login + '", c.senha = "' + senha + '", c.planos_id = ' + str(planos_id) + ', c.email = "' + email + '" '
    'WHERE c.id = ' + str(_cliente) + ';')
            
        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update

        #delete
   
    def deleta_cliente(cliente_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _cliente = cliente_id

        delete = ('DELETE FROM clientes '
                'WHERE id = ' + str(_cliente) + ';')
        
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
                
        return delete

    def cliente_has_musica():  
        banco = Database.connection
        cursor = banco.cursor()
        
        select = ('select c.id as user_id, p.id as plano_id, c.login, p.descricao, p.valor, p.limite, m.nome as nome_musica '
                    'from musicas_has_clientes mc ' 
                    'join clientes c on mc.clientes_id = c.id '
                    'join musicas m on mc.musicas_id = m.id '
                    'join planos p on c.planos_id = p.id order by c.login asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'user_id': linha[0],
            'plano_id': linha[1],
            'login': linha[2],
            'descrição': linha[3],
            'valor': linha[4],
            'limite': linha[5],
            'nome_musica': linha[6],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)

class Generos:

    def cria_generos():
    
            banco = Database.connection
            
            cursor = banco.cursor()

            data = request.json

            descricao = data.get('descricao')
            

            insert = ('INSERT INTO generos '
                    '(descricao)'
                    ' VALUES ("' + descricao + '");'
                        )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert

    def get_generos():
        banco = Database.connection
        cursor = banco.cursor()
        
        select = '(SELECT id, descricao FROM generos)'
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'ID': linha[0],
            'descrição': linha[1],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
    def get_generos_id(genero_id): 
        banco = Database.connection
        cursor = banco.cursor()
        
        _genero = genero_id
        
        select = ('SELECT id, descricao FROM generos where id = ' + str(_genero) +';')
        
        cursor.execute(select)
        linhas = cursor.fetchone()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'ID': linha[0],
            'descrição': linha[1],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
    def att_generos_id(genero_id):
            banco = Database.connection
            cursor = banco.cursor()
            
            _genero = genero_id
            
            data = request.json
            
            descricao = data.get('descricao')
        
            update = ('UPDATE generos AS g '
                    'SET g.descricao = "' + _genero + '";')
        
            cursor.execute(update)
            banco.commit()
            cursor.close()
            
            return update

    def deleta_genero(genero_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _genero = genero_id

        delete = ('DELETE FROM generos '
                    'WHERE id = ' + str(_genero) + ';')
        
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
        
        return delete
    
class Gravadoras:

    def cria_grav():
        banco= Database.connection
    
        cursor = banco.cursor()

        data = request.json

        nome = data.get('nome')
        valor_contrato = data.get('valor-contrato')
        venc_contrato = data.get('venc-contrato')

        insert = ('INSERT INTO gravadoras '
                '(nome, valor_contrato, vencimento_contrato)'
                ' VALUES '
                '("' + nome +'", ' + str(valor_contrato)+ ', ' + str(venc_contrato) + ');'
                )
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert
   
    def pega_grav():
        banco = Database.connection
        cursor = banco.cursor()
        
    
        select = ('SELECT g.id AS gravadora_id, g.nome AS gravadoras, a.id AS artista_id, a.nome AS artistas '
                'FROM artistas AS a '
                'join gravadoras AS g ON g.id = a.gravadoras_id ORDER BY g.id asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'gravadora_id': linha[0],
            'gravadoras': linha[1],
            'artista_id': linha[2],
            'artistas': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)   
    
    def pega_grav_por_id(gravadora_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _gravadora = gravadora_id
        
        select = ('SELECT g.id AS gravadora_id, g.nome AS gravadoras, a.id AS artista_id, a.nome AS artistas '
                'FROM artistas AS a '
                'join gravadoras AS g ON g.id = a.gravadoras_id WHERE g.id = ' + str(gravadora_id) + ' ORDER BY g.id asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'gravadora_id': linha[0],
            'gravadoras': linha[1],
            'artista_id': linha[2],
            'artistas': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
   
    def atualiza_grav(gravadora_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _gravadora = gravadora_id
        
        data = request.json
        
        nome = data.get('nome')
        valor_contrato = data.get('valor_contrato')
        vencimento = data.get('vencimento')

        update = ('UPDATE gravadora AS g '
                'SET g.nome = "' + nome + '", g.valor_contrato = ' + str(valor_contrato) + ', vencimento_contrato = "' + str(vencimento) + '" '
                'WHERE g.id = ' + + ';')

        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update
  
    def deleta_grav(gravadora_id):
                
                banco = Database.connection
                cursor = banco.cursor()
                
                _gravadora = gravadora_id
            
                delete = ('DELETE FROM gravadoras '
                            'WHERE id = ' + str(_gravadora) + ';')
                
            
                cursor.execute(delete)
                banco.commit()
                cursor.close()
                
                return delete
    
class Musicas:

    def cria_musica():
        
            banco= Database.connection
        
            cursor = banco.cursor()

            data = request.json

            nome = data.get('nome')
            duracao = data.get('duracao')
            genero_id = data.get('genero_id')
            lancamento = data.get('lancamento')

            insert = ('INSERT INTO musicas '
                    '(nome, generos_id, duracao, lancamento)'
                    ' VALUES '
                    '("' + nome + '", ' + str(duracao) +  ', ' +  str(genero_id) +  ', ' + str(lancamento) + ');'
                    )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert
        
    def pega_musica():
        banco = Database.connection
        cursor = banco.cursor()
        
        select = ('select m.nome as "nome da musica", a.nome as "nome do artista", g.nome as "nome da gravadora", m.duracao '
                    ' from musicas_has_artistas ma '
                    ' join musicas as m on ma.musicas_id = m.id'
                    ' join artistas as a on ma.artistas_id = a.id'
                    ' join gravadoras as g on a.gravadoras_id = g.id order by a.nome asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'nome_musica': linha[0],
            'nome_artista': linha[1],
            'nome_gravadora': linha[2],
            'duração': linha[3]
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
        
    def pega_musica_por_id(musica_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _musica = musica_id
        
        select = ('select m.nome as "nome da musica", a.nome as "nome do artista", g.nome as "nome da gravadora", m.duracao '
                    ' from musicas_has_artistas ma '
                    ' join musicas as m on ma.musicas_id = m.id'
                    ' join artistas as a on ma.artistas_id = a.id'
                    ' join gravadoras as g on a.gravadoras_id = g.id where m.id = ' + str(musica_id) +' order by a.nome asc;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultado = []
        for linha in linhas:
            resultados = {
            'nome_musica': linha[0],
            'nome_artista': linha[1],
            'nome_gravadora': linha[2],
            'duracao': linha[3],
            }
            resultado.append(resultados)
        
        return jsonify(resultado)
   
    def atualiza_musica(musica_id):
                banco = Database.connection
                cursor = banco.cursor()
                
                _musica = musica_id
                
                data = request.json
                
                nome_musica = data.get('nome_musica')
                duracao = data.get('duracao')
                generos_id = data.get('generos_id')
                lancamento = data.get('lancamento')
            
                update = ('UPDATE musicas AS m '
            'SET m.nome = "' + nome_musica + '", m.duracao = "' + duracao + '", m.generos_id = ' + str(generos_id) + ', m.lancamento = "' + str(lancamento) + '" '
            'WHERE m.id = ' + str(_musica) + ';')
                
                cursor.execute(update)
                banco.commit()
                cursor.close()
                
                return update

    def deleta_musica(musica_id):
        banco = Database.connection
        
        cursor = banco.cursor()

        _musica = musica_id

        delete = ('DELETE FROM musicas as m '
                    'WHERE m.id = ' + str(_musica) + ';')


        cursor.execute(delete)
        banco.commit()
        cursor.close()

        return delete
    
class Planos:
    
    def cria_plano():
    
            banco= Database.connection
        
            cursor = banco.cursor()

            data = request.json

            descricao = data.get('descricao')
            valor = data.get('valor')
            limite = data.get('limite')
            
            insert = ('INSERT INTO planos '
                    '(descricao, valor, limite)'
                    ' VALUES'
                    '("' + descricao +'", ' + str(valor) + ', ' + str(limite) +');'
                        )
            cursor.execute(insert)
            banco.commit()
            cursor.close()
            
            return insert, Database.status
        
    def pega_plano():
        banco = Database.connection
        cursor = banco.cursor()
        
        select = ('SELECT id, descricao, valor, limite FROM planos;')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultados = []
        for linha in linhas:
            resultado = {
            'id': linha[0],
            'descricao': linha[1],
            'valor': linha[2],
            'limite': linha[3]
            }
            resultados.append(resultado)
        
        return jsonify(resultados)
        
    def pega_plano_por_id(plano_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _plano = plano_id
        
        select = ('SELECT id, descricao, valor, limite '
                'FROM planos as p WHERE p.id =' + str(_plano) + ';')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultados = []
        for linha in linhas:
            resultado = {
            'id': linha[0],
            'descricao': linha[1],
            'valor': linha[2],
            'limite': linha[3]
            }
            resultados.append(resultado)
        
        return jsonify(resultados)

    def atualiza_plano( plano_id):
                banco = Database.connection
                cursor = banco.cursor()
                
                _plano = plano_id
                
                data = request.json
                
                descricao = data.get('descricao')
                valor = data.get('valor')
                limite = data.get('limite')
            
                update = ('UPDATE planos as p '
            'SET p.descricao = "' + descricao + '", p.valor = ' + str(valor) + ', p.limite = ' + str(limite) +  ' '
            'WHERE p.id = ' + str(_plano) + ';')
                
                cursor.execute(update)
                banco.commit()
                cursor.close()
                
                return update

    def deleta_plano(plano_id):
        banco = Database.connection
        
        cursor = banco.cursor()

        _plano = plano_id

        delete = ('DELETE FROM planos as p '
                    'WHERE p.id = ' + str(_plano) + ';')


        cursor.execute(delete)
        banco.commit()
        cursor.close()

        return delete
    
 #'select a.nome as "nome do artista", m.nome as "nome da musica", g.nome as "nome da gravadora" '

class Musica_has_artistas:
    
    def cria_mha():
        
        banco = Database.connection
        
        cursor = banco.cursor()
        
        data = request.json
        musica_id = data.get('musicas_id')
        artistas_id = data.get('artistas_id')
        
        insert = ('INSERT INTO musicas_has_artistas '
                  '(musica_id, artistas_id)'
                  ' VALUES ("' + str(musica_id) + '",' + str(artistas_id) + ');'
                    )
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert
    
    def get_mha():
        
        banco = Database.connection
        
        cursor = banco.cursor()
        
        select = ('select * from musicas_has_artistas')
        
        
        
        cursor.execute(select)
        Linhas = cursor.fetchall()
        
        resultados = []
        for linha in Linhas:
            resultado = {
                'mha_id':linha[0],
                'musicas_id': linha [1],
                'artistas_id': linha [2]
            }
            resultados.append(resultado)
        
        cursor.close()
        return jsonify(resultados)
        
    def get_mha_id(mha_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _mha = mha_id
        select = ('SELECT mha.id, mha.musicas_id, mha.artistas_id'
                  'FROM musicas_has_artistas mha'
                  'WHERE mha.id = ' + str(_mha) + ';')
        
        cursor.execute(select)
        linhas = cursor.fetchall
        
        resultado = []
        for linha in linhas:
            resultados = {
                'musicas_id': linha[0],
                'artistas_id': linha[1]
            }
            resultados.append(resultado)
        return jsonify(resultados)
    
    def atualiza_mha(mha_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        mha_id = mha_id
        
        data = request.json
        
        musica_id = data.get('musicas_id')
        artista_id = data.get('artista_id')
        
        update = ('UPDATE musicas_has_artistas as mha'
                  'SET mha.musica_id = "' + str(musica_id) + '", mha.artsitas_id = ' + str(artista_id) + ' WHERE mha.id = ' + str(mha_id) + ';')
        
        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update
        
    def deleta_mha_id(mha_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _mha = mha_id
        
        delete = ('DELETE FROM musicas_has_artistas mha'
                  'WHERE mha.id = ' + str(_mha) + ';')
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
        
        return delete

class Musica_has_clientes:
    def cria_mhc():

        banco = Database.connection
        
        cursor = banco.cursor()
        
        data = request.json
        musicas_id = data.get('musicas_id')
        clientes_id = data.get('clientes_id')
        
        insert = ('INSERT INTO musicas_has_clientes '
                  '(musica_id, clientes_id)'
                  'VALUES ("' + str(musicas_id) + '", ' + str(clientes_id) + ');'
                    )
        
        cursor.execute(insert)
        banco.commit()
        cursor.close()
        
        return insert
            
    def get_mhc():
    
        banco = Database.connection
        
        cursor = banco.cursor()
        
        select = ('SELECT * FROM musicas_has_clientes')
        
        cursor.execute(select)
        linhas = cursor.fetchall()
        resultados = []
        for linha in linhas:
            resultado = {
                'mhc.id' : linha[0],
                'musicas_id': linha[1],
                'clientes_id': linha[2]
            }
            resultados.append(resultado)
            
        cursor.close()
        return jsonify(resultados)
    
    def get_mhc_id(mhc_id):
        
        banco = Database.connection
        cursor = banco.cursor()
        
        _mhc = mhc_id
        
        select = ('SELECT mhc.id, musicas_id, clientes_id'
                  'FROM musicas_has_clientes mhc'
                  'WHERE mhc.id = ' + str(_mhc) + ';')

        cursor.execute(select)
        linhas = cursor.fetchall()
        
        resultados = []
        for linha in linhas:
            resultado = {
                'musicas_id': linha[0],
                'clientes_id': linha[1]
            }
            resultados.append(resultado)
        return jsonify(resultados)
                  
    def atualiza_mhc(mhc_id):
         
        banco = Database.connection
        cursor = banco.cursor()
        
        _mhc = mhc_id
        
        data = request.json
        
        musicas_id = data.get('musicas_id')
        clientes_id = data.get('clientes_id')
        
        update = ('UPDATE musicas_has_clientes mhc'
                  'SET  mhc.musicas_id = "' + str(musicas_id) + '", mhc.clientes_id = ' + str(clientes_id) + ' WHERE mhc.id = ' + str(_mhc) + ';')
        
        cursor.execute(update)
        banco.commit()
        cursor.close()
        
        return update
    
    def deleta_mhc_id(mhc_id):
        banco = Database.connection
        cursor = banco.cursor()
        
        _mhc = mhc_id
        
        delete = ('DELETE FROM musica_has_clientes mhc'
                  'WHERE mhc.id = ' + str(_mhc) + ';')
        
        cursor.execute(delete)
        banco.commit()
        cursor.close()
        
        return delete
# ' from musicas_has_artistas ma '
# ' join musicas as m on ma.musicas_id = m.id'
# ' join artistas as a on ma.artistas_id = a.id'
# ' join gravadoras as g on a.gravadoras_id = g.id order by a.nome asc;'

    
       