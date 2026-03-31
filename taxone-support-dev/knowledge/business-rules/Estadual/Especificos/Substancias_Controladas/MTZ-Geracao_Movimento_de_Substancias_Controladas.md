# MTZ-Geracao_Movimento_de_Substancias_Controladas

- **Fonte:** MTZ-Geracao_Movimento_de_Substancias_Controladas.docx
- **Modificado:** 2022-09-01
- **Tamanho:** 65 KB

---

# Geração do Movimento de Substâncias Controladas 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS3467A

Geração do Movimento de Substâncias Controladas

Geração do Movimento de Substâncias Controladas

31/08/2011

CH721\_2013

Geração do Movimento de Substâncias Controladas

Geração do Movimento de Substâncias Controladas – Resumo Trimestral de Estoque para o Ministério do Exército

31/01/2011

OS3976\-G

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS – Recuperação do campo Data Emissão da DWT\_DOCTO\_FISCAL para gravar na SAFX70

Este documento tem como objetivo permitir a geração para atendimento à Polícia Federal através da Data de Emissão da nota fiscal\.

04/04/2013

CH9683\_2015

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS – Alteração na recuperação do campo Guia de Tráfico da SAFX70

Alteração na Geração do Movimento de Substâncias Controladas – Resumo Trimestral de Estoque para o Ministério do Exército para recuperar o campo 23 \- GUIA\_TRAFEGO da SAFX70 caso preenchido\.

28/08/2015

CH18598\_2017 \(MFS\-13965\)

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS – Alteração na recuperação do campo Número do Registro de Exportação/Importação da SAFX70

Este documento tem como objetivo alterar a recepção da informação do campo 26\-Número do Registro de Exportação/Importação da SAFX70 para considerar também o conteúdo informado no campo 220\-Nº LI da SAFX08\.

10/10/2017

MFS\-31705

Inclusão de regras de preenchimento dos campos Armazém e Tipo de Frete\.

Preenchimento dos campos 30 e 31 Pessoa Física/Jurídica Armazém da SAFX70 com base nos campos 144\- CNPJ do Armazém de Saída e 147 \- CNPJ do Armazém de Recebimento da SAFX07\.

Preenchimento do campo 32 Tipo de Frete da SAFX70 com base no campo 72 \- Tipo de Frete da SAFX07\.

__REGRAS: RN30, RN31\.__

08/11/2019

MFS\-75724

Inclusão da Parametrização para Geração de Movimento por Natureza de Operação

Alteração na recuperação do movimento de documento fiscal \(SAFX07, SAFX08\) para contemplar a nova parametrização por Natureza de Operação\.

__REGRAS: RG00, RN07__

17/12/2021

MFS\-81054

Inclusão da Parametrização para Geração de Movimento do Saldo SAFX72

Inclusão do parâmetro “Geração da SAFX72 – Saldos Mensais \(a partir da SAFX52\)” para contemplar a geração da tabela X72, considerando as informações do Inventário \(X52\)\.

__REGRAS: RN01, RG02 e RN36 à RN46__

23/08/2022

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Regra para tela de geração do Movimento de Produtos:

Ao clicar no menu Movimento > Geração, o sistema deve exibir a tela de seleção conforme abaixo, com os seguintes campos: 

Período: 

Exibir campos no formato DD/MM/AAAA 

Permite que o usuário informe data inicial e final para geração dos registros\.

Campo de preenchimento obrigatório

Validação: Caso o usuário não preencha os campos, exibir mensagem de erro: “Data Final do período deve ser preenchida” “Data Inicial do período deve ser preenchida” 

Excluir somente registros calculados: 

Exibir Checkbox

Ao selecionar este campo, a geração irá excluir somente os registros calculados  

__\[MFS\-81054\]__ Inclusão do parâmetro para considerar a SAFX52 para geração da SAFX72

Geração da SAFX72 – Saldos Mensais \(a partir da SAFX52\)

Exibir Checkbox

Ao selecionar este campo, o sistema irá gerar a SAFX72 a partir da leitura do Inventário de Estoque por Produto \(SAFX52\)

__Default: Desmarcado__

Estabelecimentos:

Exibir todos os Estabelecimentos tendo a possibilidade de Selecionar/Desmarcar Todos

OS3467A

MFS\-81054

__RG00__

__Regra Geral para recuperação dos dados:__

Ao clicar no botão de geração o sistema irá compor a X70\_mov\_subst\_cont e X700 \(a ser definido pelo A&D\)

Para a composição da X70 e X700, deverão ser respeitadas as seguintes regras:

A geração de movimentos de produtos \(*X70*\) é efetuada a partir da leitura de documentos fiscais de Mercadoria *\(SAFX07 e SAFX08*\) e movimento de estoque \(*SAFX10*\)\.

__Para geração a partir da SAFX07 e safx08:__

\-Recuperar todos os documentos de entrada e saída \(CAMPO 03 MOVTO\_E\_S DA SAFX07\) não cancelados \(CAMPO 30 SITUACAO = ‘N’ da SAFX07\) para o Estabelecimento \(CAMPO 02 COD\_ESTAB DA SAFX07\) selecionado na tela de geração do Movimento em que:

- O Campo data fiscal \(CAMPO 05 DATA\_FISCAL DA DWT\_DOCTO\_FISCAL\) esteja dentro do período informado na tela__ __de geração do movimento 
- O campo código do produto \(CAMPO 14 COD\_PRODUTO DA SAFX08\) esteja cadastrado para pelo menos um tipo de obrigação na tela Parâmetro de Produto por Tipo de Obrigação\.
- O CFOP \(CAMPO COD\_CFO DA SAFX08\) esteja cadastrado na tela Parâmetros para Geração de Movimento > P/ CFO

__Ou__

\[MFS\-75724\]

- CFOP \+ Natureza de Operação \(da SAFX08\) esteja cadastrado na tela Parâmetros para Geração de Movimento > P/ Natureza de Operação\. 

Obs1: Considerar a nota caso o CFOP \+ Natureza de Operação \(da SAFX08\) não esteja parametrizado na tela Parâmetros para Geração de Movimento > P/ Natureza de Operação, mas o CFOP esteja parametrizado tela Parâmetros para Geração de Movimento > P/ CFO\. 

__Para geração a partir da SAFX10:__

Recuperar todos os documentos de entrada e saída \(CAMPO 03 MOVTO\_E\_S DA SAFX10\) para o Estabelecimento \(CAMPO 02 COD\_ESTAB DA SAFX10\) selecionado na tela de geração do Movimento em que:

- O Campo data do movimento \(CAMPO 07 DATA\_MOVTO DA SAFX10\) esteja dentro do período informado na tela__ __de geração do movimento 
- O campo código do produto \(CAMPO 12 COD\_PRODUTO DA SAFX10\) esteja cadastrado para pelo menos um tipo de obrigação na tela Parâmetro de Produto por Tipo de Obrigação\.
- O código da operação \(CAMPO 27 COD\_OPERACAO DA SAFX10\) esteja cadastrado na tela de Parâmetros para Geração de Movimento > P/ Operação\.

OS3467A

MFS\-75724

__RN02__

Campo 01 – Empresa \(SAFX70\)

__Nome do Campo: COD\_EMPRESA__

__Tamanho__: 3

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o Código da Empresa \(CAMPO 01 COD\_EMPRESA DA SAFX07\) OU Recuperar o Código da Empresa \(CAMPO 01 COD\_EMPRESA DA SAFX10\)

OS3467A

__RN03__

Campo 02 – Estabelecimento \(SAFX70\)

__Nome do Campo: COD\_ESTAB__

__Tamanho__: 06

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o Código do Estabelecimento \(CAMPO 02 COD\_ESTAB DA SAFX07\) OU Recuperar o Código do Estabelecimento \(CAMPO 02 COD\_ESTAB DA SAFX10\)

OS3467A

__RN04__

Campo 03 – Ident Produto \(SAFX70\)

__Nome do Campo: IDENT\_PRODUTO__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o código de identificação do produto \(CAMPO 12 IDENT\_PRODUTO DA X08\_ITENS\_MERC\) OU Recuperar o código de identificação do produto \(CAMPO 11 IDENT\_PRODUTO DA X10\_ESTOQUE\)

