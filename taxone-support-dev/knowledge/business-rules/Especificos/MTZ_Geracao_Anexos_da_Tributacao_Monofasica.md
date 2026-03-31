# MTZ_Geracao_Anexos da Tributação Monofásica

> Fonte: MTZ_Geracao_Anexos da Tributação Monofásica.docx





Combustíveis e Derivados de Petróleo

Geração dos Anexos da Tributação Monofásica para Distribuidoras


Localização: Específicos à Combustíveis e Derivados de Petróleo,
Menu: Movimento Distribuidora  Geração  Anexos da Tributação Monofásica  Geração





Quadro de Revisões








## Introdução


Essa funcionalidade permite a geração dos Anexos que atendem a Tributação Monofásica para as Distribuidoras.

## Base Legal:

Ato Cotepe ICMS nº 22/23 para Diesel
Ato Cotepe ICMS n° 44/23 para Gasolina


## Pré-Requisitos:

- Importação da TACES 114.

- Cadastro dos Grupos de Combustível e Derivados:
- Localização: Menu Específicos  Combustíveis e Derivados de Petróleo
- Menu: Parâmetros  Grupos de Combustíveis e Derivados

- Realizar o cadastro de todos os combustíveis tomando como base os Códigos de Produtos presentes no manual do SCANC-CTB (tópico 4.3). Veja a relação de todos os grupos combustíveis:

- Exemplo de Cadastro para Grupo de combustível e Derivados


- O campo “Grupo Combustível” é um código livre.
- O campo Descrição será utilizado para o Anexo III-M.
- O campo “Produto SEF” deve ser preenchido com Códigos de Produtos presentes no manual do SCANC-CTB (tópico 4.3).
- Todos os produtos do Diesel e Gasolina devem estar com indicador I-M, II-M e III-M marcados para que os respectivos anexos sejam gerados.

- Parametrização dos Produtos x Grupos de Combustíveis e Derivados
- Localização: Menu Específicos  Combustíveis e Derivados de Petróleo
- Menu: Parâmetros  Produtos x Grupos de Combustíveis e Derivados

- Relacionar os produtos (SAFX2013) aos Grupos de Combustíveis informando a unidade de medida em que a quantidade do combustível deve ser informada nos anexos. Exemplo: Diesel e Gasolina em litros.
- Campos que não serão utilizados na geração dos anexos: Fator Conv. Gas. A, Fator Divisão do Vlr. Unitário Produto A, Fator de Ganho, Fator de Perda.

- Essa parametrização também pode ser importada através da SAFX96.

- Parametrização CFOP ou CFOP/Natureza de Operação
- Localização: Menu Específicos  Combustíveis e Derivados de Petróleo
- Menu: Parâmetros > Anexos I, II, III, IV, V, VI e VIII> Por CFOP ou Por Extensão de CFOP

- Cadastre os CFOPs do item de mercadoria para operações de saídas, entradas ou devoluções.

- Parametrização Pessoa Física/Jurídica por Ramo de Atividade
- Localização: Módulo Básicos > Data Warehouse
- Menu Manutenção > Cadastros Parâmetros > Pessoa Física/Jurídica por Ramo de Atividade

- Configure a classificação da atividade para os fornecedores de combustíveis, indicando suas categorias como refinaria, formulador, importador, etc.

- Esse cadastro também pode ser importado através da SAFX45.

- Conversão de Unidade de Medida
- Localização: Módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida > Padrão ou Por Produto

- Cadastre as medidas presentes nas movimentações de nota fiscal para a medida cadastrada na Parametrização dos Produtos x Grupos de Combustíveis e Derivados.

- Importação SAFX07, SAFX08 e SAFX325 para o estabelecimento e período da geração




## Parâmetros de Tela


Mês/Ano Referência :                 [ dd/aaaa ]

Anexos:
[ ] I-M
[ ] II-M
[ ] III-M
[ ] IV-MB

Combustíveis:
[ ] Diesel - DSL, BXD, S10 e BXS
[ ] Diesel Marítimo - DSM
[ ] Gasolina - GSL e GSC
[ ] Gasolina Premium - GSP e GCP
[ ] Gasolina de Aviação – GSV
[ ] Álcool Etílico Anidro - AEA


Pesquisa UF (Estabelecimento): [ *Todas *                              \/]

Estabelecimentos:     [ ] Selecionar [ ] Marcar Todos
[ x ] xx - xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[ y ] xx - xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[    ] xx - xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:




## Regras de Negócio


### RN00 – Regras de Consistências


Ao acionar a geração, realizar as validações abaixo e prosseguir com a geração dos anexos.

- Cadastro do “Grupo de Combustível e Derivados”:
- Validar Cadastro do “Grupo de Combustível e Derivados” para o Anexo escolhido na tela de geração:
- Para cada Anexo (I-M, II-M, III-M, IV-MB) selecionado na tela de geração, verificar se existe Grupo de Combustível cadastrado em Cadastro de “Grupo de Combustível e Derivados” (tabela CBT_GRP_COMB).
- Para isso realizar a consulta na tabela CBT_GRP_COMB com os seguintes critérios:
- IND_ANEXO1M = ‘S’, quando opção do Anexo I-M for selecionada na tela de geração
- IND_ANEXO2M = ‘S’, quando opção do Anexo II-M for selecionada na tela de geração
- IND_ANEXO3M = ‘S’, quando opção do Anexo III-M for selecionada na tela de geração
- IND_ANEXO3M = ‘S’, quando opção do Anexo III-M for selecionada na tela de geração
- IND_ANEXO4MB = ‘S’, quando opção do Anexo IV-M for selecionada na tela de geração

- Caso não exista exibir a seguinte mensagem de aviso no log da geração:
- Não foi cadastrado Grupo de Combustível para geração do Anexo xxx.
- Acesse o Cadastro do Grupo de Combustível e Derivados no menu Parâmetros, inclua o grupo combustível preenchendo o campo Produto SEF conforme tabela 4.3 do manual de orientação do SCANC CTB e indique os anexos para geração.
- Onde xxx é a identificação do anexo: I-M, II-M, III-M, IV-MB.

- Validar Cadastro do “Grupo de Combustível e Derivados” para o Combustível escolhido na tela de geração:
- Para a opção de Combustível selecionada na tela de geração (ex: “Diesel - DSL, BXD, S10 e BXS”, “Gasolina - GSL e GSC”, “BioCombustível – AEA”), recuperar na TACES114 – “Grupamento dos Combustíveis para Composição dos Anexos Monofásicos”, os Códigos de Produto SEF relacionados, que são considerados na geração do Anexo.
- Para isso realizar consulta na tabela CBT_PROD_SEF_CENTR (TACES114) com os seguintes critérios:
- COD_ANEXO = ‘1M’ quando opção do Anexo I-M for selecionada na tela de geração
- = ‘2M’ quando opção do Anexo II-M for selecionada na tela de geração
- = ‘3M’ quando opção do Anexo III-M for selecionada na tela de geração
- = ‘4MB’ quando opção do Anexo IV-M for selecionada na tela de geração
- COD_PROD_SEF_CENTR = ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel - DSL, BXD, S10 e BXS”
- = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo - DSM”
- = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina - GSL e GSC”
- = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium - GSP e GCP”
- = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação - GSV”
- = ‘AEA’ , p/ opção de Combustível selecionada na tela de geração for “Álcool Etílico Anidro - AEA”
- Recuperar COD_PROD_SEF.

- Obs: essa consulta pode recuperar mais de um registro. Ex: para o COD_PROD_SEF_CENTR = DSL, o resultado da consulta são dois registros DSL e BXD.

- Para cada Código de Produto SEF recuperado na consulta acima, verificar se existe Grupo de Combustível no Cadastro de “Grupo de Combustível e Derivados” (tabela CBT_GRP_COMB) com campo COD_PROD_SEF preenchido.
- Para isso realizar a consulta na tabela CBT_GRP_COMB com os seguintes critérios:
- COD_PROD_SEF = COD_PROD_SEF recuperado
- Caso não exista exibir a seguinte mensagem de aviso no log da geração:
- Não foi cadastrado Grupo de Combustível referente ao COD_PROD_SEF.
- Acesse o Cadastro do Grupos de Combustíveis e Derivados no menu Parâmetros e inclua o grupo combustível preenchendo o campo Produto SEF com COD_PROD_SEF e indique os anexos para geração.

- Caso exista, verificar se o indicador do Anexo I-M ou II-M ou III-M foi marcado no cadastro. Considerar os campos IND_ANEXO1M, IND_ANEXO2M e IND_ANEXO3M da tabela CBT_GRP_COMB.

- Se a opção do Anexo I-M for selecionada na tela de geração e o campo IND_ANEXO1M recuperado for diferente de ‘S’, exibir a seguinte mensagem de aviso no log da geração:
- O Grupo de Combustível COD_GRP_COMB referente ao COD_PROD_SEF foi cadastrado sem indicação de geração do Anexo I-M. Acesse o Cadastro do Grupo de Combustível e Derivados no menu Parâmetros, e reveja a indicação dos anexos para geração.

- Se a opção do Anexo II-M for selecionada na tela de geração e o campo IND_ANEXO2M recuperado for diferente de ‘S’, exibir a seguinte mensagem de aviso no log da geração:
- O Grupo de Combustível COD_GRP_COMB referente ao COD_PROD_SEF foi cadastrado sem indicação de geração do Anexo II-M. Acesse o Cadastro do Grupo de Combustível e Derivados no menu Parâmetros, e reveja a indicação dos anexos para geração.

- Se a opção do Anexo III-M for selecionada na tela de geração e o campo IND_ANEXO3M recuperado for diferente de ‘S’, exibir a seguinte mensagem de aviso no log da geração:
- O Grupo de Combustível COD_GRP_COMB referente ao COD_PROD_SEF foi cadastrado sem indicação de geração do Anexo III-M. Acesse o Cadastro do Grupo de Combustível e Derivados no menu Parâmetros, e reveja a indicação dos anexos para geração.

- Parametrização de “Produtos x Grupo de Combustível e Derivados”
- Validar a Parametrização de “Produtos x Grupo de Combustível e Derivados” para o Anexo escolhido na tela de geração:
- Para cada Anexo (I-M, II-M, III-M, IV-MB) selecionado na tela de geração, recuperar do Cadastro de “Grupo de Combustível e Derivados” (tabela CBT_GRP_COMB), os Grupos Combustíveis referentes ao indicador do Anexo marcado.
- Para isso realizar a consulta na tabela CBT_GRP_COMB com os seguintes critérios:
- IND_ANEXO1M = ‘S’, quando opção do Anexo I-M for selecionada na tela de geração
- IND_ANEXO2M = ‘S’, quando opção do Anexo II-M for selecionada na tela de geração
- IND_ANEXO3M = ‘S’, quando opção do Anexo III-M for selecionada na tela de geração
- IND_ANEXO4MB = ‘S’, quando opção do Anexo IV-M for selecionada na tela de geração

- Para cada Grupo Combustível recuperado acima, verificar se existe parametrização de “Produtos x Grupo de Combustível e Derivados” (SAFX96).
- Para isso realizar uma consulta na tabela X96_GRP_COMB_PROD com os seguintes critérios:
- IDENT_GRP_COMB = Identificador do Grupo de Combustível recuperado da CBT_GRP_COMB.
- VALID_GRP_COMB_PROD <= último dia do mês/ano informado na tela de geração

- Caso não exista exibir a seguinte mensagem de aviso no log da geração:
- Falta parametrização de Produto x Grupo de Combustível para o Grupo de Combustível COD_GRP_COMB referente ao COD_PROD_SEF.
- Acesse a opção Produtos x Grupo de Combustível e Derivados disponível no menu Parâmetros, e relacione os produtos ao grupo combustível e informe a unidade de medida em que a quantidade deve ser apresentada nos anexos. Essa parametrização também pode ser importada através da SAFX96.

- Validar a Parametrização de “Produtos x Grupo de Combustível e Derivados” para o Combustível escolhido na tela de geração:
- Para as opções de Combustíveis selecionadas na tela de geração (ex: “Diesel - DSL, BXD, S10 e BXS”, “Gasolina - GSL e GSC”, “BioCombustível – AEA”), realizar a consistência da parametrização do “Produto x Grupo de Combustível e Derivados”:

- Para a opção de Combustível selecionada na tela de geração (ex: “Diesel - DSL, BXD, S10 e BXS”, “Gasolina - GSL e GSC”, “BioCombustível – AEA”), recuperar na TACES114 – “Grupamento dos Combustíveis para Composição dos Anexos Monofásicos”, os Códigos de Produto SEF relacionados, que são considerados na geração do Anexo.
- Para isso realizar consulta na tabela CBT_PROD_SEF_CENTR (TACES114) com os seguintes critérios:
- COD_ANEXO = ‘1M’ quando opção do Anexo I-M for selecionada na tela de geração
- = ‘2M’ quando opção do Anexo II-M for selecionada na tela de geração
- = ‘3M’ quando opção do Anexo III-M for selecionada na tela de geração
- = ‘4MB’ quando opção do Anexo IV-M for selecionada na tela de geração
- COD_PROD_SEF_CENTR = ‘DSL’, p/ opção de Combustível selecionada na tela de geração for “Diesel - DSL, BXD, S10 e BXS”
- = ‘DSM’, p/ opção de Combustível selecionada na tela de geração for “Diesel Marítimo - DSM”
- = ‘GSL’, p/ opção de Combustível selecionada na tela de geração for “Gasolina - GSL e GSC”
- = ‘GSP’, p/ opção de Combustível selecionada na tela de geração for “Gasolina Premium - GSP e GCP”
- = ‘GSV’, p/ opção de Combustível selecionada na tela de geração for “Gasolina de Aviação - GSV”
- = ‘AEA’ , p/ opção de Combustível selecionada na tela de geração for “Álcool Etílico Anidro - AEA”

- Recuperar COD_PROD_SEF.

- Obs: essa consulta pode recuperar mais de um registro. Ex: para o COD_PROD_SEF_CENTR = DSL, o resultado da consulta são dois registros DSL e BXD.

- Para cada Código de Produto SEF recuperado na consulta acima, consultar o Cadastro de “Grupo de Combustível e Derivados” (tabela CBT_GRP_COMB) para recuperar o Grupo Combustível.
- Para isso realizar a consulta na tabela CBT_GRP_COMB com os seguintes critérios:
- COD_PROD_SEF = COD_PROD_SEF recuperado
- Recuperar o Identificador do Grupo Combustível (IDENT_GRP_COMB).

- Para o Grupo Combustível recuperado acima, verificar se existe parametrização de “Produtos x Grupo de Combustível e Derivados” (SAFX96).
- Para isso realizar uma consulta na tabela X96_GRP_COMB_PROD com os seguintes critérios:
- IDENT_GRP_COMB = Identificador do Grupo de Combustível recuperado da CBT_GRP_COMB.
- VALID_GRP_COMB_PROD <= último dia do mês/ano informado na tela de geração

- Caso não exista exibir a seguinte mensagem de aviso no log da geração:
- Falta parametrização de Produto x Grupo de Combustível para o Grupo de Combustível COD_GRP_COMB referente ao COD_PROD_SEF.
- Acesse a opção Produtos x Grupo de Combustível e Derivados disponível no menu Parâmetros, e relacione os produtos ao grupo combustível e informe a unidade de medida em que a quantidade deve ser apresentada nos anexos. Essa parametrização também pode ser importada através da SAFX96.


- Cadastro do Estabelecimento x Pessoa Física/Jurídica
Verificar se o estabelecimento selecionado para geração possui Pessoa Física/Jurídica que a represente, no “Cadastros de Estabelecimentos x Pessoas Física/Jurídica” disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Estabelecimentos x Pessoas Física/Jurídica;
Tabela: DWT_PFJ_ESTAB
Caso esse cadastro não exista, exibir a seguinte mensagem de aviso no log da geração:
- Faltou cadastrar Pessoa Física/Jurídica relativa ao Estabelecimento. Acessar opção Estabelecimentos x Pessoas Física/Jurídica, disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Estabelecimentos x Pessoas Física/Jurídica;

- Cadastro de Pessoa Física/Jurídica por Ramo de Atividade
Verificar a Pessoa Física/Jurídica que foi relacionada ao estabelecimento, possui Cadastro de Pessoa Física Jurídica por Ramo de Atividade, disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros Parâmetros > Pessoa Física/Jurídica por Ramo de Atividade.
Tabela: PRT_PFJ_MSAF;
Caso esse cadastro não exista, exibir a seguinte mensagem de aviso no log da geração:
- Faltou cadastrar o Ramo de Atividade da Pessoa Física/Jurídica relacionada ao Estabelecimento. Acessar opção Pessoa Física/Jurídica por Ramo de Atividade, disponível no Módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros Parâmetros > Pessoa Física/Jurídica por Ramo de Atividade;

