# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R2050_Analitico.docx
- **Modificado:** 2021-03-17
- **Tamanho:** 90 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento R\-2050 \- Analítico__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios 🡪 Conferência dos Eventos 🡪 R\-2050

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS17631

Lara Aline

Alteração do Modulo REINF para criação de um relatório de conferência do evento R\-2050\. Novo relatório 🡪 “Relatório de Conferência do Evento R\-2050”\. 

21/05/2018

\(criação do documento\)

MFS18226

Lara Aline

Inclusão do campo Tipo de Ambiente

04/06/2018

MFS21968

Eduardo Cruz

Inclusão dos campos: ID Evento, Data Evento, Nº Recibo, Tipo Arquivo

20/02/2019

MFS20474

Vânia Mattos

Inclusão de colunas no relatório, e linha de totalização dos valores por indicativo de comercialização

06/06/2019

MFS30234

Alessandra Cristina Navatta

Considerar as informações dos ajustes de adição na tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria” que não possuem notas fiscais relacionadas\.

12/09/2019

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc19180470)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc19180471)

[2\.1\.	Layout do Relatório	14](#_Toc19180472)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc19180470"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios > Conferência dos Eventos > R\-2050 

__Título da tela: __Relatório de Conferência do Evento R\-2050

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

MFS17631

Período

Data 

S

S

Formato: MM/AAAA 

Default: Habilitado

Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA\. 

Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório\.

MFS17631

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS18226

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, todas as empresas, contendo o código da empresa, código e a razão social de cada estabelecimento\. 

MFS17631

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

MFS17631

# <a id="_Toc427766287"></a><a id="_Toc19180471"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-2050 \(SAFX07, SAFX263, Cadastro do Estabelecimento e tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\)\.
- Tabela das Notas Fiscais que compõem os valores do R\-2050 \(REINF\_PGER\_R2050\_NF\); 

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

Serão recuperadas as informações do evento R\-2050 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento, Tipo de Comercialização, NFs e Processos\. Será recuperado sempre a última ocorrência do evento R\-2050 por tipo de número de inscrição do contribuinte\.

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

MFS17631

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS17631

Página

Numérico

Número da página sequencial do relatório

MFS17631

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-2050 \- Analítico”

MFS17631

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS17631

__Corpo do Relatório__

Estabelecimento

Texto 

Estabelecimento informado em tela

MFS17631

ID Evento

Texto

Campo ID\_EVENTO gravado na tabela REINF\_PGER\_R2050\_OC 

MFS21968

Data Evento

Data

Formato: DD/MM/YYYY HH:MM:SS

Campo DAT\_OCORRENCIA gravado na tabela REINF\_PGER\_R2050\_OC

MFS21968

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R2050\_OC

MFS21968

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R2050\_OC

MFS21968

Tipo Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-2050\.

MFS17631

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-2050\.

MFS17631

<a id="_Hlk10727609"></a>

__Corpo do Relatório – Detalhamento de Nota Fiscal por Tipo de Comercialização__

Esta parte do relatório demonstra as notas fiscais utilizadas na geração do evento R\-2050, agrupadas por Indicativo de Comercialização\. 

As informações são recuperadas da tabela __REINF\_PGER\_R2050\_NF__, tabela alimentada durante a geração do evento R\-2050\.

__  __

Indicativo de Comercialização

Alfanumérico

Indicativo de Comercialização \(IND\_TIPO\_AQUIS da SAFX07 \+  Descrição correspondendo conforme abaixo\), gerado no campo indCom do evento R\-2050\.

Descrição correspondente a cada código:

1 \- Aquisição da Produção de Prod\. Rural PF ou segurado especial/Comercialização da Produção por Prod\. Rural PJ/Agroindústria;

8 \- Comercialização da Produção para Entidade inscrita no PAA;

9 \- Comercialização da Produção no Mercado Externo\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do campo “Indicativo de Comercialização\.

MFS17631

MFS30234

N° Nota Fiscal

Alfanumérico

N° Nota Fiscal \(NUM\_DOCFIS\) SAFX07 gerado no campo numDocto vinculado ao evento R\-2050\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o texto “AJUSTE\.

MFS17631

MFS30234

Série

Alfanumérico

Série da Nota Fiscal \(SERIE\_DOCFIS\) SAFX07, gerado no campo serie vinculado ao evento R\-2050\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, não exibir nenhuma informação no campo relativo a série do documento\.

MFS17631

MFS30234

Data de Emissão

Data

DD/MM/AAAA

Data de Emissão da Nota Fiscal \(DATA\_EMISSAO\) SAFX07 vinculado ao evento R\-2050\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar a data do último dia do mês do ajuste\.

MFS17631

MFS30234

Valor Bruto

Numérico

Default: 0,000

Valor Bruto \(VLR\_BRUTO da SAFX07\), gerado no campo vlrBruto vinculado ao evento R\-2050\.

Obs: Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais\. Será considerado o valor bruto de todos os itens da nota, mesmo os itens que foram desconsiderados na geração com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado”\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor da Receita Bruta” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\. 

MFS17631

MFS30234

Contrib\. Previdenciária

*\(Coluna incluída na MFS20474\)*

Numérico

Campo “Valor da Contribuição Previdenciária” da nota fiscal \(VLR\_CONTRIB\_PREV da SAFX07\)\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor da Contribuição Previdenciária” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\. 

MFS20474

MFS30234

GILRAT

*\(Coluna incluída na MFS20474\)*

Numérico

Campo “Valor da GILRAT” da nota fiscal \(VLR\_GILRAT da SAFX07\)\.

\[MFS30234\] Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor do GILRAT” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\. 

MFS20474

MFS30234

SENAR

*\(Coluna incluída na MFS20474\)*

Numérico

Campo “Valor da Contribuição destinada ao SENAR” da nota fiscal \(VLR\_CONTRIB\_SENAR da SAFX07\)\.

\[MFS30234\] Se houver ajuste de adição nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor do SENAR” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\. 

MFS20474

MFS30234

__Corpo do Relatório – Linha de total das notas fiscais por Indicativo de Comercialização__

Totais Comercialização

*\(Linha incluída na MFS20474\)*

Numérico

Totalização das colunas de valor para cada indicativo de comercialização:

\- Valor Bruto

\- Contrib\. Previdenciária

\- GILRAT

\- SENAR

 

__MFS20474__

__Corpo do Relatório – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte__

Tipo de Processo

Alfanumérico

Tipo de Processo \(IND\_TIP\_PROC\) SAFX263 correspondente gerado no campo tpProc do evento R\-2050\.  

MFS17631

Número Processo

Alfanumérico

Número Processo \(NUM\_PROC\) SAFX263 correspondente gerado no campo nrProc do evento R\-2050\.  

MFS17631

Código Suspenção

Alfanumérico

Código Suspenção \(COD\_SUSP\) SAFX263 correspondente gerado no campo codSusp do evento R\-2050\.  

MFS17631

Valor CPRB Exigibilidade Suspensa

Numérico

Default: 0,000

Valor CPRB Exigibilidade Suspensa \(VLR\_PREV\_EXIG\_SUSP\) SAFX263, gerado no campo vlrCPSusp do  evento R\-2050\.

MFS17631

Valor Contribuição Gilrat Exigibilidade Suspensa

Numérico

Default: 0,000

Valor CPRB Exigibilidade Suspensa \(VLR\_GILRAT\_EXIG\_SUSP\) SAFX263, gerado no campo vlrRatSusp do  evento R\-2050\.

MFS17631

Valor Contribuição Senar Exigibilidade Suspensa

Numérico

Default: 0,000

Valor CPRB Exigibilidade Suspensa \(VLR\_SENAR\_EXIG\_SUSP\) SAFX263, gerado no campo vlrSenarSusp do  evento R\-2050\.

MFS17631

## <a id="_Toc427766288"></a><a id="_Toc19180472"></a>Layout do Relatório

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

__XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                    Data: 99/99/9999   Pág\.: 999999__

__                                                               Relatório de Pagamento do Evento R\-2050 – Analítico__

__                                                                                            Período: 99/9999  __

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__ID Evento: __XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                    __Data Evento: __99/99/9999 99:99:99

__N\. Recibo: __XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX__                                          Tipo Arquivo: __XXXXXXXXXXXXXXXXXX

__Tipo Inscrição Estabelecimento__: X\-XXXXXXXXXXXXXXXXXXX                                            __Número Inscrição Estabelecimento__: XXXXX

__Detalhamento de Nota Fiscal por Tipo de Comercialização__

__Indicativo Comercialização__: X \- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__N\. Nota Fiscal__

__Série__

__Data de Emissão__

__Valor Bruto__

__Contrib\. Previdenciária__

__GILRAT__

__SENAR__

xxxxxxxxxxxx

xxx

99/99/9999

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxx

xxx

99/99/9999

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

xxxxxxxxxxxx

xxx

99/99/9999

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

                                      Totais Comercialização:

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

__Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao usuário__

__Tipo de Processo__

__Número Processo__

__Código Suspensão__

__Valor CPRB__

__Exigibilidade Suspensa__

__Valor Contribuição Gilrat__

__Exigibilidade Suspensa__

__Valor Contribuição Senar__

__Exigibilidade Suspensa__

x\-xxxxxxxxx

xxxxxxxxxxxxx

xxxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

x\-xxxxxxxxx

xxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

x\-xxxxxxxxx

xxxxxxxxxxxxx

xxxxxxxxxxxxx

999\.999\.999\.999,99

999\.999\.999\.999,99

999\.999\.999\.999,99

