# Notas_Especiais_D500_Saidas

> Fonte: Notas_Especiais_D500_Saidas.doc

Notas com tratamento especial na geração dos sub-blocos D500 e D600 para as saídas: 

Operações de saída
Base: X42 / X43


                                                                  NF Cancelada   
                                                               (SITUACAO = ‘S’)
		Escrituração Mastersaf	P1/P2 – a nota é lançada apenas com os dados de identificação (sem os valores)
P8 /P9 – a nota não é considerada na apuração		Regra do Validador	Não gerar os filhos do D500
No D500 preencher apenas os campos chave (com exceção do campo COD_PART), e também o IND_OPER, COD_SIT e COD_MOD:
-REG
-IND_OPER
-IND_EMIT
-COD_MOD
-COD_SIT
-SER
-NUM_DOC
-DT_DOC		Gravação do D500 e filhos	Proceder exatamente de acordo com a regra do validador.		Obs	Para o D600 não há tratamento diferenciado a ser feito, pois trata-se de um registro consolidado. Conforme definido no documento de regras, as notas canceladas não serão consideradas na consolidação (para que os seus valores não interfiram).		

    Observação sobre nota complementar na SAFX42/SAFX43: no caso das saídas, não existe tratamento diferenciado para as
    notas complementares, por dois motivos:

Não existe regra específica no validador;
O Mastersaf também não tem tratamento especial para as notas da SAF42/SAFX43. O parâmetro “48” não é utilizado na geração dos mapas resumo, além disso, também não existe como identificar esta nota na SAFX42/43 (talvez seja criado um indicador por causa do Sped Fiscal).