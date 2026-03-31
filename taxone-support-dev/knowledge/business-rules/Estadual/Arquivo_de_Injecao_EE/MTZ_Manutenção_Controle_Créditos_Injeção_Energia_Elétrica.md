# MTZ_Manutenção_Controle_Créditos_Injeção_Energia_Elétrica

- **Fonte:** MTZ_Manutenção_Controle_Créditos_Injeção_Energia_Elétrica.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 33 KB

---

__THOMSON REUTERS__

__Manutenção do Controle de Créditos de Injeção de Energia Elétrica__

__Módulo Arquivo de Injeção de Energia Elétrica__

Localização: Módulo Estadual >> Arquivo de Injeção de Energia Elétrica

Menu: Obrigações >> Ato Cotepe ICMS 52/2015 >> Manutenção >> Controle de Créditos de Injeção de Energia Elétrica

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS981988

Liliane Assaf

Criação da janela\.

__Sumário__

[__1\. Regras Gerais__	1](#_Toc218014807)

[__2\. Layout da Tela__	1](#_Toc218014808)

[__3\. Regras de Funcionamento dos Campos__	1](#_Toc218014809)

# <a id="_Toc218014807"></a>__1\. Regras Gerais__

  
A tela de manutenção "Controle de Créditos de Injeção de Energia Elétrica" tem como finalidade possibilitar o cadastro, consulta, alteração e exclusão dos registros referentes ao controle de crédito de injeção de energia elétrica\. O objetivo é garantir o correto carregamento das informações para geração do Arquivo de Créditos, conforme estabelecido pelo Ato Cotepe ICMS nº 52, de 25 de novembro de 2015\.

Essas informações também podem ser importadas a partir da SAFX433\.

# <a id="_Toc218014808"></a>__2\. Layout da Tela__

Estabelecimento:                                             \[xxxxxx\-xxxxxxxxxxxxxxxxxx  \\/\]     

Período Apuração:                                           \[MM/AAAA\]  

Num Instalação Unidade Injetora:                \[xxxxxxxxxxxx\]  

Período Injeção:                                               \[MM/AAAA\] 

Posto Tarifário Energia Injetada:                   \[FP – Fora de Ponta       \\/\]

Vlr\. Tarifa Energia Injetada:                            \[00000,000000\] 

Qtde Inicial de Energia \(kWh\):                       \[0000000000,000\] 

Qtde Energia Injetada \(kWh\):                         \[000000000,000\]

Qtde Saída de Energia \(kWh\):                        \[000000000,000\] 

Qtde Final de Energia \(kWh\):                         \[0000000000,000\]

No Processo:                                                     \[xxxxxxxxxxxx\]

__Tabela Definitiva:__

X433\_CTRL\_CRED\_EE

Campos que fazem parte da PK:

- Empresa
- Estabelecimento 
- Período de Referência da Apuração 
- Número da Instalação da Unidade Injetora 
- Período de Referência da Injeção 
- Posto Tarifário da Energia Injetada

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar a parametrização para um novo estabelecimento\. 

ABRE

Exibe janela de pesquisa dos dados já parametrizados, para que o usuário selecione a parametrização <a id="OLE_LINK4"></a>desejada a ser exibida em tela\.

EXCLUI

Opção para excluir a parametrização de um estabelecimento

CONFIRMA

Opção para salvar os dados da parametrização incluída / alterada\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc218014809"></a>__3\. Regras de Funcionamento dos Campos__

__Estabelecimento \(COD\_ESTAB\)__

- Obrigatoriedade: Campo obrigatório\.
- Tipo: Lista demonstrando Código \+ Razão Social dos Estabelecimentos da Empresa de login
- Caso o estabelecimento seja informado no login do Manager, este campo deve ser apresentado desabilitado\. 
- Caso contrário, este campo será habilitado e apresentar uma lista contendo todos os estabelecimentos da empresa de login\.
- Consistência de Salvamento: 
	- Se não preenchido, ao salvar o registro exibir a mensagem: "*Campo Estabelecimento deve ser preenchido*"\.

__Período Apuração \(DAT\_APURACAO\)__

- Obrigatoriedade: Campo obrigatório\.
- Tipo: Texto com formato MM/YYYY\.
- Gravar o campo DAT\_APURACAO com o último dia do mês/ano informado
- Consistência de Salvamento: 
	- Se não preenchido, ao salvar o registro exibir a mensagem: "*Campo Período Apuração deve ser preenchido*"

__Num Instalação Unidade Injetora \(NUM\_INSTAL\_INJ\)__

- Obrigatoriedade: Campo obrigatório\.
- Tipo: Texto de livre digitação \(12 caracteres alfanuméricos\)\.
- Consistência de Salvamento: 
	- Se não preenchido, ao salvar o registro exibir a mensagem: "*Campo Núm Instalação Unidade Injetora deve ser preenchido*"

__Período Injeção \(DAT\_REF\_INJ\)__

- Obrigatoriedade: Campo obrigatório\.
- Tipo: Texto com formato MM/YYYY\.
- Gravar o campo DAT\_REF\_INJ com o último dia do mês/ano informado
- Consistência de Salvamento: 
	- Se não preenchido, ao salvar o registro exibir a mensagem: "*Campo Período Injeção deve ser preenchido*"

__Posto Tarifário Energia Injetada \(COD\_POSTO\_INJ\)__

- Obrigatoriedade: Campo obrigatório\.
- Tipo: ListBox composta pelos itens:
	- FP – Fora de Ponta
	- IN – Intermediário
	- PO – Ponta
- Consistência de Salvamento: 
	- Se não preenchido, ao salvar o registro exibir a mensagem: "*Campo Posto Tarifário Energia Injetada deve ser preenchido*"

__Vlr\. Tarifa Energia Injetada \(VLR\_TARIFA\_INJ\)__

- Obrigatoriedade: Campo opcional\.
- Tipo: Numérico \(5 inteiros e 6 decimais\)\.

__Qtde Inicial de Energia \(kWh\) \(QTD\_ENERGIA\_INI\)__

- Obrigatoriedade: Campo opcional\.
- Tipo: Numérico \(10 inteiros e 3 decimais\)\.

__Qtde Energia Injetada \(kWh\) \(QTD\_ENERGIA\_INJ\)__

- Obrigatoriedade: Campo opcional\.
- Tipo: Numérico \(9 inteiros e 3 decimais\)\.

__Qtde Saída de Energia \(kWh\) \(QTD\_ENERGIA\_SAI\)__

- Obrigatoriedade: Campo opcional\.
- Tipo: Numérico \(9 inteiros e 3 decimais\)\.

__Qtde Final de Energia \(kWh\) \(QTD\_ENERGIA\_FIM\)__

- Obrigatoriedade: Campo opcional\.
- Tipo: Numérico \(10 inteiros e 3 decimais\)\.

__No Processo \(NUM\_PROCESSO\)__

- Desabilitado
- Número do Processo gravado pela importação da SAFX433\.
- Se o registro for incluído via tela, gravar zero\.

__Ind Gravacao \(IND\_GRAVACAO\):__

- Não apresentar na tela\. 
- Valores padrão do campo \(tabelas de importação\):
	- 1\.  Incluído por Importação
	- 2\.  Atualizado por Importação
	- 3\.  Incluído por Importação / Atualizado por Digitação
	- 4\.  Incluído por Digitação
	- 5\.  Incluído por Digitação / Atualizado por Digitação

__Usuário __

- Não apresentar na tela\. 
- Gravar o usuário de login da aplicação\.