OS3467A

__RN05__

Campo 04 – Data do Movimento \(SAFX70\)

__Nome do Campo: DATA\_MOVTO__

__Tamanho__: 8

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo data fiscal \(CAMPO 04 DATA\_FISCAL DA DWT\_DOCTO\_FISCAL\) OU o campo data do movimento \(CAMPO 07 DATA\_MOVTO DA SAFX10\)

OS3467A

__RN06__

Campo 05 – Movimento E/S \(SAFX70\)

__Nome do Campo: MOVTO\_E\_S__

__Tamanho__: 1

__Tipo__: VARCHAR2

__Regra de Negócio: __Verificar o campo movimento entrada/saída \(CAMPO 03 MOVTO\_E\_S DA SAFX07\) OU Verificar o campo movimento entrada/saída \(CAMPO 03 MOVTO\_E\_S DA SAFX10\)

Para este campo, caso o preenchimento seja = ‘1’, ‘2’, ‘3’, ‘4’, ‘5’ atribuir o valor __‘1’__

Caso o preenchimento seja = ‘9’, manter o número\.

OS3467A

__RN07__

Campo 06 – Tipo de Operação \(SAFX70\)

__Nome do Campo: TIPO\_OPERACAO__

__Tamanho__: 2

__Tipo__: VARCHAR2

__Regra de Negócio: __Verificar o CFOP \(da SAFX08\), e recuperar o campo Tipo de Operação para o CFOP correspondente na tela de Parâmetros p/ Geração de Movimento por CFOP \- menu Cadastro> Parâmetros p/ Geração de Movimento > p/ CFO

OU

\[MFS\-75724\]

Verificar o CFOP \+ Natureza de Operação \(da SAFX08\) e recuperar o campo Tipo de Operação cadastrado na tela Parâmetros para Geração de Movimento por Natureza de Operação \- menu Cadastro> Parâmetros p/ Geração de Movimento > p/ Natureza de Operação\. 

OU

Verificar a operação \(CAMPO 27 COD\_OPERACAO DA SAFX10\), e recuperar o campo Tipo de Operação para a operação correspondente na tela de Parâmetros p/ Geração de Movimento por Operação \- menu Cadastro> Parâmetros p/ Geração de Movimento > p/ Operação\.

OS3467A

MFS\-75724

__RN08__

Campo 07 – Número do Documento Fiscal \(SAFX70\)

__Nome do Campo: NUM\_DOCFIS__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo número do documento fiscal \(CAMPO 08 NUM\_DOCFIS DA SAFX07\) OU Recuperar o campo número do documento \(CAMPO 08 NUM\_DOCTO DA SAFX10\)

OS3467A

__RN09__

Campo 08 – Série do Documento Fiscal \(SAFX70\)

__Nome do Campo: SERIE\_DOCFIS__

__Tamanho__: 3

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo série do documento fiscal \(CAMPO 09 SERIE\_DOCFIS DA SAFX07\) OU Recuperar o campo série do documento \(CAMPO 09 SERIE\_DOCFIS DA SAFX10\)

OS3467A

__RN10__

Campo 09 – Subsérie do Documento Fiscal \(SAFX70\)

__Nome do Campo: SUB\_SERIE\_DOCFIS__

__Tamanho__: 2

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Subsérie do documento fiscal \(CAMPO 10 SUB\_SERIE\_DOCFIS DA SAFX07\) OU Recuperar o campo Subsérie do documento \(CAMPO 10 SUB\_SERIE\_DOCFIS DA SAFX10\)

OS3467A

__RN11__

Campo 10 – Identificação da Pessoa Física/Jurídica \(SAFX70\)

__Nome do Campo: IDENT\_FIS\_JUR__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Identificação da Pessoa Física/Jurídica \(CAMPO 08 IDENT\_FIS\_JUR DA DWT\_DOCTO\_FISCAL\) OU Recuperar na tabela de Estabelecimentos x Pessoas Físicas/Jurídicas \(DWT\_PFJ\_ESTAB\) o código e indicador da Pessoa Fis/Jur atribuído ao Estabelecimento do Movimento \(Campo COD\_FIS\_JUR colocar campo do indicador da tabela DWT\_PFJ\_ESTAB\) \.

