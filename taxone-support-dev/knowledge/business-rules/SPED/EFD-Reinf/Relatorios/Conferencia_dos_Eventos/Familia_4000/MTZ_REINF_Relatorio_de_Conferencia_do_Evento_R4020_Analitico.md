# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4020_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4020_Analitico.docx
- **Modificado:** 2025-10-13
- **Tamanho:** 102 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento – Família 4000 \- \(R\-4020 – Analítico\)__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios à Conferência dos Eventos à  Família 4000

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS\-79888

Alessandra Cristina Navatta

Criação de um relatório de conferência do evento R\-4020 \(analítico\)\. Relatórios à “Conferência dos Eventos àR\-4020”\.

06/10/2022

MFS\- 511669

Alessandra Cristina Navatta

Inclusão de formato para a exibição dos beneficiários do exterior\.

09/02/2023

MFS\-537195

Alessandra Cristina Navatta

Inclusão dos campos \(a partir da  versão 2\.1\.2\): 

- Identificador do evento Adicional, no agrupamento Identificação do Beneficiário
- Data Escr\. Cont\. e Observ, no agrupamento – Informações Relativas ao Pagamento Efetuado

31/05/2023

MFS\-543004

Alessandra Cristina Navatta

Alteração na regra de exibição dos estabelecimentos

15/06/2023

MFS\-594002

Alessandra Cristina Navatta

Criada tela única, para a geração dos relatórios de conferência da família 4000\.

Excluído o layout da versão 2\.1\.1 da documentação

12/12/2023

MFS\-613110

Rogério Ohashi

Alteração da regra de recuperação dos registros para desconsiderar os eventos com Status de Exclusão e para considerar o envio do novo evento após o evento de Exclusão \(Evento Excluído na Mensageria\)\. 

20/03/2024

MFS\-623425

Alessandra Cristina Navatta

Inclusão da coluna de status no relatório\. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados \(formato Excel\)\. 

Exclusão do agrupamento ‘Informação de Identificação do Evento / Contribuinte’ e as informações existentes anteriormente neste agrupamento foram transferidas para o agrupamento ‘Identificação do Evento/ Beneficiário’, que anteriormente chama\-se ‘Identificação do Beneficiário’\. Este ponto foi ajustado, pois a tabela de ocorrência possui as informações por beneficiário, tipo Arquivo, Nº Recibo, Tipo do Amb\., Versão do Processo de Emissão, etc\.\.\.

28/03/2024

MFS626907

Andréa Rocha

Retirada a opção de salvar como da geração do relatório\.

20/05/2024

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc101182970)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc101182971)

[2\.1\.	Layout do Relatório	11](#_Toc101182972)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc101182970"></a>REGRAS DOS CAMPOS 

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

MFS\-79888

Versão

Texto

S

S

Default: Versão atual

Este campo exibe as versões de layout do Reinf\. A partir da versão 2\.1\.1

MFS\-79888

Tipo do Relatório

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS\-79888

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS\-79888

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento\. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados\.

MFS\-79888

Estabelecimentos

CheckBox

S

S

XXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento centralizador\) ou

XXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento descentralizado\) 

Default: não selecionado

\- Caso o parâmetro “Geração Multiempresa” estiver desmarcado:

Na lista será demonstrado os estabelecimentos que fizeram a geração do evento apenas da empresa que acessou o módulo\.

    

\- Caso o parâmetro “Geração Multiempresa” estiver marcado:

Na lista será demonstrado o estabelecimento de todas as empresas que geraram o evento e que o usuário tem acesso:

       

O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório\.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”

Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”\.

MFS\-79888

MF\-543004

# <a id="_Toc427766287"></a><a id="_Toc101182971"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

__\[MFS626907\] __Retirar a opção de “salvar como”\.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-4020 \(Cadastro do Estabelecimento, SAFX04, SAFX53, SAFX531, SAFX532\)\.

__Regra de seleção: __

A geração do relatório será de acordo com os critérios de filtro informados na tela de geração\.

      \-Empresa = empresa do login      

      \-Período = período informado em tela

      \- Versão = versão informada em tela

      \-Tipo = tipo de relatório informado em tela

      \-Estabelecimento = estabelecimento informado em tela

    

Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a mensagem “NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS” no relatório\. 

__Regra de processamento: __

__\[MFS\-613110\] __Tratamento p/ desconsiderar os eventos com status de exclusão e para considerar o envio do novo evento R\-4020, após evento de exclusão\.

__ __

Para cada estabelecimento selecionado em tela será gerado um relatório\. 

Serão recuperadas as informações do evento R\-4020 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Estabelecimento, Evento, Contribuinte, Informações Complementares do Contribuinte, Beneficiário, Identificação do Rendimento, Informações Relativas ao Pagamento, Informações Relativas a Retenções na Fonte, Processos Relacionados a não Retenção de Tributos, Informações Complementares Decorrentes de Decisão Judicial, Despesas com Processo Judicial, Identificação do Advogado, Informações Complementares Relativas a Pagamentos no Exterior e Endereço do Beneficiário Residente ou Domiciliado no Exterior\.

Será recuperado sempre a última ocorrência do evento R\-4020, exceto para os eventos com status de exclusão \(Evento Excluído na Mensageria\), pois não devem ser considerados no Relatório, para o evento que teve exclusão e está com status de exclusão \(Evento Excluído na Mensageria\), 

Se o evento tiver uma nova geração, o mesmo deverá ser demonstrado no relatório, por Estabelecimento, Evento, Contribuinte, Informações Complementares do Contribuinte, Beneficiário, Identificação do Rendimento, Informações Relativas ao Pagamento, Informações Relativas a Retenções na Fonte, Processos Relacionados a não Retenção de Tributos, Informações Complementares Decorrentes de Decisão Judicial, Despesas com Processo Judicial, Identificação do Advogado, Informações Complementares Relativas a Pagamentos no Exterior e Endereço do Beneficiário Residente ou Domiciliado no Exterior\. Será recuperado sempre a última ocorrência do evento, \(exceto se último status for de exclusão\)\.

__Ordenação: __

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa
- Estabelecimento
- Evento
- Contribuinte
- Informações Complementares do Contribuinte 
- Beneficiário
- Identificação do Rendimento
- Informações Relativas ao Pagamento
- Informações Relativas a Retenções na Fonte
- Processos Relacionados a não Retenção de Tributos
- Informações Complementares Decorrentes de Decisão Judicial
- Despesas com Processo Judicial
- Identificação do Advogado
- Informações Complementares Relativas a Pagamentos no Exterior
- Endereço do Beneficiário Residente ou Domiciliado no Exterior

__Agrupamento:__

- Empresa
- Estabelecimento
- Evento
- Contribuinte
- Informações Complementares do Contribuinte 
- Beneficiário
- Identificação do Rendimento
- Informações Relativas ao Pagamento

  


Segue regras do preenchimento dos dados no relatório:

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Empresa

Texto

Código \- Descrição

Razão social da empresa\.

MFS\-79888

Página

Numérico

Número da página sequencial do relatório

MFS\-79888

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS\-79888

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-4020 \- Analítico”

MFS\-79888

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS\-79888

__Corpo do Relatório__

Estabelecimento

Texto 

Código \- Descrição

Estabelecimento informado em tela

MFS\-79888

__\[EXCLUSÃO MFS\-__ MFS\-622783__\] Informação de Identificação do Evento / Contribuinte__

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4020\_OC

MFS\-79888

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4020\_OC

MFS\-79888

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4020\.

MFS\-79888

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4020\.

MFS\-79888

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4020\.

MFS\-79888

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4020\.

MFS\-79888

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4020\.

MFS\-79888

__Corpo do Relatório – Informações Complementares do Contribuinte__

Natureza Jurídica

Texto

Natureza Jurídica

MFS\-79888

__Corpo do Relatório – Identificação do Evento / Beneficiário__

Esta parte do relatório demonstra os dados do beneficiário

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4020\_OC

MFS\-79888

Status

Texto

Código\-Descrição

Campo IND\_STATUS gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-623425

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4020\_OC

MFS\-79888

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4020\.

MFS\-79888

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4020\.

MFS\-79888

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4020\.

MFS\-79888

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4020\.

MFS\-79888

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4020\.

MFS\-79888

