# Consistencias_Bloco_X_e_Bloco_Y

> Fonte: Consistencias_Bloco_X_e_Bloco_Y.doc

THOMSON REUTERS

Importação
Bloco X e Bloco Y


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		08/05/2018	MFS-12631	Criação do documento	Alessandra Cristina Navatta		04/10/2018	MFS-21400	Inclusão dos registros X320, X330, X340, X350, X351, X352, X353, X354, X355, X356, X390, X400, X410, X420, X430, X450, X460, X470, X480, X490, X500, X510.	Alessandra Cristina Navatta		08/10/2018	MFS-21400	Inclusão dos registros do Bloco Y ((Y520, Y540, Y550, Y560, Y570, Y580, Y590, Y600, Y612, Y620, Y630, Y640, Y650, Y660, Y671, Y672, Y680, Y681, Y682, Y690, Y720, Y800).	Alessandra Cristina Navatta		
REGRAS DE NEGÓCIO

As regras destacas em amarelo com fonte vermelha não serão desenvolvidas neste momento.

CÓD	DESCRIÇÃO	MFS		RN01	Deverá ser criada uma rotina de importação para o Bloco X e Bloco Y, que será inicializada pela tela Importação (Apuração>> Bloco X e Y – Informações Econômicas e Gerais >> Importação)	MFS-12631		RN02	Estrutura dos Arquivos de Importação:

Normalizada:

Este tipo de arquivo exibe em cada linha um registro.
		RN03	Registros X Campos

A rotina deve contemplar um arquivo que terá um cabeçalho (1ª linha), acrescido de outras linhas (informações dos registros e campos) com a mesma estrutura do layout do arquivo da ECF, conforme regras abaixo:

Cabeçalho do Arquivo:

Campo Obrig.
Descrição Funcional
Origem

*
Código do Registro (0000)
Sistema

*
Estabelecimento (CNPJ)
Sistema

*
Exercício
Sistema

*
Data Inicial
Sistema


Indicador de Exclusão
Sistema


Código dos Registros de Tabela Dinâmica e seus respectivos campos:

X291 
X292 
X390
X400
X460
X470
X480
X490
X500
X510
Y681

Os campos definidos estão contidos na própria tabela dinâmica (código do registro, linha, descrição e valor)

Códigos dos Registros de tabela Interna e seus respectivos campos:
X280
X300
X310
X320
X330
X340 
X350 
X351
X352 
X353 
X354 
X355 
X356 
X410
X420 
X430 
X450
Y520
Y540
Y550
Y560
Y570
Y580
Y590
Y600
Y612
Y620
Y630
Y640
Y650
Y660
Y671
Y672
Y680
Y682
Y690
Y720
Y800

Considerar todos os campos (por registro) informados no documento ‘Validação Bloco X.xlsx’.
	MFS-12631
MFS-21400		RN04	Campos identificadores do registro na mensagem de erro:

Em todos os registros desta importação: 
Devem ser considerados os campos chaves do registro. 

Estas informações estão nos documentos ‘Validacao Bloco X.xlsx’ e ‘Validacao Bloco Y.xlsx’, quando o registro for de origem tabela interna. Caso o registro seja de origem de tabela dinâmica, considerar o campo Código.
	MFS-12631
MFS-21400		RN05	Regras Gerais:

Aplicar a regra RNG00057 - Importação de Arquivos 	MFS-12631		RN06	
Documentos Referencia:

Validacao_Bloco_X.xlsx e Validacao_Bloco_Y.xlsx (validações, campos chaves)
 Layout_ECF.xlsx (coluna nível hierárquico)
Tela_Informacoes_Economicas_e_Gerais.doc (tópico 4 - Permissão de exibição dos registros na tela, definidos do documento).
MTZ_ECF_BlocoX.doc e MTZ_ECF_BlocoY.doc
	MFS-12631
MFS-21400		RN07	Registros Aceitos:

Registros aceitos nesta importação: Bloco X: (X280, X291, X292, X300, X310, X320, X330, X340, X350, X351, X352, X353, X354, X355, X356, X390, X400, X410, X420, X430, X450, X460, X470, X480, X490, X500, X510). Bloco Y:(Y520, Y540, Y550, Y560,Y570,Y580,Y590,Y600,Y612,Y620,Y630,Y640,Y650,Y660,Y671,Y672,Y680,Y681,Y682,Y690,Y720,Y800).	MFS-12631
MFS-21400		RN08	Cabeçalho – Campo Indicador de Exclusão

Lista – Valores Válidos: ‘S’ -  Exclusão e ‘N’- Inclusão.
Aplicar a RNG00028 - Identificação de registros com erro
Aplicar a RNG00021 - Validação de valores dos campos de lista.
Aplicar a RNG00059 - Indicador de exclusão 

Tratamentos:
Um arquivo com o indicador de exclusão = "S", todos os registros que estiverem dentro do arquivo devem ser excluídos da base, se nenhum problema for encontrado no momento da deleção.
- Se no arquivo de importação, com Indicações de Exclusão = ‘S’, conter um registro pai, sem relacionar todos os registros filhos, o sistema não irá excluir o registro pai, devido à dependência com os filhos e nenhum item filho relacionado a este pai será excluído. Neste caso, se um arquivo possuir apenas o registro pai sem os filhos, ou não conter todos os filhos, exibir a mensagem DW00270.
- Um arquivo com Indicador de Exclusão = ‘S’, excluíra um registro pai, e seus registros filhos, quando todos os registros filhos estiverem relacionados no mesmo arquivo. Neste caso, todos os registros (pai e filhos) devem ser excluídos da base.	MFS-12631		

Tela da Importação		RN01	Tela Importação:

A importação será realizada na tela (Título: Importação Blocos X e Y), disponibilizada no caminho Apuração>> Bloco X e Y – Informações Econômicas e Gerais>> Importação. Na tela serão exibidos os campos:

Exercício (Aplicar RNG00010 - Campo Obrigatório, Formato AAAA)
Informação ECF (Aplicar RNG00010 - Campo Obrigatório, Formato: Estabelecimento – CNPJ – Exercício – Data Inicial)
Recuperar todos os registros de Informação ECF, que estão cadastrados com o mesmo ano de exercício informado na tela (campo anterior).
Arquivo (Aplicar RNG00010 - Campo Obrigatório)
Botão Executar (Executa a importação, se todos os campos obrigatórios forem preenchidos)
	MFS-12631		RN02	Visualização dos Registros Importados com Sucesso:

Os registros importados com sucesso, serão vinculados a escrituração que foi indicada no processo de importação, e serão exibidos na tela Apuração>> Bloco X e Y – Informações Econômicas e Gerais >> Manutenção.	MFS-12631		
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN