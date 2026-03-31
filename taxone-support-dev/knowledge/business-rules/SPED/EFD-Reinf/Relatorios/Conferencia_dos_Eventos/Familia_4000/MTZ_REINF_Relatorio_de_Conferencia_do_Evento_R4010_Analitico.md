# MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4010_Analitico

- **Fonte:** MTZ_REINF_Relatorio_de_Conferencia_do_Evento_R4010_Analitico.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 116 KB

---

THOMSON REUTERS

Módulo EFD \- REINF

__Relatório de Conferência do Evento – Família 4000 \- \(R\-4010 – Analítico\)__

__Localização__: Menu SPED, Módulo: EFD \- REINF, item de menu Relatórios à Conferência dos Eventos à Família 4000

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data __

MFS\-79885

Alessandra Cristina Navatta

Criação de um relatório de conferência do evento R\-4010 \(analítico\)\. Relatórios à “Conferência dos Eventos àR\-4010”\.

12/09/2022

MFS\-511669

Alessandra Cristina Navatta

Inclusão de formato para a exibição dos beneficiários do exterior\.

09/02/2023

MFS\-535745

Alessandra Cristina Navatta

Inclusão dos campos \(a partir da  versão 2\.1\.2\): 

- Identificador do evento Adicional, no agrupamento Identificação do Beneficiário
- Data Escr\. Cont\. e Observ, no agrupamento – Informações Relativas ao Rendimento

19/05/2023

MFS\-542897

Alessandra Cristina Navatta

Alteração na regra de exibição dos estabelecimentos

15/06/2023

MFS\-549365

Alessandra Cristina Navatta

Mudança de domínio no campo Tipo de Isenção\.  Atendimento ao layout 2\.1\.2 

11/07/2023

__MFS\-566870__

Alessandra Cristina Navatta

Alterações nos campos do evento R\-4010:

Tipo Dedução \- inclusão do tipo de dedução “8 – Desconto simplificado mensal” nos agrupamentos ‘Informações Relativas às Deduções do Rendimento Tributável’ \(tag detDed\) e ’Detalhamento das Deduções Suspensas’ \(tag dedSusp\)\. 

14/09/2023

MFS\-578044

Alessandra Cristina Navatta

Criada tela única, para a geração dos relatórios de conferência da família 4000\.

Excluído o layout da versão 2\.1\.1 da documentação

06/11/2023

MFS\-622783

Alessandra Cristina Navatta

Inclusão da coluna de status no relatório\. Foi necessário incluir essa coluna no relatório, que não está prevista no layout do evento, para evitar duplicidade de dados na conferência dos dados \(formato Excel\)\. Além disso, será sempre demonstrado a última ocorrência do evento\.

Exclusão do agrupamento ‘Informação de Identificação do Evento / Contribuinte’ e as informações existentes anteriormente neste agrupamento foram transferidas para o agrupamento ‘Identificação do Evento/ Beneficiário’, que anteriormente chama\-se ‘Identificação do Beneficiário’\. Este ponto foi ajustado, pois a tabela de ocorrência possui as informações por beneficiário, tipo Arquivo, Nº Recibo, Tipo do Amb\., Versão do Processo de Emissão, etc\.\.\.

21/03/2024

MFS626907

Andréa Rocha

Retirada a opção de “salvar como” da geração do relatório\.

20/05/2024

MFS\-805178

Alessandra Cristina Navatta

Ajustes referente a nota técnica 01/2025, conforme INFOLEGIS 1740/25 \- Z \- 104 \- EFD REINF\_NT 01/2025 \- DW/T1

Inclusão da opção 3 – Sem Processo no campo Tipo de Processo \(tag infoRRA\)

