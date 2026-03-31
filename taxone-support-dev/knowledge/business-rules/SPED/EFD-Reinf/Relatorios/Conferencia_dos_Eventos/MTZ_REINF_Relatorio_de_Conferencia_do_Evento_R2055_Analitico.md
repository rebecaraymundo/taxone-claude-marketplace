# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2055_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2055_Analitico.docx
- **Modificado:** 2022-09-06
- **Tamanho:** 95 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento R\-2055 \- Analítico__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios 🡪 Conferência dos Eventos 🡪 R\-2055

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS58386

Alessandra Cristina Navatta

Criação de um relatório de conferência do evento R\-2055 \(analítico\)\. Relatórios 🡪 “Conferência dos Eventos 🡪R\-2055”\.

17/03/2021

MFS\-79878

Alessandra Cristina Navatta

Exclusão do campo Retificação S\-1250, a partir da versão 2\.1\.1 do REINF\.

31/01/2022

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc67385623)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc67385624)

[2\.1\.	Layout do Relatório	14](#_Toc67385625)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc67385623"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios > Conferência dos Eventos > R\-2055

__Título da tela: __Relatório de Conferência do Evento R\-2055

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

MFS58386

Versão

Texto

S

S

Default: Versão atual

Este campo exibe as versões de layout do Reinf\. A partir da versão 1\.5\.1

MFS58386

Tipo do Relatório

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS58386

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS58386

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento\. 

MFS58386

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

MFS58386

# <a id="_Toc427766287"></a><a id="_Toc67385624"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-2055 \(SAFX07, SAFX63, Cadastro do Estabelecimento e tela “Devoluções de Aquisição de Produtor Rural”\)\.
- Tabela compõem os valores das aquisições \(por produtor rural\) R\-2055 \(REINF\_PGER\_R2055\_DETAQUIS\); 

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

Serão recuperadas as informações do evento R\-2055 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento, Produtor Rural, Tipo de Aquisição e Processos\. Será recuperado sempre a última ocorrência do evento R\-2055 por tipo de número de inscrição do contribuinte\.

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

          \- Empresa 

          \- Estabelecimento

          \- Produtor Rural

			\- Tipo de Aquisição 

  


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

MFS58386

Página

Numérico

Número da página sequencial do relatório

MFS58386

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS58386

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-2055 \- Analítico”

MFS58386

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS58386

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS58386

__Informação de Identificação do Evento / Contribuinte__

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R2055\_OC

MFS58386

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R2055\_OC

MFS58386

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-2055\.

MFS58386

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-2055\.

MFS58386

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-2055\.

MFS58386

Indicativo de Retificação do Evento S\-1250

Texto

Indicativo de Retificação, gerado no evento R\-2055\.

__\[ALTERAÇÃO MFS\-79878\]__ Este campo não deve ser gerado a partir da versão 2\.1\.1 do REINF

MFS58386

__ MFS\-79878__

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-2055\.

MFS58386

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-2055\.

MFS58386

<a id="_Hlk10727609"></a>

__Corpo do Relatório – __Identificação do Produtor Rural

Esta parte do relatório demonstra o produtor gerado no evento R\-2055\. 

As informações são recuperadas da tabela REINF\_PGER\_R2055\_PRODUTOR, tabela alimentada durante a geração do evento R\-2055\.

__  __

Tipo de Inscrição

Texto

Tipo de Inscrição: 

Opções Válidas:

1 \- CNPJ

2 \- CPF

MFS58386

Número de Inscrição

Texto

Número de Inscrição vinculado ao evento R\-2055\.

MFS58386

Forma de Tributação da Contribuição Previdenciária

Texto

Indicador OpcCP vinculado ao evento R\-2055

MFS58386

__Corpo do Relatório – __Detalhamento da Aquisição de Produção Rural

Esta parte do relatório demonstra o detalhamento das aquisições por produtor rural\. 

As informações são recuperadas da tabela REINF\_PGER\_R2055\_DETAQUIS, tabela alimentada durante a geração do evento R\-2055\.

Indicador de Aquisição

Texto

Indicador da aquisição, vinculado ao evento R\-2055\.

Valores Válidos:

 1 \- Aquisição de produção de produtor rural pessoa física ou segurado especial em geral; 

2 \- Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do Programa de Aquisição de Alimentos \- PAA; 

3 \- Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA; 

4 \- Aquisição de produção de produtor rural pessoa física ou segurado especial em geral \- Produção isenta \(Lei 13\.606/2018\); 

5 \- Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do PAA \- Produção isenta \(Lei 13\.606/2018\); 

6 \- Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA \- Produção isenta \(Lei 13\.606/2018\); 7 \- Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação 

MFS58386

Valor da Receita Bruta Total

Numérico

0,00

Valor vinculado ao evento R\-2055\.

\(campo vlrBruto do evento R\-2055\)\.

MFS58386

Valor da Contribuição Previdenciária 

Numérico

0,00

Valor vinculado ao evento R\-2055\.

\(campo vlrCPDescPR do evento R\-2055\)\.

MFS58386

Valor da Contribuição Previdenciária GILRAT

Numérico

0,00

Valor vinculado ao evento R\-2055\.

\(campo vlrRatDescPR do evento R\-2055\)\.

MFS58386

Valor da Contribuição Previdenciária SENAR

Numérico

0,00

Valor vinculado ao evento R\-2055\.

\(campo vlrSenarDesc do evento R\-2055\)\.

MFS58386

__Corpo do Relatório – Informação do Processo Judicial do Produtor Rural__

Número Processo

Alfanumérico

Número Processo \(NUM\_PROC\) correspondente gerado no campo nrProc do evento R\-2055\.  

MFS58386

Código Suspenção

Alfanumérico

Código Suspenção \(COD\_SUSP\) correspondente gerado no campo codSusp do evento R\-2055\.  

MFS58386

Valor da Contribuição Previdenciária Não Retida

Numérico

0,00

Valor da Contribuição Previdênciária, campo vrCPNRet, gerado do evento R\-2055\.

MFS58386

Valor da Contribuição Previdenciária GILRAT Não Retida

Numérico

0,00

Valor da Contribuição Previdênciária destinada ao GILRAT, gerado no campo vrRatNRet do evento R\-2055\.

MFS58386

Valor da Contribuição Previdenciária SENAR Não Retida

Numérico

0,00

Valor da Contribuição Previdênciária destinada ao SENAR, gerado no campo vrSenarNRet do evento R\-2055\.

MFS58386

Total Geral das Aquisições 

Esta parte do relatório demonstra o total das das aquisições por produtor rural \(independente do indicador de aquisição\)\. 

As informações são recuperadas da tabela REINF\_PGER\_R2055\_DETAQUIS, tabela alimentada durante a geração do evento R\-2055\.

MFS58386

Valor da Receita Bruta Total

Numérico

0,00

Valor Bruto \(sumarizado por produtor rural\) vinculado ao evento R\-2055\.

\(campo vlrBruto do evento R\-2055\)\.

Obs\. Não exibir o label\.

MFS58386

Valor da Contribuição Previdenciária 

Numérico

0,00

Valor \(sumarizado por produtor rural\) vinculado ao evento R\-2055\.

\(campo vlrCPDescPR do evento R\-2055\)\.

Obs\. Não exibir o label\.

MFS58386

Valor da Contribuição Previdenciária GILRAT

Numérico

0,00

Valor \(sumarizado por produtor rural\) vinculado ao evento R\-2055\.

\(campo vlrRatDescPR do evento R\-2055\)\.

Obs\. Não exibir o label\.

MFS58386

Valor da Contribuição Previdenciária SENAR

Numérico

0,00

Valor \(sumarizado por produtor rural\) vinculado ao evento R\-2055\.

\(campo vlrSenarDesc do evento R\-2055\)\.

Obs\. Não exibir o label\.

MFS58386

## <a id="_Toc427766288"></a><a id="_Toc67385625"></a>Layout do Relatório

<a id="_Hlk66960364"></a>= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-2055 – Analítico__

__                                                                                      		Período: 99/9999  __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

<a id="_Hlk66960595"></a>__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

__Informação de Identificação do Evento / Contribuinte__

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	    N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           __Tipo Amb\.__ : XXXXXXXXX__        __

__Processo de Emissão: __X\-XXXXXX                 __Versão do Processo de Emissão: __XXXXXXXX              __Indicativo de Retificação do Evento S\-1250: Não               __

__Tipo Inscrição Estabelecimento__: X\-XXXXXXXXXXXX                  	__Número Inscrição Estabelecimento__: XXXXX

__Identificação do Produtor Rural__

__Tipo de Inscrição__

__Número de Inscrição__

Forma de Tributação da Contribuição Previdenciária

X\-XXXX

xxxxxxxxxxxx

xxx

__Detalhamento da Aquisição de Produção Rural__

__Indicador de Aquisição: X\-XXXXXXXX__

__Valor da Receita  Bruta Total__

__Valor da Contribuição Previdenciária__

__Valor da Contribuição Previdenciária GILRAT__

__Valor da Contribuição Previdenciária SENAR__

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Informação do Processo Judicial do Produtor Rural__

__Número Processo__

__Código Suspensão__

__Valor da Contribuição Previdenciária Nâo Retida__

__Valor da Contribuição Previdenciária GILRAT Nâo Retida__

__Valor da Contribuição Previdenciária SENAR Nâo Retida__

xxxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Total Geral  das Aquisições __

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__A partir da Versão 2\.1\.1 do REINF__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-2055 – Analítico__

__                                                                                      		Período: 99/9999  __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

__Informação de Identificação do Evento / Contribuinte__

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	    N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           __Tipo Amb\.__ : XXXXXXXXX__        __

__Processo de Emissão: __X\-XXXXXX                 __Versão do Processo de Emissão: __XXXXXXXX              __               __

__Tipo Inscrição Estabelecimento__: X\-XXXXXXXXXXXX                  	__Número Inscrição Estabelecimento__: XXXXX

__Identificação do Produtor Rural__

__Tipo de Inscrição__

__Número de Inscrição__

Forma de Tributação da Contribuição Previdenciária

X\-XXXX

xxxxxxxxxxxx

xxx

__Detalhamento da Aquisição de Produção Rural__

__Indicador de Aquisição: X\-XXXXXXXX__

__Valor da Receita  Bruta Total__

__Valor da Contribuição Previdenciária__

__Valor da Contribuição Previdenciária GILRAT__

__Valor da Contribuição Previdenciária SENAR__

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Informação do Processo Judicial do Produtor Rural__

__Número Processo__

__Código Suspensão__

__Valor da Contribuição Previdenciária Nâo Retida__

__Valor da Contribuição Previdenciária GILRAT Nâo Retida__

__Valor da Contribuição Previdenciária SENAR Nâo Retida__

xxxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Total Geral  das Aquisições __

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

