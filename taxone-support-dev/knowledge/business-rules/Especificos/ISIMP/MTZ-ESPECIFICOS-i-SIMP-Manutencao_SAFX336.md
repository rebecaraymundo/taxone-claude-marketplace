# MTZ-ESPECIFICOS-i-SIMP-Manutencao_SAFX336

- **Fonte:** MTZ-ESPECIFICOS-i-SIMP-Manutencao_SAFX336.docx
- **Modificado:** 2024-10-08
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Módulo i\-SIMP

Tabela dos Produtos Dispensados de Coleta

__Localização__: Menu Específicos, módulo i\-SIMP, menu Geração 🡪 Manutenção à Produto Dispensado de Coleta

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS682665

Andréa Rocha

Criação da tela de manutenção da tabela de Produto Dispensado de Coleta para o i\-SIMP, referente a SAFX336\.

13/09/2024

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Tabela SAFX336 \- Produto Dispensado de Coleta – i\-SIMP\.

Estrutura da tabela: Consultar o Manual Layout\.

Informações gravadas na tabela: X336\_PROD\_DISP\_COLETA

O objetivo dessa tabela é armazenar o volume total dispensado de coleta por produto e por unidade federativa, para gerar o registro Produto Dispensado de Coleta do i\-SIMP\. 

 

# <a id="_Toc451260496"></a>Layout da Tela

__Título da tela: __Produto Dispensado de Coleta

Estabelecimento__:            __\[xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Mês / Ano Referência:    \[mm/aaaa\]

Operação ANP:               \[xxxxxxxxxx\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Cód\. Produto Obrig:        \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Quantidade ANP:            99999999999,9999

Quantidade KG:              99999999999,9999

Pessoa Fis/Jur Terceiro: \[x\-xxxxxxxxxxxxxx\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

UF / Município:                \[XX\] \[99999\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Atividade Econômica Terceiro:     \[9999999\] \[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__ABRE – __Permite abrir seleção de registros inseridos\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__RELATÓRIO – __Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login \(mostrar todos os campos como critério de busca\)\.

__FECHA – __Permite sair da tela\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico

S

S

Listbox

Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário\. 

Caso tenha sido informado um estabelecimento no login, este campo exibirá fixo o estabelecimento informado, e o usuário não poderá alterá\-lo\.

__MFS682665__

Período de Referência

Numérico

S

S

__MM/AAAA__

Campo habilitado para preenchimento de mês/ano de referência\.  Verificar se é um mês válido\.

__MFS682665__

Código Operação ANP

Alfanumérico

S

S

Este campo trabalha com janela de seleção da tabela de Cadastro de Operações das Obrigações – TFIX116 \(PRT\_OPER\_OBRIG\), quando o código do módulo for igual a 361 \(i\-SIMP\)\.

Demonstrar código e descrição\.

Quando o Código da Operação for digitado, será validado a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Código da Operação ANP não cadastrado*”\.* *

__MFS682665__

Código do Produto Operado 

Alfanumérico

S

S

Este campo trabalha com janela de seleção da tabela de Cadastro de Produtos das Obrigações \-TFIX117 \(PRT\_PROD\_OBRIG\), quando o código do módulo for igual a 361 \(i\-SIMP\)\.

Demonstrar código e descrição\.

Quando o Código do Produto Operado for digitado, será validado a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Código do Produto Operado não cadastrado*”\.* *

__MFS682665__

Quantidade ANP

Numérico

N

S

__Formato: ,0000__

Campo texto para digitação de número com 11 inteiros e 4 decimais\.

__MFS682665__

Quantidade KG

Numérico

N

S

__Formato: ,0000__

Campo texto para digitação de número com 11 inteiros e 4 decimais\.

__MFS682665__

Pessoa Física /Jurídica Terceiro

Alfanumérico

N

S

Este campo trabalha com janela de seleção da tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\.

Demonstrar indicador, código e razão social\.

Quando o Indicador e o Código da PFJ forem digitados, será validado a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Pessoa Fìsica / Jurídica não cadastrada*”\.* *

__MFS682665__

UF Coleta

Alfanumérico

S

S

Listbox

Neste campo será exibida a lista das UFs cadastradas na tabela ESTADO\.

__MFS682665__

Município Coleta

Numérico

S

S

Este campo trabalha com janela de seleção da tabela de Município \(MUNICÍPIO\)\.  Deverão ser exibidos os municípios da UF selecionada\.

Demonstrar código e descrição\.

Quando o Código do Município for digitado, será validado a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Código do Município não cadastrado*”\.* *

__MFS682665__

Atividade Econômica Terceiro

Numérico

N

S

Este campo trabalha com janela de seleção da tabela de Cadastro de Atividades Econômicas das Obrigações \-TFIX119 \(PRT\_CNAE\_OBRIG\), quando o código do módulo for igual a 361 \(i\-SIMP\)\.

Demonstrar código e descrição\.

Quando a Atividade Econômica for digitada, será validada a sua existência na tabela\.  Caso não exista, será exibida a mensagem “*Atividade Econômica* *não cadastrada*”\.* *

__MFS682665__

       = = = = = =

