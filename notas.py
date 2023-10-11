import oracledb


def get_notas():
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = '''SELECT * FROM NotaFiscal'''
                cur.execute(sql)
                result = cur.fetchall()

            return result
    except Exception as erro:
        print("Não foi possível concluir sua solicitação")
        raise erro
    

def get_nota_by_id(nota_id):
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = 'SELECT * FROM NotaFiscal WHERE id = :nota_id'
                cur.execute(sql, nota_id=nota_id)
                result = cur.fetchone()

            return result
    except Exception as erro:
        print("Não foi possível concluir sua solicitação")
        raise erro
    

def insert_nota(dado):
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = '''insert into NotaFiscal values(
                    :ID, 
                    :NumeroNota,
                    TO_DATE(:DataEmissao, 'DD-MM-YYYY'),
                    :NomeEmitente, 
                    :CNPJCPF_Emitente, 
                    :NomeDestinatario, 
                    :CNPJCPF_Destinatario, 
                    :ValorTotal, 
                    :FormaPagamento,
                    :Observacoes, 
                    :ChaveAcesso )'''
                cur.execute(sql, dado)
            
            con.commit()
    except Exception as erro:
        print("Não foi possível concluir sua solicitação")
        raise erro
    

def update_nota(nota_id, nota_data):
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = '''UPDATE NotaFiscal
                         SET NumeroNota = :NumeroNota,
                            DataEmissao = TO_DATE(:DataEmissao, 'DD-MM-YYYY'),
                            NomeEmitente = :NomeEmitente,
                            CNPJCPF_Emitente = :CNPJCPF_Emitente,
                            NomeDestinatario = :NomeDestinatario,
                            CNPJCPF_Destinatario = :CNPJCPF_Destinatario,
                            ValorTotal = :ValorTotal,
                            FormaPagamento = :FormaPagamento,
                            Observacoes = :Observacoes,
                            ChaveAcesso = :ChaveAcesso
                         WHERE id = :nota_id'''
                nota_data['nota_id'] = nota_id  
                cur.execute(sql, nota_data)
            
            con.commit()
    except Exception as erro:
        print("Não foi possível concluir sua solicitação")
        raise erro
    

def delete_nota(nota_id):
    try:
        with oracledb.connect(
            user='rm552579', 
            password='fiap23',
            dsn='oracle.fiap.com.br/orcl') as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM NotaFiscal WHERE id = :nota_id'
                cur.execute(sql, nota_id=nota_id)
            
            con.commit()
    except Exception as erro:
        print("Não foi possível concluir sua solicitação")
        raise erro
