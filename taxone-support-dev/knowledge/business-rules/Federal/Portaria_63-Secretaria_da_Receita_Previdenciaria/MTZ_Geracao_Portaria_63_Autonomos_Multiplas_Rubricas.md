# MTZ_Geracao_Portaria_63_Autonomos_Multiplas_Rubricas

- **Fonte:** MTZ_Geracao_Portaria_63_Autonomos_Multiplas_Rubricas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 48 KB

---

# PORTARIA 63

# Geração do Arquivo da Portaria 63 para Autônomos

# Considerando parametrização com Múltiplas Rubricas

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS4010

Criação do documento

Definição das regras para geração das informações de autônomos para situações de múltiplas rubricas\.

__Regra De Negócio Geral__

#### Cód\.

### Descrição

### DR

__RN00__

A geração do arquivo da Portaria 63 deve ser alterada para demonstração das informações de autônomos quando há existência de registros na tela de “Parâmetros p/ Autônomos – Múltiplas Rubricas” \(menu Parâmetros\)\.

Quando, para o Perfil parametrizado na tela de geração do meio magnético existir um ou mais registros na tela de “Parâmetros p/ Autônomos – Múltiplas Rubricas” e for selecionada a opção “Gerar para Autônomos” da tela de geração, as informações de autônomos demonstradas nos registros K050, K100, K150, K200, K250 e K300 serão apresentadas considerando as regras definidas abaixo\.

Estas regras se aplicam apenas para a geração de autônomos com múltiplas rubricas, sendo que, a geração dos funcionários que é realizada através da Ficha Financeira não será impactada\.

Caso tenha sido selecionada a opção “Gerar para Autônomos” da tela de geração e não exista nenhum registro na tela de Parâmetros p/ Autônomos – Múltiplas Rubricas, mas exista código de rubrica vinculado ao Perfil no cadastro do Perfil, a geração deverá ser realizada conforme regras já existentes\. Esta forma de geração só não será considerada se existir cadastro de Parâmetros p/ Autônomos – Múltiplas Rubricas\.

OS4010

__Regra De Negócio – Registro I050__

#### Cód\.

### Descrição

### DR

__RNI050\-00__

__Origem das informações__: SAFX2002 – Tabela do Plano de Contas

__Regra de geração__: O registro I050 é o Cadastro do Plano de Contas\. Para a atualização da geração para trabalhadores autônomos, ele será gerado considerando as seguintes regras:

- Para geração para estabelecimento Centralizador ou Sem Centralização
	- Se o parâmetro "Gerar apenas Plano de Contas com movimento \(I050\)" estiver marcado

Para cada conta contábil gerada no registro K200, buscar na SAFX2002 o cadastro da conta correspondente, considerando que a conta esteja no grupo ao qual o estabelecimento matriz esteja vinculado e considerando a menor data do cadastro\. Caso o estabelecimento matriz esteja vinculado em mais de um grupo, deve ser considerado o registro mais atual em relação ao registro K200\.

Deve ser gerado também as informações de cadastro das contas superiores\. Exemplo:

\-> No K200 foi gerada a conta 00001\.001\.01

\-> No plano de contas a conta 00001\.001\.01 tem como conta superior a conta 00001\.001

\-> No plano de contas a conta 00001\.001 tem como conta superior a conta 00001

No arquivo devem ser demonstrados registros I050 para as contas: 00001\.001\.01 e 00001\.001 e 00001

- 
	- Se o parâmetro "Gerar apenas Plano de Contas com movimento \(I050\)" não estiver marcado

Gerar as informações da tabela de Plano de Contas, considerando os registros de contas que estejam vinculados ao grupo no qual o estabelecimento matriz está vinculado, gerando sempre os registros mais atuais\.

Para estabelecimentos sem centralização, as contas serão consideradas do grupo do estabelecimento matriz da empresa de geração\.

__Campos\-chave do registro__: 02 \- DT\_INC\_ALT e 06 \- COD\_GRP\_CTA\.