### RN01 - Geração do Anexo I-M


Ver documento matriz MTZ_Geracao_Anexos I-M.docx


### RN02 - Geração do Anexo II-M


Ver documento matriz MTZ_Geracao_Anexos II-M.docx

### RN03 - Geração do Anexo III-M


Ver documento matriz MTZ_Geracao_Anexos III-M.docx

### RN04 - Geração do Anexo IV-MB


Ver documento matriz MTZ_Geracao_Anexos IV-MB.docx


| Data | OS / Chamado | Descrição | Responsável |
| --- | --- | --- | --- |
| 28/04/2025 | MFS772704 | Geração do Anexo I-M para produtos com tributação monofásica. | Liliane Assaf |
| 29/09/2025 | MFS772738 | Geração do Anexo I-M para produtos com tributação monofásica. | Graciela Soares |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


| Grupo Combustível | Descrição | Produto SEF | I-M | II-M | III-M | IV-M |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Diesel A | DSL | Sim | Sim | Sim | Não |
| 02 | Diesel B | BXD | Sim | Sim | Sim | Si m |
| 03 | Gasolina A | GSL | Sim | Sim | Sim | Não |
| 04 | Gasolina C | GSC | Sim | Sim | Sim | Não |
| 05 | Diesel A S10 | S10 | Sim | Sim | Sim | Não |
| 06 | Diesel B S10 | BXS | Sim | Sim | Sim | Não |
| 07 | Gasolina A Premium | GSP | Sim | Sim | Sim | Não |
| 08 | Gasolina C Premiun | GCP | Sim | Sim | Sim | Não |
| 09 | Álcool Etílico Anidro | AEA | Não | Não | Não | Sim |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Mês/Ano Referência | Data (mês e ano) | S | S | (MM/AAAA) | Neste campo será informado o período (mês e ano) para a geração dos lançamentos Deve ser um mês válido.  Default: Apresentar o mês/ano anterior ao mês/ano do dia da execução.  Crítica Se o período não for informado exibir mensagem de erro:     Informe o Mês/Ano Referência |
| Anexos | Anexos | Anexos | Anexos | Anexos | Anexos |
| Anexo I-M | Check-box | N | S | Default Desmarcado |  |
| Anexo II-M | Check-box | N | S | Default Desmarcado |  |
| Anexo III-M | Check-box | N | S | Default Desmarcado | Crítica: Pelo menos um dos Anexos deve ser selecionado (I-M ou II-M ou III-M). Caso nenhum Anexo tenha sido selecionado, exibir mensagem de erro no log da geração e abortar o processo de geração:     Informar o Anexos para geração. |
| Anexo IV-M | Check-box | N | S | Default Desmarcado |  |
| Combustíveis | Combustíveis | Combustíveis | Combustíveis | Combustíveis | Combustíveis |
| Diesel - DSL, BXD, S10 e BXS | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: I-M ou II-M ou III-M |
| Diesel Marítimo – DSM | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: I-M ou II-M ou III-M |
| Gasolina - GSL e GSC | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: I-M ou II-M ou III-M |
| Gasolina Premium - GSP e GCP | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: I-M ou II-M ou III-M |
| Gasolina de Aviação - GSV | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: I-M ou II-M ou III-M  Crítica: Pelo menos um dos Combustíveis deve ser selecionado, caso contrário, exibir mensagem de erro no log da geração e abortar o processo de geração:     Informar o Combustível para geração. |
| Álcool Etílico Anidro - AEA | Check-box | N | S | Default Desmarcado | Habilitar a opção quando um dos Anexos for selecionado: IV-M |
| Pesquisa UF (Estabelecimento) | Lista | S | S | Default “Todos” | Este campo é composto pelos códigos de Unidades Federativas oriundas da tabela Estado. Adicionar à lista o item “Todos”. Servirá para filtro dos estabelecimentos apresentados para seleção. |
| Estabelecimentos | Multi-seleção | S | S |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login.  Apresentar os estabelecimentos de acordo com a UF selecionada em “Pesquisa UF (Estabelecimento)”. |
| Selecionar |  | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”.  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos |  | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |
