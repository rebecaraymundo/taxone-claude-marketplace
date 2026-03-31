# MTZ_EFD_Pre_Geracao_Registro_K280

> Fonte: MTZ_EFD_Pre_Geracao_Registro_K280.docx






THOMSON REUTERS

Módulo Sped Fiscal


Pré-Geração Registro K280



Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré-Geração à Registro K280



DOCUMENTO DE REQUISITO





Sumário

1.	Introdução	3
2.	Parâmetros de Tela	3
3.	Processamento	4
3.1 – Etapa 1: Limpeza dos registros gerados:	4
3.2 - Etapa 2: Geração das Correções de Apontamento (SAFX235)	5



## Introdução


O objetivo é gerar os dados para o registro K280 para os períodos anteriores, a partir do registro carregado para a Tabela das Correções de Apontamento (SAFX235) para o período de referência da correção, utilizando a Data do Estoque Final e o período de apuração para definir quais os meses que devem ser gerados na Tabela das Correções de Apontamento (SAFX235).



## Parâmetros de Tela



Período Referência: [MM/AAAA]


Funcionamento dos campos:




## Processamento




### 3.1 – Etapa 1: Limpeza dos registros gerados:


Tabela: X235_CAPA_COR_APONT – Tabela das Correções de Apontamento da EFD - Bloco K.

- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Período de referência - período informado em tela;
- Tipo de Correção = ‘1’;

- IND_GRAVACAO = '0', '6','7'.

Obs.: Os registros importados que estão no período de referência informado em tela, não podem ser excluídos porque a rotina de pré-geração recupera esses registros para gerar os demais registros de correção para os meses anteriores. Ou seja, não pode ser feita a limpeza dos registros importados para o período de referência.


### 3.2 - Etapa 2: Geração das Correções de Apontamento (SAFX235)


Nesta etapa, a partir das Correções de Apontamento do período, serão geradas as correções para os meses anteriores a partir da Data do Estoque Final até o mês do período de apuração.

Origem dos dados:
- SAFX235 – Tabela das Correções de Apontamento da EFD - Bloco K;


Critérios da recuperação das Correções de Apontamento:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Período de referência – período de referência informado para geração;

- Tipo de Correção igual a “1” (1 - Correção de apontamento de Estoque Escriturado (K200));

- Data Inicial e Final do Período de Apuração <> 0 (datas preenchidas) ou <> 01/01/1900 ;

Obs.: Como os campos Data Inicial e Final do Período de Apuração fazem parte da chave da tabela, eles são gravados com “01/01/1900”, quando não tem informação.  Por esse motivo, essas datas não podem ser consideradas para a rotina de pré-geração.

Recuperar todos os campos da tabela para gravar um novo registro na mesma tabela (SAFX235), com todos os campos iguais, menos a data do Estoque Final.
O número de registros que devem ser gravados, vai depender da quantidade de meses existentes entre a data do Estoque Final e o período de apuração, informados na tabela de Correções de Apontamento.  Devem ser gerados os novos registros decrescendo a data do estoque final até o mês informado no período de apuração.

Exemplo da geração dos registros:



3) Gravação da Tabela:


- Informações da tabela de Correções de Apontamento:


Obs:
1) Os campos NUM_PROCESSO e IND_GRAVACAO existem na tabela definitiva (X235_CAPA_COR_APONT) e não na SAFX235.
2) Caso o registro já exista na base, não atualizar, uma vez que ele foi inserido via manutenção/importação.



= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS594148 | Andréa Rocha | Criação da pré-geração dos dados para o registro K280 | 18/12/2023 |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período Referência | Numérico | S | S | MM/AAAA | Neste campo o usuário informa o período de referência para a recuperação dos dados.  Deve ser um mês válido. |
| Estabelecimentos | Alfanumérico | S | S |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário. |
| Selecionar |  | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos |  | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |


| PK | Item SAFX235 | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa | COD_EMPRESA | Código da Empresa da geração |
| (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do Estabelecimento da geração |
| (*) | 03 | Período de Referência | PERIODO_REF | Período de Referência da geração |
| (*) | 04 | Tipo da Correção | IND_TP_CORRECAO | Tipo da Correção recuperado da tabela |
| (*) | 05 | Indicador do Produto | IND_PRODUTO_OP | Indicador do Produto recuperado da tabela |
| (*) | 06 | Código do Produto | COD_PRODUTO_OP | Código do Produto recuperado da tabela |
| (*) | 07 | Data Inicial do Período de Apuração | DAT_INI_APUR | Data Inicial do Período de Apuração recuperado da tabela |
| (*) | 08 | Data Final do Período de Apuração | DAT_FIM_APUR | Data Final do Período de Apuração recuperado da tabela |
| (*) | 09 | Código da Ordem de Produção/Serviço | COD_OP | Código da Ordem de Produção/Serviço recuperado da tabela |
| (*) | 10 | Código Diferenciador de Produção | COD_DIF_PRODUCAO | Código Diferenciador de Produção recuperado da tabela |
| (*) | 11 | Data do Estoque Final | DAT_ESTQ_FIM | Data do Estoque Final calculada, conforme definição acima |
| (*) | 12 | Grupo de Contagem | GRUPO_CONTAGEM | Grupo de Contagem recuperado da tabela |
| (*) | 13 | Indicador da Pessoa Fis/Jur | IND_FIS_JUR | Indicador da Pessoa Fis/Jur recuperado da tabela |
| (*) | 14 | Código da Pessoa Fis/Jur | COD_FIS_JUR | Código da Pessoa Fis/Jur recuperado da tabela |
|  | 15 | Unidade de Medida | COD_MEDIDA | Unidade de Medida recuperado da tabela |
|  | 16 | Quantidade da Correção | QTD_CORRECAO | Quantidade da Correção recuperado da tabela |
|  | 17 | Correção Positiva/Negativa | IND_POS_NEG | Correção Positiva/Negativa recuperado da tabela |
|  | 18 | Inscrição Estadual – AM | INSC_ESTADUAL | Inscrição Estadual – AM recuperado da tabela |
|  |  | Número do Processo | NUM_PROCESSO | preencher com o número do processo da execução da geração |
|  |  | Indicador de Gravação | IND_GRAVACAO | preencher com ‘6’ |