OS4010

__RNI050\-03__

Campo 03 \- IND\_NAT

Para geração da informação deve ser feita a seguinte conversão com base no conteúdo do campo na tabela:

__SAFX2002 \- IND\_NATUREZA__

__Registro I050 \- IND\_NAT__

1\. Ativo

1

2\. Passivo

2

7\. Patrimônio Líquido

3

3\. Despesa ou 8\. Custo

4

4\. Receita

5

9\. Outros ou 5\. Mutações Ativas ou 6\. Mutações  Passivas

9

OS4010

__Regra De Negócio – Registro I100__

#### Cód\.

### Descrição

### DR

__RNI100\-00__

__Origem das informações__: SAFX2003 \- Tabela de Centro de Custo

__Regra de geração__: O registro I100 é o Cadastro do Centro de Custos\. Para a atualização da geração para trabalhadores autônomos, ele será gerado considerando as seguintes regras:

- Para geração para estabelecimento Centralizador ou Sem Centralização

Para cada centro de custo informado no registro K200, buscar na SAFX2003 o cadastro do centro de custo correspondente, considerando que este cadastro esteja no grupo ao qual o estabelecimento matriz esteja vinculado e considerando a menor data do cadastro\. Caso o estabelecimento matriz esteja vinculado em mais de um grupo, deve ser considerado o registro mais atual em relação ao registro K200\.

Para estabelecimentos sem centralização, os cadastros serão considerados do grupo do estabelecimento matriz da empresa de geração\.

__Campos\-chave do registro__: 02 \- DT\_INC\_ALT e 03 \- COD\_CCUS\.

OS4010

__Regra De Negócio – Registro K050__

#### Cód\.

### Descrição

### DR

__RNK050\-00__

__Origem das informações__: SAFX04 – Arquivo de Cadastro de Pessoas Físicas/Jurídicas e Cadastro do Estabelecimento

__Regra de geração__: O registro K050 é o Cadastro de Trabalhadores\. Para trabalhadores autônomos ele tem como origem da informação a tabela SAFX04 e será gerado em função do registro K250 – Mestre de Folha de Pagamento\. Para cada Código de Registro do Trabalhador \(campo 05 do K250\) informado no K250 deve existir pelo menos um cadastro correspondente no registro no K050, demonstrando o cadastro vinculado ao documento fiscal considerado para geração das informações de autônomos\.

__Campos\-chave do registro__: 02 \- CNPJ/CEI, 03 \- DT\_INC\_ALT, 04 \- COD\_REG\_TRAB e 05 \- CPF\.

OS4010

__RNK050\-02__

Campo 02 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__Regra De Negócio – Registro K100__

#### Cód\.

### Descrição

### DR

__RNK100\-00__

__Origem das informações__: SAFX2037 \- Tabela de Setor e SAFX03 \- Arquivo de Fornecedores \(Contas a Pagar\)

__Regra de geração__: O registro K100 é o Cadastro de Lotação\. Para trabalhadores autônomos ele tem como origem da informação a tabela SAFX2037, referenciada na tabela SAFX03\* e será gerado em função do registro K250 – Mestre de Folha de Pagamento\. Para cada Código de Lotação \(campo 04 do K250\) informado no K250 deve existir pelo menos um cadastro correspondente no registro no K100, demonstrando o cadastro com a menor data de Inclusão\.

\**Na tabela SAFX03 estão os lançamentos de Contas a Pagar\. Para cada NF \(SAF07\) considerada na geração do K250 haverá um registro correspondente na SAFX03 e lá existe o campo Código do Setor \(COD\_SETOR\) que é justamente o código da lotação e que permitirá o vinculo com a SAFX2037\.*

__Campos\-chave do registro__: 02 \- DT\_INC\_ALT e 03 \- COD\_LTC\.

OS4010

__RNK100\-04__

Campo 04 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__Regra De Negócio – Registro K150__

