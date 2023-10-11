CREATE TABLE NotaFiscal (
    ID NUMBER(10) PRIMARY KEY, 
    NumeroNota NUMBER(10) NOT NULL, 
    DataEmissao DATE NOT NULL, 
    NomeEmitente VARCHAR2(255) NOT NULL, 
    CNPJCPF_Emitente VARCHAR2(18) NOT NULL, 
    NomeDestinatario VARCHAR2(255) NOT NULL, 
    CNPJCPF_Destinatario VARCHAR2(18) NOT NULL, 
    ValorTotal FLOAT NOT NULL, 
    FormaPagamento VARCHAR2(50) NOT NULL,
    Observacoes VARCHAR2(70) NOT NULL, 
    ChaveAcesso VARCHAR2(50) NOT NULL
);

SELECT * FROM NotaFiscal;

