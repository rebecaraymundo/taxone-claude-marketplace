# MTZ_Report_Fiscal_Saldo_Consolidado_ICMS_SAFX304_XLS

- **Fonte:** MTZ_Report_Fiscal_Saldo_Consolidado_ICMS_SAFX304_XLS.docx
- **Modificado:** 2024-01-11
- **Tamanho:** 73 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo Report Fiscal

Relatório do Saldo Consolidado da Restituição/Complemento de ICMS \(SAFX304\)

__Localização__: Menu Básicos à Report Fiscal, item de menu Obrigações Acessórias à ICMS por Substituição à Operações com Substituição Tributária à Saldo Consolidado Rest\./Compl\. ICMS \(SPED\-EFD 1250 e 1255\) – Formato XLS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS561102

Andréa Rocha

Criação do Relatório do Saldo Consolidado da Restituição/Complemento de ICMS – Formato XLS\.

MFS571642

Graciela Soares

Ajuste na geração do relatório para gerar as informações de todos os estabelecimentos selecionados em um único arquivo no formato XLS\.

Sumário

[TELA A SER DESENVOLVIDA	3](#_Toc47543865)

[1\.	REGRAS DA TELA	3](#_Toc47543866)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	4](#_Toc47543867)

# <a id="_Toc462838137"></a><a id="_Toc47543865"></a>TELA A SER DESENVOLVIDA

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc462838138"></a><a id="_Toc47543866"></a>REGRAS DA TELA

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Data Inicial

Data

S

S

DD/MM/AAAA

Neste campo o usuário informará uma data inicial, a ser utilizada como filtro dos registros do relatório\.

MFS561102

Data Final

Data

S

S

DD/MM/AAAA

Neste campo o usuário informará uma data final, a ser utilizada como filtro dos registros do relatório\.

MFS561102

UF

Alfanumérico

S

S

Listbox

Neste campo será disponibilizada a lista montada com todas as Unidades Federativas, adicionando a opção \* Todas as UFs\*\.

Origem:Tabela ESTADO

Montar a lista começando pela opção \* Todas as UFs\* e as demais opções em ordem crescente pela descrição da UF\.

MFS561102

Estabelecimento

S

S

Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login\. 

Serão disponibilizados para seleção os estabelecimentos que atendam a “UF” informada em tela\.

Para montagem dessa listagem, fazer uma consulta envolvendo a tabela:

    \- ESTABELECIMENTO

     Se campo “UF” for preenchido com opção  \*Todas as Ufs\*:

        Considerar os estabelecimentos de todas as Unidades Federativas

    Senão

       Considerar apenas os estabelecimentos da UF selecionada\. 

Demonstrar os seguintes campos de forma concatenada, na listagem de estabelecimentos:

    \- COD\_ESTAB \+ RAZAO\_SOCIAL 

Incluir a opção de selecionar todos os estabelecimentos\.

MFS561102

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc47543867"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte tabela:

- __SAFX304 __\- Tabela do Saldo Consolidado da Restituição/Complemento de ICMS; 
- Gerar as informações em um único arquivo no Formato XLS de todos os estabeleciemnto selecionados\.

__Regra de seleção do Relatório: __

Deverá criar um relatório de conferência dos dados da tabela do Saldo Consolidado da Restituição/Complemento de ICMS \(SAFX304\) em formato XLS\.

Como filtro para emissão do relatório, deve utilizar um período \(data inicial e data final\) e o estabelecimento\. 

   

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

Empresa

Texto

Código da empresa do login\.

MFS561102

Estabelecimento

Texto

Código do estabelecimento\.

MFS561102

CNPJ

Alfanumérico

Campo CNPJ da tabela Estabelecimento\.

MFS561102

Razão Social

Texto

Campo Razão social da tabela Estabelecimento\.

MFS561102

Data da Apuração

Numérico

Formato: DD/MM/AAAA

Campo 03\- Data da Apuraçãoda SAFX304\.

MFS561102

Código do Motivo

Alfanumérico

Campo 04\- Código do Motivo da SAFX304\.

MFS561102

Valor do ICMS

Numérico

Campo 05\- Valor do ICMS da SAFX304\.

MFS561102

Valor do ICMS\-ST Restituição

Numérico

Campo 06\- Valor do ICMS\-ST Restituição da SAFX304\.

MFS561102

Valor do FCP\-ST  Restituição

Numérico

Campo 07\- Valor do FCP\-ST  Restituição da SAFX304\.

MFS561102

                                                       Valor do ICMS\-ST Complemento

Numérico

Campo 08\- Valor do ICMS\-ST Complemento da SAFX304\.

MFS561102

Valor do FCP\-ST Complemento

Numérico

Campo 09\- Valor do FCP\-ST Complemento da SAFX304\.

MFS561102

