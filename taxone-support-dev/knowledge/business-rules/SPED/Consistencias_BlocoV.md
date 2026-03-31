# Consistencias_BlocoV

> Fonte: Consistencias_BlocoV.doc

THOMSON REUTERS

Importação
Declaração DEREX - Bloco V


DOCUMENTO DE REQUISITO

Data	MFS	Descrição	Autor		13/08/2018	MFS-20275	Criação do documento	Alessandra Cristina Navatta		
REGRAS DE NEGÓCIO


CÓD	DESCRIÇÃO	MFS		RN01	Deverá ser criada uma rotina de importação para o BlocoV, que será inicializada pela tela Importação (Apuração>> Bloco V -Declaração DEREX >> Importação)
	MFS-20275
		RN02	Estrutura dos Arquivos de Importação:

Normalizada:

Este tipo de arquivo exibe em cada linha um registro.
	MFS-20275
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


Código dos Registros e seus respectivos campos

Registros de Origem de Tabela Interna:
V010
V020
V030
Registros de Origem de Tabela Dinâmica:
V100

Considerar todos os campos (por registro) informados no documento ‘Validacao_Bloco_V.xlsx’.

	MFS-20275		RN04	Campos identificadores do registro na mensagem de erro:

Em todos os registros desta importação: 
Devem ser considerados os campos chaves do registro. 

Estas informações estão no documento ‘Validacao_Bloco_V.xlsx’.
	MFS-20275		RN05	Regras Gerais:

Aplicar a regra RNG00057 - Importação de Arquivos	MFS-20275		RN06	Documentos Referencia:

Validacao_Bloco_V.xlsx (validações, campos chaves)
Layout_ECF.xlsx (coluna nível hierárquico)
Tela_Declaracao_DEREX.doc (tópico 4 - Permissão de exibição dos registros na tela, definidos do documento).
MTZ_ECF_BlocoV.doc 
	MFS-20275		RN07	Cabeçalho – Campo Indicador de Exclusão

Lista – Valores Válidos: ‘S’ -  Exclusão e ‘N’- Inclusão.
Aplicar a RNG00028 - Identificação de registros com erro
Aplicar a RNG00021 - Validação de valores dos campos de lista.
Aplicar a RNG00059 - Indicador de exclusão 

Tratamentos:
Um arquivo com o indicador de exclusão = "S", todos os registros que estiverem dentro do arquivo devem ser excluídos da base, se nenhum problema for encontrado no momento da deleção.
- Se no arquivo de importação, com Indicações de Exclusão = ‘S’, conter um registro pai, sem relacionar todos os registros filhos, o sistema não irá excluir o registro pai, devido à dependência com os filhos e nenhum item filho relacionado a este pai será excluído. Neste caso, se um arquivo possuir apenas o registro pai sem os filhos, ou não conter todos os filhos, exibir a mensagem DW00270.
- Um arquivo com Indicador de Exclusão = ‘S’, excluíra um registro pai, e seus registros filhos, quando todos os registros filhos estiverem relacionados no mesmo arquivo. Neste caso, todos os registros (pai e filhos) devem ser excluídos da base	MFS-20275		

Tela da Importação		Tela Importação:

A importação será realizada na tela (Título: Importação Bloco V), disponibilizada no caminho Apuração>> Bloco V - Declaração DEREX >> Importação. Na tela serão exibidos os campos:

Exercício (Aplicar RNG00010 - Campo Obrigatório, Formato AAAA)
Informação ECF (Aplicar RNG00010 - Campo Obrigatório, Formato: Estabelecimento – CNPJ – Exercício – Data Inicial)
Recuperar todos os registros de Informação ECF, que estão cadastrados com o mesmo ano de exercício informado na tela (campo anterior).
Arquivo (Aplicar RNG00010 - Campo Obrigatório)
Botão Executar (Executa a importação, se todos os campos obrigatórios forem preenchidos)
	MFS-12631		Visualização dos Registros Importados com Sucesso:

Os registros importados com sucesso, serão vinculados a escrituração que foi indicada no processo de importação, e serão exibidos na tela Apuração>> Bloco V - Declaração DEREX >> Manutenção.	MFS-12631		
Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN