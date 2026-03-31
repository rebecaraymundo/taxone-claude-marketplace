# MTZ-ICMS-Param_Dados_Geracao_Itens_Doctos_Fiscais

- **Fonte:** MTZ-ICMS-Param_Dados_Geracao_Itens_Doctos_Fiscais.docx
- **Modificado:** 2022-02-17
- **Tamanho:** 91 KB

---

THOMSON REUTERS

Módulo DW

Parametrização dos Dados para Geração de Itens de Documento Fiscal

__Localização__: Menu Estadual, Módulo ICMS, menu <a id="_Hlk87536457"></a>Manutenção 🡪 Parâmetros Transferência de Crédito/Débito Automática 🡪 Dados para Geração de Itens de Documento Fiscal

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS36422

Criação da tela

Atendimento a __Nota Técnica 002/2010 do Rio Grande do Norte__

11/11/2021

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Esta parametrização tem como objetivo definir informações para geração dos itens de mercadoria na rotina de Geração das Transferência de Crédito/Debito \(__Centralização__\)\.

A parametrização foi criada para ser utilizada apenas na opção de transferência da Centralização\.

Base Legal: Orientação Técnica EFD nº 002/2010 do Rio Grande do Norte\.

Estrutura da tabela:

__Descrição__

__CAMPO__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Empresa

COD\_EMPRESA

A

003

SIM

SIM

Estabelecimento

COD\_ESTAB

A

006

SIM

SIM

Grupo Produto Entrada Credito

GRUPO\_PRODUTO\_ENTR\_CRED

A

009

SIM

NÃO

Indicador do Produto Entrada Credito

IND\_PRODUTO\_ENTR\_CRED

A

001

SIM

NÃO

Código do Produto Entrada Credito

COD\_PRODUTO\_ENTR\_CRED

A

060

SIM

NÃO

Grupo Produto Saída Crédito

GRUPO\_PRODUTO\_SAIDA\_CRED

A

009

SIM

NÃO

Indicador do Produto Saída Crédito

IND\_PRODUTO\_SAIDA\_CRED

A

001

SIM

NÃO

Código do Produto Saída Crédito

COD\_PRODUTO\_SAIDA\_CRED

A

060

SIM

NÃO

Grupo Produto Entrada Débito

GRUPO\_PRODUTO\_ENTR\_DEB

A

009

SIM

NÃO

Indicador do Produto Entrada Débito

IND\_PRODUTO\_ENTR\_DEB

A

001

SIM

NÃO

Código do Produto Entrada Débito

COD\_PRODUTO\_ENTR\_DEB

A

060

SIM

NÃO

Grupo Produto Saída Débito

GRUPO\_PRODUTO\_SAIDA\_DEB

A

009

SIM

NÃO

Indicador do Produto Saída Débito

IND\_PRODUTO\_SAIDA\_DEB

A

001

SIM

NÃO

Código do Produto Saída Débito

COD\_PRODUTO\_SAIDA\_DEB

A

060

SIM

NÃO

Grupo Unidade Padrão

GRUPO\_UND\_PADRAO

A

009

SIM

NÃO

Código Unidade Padrão

COD\_UND\_PADRAO

A

008

SIM

NÃO

Grupo Medida

GRUPO\_MEDIDA

A

009

SIM

NÃO

Código Medida

COD\_MEDIDA

A

008

SIM

NÃO

CFOP Entrada Credito

COD\_CFO\_ENTR\_CRED

A

004

SIM

NÃO

CFOP Saída Credito

COD\_CFO\_SAIDA\_CRED

A

004

SIM

NÃO

CFOP Entrada Débito

COD\_CFO\_ENTR\_DEB

A

004

SIM

NÃO

CFOP Saída Débito

COD\_CFO\_SAIDA\_DEB

A

004

SIM

NÃO

Grupo Natureza Operação Entrada Credito

GRUPO\_NATUREZA\_OP\_ENTR\_CRED

