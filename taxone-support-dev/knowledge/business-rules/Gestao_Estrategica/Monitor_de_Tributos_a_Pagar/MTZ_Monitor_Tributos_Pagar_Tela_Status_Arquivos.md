# MTZ_Monitor_Tributos_Pagar_Tela_Status_Arquivos

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Status_Arquivos.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 83 KB

---

	    

THOMSON REUTERS

Monitor de Tributos

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3962\-A

Criação da Tela de Status dos Arquivos Gerados

O objetivo deste documento é definir as regras para a tela de Status dos Arquivos Gerados\.

OS3962\-B

Criação da Tela de Status dos Arquivos Gerados

Inclusão da opção “Federal” no campo “Grupo Tributo” e das opções “IRPJ”, “IRRF”, “PIS”, “COFINS” e “CSLL” no campo “Tributo da tela de parametrização de layout\.

OS3962\-C

Criação da Tela de Status dos Arquivos Gerados 

Inclusão da opção “Previdenciário” no campo “Grupo Tributo” e da opção “INSS” no campo “Tributo da tela de parametrização de layout\.

MFS\-1685

Inclusão de Tributo

Atualização da tela Status dos Arquivos Gerados para que demonstre o imposto IPI

MFS\-1683

Inclusão de Tributo

Atualização da tela Status dos Arquivos Gerados para que demonstre o imposto ICMS

MFS\-1686

Inclusão de Tributo

Atualização da tela Status dos Arquivos Gerados para que demonstre os impostos PIS/PASEP e COFINS\.

MFS\-1684

Inclusão de Tributo

Atualização da tela Status dos Arquivos Gerados para que demonstre o imposto ICMS\-ST

MFS\-1689

Ajuste na tela de Status

Criação de campos na tela de Status dos Arquivos

MFS\-5049

Alteração de Regra

Status Pago Automático – Retroalimentação da SAFX75

MFS\-6310

Ajuste na tela de Status

Alteração na regra para os status Pago Manual e Pago Automático

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc370119652)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc370119653)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc370119654)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc370119655)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc370119656)

[2\.	Regras dos Campos	4](#_Toc370119657)

# <a id="_Toc370119652"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc370119653"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc370119654"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema\.

__Pré\- Condições__

Estar logado no produto MasterSAF DW\. 

__Pós\-Condições__

Não se aplica\.

<a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a>

### <a id="_Toc370119655"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc370119656"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc370119657"></a>Regras dos Campos 

__Localização da tela:__ Geração >> Status dos Arquivos 

__Título da tela: __Status dos Arquivos 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Lista

S

S

Listagem dos estabelecimentos \(default: estabelecimento selecionado no Manager\)

Deverá exibir a lista dos estabelecimentos pertencentes à empresa logada, juntamente com a opção “Todos”\.

OS3962\-A

Data Inicial

Data

S

S

A data deverá ser informada no formato dd/mm/aaaa\. Por default não estará preenchida\.

Caso o campo não esteja preenchido deve ser exibida a seguinte mensagem de erro: “Informe Data Inicial”\.

OS3962\-A

Data Final

Data

S

S

A data deverá ser informada no formato dd/mm/aaaa\. Por default não estará preenchida\.

A Data Final informada deve ser maior ou igual a Data Inicial\. Caso seja informada uma data menor, retornar a mensagem: “Data Final deve ser maior ou igual a Data Inicial”\.

Caso o campo não esteja preenchido deve ser exibida a seguinte mensagem de erro: “Informe Final”\.

Caso o campo seja menor do que o campo Data Inicial deve ser exibida a seguinte mensagem de erro: “A Data Final deve ser maior ou igual a Data Inicial”\.

OS3962\-A

Grupo Tributo

Lista

S

S

Lista com as opções \(default: não preenchido\)

Preencher conforme abaixo:

     Todos

1 – Federal

2 – Estadual 

3 – Municipal 

4 – Previdenciário

Caso o campo nao esteja preenchido, deve ser exibida a seguinte mensagem de erro: “Informe Grupo Tributo”\.

Obs: Não serão apresentados os respectivos “números” dos tributos, apenas a descrição\. Estes números serão a referencia para o campo “grupo\_tributo” da TFIX140\.

OS3962\-A

OS3962\-B

MFS\-1683

Tributo

Lista

S

S

Lista com as opções \(default: não preenchido\)

Será habilitado quando for informado o Grupo Tributo, demonstrando apenas os Tributos relacionados ao Grupo indicado, conforme regras abaixo:

Para o Grupo Federal, demonstrar as opções:

- TODOS
- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS 
- IPI
- PIS/PASEP \(PRÓPRIO\)
- COFINS \(PRÓPRIO\)

\[MFS\-6310\]

Para o Grupo Municipal, demonstrar as opções:

- ISS

Para o Grupo Previdenciário, demonstrar as opções:

- INSS

Caso o campo não esteja preenchido, deve ser exibida a mensagem de erro: “Informe Tributo”\.

Obs: Caso a opção “Todos” esteja preenchido no campo “Grupo tributo” este campo receberá o valor “Todos” automaticamente\.

OS3962\-A

OS3962\-B

MFS\-1685

MFS\-1683

MFS\-1686

MFS\-1684

MFS\-6310

Cód\. Tipo Arq

Texto

N

S

MFS\-1689

Cód\.Layout

Texto

N

S

OS3962\-A

Nº do Lote

Texto

N

S

OS3962\-A

Consultar

Botão

S

N

Quando acionado, retornará para a Listagem de Arquivos Gerados a relação de layouts de arquivos gerados considerando a parametrização de Estabelecimento, Data Inicial, Data Final, Grupo Tributo, Tributo, Layout e Nº do Lote\.

Caso um dos campos indicados como obrigatórios \(coluna Obrig = S\) não estiver parametrizado, retornar a mensagem: “Campo obrigatório não parametrizado” e posicionar o cursor sobre o campo que precisa ser indicado\. Se existir mais de um campo, posicionar o cursor sobre o primeiro campo não parametrizado;

Caso não existam registros de arquivos gerados que atendam aos critérios parametrizados, retornar a mensagem: “Não existem informações que atendem aos critérios indicados\. Reveja os critérios de seleção”\.

OS3962\-A

__Listagem de Arquivos Gerados__

Opção de seleção\*

Checkbox

N

S

\(default: desabilitado e não selecionado\)

Este campo estará habilitado para seleção somente quando o conteúdo do campo “Status” for igual a “Enviado”\.

OS3962\-A

Estabelecimento

Texto

S

N

Formato: <Código> \- <Descrição do Estabelecimento>

Com base nos critérios selecionados pelo usuário de estabelecimento, data inicial, data final, grupo tributo e tributo e que o usuário possua direito de acesso, demonstrar o estabelecimento que se enquadra no parametrizado\.

OS3962\-A

Cód\. Tipo Arq 

Texto

S

N

Com base nos parâmetros de seleção da tela demonstrar o código do tipo do arquivo\.

MFS\-1689

Cód\. Layout

Texto

S

N

Com base nos parâmetros de seleção da tela demonstrar o código do layout\.

MFS\-1689

Grupo Tributo

Texto

S

N

Com base nos parâmetros de seleção da tela demonstrar o grupo do tributo\.

MFS\-1689

Tributo

Texto

S

N

Com base nos parâmetros de seleção da tela demonstrar o tributo\.

MFS\-1689

MFS\-1689

MFS\-1689

Data Inicial

Texto

S

N

Formato: DD/MM/AAA

Com base nos critérios selecionados pelo usuário de estabelecimento, data inicial, data final, grupo tributo e tributo, demonstrar a Data Inicial do layout apresentado\.

OS3962\-A

Data Final

Texto

S

N

Formato: DD/MM/AAA

Com base nos critérios selecionados pelo usuário de estabelecimento, data inicial, data final, grupo tributo e tributo, demonstrar a Data Final do layout apresentado\.

OS3962\-A

Lote

Texto

S

N

Com base nos critérios selecionados pelo usuário de estabelecimento, data inicial, data final, grupo tributo e tributo, demonstrar o número de Lote associado ao layout\.

OS3962\-A

ID Geração

Texto 

S

N

Com base nos parâmetros de seleção da tela demonstrar o ID Geração\.

MFS\-1689

Status

Lista

S

S

Lista com as opções

Preencher conforme abaixo:

- Enviado
- Pago \(Manual\)
- Cancelado
- Pago \(Automático\)
- Divergente 
- Rejeitado

Pago \(Manual\): Alteração realizada manualmente pelo usuário, quando não houver importação de arquivo de retorno\.

Cancelado: Alteração realizada manualmente pelo usuário\. 

Divergente: Quando identificado divergência de valor entre o layout de envio e Layout de Retorno no processo de importação\. A alteração para esse status será automática\.

Rejeitado: Quando identificado divergência de layout no momento da importação do arquivo de retorno\. A alteração para esse status será automática\.

Pago \(Automático\): Caso não identificado divergência de valor ou de layout no momento da importação do arquivo de retorno\. A alteração para esse status será automática e deverá atualizar a SAFX75 os campos AUTENT\_BANCARIA e DATA\_PAGTO\. Caso não informado a Data de pagamento não haverá a retroalimentação do campo\.

Obs:

Este campo estará habilitado para edição somente quando o conteúdo informado for igual a “Enviado”, “Pago Manual” e “Pago Automático”\. 

A edição do status “Enviado” poderá ser realizada manualmente apenas para “Pago\(Manual\) e Cancelado”\.

“Pago Manual” e “Pago Automático” poderá ser alterado apenas para “Cancelado”\.

Para outras opções deve estar desabilitado e não deve permitir edição\.

OS3962\-A

MFS\-1689

MFS\-5049

MFS\-6310

Selecionar Todos

Botão

N

N

Quando acionado este botão, todos os registros que tenham Status “Enviado” cuja Opção de Seleção estiver como não selecionada deverá mudar de status para selecionada\.

Caso o usuário acione este botão sem que existam registros com Status “Enviado” com a Opção de Seleção desmarcada, retornar a mensagem: “Não existem registros para serem selecionados”\.

OS3962\-A

Desmarcar Todos

Botão

N

N

Quando acionado este botão, todos os registros que tenham Status “Enviado” cuja Opção de Seleção estiver selecionada deverá mudar de status para não selecionada\.

Caso o usuário acione este botão sem que existam registros com Status “Enviado” com a Opção de Seleção marcada, retornar a mensagem: “Não existem registros para serem desmarcados”\.

OS3962\-A

Pagar Selecionados

Botão

N

N

Caso o usuário acione este botão sem ter marcado a Opção de Seleção de nenhum registro, retornar a mensagem: “Não existem registros selecionados para realização da mudança de Status”\.

Quando acionado este botão, todos os registros cuja Opção de Seleção estiver selecionada e que tenha o campo Status com o conteúdo “Enviado” deverá ser atualizado, mudando o Status para “Pago \(Manual\)”\.

OS3962\-A

Cancelar Selecionados

Botão

N

N

Caso o usuário acione este botão sem ter marcado a Opção de Seleção de nenhum registro, retornar a mensagem: “Não existem registros selecionados para realização da mudança de Status”\.

Quando acionado este botão com a Opção de Seleção selecionada para, ao menos um registros, retornar a mensagem para o usuário: “Atenção, a mudança de Status para Cancelado fará com que os registros já gerados no arquivo voltem ao status de não gerado\. Deseja prosseguir com a alteração?”, com as opções “SIM” e “NÃO”\.

Caso ele escolha “NÃO”, não realizar nenhuma alteração\.

Caso ele escolha “SIM”, todos os registros cuja Opção de Seleção estiver selecionada e que tenha o campo Status com o conteúdo “Enviado” deverá ser atualizado, mudando o Status para “Cancelado” e na tabela de origem da informação \(identificada pelo Grupo Tributo/Tributo\), os registros que tenham a marcação de Estabelecimento, Data Inicial, Data Final, Grupo Tributo, Tributo, Código do Layout e Lote que foi cancelado deve ter a informação do identificador deletada, de forma que o registro estará disponível novamente para geração, assim como a tabela de armazenamentos dos dados gerados deverá ter seus dados deletados para registro\(Lote\) que foi cancelado, para este estar disponível novamente para geração\.

OS3962\-A

MFS\-1689

*\* Descrição não será exibida*

