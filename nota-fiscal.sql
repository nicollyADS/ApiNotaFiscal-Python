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

INSERT INTO NotaFiscal (
    ID, NumeroNota, DataEmissao, NomeEmitente, CNPJCPF_Emitente,
    NomeDestinatario, CNPJCPF_Destinatario, ValorTotal, FormaPagamento,
    Observacoes, ChaveAcesso
)
VALUES (
    1, 12345, '2023-10-10', 'Emitente ABC Ltda', '123456789000101',
    'Destinatario XYZ Ltda', '987654321000102', 1500.50,
    'Cartão de Crédito', 'Observações sobre a nota fiscal',
    '12345678901234567890123456789012345678901234567890'
);

