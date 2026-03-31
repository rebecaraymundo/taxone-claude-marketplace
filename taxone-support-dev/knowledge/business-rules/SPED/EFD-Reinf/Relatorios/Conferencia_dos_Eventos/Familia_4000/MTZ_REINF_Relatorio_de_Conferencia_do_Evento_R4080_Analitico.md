# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4080_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4080_Analitico.docx
- **Modificado:** 2024-05-21
- **Tamanho:** 85 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento – Família 4000 \- \(R\-4080 – Analítico\)__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios 🡪 Conferência dos Eventos 🡪 Família 4000

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS\-79907

Alessandra Cristina Navatta

Criação de um relatório de conferência do evento R\-4080 \(analítico\)\. Relatórios 🡪 “Conferência dos Eventos 🡪R\-4080”\.

18/04/2022

MFS\-537238

Alessandra Cristina Navatta

Adequação do relatório, atendendo o layout 2\.1\.2 do REINF:

Inclusão do campo Observ no agrupamento “Informações Relativas ao Recebimento do Rendimento”

20/07/2023

MFS\-594004

Alessandra Cristina Navatta

Criada tela única, para a geração dos relatórios de conferência da família 4000\.

Excluído o layout da versão 2\.1\.1 da documentação

21/12/2023

MFS\-627081

Rosemeire Santos

Inclusão da coluna de status no relatório\. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados \(formato Excel\)\. 

03/04/2024

MFS626907

Andréa Rocha

Retirada a opção de “salvar como” da geração do relatório\.

20/05/2024

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc154068321)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc154068322)