OS3467A

__RN12__

Campo 11 – Tipo de Visto \(SAFX70\)

__Nome do Campo: TIPO\_VISTO__

__Tamanho__: 6

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO UTILIZADO

OS3467A

__RN13__

Campo 12 – Quantidade Movimentada \(SAFX70\)

__Nome do Campo: QTD\_MOVTO__

__Tamanho__: 17,6

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Quantidade \(CAMPO 24 QUANTIDADE DA SAFX08\) OU Recuperar o campo quantidade\(CAMPO 20 QTD\_MOVTO DA SAFX10\)

OS3467A

__RN14__

Campo 13 – Identificação da medida \(SAFX70\)

__Nome do Campo: IDENT\_MEDIDA__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Identificação da Medida \(CAMPO 25 IDENT\_MEDIDA DA X08\_ITENS\_MERC\) OU Recuperar o campo Identificação da Medida \(CAMPO 33 IDENT\_MEDIDA DA X10\_ESTOQUE\)

OS3467A

__RN15__

Campo 14 – Tipo \(SAFX70\)

__Nome do Campo: TIPO__

__Tamanho__: 6

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO PREENCHIDO ATRAVÉS DA GERAÇÃO

OS3467A

__RN16__

Campo 15 – UF \(SAFX70\)

__Nome do Campo: IDENT\_ESTADO__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Identificação do Estado \(CAMPO 21 IDENT\_ESTADO DA X04\_PESSOA\_FIS\_JUR\) OU Recuperar o campo Identificação Do Estado \(CAMPO 18 IDENT\_ESTADO DA TABELA ESTABELECIMENTO\)

OS3467A

__RN17__

Campo 16 – Referência \(SAFX70\)

__Nome do Campo: REFERENCIA__

__Tamanho__: 45

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO UTILIZADO

OS3467A

__RN18__

Campo 17 – Observações \(SAFX70\)

__Nome do Campo: OBSERVACAO__

__Tamanho__: 90

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO PREENCHIDO ATRAVÉS DA GERAÇÃO

OS3467A

__RN19__

Campo 18 – Especificação do Material \(SAFX70\)

__Nome do Campo: IND\_ESPEC\_MAT__

__Tamanho__: 1

__Tipo__: CHAR

__Regra de Negócio: __CAMPO NÃO PREENCHIDO ATRAVÉS DA GERAÇÃO

OS3467A

__RN20__

Campo 19 – Identificação do CFOP \(SAFX70\)

__Nome do Campo: IDENT\_CFO__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio:__ Recuperar o campo Código Fiscal de Operação \(CAMPO 22 COD\_CFO DA SAFX08\), não será preenchido a partir da geração por estoque\.

OS3467A

__RN21__

Campo 20 – Identificação da Natureza de Operação \(SAFX70\)

__Nome do Campo: IDENT\_NATUREZA\_OP__

__Tamanho__: 40

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO PREENCHIDO ATRAVÉS DA GERAÇÃO

\[MFS\-75724\] Campo continuará não sendo preenchido pois na condição da nota possuir mais de um item com CFOP/Natureza Operação distintos, com mesmo Tipo de Operação, os distintos CFOP/Natureza Operação não seriam gravados na tabela do movimento \(SAFX70\), visto que a chave da tabela contém o Tipo de Operação, e não contém o CFOP/Natureza Operação\.

OS3467A

__RN22__

__\[ALTERADA \- CH721\_2013\]\[ALTERADA – CH9683\_2015\]__

Campo 21 – Guia de Tráfego \(SAFX70\)

__Nome do Campo: GUIA\_TRAFEGO__

__Tamanho__: 40

__Tipo__: VARCHAR2

__Regra de Negócio: __Campo não preenchido através da geração __exceto__ para geração do Resumo Trimestral de Estoque para o Ministério do Exército, onde deverá ser verificado se o campo 23 \- GUIA\_TRAFEGO da SAFX70 está preenchido, caso preenchido deverá recuperar essa informação do campo, caso contrário não será preenchido através dessa geração\.

OS3467A

__CH721\_2013__

CH9683\_2015

__RN23__

Campo 22 – Indicador de Gravação \(SAFX70\)

__Nome do Campo: IND\_GRAVACAO__

__Tamanho__: 1

__Tipo__: CHAR

__Regra de Negócio: __Atribuir o número ‘6’ ao campo

OS3467A

__RN24__

Campo 23 – Número do Processo \(SAFX70\)

__Nome do Campo: NUM\_PROCESSO__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __O valor deste campo é gerado internamente

OS3467A

__RN25__

Campo 24 – Número de Receita \(SAFX70\)

__Nome do Campo: NUM\_RECEITA__

__Tamanho__: 15

__Tipo__: VARCHAR2

__Regra de Negócio: __CAMPO NÃO PREENCHIDO ATRAVÉS DA GERAÇÃO

OS3467A

__RN26__

Campo 25 – Valor Total do Documento Fiscal \(SAFX70\)

__Nome do Campo: VLR\_TOT\_NOTA__

__Tamanho__: 17,2

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo valor contábil do Item \(CAMPO 64 VLR\_CONTAB\_ITEM DA SAFX08\) OU Recuperar o campo preço do Item \(CAMPO 22 PRECO\_ITEM DA SAFX10\)

OS3467A

__RN27__

Campo 26 – Número do Registro de Exportação/Importação \(SAFX70\)

__\[ALTERADA \- CH18598\_2017 \(MFS\-13965\)\]__

__Nome do Campo: NUM\_REG\_EXP\_IMP__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o conteúdo do campo 220\-NUM\_LI da tabela definitiva da SAFX08, se não estiver preenchido recuperar o conteúdo do campo 72\-NUM\_REG\_EXP da tabela definitiva da SAFX08, se também não estiver preenchido recuperar o conteúdo do campo 103\-NUM\_DEC\_IMP\_REF da tabela definitiva da SAFX08, se nenhum dos campos estiver preenchido o campo não será preenchido na SAFX70\.

OS3467A

CH18598\_2017 \(MFS\-13965\)

__RN28__

Campo 27 e 28 – Identificação de Pessoa Física/Jurídica Transportadora \(SAFX70\)

__Nome do Campo: IDENT\_FIS\_JUR\_TRANSP__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Identificação da Pessoa Física/Jurídica Transportadora \(CAMPO 07 IDENT\_FIS\_JUR DA X50\_TRANSP\_DOCFIS\) 

OS3467A

__RN29__

Campo 29 \- Data de Emissão \(SAFX70\)

__Nome do Campo: DATA\_EMISSAO__

__Tamanho__: 8

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo data emissão \(CAMPO 11 DATA\_EMISSAO DA DWT\_DOCTO\_FISCAL\)

OS3976\-G

__RN30__

Campo 30 e 31 – Identificação de Pessoa Física/Jurídica Armazém \(SAFX70\)

__Nome do Campo: IDENT\_FIS\_JUR\_ARMAZEM__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __Preenchimento com base nos campos 144\- CNPJ do Armazém de Saída e 147 \- CNPJ do Armazém de Recebimento da SAFX07\.

Caso o documento fiscal recuperado da SAFX07 seja de saída \(campo 03 \- Movimento Entrada/Saída = ‘9’\) então:

      Considerar o 144\- CNPJ do Armazém de Saída \(CNPJ\_ARMAZ\_ORIG\)\.

Caso o documento fiscal recuperado da SAFX07 seja de entrada \(campo 03 \- Movimento Entrada/Saída diferente de ‘9’\) então:

      Considerar o 147\- CNPJ do Armazém de Recebimento \(CNPJ\_ARMAZ\_DEST\)\.

Uma vez determinado o Armazém a ser considerado, segundo regra acima, recuperar o Cadastro da Pessoa Física Jurídica \(SAFX04\) referente ao armazém:

\- CPF\-CGC = CNPJ do Armazém

\- Validade = recuperar o cadastro do armazém de cuja validade seja a mais recente e menor ou igual à data fiscal da SAFX07\.

Preencher o campo __IDENT\_FIS\_JUR\_ARMAZEM__ com a Identificação da Pessoa Física/Jurídica recuperada\.

MFS\-31705

__RN31__

Campo 32 – Indicador do Tipo de Frete \(SAFX70\)

__Nome do Campo: IND\_TP\_FRETE__

__Tamanho__: 1

__Tipo__: VARCHAR2

__Valores aceitos:__

1 \- Frete para Conta do Emitente \(CIF\);

2 \- Frete para Conta do Destinatário \(FOB\);

3 \- Frete por conta de Terceiros\.

__Regra de Negócio: __Preenchimento com base no campo 72 \- Tipo de Frete da SAFX07\.

Se o campo 72\- Indicador do Tipo de Frete \(IND\_TP\_FRETE\) for igual a:

  1\-Frete para Conta do Emitente \(CIF\), preencher com 1;

  2\-Frete para Conta do Destinatário \(FOB\) , preencher com 2;

  3\-Transporte Próprio por conta do Remetente, preencher com 1;

  4\-Transporte Próprio por conta do Destinatário, preencher com 2;

  0\-Outros, preencher com 3\.

Se o campo 72\- Indicador do Tipo de Frete \(IND\_TP\_FRETE\) for nulo, não preencher\.

MFS\-31705

__RG01__

__Regra Geral para recuperação dos dados:__

Com base na RG00, verificar se existe registro na SAFX119 para o registro correspondente na SAFX08\.

Cada registro correspondente da SAFX119 deve gerar uma linha na SAFX700 com os dados abaixo\.

OS3467A

__RN32__

Campo 28 – Número de Fabricação do Lote \(SAFX700\)

__Nome do Campo: NUM\_FAB\_LOTE__

__Tamanho__: 50

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo Número de Fabricação do Lote \(CAMPO 16 NUM\_FAB\_ LOTE DA SAFX119\) 

OS3467A

__RN33__

Campo 29 – Quantidade de Item por Lote \(SAFX700\)

__Nome do Campo: QTD\_LOTE__

__Tamanho__: 17,6

__Tipo__: VARCHAR2

__Regra de Negócio:__ Recuperar o campo quantidade de item por lote \(CAMPO 17 QTD\_ LOTE DA SAFX119\)

OS3467A

__RN34__

Campo 30 – Data de Fabricação do Medicamento \(SAFX700\)

__Nome do Campo: DAT\_FABRIC__

__Tamanho__: 8

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo data de fabricação do medicamento \(CAMPO 18 DAT\_FABRIC DA SAFX119\)

OS3467A

__RN35__

Campo 31 – Data de Validade do Medicamento \(SAFX700\)

__Nome do Campo: DAT\_VALIDADE__

__Tamanho__: 8

__Tipo__: VARCHAR2

__Regra de Negócio: __Recuperar o campo data de validade do medicamento \(CAMPO 19 DAT\_VALIDADE DA SAFX119\)

OS3467A

__RG02__

__Regra Geral para recuperação dos dados :__

Ao clicar no botão de geração com o parâmetro “Geração da SAFX72 – Saldos Mensais \(a partir da SAFX52\)” __marcado__ o sistema deverá compor os registros da X72\_SALDO\_SUBST\.

Para a composição da X72, deverão ser respeitadas as seguintes regras:

A geração de saldo mensais das substâncias controlas de produtos \(*X72*\) será efetuada a partir da leitura do Inventário de Estoque por Produto \(X52\), como critério principal o sistema identificará os registros conforme os produtos cadastrados na X71\_PARAM\_SUBST\. 

__Para geração a partir da SAFX52:__

Recuperar todos os registros de Inventário em que:

- O Campo Código de Empresa \(CAMPO 01 COD\_EMPRESA DA X52\) selecionado na tela de geração do Movimento;
- O Campo Código de Estabelecimento \(CAMPO 02 COD\_ESTAB DA X52\) selecionado na tela de geração do Movimento;
- O Campo data do movimento \(CAMPO 03 DATA\_INVENTARIO DA X52\) esteja dentro do período informado na tela__ __de geração do movimento ;
- O campo código do produto \(CAMPO IDENT\_PRODUTO DA X52 igual ao CAMPO IDENT\_PRODUTO DA X71\) 

MFS\-81054

__RN36__

Campo 01 – Empresa \(SAFX72\)

__Nome do Campo: COD\_EMPRESA__

__Tamanho__: 3

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o Código da Empresa \(CAMPO 01 COD\_EMPRESA DA SAFX52\)\.

MFS\-81054

__RN37__

Campo 02 – Estabelecimento \(SAFX72\)

__Nome do Campo: COD\_ESTAB__

__Tamanho__: 06

__Tipo__: VARCHAR2

__Regra de Negócio__: Recuperar o Código do Estabelecimento \(CAMPO 02 COD\_ESTAB DA SAFX52\)\. 

MFS\-81054

__RN38__

Campo 03 – Data do Movimento \(SAFX72\)

__Nome do Campo: DATA\_MOVTO__

__Tamanho__: 8

__Tipo__: DATE

__Regra de Negócio: __Recuperar o campo data inventário\(CAMPO 03 DATA\_INVENTARIO DA SAFX52\)\. 

MFS\-81054

__RN39__

Campo 04 – Ident Produto \(SAFX72\)

__Nome do Campo: IDENT\_PRODUTO__

__Tamanho__: 12

__Tipo__: NUMBER

__Regra de Negócio: __Recuperar o código de identificação do produto \(CAMPO 05 IDENT\_PRODUTO DA X52\_INVENT\_PRODUTO\)\.

MFS\-81054

__RN40__

Campo 05 – Quantidade do Saldo \(SAFX72\)

__Nome do Campo: QUANT\_SALDO__

__Tamanho__: 17,6

__Tipo__: NUMBER

__Regra de Negócio: __Recuperar o campo de Quantidade de Inventário \(CAMPO 13 QUANTIDADE DA SAFX52\)\. 

MFS\-81054

__RN41__

Campo 06 – Identificação da medida \(SAFX72\)

__Nome do Campo: IDENT\_MEDIDA__

__Tamanho__: 12

__Tipo__: NUMBER

__Regra de Negócio: __Recuperar o campo Identificação da Medida \(CAMPO 11 IDENT\_MEDIDA DA X52\_INVENT\_PRODUTO\)\. 

MFS\-81054

__RN42__

Campo 07 \- Tipo \(SAFX72\)

__Nome do Campo: TIPO__

__Tamanho__: 6

__Tipo__: VARCHAR2

__Regra de Negócio: Campo não utilizado, deixar vazio\.__

MFS\-81054

__RN43__

Campo 08 – Observação \(SAFX72\)

__Nome do Campo: OBSERVACAO__

__Tamanho__: 90

__Tipo__: VARCHAR

__Regra de Negócio: __Recuperar o campo de Observação \(CAMPO 18 OBSERVACAO DA X52\_INVENT\_PRODUTO\)\. 

MFS\-81054

__RN44__

Campo 09 \- Especificação do Material \(SAFX72\)

__Nome do Campo: ESPECIFICA\_MAT__

__Tamanho__: 1

__Tipo__: CHAR

__Regra de Negócio: __Recuperar o campo de IND\_PRODUTO \(CAMPO 03 IND\_PRODUTO DA X2013\_PRODUTO\), e aplicar a Regra abaixo:

      __Se__ o Campo de IND\_PRODUTO da Tabela X2013\_PRODUTO for igual à '2';

              __ Preencher__ com ‘1’;

         __ Senão __

                 __Preencher__ com ‘2’\.

MFS\-81054

__RN45__

Campo 10 – Número do Processo \(SAFX72\)

__Nome do Campo: NUM\_PROCESSO__

__Tamanho__: 12

__Tipo__: VARCHAR2

__Regra de Negócio: __O valor deste campo é gerado internamente\.

MFS\-81054

__RN46__

Campo 11 – Indicador de Gravação \(SAFX72\)

__Nome do Campo: IND\_GRAVACAO__

__Tamanho__: 1

__Tipo__: CHAR

__Regra de Negócio: __Atribuir o número ‘6’ ao campo\.

MFS\-81054

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