A

009

NÃO

NÃO

Código Natureza Operação Entrada Credito

COD\_NATUREZA\_OP\_ENTR\_CRED

A

003

NÃO

NÃO

Grupo Natureza Operação Saída Credito

GRUPO\_NATUREZA\_OP\_SAIDA\_CRED

A

009

NÃO

NÃO

Código Natureza Operação Saída Credito

COD\_NATUREZA\_OP\_SAIDA\_CRED

A

003

NÃO

NÃO

Grupo Natureza Operação Entrada Débito

GRUPO\_NATUREZA\_OP\_ENTR\_DEB

A

009

NÃO

NÃO

Código Natureza Operação Entrada Débito

COD\_NATUREZA\_OP\_ENTR\_DEB

A

003

NÃO

NÃO

Grupo Natureza Operação Saída Débito

GRUPO\_NATUREZA\_OP\_SAIDA\_DEB

A

009

NÃO

NÃO

Código Natureza Operação Saída Débito

COD\_NATUREZA\_OP\_SAIDA\_DEB

A

003

NÃO

NÃO

Grupo Observação Entrada Crédito

GRUPO\_OBSERVACAO\_ENTR\_CRED

A

009

NÃO

NÃO

Código Observação Entrada Crédito

COD\_OBSERVACAO\_ENTR\_CRED

A

008

NÃO

NÃO

Grupo Observação Saída Crédito

GRUPO\_OBSERVACAO\_SAIDA\_CRED

A

009

NÃO

NÃO

Código Observação Saída Crédito

COD\_OBSERVACAO\_SAIDA\_CRED

A

008

NÃO

NÃO

Grupo Observação Entrada Débito

GRUPO\_OBSERVACAO\_ENTR\_DEB

A

009

NÃO

NÃO

Código Observação Entrada Débito

COD\_OBSERVACAO\_ENTR\_DEB

A

008

NÃO

NÃO

Grupo Observação Saída Débito

GRUPO\_OBSERVACAO\_SAIDA\_DEB

A

009

NÃO

NÃO

Código Observação Saída Débito

COD\_OBSERVACAO\_SAIDA\_DEB

A

008

NÃO

NÃO

# <a id="_Toc451260496"></a>Layout da Tela

__Título: Dados para Geração de Itens de Documento Fiscal__

Estabelecimento:  \[codigo – razão social\]

\-\- Produto – Transferência de Crédito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[indicador\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[indicador\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- Produto – Transferência de Débito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[indicador\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[indicador\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Unidade Padrão:       \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Unidade de Medida: \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\- CFOP – Transferência de Crédito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- CFOP – Transferência de Débito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- Natureza Operação – Transferência de Crédito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- Natureza Operação – Transferência de Débito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- Observação – Transferência de Crédito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

\-\- Observação – Transferência de Débito \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Entrada: \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

Saída:     \[grupo\] \[pastinha\] \[código \] \[validade\] \[ descrição                                 \]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

Replicar para os Estabelecimentos \[x\]          Filtro UF \[\\/     \]

\[ \] codigo – razão social do estabelecimento

\[ \] codigo – razão social do estabelecimento

\[ \] codigo – razão social do estabelecimento

\[ \] codigo – razão social do estabelecimento

__Botões da barra de menu__:

GRUPO

Abre a janela padrão de seleção Estabelecimento/Grupo/Validade considerando o código da tabela “2013”

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão do registro\. 

CONFIRMA

Opção para salvar as informações do registro incluído ou alterado\.

RELATÓRIO

Esta opção permite imprimir os dados da tabela\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

O funcionamento da janela é bastante semelhante ao da janela de __Dados para Geração de Documentos Fiscais__\.

Ao acionar a janela via menu, o sistema disponibiliza a janela padrão de seleção de Estabelecimento/Grupo/Validade considerando o código da tabela “2013”\. O usuário escolhe o estabelecimento e grupo e o sistema abre a janela de __Dados para Geração de Itens de Documento Fiscal__, preenchendo o campo Estabelecimento automaticamente\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

N

Texto

Campo desabilitado\.

Apresentar o estabelecimento selecionado na janela padrão de seleção de Estabelecimento/Grupo/Validade\.

- Produto – Transferência de Crédito \(Entrada\)
- Produto – Transferência de Crédito \(Saída\)
- Produto – Transferência de Débito \(Entrada\)
- Produto – Transferência de Débito \(Saída\)

Alfanumérico

__S__

S

Pastinha \+ grupo \+ indicador \+ código \+ validade \+ descrição

Estes campos trabalham com janela de seleção da Tabela de Cadastro da Produtos \(SAFX2013\)\.

Serão disponibilizadas para seleção apenas os produtos da SAFX2013 cujo do Grupo foi selecionado na abertura da janela\.

Se o código do produto for digitado, deve recuperar o registro do produto do grupo em questão e de máxima validade\. 

Caso o código do produto digitado não exista na tabela SAFX2013, exibir a mensagem, dependendo do campo que está sendo criticado: 

     *“O Código do Produto Transferência de Crédito \(Entrada\) não está cadastrado”\.*

 ou

*     “O Código do Produto Transferência de Crédito \(Saída\) não está cadastrado”\.*

ou

     *“O Código do Produto Transferência de Débito \(Entrada\) não está cadastrado”\.*

ou

*     “O Código do Produto Transferência de Débito \(Saída\) não está cadastrado”\.*

Se o produto não estiver preenchido, exibir a mensagem, dependendo do campo que está sendo criticado:

*     “O Produto Transferência de Crédito \(Entrada\) é de preenchimento obrigatório e não foi informado”\.*

ou

*     “O Produto Transferência de Crédito \(Saída\) é de preenchimento obrigatório e não foi informado”\.*

ou

*     “O Produto Transferência de Débito \(Entrada\) é de preenchimento obrigatório e não foi informado”\.*

ou

*     “O Produto Transferência de Débito \(Saída\) é de preenchimento obrigatório e não foi informado”\.*

Unidade Padrão

Alfanumérico

__S__

S

Pastinha \+ grupo \+  código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Unidade Padrão \(SAFX2017\)\.

Serão disponibilizadas para seleção apenas os registros da SAFX2017 cujo do Grupo foi selecionado na abertura da janela\.

Se o código da unidade padrão for digitado, deve recuperar o registro do grupo e código em questão e de máxima validade\. 

Caso o código da unidade padrão digitado não exista na tabela SAFX2017, exibir a mensagem: 

     *“O Código da Unidade Padrão não está cadastrado ou não pertence ao Grupo”\.*

Se a unidade padrão não estiver preenchida, exibir a mensagem:

*     “A Unidade Padrão é de preenchimento obrigatório e não foi informada”\.*

Unidade Medida

Alfanumérico

__S__

S

Pastinha \+ grupo \+  código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Unidade de Medida \(SAFX2007\)\.

Serão disponibilizadas para seleção apenas os registros da SAFX2007 cujo do Grupo foi selecionado na abertura da janela\.

Se o código da unidade de medida for digitado, deve recuperar o registro do grupo e código em questão e de máxima validade\. 

Caso o código da unidade de medida digitado não exista na tabela SAFX2007, exibir a mensagem: 

     *“O Código da Unidade de Medida não está cadastrado ou não pertence ao Grupo”\.*

Se a unidade de medida não estiver preenchida, exibir a mensagem:

*     “A Unidade de Medida é de preenchimento obrigatório e não foi informada”\.*

- CFOP – Transferência de Crédito \(Entrada\)
- CFOP – Transferência de Crédito \(Saída\)
- CFOP – Transferência de Débito \(Entrada\)
- CFOP – Transferência de Débito \(Saída\)

Alfanumérico

__S__

S

Pastinha \+ código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro de CFOP \(SAFX2012\)\.

Se o código do CFOP for digitado, deve recuperar o registro do código em questão de máxima validade\. 

Caso o código do CFOP digitado não exista na tabela SAFX2012, exibir a mensagem, dependendo do campo que está sendo criticado: 

     *“O Código do CFOP Transferência de Crédito \(Entrada\) não está cadastrado”\.*

Ou

     *“O Código do CFOP Transferência de Crédito \(Saída\) não está cadastrado”\.*

Ou

     *“O Código do CFOP Transferência de Débito \(Entrada\) não está cadastrado”\.*

Ou

     *“O Código do CFOP Transferência de Débito \(Saída\) não está cadastrado”\.*

Se o CFOP não estiver preenchido, exibir a mensagem, dependendo do campo que está sendo criticado:

*     “O CFOP Transferência de Crédito \(Entrada\) é de preenchimento obrigatório e não foi informado”\.*

Ou

*     “O CFOP Transferência de Crédito \(Saída\) é de preenchimento obrigatório e não foi informado”\.*

Ou

*     “O CFOP Transferência de Débito \(Entrada\) é de preenchimento obrigatório e não foi informado”\.*

Ou

*     “O CFOP Transferência de Débito \(Saída\) é de preenchimento obrigatório e não foi informado”\.*

- Natureza Operação – Transferência de Crédito \(Entrada\)
- Natureza Operação – Transferência de Crédito \(Saída\)
- Natureza Operação – Transferência de Débito \(Entrada\)
- Natureza Operação – Transferência de Débito \(Saída\)

Alfanumérico

__N__

S

Pastinha \+ grupo \+  código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro da Natureza Operação \(SAFX2006\)\.

Serão disponibilizadas para seleção apenas os registros da SAFX2006 cujo do Grupo foi selecionado na abertura da janela\.

Se o código da natureza da operação for digitado, deve recuperar o registro do grupo e código em questão e de máxima validade\. 

Caso o código da natureza da operação digitado não exista na tabela SAFX2006, exibir a mensagem, dependendo do campo que está sendo criticado: 

     *“O Código da Natureza da Operação Transferência de Crédito \(Entrada\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código da Natureza da Operação Transferência de Crédito \(Saída\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código da Natureza da Operação Transferência de Débito \(Entrada\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código da Natureza da Operação Transferência de Débito \(Saída\) não está cadastrado ou não pertence ao Grupo”\.*

Depois, verificar se o CFOP e a Natureza de Operação estão cadastrados na tabela de Cadastro de Extensão CFOP \(SAFX2081\)\.  Esta verificação deve ser feita com os seguintes pares de campos:

\- CFOP \+ Natureza Operação da Transferência de Crédito Entrada

\- CFOP \+ Natureza Operação da Transferência de Crédito Saída

\- CFOP \+ Natureza Operação da Transferência de Débito Entrada

\- CFOP \+ Natureza Operação da Transferência de Débito Saída

Caso não exista cadastro, exibir a mensagem referente ao par de campos que ficou inválido:

*“O Código da CFOP \+ Natureza de Operação da Transferência de Crédito Entrada não estão cadastrados na Tabela de Extensão CFOP”\.*

*“O Código da CFOP \+ Natureza de Operação da Transferência de Crédito Saída não estão cadastrados na Tabela de Extensão CFOP”\.*

*“O Código da CFOP \+ Natureza de Operação da Transferência de Débito Entrada não estão cadastrados na Tabela de Extensão CFOP”\.*

*“O Código da CFOP \+ Natureza de Operação da Transferência de Débito Saída não estão cadastrados na Tabela de Extensão CFOP”\.*

- Observação – Transferência de Crédito \(Entrada\)
- Observação – Transferência de Crédito \(Saída\)
- Observação – Transferência de Débito \(Entrada\)
- Observação – Transferência de Débito \(Saída\)

Alfanumérico

__N__

S

Pastinha \+ grupo \+  código \+ validade \+ descrição

Este campo trabalha com janela de seleção da Tabela de Cadastro de Observações \(SAFX2009\)\.

Serão disponibilizadas para seleção apenas os registros da SAFX2009 cujo do Grupo foi selecionado na abertura da janela\.

Se o código da observação for digitado, deve recuperar o registro do grupo e código em questão e de máxima validade\. 

Caso o código da observação digitado não exista na tabela SAFX2009, exibir a mensagem, dependendo do campo que está sendo criticado: 

     *“O Código de Observação Transferência de Crédito \(Entrada\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código de Observação Transferência de Crédito \(Saída\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código de Observação Transferência de Débito \(Entrada\) não está cadastrado ou não pertence ao Grupo”\.*

Ou

     *“O Código de Observação Transferência de Débito \(Saída\) não está cadastrado ou não pertence ao Grupo”\.*

Nenhum código de observação parametrizado nesta tela pode existir na parametrização dos “Dados para Geração de Documentos Fiscais”, para o estabelecimento em questão \(vide menu Manutenção 🡪 Parâmetros Transferência de Crédito/Débito Automática 🡪 “Dados para Geração de Documentos Fiscais”\)\.

Para isso, verificar se os códigos de observação estão parametrizados para o estabelecimento na tabela ICT\_PAR\_TC\_ESTAB\. Caso afirmativo, exibir a mensagem:

     *“O Código de Observação Transferência de Crédito \(Entrada\) não pode ser o mesmo Código de Observação cadastrado em Dados para Geração de Documentos Fiscais\. O código de Observação cadastrado em Dados para Geração de Documentos Fiscais pode ser excluído, uma vez que os codigos de observações estão sendo cadastrados nesta parametrização\. \(vide menu Manutenção > Parâmetros Transferência de Crédito/Débito Automática > Dados para Geração de Documentos Fiscais\)”\.*

Ou

     *“O Código de Observação Transferência de Crédito \(Saída\) não pode ser o mesmo Código de Observação cadastrado em Dados para Geração de Documentos Fiscais\. O código de Observação cadastrado em Dados para Geração de Documentos Fiscais pode ser excluído, uma vez que os codigos de observações estão sendo cadastrados nesta parametrização\. \(vide menu Manutenção > Parâmetros Transferência de Crédito/Débito Automática > Dados para Geração de Documentos Fiscais\)”\.*

Ou

     *“O Código de Observação Transferência de Débito \(Entrada\) não pode ser o mesmo Código de Observação cadastrado em Dados para Geração de Documentos Fiscais\. O código de Observação cadastrado em Dados para Geração de Documentos Fiscais pode ser excluído, uma vez que os codigos de observações estão sendo cadastrados nesta parametrização\. \(vide menu Manutenção > Parâmetros Transferência de Crédito/Débito Automática > Dados para Geração de Documentos Fiscais\)”\.*

Ou

     *“O Código de Observação Transferência de Débito \(Saída\) não pode ser o mesmo Código de Observação cadastrado em Dados para Geração de Documentos Fiscais\. O código de Observação cadastrado em Dados para Geração de Documentos Fiscais pode ser excluído, uma vez que os codigos de observações estão sendo cadastrados nesta parametrização\. \(vide menu Manutenção > Parâmetros Transferência de Crédito/Débito Automática > Dados para Geração de Documentos Fiscais\)”\.*

Filtro UF

Filtro com as UF’s para ser aplicado a lista de estabelecimentos para replicação\.

Replicar para os Estabelecimentos

Apresentar os demais estabelecimentos da empresa que na Relação Tabela Grupo \(RELAC\_TAB\_GRUPO\) possuam o grupo que foi selecionado na janela padrão de seleção de Estabelecimento/Grupo/Validade e código da tabela “2013”\.

       = = = = = =