CNPJ/Ident\. Benef\. Exterior

Texto

XXX\.XXX\.XX/XXXX\-XX ou 

Grp/Ind/Cod do Benef\.

CNPJ do Beneficiário\. 

__\[ALTERAÇÃO MFS\-511669\] __

Caso beneficiário seja do exterior, apresentar o código do beneficiário, no formato: Grp/Ind/Cod do Benef\.

MFS\-79888

MFS\- 511669

Nome

Texto

Nome do Beneficiário\. 

 

MFS\-79888

IsenImun

Texto

Código \- Descrição

Informações sobre isenção e imunidade

MFS\-79888

Identificador Evento Adicional

Texto

Identificador de evento adicional por beneficiário, a critério do declarante\.

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-537195

__Corpo do Relatório – Identificação do Rendimento__

Natureza do Rendimento

Texto

Natureza de Rendimento

MFS\-79888

Observação

Texto

Descrição

Observação

MFS\-79888

__Corpo do Relatório – Informações Relativas ao Pagamento Efetuado __

Fato Gerador

Texto

DD/MM/AAAA

Data do Fato Gerador

MFS\-79888

Valor Bruto

Texto

0,00

Valor bruto do rendimento 

MFS\-79888

FCI\_SPC

Texto

Código \- Descrição

 

Indicativo de Fundo/Clube de Investimento ou Sociedade em Conta de Participação

Lista de Valores Válidos:

1 \- FCI \- Fundo ou clube de investimento; 

2 \- SCP \- Sociedade em conta de participação

MFS\-79888

Núm\. Insc\. FCI\_SCP

Texto

XX\.XXX\.XXX/XXXX\-XX

Número de inscrição no CNPJ, de acordo com o conteúdo do campo indFciScp:

MFS\-79888

% SCP

Texto

999

Percentual de SCP

MFS\-79888

IndJud

Texto

Código \- Descrição

Indicativo de Rendimento oriundo de decisão judicial

Lista de Valores Válidos:

S\-Sim;

N\-Não

MFS\-79888

País Resid\. Exterior

Texto

999

Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior\.

MFS\-79888

Data Escr\. Cont\.

Texto

DD/MM/AAAA

Informar a data da escrituração contábil\.

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-537195

Observ\.

Texto

Observações

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-537195

__Corpo do Relatório – Informações Relativas a Retenções na Fonte e Respectivas Bases de Cálculo__

Valor Base IR

Texto

0,00

Valor da base de retenção do IR, efetivamente realizada\.

MFS\-79888

Valor IR

Texto

0,00

Valor do imposto de renda retido na fonte\.

MFS\-79888

Valor Base Agregada

Texto

0,00

Valor da base de retenção de tributos de forma agregada, efetivamente realizada

MFS\-79888

Valor Agregado

Texto

0,00

Valor da retenção em valor agregado de tributos \(IR, CSLL, Cofins e PIS/Pasep\)\.

MFS\-79888

Valor Base CSLL

Texto

0,00

Valor da base de cálculo da Contribuição Social sobre Lucro Líquido \- CSLL, relativa à retenção efetivamente realizada\.

MFS\-79888

Valor CSLL

Texto

0,00

Valor da retenção da Contribuição Social sobre Lucro Líquido \- CSLL

MFS\-79888

Valor Base COFINS

Texto

0,00

Valor da base de cálculo da Cofins, relativa à retenção efetivamente realizada\.

MFS\-79888

Valor COFINS

Texto

0,00

Valor da retenção relativa a COFINS

MFS\-79888

Valor Base PIS/PASEP

Texto

0,00

Valor da base do PIS/PASEP, relativa à retenção efetivamente realizada\.

MFS\-79888

Valor PIS/PASEP

Texto

0,00

Valor da retenção do PIS/PASEP\.

MFS\-79888

__Corpo do Relatório – Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais__

Tipo Processo

Texto

Código \- Descrição

Preencher com o código correspondente ao tipo de processo

Lista de Valores Válidos:

1 \- Administrativo; 

2 \- Judicial\.

MFS\-79888

Núm\. Processo

Texto

Informar o número do processo administrativo/judicial\.

MFS\-79888

Cód\. Susp\.

Texto

Informar o código indicativo da suspensão

MFS\-79888

Valor Base Susp IR

Texto

0,00

Valor da base de cálculo do IR com exibilidade suspensa\.

MFS\-79888

Valor N IR

Texto

0,00

Valor da retenção de IR que deixou de ser efetuada em função de processo\.

MFS\-79888

Valor Dep\. IR

Texto

0,00

Valor do depósito judicial relativo ao IR\.

MFS\-79888

Valor Base Susp CSLL

Texto

0,00

Valor da base de cálculo da CSLL com exibilidade suspensa\.

MFS\-79888

Valor N CSLL

Texto

0,00

Valor da retenção de CSLL que deixou de ser efetuada em função de processo\.

MFS\-79888

Valor Dep\. CSLL

Texto

0,00

Valor do depósito judicial da CSLL em função de processo administrativo ou judicial\.

MFS\-79888

Valor Base Susp Cofins

Texto

0,00

Valor da base de cálculo da Cofins com exibilidade suspensa\.

MFS\-79888

Valor N Cofins

Texto

0,00

Valor da retenção de COFINS que deixou de ser efetuada em função de processo\.

MFS\-79888

Valor Dep Cofins

Texto

0,00

Valor do depósito judicial da Cofins em função de processo administrativo ou judicial\.

MFS\-79888

Valor Base Susp PIS/PASEP

Texto

0,00

Valor da base de cálculo do PIS/PASEP com exibilidade suspensa\.

MFS\-79888

Valor N PIS/PASEP

Texto

0,00

Valor da retenção de PIS/PASEP que deixou de ser efetuada em função de processo\.

MFS\-79888

Valor Dep PIS/PASEP

Texto

0,00

Valor do depósito judicial do PIS/PASEP em função de processo administrativo ou judicial\.

MFS\-79888

__Corpo do Relatório – Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial__

Núm\. Processo

Texto

Informar o número do processo judicial\.

MFS\-79888

Origem dos Recursos

Código \- Descrição

Informar o indicativo da origem dos recursos\.

Lista de Valores Válidos: 

1\-Recursos do próprio declarante; 

2\-Recursos de terceiros \- Declarante é a instituição financeira responsável pelo repasse dos valores

MFS\-79888

CNPJ Origem Recursos

Texto

XX\.XXX\.XXX/XXXX\-XX

CNPJ da empresa que repassou os recursos\.

MFS\-79888

Descrição

Texto

Descrição 

MFS\-79888

__Corpo do Relatório – Despesas com Processo Judicial__

Valor Despesas Custas Judiciais

Texto

0,00

Informar o valor da despesa com custas judiciais

MFS\-79888

Valor Despesa Advogados

Texto

0,00

Informar o valor da despesa com advogado\(s\)\.

MFS\-79888

__Corpo do Relatório – Identificação do advogado__

Tipo Inscrição

Texto

Código \- Descrição

Tipo de inscrição do advogado\.

Lista de Valores Válidos:

1\-CNPJ; 

2\-CPF

MFS\-79888

Núm\. Inscrição

Texto

Informar o número de inscrição do advogado\.

MFS\-79888

Valor Advogado

Texto

0,00

Valor da despesa com o advogado\.

MFS\-79888

__Corpo do Relatório – Informações Complementares Relativas a Pagamentos a Residente Fiscal no Exterior__

Ind\. Núm\. Identificação Fiscal

Texto

Código \- Descrição

Informar o indicativo do Número de Identificação Fiscal \- NIF: 

Lista de Valores Válidos:

1\-Beneficiário com NIF;

2\-Beneficiário dispensado do NIF; 

3\-País não exige NIF\.

MFS\-79888

Núm\. Identificação Fiscal

Texto

Informar o número de Identificação Fiscal \- NIF\.

MFS\-79888

Rel\. Fonte Pagadora

Texto

Código \- Descrição

Relação da fonte pagadora com o beneficiário\.

MFS\-79888

Forma de Tributação

Texto

Informar a forma de tributação\.

MFS\-79888

__Corpo do Relatório – Endereço do Bbeneficiário Residente ou Domiciliado no Exterior__

Logradouro

Texto

Informar o logradouro

MFS\-79888

Núm\.

Texto

Informar o número do logradouro\.

MFS\-79888

Complemento

Texto

Informar o complemento do logradouro\.

MFS\-79888

Bairro

Texto

Informar o bairro

MFS\-79888

Cidade

Texto

Informar a cidade

MFS\-79888

Estado

Texto

Informar o estado

MFS\-79888

Cód\. Postal

Texto

Informar o código postal \(CEP\)

MFS\-79888

Telefone

Texto

Informar o telefone\.

MFS\-79888

  


## <a id="_Toc427766288"></a><a id="_Toc101182972"></a>Layout do Relatório

__A partir da Versão 2\.1\.2 do REINF__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ===============================

__XXX\-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-4020 – Analítico__

__                                                                                      		Período: MM/AAAA__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ================================

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

__Informações Complementares do Contribuinte__

__Natureza Jurídica:__ XXXX

__	Identificação do Evento / Beneficiário__

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	__

__    Status: __X\-XXXXXXXXXXXX

__N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           

__Tipo do Amb\.__ : XXXXXXXXX__        __

__Processo de Emissão: __X\-XXXXXX   

  __Versão do Processo de Emissão: __XXXXXXXX              __               __

__Tipo de Inscrição Estabelecimento__: X\-XXXXXXXXXXXX           

__Número Inscrição Estabelecimento__: XXXXX

__CNPJ__/Ident\. Benef\. Exterior__:__ XXX\.XXX\.XX/XXXX\-XX ou Grp/Ind/Cod do Benef\.

	__Nome:__ XXXXXXXXX

__IsenImun:__ Codigo \- Descrição

Identificador Evento Adicional: XXXXXXXX

__Identificação do Rendimento__

__Natureza do Rendimento: __XXXXXXX

__Observação:__ Descrição

__Informações Relativas ao Pagamento Efetuado__

__Fato Gerador__

__Valor Bruto__

__FCI\_SPC__

__Núm\. Insc\. FCI\_SCP__

__% SCP__

__IndJud__

__País Resid\. Exterior__

__Data Escr\. Cont__

__Observ__

DD/MM/AAAA

0,00

Cód\.  – Descrição

XX\.XXX\.XXX/XXXX\-XX

999

Cód\.

999

DD/MM/AAAA

XXXXXX

__Informações Relativas a Retenções na Fonte e Respectivas Bases de Cálculo__

__IR__

__Agregado__

__CSLL__

__COFINS__

__PIS/PASEP__

__Valor Base __

__Valor __

__Valor Base __

__Valor __

__Valor Base __

__Valor __

__Valor Base __

__Valor __

__Valor Base __

__Valor __

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

__Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais__

__Processo__

__IR__

__CSLL__

__COFINS__

__PIS/PASEP__

Tipo 

Núm\.

Cód\. Suspensão

Valor Base Susp 

Valor N 

Valor Dep

Valor Base Susp 

Valor N 

Valor Dep\. 

Valor Base Susp 

Valor N 

Valor Dep 

Valor Base Susp 

Valor N 

Valor Dep 

Código \- Descrição

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

0,00

__Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial__

__Núm\. Processo__

__Origem dos Recursos__

__CNPJ Origem Recursos__

__	Descrição__

Código \- Descrição

XX\.XXX\.XXX/XXXX\-XX

__Despesas com Processo Judicial__

__Valor Despesas Custas Judiciais:__ 0,00

__Valor Despesa Advogados: __0,00

__Identificação do Advogado__

__Tipo Inscrição: __

__Núm\. Inscrição__

__Valor Advogado__

Código \- Descrição

0,00

__Informações Complementares Relativas a Pagamentos a Residente Fiscal no Exterior__

__Ind\. Núm\. Identificação Fiscal__

__Núm\. Identificação Fiscal__

__Rel\. Fonte Pagadora__

__Forma de Tributação__

Código \- Descrição

Código \- Descrição

__Endereço do Beneficiário Residente ou Domiciliado no Exterior__

__Logradouro: __Descrição

__Número: __XXX

__Complemento: __XXXX

__Bairro:__ Descrição

__Cidade: __Descrição

__Estado: __XX

__Cód\. Postal:__ XXXXX

__Telefone: __XXXXXXXXXX