12/05/2025

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc101182970)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	6](#_Toc101182971)

[2\.1\.	Layout do Relatório	11](#_Toc101182972)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc101182970"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD \- REINF, item de menu Relatórios > Conferência dos Eventos > Família 4000 >

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

MFS\-79885

Versão

Texto

S

S

Default: Versão atual

Este campo exibe as versões de layout do Reinf\. A partir da versão 2\.1\.1

MFS\-79885

Tipo do Relatório

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções:

\- Analítico

\- Sintético

MFS\-79885

Tipo de Ambiente

Checkbox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de ambiente entre as opções:

\- Produção Restrita

\- Produção

MFS\-79885

Geração Multiempresa

CheckBox

S

S

Default: não selecionado

Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso e que geraram o evento\. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada que geraram o evento serão demonstrados\.

MFS\-79885

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

MFS\-79885

MFS\-542897

# <a id="_Toc427766287"></a><a id="_Toc101182971"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __

__\[MFS626907\] __Retirar a opção de “salvar como”\.  O relatório passará a ter as opções de salvar em excel ou em PDF

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\.

__Origem das informações para geração:__ 

Para geração deste relatório, serão consideradas as informações da seguinte origem:

- Evento R\-4010 \(Cadastro do Estabelecimento, SAFX04, SAFX53, SAFX536, SAFX531, SAFX532, SAFX534, SAFX535, SAFX275, SAFX276, SAFX277\)\.

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

Serão recuperadas as informações do evento R\-4010 de acordo com a regra de seleção, todas as informações para a Empresa e Estabelecimento de acordo com o período informado\. Relatório demonstrará as informações por Evento, Contribuinte, Informações Complementares do Contribuinte,  Estabelecimento, Beneficiário, Dependentes, Identificação do Rendimento, Rendimento pago/creditado, Deduções do rendimento Tributável, Dependentes e beneficiários da pensão alimentícia, rendimentos isentos ou não tributáveis, processos relacionados a não retenção de tributos , detalhamento das deduções suspensas, deduções suspensas por dependentes e beneficiários da pensão alimentícia, informações complementares RRA, despesas com processo judicial, identificação do advogado, informações de processos judicial, despesas com processo judicial, identificação do advogado, informações complementares relativas a pagamento do exterior, endereço do beneficiário residente ou domiciliado no exterior, identificação da operadora do plano privado coletivo empresarial de assistência à saúde, Reembolso do titular do plano de saúde coletivo, informações de dependente do plano de saúde coletivo empresarial, Reembolso do dependente do plano de saúde coletivo empresarial\.

__Ordenação:__

Para o relatório de cada Estabelecimento selecionado em tela, os dados serão ordenados da seguinte forma:

- Empresa 
- Estabelecimento
- Evento
- Contribuinte
- Informações Complementares do Contribuinte 
- Beneficiário
- Dependente
- Identificação do Rendimento, 
- Rendimento pago/creditado, 
- Deduções do rendimento Tributável, 
- Dependentes e beneficiários da pensão alimentícia, 
- Rendimentos isentos ou não tributáveis, 
- Processos relacionados a não retenção de tributos, 
- Detalhamento das deduções suspensas, 
- Deduções suspensas por dependentes e beneficiários da pensão alimentícia, 
- Informações complementares RRA, 
- Despesas com processo judicial,
- Identificação do advogado, 
- Informações de processos judicial, 
- Despesas com processo judicial,
- Identificação do advogado, 
- Informações complementares relativas a pagamento do exterior,
- Endereço do beneficiário residente ou domiciliado no exterior, 
- Identificação da operadora do plano privado coletivo empresarial de assistência à saúde, 
- Reembolso do titular do plano de saúde coletivo,
- Informações de dependente do plano de saúde coletivo empresarial, 
- Reembolso do dependente do plano de saúde coletivo empresarial\.

__Agrupamento:__

- Empresa 
- Estabelecimento
- Evento
- Contribuinte
- Informações Complementares do Contribuinte 
- Beneficiário
- Identificação do Rendimento
- Informações de Rendimento

__\[ALTERAÇÂO MFS\-622783\]__ Para a exibição das informações no relatório:

- Apresentar sempre a última ocorrência do evento\.

  


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

MFS\-79885

Página

Numérico

Número da página sequencial do relatório

MFS\-79885

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS\-79885

Título

Texto

Título do relatório: “Relatório de Conferência do Evento R\-4010 \- Analítico”

MFS\-79885

Período

Data

Formato: MM/AAAA

Deverá ser exibido o período informado em tela\.

MFS\-79885

__Corpo do Relatório__

Estabelecimento

Texto 

Código \- Descrição

Estabelecimento informado em tela

MFS\-79885

__\[EXCLUSÃO MFS\-__ MFS\-622783__\] Informação de Identificação do Evento / Contribuinte__

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-79885

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-79885

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4010\.

MFS\-79885

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4010\.

MFS\-79885

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4010\.

MFS\-79885

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4010\.

MFS\-79885

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4010\.

MFS\-79885

__Corpo do Relatório – Informações Complementares do Contribuinte__

Natureza Jurídica

Texto

Natureza Jurídica

MFS\-79885

__Corpo do Relatório – Identificação do Evento / Beneficiário__

Esta parte do relatório demonstra os dados do beneficiário

Tipo Arquivo

Texto

Campo IND\_OPER gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-79885

Status

Texto

Código\-Descrição

Campo IND\_STATUS gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-622783

Nº Recibo

Texto

Campo Num\_recibo gravado na tabela REINF\_PGER\_R4010\_OC

MFS\-79885

Tipo do Amb\.

Texto

Tipo do ambiente, gerado no evento R\-4010\.

MFS\-79885

Processo de Emissão

Texto

Processo de Emissão, gerado no evento R\-4010\.

MFS\-79885

Versão do Processo de Emissão

Texto

Versão do Processo de Emissão, gerado no evento R\-4010\.

MFS\-79885

Tipo de Inscrição Estabelecimento

Alfanumérico

Tipo Inscrição Estabelecimento, gerado no campo tplnsEstab do evento R\-4010\.

MFS\-79885

Número Inscrição Estabelecimento

Alfanumérico

Número Inscrição Estabelecimento, gerado no campo nrlnscEstab do evento R\-4010\.

MFS\-79885

CPF/Ident\. Benef\. Exterior

Texto

XXX\.XXX\.XXX\-XX ou

Grp/Ind/Cod do Benef\.

CPF do Beneficiário\. 

__\[ALTERAÇÃO MFS\-511669\] __

Caso beneficiário seja do exterior, apresentar o código do beneficiário, no formato: Grp/Ind/Cod do Benef\.

MFS\-79885

MFS\- 511669

Nome

Texto

Nome do Beneficiário\. 

MFS\-79885

Identificador Evento Adicional

Texto

Identificador de evento adicional por beneficiário, a critério do declarante\.

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-535745

__Corpo do Relatório – Identificação dos Dependentes __

CPF

Texto

XXX\.XXX\.XXX\-XX

Neste campo deve ser considerado o somatório do valor bruto do rendimento R\-4010, independente da data do recebimento e sim do período de apuração\.

MFS\-79885

Relação de Dependência

Texto

Código \- Descrição

Informar a Relação de Dependência

MFS\-79885

Descrição

Texto

Descrição

Descrição da Dependência, quando o tipo de relação de dependência for igual a ‘99 – Outros’

MFS\-79885

__Corpo do Relatório – Identificação do Rendimento__

Natureza do Rendimento

Texto

Natureza de Rendimento

MFS\-79885

Observação

Texto

Descrição

Observação

MFS\-79885

__Corpo do Relatório – Informações Relativas ao Rendimento __

Fato Gerador

Texto

DD/MM/AAAA

Data do Fato Gerador

MFS\-79885

Comp\.

Texto

DD/AAAA

Mês e Ano da Competência

MFS\-79885

13º

Texto

Código

Indicador de 13º

Lista de Valor Válido:

S

MFS\-79885

Rend\. Bruto

Texto

0,00

Valor do rendimento bruto

MFS\-79885

Rend\. Tributável

Texto

0,00

Valor tributável

MFS\-79885

Valor IR

Texto

0,00

Valor do IR

MFS\-79885

RRA

Texto

Código

Indicador de Rendimento Recebido Acumuladamente\.

Lista de Valor Válido:

S

MFS\-79885

FCI\_SCP

Texto

Código \- Descrição

 

Indicador de FCI e SCP

Lista de Valores Válidos:

1\-FCI; 

2\-SCP

MFS\-79885

Núm\. Insc\. FCI\_SCP

Texto

XX\.XXX\.XXX/XXXX\-XX

Número da Inscrição de FCI/SCP

MFS\-79885

% SCP

Texto

999

Percentual de SCP

MFS\-79885

IndJud

Texto

Código 

Informar o Indicativo exclusivo de rendimento de natureza diversa de RRA e que seja oriundo de decisão judicial

Lista de Valores Válidos:

S;

N

MFS\-79885

País Resid\. Exterior

Texto

999

Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior\.

MFS\-79885

Data Escr\. Cont\.

Texto

DD/MM/AAAA

Informar a data da escrituração contábil\.

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-535745

Observ\.

Texto

Observações

Este campo deve ser apresentado a partir da versão 2\.1\.2

MFS\-535745

__Corpo do Relatório – Informações Relativas às Deduções do Rendimento Tributável__

Tipo Dedução

Texto

Código \- Descrição

Informar o indicativo do tipo de dedução

__\[ALTERAÇÃO__ __ MFS\-566870\] __Inclusão da opção 8: 

Lista de valores válidos:

1 \- Previdência oficial;

2 \- Previdência privada;

3 \- Fundo de aposentadoria programada individual \- Fapi; 

4 \- Fundação de previdência complementar do servidor público \- Funpresp;

5 \- Pensão alimentícia;

7 – Dependentes;

8 – Desconto simplificado mensal\.

MFS\-79885

__MFS\-566870__

Valor Dedução 

Texto

0,00

MFS\-79885

Inform\. Entidade

Texto

Código

Informar se há informações da entidade de previdência complementar

Lista de valores válidos:

S \- Sim; 

N \- Não\.

MFS\-79885

Núm\. Inscr\. Previdencia Compl\.

Texto

Número da inscrição da entidade da previdência complementar

MFS\-79885

Valor Patroc\. FUNPRESP

Texto

0,00

Valor da contribuição do ente público patrocinador da Fundação de Previdência do Servidor Público \(Funpresp\)\. 

MFS\-79885

__Corpo do Relatório – Dependentes e Beneficiários da Pensão Alimentícia__

CPF 

Texto

XXX\.XXX\.XXX\-XX

CPF do dependente ou beneficiário da pensão alimentícia\.

MFS\-79885

Valor Dedução

Texto

0,00

Valor da dedução referente ao dependente ou do beneficiário da pensão alimentícia\.

MFS\-79885

__Corpo do Relatório – Rendimentos Isentos ou não Tributáveis__

Tipo Isenção

Texto

Código \- Descrição

Infomar o Tipo de Isenção:

Lista de valores válidos: 

1 \- Parcela isenta 65 anos;

2 \- Diária de viagem; 

3 \- Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho; 

4 \- Abono pecuniário; 

5 \- Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró\-labore, aluguéis e serviços prestados; 

6 \- Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço; 

7 \- Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995; 

8 \- Ajuda de custo;

EXCLUSÃO MFS\-549365\] 9 \- Rendimentos pagos sem retenção do IR na fonte \- Lei 10\.833/2003; 

\[INCLUSÃO MFS\-549365\] – 10 \- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função;

\[INCLUSÃO MFS\-549365\] – 11\- Resgate de previdência complementar por portador de moléstia grave;

99 \- Outros \(especificar\)\. 

MFS\-79885

MFS\-549365

Valor Isento

Texto

0,00

Valor da parcela isenta\.

MFS\-79885

Descrição do Rendimento

Texto

Descrição do rendimento isento/não tributável\.

MFS\-79885

Data Laudo

Texto

DD/MM/AAAA

Data da moléstia grave atribuída pelo laudo\.

MFS\-79885

__Corpo do Relatório – Processos Relacionados a não Retenção de Tributos__

Tipo Processo

Texto

Código \- Descrição

Preencher com o código correspondente ao tipo de processo

Lista de Valores Válidos:

1 \- Administrativo; 

2 – Judicial;

MFS\-79885

Núm\. Processo

Texto

Informar o número do processo administrativo/judicial\.

MFS\-79885

Cód\. Suspensão

Texto

Informar o código indicativo da suspensão

MFS\-79885

Valor Retenção que Deixou de ser Efetuada

Texto

0,00

Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial\. 

MFS\-79885

Valor Depósito Judicial

Texto

0,00

Valor do depósito judicial em função de processo administrativo ou judicial\.

MFS\-79885

Valor Comp\. Ano Calendário

Texto

0,00

Valor da compensação relativa ao ano calendário em função de processo judicial\. 

MFS\-79885

Valor Comp\. Anos Anteriores

Texto

0,00

Valor da compensação relativa a anos anteriores, em função de processo judicial\. 

MFS\-79885

Valor Rend\. Exigibilidade Suspensa

Texto

0,00

Valor do rendimento com exigibilidade suspensa\. 

MFS\-79885

__Corpo do Relatório – Detalhamento das Deduções Suspensas__

Tipo Dedução 

Texto

Código \- Descrição

Informar o indicativo do tipo de dedução: 

__\[ALTERAÇÃO__ __ MFS\-566870\] __Inclusão da opção 8: 

Lista de Valores Válidos:

1 \- Previdência oficial; 

2 \- Previdência privada; 

3 \- Fundo de aposentadoria programada individual \- Fapi; 

4 \- Fundação de previdência complementar do servidor público \- Funpresp; 

5 \- Pensão alimentícia; 

7 – Dependentes;

8 – Desconto simplificado mensal\.

MFS\-79885

MFS\-542897

MFS\-566870

Valor Dedução Suspensa

Texto

0,00

Valor da dedução da base de cálculo do imposto de renda, com exigibilidade suspensa\. 

MFS\-79885

__Corpo do Relatório – Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia__

CPF 

Texto

XXX\.XXX\.XXX\-XX

CPF do dependente ou beneficiário da pensão alimentícia\.

MFS\-79885

Valor Dedução Exigibilidade Suspensa

Texto

0,00

Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa

MFS\-79885

__Corpo do Relatório – Informações Complementares \- RRA__

Tipo Processo

Texto

Código \- Descrição

Informar o código e descrição correspondente ao tipo de processo: 

Lista de Valores Válidos:

1 \- Administrativo; 

2 – Judicial;

3 – Sem Processo

MFS\-79885

MFS\-805178

Núm\. Processo

Texto

Informar o número do processo/requerimento administrativo/judicial\.

MFS\-79885

Origem dos Recursos

Texto

Código \- Descrição

Informar o indicativo da origem dos recursos\.

Lista de Valores Válidos: 

1\-Recursos do próprio declarante; 

2\-Recursos de terceiros \- Declarante é a instituição financeira responsável pelo repasse dos valores

MFS\-79885

Descrição

Texto

Descrição dos Rendimentos Recebidos Acumuladamente \- RRA\.

MFS\-79885

Qtd Meses

Texto

0,0

Informar o número de meses relativo aos Rendimentos Recebidos Acumuladamente \- RRA

MFS\-79885

CNPJ Origem Recursos

Texto

XX\.XXX\.XXX/XXXX\-XX

CNPJ da empresa que repassou os recursos\.

MFS\-79885

__Corpo do Relatório – Despesas com Processo Judicial__

Valor Despesas Custas Judiciais

Texto

0,00

Informar o valor da despesa com custas judiciais

MFS\-79885

Valor Despesa Advogados

Texto

0,00

Informar o valor da despesa com advogado\(s\)\.

MFS\-79885

__Corpo do Relatório – Identificação do Advogado__

Tipo Inscrição

Texto

Código \- Descrição

Tipo de inscrição do advogado\.

Lista de Valores Válidos:

1\-CNPJ; 

2\-CPF

MFS\-79885

Núm\. Inscrição

Texto

Informar o número de inscrição do advogado\.

MFS\-79885

Valor Advogado

Texto

0,00

Valor da despesa com o advogado\.

MFS\-79885

__Corpo do Relatório – Informações de Processo Judicial__

Núm\. Processo

Texto

Informar o número do processo judicial

MFS\-79885

Origem Recurso

Texto

Código \- Descrição

Informar o indicativo da origem dos recursos: 

Lista de Valores Válidos:

1 \- Recursos do próprio declarante; 

2 \- Recursos de terceiros \- Declarante é a instituição financeira responsável pelo repasse dos valores\.

MFS\-79885

CNPJ Origem Recurso

Texto

Informar o CNPJ da empresa que repassou os recursos\.

MFS\-79885

Descrição

Texto

Descrição

MFS\-79885

__Corpo do Relatório – Despesas com Processo Judicial__

Valor Despesas Custas Judiciais

Texto

0,00

Informar o valor da despesa com custas judiciais

MFS\-79885

Valor Despesa Advogados

Texto

0,00

Informar o valor da despesa com advogado\(s\)\.

MFS\-79885

__Corpo do Relatório – Identificação do Advogado__

Tipo Inscrição

Texto

Código \- Descrição

Tipo de inscrição do advogado\.

Lista de Valores Válidos:

1\-CNPJ; 

2\-CPF

MFS\-79885

Núm\. Inscrição

Texto

Informar o número de inscrição do advogado\.

MFS\-79885

Valor Advogado

Texto

0,00

Valor da despesa com o advogado\.

MFS\-79885

__Corpo do Relatório – Informações Complementares Relativas a Pagamentos no Exterior__

Ind\. Núm\. Identificação Fiscal

Texto

Código \- Descrição

Informar o indicativo do Número de Identificação Fiscal \- NIF: 

Lista de Valores Válidos:

1\-Beneficiário com NIF;

2\-Beneficiário dispensado do NIF; 

3\-País não exige NIF\.

MFS\-79885

Núm\. Identificação Fiscal

Texto

Informar o número de Identificação Fiscal \- NIF\.

MFS\-79885

Forma de Tributação

Texto

Informar a forma de tributação\.

MFS\-79885

__Corpo do Relatório – Endereço do Beneficiário Residente ou Domiciliado no Exterior__

Logradouro

Texto

Informar o logradouro

MFS\-79885

Núm\.

Texto

Informar o número do logradouro\.

MFS\-79885

Complemento

Texto

Informar o complemento do logradouro\.

MFS\-79885

Bairro

Texto

Informar o bairro

MFS\-79885

Cidade

Texto

Informar a cidade

MFS\-79885

Estado

Texto

Informar o estado

MFS\-79885

Cód\. Postal

Texto

Informar o código postal \(CEP\)

MFS\-79885

Telefone

Texto

Informar o telefone\.

MFS\-79885

__Corpo do Relatório – Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde\.__

Núm\. Inscrição

Texto

Informar o número do CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde\.

MFS\-79885

Registro ANS

Texto

Informar o Registro na Agência Nacional de Saúde \- ANS\.

MFS\-79885

Valor Saúde

Texto

0,00

Informar o valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular

MFS\-79885

__Corpo do Relatório – Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial__

Tipo Inscrição

Texto

Código \- Descrição

Tipo de Inscrição

Lista de Valores Válidos

1 \- Pessoa jurídica; 

2 \- Pessoa física\.

MFS\-79885

Núm\. Inscrição

Texto

XX\.XXX\.XXX/XXXX\-XX ou

XXX\.XXX\.XXX\-XX

Número de Inscrição

MFS\-79885

Valor Reembolso

Texto

0,00

Valor do Reembolso relativo ao período da apuração

MFS\-79885

Valor Reembolso Anos Anteriores

Texto

0,00

Valor do Reembolso relativo aos anos anteriores

MFS\-79885

__Corpo do Relatório – Informações de Dependente do Plano de Saúde Coletivo Empresarial__

CPF 

Texto

XXX\.XXX\.XXX\-XX

CPF do dependente

MFS\-79885

Valor Saúde

Texto

0,00

Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente

MFS\-79885

__Corpo do Relatório – Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial__

Tipo Inscrição

Texto

Código \- Descrição

Informar o tipo de inscrição do prestador de serviços

Lista de Valores Válidos

1 \- Pessoa jurídica; 

2 \- Pessoa física\.

MFS\-79885

Núm\. Inscrição

Texto

XX\.XXX\.XXX/XXXX\-XX ou

XXX\.XXX\.XXX\-XX

Informar o tipo de inscrição do prestador de serviços de assistência médica\.

MFS\-79885

Valor Reembolso Per\. Apur,

Texto

0,00

Informar o valor do reembolso relativo ao período\.

MFS\-79885

Valor Reembolso Anos Anteriores

Texto

0,00

Informar o valor do reembolso relativo aos anos anteriores\.

MFS\-79885

## <a id="_Toc427766288"></a><a id="_Toc101182972"></a>Layout do Relatório

__\[ALTERAÇÃO MFS\-535745 \] \- A partir da Versão 2\.1\.2 do REINF__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ==

__XXX\-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                           							   Pág\.: 999999__

__Data: 99/99/9999 às HH:MM:SS  hs__

__                                                        			 Relatório de Conferência do Evento R\-4010 – Analítico__

__                                                                                      		Período: MM/AAAA__

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

__Estabelecimento__: XXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

__\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\___

          

      	

__Informações Complementares do Contribuinte__

__Natureza Jurídica:__ XXXX

__	Identificação do Evento / Beneficiário __

__Tipo Arquivo: __XXXXXXXXXXXXXXX__ 	__

__    Status: __X\-XXXXXXXXXXXX

__N\. Recibo: __XXXXXXXXXXXXXXXXXXX                           

__Tipo do Amb\.__ : XXXXXXXXX__        __

__Processo de Emissão: __X\-XXXXXX   

  __Versão do Processo de Emissão: __XXXXXXXX              __               __

__Tipo de Inscrição Estabelecimento__: X\-XXXXXXXXXXXX           

__Número Inscrição Estabelecimento__: XXXXX

__CPF/__ Ident\. Benef\. Exterior__:__ XXX\.XXX\.XXX\-XX ou 

Grp/Ind/Cod do Benef\.

	__Nome:__ XXXXXXXXX 

Identificador Evento Adicional: XXXXXXXX

__Identificação dos Dependentes__

__CPF: __XXX\.XXX\.XXX\-XX

__Relação de Dependência:__ Codigo \- Descrição

__Descrição:__ Descrição

__Identificação do Rendimento__

__Natureza do Rendimento: __XXXXXXX

__Observação:__ Descrição

__Informações Relativas ao Rendimento__

__Fato Gerador__

__Comp\.__

__13º__

__Rend\. Bruto__

__Rend\. Tributável__

__Valor IR__

__RRA__

__FCI\_SPC__

__Núm\. Insc\. FCI\_SCP__

__% SCP__

__IndJud__

__País Resid\. Exterior__

Data Escr\. Cont\.

Observ\.

DD/MM/AAAA

DD/AAAA

Cód\.

0,00

0,00

0,00

Cód\.

Cód\.  – Descrição

XX\.XXX\.XXX/XXXX\-XX

999

Cód\.

999

DD/MM/AAAA

XXXX

__Informações Relativas às Deduções do Rendimento Tributável__

__Tipo Dedução__

__Valor Dedução__

__Inform\. Entidade__

__Núm\. Inscr\. Previdência Compl\.__

__Valor Patroc\. FUNPRESP__

Código \- Descrição

0,00

Código

0,00

__Dependentes e Beneficiários da Pensão Alimentícia__

__CPF: __XXX\.XXX\.XXX\-XX

__Valor Dedução:__ 0,00

__Rendimentos Isentos ou não Tributáveis__

__Tipo Isenção__

__Valor Isento__

__Descrição Rendimento__

__Data Laudo__

Código \- Descrição

0,00

DD/MM/AAAA

__Processos Relacionados a não Retenção de Tributos__

__Tipo Processo__

__Núm\. Processo__

__Cód\. Suspensão__

__Valor Retenção que Deixou de ser Efetuada__

__Valor Depósito Judicial__

__Valor Comp\. Ano Calendário__

__Valor Comp\. Anos Anteriores__

__Valor Rend\. Exigibilidade Suspensa__

Código \- Descrição

0,00

0,00

0,00

0,00

__Detalhamento das Deduções Suspensas__

__Tipo Dedução:__ Código \- Descrição

__Valor Dedução Suspensa:__0,00

__Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia__

__CPF: __XXX\.XXX\.XXX\-XX

__Valor Dedução Exigibilidade Suspensa:__ 0,00

__Informações Complementares \- RRA__

__Tipo Processo__

__Núm\. Processo__

__Origem dos Recursos__

__Descrição__

__Qtd\. Meses__

__CNPJ Origem Recursos__

Código \- Descrição

Código \- Descrição

__0,0__

XX\.XXX\.XXX/XXXX\-XX

__Despesas com Processo Judicial__

__Valor Despesas Custas Judiciais:__ 0,00

__Valor Despesa Advogados:__ 0,00

__ Identificação do Advogado__

__Tipo Inscrição__

__Núm\. Inscrição__

__Valor Advogado__

Código \- Descrição

__0,00__

__Informações de Processo Judicial__

__Núm\. Processo__

__Origem Recurso__

__CNPJ Origem Recurso__

__Descrição__

Código \- Descrição

__Despesas com Processo Judicial__

__Valor Despesas Custas Judiciais:__ 0,00

__Valor Despesa Advogados:__0,00

__Identificação do Advogado__

__Tipo Inscrição: __

__Núm\. Inscrição__

__Valor Advogado__

Código \- Descrição

__0,00__

__Informações Complementares Relativas a Pagamentos no Exterior__

__Ind\. Núm\. Identificação Fiscal__

__Núm\. Identificação Fiscal__

__Forma de Tributação__

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

__Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde\.__

Núm\. Inscrição: XXXXXXXXX

Registro ANS: XXXXXXXXXXX

Valor Saúde: 0,00

__Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial__

__Tipo Inscrição__

__Núm\. Inscrição__

__Valor Reembolso__

__Valor Reembolso Anterior__

Cód\. \-  Descrição

XX\.XXX\.XXX/XXXX\-XX ou XXX\.XXX\.XXX\-XX

0,00

0,00

__Informações de Dependente do Plano de Saúde Coletivo Empresarial__

__CPF : __XXX\.XXX\.XXX\-XX

__Valor Saúde: __0,00

__Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial__

__Tipo Inscrição__

__Núm\. Inscrição__

__Valor Reembolso__

__Valor Reembolso Anterior__

Cód\. \-  Descrição

XX\.XXX\.XXX/XXXX\-XX ou XXX\.XXX\.XXX\-XX

0,00

0,00

