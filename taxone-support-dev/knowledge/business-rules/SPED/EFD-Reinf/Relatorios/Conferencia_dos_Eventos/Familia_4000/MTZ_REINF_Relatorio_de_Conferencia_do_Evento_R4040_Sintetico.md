# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4040_Sintetico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4040_Sintetico.docx
- **Modificado:** 2026-02-16
- **Tamanho:** 85 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento Família 4000 \- \(R\-4040 Sintético\)__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios 🡪 Conferência dos Eventos 🡪 Família 4000

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS\-79893

Alessandra Cristina Navatta

Criação de um relatório de conferência do evento R\-4040 \(sintético\)\. Relatórios 🡪 “Conferência dos Eventos 🡪R\-4040”\.

11/04/2022

MFS\-537211

Alessandra Cristina Navatta

Adequação do relatório, atendendo o layout 2\.1\.2 do REINF:

Inclusão dos campos: 

- Identificador do evento Adicional, no agrupamento Identificação do Evento/Contribuinte

Inclusão de opção válida no campo Natureza de Rendimento \(agrupamento Natureza de Rendimento\)

13/07/2023

MFS\-594003

Alessandra Cristina Navatta

Criada tela única, para a geração dos relatórios de conferência da família 4000\.

Ajustada a informação do layout, a partir da versão 2\.1\.2 \(apenas ajuste em documentação\)

14/02/2024

MFS\-627086

Rosemeire Santos

Inclusão da coluna de status no relatório\. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados \(formato Excel\)\. 

03/04/2024

MFS626907

Andréa Rocha

Retirada a opção de “salvar como” da geração do relatório\.

20/05/2024

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc67385623)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc67385624)

[2\.1\.	Layout do Relatório	14](#_Toc67385625)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc67385623"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios > Conferência dos Eventos > > Família 4000 >

__Título da tela: __Relatório de Conferência do Eventos – Família 4000

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

MFS\-79893

Versão

Texto

S

S

Default: Versão atual

Este campo exibe as versões de layout do Reinf\. A partir da versão 2\.1\.1

MFS\-79893

Tipo do Relatório

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS\-79893

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS\-79893

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento\. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados\.

MFS\-79893

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

MFS\-79893

# <a id="_Toc427766287"></a><a id="_Toc67385624"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

__\[MFS626907\] __Retirar a opção de “salvar como”\.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-4040 \(SAFX279, SAFX282, Cadastro do Estabelecimento\)\.
- Tabela compõem os valores de pagamento/crédito a beneficiários não identificados R\-4040 ; 

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

Serão recuperadas as informações do evento R\-4040 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento, Natureza de Rendimento\. 

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

          \- Empresa 

          \- Estabelecimento

          \- Natureza do Rendimento

			

  


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

MFS\-79893

Página

Numérico

Número da página sequencial do relatório

MFS\-79893

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS\-79893

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-4040 \- Sintético”

MFS\-79893

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS\-79893

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS\-79893

__Informação de Identificação do Evento __

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4040\_OC

MFS\-79893

Status

Texto

Código\-Descrição

Campo IND\_STATUS gravado na tabela REINF\_PGER\_R4040\_OC

MFS\-627086

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4040\_OC

MFS\-79893

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4040\.

MFS\-79893

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4040\.

MFS\-79893

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4040\.

MFS\-79893

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4040\.

MFS\-79893

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4040\.

MFS\-79893

Identificador Evento Adicional

Texto

Identificador de evento adicional por beneficiário, a critério do declarante\.

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-537211

__Corpo do Relatório – Natureza do Rendimento__

Esta parte do relatório demonstra a natureza do rendimento

Natureza do Rendimento

Texto

__Código: Descrição__

Natureza do Rendimento, vinculado ao evento R\-4040\.

__\[ALTERAÇÃO MFS\-537211\]__ Inclusão de natureza de rendimento 12052:

Valores Válidos:

12052;

19001;

19009 

MFS\-79893

__MFS\-537211__

__Corpo do Relatório – Totais de Pagamentos a Beneficiários não Indentificados__

Valor Líquido

Numérico

0,00

Neste campo deve ser considerado o somatório do valor líquido do pagamento a beneficiários do evento R\-4040, independente da data do movimento e sim do período de apuração\.

MFS\-79893

Valor Reajustado

Numérico

0,00

Neste campo deve ser considerado o somatório do valor reajustado do pagamento a beneficiários do evento R\-4040, independente da data do movimento e sim do período de apuração\.

MFS\-79893

Valor do Imposto de Renda Retido na Fonte

Numérico

0,00

Neste campo deve ser considerado o somatório do valor do imposto de renda retido na fonte de pagamento a beneficiários do evento R\-4040, independente da data do movimento e sim do período de apuração\.

MFS\-79893

## <a id="_Toc427766288"></a><a id="_Toc67385625"></a>Layout do Relatório

__A partir da Versão 2\.1\.2 do REINF__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-4040 – Sintético__

__                                                                                      		Período: 99/9999  __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

__Informação de Identificação do Evento __

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	   		Status: X\-XXXXX   			              N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           

__Tipo Amb\.__ : XXXXXXXXX__        __				__Processo de Emissão: __X\-XXXXXX                      __Versão do Processo de Emissão: __XXXXXXXX              __               __

__Tipo Inscrição Estabelecimento__: X\-XXXXXXXXXXXX       __Número Inscrição Estabelecimento__: XXXXX	  __Identificador Evento Adicional: __XXXXX

__Natureza do Rendimento__

XXXXX: XXXXXXXXX

__Totais de Pagamentos a Beneficiários não Indentificados__

__Valor Líquido__

__Valor Reajustado__

__Valor do Imposto de Renda Retido na Fonte__

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

