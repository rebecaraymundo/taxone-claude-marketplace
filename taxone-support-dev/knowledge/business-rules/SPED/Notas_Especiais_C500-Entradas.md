# Notas_Especiais_C500-Entradas

> Fonte: Notas_Especiais_C500-Entradas.doc

Notas com tratamento especial na geração dos sub-blocos C500 e C600 para as entradas: 


MFS/CH	Nome	Descrição		MFS535348
	Andréa Rocha	Alteração da regra para notas canceladas que possuem modelo igual a “66”.		
Notas com tratamento especial na geração dos registros C500 e C590 para as notas de entrada

Operações de entrada
Base: X07 / X08


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
		Gravação do C500 e filhos	Proceder exatamente de acordo com a regra do validador.		Obs		
                                                             NF Complementar
                                                         (IND_SITUACAO_ESP= 5)

O tratamento desta nota nos livros P1/P2/P9 está associado ao parâmetro 48 (“Tratamento das NFs de Complemento de ICMS”)  da parametrização por UF.		Escrituração Mastersaf	P1/P2 - Se o parâmetro 48 estiver ativo, a nota não será apresentada no livro.
P9 - Se o parâmetro 48 estiver ativo, a nota não será considerada p/a apuração.
(Obs: no P8 não existe nenhum tratamento especial p/esta nota)		Regra do Validador	Não consta regra específica sobre nota complementar para o registro C500. 		Gravação do C500 e filhos	Gravar os registros C500 e C590 considerando a regra de escrituração do Mastersaf:

Se o parâmetro 48 estiver ativo, os valores referentes ao ICMS (Base ICMS, ICMS, Base ICMS-ST, ICMS-ST e Base de Redução) não devem ser preenchidos (pois a nota não foi considerada na apuração). 

Se o parâmetro 48 estiver desativado a nota deve ser gerada normalmente, com todos os campos preenchidos. 		Obs	OBS1: Quando esta situação for utilizada, e a nota for gravada sem carregar os valores de ICMS, é  preciso que o código CST seja preenchido corretamente, para evitar críticas do validador. Deve ser utilizado um código de acordo com a escrituração da nota, ou seja, considerando se haverá ou não o crédito/débito (no CT foi utilizado o CST_ICMS = 090).