#### Cód\.

### Descrição

### DR

__RNK150\-00__

__Origem das informações__: SAFX2023 \- Tabela de Verbas

__Regra de geração__: O registro K150 é o Cadastro de Verbas\. Para trabalhadores autônomos ele tem como origem da informação a tabela SAFX2023 e será gerado em função do registro K300 – Itens da Folha de Pagamento\. Para cada Código de Rubrica \(campo 07 do K300\) informado no K300 deve existir pelo menos um cadastro correspondente no registro no K150, considerando o grupo mais recente do estabelecimento que está sendo gerado e demonstrando o cadastro de verba com a mínima validade da verba associada a este grupo\.

__Campos\-chave do registro__: 02 \- DT\_INC\_ALT e 03 \- COD\_LTC\.

OS4010

__RNK150\-02__

Campo 02 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__Regra De Negócio – Registro K200__

#### Cód\.

### Descrição

### DR

__RNK200\-00__

__Origem das informações__: Tela de Parâmetros p/ Autônomos – Múltiplas Rubricas

__Regra de geração__: O registro K200 é onde serão demonstradas as informações referentes à Contabilização da Folha de Pagamento\. Para trabalhadores autônomos ele tem como origem da informação a tela de Parâmetros p/ Autônomos – Múltiplas Rubricas e será gerado em função do registro K300 – Itens da Folha de Pagamento\. Para cada Código de Lotação \(campo 04 do K300\) e Código de Rubrica \(campo 07 do K300\) informado no K300 deve existir pelo menos um cadastro correspondente no registro no K200, com Data de Inclusão ou Alteração \(campo 02 do K100\) menor ou igual a Data de Competência \(campo 06 do K300\)\.

Na geração anterior de autônomos este registro era gerado com base na SAFX03, porém, nesta tabela há informação de apenas uma conta contábil relacionada à NF e neste registro é necessário demonstrar a conta associada à rubrica\. Ex\.: a rubrica detalha o valor do INSS e a conta contábil a ser demonstrada será a de contabilização dos valores de INSS\.

__Campos\-chave do registro__: todos os campos

OS4010

__RNK200\-03__

Campo 03 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__RNK200\-06__

Campo Código Centro de Custos

Este campo será gerado conforme parametrizado na tela de Parâmetros p/ Autônomos – Múltiplas Rubricas\. Para cada código aqui referenciado, deverá existir um cadastro correspondente no registro I100, como já é feito atualmente\.

OS4010

__RNK200\-07__

Campo Código da Conta Contábil

Este campo será gerado conforme parametrizado na tela de Parâmetros p/ Autônomos – Múltiplas Rubricas\. Para cada código aqui referenciado, deverá existir um cadastro correspondente no registro I050, como já é feito atualmente\.

OS4010

__Regra De Negócio – Registro K250__

#### Cód\.

### Descrição

### DR

__RNK250\-00__

__Origem das informações__: SAFX07 \- Arquivo de Notas Fiscais

__Regra de geração__: O registro K250 é o Mestre da Folha de Pagamento\. Para autônomos ele será gerado com base na tabela de Arquivo de Notas Fiscais \(SAFX07\) e será gerado com informações de autônomos quando, na tela de geração do meio magnético, a opção “Gerar para Autônomos” estiver selecionada\.

Na seleção das informações serão considerados os registros da SAFX07 para a empresa e estabelecimento \(ou estabelecimentos, no caso de geração centralizada\) parametrizadas pelo usuário, cuja data fiscal da NF compreenda o período de geração, que seja um documento de entrada \(campo MOVTO\_E\_S diferente de 9\), com classificação referente a serviços \(campo COD\_CLASS\_DOC\_FIS igual a 2 ou 3\) e que tenha como Cadastro de Pessoa Física/Jurídica uma Pessoa Física com os campos CBO e Ocorrência do Trabalhador e Função preenchidos\.

Os campos de valor do registro devem ser somados caso exista mais de uma NF que atenda aos critérios de chave do registro\.

__Campos\-chave do registro__: 02 \- CNPJ, 03 \- IND\_FL, 04 \- COD\_LTC, 05 \- COD\_REG\_TRAB e 06 \- DT\_COMP\.

OS4010

__RNK250\-02__

Campo 02 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__RNK250\-06__

Campo 06 – DT\_COMP

O sistema deverá recuperar a informação do campo Data Fiscal NF, gerando apenas as informações de mês e ano, no formato MMAAAA\.

OS4010

__RNK250\-07__

Campo 07 – DT\_PGTO

O sistema deverá recuperar a informação do campo Data de Pagamento \(DT\_PAGTO\_NF\) da SAFX07, gerando a informação no formato DDMMAAAA\. Caso exista mais de um documento de serviço no período de competência com datas de pagamento distintas \(para autônomos\), deverá ser considerada a última data encontrada para geração do registro\.

__Exemplo__:

__Competência   Data de Pagamento__

01/2013            09/01/2013

01/2013            15/01/2013

Neste caso, será gerado o registro com data de 15/01/2013\.\.

OS4010

__RNK250\-08__

Campo COD\_CBO

Buscar no Cadastro da Pessoa Física Jurídica do Autônomo correspondente ao profissional aqui detalhada a informação do campo CBO \(COD\_CBO\)\.

OS4010

__RNK250\-09__

Campo COD\_OCORR

Buscar no Cadastro da Pessoa Física Jurídica do Autônomo correspondente ao profissional aqui detalhada a informação do campo Ocorrência do Trabalhador \(OCORRENCIA\_TRAB\)\.

OS4010

__RNK250\-10__

Campo DESC\_CARGO

Buscar no Cadastro da Pessoa Física Jurídica do Autônomo correspondente ao profissional aqui detalhada a informação do campo Função \(COD\_FUNCAO\)\.

OS4010

__RNK250\-11__

Campo QTD\_DEP\_IR

Buscar no Cadastro da Pessoa Física Jurídica do Autônomo correspondente ao profissional aqui detalhada a informação do campo Quantidade de Dependentes – IR \(IMP\_RENDA\_DEPEND\)\.

OS4010

__RNK250\-12__

Campo QTD\_DEP\_SF

Buscar no Cadastro da Pessoa Física Jurídica do Autônomo correspondente ao profissional aqui detalhada a informação do campo Quantidade de Dependentes – SF \(SAL\_FAMILIA\_DEPEND\)\.

OS4010

__RNK250\-13__

Campo VL\_BASE\_IRRF

Será gerado com base na totalização do valor do campo informado na tela “Parâmetros p/ Autônomos”, campo “Campo a ser detalhado”, cuja rubrica associada tenha informado no campo “Indicador de Base de Cálculo para Previdência Social” \(campo IND\_PREV\_SOCIAL da SAFX2023\)\* o conteúdo “10 \- Base de Cálculo para o IRPF”\.

*\* Para seleção do Cadastro de Verba, será considerado o grupo mais recente do estabelecimento que está sendo gerado e demonstrando o cadastro de verba com a mínima validade da verba associada a este grupo\.*

OS4010

__RNK250\-14__

Campo VL\_BASE\_PS

Será gerado com base na totalização do valor do campo informado na tela “Parâmetros p/ Autônomos”, campo “Campo a ser detalhado”, cuja rubrica associada tenha informado no campo “Indicador de Base de Cálculo para Previdência Social” \(campo IND\_PREV\_SOCIAL da SAFX2023\)\* o conteúdo “11 \- Base de Cálculo para a Previdência Social”\.

*\* Para seleção do Cadastro de Verba, será considerado o grupo mais recente do estabelecimento que está sendo gerado e demonstrando o cadastro de verba com a mínima validade da verba associada a este grupo\.*

OS4010

__Regra De Negócio – Registro K300__

#### Cód\.

### Descrição

### DR

__RNK300\-00__

__Origem das informações__: SAFX07 \- Arquivo de Notas Fiscais

__Regra de geração__: O registro K300 é para demonstração dos Itens da Folha de Pagamento\. Para autônomos ele será gerado com base na tabela de Arquivo de Notas Fiscais \(SAFX07\) considerando todas as NFs que foram consideradas para geração do registro K250\. Ele demonstrará por código de rubrica os valores dos Documentos Fiscais considerados no K250\.

Será gerado um registro para cada código de rubrica informada na tela de Parâmetros p/ Autônomos – Múltiplas Rubricas para demonstrar o valor existente no campo “Campo a ser detalhado” associado à rubrica\. Será gerado inclusive as rubricas dos campos cujo conteúdo seja igual a zero\.

Este registro deve ser gerado considerando a chave do registro, ou seja, um registro por tipo de folha, lotação, registro do trabalhador, competência e rubrica\.

__Campos\-chave do registro__: 02 \- CNPJ, 03 \- IND\_FL, 04 \- COD\_LTC, 05 \- COD\_REG\_TRAB, 06 \- DT\_COMP e 07 \- COD\_RUBR\.

OS4010

__RNK300\-02__

Campo 02 \- CNPJ/CEI

O sistema deverá recuperar a informação do campo “Cadastro Específico INSS\-CEI” do box “Atendimento à Portaria 63” do Cadastro do Estabelecimento, caso o campo esteja vazio, o sistema deve recuperar a informação do campo “CNPJ” do Cadastro\.

OS4010

__RNK300\-06__

Campo 06 – DT\_COMP

O sistema deverá recuperar a informação do campo Data Fiscal NF, gerando apenas as informações de mês e ano, no formato MMAAAA\.

OS4010

__RNK300\-08__

Campo 08 – VL\_RUBR

O sistema deverá recuperar a informação do campo “Campo a ser detalhado”, buscando o conteúdo informado na SAFX07\.

OS4010

__RNK300\-09__

Campo 09 – IND\_RUBR

Campo Indicador de Verba do Cadastro de Verba \(SAFX2023\)\* referente à rubrica informado\. Será gerado considerando a seguinte regra:

Quando o campo Indicador de Verba for igual a 1 \- Verba Provento, será gerado o conteúdo “P”;

Quando o campo Indicador de Verba for igual a 2 \- Verba Desconto, será gerado o conteúdo “D”;

Quando o campo Indicador de Verba for diferente de 1 \- Verba Provento ou 2 \- Verba Desconto, será gerado o conteúdo “O”;

*\* Para seleção do Cadastro de Verba, será considerado o grupo mais recente do estabelecimento que está sendo gerado e demonstrando o cadastro de verba com a mínima validade da verba associada a este grupo\.*

OS4010

__RNK300\-11__

Campo 11 – IND\_BASE\_PS

Campo Indicador de Base de Cálculo para Previdência Social do Cadastro de Verba \(SAFX2023\)\* referente à rubrica informado\. Será gerado considerando a seguinte regra:

Quando o campo Indicador de Base de Cálculo para Previdência Social for um valor de 1 a 9, será gerado o conteúdo existente no campo Indicador de Base de Cálculo para Previdência Social\.

Quando o campo Indicador de Base de Cálculo para Previdência Social for um valor diferente do valor de 1 a 9 e diferente de nulo, será gerado o conteúdo “9”\.

Quando o campo Indicador de Base de Cálculo para Previdência Social for um valor igual a nulo, gerar nulo e retornar a mensagem no log: “Registro K300, campo 11 \- IND\_BASE\_PS: conteúdo não informado na Tabela de Verbas”

*\* Para seleção do Cadastro de Verba, será considerado o grupo mais recente do estabelecimento que está sendo gerado e demonstrando o cadastro de verba com a mínima validade da verba associada a este grupo\.*

OS4010

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

