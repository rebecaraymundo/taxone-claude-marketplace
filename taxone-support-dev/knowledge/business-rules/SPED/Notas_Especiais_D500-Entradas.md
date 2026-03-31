# Notas_Especiais_D500-Entradas

> Fonte: Notas_Especiais_D500-Entradas.doc

Notas com tratamento especial na geração dos registros D500 e D590 para as notas de entrada

Operações de entrada
Base: X07 / X08


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
-DT_DOC		Gravação do D500 e filhos	Proceder exatamente de acordo com a regra do validador.		Obs		
                                                             NF Complementar
                                                         (IND_SITUACAO_ESP= 5)

O tratamento desta nota nos livros P1/P2/P9 está associado ao parâmetro 48 (“Tratamento das NFs de Complemento de ICMS”)  da parametrização por UF.		Escrituração Mastersaf	P1/P2 - Se o parâmetro 48 estiver ativo, a nota não será apresentada no livro.
P9 - Se o parâmetro 48 estiver ativo, a nota não será considerada p/a apuração.
(Obs: no P8 não existe nenhum tratamento especial p/esta nota)		Regra do Validador	Não consta regra específica sobre nota complementar para o registro D500. 		Gravação do D500 e filhos	Gravar os registros D500 e D590 considerando a regra de escrituração do Mastersaf:

Se o parâmetro 48 estiver ativo, os valores referentes ao ICMS (Base ICMS, ICMS, Base ICMS-ST, ICMS-ST e Base de Redução) não devem ser preenchidos (pois a nota não foi considerada na apuração). 

Se o parâmetro 48 estiver desativado a nota deve ser gerada normalmente, com todos os campos preenchidos. 		Obs	OBS1: Quando esta situação for utilizada, e a nota for gravada sem carregar os valores de ICMS, é  preciso que o código CST seja preenchido corretamente, para evitar críticas do validador. Deve ser utilizado um código de acordo com a escrituração da nota, ou seja, considerando se haverá ou não o crédito/débito (no CT foi utilizado o CST_ICMS = 090).