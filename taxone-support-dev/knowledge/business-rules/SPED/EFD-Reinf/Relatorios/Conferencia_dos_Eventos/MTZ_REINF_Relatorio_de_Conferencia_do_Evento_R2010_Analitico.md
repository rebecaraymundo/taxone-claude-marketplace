# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2010_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2010_Analitico.docx
- **Modificado:** 2025-10-15
- **Tamanho:** 122 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento R\-2010 \- Analítico__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios 🡪 Conferência dos Eventos 🡪 R\-2010

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS15340

Lara Aline

Alteração do Modulo REINF para criação de um relatório de conferência do evento R\-2010\. Novo relatório 🡪 “Relatório de Conferência do Evento R\-2010”\. 

04/01/2018

\(criação do documento\)

MFS18226

Lara Aline

Inclusão do campo Tipo de Ambiente

04/06/2018

MFS18964

Lara Aline

Ajuste no campo CNPJ Prestador para recuperar a razão social mais atual\.

06/06/2018

MFS18433

Lara Aline

Inclusão filtro por Prestador e inclusão de totalização dos valores

29/06/2018

MFS20732

Lara Aline

Inclusão do campo Data Fiscal

03/09/2018

MFS21968

Eduardo Cruz

Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo

20/02/2019

MFS39407

Alessandra Cristina Navatta

Inclusão do campo Indicativo CPRB

30/06/2020

MFS533595

Rogério Ohashi

Alteração da regra de recuperação dos registros para desconsiderar os eventos com Status de Exclusão \(Evento Excluído na Mensageria\)\.

29/05/2023

__MFS572946__

Rosemeire Santos

Alteração da regra de para considerar o envio do novo evento após o evento de Exclusão \(Evento Excluído na Mensageria\)\.

03/10/2023

MFS[938875](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/938875)

Rogério Ohashi

Inclusão do parâmetro “Razão Social”, se desmarcado não será gerado a informação de Razão Social na coluna “CNPJ Prestador” melhorando consideravelmente o tempo de geração

15/10/2025

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc489284546)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	4](#_Toc489284547)

[2\.1\.	Layout do Relatório	9](#_Toc489284548)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc489284546"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios  Conferência dos Eventos  R\-2010 

__Título da tela: __Relatório de Conferência do Evento R\-2010

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS15340

Período

Data 

S

S

Formato: MM/AAAA 

Default: Habilitado

Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA\. 

Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório\.

MFS15340

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS18226

Prestador do Serviço – __Todos__

Alfanumérico

N

S

Default:

Opção “Todos” marcada

Na abertura da tela a opção “__*Todos*__” aparecerá sempre marcada, e o campo “CNPJ” fica *desabilitado*;

Caso o usuário desmarque a opção “__*Todos*__”, o campo “CNPJ” será habilitado, e o usuário poderá informar o CNPJ do prestador\.

MFS18433

Prestador do Serviço – __CNPJ__

Alfanumérico

N

S

Na abertura da tela este campo aparecerá sempre *desabilitado*;

Será habilitado apenas quando o usuário desmarcar a opção “__*Todos*__”\.

Quando preenchido, deve ser um CNPJ válido, caso contrário, será exibida uma mensagem \(ex: “*CNPJ inválido*”\)\.

Sempre que a opção “__*Todos*__” estiver desmarcada, será obrigatório informar o CNPJ do prestador antes de solicitar a emissão do relatório\. Caso contrário, será exibida uma mensagem \(ex: “*Informar o CNPJ do Prestador do Serviço*”\)\.

MFS18433

Razão Social

CheckBox

N

S

Default: Selecionado

Caso o usuário desmarque essa opção o Relatório será gerado sem a informação da Razão Social do Prestador de Serviço, na coluna CNPJ do Prestador, e passará a ser informado somente a informação de CNPJ 

MFS[938875](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/938875)

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento\. 

MFS15340

Estabelecimentos

CheckBox

S

S

Default: não selecionado

Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD\-Reinf\. 

A partir do parâmetro “Geração Multiempresa”, a lista passou a funcionar da seguinte forma:

\- Caso o parâmetro “Geração Multiempresa” estiver desmarcado:

Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo\.

XXXXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento\)\. 

    

\- Caso o parâmetro “Geração Multiempresa” estiver marcado:

Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas:

XXXXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento\)

       

Obs: No caso da geração multiempresa, as regras da geração do relatório não se modificam\. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas\.

O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório\.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”

Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”\.

MFS15340

# <a id="_Toc427766287"></a><a id="_Toc489284547"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-2010 \(SAFX04, SAFX07, SAFX08, SAFX09 e Cadastro do Estabelecimento\)\.

__Regra de seleção: __

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração\.

      \-Empresa = empresa do login      

      \-Período = período informado em tela

      \- Versão = versão informada em tela

      \-Tipo = tipo de relatório informado em tela

      \-Estabelecimento = estabelecimento informado em tela

    

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório\. 

__Regra de processamento: __

__ __

__\[MFS533595\] __Tratamento p/ desconsiderar os eventos com status de exclusão\.

Para cada estabelecimento selecionado em tela será gerado um relatório\. 

Serão recuperadas as informações do evento R\-2010 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento/Obra, Prestador, NFs e Tipo de Serviço\. Será recuperado sempre a última ocorrência do evento R\-2010, exceto para os eventos com status de exclusão \(Evento Excluído na Mensageria\), pois não devem ser considerados no Relatório\.

__\[MFS572946\] Complemento da regra da \[MFS533595\], para considerar o envio do novo evento R\-2010, após evento de exclusão\.__

Para o evento que teve exclusão e está com status de exclusão \(Evento Excluído na Mensageria\), SE o evento tiver uma nova geração, o mesmo deverá ser demonstrado no relatório, por Estabelecimento/Obra, Prestador, NFs e Tipo de Serviço\. Será recuperado sempre a última ocorrência do evento

__\[MFS18433\]__

__Obs\.: __Ao final do relatório nos campos de valores deve ser realizada uma totalização dos valores gerados no relatório\.

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

          \- Empresa 

          \- Estabelecimento

          \- Nota Fiscal 

  


Segue regras do preenchimento dos dados no relatório:

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Empresa

Texto

Razão social da empresa\.

MFS15340

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS15340

Página

Numérico

Número da página sequencial do relatório

MFS15340

Título

Texto

Título do relatório: “Relatório de Conferência do R\-2010”

MFS15340

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS15340

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS15340

ID Evento

Texto

Campo ID\_EVENTO gravado na tabela REINF\_PGER\_R2010\_OC 

MFS21968

Data Evento

Data

Formato: DD/MM/YYYY HH:MM:SS

Campo DAT\_OCORRENCIA gravado na tabela REINF\_PGER\_R2010\_OC

MFS21968

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R2010\_OC

MFS21968

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R2010\_OC

MFS21968

Tipo Inscrição Estabelecimento Tomador

Alfanumérico 

Tipo Inscrição Estabelecimento Tomador, gerado no campo tpInscEstab do evento R\-2010\.

MFS15340

Número Inscrição Estabelecimento Tomador

Alfanumérico 

Número Inscrição Estabelecimento Tomador, gerado no campo nrInscEstab do evento R\-2010\.

MFS15340

CNPJ Prestador

Alfanumérico 

Demostrar o CNPJ \(cnpjPrestador\) \+ Razão Social do Prestador gerado no evento R\-2010 \(CPF\_CGC da SAFX04\)\.

A razão social será buscada da tabela SAFX04 conforme o CNPJ do Prestador do evento R\-2010\. Será recuperada a Razão Social de validade mais atual do Prestador\.

MFS15340

MFS18964

__Corpo do Relatório – Detalhamento das Notas Fiscais de Serviços Prestados__

N° Nota Fiscal

Alfanumérico

Número da Nota Fiscal \(NUM\_DOCFIS\) SAFX08 ou SAFX09, gerado no campo numDocto do evento R\-2010\.

MFS15340

Série

Alfanumérico

Série da Nota Fiscal \(SERIE\_DOCFIS\) SAFX08 ou SAFX09, gerado no campo serie do evento R\-2010\.

MFS15340

Data de Emissão

Data

DD/MM/AAAA

Data de Emissão da Nota Fiscal \(DATA\_EMISSAO\) SAFX07, gerado no campo dtEmissaoNF do evento R\-2010\.

MFS15340

Data Fiscal

Data

DD/MM/AAAA

Data Fiscal da Nota Fiscal \(DATA\_SAIDA\_REC\) SAFX07

MFS20732

Valor Bruto

Numérico

Default: 0,000

Valor Bruto \(VLR\_ITEM da SAFX08 ou VLR\_TOT da SAFX09\), gerado no campo vlrBruto do evento R\-2010\.

MFS15340

Observações

Alfanumérico

Observação \(OBS\_REINF\) SAFX07, gerado no campo obs do evento R\-2010\.

MFS15340

__Corpo do Relatório – Informações sobre os tipos de Serviços constantes da Nota Fiscal__

Tipo Serviço

Alfanumérico

Tipo de serviço correspondente gerado no campo tpServico do evento R\-2010\.

Pela SAFX08:

Tipo de serviço vinculado ao Código do produto parametrizado na tela de “Identificador do Tipo de Serviço > Por Produto” Menu: Retenções Previdenciárias>> Parâmetros

Pela SAFX09:

Tipo de Serviço vinculado ao código do serviço prestado parametrizado na tela de “Identificador do Tipo de Serviço” Menu: Retenções Previdenciárias>> Parâmetros                 

MFS15340

Valor Base Retenção

Numérico

Default: 0,000

Valor Base Retenção \(VLR\_BASE\_INSS\) SAFX08 ou SAFX09, gerado no campo vlrBaseRet do evento R\-2010\.

MFS15340

Valor Retenção 

Numérico

Default: 0,000

Valor Retenção \(VLR \_INSS\_RETIDO\) SAFX08 ou SAFX09, gerado no campo vlrRetencao do evento R\-2010\.

MFS15340

Valor Retenção Subcontratados

Numérico

Default: 0,000

Valor Retenção Subcontratados \(VLR\_RET\_SERV\) SAFX08 ou SAFX09, gerado no campo vlrRetSub do evento R\-2010\.

MFS15340

Valor Não Retenção Principal

Numérico

Default: 0,000

Valor Não Retenção Principal \(VLR\_N\_RET\_PRINC\) SAFX08 ou SAFX09, gerado no campo vlrNRetPrinc  do evento R\-2010\.

MFS15340

Valor Serviços 15 anos

Numérico

Default: 0,000

Valor Serviços 15 anos \(VLR\_SERV\_15\) SAFX08 ou SAFX09, gerado no campo vlrServicos15 do evento R\-2010\.

MFS15340

Valor Serviços 20 anos

Numérico

Default: 0,000

Valor Serviços 20 anos \(VLR\_SERV\_20\) SAFX08 ou SAFX09, gerado no campo vlrServicos20 do evento R\-2010\.

MFS15340

Valor Serviços 25 anos

Numérico

Default: 0,000

Valor Serviços 25 anos \(VLR\_SERV\_25\) SAFX08 ou SAFX09, gerado no campo vlrServicos25 do evento R\-2010\.

MFS15340

Valor Adicional

Numérico

Default: 0,000

Valor Adicional \(VLR\_TOT\_ADIC\) SAFX08 ou SAFX09, gerado no campo vlrAdicional do evento R\-2010\.

MFS15340

Valor Não Retenção Adicional

Numérico

Default: 0,000

Valor Não Retenção Adicional \(VLR\_N\_RET\_ADIC\) SAFX08 ou SAFX09, gerado no campo lrNRetAdic do evento R\-2010\.

MFS15340

Indicativo CPRB

Alfanumérico

Indicativo CPRB, gerado no campo indCPRB do evento R\-2010\.

MFS39407

__Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária__

Tipo Processo Retenção Principal

Alfanumérico

Tipo Processo Retenção Principal \(IND\_TP\_PROC\_ADJ\_PRINC\) SAFX08 ou SAFX09 correspondente gerado no campo tpProcRetPrinc do evento R\-2010\.  

MFS15340

Número Processo Retenção Principal

Alfanumérico

Número Processo Retenção Principal \(NUM\_PROC\_ADJ\_PRINC\) SAFX08 ou SAFX09 correspondente gerado no campo nrProcRetPrinc do evento R\-2010\.  

MFS15340

Código Suspenção Principal

Alfanumérico

Código Suspenção Principal \(COD\_SUSP\_PRINC\) SAFX08 ou SAFX09 correspondente gerado no campo codSuspPrinc do evento R\-2010\.  

MFS15340

Valor Principal

Numérico

Default: 0,000

Valor Principal \(VLR\_N\_RET\_PRINC\) SAFX08 ou SAFX09, gerado no campo valorPrinc do  evento R\-2010\.

MFS15340

__Corpo do Relatório – Informações de processos relacionados a não retenção de contribuição previdenciária adicional__

Tipo Processo Retenção Adicional

Alfanumérico

Tipo Processo Retenção Principal \(IND\_TP\_PROC\_ADJ\_ADIC\) SAFX08 ou SAFX09 correspondente gerado no campo pProcRetAdic do evento R\-2010\.  

MFS15340

Número Processo Retenção Adicional

Alfanumérico

Número Processo Retenção Principal \(NUM\_PROC\_ADJ\_ADIC\) SAFX08 ou SAFX09 correspondente gerado no campo nrProcRetAdic do evento R\-2010\.  

MFS15340

Código Suspenção Adicional

Alfanumérico

Código Suspenção Principal \(COD\_SUSP\_ADIC\) SAFX08 ou SAFX09 correspondente gerado no campo codSuspAdic do evento R\-2010\.  

MFS15340

Valor Adicional

Numérico

Default: 0,000

Valor Principal \(VLR\_N\_RET\_ADIC\) SAFX08 ou SAFX09, gerado no campo valorAdic do evento R\-2010\.

MFS15340

## <a id="_Toc427766288"></a><a id="_Toc489284548"></a>Layout do Relatório

![](data:image/png;base64,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) ![](data:image/png;base64,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)

