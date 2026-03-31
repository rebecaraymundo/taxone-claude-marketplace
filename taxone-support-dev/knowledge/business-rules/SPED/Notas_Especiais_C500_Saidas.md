# Notas_Especiais_C500_Saidas

> Fonte: Notas_Especiais_C500_Saidas.doc

Notas com tratamento especial na geração dos sub-blocos C500 e C600 para as saídas: 


MFS/CH	Nome	Descrição		MFS67913	Andréa Rocha	Inclusão da regra para Notas Fiscais de Energia Elétrica Eletrônicas (NF3e) de emissão própria		MFS535348
	Andréa Rocha	Alteração da regra para notas canceladas que possuem modelo igual a “66”.		
Operações de saída
Base: X42 / X43


NF Cancelada
(SITUACAO = ‘S’)
		Escrituração Mastersaf	P1/P2 – a nota é lançada apenas com os dados de identificação (sem os valores)
P8 /P9 – a nota não é considerada na apuração		Regra do Validador	[MFS535348] Inclusão do preenchimento do campo CHV_DOC para modelo 66

Não gerar os filhos do C500
No C500 preencher apenas os campos chave (com exceção do campo COD_PART), e também o IND_OPER, COD_SIT e COD_MOD:
-REG
-IND_OPER
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-SUB 
-NUM_DOC
-DT_DOC
-CHV_DOC (o campo deve ser preenchido quando o código de modelo = ‘66’)
		Gravação do C500 e filhos	Proceder exatamente de acordo com a regra do validador.		Obs	Para o C600 não há tratamento diferenciado a ser feito, pois trata-se de um registro consolidado. Conforme definido no documento de regras, as notas canceladas devem ser consideradas na consolidação, e serão contabilizadas para o preenchimento dos campos 07-QTD_CONS e 08-QTD_CANC do C600.  Para cada nota cancelada que corresponda ao grupamento de notas gravado no C600, deve ser gravado um registro C601 com a sua identificação.

Caso ocorra de num grupo de notas consolidadas do C600, todas estarem canceladas, neste caso, devemos seguir a mesma regra do C500, não gravando os registros filhos C610 (Itens) e C690 (Totais por CST/CFOP/Aliq).		

    Observação sobre nota complementar na SAFX42/SAFX43: no caso das saídas, não existe tratamento diferenciado para as
    notas complementares, por dois motivos:

Não existe regra específica no validador;
O Mastersaf também não tem tratamento especial para as notas da SAF42/SAFX43. O parâmetro “48” não é utilizado na geração dos mapas resumo, além disso, também não existe como identificar esta nota na SAFX42/43 (talvez seja criado um indicador por causa do Sped Fiscal).


[MFS67913] Inclusão da regra para Notas Fiscais de Energia Elétrica Eletrônicas (NF3e) de emissão própria


NF Eletrônica emitida pelo contribuinte 
                                             (COD_MOD = 66 e IND_EMIT = 0)
		Escrituração Mastersaf	Não existe nenhum tratamento especial nos livros		Regra do Validador	Para as NF3e de emissão própria, não será necessário gerar todos os filhos do C500.
		Gravação do C500 e filhos	Proceder exatamente de acordo com a regra do validador.

Deve ser gerado o registro C500, e os “filhos” C590, C591, C595 e C597.
		Obs