[2\.1\.	Layout do Relatório	12](#_Toc154068323)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc154068321"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000> 

__Título da tela: __Relatório de Conferência dos Eventos – Família 4000

As regras da tela, estão disponíveis no documento MTZ\_REINF\_Tela\_Relatorio\_de\_Conferencia\_do\_Evento\_Familia4000\.docx, link:

[https://trten\.sharepoint\.com/sites/REQ\_MTZ/Mastersaf%20DW%20TaxOne/Documento\_Matriz/SPED/EFD\-Reinf/Relatorios/Conferencia\_dos\_Eventos/Familia\_4000/MTZ\_REINF\_Tela\_Relatorio\_de\_Conferencia\_do\_Evento\_Familia4000\.docx?web=1](https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/SPED/EFD-Reinf/Relatorios/Conferencia_dos_Eventos/Familia_4000/MTZ_REINF_Tela_Relatorio_de_Conferencia_do_Evento_Familia4000.docx?web=1)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Período

Data 

S

S

Formato: MM/AAAA 

Default: Habilitado

Local para digitação do período inicial e final de referência da geração do relatório, no formato de DD/MM/AAAA\. 

Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório\.

MFS\-79907

Versão

Texto

S

S

Default: Versão atual

Este campo exibe as versões de layout do Reinf\. A partir da versão 2\.1\.1

MFS\-79907

Tipo do Relatório

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS\-79907

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS\-79907

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento\. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados\.

MFS\-79907

Estabelecimentos

CheckBox

S

S

Default: não selecionado

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

MFS\-79907

# <a id="_Toc427766287"></a><a id="_Toc154068322"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

__\[MFS626907\] __Retirar a opção de “salvar como”\.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-4080 \(Cadastro do Estabelecimento, SAFX283, SAFX284\)\.

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

Para cada estabelecimento selecionado em tela será gerado um relatório\. 

Serão recuperadas as informações do evento R\-4080 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento, Fonte Pagadora, Natureza de Rendimento, Data do Rendimento e Processos\. 

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

          \- Empresa 

          \- Estabelecimento

          \- Fonte Pagadora

          \- Natureza do Rendimento

			\- Data do Movimento

  


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

MFS\-79907

Página

Numérico

Número da página sequencial do relatório

MFS\-79907

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS\-79907

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-4080 \- Analítico”

MFS\-79907

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS\-79907

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS\-79907

__Informação de Identificação do Evento / Contribuinte__

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4080\_OC

MFS\-79907

Status

Texto

Código\-Descrição

Campo IND\_STATUS gravado na tabela REINF\_PGER\_R4080\_OC

MFS\-627081

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4080\_OC

MFS\-79907

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4080\.

MFS\-79907

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4080\.

MFS\-79907

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4080\.

MFS\-79907

Tipo de Inscrição Estabelecimento

Texto

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4080\.

MFS\-79907

Número Inscrição Estabelecimento

Texto

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4080\.

MFS\-79907

__Corpo do Relatório – Identificação da Fonte Pagadora do Rendimento__

CNPJ da Fonte Pagadora

Alfanumérico

CNPJ da fonte pagadora do rendimento

MFS\-79907

__Corpo do Relatório – Identificação do Rendimento__

Esta parte do relatório demonstra a natureza do rendimento

Natureza do Rendimento

Texto

Natureza do Rendimento, vinculado ao evento R\-4080\.

Valores Válidos:

20001;

20002;

20003;

20004;

20005;

20006;

20007;

20008;

20009;

20010

MFS\-79907

Observações

Texto

Observações

MFS\-79907

__Corpo do Relatório – Informações Relativas ao Recebimento do Rendimento__

Data do Recebimento 

Data 

__DD/MM/AAA__

Data do recebimento vinculado ao evento R4080

MFS\-79907

Valor Bruto

Numérico

0,00

Valor Bruto vinculado ao evento R\-4080\.

MFS\-79907

Valor Base IR

Numérico

0,00

Valor Base IR vinculado ao evento R\-4080\.

MFS\-79907

Valor do Imposto de Renda Retido na Fonte

Numérico

0,00

Valor do Imposto de Renda Retido na Fonte vinculado ao evento R\-4080\.

MFS\-79907

Observ

Texto

Observações

MFS\-537238

__Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais__

Tipo do Processo

Alfanumérico

Tipo de Processo , correspondente o evento R\-4080

Valores Válidos

1\-Administrativo

2\-Judicial

MFS\-79907

Número do Processo

Alfanumérico

Número Processo \(NUM\_PROC\) correspondente gerado no campo nrProc do evento R\-4080\.  

MFS\-79907

Código de Suspenção

Alfaumérico

Código Suspenção \(COD\_SUSP\) correspondente gerado no campo codSusp do evento R\-4080\.  

MFS\-79907

Valor da Base com Exigibilidade Suspensa

Numérico

0,00

Valor da Base com Exigibilidade Suspensa gerado no evento R\-4080

MFS\-79907

Valor da Retenção que Deixou de ser Efetuada

Numérico

0,00

Valor da Retenção que Deixou de ser Efetuada gerado no evento R\-4080

MFS\-79907

Valor do Depósito Judicial

Numérico

0,00

Valor do Depósito Judicial gerado no evento R\-4080

MFS\-79907

## <a id="_Toc427766288"></a><a id="_Toc154068323"></a>Layout do Relatório

__A partir da Versão 2\.1\.2 do REINF__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-4080 – Analítico__

__                                                                                      		Período: 99/9999  __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

__Informação de Identificação do Evento / Contribuinte__

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	    N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           __Tipo Amb\.__ : XXXXXXXXX__        __

__Processo de Emissão: __X\-XXXXXX                 __Versão do Processo de Emissão: __XXXXXXXX              __               __

__Tipo Inscrição Estabelecimento__: X\-XXXXXXXXXXXX                  	__Número Inscrição Estabelecimento__: XXXXX

__Identificação da Fonte Pagadora do Rendimento__

__CNPJ da Fonte Pagadora:__ XX\.XXX\.XXX/XXXX\-XX

__	Identificação do Rendimento	__

__Natureza do Rendimento :__XXXXX

__Observações:__ 

__Informações Relativas ao Recebimento do Rendimento __

__Data do Recebimento__

__Valor Bruto__

__Valor Base IR__

__Valor do Imposto de Renda Retido na Fonte__

__Observ__

DD/MM/AAAA

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

XXXXXXX

__Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais\.__

__Tipo do Processo__

__Número do Processo__

__Código de Suspensão__

Valor da Base com Exigibilidade Suspensa

Valor da Retenção que Deixou de ser Efetuada

Valor do Depósito Judicial

X\- XXXXXXX

xxxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

X\- XXXXXXX

xxxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

X\- XXXXXXX

xxxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

