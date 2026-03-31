# MTZ-VAFMG_Geracao_Relatorio_EFD-Fiscal

- **Fonte:** MTZ-VAFMG_Geracao_Relatorio_EFD-Fiscal.docx
- **Modificado:** 2026-01-07
- **Tamanho:** 429 KB

---

THOMSON REUTERS

Módulo VAF\-MG 

 VAF\-MG – Geração do Relatório da DAMEF com base no EFD\- Fiscal \(Portaria 175/2020\) 

__Localização__: Menu Estadual, Módulo VAF\-MG, item de menu DAMEF\-EFD Fiscal  Geração do Relatório \(Portaria SRE 175/2020\)	

Packages envolvidas: est\_vafmg\_damef\_EFD\_fproc, est\_vafmg\_r\_damef\_efd

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS\-45348

Liliane Assaf

Criar relatório da DAMEF em atendimento a Portaria SRE n° 175/2020

Escopo:

1. Quadro das Operações e Prestações de Entradas e Saídas \- campos 60 a 115 da Portaria 175/2020, com exceção dos campos 84, 85, 112, 114\.
2. Quadro Resumo das Entradas e Saídas \- campos 26 a 47 da Portaria 175/2020\.

Tópicos do documento:

\- 1\.1, 1\.2, 1\.3, 2\.1 ao 2\.10, 3 e 4\.

05/10/2020

MFS\-44425

Liliane Assaf

Dar prosseguimento à criação do Relatório da DAMEF em atendimento a Portaria SRE n° 175/2020

Escopo:

1. Quadro de Exclusão do VAF \- campos 1 ao 20 da Portaria 175/2020\. 
2. Quadro VAF \- campos 21 ao 25 da Portaria 175/2020\.

  

Tópicos do documento:

\- 1\.3 \(nova crítica\), 2\.11, 2\.12, 5 e 6\.

14/10/2020

MFS\-46069

Liliane Assaf

Criação do Relatório de Conferência Nota a Nota\.

Escopo:

1. Inclusão de campo na tela de geração: 

“Gerar Relatório com Detalhamento Nota a Nota em arquivo xls”

1. Disponibilização do Relatório de Conferência que demonstra os documentos que compõe os 4 quadros já liberados:

\- Quadro das Operações e Prestações de Entradas e Saídas

\- Quadro Resumo das Entradas e Saídas

\- Quadro de Exclusão do VAF

\- Quadro VAF

           

Tópicos do documento

\- 1\.1 – Tela da Geração

\- 8 – Relatório de Conferência

27/10/2020

MFS\-45263

Liliane Assaf

Tratamento dos quadros com valores originários do registro 1400 da EFD\-FISCAL\.

__Escopo__:

\- Regra de recuperação do registro 1400 \(tópico [2\.13](#_2.13_–_Recuperação)\)

\- Alteração no Quadro das Operações e Prestações de Entradas e Saídas \([tópico 3](#_QUADRO_DAS_OPERAÇÕES)\), para preenchimento dos campos baseados no 1400:

   \- ENTRADAS \- PRODUTOS AGROPECUÁRIOS \(RN84\)

   \- ENTRADAS \- GERAÇÃO DE ENERGIA ELÉTRICA PARA CONSUMO PRÓPRIO \(RN85\)

   \- SAÍDAS \- TRANSPORTE TOMADO \(RN112\)

   \- SAÍDAS – COOPERATIVAS \(RN114\)

\- Alteração no Quadro Resumo das Entradas e Saídas \([tópico 4](#_QUADRO_RESUMO_DAS)\), para preenchimento dos campos baseados no 1400:

   \- ENTRADAS \- PRODUTOS AGROPECUÁRIOS/ HORTIFRUTIGRANJEIROS \(RN44\)

   \- ENTRADAS \- GERAÇÃO ENERGIA ELÉTRICA PARA CONSUMO PRÓPRIO \(RN45\)

   \- SAÍDAS \- TRANSPORTE TOMADO \(RN46\)

   \- SAÍDAS – COOPERATIVAS \(RN47\)

\- Alteração no Quadro VAF \([tópico 6](#_Quadro_VAF)\), completando a regra de preenchimento do campo:

   \- OUTRAS ENTRADAS \(RN23\)

\- Inclusão do Quadro VAF – Detalhamento de Outras Entradas \([tópico 7](#_Quadro_VAF_-)\)\.

\- Alteração no Relatório de Conferência para inclusão do registro 1400 \([tópico 8](#_Relatório_de_Conferência)\) para inclusão dos registros 1400\.

29/10/2020

MFS\-45264

Liliane Assaf

Tratamento do inventário: criação do “Quadro de Totalização do Inventário” e alteração no relatório de conferência\.

Escopo:

\- Criação dos campos Data de Inventário Inicial e Data de Inventário Final na tela \(ver tópico [1\.1](#_–_Tela_da)\)

\- Definição da recuperação dos registros de Inventário \(ver tópico [2\.14](#_2.14_–_Recuperação)\)

\- Definição do Quadro de Totalização do Inventário a ser apresentado no relatório \(ver tópico [8](#_Quadro_Totalização_do)\)

\- Definição do Relatório de Conferência para demonstrar o inventário \(ver tópico [9](#_Relatório_de_Conferência)\)

13/09/2021

MFS \- 418008

Graciela Soares

Os ajustes relacionados nesta MFS correspondem à inserção de Novos CFOP´s na composição dos campos, foram alterados as RN´s: 08, 12, 13, 17, 66, 94 e 101 e  
Exclusão do CFOP 7210da RN 17

MFS \-544515

Graciela Soares

Ajuste na Geração do Relatório da DAMEF, no item de Operações e Prestações de Saída \-> Saídas para o Estado, à composição dos campos Vendas e Outras incluindo os registros do Sped Fiscal C320 e C490\. Foram alteradas as RN´s: 88 e 94\. 

Sumário

[1\.	Introdução	5](#_Toc139647329)

[1\.1	– Tela da Geração	6](#_Toc139647330)

[1\.2 \- Tratamento para Geração centralizada por Inscrição Estadual Única	6](#_Toc139647331)

[1\.3 – Críticas da Geração	7](#_Toc139647332)

[2\.	Regras de Geração dos Registros EFD\-Sped Fiscal	8](#_Toc139647333)

[2\.1 – Recuperação das Notas Fiscais de Entrada e Saída de Modelos 01, 1B, 04, 55, 65 \(C190\)	8](#_Toc139647334)

[2\.2 – Recuperação das Notas Fiscais de Entrada de Energia Elétrica Modelos 06, 66 \(C590\)	12](#_Toc139647335)

[2\.3 – Notas Fiscais de Saída Energia Elétrica Modelos 06, 66 \(C590, C690, C790\)	14](#_Toc139647336)

[2\.3\.1 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06, 66 \(C590\)	16](#_Toc139647337)

[‘2\.3\.2 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06 \(C690\)	18](#_Toc139647338)

[2\.3\.3 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06 \(C790\)	20](#_Toc139647339)

[2\.4 – Recuperação das Notas Fiscais de Entrada de Comunicação Modelos 21, 22 \(D590\)	21](#_Toc139647340)

[2\.5 – Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D590, D690, D696\)	23](#_Toc139647341)

[2\.5\.1 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D590\)	25](#_Toc139647342)

[2\.5\.2 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D690\)	26](#_Toc139647343)

[2\.5\.3 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D696\)	28](#_Toc139647344)

[2\.6 – Recuperação das Notas Fiscais de Entrada e Saída de Transporte Modelo 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 \(D190\)	29](#_Toc139647345)

[2\.7 – Recuperação dos Cupons Fiscais Modelos 02, 2D, 60 \(C490\)	33](#_Toc139647346)

[2\.8 – Recuperação dos Cupons Fiscais Modelos 13, 14, 15, 16 e 2E \(D390\)	35](#_Toc139647347)

[2\.9 – Recuperação dos Bilhetes Modelos 13, 14, 15, 16 \(D300\)	35](#_Toc139647348)

[2\.10 – Recuperação dos Bilhetes de Modelos 13, 14, 15 E 16 \(D410\)	37](#_Toc139647349)

[2\.11 – Recuperação dos Ajuste/Outros Valores do Lançamento Fiscal das Notas de Entrada e Saída de Modelos 01, 1B, 04, 55, 65 \(C197\)	39](#_Toc139647350)

[2\.12 – Recuperação das Informações Adicionais da Apuração – Valores Declaratórios \(E115\)	41](#_Toc139647351)

[2\.13 – Recuperação dos Registros 1400 \(1400\)	42](#_Toc139647352)

[2\.14 – Recuperação dos Registros de Inventário Inicial e Final \(H005\)	44](#_Toc139647353)

[2\.15 – Recuperação das Notas Fiscais de Venda a Consumidor Modelo 02 \(C320\)	45](#_Toc139647354)

[3\.	QUADRO DAS OPERAÇÕES E PRESTAÇÕES DE ENTRADAS e SAÍDAS	48](#_Toc139647355)

[3\.1 – Layout	48](#_Toc139647356)

[3\.2 – Gravação dos Campos	51](#_Toc139647357)

[3\.2\.1 \- Operações e Prestações de Entradas	51](#_Toc139647358)

[3\.2\.2 \- Operações e Prestações de Saída	60](#_Toc139647359)

[4\.	QUADRO RESUMO DAS ENTRADAS e SAÍDAS	71](#_Toc139647360)

[4\.1 – Layout	71](#_Toc139647361)

[4\.2 – Gravação dos Campos	72](#_Toc139647362)

[5\.	Quadro Exclusão do VAF	76](#_Toc139647363)

[5\.1 – Layout	76](#_Toc139647364)

[5\.2 – Gravação dos Campos	77](#_Toc139647365)

[5\.2\.1 – Exclusão do VAF \- Entradas	77](#_Toc139647366)

[5\.2\.2 – Exclusão do VAF – Saídas	81](#_Toc139647367)

[6\.	Quadro VAF	85](#_Toc139647368)

[6\.1 – Layout	85](#_Toc139647369)

[6\.2 – Gravação dos Campos	85](#_Toc139647370)

[7\.	Quadro VAF \- Detalhamento de Outras Entradas	88](#_Toc139647371)

[7\.1 – Layout	88](#_Toc139647372)

[7\.2 – Gravação dos Campos	90](#_Toc139647373)

[8\.	Quadro Totalização do Inventário	97](#_Toc139647374)

[8\.1 – Layout	97](#_Toc139647375)

[8\.2 – Gravação dos Campos	97](#_Toc139647376)

[9\.	Relatório de Conferência	98](#_Toc139647377)

[9\.1 – Layout	98](#_Toc139647378)

[9\.2 – Regra de Geração do Relatório	99](#_Toc139647379)

# <a id="_Toc139647329"></a>Introdução 

A partir de 2020 \(VAF ano\-base 2019\) a DAMEF será elaborada pela SEF/MG através do processamento dos arquivos da Escrituração Fiscal Digital – EFD do exercício de 2019, que foram transmitidos pelos contribuintes\. A DAMEF será disponibilizada no Sistema Integrado de Administração da Receita Estadual – SIARE para que os contribuintes complementem alguns dados e validem a declaração, no período de 01/09/2020 a 30/09/2020\.

As Regras Gerais de Elaboração e Validação da DAMEF foram estabelecidas pelo Anexo I da Portaria SRE Nº 175, de 17 de julho de 2020 \(publicada em 18/07/2020\), que dispõe em detalhes sobre a nova forma de elaboração da declaração\.

Sendo assim o relatório disponível no menu “*DAMEF\-EFD Fiscal  Geração do Relatório \(Portaria SRE 175/2020\)*” não tem mais função de entrega ao fisco, mas servirá de apoio na etapa de validação da DAMEF gerada pelo SIARE\.

Como a DAMEF disponibilizada pela SEF/MG é feita com base nas informações prestadas nos arquivos deo EFD \(Sped Fiscal\), as regras de *“Geração do Relatório \(Portaria SRE 175/2020\)”* do módulo VAF\-MG, foram definidas com base nas regras de geração do SPED FISCAL\. O objetivo é evitar  divergência entre as informações apresentadas na DAMEF gerada pelo sistema SIARE da Receita Estadual e a DAMEF gerada no módulo VAF\-MG\.

O relatório da DAMEF emitido através do menu Obrigações  Geração do Relatório, se mantém disponível no sistema para qualquer necessidade de retificação da VAF originalmente emitida por essa opção \(VAF ano\-base anterior a 2019\)\. 

Para ano\-exercício A PARTIR DE 2020, então:

    Utlizar a Geração do Relatório do menu DAMEF\-EFD FISCAL >> Geração do Relatório \(Portaria SRE 175/2020\)\.

Para ano\-exercício ANTERIOR A 2020, então:

    Utlizar a Geração do Relatório do menu Obrigações  Geração do Relatório\.

O relatório da DAMEF emitido através do Obrigações  Geração do Relatório é composto pelos quadros:

- Cadastro do Responsável Legal
- Cadastro do Contribuinte
- Totalização dos Valores de Inventário Inicial
- Totalização dos Valores de Inventário Final
- Operações e Prestações de Entradas e Saídas
- Resumo das Entradas e Saídas
- Exclusão do VAF
- VAF
- Detalhamento de Outras Entradas – VAF
- DRO
- DESPESAS OPERACIONAIS 

Já o relatório da DAMEF emitido pelo menu DAMEF\-EFD FISCAL, não apresenta os quadros que são oriundos de informações incluídas manualmente, como DRO, DESPESAS OPERACIONAIS\.  Também não apresentamos no quadro VAF \- Detalhamento de Outras Entradas \([tópico 7](#_Quadro_VAF_-)\) os campos referentes às regras da Portaria 175/2020:

\- RN124 \- PRESTAÇÃO SERVIÇO TRANSPORTE RODOVIÁRIO 

\- RN127 \- MUDANÇA DE MUNICÍPIO

\- RN130 \- RESUMO POR MUNICÍPIO

Base Legal: Portaria SRE Nº 175 DE 17 de julho de 2020

Veja:

[https://www\.mg\.gov\.br/servico/validar\-declaracao\-anual\-do\-movimento\-economico\-fiscal\-damef](https://www.mg.gov.br/servico/validar-declaracao-anual-do-movimento-economico-fiscal-damef)

[http://www\.fazenda\.mg\.gov\.br/empresas/legislacao\_tributaria/portarias/2020/port\_subsec175\_2020\.html](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/portarias/2020/port_subsec175_2020.html)

## <a id="_–_Tela_da"></a><a id="_Toc139647330"></a>– Tela da Geração

A tela de geração é formada pelos seguintes parâmetros:

- Exercício
- Ano Base

\[MFS\-45264\]

- Data de Inventário Inicial: default 31/12/AAAA, onde AAAA é o ano anterior ao Ano Base\.
- Data de Inventário Final: default 31/12/AAAA, onde AAAA é o Ano Base\.
- Geração centralizada por Inscrição Estadual Única
- Gerar Relatório com Detalhamento Nota a Nota em arquivo xls
- Estabelecimentos com UF = MG

## <a id="_1.2_-_Tratamento"></a><a id="_Toc139647331"></a>1\.2 \- Tratamento para Geração centralizada por Inscrição Estadual Única

Parâmetro “Geração centralizada por Inscrição Estadual Única”\. 

A geração do relatório da VAF\-MG deve considerar o parâmetro disponível na tela de Geração do Relatório do módulo VAF\-MG\. O tratamento da inscrição estadual única será o mesmo já existente no Mastersaf para a emissão dos livros fiscais, da seguinte forma:

- Os registros de identificação do contribuinte devem ser gerados com os dados do estabelecimento centralizador;
- Ao utilizar qualquer parametrização cujo cadastro seja por estabelecimento, deve\-se utilizar a parametrização feita em nome do estabelecimento centralizador;
- Além dos documentos fiscais do estabelecimento da geração, que é o estabelecimento centralizador, deverão ser recuperados também os documentos dos estabelecimentos centralizados\. Assim, a regra é considerar os documentos fiscais de todos os estabelecimentos envolvidos na centralização, lembrando que a parametrização dos estabelecimentos Centralizador x Centralizados fica no módulo Controle das Obrigações Estaduais, no item “Obrigações  Empresas/Estabelecimentos com Inscrição Estadual Única”; 
- Quando se tratar de Cupom Fiscal e Inventário, também devem ser recuperados os registros referentes aos estabelecimentos centralizador e centralizados\.
- Os registros gerados a partir dos dados dos livros fiscais \(P1, P2 e P9\) deverão considerar as gerações feitas p/o estabelecimento centralizador, utilizando sempre os livros das obrigações fiscais 161, 162, 163, 164 e 165, que são os códigos dos livros fiscais utilizados por quem trabalha com inscrição estadual única\. 

Segue detalhes de cada quadro apresentados no relatório nos próximos tópicos\.

## <a id="_Toc139647332"></a>1\.3 – Críticas da Geração 

Caso não exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, exbir mensagem no log:

ATENCAO: Dados Iniciais Não preenchidos para a empresa XXX e estabelecimento YYYYYY\. As Informações do VAF não serão calculadas\. Favor acessar o menu DAMEF\-EFD Fiscal >> Dados Iniciais e incluir as informações solicitadas\.

Caso exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, mas o campo “Tipo de Contribuinte” estiver sem preenchimento, exbir mensagem no log:

ATENCAO: Campo Tipo de Contribuinte Não preenchido para a empresa XXX e estabelecimento YYYYYY\. As Informações do VAF não serão calculadas\. Favor acessar o menu DAMEF\-EFD Fiscal >> Dados Iniciais e incluir as informações solicitadas\.

\[MFS\-44425\]

Caso exista registro na tabela de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, mas o campo “Tipo de Contribuinte” estiver preenchimento com a opção Outros, exbir mensagem no log e abortar o processo:

ATENCAO: Campo Tipo de Contribuinte preenchido com opção Outros para a empresa XXX e estabelecimento YYYYYY\.  Esta opção deixou de ser válida para a DAMEF a partir da Portaria 175/2020\. Favor acessar o menu DAMEF\-EFD Fiscal >> Dados Iniciais e corrigir a informação solicitada\.

Caso o ano exercício informado na tela seja anterior a 2020, exibir a seguinte mensagem no log e continuar o processamento:

Para retificações dos relatórios da DAMEF de exercícios anteriores a 2020, utilizar a geração disponível no menu Obrigações >> Geração do Registro\. 

Caso exista registro na tabela de Manutenção de Dados Iniciais da VAF, para o estabelecimento e ano exercício informado na tela de geração, mas o campo “Perfil de Apresentação da EFD” estiver sem preenchimento, exbir mensagem no log e abortar o processo:

ATENCAO: Campo Perfil de Apresentação da EFD Não preenchido para a empresa XXX e estabelecimento YYYYYY\. As Informações do VAF não serão calculadas\. Favor acessar o menu DAMEF\-EFD Fiscal >> Dados Iniciais e incluir as informações solicitadas\.

Caso não exita registro na tabela de Dados Iniciais do Sped Fiscal, para o estabelecimento informado na tela da geração, então exibir a mensagem no log:

ATENCAO: Parametrização dos Dados Iniciais do SPED – EFD Escrituração Fiscal Digital não encontrada para a empresa XXX e estabelecimento YYYYYY\. Favor acessar o módulo SPED \- EFD Escrituração Fiscal Digital e informar os dados iniciais no menu Parâmetros >> Dados Iniciais\.

# <a id="_Toc139647333"></a>Regras de Geração dos Registros EFD\-Sped Fiscal

Neste tópico vamos definir todas as regras de geração dos registros dos Sped Fiscal que serão utilizados na montagem dos quadros da VAF\-MG\.

Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nesses regras os mesmos critérios de geração dos registros do SPED FISCAL\.

## <a id="_2.1_–_Recuperação"></a><a id="_Toc139647334"></a>2\.1 – Recuperação das Notas Fiscais de Entrada e Saída de Modelos 01, 1B, 04, 55, 65 \(C190\)

O objetivo desta geração é recuperar toda movimentação de entrada e saída de modelos 01, 1B, 04, 55, 65, com os mesmos critérios da geração do registro C190 do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __C190__\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx e Notas\_Especiais\_C100\_v8\.doc\.

__Origem dos dados__: 

\- SAFX07 / SAFX08 / SAFX09 – Tabelas dos Documentos Fiscais;

                                 

\- Parametrização dos Dados Iniciais do SPED FISCAL

                                  

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 01, 1B, 04, 55, 65

\- Classificação do Documento Fiscal = '1' \- Mercadoria,'3' – Mercadoria e Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas e Saídas \(MOVTO\_E\_S da SAFX07\)

\- Somente notas *não canceladas*;

\- Considerar notas fiscais com e sem itens de mercadoria e serviço;

\- Não considerar as notas de mapa resumo de Utilities \(Ind\_Origem\_Info <> '1' \)

\- Não considerar as notas fiscais extemporâneas de saída \(MOVTO\_E\_S = ‘9’ e DAT\_ESCR\_EXTEMP > 0\);

\- Não considerar as notas fiscais de Transferência de Crédito / Débito \(IND\_TRANS\_CRED da SAFX07\)

\- Não considerar as notas de Situação Especial ‘1’ – Venda Globalizada, ‘2’ – Acompanhamento de ECF, ‘8’\-Remessa por Conta e Ordem  \(IND\_SITUACAO\_ESP da SAFX07\) 

\- Para notas com Código Modelo 65, recuperar só notas de saída \(MOVTO\_E\_S = '9'\)

  

\- Não considerar NF Eletrônica denegada/inutilizada \(campo IND\_NFE\_DENEG\_INUT da SAFX07 não preenchido\)\.

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo 23 \- VLR\_TOT\_NOTA da SAFX07\);

\- Valor ICMS Substituição Tributária \(campo 48 \- VLR\_SUBST\_ICMS da SAFX07\);

Importante: o valor de ST deve ser considerado apenas quando o campo “82\-Apropria” da SAFX07  for =  “S”  \(IND\_CRED\_ICMSS\)\.

\- Valor do IPI \(campo 40 \- VLR\_IPI da SAFX07\);

Para os itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX08;

\- Valor Contábil do Item \(campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\);

\- Valor ICMS Substituição Tributária \(campo 52 \- VLR\_SUBST\_ICMS da SAFX08\);

Importante: o valor de ST deve ser considerado apenas quando o campo “78\-Apropria” da SAFX08  for =  “S”  \(IND\_CRED\_ICMSS\)\.

\- Valor do IPI \(campo 48 \- VLR\_IPI da SAFX08\)

Para os itens de serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX09;

\- Valor Total do Serviço \(campo 15 \- VLR\_TOT da SAFX09\)\.

\- Valor do ICMS\-ST : considerar zero;

\- Valor do IPI: considerar zero;

Aplicar os Tratamentos de Situação Especial:

1\) __NF Simples Faturamento__:

A nota fiscal de Simples Faturamento é identificada pelos campos:

\- Nvl\(CAP\.IND\_SITUACAO\_ESP,' '\) = 'D' e

\- CFO\.COD\_CFO IN \('1922', '2922','1117','2117','5922', '6922','5116', '6116','1923', '2923', '5923', '6923'\)

Caso a nota seja de Simples Faturamento, verificar o quadro “Situação Especial 08 – Faturamento Simples” presente na tela de Dados Iniciais do Sped Fiscal, onde estão contidos os seguintes flags: ICMS, ICMS\-ST, PIS/COFINS\-ST, PIS/COFINS, IPI\.

Se __todos__ os flags estiverem desmarcados, então:

     ZERAR todos os valores indicados acima \(Valor Total, ICMS\-ST, IPI\)

Senão

    Recuperar o valor Total da nota\.

    Se flag ICMS\-ST estiver desmarcado, então:

             ZERAR o Valor do ICMS\-ST;

     Se flag IPI estiver desmarcado, então:

             ZERAR o valor do IPI;

2\) __NF Importação sem lancto do ICMS no P1/P9__:

Essa nota fiscal é identificada pelo campo IND\_SITUACAO\_ESP da SAFX07= ‘9’\.

Caso a nota se encaixe nessa situação, ZERAR o Valor do ICMS\-ST\.

__Observações__:

Observação sobre as notas extemporâneas:

As notas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

*\[Alteração – OS 3227\]*

*Exceção para notas fiscais extemporâneas de Saída:*

*Não apresentar os valores dos documentos extemporâneos de saída, tendo em vista que não serão considerados para os livros P2, P2A e P9\.*

*Ver regra para o tratamento destas notas no documento “Notas\_Especiais\_C100\_ v7\.doc”*

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas, de transferência, de simples faturamento,extemporâneos\) foram definidos com base no tratamento do C190 do Sped Fiscal, conforme *documento “Notas\_Especiais\_C100\_ v8\.doc”\. Não há necessidade de tratar notas complementares uma vez que, segundo o documento “Notas\_Especiais\_C100\_V8\.doc”, ela passou a ser gerada normalmente no C190, sem aplicação de tratamento que zera valor contábil\.*

__Nota técnica:__

__*Ver C\_EFD01 da Efd\_Dic\_Dados*__

## <a id="_2.2_–_Recuperação"></a><a id="_Toc139647335"></a>2\.2 – Recuperação das Notas Fiscais de Entrada de Energia Elétrica Modelos 06, 66 \(C590\)

O objetivo desta geração é recuperar toda movimentação de entrada modelos 06, 66, com os mesmos critérios da geração do registro __C590__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C590\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx e Notas\_Especiais\_C500\-Entradas\.doc\.

__Origem dos dados__: 

\- SAFX07 / SAFX08 / SAFX09 – Tabelas dos Documentos Fiscais;

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 06, 66

\- Classificação do Documento Fiscal = '1' \- Mercadoria,'3' – Mercadoria e Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas \(MOVTO\_E\_S <> ‘9’ da SAFX07\)

\- Somente notas *não canceladas*;

\- Considerar notas fiscais com e sem itens de mercadoria e serviço;

\-  Se o parâmetro “Não gerar os itens de serviço nos registros C510, C590, C610 e C690” da tela dos Dados Iniciais do Sped Fiscal estiver marcado, os itens de serviço da SAFX09 serão desconsiderados;

\- Não considerar as notas de mapa resumo de Utilities \(Ind\_Origem\_Info <> '1' \)

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo 23 \- VLR\_TOT\_NOTA da SAFX07\);

\- Valor ICMS Substituição Tributária \(campo 48 \- VLR\_SUBST\_ICMS da SAFX07\);

Importante: o valor de ST deve ser considerado apenas quando o campo “82\-Apropria” da SAFX07  for =  “S”  \(IND\_CRED\_ICMSS\)\.

Para os itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX08;

\- Valor Contábil do Item \(campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\);

\- Valor ICMS Substituição Tributária \(campo 52 \- VLR\_SUBST\_ICMS da SAFX08\);

Importante: o valor de ST deve ser considerado apenas quando o campo “78\-Apropria” da SAFX08  for =  “S”  \(IND\_CRED\_ICMSS\)\.

Para os itens de serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX09;

\- Valor Total do Serviço \(campo 15 \- VLR\_TOT da SAFX09\)\.

\- Valor do ICMS\-ST : considerar zero;

Aplicar os Tratamentos de Situação Especial:

1\) __NF Complementar__:

A nota fiscal Complementar é identificada pelo campo IND\_SITUACAO\_ESP da SAFX07= ‘5’\.

O tratamento dessa nota é determinado pelo parâmetro 48 \(“Tratamento das NFs de Complemento de ICMS”\)  da parametrização por UF do módulo ICMS\.

Se parâmetro 48 estiver marcado, então:

     ZERAR o Valor do ICMS\-ST;

Senão

     Recuperar o valor do ICMS\-ST que está na nota\.

__Observações__:

Observação sobre as notas extemporâneas:

As notas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no C590 do Sped Fiscal, conforme *documento “Notas\_Especiais\_C500\_ Entrada\.doc”\.  *

__Nota técnica:__

__*Ver C\_EFD30 da Efd\_Dic\_Dados*__

## <a id="_2.3_–_Recuperação"></a><a id="_Toc139647336"></a>2\.3 – Notas Fiscais de Saída Energia Elétrica Modelos 06, 66 \(C590, C690, C790\)

No Sped Fiscal existem três sub\-blocos que demonstram as notas de saída de energia elétrica:

- Sub\-bloco C500 \(movimento nota a nota\)
- Sub\-bloco C600 \(movimento consolidado\)
- Sub\-bloco C700 \(Convênio 115\)  

O perfil __A__ contém os sub\-blocos do C500 e C700 e o perfil __B__ o sub\-bloco do C600\.

Segue uma breve explicação extraída da matriz de regras do bloco C do Sped Fical:   

__                Entendimento dos sub\-blocos C500 x C600 x C700 x 1500__

Sub\-bloco C500 \(movimento nota a nota\):   \(EE, Gás e Água\)

- Para as Empresas *obrigadas* ao Convênio ICMS 115 \(EE, Gás ou Água\), gerar apenas as notas emitidas em __*várias vias*__\. São as notas da X42/X43 com o campo “61\-Indicador de NF via única” = “N”;
- Para as Empresas *não obrigadas* ao Convênio ICMS 115, gerar todas as notas;

Sub\-bloco C600 \(movimento consolidado\):   \(EE, Gás e Água\)

- Somente para Empresas *não obrigadas* ao Convênio ICMS 115;
- Gerar todas as notas consolidadas por modelo, município, série, classe de consumo e data de emissão;

Sub\-bloco C700 \(movimento consolidado\):   \(EE e Gás\)

- Somente para Empresas *obrigadas* ao Convênio ICMS 115;
- Gerar os valores totalizados dos arquivos do Convênio ICMS 115;
- Somente EE \(modelo ‘06’\) e Gás \(modelo 28/01\); 

Sub\-bloco 1500 \(nota a nota\):   \(EE\)

- Somente EE \(modelo ‘06’\); 
- Gerar somente as operações interestaduais;

__*Obs importante \(30/09/2008\)*__*: até o AC30/2008, o Sped não reconhecia as empresas de Gás como obrigadas ao Convênio ICMS 115, e por isso o código “28” não constava no registro C700\. Mas em call realizado em 29/09/08, o Tutomo afirmou que o próximo AC já trará esta alteração, e o código “28” já constará no registro C700\. Por isso, nós já estamos considerando esta alteração nas nossas regras de geração\.*

__Outra interpretação das regras considerando primeiro o tipo de Empresa__:

Empresas *não* enquadradas no Convênio ICMS 115: 

Se perfil = A  deve gerar todas as operações de saída, nota a nota no sub\-bloco C500;

Se perfil = B  deve gerar todas as operações de saída, consolidadas no sub\-bloco C600;

                           \(consolidação por modelo e município dos terminais faturados\)

Empresas enquadradas no Convênio ICMS 115:

Gerar as notas emitidas em várias vias no sub\-bloco C500;

Gerar o movimento totalizado dos arquivos do Convênio 115 no sub\-bloco C700;

Gerar as operações interestaduais no sub\-bloco 1500 do Bloco 1 \(somente para EE\);

__Observações importantes:__

Diferenças entre o C500 x C600:

\-C500 é movimento nota a nota, enquanto o C600 é consolidado p/ modelo e munic;

\-C500 é para empresas do perfil A, enquanto o C600 é para o perfil B;

O sub\-bloco C600 é para ser utilizado apenas pelas empresas enquadradas ao perfil B do Sped Fiscal;

Devido a todas estas regras, é importante que as empresas de EE, Gás e Água saibam parametrizar corretamente o perfil de geração destes registros;

Como a VAF deve refletir o resultado do Sped Fiscal, abaixo vamos especificar as regras de recuperação de cada um dos registros C590, C690, C790, onde são demonstradas as notas de Saída Energia Elétrica Modelos 06, 66\.

### <a id="_2.3.1_Recuperação_das"></a><a id="_Toc139647337"></a>2\.3\.1 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06, 66 \(C590\)

O objetivo desta geração é recuperar toda movimentação de saída modelos 06, 66, com os mesmos critérios da geração do registro C590 do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C590\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx e Notas\_Especiais\_C500\_Saidas\.doc\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação A\.

__Origem dos dados__: 

\- SAFX42 / SAFX43  – Tabelas dos Documentos Fiscais Utilities;

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data Fiscal \(campo 03 da SAFX42\) enquadrada no período de geração

\- Código do Modelo = 06, 66

\- Classificação do Documento Fiscal = '1' \- Mercadoria, '2' –Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Somente notas *não canceladas*;

\- Não considerar Itens Informativos \(IND\_TP\_REGISTRO da SAFX43 <> 1\)\)

\-  Se o parâmetro “Não gerar os itens de serviço nos registros C510, C590, C610 e C690” da tela dos Dados Iniciais do Sped Fiscal estiver marcado, os itens de serviço serão desconsiderados \(itens da SAFX43 com COD\_CLASS\_DOC\_FIS = 2 – Serviços\);

\- Estabelecimento do Perfil __A__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

\- Se Empresa enquadrada ao Convênio ICMS 115

                    Gerar apenas as notas emitidas em várias vias   \(IND\_CONVENIO\_115 <> 'S'\)   

             Senão 

                    Gerar todas as notas;

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o campo “Estabelecimento obrigado à geração do arquivo do Convênio ICMS 115/03” na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

__Campos a serem recuperados: __

\- Modelo da SAFX42

\- CFOP da SAFX43;

\- Valor do Serviço \(campo 19 \- VLR\_SERVICO da SAFX43\);

\- Valor do Desconto \(campo 18 \- VLR\_DESCONTO da SAFX43\);

\- Valor Outras Despesas \(campo 46 \- VLR\_OUTRAS\_DESP da SAFX43\);

\- Valor Substituição Tributária \(campo 39 – VLR\_SUBST\_TRIB da SAFX43\);

__Valor Contábil = Valor do Serviço \- Valor do Desconto \+ Valor Outras Despesas__

__ __

__Observações__:

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no C590 do Sped Fiscal, conforme *documento “Notas\_Especiais\_C500\_Saída\.doc”\.  *

__Nota técnica:__

__*Ver C\_EFD30\_90\_Saida da Efd\_Dic\_Dados\_Telecom*__

### <a id="_‘2.3.2_Recuperação_das"></a><a id="_Toc139647338"></a>‘2\.3\.2 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06 \(C690\)

O objetivo desta geração é recuperar toda movimentação de saída modelo 06, com os mesmos critérios da geração do registro C690 do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C690\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx e Notas\_Especiais\_C500\_Saidas\.doc\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação __B__\.

__Origem dos dados__: 

\- SAFX42 / SAFX43  – Tabelas dos Documentos Fiscais Utilities;

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                  

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data Fiscal \(campo 03 da SAFX42\) enquadrada no período de geração

\- Código do Modelo = 06

\- Somente notas *não canceladas*;

\- Não considerar Itens Informativos \(IND\_TP\_REGISTRO da SAFX43 <> 1\)\);

\-  Se o parâmetro “Não gerar os itens de serviço nos registros C510, C590, C610 e C690” da tela dos Dados Iniciais do Sped Fiscal estiver marcado, os itens de serviço serão desconsiderados \(itens da SAFX43 com COD\_CLASS\_DOC\_FIS = 2 – Serviços\);

\- Estabelecimento do Perfil __B__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

__Campos a serem recuperados: __

\- Modelo da SAFX42

\- CFOP da SAFX43;

\- Valor do Serviço \(campo 19 \- VLR\_SERVICO da SAFX43\);

\- Valor do Desconto \(campo 18 \- VLR\_DESCONTO da SAFX43\);

\- Valor Outras Despesas \(campo 46 \- VLR\_OUTRAS\_DESP da SAFX43\);

\- Valor Substituição Tributária \(campo 39 – VLR\_SUBST\_TRIB da SAFX43\);

__Valor Contábil = Valor do Serviço \- Valor do Desconto \+ Valor Outras Despesas__

__Observações__:

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no C590 do Sped Fiscal, conforme *documento “Notas\_Especiais\_C500\_Saída\.doc”\.  *

__Nota técnica: __

__*Ver C\_EFD31 da da Efd\_Dic\_Dados\_Telecom*__

### <a id="_2.3.3_Recuperação_das"></a><a id="_Toc139647339"></a>2\.3\.3 Recuperação das Notas Fiscais de Saída Energia Elétrica Modelos 06 \(C790\)

O objetivo desta geração é recuperar toda movimentação de saída modelo 06, com os mesmos critérios da geração do registro C790 do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C790\.

Nos registros do sub\-bloco “700” \(700, 790 e 791\) do SPED FISCAL serão demonstrados os dados das notas fiscais de saída, emitidas em via única, que compõe o arquivo do Convênio 115, para Empresas que são obrigadas a atender ao Convênio 115/03\.  

Esses registros são gerados a partir da tabelas que armazenam os dados da geração do Convênio 115 \(ICT\_MM\_CONV115 e  ICT\_MM\_CONV115\_UF\_CFO\)\.  Desta forma, será necessário que todos os procedimentos de geração do Convênio 115 sejam executados antes de gerar o Sped Fiscal e a VAF\-MG\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação A\.

__Origem dos dados__: 

\- ICT\_MM\_CONV115 – Tabela do arquivo Mestre do Convênio 115

\- ICT\_MM\_CONV115\_UF\_CFO – Tabela de Detalhamento por CST, CFOP, Alíquota do Convênio 115

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                  

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Mês/Ano da ICT\_MM\_CONV115 enquadrada no período de geração

\- Código do Modelo da ICT\_MM\_CONV115 = 06

\- Somente considerar Empresa enquadrada no Convênio ICMS 115

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o campo “Estabelecimento obrigado à geração do arquivo do Convênio ICMS 115/03” na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

\- Estabelecimento do Perfil  __A__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

__Campos a serem recuperados: __

\- Modelo da ICT\_MM\_CONV115

\- CFOP da ICT\_MM\_CONV115\_UF\_CFO;

\- Valor do Serviço da ICT\_MM\_CONV115\_UF\_CFO \(VLR\_SERVICO\);

\- Valor Substituição Tributária da ICT\_MM\_CONV115\_UF\_CFO \(VLR\_SUBST\_TRIB\);

__Valor Contábil = Valor do Serviço__

__Observações__:

__Nota técnica:__

__*Ver C\_EFD32 da Efd\_Dic\_Dados\_Telecom*__

## <a id="_2.4_–_Recuperação"></a><a id="_Toc139647340"></a>2\.4 – Recuperação das Notas Fiscais de Entrada de Comunicação Modelos 21, 22 \(D590\)

__Origem dos dados__: \- SAFX07 / SAFX08 / SAFX09 – Tabelas dos Documentos Fiscais;

                                  

O objetivo desta geração é recuperar toda movimentação de entrada modelos 21, 22, com os mesmos critérios da geração do registro __D590__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D590\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx e Notas\_Especiais\_D500\-Entradas\.doc\.

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 21, 22

\- Classificação do Documento Fiscal = '1' \- Mercadoria,'3' – Mercadoria e Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas \(MOVTO\_E\_S <> ‘9’ da SAFX07\)

\- Somente notas *não canceladas*;

\- Considerar notas fiscais com e sem itens de mercadoria;

\- Não considerar as notas de mapa resumo de Utilities \(Ind\_Origem\_Info <> '1' \)

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo VLR\_TOT\_NOTA da SAFX07\)\.

Para os itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX08;

\- Valor Contábil do Item \(campo VLR\_CONTAB\_ITEM da SAFX08\)\.

Não recuperar itens de serviços\.

__Observações__:

Observação sobre as notas extemporâneas:

As notas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no D590 do Sped Fiscal, conforme *documento “Notas\_Especiais\_D500\_Entrada\.doc”\.  Não há necessidade de tratar notas complementares uma vez que, segundo o documento “Notas\_Especiais\_D500\_ Entrada\.doc”, o valor contábil permanece sendo gerado no D590\. *

__Nota técnica:__

__*Ver C\_EFD90 da Efd\_Dic\_Dados*__

## <a id="_2.5_–_Recuperação"></a><a id="_Toc139647341"></a>2\.5 – Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D590, D690, D696\)

No Sped Fiscal existem três sub\-blocos que demonstram as notas de saída de Comunicação/Telecomunicação:

- Sub\-bloco D500 \(movimento nota a nota\)
- Sub\-bloco D600 \(movimento consolidado\)
- Sub\-bloco D695 \(Convênio 115\)  

O perfil __A__ contém os sub\-blocos do D500 e D695 e o perfil __B__ o sub\-bloco do D600\.

Segue uma breve explicação extraída da matriz de regras do bloco D do Sped Fical:   

__                  Entendimento dos sub\-blocos D500 x D600 x D695__

Sub\-bloco D500 \(movimento nota a nota\):

- Para as Empresas *obrigadas* ao Convênio ICMS 115, gerar apenas as notas emitidas em __*várias vias*__\. São as notas da X42/X43 com o campo “61\-Indicador de NF via única” = “N”;
- Para as Empresas *não obrigadas* ao Convênio ICMS 115, gerar todas as notas;

Sub\-bloco D600 \(movimento consolidado\):

- Somente para Empresas *não obrigadas* ao Convênio ICMS 115;
- Gerar todas as notas; 

Sub\-bloco D695 \(movimento consolidado\):

- Somente para Empresas *obrigadas* ao Convênio ICMS 115;
- Gerar os valores totalizados dos arquivos do Convênio ICMS 115; 

__Outra interpretação das regras considerando primeiro o tipo de Empresa__:

Empresas *não* enquadradas no Convênio ICMS 115: 

Se perfil = A  deve gerar todas as operações de saída, nota a nota no sub\-bloco D500;

Se perfil = B  deve gerar todas as operações de saída, consolidadas no sub\-bloco D600;

                           \(consolidação por modelo e município dos terminais faturados\)

Empresas enquadradas no Convênio ICMS 115:

Gerar as notas emitidas em várias vias no sub\-bloco D500;

Gerar o movimento totalizado dos arquivos do Convênio 115 no sub\-bloco D695;

Obs 07/04/2009 \(OS2388\-E8\) Este conceito original foi contrariado pela Portaria SC 03/09\. De acordo com a Portaria, SC irá exigir todas as operações de Utilities nos registros C500 e D500 \(e “filhos”\)\. Os demais registros não serão utilizados, mesmo no caso das empresas obrigadas ao Convênio 115\. Neste caso, estas empresas não deverão marcar o parâmetro “Estabelecimento obrigado à entrega do arquivo do Convênio 115/03” \(ver help deste campo na tela de cadastro dos Estabelecimentos\)\. Conforme testes realizados em Abr/2009, a geração da EFD só não atendeu 100% a Portaria por um pequeno detalhe: os registros D510 e D530 não são habilitados no perfil B, já que conforme a regra original da EFD eles nunca seriam gerados neste perfil\. Os ajustes para solução deste problema foram feitos na OS2388\-E8\.     

Diferenças entre o D500 x D600:

D500 é movimento nota a nota, enquanto o D600 é consolidado p/ modelo e munic;

D500 é para empresas do perfil A, enquanto o D600 é para o perfil B;

O sub\-bloco D600 é para ser utilizado apenas pelas empresas enquadradas ao perfil B do Sped Fiscal;

Como a VAF deve refletir o resultado do Sped Fiscal, abaixo vamos especificar as regras de recuperação de cada um dos registros D500 x D600 x D695, onde são demonstradas as notas de Saída dos Modelos 21, 22\.

### <a id="_2.5.1_Recuperação_das"></a><a id="_Toc139647342"></a>2\.5\.1 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D590\)

O objetivo desta geração é recuperar toda movimentação de saída modelos 21, 22, com os mesmos critérios da geração do registro __D590__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D590\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx e Notas\_Especiais\_D500\_Saidas\.doc\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação A\.

__Origem dos dados__: 

\- SAFX42 / SAFX43  – Tabelas dos Documentos Fiscais Utilities;

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                  

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data Fiscal \(campo 03 da SAFX42\) enquadrada no período de geração

\- Código do Modelo = 21, 22

\- Classificação do Documento Fiscal = '1' \- Mercadoria, '2' –Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Somente notas *não canceladas*;

\- Não considerar Itens Informativos \(IND\_TP\_REGISTRO da SAFX43 <> 1\)\)

\- Estabelecimento do Perfil  __A__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

\- Se Empresa enquadrada ao Convênio ICMS 115

                    Gerar apenas as notas emitidas em várias vias  \(IND\_CONVENIO\_115 <> 'S'\)   

             Senão 

                    Gerar todas as notas;

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o campo “Estabelecimento obrigado à geração do arquivo do Convênio ICMS 115/03” na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

__Campos a serem recuperados: __

\- Modelo da SAFX42

\- CFOP da SAFX43;

\- Valor do Serviço \(campo 19 \- VLR\_SERVICO da SAFX43\);

\- Valor do Desconto \(campo 18 \- VLR\_DESCONTO da SAFX43\);

\- Valor Outras Despesas \(campo 46 \- VLR\_OUTRAS\_DESP da SAFX43\);

__Valor Contábil = Valor do Serviço \- Valor do Desconto \+ Valor Outras Despesas__

__ __

__Observações__:

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no D590 do Sped Fiscal, conforme *documento “Notas\_Especiais\_D500\_Saída\.doc”\.  *

__Nota técnica:__

__*Ver C\_EFD30\_90\_Saida da Efd\_Dic\_Dados\_Telecom*__

### <a id="_‘2.5.2_Recuperação_das"></a><a id="_2.5.2_Recuperação_das"></a><a id="_Toc139647343"></a>2\.5\.2 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D690\)

O objetivo desta geração é recuperar toda movimentação de saída modelo 21, 22, com os mesmos critérios da geração do registro __D690__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D690\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx e Notas\_Especiais\_D500\_Saidas\.doc\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação __B__\.

__Origem dos dados__: 

\- SAFX42 / SAFX43  – Tabelas dos Documentos Fiscais Utilities;

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                  

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data Fiscal \(campo 03 da SAFX42\) enquadrada no período de geração

\- Código do Modelo = 21, 22

\- Somente notas *não canceladas*;

\- Não considerar Itens Informativos \(IND\_TP\_REGISTRO da SAFX43 <> 1\)\)

\- Somente considerar Empresa __não__ enquadrada no Convênio ICMS 115

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o campo “Estabelecimento obrigado à geração do arquivo do Convênio ICMS 115/03” na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

\- Estabelecimento do Perfil __ B__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

__Campos a serem recuperados: __

\- Modelo da SAFX42

\- CFOP da SAFX43;

\- Valor do Serviço \(campo 19 \- VLR\_SERVICO da SAFX43\);

\- Valor do Desconto \(campo 18 \- VLR\_DESCONTO da SAFX43\);

\- Valor Outras Despesas \(campo 46 \- VLR\_OUTRAS\_DESP da SAFX43\);

__Valor Contábil = Valor do Serviço \- Valor do Desconto \+ Valor Outras Despesas__

__Observações__:

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas\), foram definidos com base no tratamento dados no D690 do Sped Fiscal, conforme *documento “Notas\_Especiais\_D500\_Saída\.doc”\.  *

__Nota técnica: __

__*Ver C\_EFD91 da da Efd\_Dic\_Dados\_Telecom*__

### <a id="_2.5.3_Recuperação_das"></a><a id="_Toc139647344"></a>2\.5\.3 Recuperação das Notas Fiscais de Saída Comunicação Modelos 21, 22 \(D696\)

O objetivo desta geração é recuperar toda movimentação de saída modelo 21, 22, com os mesmos critérios da geração do registro __D696__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D696\.

Nos registros do sub\-bloco “D695” \(D695, D696 e D697\) do SPED FISCAL serão demonstrados os dados das notas fiscais de saída, emitidas em via única, que compõe o arquivo do Convênio 115, para Empresas que são obrigadas a atender ao Convênio 115/03\.  

Esses registros são gerados a partir da tabelas que armazenam os dados da geração do Convênio 115 \(ICT\_MM\_CONV115 e  ICT\_MM\_CONV115\_UF\_CFO\)\.  Desta forma, será necessário que todos os procedimentos de geração do Convênio 115 sejam executados antes de gerar o Sped Fiscal e a VAF\-MG\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx\.

Registro gerado no Sped Fiscal para o Perfil de Apresentação __A__\.

__Origem dos dados__: 

\- ICT\_MM\_CONV115 – Tabela do arquivo Mestre do Convênio 115

\- ICT\_MM\_CONV115\_UF\_CFO – Tabela de Detalhamento por CST, CFOP, Alíquota do Convênio 115

\- Tabela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)                                 

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Mês/Ano da ICT\_MM\_CONV115 enquadrada no período de geração

\- Código do Modelo da ICT\_MM\_CONV115 = 21, 22

\- Somente considerar Empresa enquadrada ao Convênio ICMS 115

Para verificar se a Empresa é obrigada ou não a geração do Convênio 115, verificar o campo “Estabelecimento obrigado à geração do arquivo do Convênio ICMS 115/03” na tela de cadastro do Estabelecimento \(módulo Parâmetros\)\. 

\- Estabelecimento do Perfil  __A__ do Sped Fiscal\. Para verificar o Perfil, verificar campo “Perfil de Apresentação da EDF” na tela de Manutenção dos Dados Iniciais – VAF \(menu Preliminares >> Manutenção de Dados Iniciais\)

__Campos a serem recuperados: __

\- Modelo da ICT\_MM\_CONV115

\- CFOP da ICT\_MM\_CONV115\_UF\_CFO;

\- Valor do Serviço da ICT\_MM\_CONV115\_UF\_CFO \(VLR\_SERVICO\);

__Valor Contábil = Valor do Serviço__

__Observações__:

__Nota técnica:__

__*Ver C\_EFD92 da Efd\_Dic\_Dados\_Telecom*__

## <a id="_2.6_–_Recuperação"></a><a id="_Toc139647345"></a>2\.6 – Recuperação das Notas Fiscais de Entrada e Saída de Transporte Modelo 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 \(D190\)

O objetivo desta geração é recuperar toda movimentação de entrada e saída de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63, com os mesmos critérios da geração do registro __D190__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D190\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx\.

__Origem dos dados__: 

\- SAFX07 / SAFX08 / SAFX09 – Tabelas dos Documentos Fiscais;

                                                                    

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63, 67

\- Classificação do Documento Fiscal = '1' \- Mercadoria, ’2’ – Serviço, '3' – Mercadoria e Serviço, ‘4’ – Conhecimento de Frete \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas e Saídas \(MOVTO\_E\_S da SAFX07\)

\- Somente notas *não canceladas*;

\- Considerar notas fiscais com e sem itens de mercadoria e serviço;

\- Não considerar as notas de mapa resumo de Utilities \(Ind\_Origem\_Info <> '1' \)

\- Não considerar as notas fiscais extemporâneas de saída \(MOVTO\_E\_S = ‘9’ e DAT\_ESCR\_EXTEMP > 0\);

\- Não considerar NF Eletrônica denegada/inutilizada \(campo IND\_NFE\_DENEG\_INUT da SAFX07 não preenchido\)\.

__Critérios Específicos:__

__Notas de Entrada de Terceiros __ Selecionar na tabela SAFX07 as prestações de serviços de transportes/notas fiscais emitidas por terceiros:

      Movimento Entrada/Saída = “1”,

       Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 ou 67\.

              Classificação do Documento Fiscal = “1”,

      Movimento Entrada/Saída = “1”, NORM\_DEV = 1

       Se Modelo de Documento = 07, 63 ou 67 

              Classificação do Documento Fiscal = “2”

__Notas de Entrada  Emitidas pelo próprio Estabelecimento__  __S__elecionar na tabela SAFX07 as prestações de serviços de transportes e/ou notas fiscais emitidas pelo estabelecimento com as seguintes condições:

      Movimento Entrada/Saída = “2”; “3”; “4” ou “5”;

       Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 ou 67;

               Classificação do Documento Fiscal = “1”   se for nota fiscal \(modelo = 07\) ou modelo 63;

               Classificação do Documento Fiscal = “1” ou “4”  se for conhecimento \(modelo = 08, 8B, 09, 10, 

                                                                                               11,  26, 27, 57 ou 67\)\.

__Notas de Saída__  Se__l__ecionar na tabela SAFX07 as prestações de serviços de transportes e/ou notas__ __fiscais emitidas com as seguintes condições:

       Movimento Entrada/Saída = “9”;

       Se Modelo de Documento = 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67;

           Classificação do Docto Fiscal = “1”   se for nota fiscal \(modelo = 07\) ou modelo 63 ou

                                                                        Conhecimento de Modelo = 08  ou modelo = 57;

           Classificação do Documento Fiscal = “4”  se for conhecimento \(modelo= 08, 8B, 09, 10, 11,

                                                                                26, 27, 57 ou 67\)\.

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo VLR\_TOT\_NOTA da SAFX07\)\.

Para os itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX08;

\- Valor Contábil do Item \(campo VLR\_CONTAB\_ITEM da SAFX08\)\.

Para os itens de serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX09;

\- Valor Total do Serviço \(campo VLR\_TOT da SAFX09\)\.

Aplicar os Tratamentos de Situação Especial:

1\) __NF Simples Faturamento__:

A nota fiscal de Simples Faturamento é identificada pelos campos:

\- Nvl\(CAP\.IND\_SITUACAO\_ESP,' '\) = 'D' e

\- CFO\.COD\_CFO IN \('1922', '2922','1117','2117','5922', '6922','5116', '6116','1923', '2923', '5923', '6923'\)

Caso a nota seja de Simples Faturamento, verificar o quadro “Situação Especial 08 – Faturamento Simples” presente na tela de Dados Iniciais do Sped Fiscal, onde estão contidos os seguintes flags: ICMS, ICMS\-ST, PIS/COFINS\-ST, PIS/COFINS, IPI\.

Se __todos__ os flags estiverem desmarcados, então:

     ZERAR todos os valores indicados acima \(Valor Total\)

Senão

    Recuperar o Valor total da nota;

__Observações__:

Observação sobre as notas extemporâneas:

As notas extemporâneas serão tratadas normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, a nota extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

*Exceção para notas fiscais extemporâneas de Saída: Não apresentar os valores dos documentos extemporâneos de saída, tendo em vista que não serão considerados para os livros P2, P2A e P9\.*

Observação sobre tratamento de Notas com Situação Especial

Os tratamentos para situações especiais \(notas canceladas, de simples faturamento, foram definidos com base no tratamento para o D190 do Sped Fiscal, conforme RND100 documento “Sped\_Fiscal\_Regras\_Bloco\_D\.docx”\. Não há necessidade* de tratar notas complementares uma vez que, independente do parâmetro 48 o valor contábil é apresentado no campo VLR\_OPER\.*

__Nota técnica:__

__*Ver C\_EFD40 da Efd\_Dic\_Dados*__

## <a id="_2.7_–_Recuperação"></a><a id="_Toc139647346"></a>2\.7 – Recuperação dos Cupons Fiscais Modelos 02, 2D, 60 \(C490\)

O objetivo desta geração é recuperar toda movimentação de cupom de modelos 02, 2D e 60, com os mesmos critérios da geração do registro __C490__ do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C490\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx\.

__Origem dos dados__: 

\- SAFX991 – Tabela de Capa da Redução Z;

\- SAFX993 – Tabela de Capa do Cupom Fiscal;

\- SAFX994 – Tabela de Item do Cupom Fiscal;

\- SAFX2087 \-Tabela de Equipamento ECF

                                                                    

__Critérios da recuperação dos Cupons Fiscais: __

\- Empresa da Redução Z \(SAFX991\) – código da empresa do login;

\- Estabelecimento da Redução Z \(SAFX991\) – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data do movimento da Redução Z \(DATA\_FISCAL SAFX991\) enquadrada no período de geração;

\- Com os dados do Equipamento ECF da Redução Z \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO e COD\_CAIXA\_ECF da SAFX991\), acessar a Tabela de Equipamento ECF  \(SAFX2087\) e recuperar o Código Modelo NF \(COD\_MODELO\_COTEPE\) e COO Final para Reinicio \(NUM\_COO\_FIM\_REI\);

\- Código Modelo NF do Equipamento ECF \(COD\_MODELO\_COTEPE da SAFX2087\) = 02, 2D, 60;

\- Com os dados do COO Inicial e COO Final da Redução Z \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO, COD\_CAIXA\_ECF, DATA\_FISCAL, NUM\_COO\_INI, NUM\_COO\_FIM da SAFX991\) acessar a Tabela de Capa do Cupom Fiscal \(SAFX993\) e recuperar os cupons emitidos no dia\. Fazer a seguinte associação de campos:

- COD\_EMPRESA SAFX991 = COD\_EMPRESA SAFX993
- COD\_ESTAB SAFX991= COD\_ESTAB SAFX993
- COD\_MODELO SAFX991= COD\_MODELO SAFX993
- COD\_CAIXA\_ECF SAFX991= COD\_CAIXA\_ECF SAFX993
- DATA\_FISCAL SAFX991 = DATA\_EMISSAO SAFX993
- NUM\_COO SAFX993 compreendido entre o NUM\_COO\_INI, NUM\_COO\_FIM da SAFX991

Fazer tratamento para quando o contador do cupom é reiniciado no meio do dia,caso em que o NUM\_COO\_INI fica maior que o NUM\_COO\_FIM\. Nesse caso, recupera os cupons compreendidos em duas faixas:

- NUM\_COO SAFX993 compreendido entre o NUM\_COO\_INI da SAFX991 e NUM\_COO\_FIM\_REI da SAFX2087;

e

- NUM\_COO SAFX993 compreendido entre 000000 e NUM\_COO\_FIM da SAFX991;

\- Data Emissão do Cupom \(DATA\_EMISSAO SAFX993\) enquadrada no período de geração

\- Situação do Cupom = 1 – Documento Normal *\(*IND\_SITUACAO\_CUPOM da SAFX993*\)*;

\- Tipo de Documento = 1 – Cupom Fiscal \(IND\_TIPO\_CUPOM da SAFX993\);

\- Com os dados da Capa do Cupom \(campos COD\_EMPRESA, COD\_ESTABELECIMETO, COD\_MODELO, COD\_CAIXA\_ECF, DATA\_EMISSAO, NUM\_COO da SAFX993\) acessar a Tabela de Item do Cupom Fiscal \(SAFX994\) e recuperar os itens dos cupons emitidos no dia\.

\- Situação do item no Cupom = 1 – Item Normal  ou 3 – Item Cancelado Parcialmente \(IND\_SITUACAO\_ITEM da SAFX994\);

\- Não considerar as Reduções Z com Venda Bruta Zerada, ou seja, registro da SAFX991 com os três critérios atendidos:

- VLR\_VENDA\_BRUTA = 0
- VLR\_VENDA\_LIQ = 0 e 
- NUM\_COO\_INI = NUM\_COO\_FIM\.

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Código Modelo NF do Equipamento ECF \(COD\_MODELO\_COTEPE da SAFX2087\);

\- CFOP da SAFX994;

\- Valor total líquido \(campo VLR\_LIQ\_ITEM da SAFX994\)\.

__Nota técnica:__

__*Ver C\_EFD21 da Efd\_Dic\_Dados\_ECF*__

## <a id="_2.8_–_Recuperação"></a><a id="_Toc139647347"></a>2\.8 – Recuperação dos Cupons Fiscais Modelos 13, 14, 15, 16 e 2E \(D390\)

O objetivo desta geração é recuperar toda movimentação de cupom de modelos 13,14,15,16 e 2E com os mesmos critérios da geração do registro D390 do SPED FISCAL\.  Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro D390\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx\.

Mesma regra de recuperação especificada no tópico [2\.7](#_2.7_–_Recuperação) \(Recuperação dos Cupons Fiscais Modelos 02, 2D, 60 \(C490\)\), só que considerando os modelos 13,14,15,16 e 2E ao ínvés de 02, 2D, 60\.

__Nota técnica:__

__*Ver C\_EFD81 da Efd\_Dic\_Dados\_ECF*__

## <a id="_2.9_–_Recuperação"></a><a id="_Toc139647348"></a>2\.9 – Recuperação dos Bilhetes Modelos 13, 14, 15, 16 \(D300\)

O objetivo desta geração é recuperar toda movimentação de saída que são bilhetes de modelos 13, 14, 15 e 16, com os mesmos critérios da geração dos registros __D300__ do SPED FISCAL\.  

Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __D300__\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx\.

__Origem dos dados__: 

\- SAFX07 – Tabelas dos Documentos Fiscais;

                                                                    

__Critérios da recuperação dos Bilhetes: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 13, 14, 15, 16

\- Classificação do Documento Fiscal = '1' \- Mercadoria,  '3' – Mercadoria e Serviço, \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Saídas \(MOVTO\_E\_S da SAFX07 = ‘9’\)

\- Somente notas *não canceladas*;

\- Considerar apenas a capa do documento fiscal;

__Campos a serem recuperados: __

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo 23 \- VLR\_TOT\_NOTA da SAFX07\)\.

__Observações__:

Observação sobre as notas extemporâneas:

Os bilhetes com data extemporânea serão tratados normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, o documento com data extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

__Nota técnica:__

__*Ver C\_EFD51 da Efd\_Dic\_Dados\_bilh*__

## <a id="_2.10_–_Recuperação"></a><a id="_Toc139647349"></a>2\.10 – Recuperação dos Bilhetes de Modelos 13, 14, 15 E 16 \(D410\)

Não tem tratamento de Inscrição Estadual Unica\.

O objetivo desta geração é recuperar toda movimentação de saída que são bilhetes de modelos 13, 14, 15 e 16, associados ao Resumo de Movimento Diário \(modelo 18\) com os mesmos critérios da geração dos registros __D400__ e __D410 __do SPED FISCAL\.  O D410 demonstra os bilhetes \(modelos 13, 14, 15 e 16\) e o D400 demonstra o Resumo de Movimento Diário \(modelo 18\)\. O D410 é filho do D400\.

Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __D410__\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_D\.docx\.

__Origem dos dados__: 

\- SAFX07 – Tabelas dos Documentos Fiscais;

                                                                    

__Critérios da recuperação dos Resumo de Movimento Diário \- RMD \(modelo 18\): __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) __Não__ tem tratamento de Inscrição Estadual Unica\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 18

\- Classificação do Documento Fiscal = '1' \- Mercadoria,  '3' – Mercadoria e Serviço, \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Saídas \(MOVTO\_E\_S da SAFX07 = ‘9’\)

\- Somente notas *não canceladas*;

\- Considerar apenas a capa do documento fiscal;

__Critérios da recuperação dos Bilhetes \(modelo 13, 14, 15, 16\): __

Recuperação dos Bilhetes que referenciam aos Resumos de Movimentos Diários \(RMD\) recuperados com os critérios acima\.

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) __Não__ tem tratamento de Inscrição Estadual Unica\.

\- Código do Modelo = 13, 14, 15, 16

\- Classificação do Documento Fiscal = '9' \- Outros Documentos não escriturados \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Saídas \(MOVTO\_E\_S da SAFX07 = ‘9’\)

\- Somente notas *não canceladas*;

\- Considerar apenas a capa do documento fiscal;

\- Número do Docto\. Fiscal de Referência do Bilhete \(NUM\_DOCFIS\_REF\) =  Número do Documento Fiscal do RMD \(NUM\_DOCFIS\)

\- Série do Docto\. Fiscal de Referência do Bilhete \(SERIE\_DOCFIS\_REF\) =  Série do Documento Fiscal do RMD \(SERIE\_DOCFIS\)

\- Subsérie do Docto\. Fiscal de Referência do Bilhete \(S\_SER\_DOCFIS\_REF\) =  Subsérie do Documento Fiscal do RMD \(SUB\_SERIE\_DOCFIS\)

\- Data da Declaração de Importação/Data Doc\. Original nas Oper\. de Devolução do Bilhete \(DAT\_DI\) =   Data Fiscal do RMD   \(DATA\_FISCAL\)

__Campos a serem recuperados: __

\- Modelo da SAFX07 do Bilhete;

\- CFOP da SAFX07 do Bilhete;

\- Valor Total do Documento Fiscal do Bilhete\(campo 23 \- VLR\_TOT\_NOTA da SAFX07\)\.

__Observações__:

Observação sobre as notas extemporâneas:

O RMD com data extemporânea será tratado normalmente, exatamente da mesma forma como é feito na versão atual do Mastersaf, ou seja, o documento com data extemporânea é lançada normalmente nos livros P1/P2/P9, sem nenhum tipo de tratamento especial\.

A lógica para recuperação destas notas deve ser a mesma que é aplicada hoje nos livros:

*Se \(data\_fiscal entre data inicial e data final e data\_extemporânea não*

*       preenchida\) *

*ou*

*     Data\_extemporânea entre data inicial e data final*

__Nota técnica:__

__*Ver C\_EFD52 da Efd\_Dic\_Dados\_bilh*__

## <a id="_2.11_–_Recuperação"></a><a id="_Toc139647350"></a>2\.11 – Recuperação dos Ajuste/Outros Valores do Lançamento Fiscal das Notas de Entrada e Saída de Modelos 01, 1B, 04, 55, 65 \(C197\)

O objetivo desta geração é recuperar as informações de ajustes/outros valores do lançamento fiscal da movimentação de entrada e saída de modelos 01, 1B, 04, 55, 65, com os mesmos critérios da geração do registro C197 do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __C197__\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx e Notas\_Especiais\_C100\_v8\.doc\.

__Origem dos dados__: 

\- SAFX07 – Tabela de Capa do Documento Fiscal;

\- SAFX112 – Tabela de Observações do Documentos Fiscal;

\- SAFX113 – Tabela de Ajuste/Outros Valores do Lançamento Fiscal do Documento Fiscal;

__Critérios da recuperação das Notas Fiscais: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 01, 1B, 04, 55, 65

\- Classificação do Documento Fiscal = '1' \- Mercadoria,'3' – Mercadoria e Serviço \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas e Saídas \(MOVTO\_E\_S da SAFX07\)

\- Somente notas *não canceladas*;

\- Não considerar as notas de mapa resumo de Utilities \(Ind\_Origem\_Info <> '1' \)

\- Para notas com Código Modelo 65, recuperar só notas de saída \(MOVTO\_E\_S = '9'\)

\- Não considerar NF Eletrônica denegada/inutilizada \(campo IND\_NFE\_DENEG\_INUT da SAFX07 não preenchido\)\.

\- Com os campos de identificação da Capa do Documento Fiscal \(SAFX07\) acessar a Tabela de Observações do Documentos Fiscais \(SAFX112\) e recuperar as observações cujo campo Tipo de Observação seja igual a “__L__” \(campo  IND\_ICOMPL\_LANCTO\)\.

\- Com os registros de Observação recuperados da Tabela de Observações do Documentos Fiscais \(SAFX112\), acessar a Tabela de Ajuste/Outros Valores do Lançamento Fiscal do Documento Fiscal \(SAFX113\) e recuperar todos os registros relacionados vinculados à observação\.

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria e serviço, recuperar:

\- Movimento Entrada/Saída \(MOVTO\_E\_S\)

\- Código do Ajuste \(campo 13 \- COD\_AJUSTE\_SPED da SAFX113\);

\- Valor do ICMS \(campo 18 \- VLR\_ICMS da SAFX113\);

__Nota técnica:__

__*Ver C\_EFD05 da Efd\_Dic\_Dados*__

__Observação__:

Durante os testes da VAF\-MG foi diagnosticado que notas de modelo 04 não estão gerando o registro C197 no Sped Fiscal\. 

O matriz “Sped\_Fiscal\_Regras\_Bloco\_C\.doc” indica que esse modelo deveria gerar o C195, por consequência o C197\. 

Sendo assim mantivemos a especificação da VAF considerando o modelo 04, mas decidimos retirar o modelo 04 da implementação, para que não haja divergência com o resultado apresentado no Sped Fiscal\.

## <a id="_2.12_–_Recuperação"></a><a id="_Toc139647351"></a>2\.12 – Recuperação das Informações Adicionais da Apuração – Valores Declaratórios \(E115\)

O objetivo desta geração é recuperar as Informações Adicionais da Apuração – Valores Declaratórios, com os mesmos critérios da geração do registro E115 do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __E115__\.

Esta regra foi escrita com base no documento Sped\_Fiscal\_Regras\_Bloco\_E\.docx\.

__Origem dos dados__: 

\- EFD\_REG\_E115 – Tabela dos Registros E115/1925 \(Valores Declaratórios\);

Essa tabela é carregada no módulo Sped Fiscal por duas funcionalidades: 

- Manutenção do E115 \(menu Geração  Manutenção  Registros E115 \(Valores Declaratórios\)\)
- Pré\-Geração \(menu Pré\-Geração  Registro E115 \(Geral\)\)

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) __Não__ tem Tratamento para Inscrição Estadual Única, pois as informações adicionais são inseridas em nome do estabelecimento centralizador, caso o contribuinte trabalhe com Inscrição Estadual Única\.

\- Campo Período \(data inicial e final\) da Tabela dos Registros E115/1925 \(Valores Declaratórios\): deve se enquadrar no período de geração;

\- Campo “Sub Apuração do Sped Fiscal” da Tabela dos Registros E115/1925 \(Valores Declaratórios\): deve não estar preenchido;

\- Campo “Tipo de Apuração do ICMS utilizada no Mastersaf” do Cadastro do Estabelecimento preenchido com '1', '2', '3' ou '4' \(Módulo Parâmetros – menu Preliminares >> Empresa/Estabelecimento \- campo Ind\_Apur\_Icms da tabela ESTABELECIMENTO\);

__Campos a serem recuperados: __

\- Código da Informação Adicional  \(COD\_INF\_ADIC\)

\- Valor da Informação Adicional  \(VLR\_INF\_ADIC\)

__Nota técnica:__

__*Ver função GravaInfAdic  da package Efd71\_Gera*__

## <a id="_2.13_–_Recuperação"></a><a id="_Toc139647352"></a>2\.13 – Recuperação dos Registros 1400 \(1400\)

O objetivo desta geração é recuperar as Informações do registro 1400 do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __1400__\.

Esta regra foi escrita com base no documento Sped\_Fiscal\_Regras\_atual\.docx\.

Os registros 1400 gerados no Sped Fiscal, são armazenados numa tabela \(EFD\_REG\_1400\) permitir consulta via tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

Sendo assim a geração da DAMEF\-EFD Fiscal irá recuperar os registros desta tabela\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Origem dos dados__: 

\- EFD\_REG\_1400 – Tabela dos Registros 1400;

Essa tabela é carregada no módulo Sped Fiscal por duas funcionalidades: 

- Manutenção do 1400 \(menu Geração >> Manutenção >> Registro 1400\)
- Pré\-Geração \(menu Pré\-Geração  Registro 1400 \- Periodicidade Anual / Específicos por UF\)

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Campo Período \(data inicial e final\) da Tabela dos Registros 1400: deve se enquadrar no período de geração;

__Campos a serem recuperados: __

\- Código e Descrição do Município

\- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\)

\- Valor Total  \(VLR\_TOTAL\)

__Nota técnica:__

__*Ver cursor c\_Efd79 da package Efd\_Dic\_Dados\_Va*__

## <a id="_2.14_–_Recuperação"></a><a id="_Toc139647353"></a>2\.14 – Recuperação dos Registros de Inventário Inicial e Final \(H005\)

\[MFS\-45264\]

O objetivo desta geração é recuperar as informações do Inventário inicial e final, com os mesmos critérios da geração do registro H005 do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro __H005__\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_H\.docx\.

__Origem dos dados: __

\- SAFX52 – Tabela de Inventário por Produto;

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data do Inventário \(DATA\_INVENTARIO\): Data do Inventário Inicial ou Data do Inventário Final informadas na tela de geração

\- Grupo de Contagem \(GRUPO\_CONTAGEM\) = 1, 2, 3 e 5

\- Motivo do Inventário \(IND\_MOT\_INV\) = '01' 

__Campos a serem recuperados: __

\- Indicador do Produto

\- Código do Produto

\- Data do Inventário

\- Valor Total \(VLR\_TOT – campo 14 da SAFX52\)

Esta consulta pode recuperar mais de um registro por data do inventário e produto, pois a chave da tabela X52 contém ainda os campos natureza do estoque e grupo contagem\.

Na geração do Quadro de Totalização do Inventário \(ver tópico [8](#_Quadro_Totalização_do)\), os registros de inventário aqui recuperados serão consolidados por Data do Inventário\.

E na geração do Relatório de Conferência \(ver tópico [9](#_Relatório_de_Conferência)\), os registros de inventário aqui recuperados serão consolidados por Data do Inventário, Indicador e Código do Produto\.

## <a id="_2.15_–_Recuperação"></a><a id="_Toc139647354"></a>2\.15 – Recuperação das Notas Fiscais de Venda a Consumidor Modelo 02 \(C320\)

O objetivo desta geração é recuperar toda movimentação \(Consolidada\) das Notas Fiscais de Venda ao Consumidor de modelo 02, com os mesmos critérios da geração do registro __C320__ do SPED FISCAL\. Todas as regras da VAF\-MG são baseadas nos registros do SPED FISCAL, logo devemos refletir nessa regra os mesmos critérios de geração do registro C320\.

Esta regra foi escrita com base nos documentos Sped\_Fiscal\_Regras\_Bloco\_C\.docx\.

__Origem dos dados__: 

- SAFX07 – Capa das Notas Fiscais
- SAFX08 – Itens das Notas Fiscais Mercadoria e Produtos

__Critérios da recuperação das Notas Fiscais de Venda a Consumidor:__

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração; 

\(\*\) Ver Tratamento para Geração por Inscrição Estadual Única, no tópico [1\.2](#_1.2_-_Tratamento)\.

\- Data da nota:

Notas com data fiscal enquadrada no período de geração

Notas com data extemporânea enquadrada no período de geração

\- Código do Modelo = 02

\- Classificação do Documento Fiscal = '1' \- Mercadoria \(COD\_CLASS\_DOC\_FIS\)

\- Notas de Entradas \(MOVTO\_E\_S =  ‘9’ da SAFX07\)

\- Somente notas *não canceladas*;

\- Considerar notas fiscais com e sem itens de mercadoria e serviço;

__Campos a serem recuperados: __

Para notas fiscais sem itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX07;

\- Valor Total do Documento Fiscal \(campo 23 \- VLR\_TOT\_NOTA da SAFX07\);

Para os itens de mercadoria, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX08;

\- Valor Contábil do Item \(campo 64 \- VLR\_CONTAB\_ITEM da SAFX08\);

\- Valor ICMS Substituição Tributária \(campo 52 \- VLR\_SUBST\_ICMS da SAFX08\);

Importante: o valor de ST deve ser considerado apenas quando o campo “78\-Apropria” da SAFX08  for =  “S”  \(IND\_CRED\_ICMSS\)\.

Para os itens de serviço, recuperar:

\- Modelo da SAFX07;

\- CFOP da SAFX09;

\- Valor Total do Serviço \(campo 15 \- VLR\_TOT da SAFX09\)\.

\- Valor do ICMS\-ST: considerar zero;

__Abaixo Regra da Matriz do Sped Fiscal:__

Este registro é filho do C300\. 

 

Este registro tem por objetivo informar a consolidação diária de cada intervalo de notas fiscais de venda ao consumidor não emitidas por ECF, que de forma agrupada foi selecionada no registro C300, pela combinação CST\_ICMS, CFOP e Alíquota de ICMS\. 

 

Os campos deste registro deverão ser totalizados dos itens da SAFX08 e quando se tratar de notas sem itens totalizar pela SAFX07\. 

 

Este registro deve apresentar somente os itens com condição 3 e agrupamento 2\. 

 

__Condição 3:__ 

 

Se Movimento Entrada/Saída = “9”, 

  Se Modelo de Documento = “02”, 

           Classificação do Documento Fiscal = “1”, 

                           Situação da Nota = “N”      

 

  

__Campo do Registro C320:__ 

__Totalização pelo item \(SAFX08\)__ 

__Totalização pela capa \(SAFX07\)__ 

CST\_ICMS 

Concatenação dos códigos das tabelas de situação estadual  “A” e “B” \(código A \+ código B\)\. Campos 30 e 31\. 

Concatenação dos códigos das tabelas de situação estadual  “A” e “B” \(código A \+ código B\)\. Campos 179 e 180\. 

CFOP 

Campo 22 

Campo 14 

ALIQ\_ICMS 

Campo 42 quando o código de tributação  for igual a “1” \(campo 55\)\. 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_ITENS\_MERC 

__Campo: __ ALIQ\_TRIBUTO\_ICMS 

Campo 34 

 

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_DOCTO\_FISCAL 

__Campo: __ ALIQ\_TRIBUTO\_ICMS 

VL\_OPR 

Totalização do campo 64 

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_CONTAB\_ITEM 

Campo 23  

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_DOCTO\_FISCAL 

__Campo: __ VLR\_TOT\_NOTA 

VL\_BC\_ICMS 

Totalização do campo 56 \(Base ICMS\) quando o código de tributação  for igual a “1” \(campo 55\)\. 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_BASE\_ICMS\_1 

Campo 51 

 

 

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_DOCTO\_FISCAL 

__Campo: __ VLR\_BASE\_ICMS\_1 

VL\_ICMS 

Totalização do campo 43 \(Valor ICMS\) quando o código de tributação  for igual a “1” \(campo 55\)\. 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_ITENS\_MERC, __Campo: __ VLR\_TRIBUTO\_ICMS 

Campo 35 

 

 

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_DOCTO\_FISCAL 

__Campo: __ VLR\_TRIBUTO\_ICMS 

VL\_RED\_BC 

Totalização do campo 57  \(Base Redução ICMS\)\. 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_ITENS\_MERC, __Campo:__ VLR\_BASE\_ICMS\_4 

Campo 54 

 

 

__Extração dos Dados:__ 

 

__Tabela:__ DWT\_DOCTO\_FISCAL 

__Campo: __ VLR\_BASE\_ICMS\_4 

COD\_OBS 

Não preencher  este campo 

Não preencher este campo 

 

 

# <a id="_QUADRO_DAS_OPERAÇÕES"></a><a id="_Toc139647355"></a>QUADRO DAS OPERAÇÕES E PRESTAÇÕES DE ENTRADAS e SAÍDAS

## <a id="_Toc139647356"></a>3\.1 – Layout  

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                 RESUMO DAS OPERAÇÕES E PRESTAÇÕES DE ENTRADA                                     |

|                                  ENTRADAS DO ESTADO                                              |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| COMPRAS          \- VALOR CONTÁBIL                        : 00000                                 |

| TRANSFERÊNCIAS   \- VALOR CONTÁBIL                        : 00000                                 |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 00000                                 |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 00000                                 |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 00000                                 |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 00000                                 |

| OUTROS           \- VALOR CONTÁBIL                        : 000000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  ENTRADAS DE OUTROS ESTADOS                                      |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| COMPRAS          \- VALOR CONTÁBIL                        : 000000                                |

| TRANSFERÊNCIAS   \- VALOR CONTÁBIL                        : 000000                                |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 000000                                |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 000000                                |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 000000                                |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 000000                                |

| OUTROS           \- VALOR CONTÁBIL                        : 000000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  ENTRADAS DO EXTERIOR                                            |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| COMPRAS          \- VALOR CONTÁBIL                        : 000000                                |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 000000                                |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 000000                                |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 000000                                |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 000000                                |

| OUTROS           \- VALOR CONTÁBIL                        : 000000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  SUBTOTAL DAS ENTRADAS                                           |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| ENTRADAS DO ESTADO           \- VALOR CONTÁBIL                    : 0000000                       |

| ENTRADAS DE OUTROS ESTADOS   \- VALOR CONTÁBIL                    : 0000000                       |

| ENTRADAS DO EXTERIOR         \- VALOR CONTÁBIL                    : 0000000                       |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  TOTAL DAS ENTRADAS                                              |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| TOTAL            \- VALOR CONTÁBIL                        : 0000000                               |

| PRODUTOS AGROPECUARIOS                                   : 0                                     |

| GERAÇÃO DE ENERGIA ELÉTRICA                              : 1                                     |

| AUTUAÇÕES FISCAIS                                        : 3                                     |

| AJUSTE DE TRANSFERÊNCIA                                  : 2                                     |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                 RESUMO DAS OPERAÇÕES E PRESTAÇÕES DE SAÍDAS                                      |

|                                  SAÍDAS PARA O ESTADO                                            |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| VENDAS           \- VALOR CONTÁBIL                        : 10000                                 |

| TRANSFERÊNCIAS   \- VALOR CONTÁBIL                        : 26000                                 |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 42000                                 |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 15000                                 |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 19000                                 |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 90000                                 |

| OUTROS           \- VALOR CONTÁBIL                        : 106000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  SAÍDAS PARA OUTROS ESTADOS                                      |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| VENDAS           \- VALOR CONTÁBIL                        : 122000                                |

| TRANSFERÊNCIAS   \- VALOR CONTÁBIL                        : 138000                                |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 154000                                |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 43000                                 |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 47000                                 |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 202000                                |

| OUTROS           \- VALOR CONTÁBIL                        : 218000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  SAÍDAS PARA O EXTERIOR                                          |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| VENDAS           \- VALOR CONTÁBIL                        : 234000                                |

| DEVOLUÇÕES       \- VALOR CONTÁBIL                        : 250000                                |

| ENERGIA ELÉTRICA \- VALOR CONTÁBIL                        : 67000                                 |

| COMUNICAÇÃO      \- VALOR CONTÁBIL                        : 71000                                 |

| TRANSPORTES      \- VALOR CONTÁBIL                        : 298000                                |

| OUTROS           \- VALOR CONTÁBIL                        : 314000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  SUBTOTAL DAS SAÍDAS                                             |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| SAÍDAS PARA O ESTADO         \- VALOR CONTÁBIL                    : 0000000                       |

| SAÍDAS PARA OUTROS ESTADOS   \- VALOR CONTÁBIL                    : 0000000                       |

| SAÍDAS PARA O EXTERIOR       \- VALOR CONTÁBIL                    : 0000000                       |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  TOTAL DAS SAÍDAS                                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| TOTAL            \- VALOR CONTÁBIL                        : 2466000                               |

| TRANSPORTE TOMADO                                        : 7                                     |

| AUTUAÇÕES FISCAIS                                        : 6                                     |

| COOPERATIVAS                                             : 4                                     |

| AJUSTE DE TRANFERÊNICA                                   : 5                                     |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

                                                                    

                                                                    

## <a id="_Toc139647357"></a>3\.2 – Gravação dos Campos 

### <a id="_3.2.1_-_Quadro"></a><a id="_Toc139647358"></a>3\.2\.1 \- Operações e Prestações de Entradas                                     

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Entradas do Estado__

__Compras__

\(RN60\) Somar campo 5 \(VL\_OPR\) dos Registros C190 e C590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190 e C590: \(1\.101, 1\.102, 1\.111, 1\.113, 1\.116, 1\.117, 1\.118, 1\.120, 1\.121, 1\.122, 1\.124, 1\.125, 1\.126, 1\.132, 1\.135, 1\.159, 1\.401, 1\.403, 1\.501, 1\.651, 1\.652, 1\.653\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.2](#_2.2_–_Recuperação)\.

__Transferências__

\(RN61\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(1\.151, 1\.152, 1\.153, 1\.154, 1\.408, 1\.409, 1\.451, 1\.452, 1\.658, 1\.659\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\) e [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação)  e [2\.4](#_2.4_–_Recuperação)\.

__Devoluções       __

\(RN62\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\)dos Registros C190, D190, C590 e D590: \(1\.201, 1\.202, 1\.203, 1\.204, 1\.205, 1\.206, 1\.207, 1\.208, 1\.209, 1\.212, 1\.214, 1\.215, 1\.216, 1\.410, 1\.411, 1\.503, 1\.504, 1\.660, 1\.661, 1\.662\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Energia Elétrica__

\(RN63\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 EFD para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590 EFD: \(1\.251, 1\.252, 1\.253, 1\.254, 1\.255, 1\.256, 1\.257\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Comunicações    __

\(RN64\)Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 EFD para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590 EFD: \(1\.301, 1\.302, 1\.303, 1\.304, 1\.305, 1\.306\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Transportes  __

\(RN65\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 EFD para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590 EFD: \(1\.351, 1\.352, 1\.353, 1\.354, 1\.355, 1\.356, 1\.360, 1\.931, 1\.932\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Outras      __

\(RN66\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D190 e D590: \(1\.128, 1\.131, 1\.213, 1\.406, 1\.407, 1\.414, 1\.415, 1\.453, 1\.454, 1\.455, 1\.456, 1\.505, 1\.506, 1\.551, 1\.552, 1\.553, 1\.554, 1\.555, 1\.556, 1\.557, 1\.601, 1\.602, 1\.603, 1\.604, 1\.605, 1\.657 1\.663, 1\.664, 1\.901, 1\.902, 1\.903, 1\.904, 1\.905, 1\.906, 1\.907, 1\.908, 1\.909, 1\.910, 1\.911, 1\.912, 1\.913, 1\.914, 1\.915, 1\.916, 1\.917, 1\.918, 1\.919, 1\.920, 1\.921, 1\.922, 1\.923, 1\.924,1\.925, 1\.926, 1\.933, 1\.934, 1\.949\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Entradas de Outros Estados__

__Compras__

\(RN67\) Somar campo 5 \(VL\_OPR\) dos Registros C190 e C590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) do Registro C190 e C590: \(2\.101, 2\.102, 2\.111, 2\.113, 2\.116, 2\.117, 2\.118, 2\.120, 2\.121, 2\.122, 2\.124, 2\.125, 2\.126, 2\.132, 2\.135, 2\.159, 2\.401, 2\.403, 2\.501, 2\.651, 2\.652, 2\.653\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.2](#_2.2_–_Recuperação)\.

__Transferências__

\(RN68\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(2\.151, 2\.152, 2\.153, 2\.154, 2\.408, 2\.409, 2\.658, 2\.659\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\) e [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação)  e [2\.4](#_2.4_–_Recuperação)\.

__Devoluções       __

\(RN69\)Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(2\.201, 2\.202, 2\.203, 2\.204, 2\.205, 2\.206, 2\.207, 2\.208, 2\.209, 2\.212, 2\.214, 2\.215, 2\.216, 2\.410, 2\.411, 2\.503, 2\.504, 2\.660, 2\.661, 2\.662\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Energia Elétrica__

\(RN70\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 EFD para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590 EFD: \(2\.251, 2\.252 2\.253, 2\.254, 2\.255, 2\.256, 2\.257\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Comunicações    __

\(RN71\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590: \(2\.301, 2\.302, 2\.303, 2\.304, 2\.305, 2\.306\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Transportes  __

\(RN72\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(2\.351, 2\.352, 2\.353, 2\.354, 2\.355, 2\.356, 2\.931, 2\.932\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Outras      __

\(RN73\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D190 e D590: \(2\.128, 2\.131, 2\.213, 2\.406, 2\.407, 2\.414, 2\.415, 2\.451, 2\.452, 2\.453, 2\.454, 2\.455, 2\.456,  2\.505, 2\.506, 2\.551, 2\.552, 2\.553, 2\.554, 2\.555, 2\.556, 2\.557, 2\.603, 2\.657, 2\.663, 2\.664, 2\.901, 2\.902, 2\.903, 2\.904, 2\.905, 2\.906, 2\.907, 2\.908, 2\.909, 2\.910, 2\.911, 2\.912, 2\.913, 2\.914, 2\.915, 2\.916, 2\.917, 2\.918, 2\.919, 2\.920, 2\.921, 2\.922, 2\.923, 2\.924, 2\.925, 2\.933, 2\.934, 2\.949\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Entradas do Exterior__

__Compras__

\(RN74\) Somar campo 5 \(VL\_OPR\) do Registro C190 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) do Registro C190: \(3\.101, 3\.102, 3\.126, 3\.127, 3\.129, 3\.651, 3\.652, 3\.653\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

__Devoluções       __

\(RN75\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(3\.201, 3\.202, 3\.205, 3\.206, 3\.207, 3\.211, 3\.212, 3\.503\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Energia Elétrica__

\(RN76\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com o seguinte CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(3\.251\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Comunicações    __

\(RN77\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com o seguinte CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(3\.301\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Transportes  __

\(RN78\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(3\.351, 3\.352, 3\.353, 3\.354, 3\.355, 3\.356\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__Outras      __

\(RN79\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(3\.128, 3\.551, 3\.553, 3\.556, 3\.930, 3\.949\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação)\.

__Subtotais das Entradas__

__Entradas do Estado__

\(RN80\) Aplicar a seguinte fórmula considerando os valores das regras: RN60 \+ RN61 \+ RN62 \+ RN63 \+ RN64 \+ RN65 \+ RN66\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores apresentados em Entradas do Estado: Compras \+ Transferências \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Entradas de Outros Estados__

\(RN81\)Aplicar a seguinte fórmula considerando os valores das regras: RN67 \+ RN68 \+ RN69 \+ RN70 \+ RN71 \+ RN72 \+ RN73\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores apresentados em Entradas de Outros Estados: Compras \+ Transferências \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Entradas do Exterior__

\(RN82\)Aplicar a seguinte fórmula considerando os valores das regras: RN74 \+ RN75 \+ RN76 \+ RN77 \+ RN78 \+ RN79\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores apresentados em Entradas do Exterior: Compras \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Total das Entradas__

__Total__

\(RN83\) Aplicar a seguinte fórmula considerando os valores das regras: RN80 \+ RN81 \+ RN82\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos Subtotais das Entradas: do Estado \+ de Outros Estados \+ do Exterior\.

__Produtos Agropecuários__

\(RN84\) Somatório dos valores do campo 4 \(VALOR\) do Registro __1400__ EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Produtos Agropecuarios”\.

Regra aplicável aos tipos: Regular e Especial\.

Campo disponível para edição pelo contribuinte\.

Valor deve ser apurado em conformidade com o disposto no subitem 3\.1 da Resolução nº 5\.369, de 2020\.

__\[MFS\-45263\]__

Total do valor apresentado para Produtos Agropecuários\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Produtos\_Agropecuarios”\.

__Geração de Energia Elétrica__

\(RN85\) Somatório dos valores do campo 4 \(VALOR\) do Registro __1400__ EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Geracao\_de\_Energia\_Eletrica”\.

Regra aplicável aos tipos: Regular e Especial\.

Campo disponível para edição pelo contribuinte\.

Valor deve ser apurado em conformidade com o disposto no subitem 3\.5 da Resolução nº 5\.369, de 2020\.

__\[MFS\-45263\]__

Total do valor apresentado para Geração de Energia Elétrica\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Geracao\_de\_Energia\_Eletrica”\.

__Autuações Fiscais__

\(RN86\) Regra aplicável aos tipos: Regular e Especial\.

Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo Autuações Fiscais, do quadro Valores para as Entradas\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais 

__Ajuste de Transferência__

\(RN87\) Regra aplicável aos tipos: Regular e Especial\.

Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo Ajuste de Transferência, do quadro Valores para as Entradas\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

                                

### <a id="_3.2.2_-_Quadro"></a><a id="_Toc139647359"></a>3\.2\.2 \- Operações e Prestações de Saída                                     

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Saídas para o Estado__

__Vendas__

\(RN88\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C320 e C490 para os valores com os seguintes CFOP\- campo 3 \(CFOP\) dos Registros C190, C320 e C490: \(5\.101, 5\.102, 5\.103, 5\.104, 5\.105, 5\.106, 5\.109, 5\.110, 5\.111, 5\.112, 5\.113, 5\.114, 5\.115, 5\.116, 5\.117, 5\.118, 5\.119, 5\.120, 5\.122, 5\.123, 5\.124, 5\.125, 5\.129, 5\.132, 5\.159, 5\.160, 5\.401, 5\.402, 5\.403, 5\.405, 5\.501, 5\.502, 5\.651, 5\.652, 5\.653, 5\.654, 5\.655, 5\.656, 5\.667\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\), [2\.1](#_2.15_–_Recuperação)5 \(C320\) [2\.7](#_2.7_–_Recuperação) \(C490\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.1](#_2.15_–_Recuperação)5 , [2\.7](#_2.7_–_Recuperação)\.

__Transferências__

\(RN89\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(5\.151, 5\.152, 5\.153, 5\.155, 5\.156, 5\.408, 5\.409, 5\.451, 5\.658, 5\.659\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das) 

__Devoluções       __

\(RN90\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(5\.201, 5\.202, 5\.205, 5\.206, 5\.207, 5\.208, 5\.209, 5\.214, 5\.215, 5\.216, 5\.410, 5\.411, 5\.503, 5\.660, 5\.661, 5\.662\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das)  e [2\.6](#_2.6_–_Recuperação)\.

__Energia Elétrica__

\(RN91\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, C690, C790 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590, C690, C790: \(5\.251, 5\.252, 5\.253, 5\.254, 5\.255, 5\.256, 5\.257, 5\.258\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.3\.2](#_‘2.3.2_Recuperação_das) \(C690\), [2\.3\.3](#_2.3.3_Recuperação_das) \(C790\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.3\.2](#_‘2.3.2_Recuperação_das), [2\.3\.3](#_2.3.3_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Comunicações    __

\(RN92\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, D690, D696 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590, D690, D696: \(5\.301, 5\.302, 5\.303, 5\.304, 5\.305, 5\.306, 5\.307\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), [2\.5\.2](#_‘2.5.2_Recuperação_das) \(D690\), [2\.5\.3](#_2.5.3_Recuperação_das) \(D696\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.5\.2](#_‘2.5.2_Recuperação_das), [2\.5\.3](#_2.5.3_Recuperação_das)

__Transportes  __

\(RN93\)

7\.1\.93\.1 \- Somar campo 5 \(VL\_OPR\) dos Registros EFD C190, C590, D190, D390 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros EFD C190, C590, D190, D390 e D590: \(5\.351, 5\.352, 5\.353, 5\.354, 5\.355, 5\.356, 5\.357, 5\.359, 5\.360, 5\.932\)\.

7\.1\.93\.2 \- Somar campo 11\(VL\_OPR\) dos Registros EFD C190, C590, D190, D390 e D590 para os valores com os seguintes CFOP \- campo 8 \(CFOP\) do Registro __D300__ EFD: \(5\.351, 5\.352, 5\.353, 5\.354, 5\.355, 5\.356, 5\.357, 5\.359, 5\.360, 5\.932\)

7\.1\.93\.3 \- Somar campo 11\(VL\_OPR\) dos Registros EFD C190, C590, D190, D390 e D590 para os valores com os seguintes CFOP \- campo 9 \(CFOP\) do registro __D410__ EFD: \(5\.351, 5\.352, 5\.353, 5\.354, 5\.355, 5\.356, 5\.357, 5\.359, 5\.360, 5\.932\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) , [2\.6](#_2.6_–_Recuperação) \(D190\) e [2\.8](#_2.8_–_Recuperação) \(D390\), [2\.9](#_2.9_–_Recuperação) \(D300\)  e [2\.10](#_2.10_–_Recuperação) \(D410\) \) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.6](#_2.6_–_Recuperação), [2\.8](#_2.8_–_Recuperação), [2\.9](#_2.9_–_Recuperação) e [2\.10](#_2.10_–_Recuperação) \.

__Outras      __

\(RN94\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C320, C490, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\)dos Registros C190, C320, C490,  C590 e D590: \(5\.131, 5\.210, 5\.213, 5\.412, 5\.413, 5\.414, 5\.415,5\.452, 5\.453, 5\.454, 5\.455, 5\.456 5\.504, 5\.505, 5\.551, 5\.552, 5\.553, 5\.554, 5\.555, 5\.556, 5\.557, 5\.601, 5\.602, 5\.603, 5\.605, 5\.606, 5\.657, 5\.663, 5\.664, 5\.665, 5\.666, 5\.901, 5\.902, 5\.903, 5\.904, 5\.905, 5\.906, 5\.907, 5\.908, 5\.909, 5\.910, 5\.911, 5\.912, 5\.913, 5\.914, 5\.915, 5\.916, 5\.917, 5\.918, 5\.919, 5\.920, 5\.921, 5\.922, 5\.923, 5\.924, 5\.925, 5\.926, 5\.927, 5\.928, 5\.929, 5\.931, 5\.933, 5\.934, 5\.949\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\), [2\.1](#_2.15_–_Recuperação)5 \(C320\), [2\.7](#_2.7_–_Recuperação) \(C490\), [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.1](#_2.15_–_Recuperação)5 , [2\.7](#_2.7_–_Recuperação), [2\.3\.1](#_2.3.1_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Saídas para Outros Estados__

__Vendas__

\(RN95\) Somar campo 5 \(VL\_OPR\) dos Registros C190 e C490 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190 e C490: \(6\.101, 6\.102, 6\.103, 6\.104, 6\.105, 6\.106, 6\.107, 6\.108, 6\.109, 6\.110, 6\.111, 6\.112, 6\.113, 6\.114, 6\.115, 6\.116, 6\.117, 6\.118, 6\.119, 6\.120, 6\.122, 6\.123, 6\.124, 6\.125, 6\.129, 6\.132, 6\.159, 6\.160, 6\.401, 6\.402, 6\.403, 6\.404, 6\.501, 6\.502, 6\.651, 6\.652, 6\.653, 6\.654, 6\.655, 6\.656, 6\.667\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\), [2\.7](#_2.7_–_Recuperação) \(C490\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.7](#_2.7_–_Recuperação)\.

__Transferências__

\(RN96\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(6\.151, 6\.152, 6\.153, 6\.155, 6\.156, 6\.408, 6\.409, 6\.658, 6\.659\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Devoluções       __

\(RN97\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190 e C590 e D590: \(6\.201, 6\.202, 6\.205, 6\.206, 6\.207, 6\.208, 6\.209, 6\.214, 6\.215, 6\.216, 6\.410, 6\.411, 6\.503, 6\.660, 6\.661, 6\.662\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das)  e [2\.6](#_2.6_–_Recuperação)\.

__Energia Elétrica__

\(RN98\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, C690, C790 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590, C690, C790: \(6\.251, 6\.252, 6\.253, 6\.254, 6\.255, 6\.256, 6\.257, 6\.258\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.3\.2](#_‘2.3.2_Recuperação_das) \(C690\), [2\.3\.3](#_2.3.3_Recuperação_das) \(C790\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.3\.2](#_‘2.3.2_Recuperação_das), [2\.3\.3](#_2.3.3_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Comunicações    __

\(RN99\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, D690, D696 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590, D690, D696: \(6\.301, 6\.302, 6\.303, 6\.304, 6\.305, 6\.306, 6\.307\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), [2\.5\.2](#_‘2.5.2_Recuperação_das) \(D690\), [2\.5\.3](#_2.5.3_Recuperação_das) \(D696\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.5\.2](#_‘2.5.2_Recuperação_das), [2\.5\.3](#_2.5.3_Recuperação_das)

__Transportes  __

\(RN100\)

7\.1\.100\.1 \- Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190, D390, D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D190, D390, D590: \(6\.351, 6\.352, 6\.353, 6\.354, 6\.355, 6\.356, 6\.357, 6\.359, 6\.360, 6\.932\);

7\.1\.100\.2 \- Somar campo 11 \(VL\_OPR\) dos Registros C190, C590, D190, D390, D590 para os valores com os seguintes CFOP \- campo 8 \(CFOP\) do Registro __D300__ EFD: \(6\.351, 6\.352, 6\.353, 6\.354, 6\.355, 6\.356, 6\.357, 6\.359, 6\.360, 6\.932\);

7\.1\.100\.3 \- Somar campo 11 \(VL\_OPR\) para os valores com os seguintes CFOP \- campo 9 \(CFOP\) do registro __D410__ EFD: \(6\.351, 6\.352, 6\.353, 6\.354, 6\.355, 6\.356, 6\.357, 6\.359, 6\.360, 6\.932\)\. 

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) , [2\.6](#_2.6_–_Recuperação) \(D190\) e [2\.8](#_2.8_–_Recuperação) \(D390\), [2\.9](#_2.9_–_Recuperação) \(D300\)  e [2\.10](#_2.10_–_Recuperação) \(D410\) adicionando os critérios:

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.6](#_2.6_–_Recuperação), [2\.8](#_2.8_–_Recuperação), [2\.9](#_2.9_–_Recuperação) e [2\.10](#_2.10_–_Recuperação) \.

__Outras      __

\(RN101\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(6\.131, 6\.210, 6\.213, 6\.412, 6\.413, 6\.414, 6\.415, 6\.451, 6\.452, 6\.453, 6\.454, 6\.455, 6\.456, 6\.504, 6\.505, 6\.551, 6\.552, 6\.553, 6\.554, 6\.555, 6\.556, 6\.557, 6\.603, 6\.657, 6\.663, 6\.664, 6\.665, 6\.666, 6\.901, 6\.902, 6\.903, 6\.904, 6\.905, 6\.906, 6\.907, 6\.908, 6\.909, 6\.910, 6\.911, 6\.912, 6\.913, 6\.914, 6\.915, 6\.916, 6\.917, 6\.918, 6\.919, 6\.920, 6\.921, 6\.922, 6\.923, 6\.924, 6\.925, 6\.929, 6\.931, 6\.933, 6\.934, 6\.949\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Saídas para o Exterior__

__Vendas__

\(RN102\) Somar campo 5 \(VL\_OPR\) do Registro C190 e C490 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) Registro C190 e C490: \(7\.101, 7\.102, 7\.105, 7\.106, 7\.127, 7\.129, 7\.501, 7\.504, 7\.651, 7\.654, 7\.667\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\), [2\.7](#_2.7_–_Recuperação) \(C490\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação), [2\.7](#_2.7_–_Recuperação)\.

__Devoluções       __

\(RN103\) Somar campo 5 \(VL\_OPR\) dos Registros C190, D190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, D190, C590 e D590: \(7\.201, 7\.202, 7\.205, 7\.206, 7\.207, 7\.211, 7\.212\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das)  e [2\.6](#_2.6_–_Recuperação)\.

__Energia Elétrica__

\(RN104\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, C690, C790 para os valores com o seguinte CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D590, C690, C790: \(7\.251\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.3\.2](#_‘2.3.2_Recuperação_das) \(C690\), [2\.3\.3](#_2.3.3_Recuperação_das) \(C790\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.3\.2](#_‘2.3.2_Recuperação_das), [2\.3\.3](#_2.3.3_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Comunicações    __

\(RN105\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D590, D690, D696 para os valores com o seguinte CFOP \- campos 3 \(CFOP\) C190, C590, D590, D690, D696: \(7\.301\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\), [2\.5\.2](#_‘2.5.2_Recuperação_das) \(D690\), [2\.5\.3](#_2.5.3_Recuperação_das) \(D696\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.5\.2](#_‘2.5.2_Recuperação_das), [2\.5\.3](#_2.5.3_Recuperação_das)

__Transportes  __

\(RN106\)

7\.1\.106\.1 \- Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190, D390, D590 para os valores com o seguinte CFOP \- campos 3 \(CFOP\) C190, C590, D190, D390, D590: \(7\.358\);

7\.1\.106\.2 \- Somar campo 11 \(VL\_OPR\) dos Registros C190, C590, D190, D390, D590 para os valores com os seguintes CFOP \- campo 8 \(CFOP\) do Registro __D300__ EFD: \(7\.358\)\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) , [2\.6](#_2.6_–_Recuperação) \(D190\) e [2\.8](#_2.8_–_Recuperação) \(D390\), [2\.9](#_2.9_–_Recuperação) \(D300\)  adicionando os critérios:

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das), [2\.6](#_2.6_–_Recuperação), [2\.8](#_2.8_–_Recuperação), [2\.9](#_2.9_–_Recuperação)\.

__Outras      __

\(RN107\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com o seguinte CFOP \- campo 3 \(CFOP\) dos registros C190, C590 e D590: \(7\.210, 7\.551, 7\.553, 7\.556, 7\.930, 7\.949\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar os documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\) e [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das) e [2\.5\.1](#_2.5.1_Recuperação_das)

__Subtotais das Saídas__

__Saídas para o Estado__

\(RN108\)

7\.1\.108\.1 \- Regra aplicável aos tipos Regular e Especial: somar os valores das regras conforme a seguinte fórmula: RN88 \+ RN89 \+ RN90 \+ RN91 \+ RN92 \+ RN93 \+ RN94\.

7\.1\.108\.2 \- Regra aplicável ao tipo Transportador: valor da RN93

Somatório dos valores apresentados em Saídas para o Estado: Vendas \+ Transferências \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Saídas para Outros Estados__

\(RN109\)

7\.1\.109\.1 \- Regra aplicável aos tipos Regular e Especial: somar os valores das regras conforme a seguinte fórmula: RN95 \+ RN96 \+ RN97 \+ RN98 \+ RN99 \+ RN100 \+ RN101\.

7\.1\.109\.2 \- Regra aplicável ao tipo Transportador: valor da RN100\.

Somatório dos valores apresentados em Saídas para outros Estado: Vendas \+ Transferências \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Saídas para o Exterior__

\(RN110\)

7\.1\.110\.1 \- Regra aplicável aos tipos Regular e Especial: somar os valores das regras conforme a seguinte fórmula: RN102 \+ RN103 \+ RN104 \+ RN105 \+ RN106 \+ RN107\.

7\.1\.110\.2 \- Regra aplicável ao tipo Transportador: valor da RN106\.

Somatório dos valores apresentados em Saídas para o Exterior: Vendas \+ Devoluções \+ Energia Elétrica \+ Comunicações \+ Transportes \+ Outras\.

__Total das Saídas__

__Total__

\(RN111\)Somar os valores das regras conforme a seguinte fórmula:

RN108 \+ RN109 \+ RN110\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos Subtotais das Saídas: para o Estado \+ para Outros Estados \+ para o Exterior\.

__Transporte Tomado__

\(RN112\) Somatório dos Valores do campo 4 \(VALOR\) Registro __1400__ EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Transporte Tomado”\.

Regra aplicável aos tipos: Regular e Especial\.

Campo disponível para edição pelo contribuinte\.

Valor deve ser apurado em conformidade com o disposto no subitem 3\.2 da Resolução nº 5\.369, de 2020\.

__\[MFS\-45263\]__ 

Total do valor apresentado para Transporte Tomado\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Transporte\_Tomado”\.

__Autuações Fiscais__

\(RN113\) Regra aplicável aos tipos: Regular, Transportador e Especial\.

Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo Autuações Fiscais, do quadro Valores para as Saídas\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais 

__Cooperativas__

\(RN114\) Somatório dos Valores do campo 4 \(VALOR\) Registro __1400__ EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Cooperativas”\.

Regra aplicável aos tipos: Regular e Especial\.

Campo disponível para edição pelo contribuinte\.

Valor deve ser apurado em conformidade com o disposto no subitem 3\.3 da Resolução nº 5\.369, de 2020\.

__\[MFS\-45263\]__

Total do valor apresentado para Cooperativas\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Cooperativas”\.

__Ajuste de Transferência__

\(RN115\) Regra aplicável aos tipos: Regular e Especial\.

Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo Ajuste de Transferência, do quadro Valores para as Saídas\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

# <a id="_QUADRO_RESUMO_DAS"></a><a id="_Toc139647360"></a>QUADRO RESUMO DAS ENTRADAS e SAÍDAS

## <a id="_Toc139647361"></a>4\.1 – Layout

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                RESUMO DAS ENTRADAS                                               |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| COMPRAS                        \- VALOR CONTÁBIL          : 00000                                 |

| TRANSFERÊNCIAS                 \- VALOR CONTÁBIL          : 00000                                 |

| DEVOLUÇÕES                     \- VALOR CONTÁBIL          : 00000                                 |

| ENERGIA ELÉTRICA \+ COMUNICAÇÃO \- VALOR CONTÁBIL          : 00000                                 |

| TRANSPORTES                    \- VALOR CONTÁBIL          : 00000                                 |

| OUTROS                         \- VALOR CONTÁBIL          : 000000                                |

| TOTAL DAS ENTRADAS             \- VALOR CONTÁBIL          : 000000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                 RESUMO DAS SAÍDAS                                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| VENDAS                         \- VALOR CONTÁBIL          : 10000                                 |

| TRANSFERÊNCIAS                 \- VALOR CONTÁBIL          : 26000                                 |

| DEVOLUÇÕES                     \- VALOR CONTÁBIL          : 42000                                 |

| ENERGIA ELÉTRICA \+ COMUNICAÇÃO \- VALOR CONTÁBIL          : 15000                                 |

| TRANSPORTES                    \- VALOR CONTÁBIL          : 90000                                 |

| OUTROS                         \- VALOR CONTÁBIL          : 106000                                |

| TOTAL DAS SAÍDAS               \- VALOR CONTÁBIL          : 308000                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  TOTAL DAS ENTRADAS E SAÍDAS                                     |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| ENTRADAS \- AUTUAÇÕES FISCAIS                             : 0000000                               |

| ENTRADAS \- AJUSTE DE TRANSFERÊNCIA                       : 0000000                               |

| SAÍDAS \- AUTUAÇÕES FISCAIS                               : 0000000                               |

| SAÍDAS \- AJUSTE DE TRANSFERÊNCIA                         : 0000000                               |

| ENTRADAS \- PRODUTOS AGROPECUARIOS                        : 0000000                               |

| ENTRADAS \- GERAÇÃO DE ENERGIA ELÉTRICA                   : 0000000                               |

| SAÍDAS \- TRANSPORTE TOMADO                               : 0000000                               |

| SAÍDAS \- COOPERATIVAS                                    : 0000000                               |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

                                                                    

## <a id="_4.2_–_Gravação"></a><a id="_Toc139647362"></a>4\.2 – Gravação dos Campos 

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Resumo das Entradas__

__Compras__

\(RN26\)Aplicar a seguinte fórmula considerando os valores das regras: RN60 \+ RN67 \+ RN74\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos três valores de Compras apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados e Entradas do Exterior\. \.

__Transferências__

\(RN27\)Aplicar a seguinte fórmula considerando os valores das regras: RN61 \+ RN68\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos dois valores de Transferências apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados\.

__Devoluções       __

\(RN28\)Aplicar a seguinte fórmula considerando os valores das regras: RN62 \+ RN69 \+ RN75\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos três valores de Devolução apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados e Entradas do Exterior\.

__Energia Elétrica \+ Comunicação__

\(RN29\)Aplicar a seguinte fórmula considerando os valores das regras: RN63 \+ RN70 \+ RN76 \+ RN64 \+ RN71 \+ RN77\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores de Energia Elétrica \+ Comunicação apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados e Entradas do Exterior\.

__Transportes  __

\(RN30\)Aplicar a seguinte fórmula considerando os valores das regras: RN65 \+ RN72 \+ RN78\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores de Transporte apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados e Entradas do Exterior\.

__Outras      __

\(RN31\)Aplicar a seguinte fórmula considerando os valores das regras: RN66 \+ RN73 \+ RN79\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores de Outras apresentados nos quadros do tópico [3\.2\.1](#_3.2.1_-_Quadro): Entradas do Estado, Entradas de Outros Estados e Entradas do Exterior\.

<a id="Rn32"></a>__Total das Entradas__

\(RN32\)Aplicar a seguinte fórmula considerando os valores das regras: RN26 \+ RN27 \+ RN28 \+ RN29 \+ RN30 \+ RN31\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos campos acima mencionados:

\- Compras

\- Transferências

\- Devoluções

\- Energia Elétrica \+ Comunicação

\- Transportes

\- Outras

__Resumo das Saídas__

__Vendas__

\(RN33\) Aplicar a seguinte fórmula considerando os valores das regras: RN88 \+ RN95 \+ RN102\.

Regra aplicável aos tipos: Regular e Especial\.

Somatório dos valores de Vendas apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados e Saídas para Exterior\.

__Transferências__

\(RN34\) Aplicar a seguinte fórmula considerando os valores das regras: RN89 \+ RN96\.

Regra aplicável aos tipos: Regular e Especial\.

Somatório dos valores de Transferências apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados\.

__Devoluções       __

\(RN35\) Aplicar a seguinte fórmula considerando os valores das regras: RN90 \+ RN97 \+ RN103\.

Regra aplicável aos tipos: Regular e Especial\.

Somatório dos valores de Devoluções apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados e Saídas para Exterior\.

__Energia Elétrica \+ Comunicação__

\(RN36\) Aplicar a seguinte fórmula considerando os valores das regras: RN91 \+ RN98 \+ RN104 \+ RN92 \+ RN99 \+ RN105\.

Regra aplicável aos tipos: Regular e Especial\.

Somatório dos valores de Energia Elétrica \+ Comunicação apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados e Saídas para Exterior\.

<a id="Rn37"></a>__Transportes  __

\(RN37\)Aplicar a seguinte fórmula considerando os valores das regras: RN93 \+ RN100 \+ RN106\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Somatório dos valores de Transportes apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados e Saídas para Exterior\.

__Outras      __

\(RN38\) Aplicar a seguinte fórmula considerando os valores das regras: RN94 \+ RN101 \+ RN107\.

Regra aplicável aos tipos: Regular e Especial\.

Somatório dos valores de Outras apresentados nos quadros do tópico [3\.2\.2](#_3.2.2_-_Quadro): Saídas para Estado, Saídas para Outros Estados e Saídas para Exterior\.

<a id="Rn39"></a>__Total das Saídas__

\(RN39\) Regra aplicável aos tipos Regular e Especial: aplicar a seguinte fórmula considerando os valores das regras: RN33 \+ RN34 \+ RN35 \+ RN36 \+ RN37 \+ RN38\.

Tipo Transportador: valor da RN37\.

Somatório dos campos acima mencionados:

\- Vendas

\- Transferências

\- Devoluções

\- Energia Elétrica \+ Comunicação

\- Transportes

\- Outras

__TOTAL DAS ENTRADAS E SAÍDAS__

<a id="Rn40"></a>__ENTRADAS \- AUTUAÇÕES FISCAIS__

\(RN40\)Valor da RN86\.

Regra aplicável aos tipos: Regular e Especial\.

Valor de Autuações Fiscais apresentado no quadro do tópico [3\.2\.1](#_3.2.1_-_Quadro)\.

<a id="Rn41"></a>__ENTRADAS \- AJUSTE DE TRANSFERÊNCIA__

\(RN41\)Valor da RN87\.

Regra aplicável aos tipos: Regular e Especial\.

Valor de Ajuste de Transferência apresentado no quadro do tópico [3\.2\.1](#_3.2.1_-_Quadro)\.

<a id="Rn42"></a>__SAÍDAS \- AUTUAÇÕES FISCAIS__

\(RN42\)Valor da RN113\.

Regra aplicável aos tipos: Regular, Transportador e Especial\.

Valor de Autuações Fiscais apresentado no quadro do tópico [3\.2\.2](#_3.2.2_-_Quadro)\.

<a id="Rn43"></a>__SAÍDAS \- AJUSTE DE TRANSFERÊNCIA__

\(RN43\)Valor da RN115\.

Regra aplicável aos tipos: Regular e Especial\.

Valor de Ajuste de Transferência apresentado no quadro do tópico [3\.2\.2](#_3.2.2_-_Quadro)\.

<a id="Rn44"></a>__ENTRADAS \- PRODUTOS AGROPECUÁRIOS/ HORTIFRUTIGRANJEIROS__

\(RN44\) Valor da RN84\.

Regra aplicável aos tipos: Regular e Especial\.

__\[MFS\-45263\]__

Valor de Produtos Agropecuários apresentado no quadro do tópico [3\.2\.1](#_3.2.1_-_Quadro)\.

<a id="Rn45"></a>__ENTRADAS \- GERAÇÃO ENERGIA ELÉTRICA PARA CONSUMO PRÓPRIO__

\(RN45\)Valor da RN85\.

Regra aplicável aos tipos: Regular e Especial\.

__\[MFS\-45263\]__

Valor de Geração de Energia Elétrica apresentado no quadro do tópico [3\.2\.1](#_3.2.1_-_Quadro)\.

<a id="Rn46"></a>__SAÍDAS \- TRANSPORTE TOMADO__

\(RN46\)Campo 46 da DAMEF

Valor da RN112\.

Regra aplicável aos tipos: Regular e Especial\.

__\[MFS\-45263\]__

Valor de Transporte Tomado apresentado no quadro do tópico [3\.2\.2](#_3.2.2_-_Quadro)\.

<a id="Rn47"></a>__SAÍDAS \- COOPERATIVAS__

\(RN47\) Valor da RN114\.

Regra aplicável aos tipos: Regular e Especial\.

__\[MFS\-45263\]__

Valor de Cooperativas apresentado no quadro do tópico [3\.2\.2](#_3.2.2_-_Quadro)\.

# <a id="_Toc139647363"></a>Quadro Exclusão do VAF

## <a id="_Toc139647364"></a>5\.1 – Layout

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                        EXCLUSÃO DO VAF                                           |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                        DESCRIÇÃO                            ENTRADA                              |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| Parcela do ICMS Retido por Substituição Tributária                     0                         |

| Parcela do IPI que não integre a base de cálculo ICMS                  0                         |

| Energia Elétrica/Comunicação                                           0                         |

| Transportes\(parcela não utilizada\)                                     0                         |

| Subcontratação de Serviço de Transporte                                0                         |

| Ativo Imobilizado                                                      0                         |

| Material de Uso e Consumo                                              0                         |

| Outras – Entradas                                                      0                         |

| Ajuste – Entradas                                                      0                         |

| Extraordinária – Entradas                                              0                         |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|Total das Exclusões \- Entradas                                          0                         |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                        DESCRIÇÃO                            SAÍDA                                |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

| Parcela do ICMS Retido por Substituição Tributária                     0                         |

| Parcela do IPI que não integre a base de cálculo ICMS                  0                         |

| Transp\. Iniciados em Outros Países/UF/Municipal/Aéreo de Passageiro    0                         |

| Ativo Imobilizado                                                      0                         |

| Material de Uso e Consumo                                              0                         |

| Outras – Saídas                                                        0                         |

| Ajuste – Saídas                                                        0                         |

| Extraordinárias – Saídas                                               0                         |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|Total das Exclusões \- Saídas                                            0                         |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

## <a id="_5.2_–_Gravação"></a><a id="_Toc139647365"></a>5\.2 – Gravação dos Campos

### <a id="_Toc139647366"></a>5\.2\.1 – Exclusão do VAF \- Entradas

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Entradas__

__PARCELA DO ICMS RETIDO POR SUBSTITUIÇÃO TRIBUTÁRIA__

__\(ENTRADA\)__

\(RN01\)

7\.1\.1\.1 \- Somar campo 7 \(VL\_ICMS\) quando o campo 2 \(COD\_AJ\) do Registro C197 da EFD for o código de ajuste MG91990000 e/ou MG91990006\.

7\.1\.1\.2 \- Somar Registros C190, C590 da EFD para os CFOP:1\.101, 1\.102, 1\.111, 1\.113, 1\.116, 1\.117, 1\.118, 1\.120, 1\.121, 1\.122, 1\.124, 1\.125, 1\.126, 1\.132, 1\.135, 1\.151, 1\.152, 1\.153, 1\.154, 1\.159, 1\.201, 1\.202, 1\.203, 1\.204, 1\.205, 1\.206, 1\.207, 1\.208, 1\.209, 1\.212, 1\.214, 1\.215, 1\.216, 1\.251, 1\.252, 1\.255, 1\.256, 1\.257, 1\.301, 1\.351, 1\.352, 1\.353, 1\.356, 1\.360, 1\.401, 1\.403, 1\.408, 1\.409, 1\.410, 1\.411, 1\.414, 1\.415, 1\.451, 1\.452, 1\.501, 1\.503, 1\.504, 1\.651, 1\.652, 1\.653, 1\.658, 1\.659, 1\.660, 1\.661, 1\.662, 1\.904, 1\.910, 1,931, 1\.932, 2\.101, 2\.102, 2\.111, 2\.113, 2\.116, 2\.117, 2\.118, 2\.120, 2\.121, 2\.122, 2\.124, 2\.125, 2\.126, 2\.132, 2\.135, 2\.151, 2\.152, 2\.153, 2\.154, 2\.159, 2\.201, 2\.202, 2\.203, 2\.204, 2\.205, 2\.206, 2\.207, 2\.208, 2\.209, 2\.212, 2\.214, 2\.215, 2\.216, 2\.251, 2\.252, 2\.255, 2\.256, 2\.257, 2\.301, 2\.351, 2\.352, 2\.353, 2\.356, 2\.401, 2\.403, 2\.408, 2\.409, 2\.410, 2\.411, 2\.414, 2\.415, 2\.501, 2\.503, 2\.504, 2\.651, 2\.652, 2\.653, 2\.658, 2\.659, 2\.660, 2\.661, 2\.662, 2\.904, 2\.910, 2\.931, 2\.932, 3\.101, 3\.102, 3\.126, 3\.127, 3\.129, 3\.201, 3\.202, 3\.205, 3\.206, 3\.207, 3\.211, 3\.212, 3\.251, 3\.301, 3\.351, 3\.352, 3\.356, 3\.503, 3\.651, 3\.652, 3\.653\.

7\.1\.1\.2\.1 \- Para buscar o “CFOP” no registro C190 e C590 da EFD verificar no campo 3 \(CFOP\)\.

7\.1\.1\.2\.2 \- Para buscar o “Valor” no registro C190 e C590 da EFD verificar no campo 9 \(VL\_ICMS\_ST\)\.

7\.1\.1\.3 \- Deverão ser somados VL\_ICMS referente ao subitem 7\.1\.1\.1 e VL\_ICMS\_ST referente ao subitem 7\.1\.1\.2\. Ou seja, o valor do campo 01 será VL\_ICMS \+ VL\_ICMS\_ST\.

Regras aplicáveis aos tipos: Regular e Especial\.

Recuperar o __Valor do ICMS__ \(VLR\_ICMS\) dos  ajustes da SAFX113, de acordo com regras descritas nos tópico [2\.11](#_2.11_–_Recuperação) \(C197\), adicionando os critérios:

- Movimento Entrada/Saída \(MOVTO\_E\_S\) <> 9;
- Código do Ajuste \(COD\_AJUSTE\_SPED\) = MG91990000 ou MG91990006\.

Recuperar o __Valor do ICMS\-ST__ dos documentos, de acordo com regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\) e  [2\.2](#_2.2_–_Recuperação) \(C590\) e que atendam aos códigos CFOPs determinados na regra do Fisco, vide lista ao lado\.

Somar o __Valor do ICMS__ \+ __Valor do ICMS\-ST__\.

__PARCELA DO IPI QUE NÃO INTEGRE A BASE DE CÁLCULO DO ICMS__

__\(ENTRADA\)__

\(RN02\) Somar Registro C190 da EFD para os CFOP:

1\.101, 1\.102, 1\.111, 1\.113, 1\.116, 1\.117, 1\.118, 1\.120, 1\.121, 1\.122, 1\.124, 1\.125, 1\.126, 1\.132, 1\.135, 1\.151, 1\.152, 1\.153, 1\.154, 1\.159, 1\.201, 1\.202, 1\.203, 1\.204, 1\.205, 1\.206, 1\.207, 1\.208, 1\.209\.1\.212, 1\.214, 1\.215, 1\.216, 1\.251, 1\.252, 1\.255, 1\.256, 1\.257, 1\.301, 1\.351, 1\.352, 1\.353, 1\.356, 1\.360, 1\.401, 1\.403, 1\.408, 1\.409, 1\.410, 1\.411, 1\.414, 1\.415, 1\.451, 1\.452, 1\.501, 1\.503, 1\.504, 1\.651, 1\.652, 1\.653, 1\.658, 1\.659, 1\.660, 1\.661, 1\.662, 1\.904, 1\.910, 1\.931, 1\.932, 2\.101, 2\.102, 2\.111, 2\.113, 2\.116, 2\.117, 2\.118, 2\.120, 2\.121, 2\.122, 2\.124, 2\.125, 2\.126, 2\.132, 2\.135, 2\.151, 2\.152, 2\.153, 2\.154, 2\.159, 2\.201, 2\.202, 2\.203, 2\.204, 2\.205, 2\.206, 2\.207, 2\.208, 2\.209, 2\.212, 2\.214, 2\.215, 2\.216, 2\.251, 2\.252, 2\.255, 2\.256, 2\.257, 2\.301, 2\.351, 2\.352, 2\.353, 2\.356, 2\.401, 2\.403, 2\.408, 2\.409, 2\.410, 2\.411, 2\.414, 2\.415, 2\.501, 2\.503, 2\.504, 2\.651, 2\.652, 2\.653, 2\.658, 2\.659, 2\.660, 2\.661, 2\.662, 2\.904, 2\.910, 2\.931, 2\.932, 3\.101, 3\.102, 3\.126, 3\.127, 3\.129, 3\.201, 3\.202, 3\.205, 3\.206, 3\.207, 3\.211, 3\.212, 3\.251, 3\.301, 3\.351, 3\.352, 3\.353, 3\.356, 3\.503, 3\.651, 3\.652, 3\.653\.

Para buscar o “CFOP” no registro C190 da EFD verificar no campo 3 \(CFOP\)\.

Para buscar o “Valor” no registro C190 da EFD verificar no campo 11 \(VL\_IPI\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor do IPI__ dos documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o Valor do IPI, descrito no tópico [2\.1](#_2.1_–_Recuperação)\.

__ENERGIA ELÉTRICA/COMUNICAÇÃO \(ENTRADA\)__

\(RN03\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590 \(1\.253, 1\.254, 1\.302, 1\.303, 1\.304, 1\.305, 1\.306, 2\.253, 2\.254, 2\.302, 2\.303, 2\.304, 2\.305, 2\.306\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor Contábil__ dos documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\) e [2\.4](#_2.4_–_Recuperação) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação)  e [2\.4](#_2.4_–_Recuperação)\.

__TRANSPORTES \(PARCELA NÃO UTILIZADA\)__

__\(ENTRADA\)__

\(RN04\)

7\.1\.4\.1 \- Somar campo 3 \(VL\_INF\_ADIC\) quando o campo 2 \(COD\_INF\_ADIC\) do Registro __E115 __da EFD for o código de ajuste MG000007\.

7\.1\.4\.2 \- Somar campo 5 \(VL\_OPR\) dos Registros C190, C790 e D190 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C790 e D190 \(1\.354, 1\.355, 2\.354, 2\.355, 3\.354, 3\.355\)\.

7\.1\.4\.3 \- Deverão ser somados VL\_INF\_ADIC referente ao subitem 7\.1\.4\.1 e VL\_OPR referente ao subitem 7\.1\.4\.2\. Ou seja, o valor do campo 04 será VL\_INF\_ADIC \+ VL\_OPR\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor da Informação Adicional__ \(VLR\_INF\_ADIC\) dos  Registros de Valores Declaratórios, de acordo com regras descritas nos tópico [2\.12](#_2.12_–_Recuperação) \(E115\), adicionando os critérios:

- Código da Informação Adicional \(COD\_INF\_ADIC\) = MG000007\.

Recuperar o __Valor Contábil__ dos documentos de ENTRADA, de acordo com regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\) , [2\.3\.3](#_2.3.3_Recuperação_das) \(C790\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco, vide lista ao lado\.

Somar o __Valor da Informação Adicional__ \+ __Valor Contábil\.__

__SUBCONTRATAÇÃO DE SERVIÇO DE TRANSPORTE  \(ENTRADA\)__

\(RN05\)Regra aplicável aos tipos: Especial e Transportador\.

Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo  “Subcontratação Serviço de Transporte \(Entradas\)"\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

__ATIVO IMOBILIZADO \(ENTRADA\)__

\(RN06\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190 e D590 para os valores com os seguintes CFOP: \- campo 3 \(CFOP\) dos Registros C190, C590, D190 e D590 \(1\.406, 1\.551, 1\.552, 1\.553, 1\.554, 1\.555, 2\.406, 2\.551, 2\.552, 2\.553, 2\.554, 2\.555, 3\.551, 3\.553\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__MATERIAL DE USO E CONSUMO __

__\(ENTRADA\)__

\(RN07\)Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, D190 e D590 \(1\.407, 1\.556, 1\.557, 2\.407, 2\.556, 2\.557, 3\.556\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__OUTRAS \- ENTRADAS__

\(RN08\)Somar campo 5 \(VL\_OPR\) dos Registros C190/D190/C590/ D590 para os valores com os seguintes CFOP: \- campo 3 \(CFOP\) dos Registros C190/D190/C590/D590 \(1\.128, 1\.131, 1\.213, 1\.414, 1\.415, 1\.454 1\.505, 1\.506, 1\.601, 1\.602, 1\.603, 1\.604, 1\.605, 1\.657 1\.663, 1\.664, 1\.901, 1\.902, 1\.903, 1\.904 1\.905, 1\.906, 1\.907, 1\.908, 1\.909, 1\.911, 1\.912, 1\.913, 1\.914, 1\.915, 1\.916, 1\.917, 1\.918, 1\.919, 1\.920, 1\.921, 1\.922, 1\.923, 1\.924, 1\.925, 1\.926, 1\.933, 1\.934, 1\.949, 2\.128, 2\.131, 2\.213, 2\.414, 2\.415, 2\.454, 2\.505, 2\.506, 2\.603, 2\.657,  2\.663, 2\.664, 2\.901, 2\.902, 2\.903, 2\.904, 2\.905, 2\.906, 2\.907, 2\.908, 2\.909, 2\.911, 2\.912, 2\.913, 2\.914, 2\.915, 2\.916, 2\.917, 2\.918, 2\.919, 2\.920, 2\.921, 2\.922, 2\.923, 2\.924, 2\.925, 2\.933, 2\.934, 2\.949, 3\.128, 3\.930, 3\.949\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de ENTRADA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.2](#_2.2_–_Recuperação) \(C590\), [2\.4](#_2.4_–_Recuperação) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.2](#_2.2_–_Recuperação) , [2\.4](#_2.4_–_Recuperação) e [2\.6](#_2.6_–_Recuperação)

__AJUSTE \- ENTRADAS__

\(RN09\)

7\.1\.9\.1 \- Regra aplicável aos tipos: Regular e Especial\.

7\.1\.9\.2 \- Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo  “Ajuste Entradas"\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

__EXTRAORDINÁRIAS \- ENTRADAS__

\(RN10\)

7\.1\.10\.1 \- Regra aplicável aos tipos: Regular e Especial\.

7\.1\.10\.2 \- Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo  “Extraordinárias Entradas"\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

<a id="Rn11"></a>__TOTAL DAS EXCLUSÕES \- ENTRADAS__

\(RN11\)

7\.1\.11\.1 \- Regra aplicável aos tipos Regular e Especial: Somar os valores das RN01, RN02, RN03, RN04, RN05, RN06, RN07, RN08, RN09 e RN010\.

7\.1\.11\.2 \- Regra aplicável ao tipo Transportador: somar os valores das RN05 e RN10\.

Somatório dos valores das Entradas mencionados acima:

\- PARCELA DO ICMS RETIDO POR SUBSTITUIÇÃO TRIBUTÁRIA

\- PARCELA DO IPI QUE NÃO INTEGRE A BASE DE CÁLCULO DO ICMS

\- ENERGIA ELÉTRICA/COMUNICAÇÃO

\- TRANSPORTES \(PARCELA NÃO UTILIZADA\)

\- SUBCONTRATAÇÃO DE SERVIÇO DE TRANSPORTE  

\- ATIVO IMOBILIZADO

\- MATERIAL DE USO E CONSUMO 

\- OUTRAS – ENTRADAS

\- AJUSTE – ENTRADAS

\- EXTRAORDINÁRIAS \- ENTRADAS

### <a id="_Toc139647367"></a>5\.2\.2 – Exclusão do VAF – Saídas

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Saídas__

__PARCELA DO ICMS RETIDO POR SUBSTITUIÇÃO TRIBUTÁRIA __

__\(SAÍDAS\)__

\(RN12\) Campos 9 \(VL\_ICMS\_ST\) dos registros C190, C590 e C790 da EFD e 10 \(VL\_ICMS\_ST\) do registro C690 para os CFOP \- campo 3 \(CFOP\) dos Registros C190, C590, C690 e C790: 5\.101, 5\.102, 5\.103, 5\.104, 5\.105, 5\.106, 5\.109, 5\.110, 5\.111, 5\.112, 5\.113, 5\.114, 5\.115, 5\.116, 5\.117, 5\.118, 5\.119, 5\.120, 5\.122, 5\.123, 5\.124, 5\.125, 5\.129, 5\.132, 5\.151, 5\.152, 5\.153, 5\.155, 5\.156, 5\.159, 5\.160, 5\.201, 5\.202, 5\.205, 5\.206, 5\.207, 5\.208, 5\.209, 5\.214, 5\.215, 5\.216, 5\.251, 5\.252, 5\.253, 5\.254, 5\.255, 5\.256, 5\.257, 5\.258, 5\.301, 5\.302, 5\.303, 5\.304, 5\.305, 5\.306, 5\.307, 5\.360, 5\.401, 5\.402, 5\.403, 5\.405, 5\.408, 5\.409, 5\.410, 5\.411, 5\.414, 5\.415, 5\.451, 5\.452, 5\.453, 5\.455, 5\.456, 5\.501, 5\.502, 5\.503, 5\.651, 5\.652, 5\.653, 5\.654, 5\.655, 5\.656, 5\.657, 5\.658, 5\.659, 5\.660, 5\.661, 5\.662, 5\.667, 5\.904, 5\.910, 6\.101, 6\.102, 6\.103, 6\.104, 6\.105, 6\.106, 6\.107, 6\.108, 6\.109, 6\.110, 6\.111, 6\.112, 6\.113, 6\.114, 6\.115, 6\.116, 6\.117, 6\.118, 6\.119, 6\.120, 6\.122, 6\.123, 6\.124, 6\.125, 6\.129, 6\.132, 6\.151, 6\.152, 6\.153, 6\.155, 6\.156, 6\.159, 6\.160, 6\.201, 6\.202, 6\.205, 6\.206, 6\.207, 6\.208, 6\.209, 6\.214, 6\.215, 6\.216, 6\.251, 6\.252, 6\.253, 6\.254, 6\.255, 6\.256, 6\.257, 6\.258, 6\.301, 6\.302, 6\.303, 6\.304, 6\.305, 6\.306, 6\.307, 6\.401, 6\.402, 6\.403, 6\.404, 6\.408, 6\.409, 6\.410, 6\.411, 6\.414, 6\.415, 6\.451, 6\.452, 6\.453, 6\.455, 6\.456, 6\.501, 6\.502, 6\.503, 6\.651, 6\.652, 6\.653, 6\.654, 6\.655, 6\.656, 6\.657, 6\.658, 6\.659, 6\.660, 6\.661, 6\.662, 6\.667, 6\.904, 6\.910, 7\.129, 7\.212, 7\.504\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor do ICMS\-ST__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.3\.2](#_‘2.3.2_Recuperação_das) \(C690\), [2\.3\.3](#_2.3.3_Recuperação_das) \(C790\) e que atendam aos códigos CFOPs determinados na regra do Fisco, vide lista ao lado\.

Totalizar o __Valor do ICMS\-ST__, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.3\.2](#_‘2.3.2_Recuperação_das), [2\.3\.3](#_2.3.3_Recuperação_das)\.

__PARCELA DO IPI QUE NÃO INTEGRE A BASE DE CÁLCULO DO ICMS \(SAÍDAS\)__

\(RN13\) Campo 11 \(VL\_IPI\) do Registro C190 da EFD para os CFOP \- campo 3 \(CFOP\) do Registro C190: \(5\.101, 5\.102, 5\.103, 5\.104, 5\.105, 5\.106, 5\.109, 5\.110, 5\.111, 5\.112, 5\.113, 5\.114, 5\.115, 5\.116, 5\.117, 5\.118, 5\.119, 5\.120, 5\.122, 5\.123, 5\.124, 5\.125, 5\.129, 5\.132, 5\.151, 5\.152, 5\.153, 5\.155, 5\.156, 5\.159, 5\.160, 5\.201, 5\.202, 5\.205, 5\.206, 5\.207, 5\.208, 5\.209, 5\.214, 5\.215, 5\.216, 5\.251, 5\.252, 5\.253, 5\.254, 5\.255, 5\.256, 5\.257, 5\.258, 5\.301, 5\.302, 5\.303, 5\.304, 5\.305, 5\.306, 5\.307, 5\.401, 5\.402, 5\.403, 5\.405, 5\.408, 5\.409, 5\.410, 5\.411, 5\.414, 5\.415, 5\.451, 5\.452, 5\.453, 5\.455, 5\.456, 5\.501, 5\.502, 5\.503, 5\.651,5\.652, 5\.653, 5\.654, 5\.655, 5\.656, 5\.657, 5\.658, 5\.659, 5\.660, 5\.661, 5\.662, 5\.667, 5\.904, 5\.910, 5\.927, 5\.928, 6\.101, 6\.102, 6\.103, 6\.104, 6\.105, 6\.106, 6\.107, 6\.108, 6\.109, 6\.110, 6\.111, 6\.112, 6\.113, 6\.114, 6\.115, 6\.116, 6\.117, 6\.118, 6\.119, 6\.120, 6\.122, 6\.123, 6\.124, 6\.125, 6\.129, 6\.132, 6\.151, 6\.152, 6\.153, 6\.155, 6\.156, 6\.159, 6\.160, 6\.201, 6\.202, 6\.205, 6\.206, 6\.207, 6\.208, 6\.209, 6\.214, 6\.215, 6\.216, 6\.251, 6\.252, 6\.253, 6\.254, 6\.255, 6\.256, 6\.257, 6\.258, 6\.301, 6\.302, 6\.303, 6\.304, 6\.305, 6\.306, 6\.307, 6\.401, 6\.402, 6\.403, 6\.404, 6\.408, 6\.409, 6\.410, 6\.411, 6\.414, 6\.415, 6\.451, 6\.452, 6\.453, 6\.455, 6\.456 6\.501, 6\.502, 6\.503, 6\.651, 6\.652, 6\.653, 6\.654, 6\.655, 6\.656, 6\.657, 6\.658, 6\.659, 6\.660, 6\.661, 6\.662, 6\.667, 6\.904, 6\.910, 7\.129, 7\.212, 7\.504\)\.

Regra aplicável aos tipos: Regular e Especial\.

Campo disponível para edição pelo contribuinte\.

Recuperar o __Valor do IPI__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\) e que atendam aos códigos CFOPs determinados na regra do Fisco, vide lista ao lado\.

Totalizar o Valor do IPI, descrito no tópico [2\.1](#_2.1_–_Recuperação)\.

__TRANSP\. INICIADOS EM OUTROS PAÍSES/UF/ MUNICIPAL/AÉREO DE PASSAGEIRO __

__\(SAÍDAS\)__

\(RN14\) Somar campo 5 \(VL\_OPR\) dos Registros C190/D190/ D390 e campo 11 \(VL\_OPR\) do Registro D300 para os valores com os seguintes CFOP: \- campo 3 \(CFOP\) dos Registros C190/D190/D390 e campo 8 \(CFOP\) do D300: \(5\.932, 6\.932\)\.

Regra aplicável aos tipos: Especial e Transportador\.

Campo disponível para edição pelo contribuinte\.

Recuperar __Valor Contábil__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\), [2\.6](#_2.6_–_Recuperação) \(D190\) e [2\.8](#_2.8_–_Recuperação) \(D390\), [2\.9](#_2.9_–_Recuperação) \(D300\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.6](#_2.6_–_Recuperação), [2\.8](#_2.8_–_Recuperação), [2\.9](#_2.9_–_Recuperação)\.

__ATIVO IMOBILIZADO __

__\(SAÍDAS\)__

\(RN15\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP: \- campo 3 \(CFOP\) Registros C190, C590 e D590 \(5\.412, 5\.551, 5\.552, 5\.553, 5\.554, 5\.555, 6\.412, 6\.551, 6\.552, 6\.553, 6\.554, 6\.555, 7\.551, 7\.553\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das)\.

__MATERIAL DE USO E CONSUMO __

__\(SAÍDAS\)__

\(RN16\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590 e D590 para os valores com os seguintes CFOP \- campo 3 \(CFOP\) dos Registros C190, C590 e D590: \(5\.413, 5\.556, 5\.557, 6\.413, 6\.556, 6\.557, 7\.556\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das)\.

__OUTRAS \- SAÍDAS__

\(RN17\) Somar campo 5 \(VL\_OPR\) dos Registros C190, C590, D190 e D590 para os valores com os seguintes CFOP: \- campo 3 \(CFOP\) dos Registros C190, C590, D190 e D590 \(5\.131, 5\.213, 5\.414, 5\.415, 5\.454, 5\.504, 5\.505, 5\.601, 5\.602, 5\.603, 5\.605, 5\.606, 5\.657, 5\.663, 5\.664, 5\.665, 5\.666, 5\.901, 5\.902, 5\.903, 5\.904, 5\.905, 5\.906, 5\.907, 5\.908, 5\.909, 5\.911, 5\.912, 5\.913, 5\.914, 5\.915, 5\.916, 5\.917, 5\.918, 5\.919, 5\.920, 5\.921, 5\.922, 5\.923, 5\.924, 5\.925, 5\.926, 5\.929, 5\.931, 5\.933, 5\.934, 5\.949, 6\.131, 6\.213, 6\.414, 6\.415, 6\.454 6\.504, 6\.505, 6\.603, 6\.657, 6\.663, 6\.664, 6\.665, 6\.666, 6\.901, 6\.902, 6\.903, 6\.904, 6\.905, 6\.906, 6\.907, 6\.908, 6\.909, 6\.911, 6\.912, 6\.913, 6\.914, 6\.915, 6\.916, 6\.917, 6\.918, 6\.919, 6\.920, 6\.921, 6\.922, 6\.923, 6\.924, 6\.925, 6\.929, 6\.931, 6\.933, 6\.934, 6\.949, 7\.210, 7\.930, 7\.949\)\.

Regra aplicável aos tipos: Regular e Especial\.

Recuperar __Valor Contábil__ dos documentos de SAÍDA de acordo com as regras descritas nos tópicos [2\.1](#_2.1_–_Recuperação) \(C190\),  [2\.3\.1](#_2.3.1_Recuperação_das) \(C590\), [2\.5\.1](#_2.5.1_Recuperação_das) \(D590\) e [2\.6](#_2.6_–_Recuperação) \(D190\) e que atendam aos códigos CFOPs determinados na regra do Fisco\.

Totalizar o valor contábil, descrito nos tópicos [2\.1](#_2.1_–_Recuperação),  [2\.3\.1](#_2.3.1_Recuperação_das), [2\.5\.1](#_2.5.1_Recuperação_das) e [2\.6](#_2.6_–_Recuperação)\.

__AJUSTE \- SAÍDAS__

\(RN18\)

7\.1\.18\.1 \- Regra aplicável aos tipos: Regular e Especial\.

7\.1\.18\.2 \- Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo  “Ajuste Saídas"\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

__EXTRAORDINÁRIAS \- SAÍDAS__

\(RN19\) 

7\.1\.19\.1 \- Regra aplicável aos tipos: Regular e Especial\.

7\.1\.19\.2 \- Valor informado pelo contribuinte\.

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo  “Extraordinárias Saídas"\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

<a id="Rn20"></a>__TOTAL DAS EXCLUSÕES \- SAÍDAS__

\(RN20\)

7\.1\.20\.1 \- Regra aplicável ao tipo Regular: somar os valores das RN12, N13, RN15, RN16, RN17, RN18 e RN19\.

7\.1\.20\.2 \- Regra aplicável ao tipo e Especial: somar os valores das RN12, RN13, RN14, RN15, RN16, RN17, RN18 e RN19\.

7\.1\.20\.3 \- Regra aplicável ao tipo Transportador: somar os valores da RN14 e RN19\.

Somatório dos valores das Entradas mencionados acima:

\- PARCELA DO ICMS RETIDO POR SUBSTITUIÇÃO TRIBUTÁRIA

\- PARCELA DO IPI QUE NÃO INTEGRE A BASE DE CÁLCULO DO ICMS

\- TRANSP\. INICIADOS EM OUTROS PAÍSES/UF/ MUNICIPAL/AÉREO DE PASSAGEIRO

\- ATIVO IMOBILIZADO

\- MATERIAL DE USO E CONSUMO 

\- OUTRAS – SAÍDAS

\- AJUSTE – SAÍDAS

\- EXTRAORDINÁRIAS \- SAÍDAS

# <a id="_Quadro_VAF"></a><a id="_Toc139647368"></a>Quadro VAF

## <a id="_Toc139647369"></a>6\.1 – Layout

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                                VAF                                               |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                        DESCRIÇÃO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|SAIDAS                                                                                     2466018|

|ENTRADAS                                                                                   3240005|

|OUTRAS ENTRADAS                                                                                 12|

|TOTAL DAS ENTRADAS                                                                         3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|VAF                                                                                        \-773999|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

## <a id="_Toc139647370"></a>6\.2 – Gravação dos Campos

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

<a id="Rn21"></a>__SAÍDAS__

\(RN21\)

7\.1\.21\.1 \- Regra aplicável aos tipos Regular e Especial: somar os valores das RN39, RN42, RN43, RN46 e subtrair o valor da RN20\.

7\.1\.21\.2 \- Regra aplicável ao tipo Transportador: somar os valores da RN37, RN42 e subtrair os valores das RN11 e RN20\.

Verificar o campo “Tipo de Contribuinte” informado na tela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)

Se “Tipo de Contribuinte” = Regular ou Especial, calcular o valor das SAÍDAS  conforme segue:

RN39 \+ RN42 \+ RN43 \+ RN46 – RN20

Onde:

\- RN39: [Total das Saídas](#Rn39) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN42: [Saídas – Autuações Fiscais](#Rn42)  do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN43: [Saídas \- Ajuste de Transferência](#Rn43) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN46: [Saídas \- Transporte Tomado](#Rn46) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

\- RN20: [Total das Exclusões \- Saídas](#Rn20) do Quadro Exclusão do VAF \- Saídas \(tópico [5\.2](#_5.2_–_Gravação)\);

Se “Tipo de Contribuinte” = Transportador, calcular o valor das SAÍDAS pela seguinte regra:

RN37 \+ RN42 – RN11 – RN20

Onde:

\- RN37: [Transportes](#Rn37) do Quadro Resumo das Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN42: [Saídas – Autuações Fiscais](#Rn42) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

E subtrair dos valores abaixo:

\- RN11: [Total das Exclusões \- Entradas](#Rn11) do Quadro Exclusão do VAF \- Entradas \(tópico [5\.2](#_5.2_–_Gravação)\);

\- RN20: [Total das Exclusões \- Saídas](#Rn20) do Quadro Exclusão do VAF \- Saídas \(tópico [5\.2](#_5.2_–_Gravação)\);

<a id="Rn22"></a>__ENTRADAS__

\(RN22\)

7\.1\.22\.1 \- Regra aplicável aos tipos Regular e Especial: somar os valores das RN32, RN40, RN41 e subtrair os valores das RN44 e RN11\.

7\.1\.22\.2 \- Regra aplicável ao tipo Transportador: aplicar a seguinte fórmula considerando os valores das regras de negócio: \(RN21\) \* 0,2\.

Verificar o campo “Tipo de Contribuinte” informado na tela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)

Se “Tipo de Contribuinte” = Regular ou Especial, calcular o valor das ENTRADAS conforme segue:

RN32 \+ RN40 \+ RN41 \- RN44 \- RN11

Onde:

\- RN32: [Total das Entradas](#Rn32) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN40: [Entradas – Autuações Fiscais](#Rn40) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN41: [Entradas \- Ajuste de Transferência](#Rn41) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN44: [Entradas \- Produtos Agropecuários/ Hortifruitgranjeiros](#Rn44)  do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN11: [Total das Exclusões \- Entradas](#Rn11) do Quadro Exclusão do VAF \- Entradas \(tópico [5\.2](#_5.2_–_Gravação)\);

Se “Tipo de Contribuinte” = Transportador, calcular o valor das ENTRADAS pela seguinte regra:

Campo [SAÍDAS](#Rn21) \(RN21\) multiplicado por 0,2

<a id="Rn23"></a>__OUTRAS ENTRADAS__

\(RN23\)

7\.1\.23\.1 \- Tipo Regular: aplicar a seguinte fórmula considerando os valores das regras de negócio: RN44 \+ RN45 \+ RN46 \+ RN47\.

7\.1\.23\.2 \- Tipo Especial: aplicar a seguinte fórmula considerando os valores das regras de negócio: RN44 \+ RN45 \+ RN46 \+ RN47 \+ RN126 \+ RN128\.

7\.1\.23\.3 \- Campo disponível para edição pelo contribuinte Tipo Especial\.

7\.1\.23\.4 \- Tipo Transportador: aplicar a seguinte fórmula considerando os valores das regras de negócio: RN21 \- RN22\.

Verificar o campo “Tipo de Contribuinte” informado na tela dos Dados Iniciais da VAF   \(menu DAMEF\-EFD Fiscal >> Dados Iniciais\)\.

Se “Tipo de Contribuinte” = __Regular__, calcular o valor conforme segue:

RN44 \+ RN45 \+ RN46 \+ RN47

Onde:

\- RN44: [Entradas \- Produtos Agropecuários/ Hortifruitgranjeiros](#Rn44) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN45: [Entradas – Geração Energia Elétrica p/ Consumo Próprio](#Rn45) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN46: [Saídas \- Transporte Tomado](#Rn46) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

\- RN47: [Saídas – Cooperativas](#Rn47) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

Se “Tipo de Contribuinte” = __Especial__ calcular o valor conforme segue:

RN44 \+ RN45 \+ RN46 \+ RN47 \+ RN126 \+ RN128

Onde:

\- RN44: [Entradas \- Produtos Agropecuários/ Hortifruitgranjeiros](#Rn44) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN45: [Entradas – Geração Energia Elétrica p/ Consumo Próprio](#Rn45) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN46: [Saídas \- Transporte Tomado](#Rn46) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

\- RN47: [Saídas – Cooperativas](#Rn47) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

__\[MFS\-45263\]__

\- RN126: [Mudança de Município](#Rn126) do quadro Detalhamento de Outras Entradas \(Tópico [7\.2](#_7.2_–_Gravação)\)

\- RN128: [Outras Entradas a Detalhar por Município](#Rn128) do quadro Detalhamento de Outras Entradas \(Tópico [7\.2](#_7.2_–_Gravação)\)

Se “Tipo de Contribuinte” = Transportador calcular o valor conforme segue:

[SAÍDAS](#Rn21) \(RN21\) \- [ENTRADAS](#Rn22) \(RN22\)

<a id="Rn24"></a>__TOTAL DAS ENTRADAS__

\(RN24\)

7\.1\.24\.1 \- Somar os valores das regras RN22 e RN23\.

7\.1\.24\.2 \- Regra aplicável aos tipos: Regular, Transportador e Especial\.

Para todos os Tipos de Contribuinte, calcular o valor conforme segue:

[ENTRADAS](#Rn22) \(RN22\) e [OUTRAS ENTRADAS](#Rn23) \(RN23\)

__VAF__

\(RN25\)

7\.1\.25\.1 \- Aplicar a seguinte fórmula considerando os valores das regras: RN21 \- RN24\.

7\.1\.25\.2 \- Regra aplicável aos tipos: Regular, Transportador e Especial\.

Para todos os Tipos de Contribuinte, calcular o valor conforme segue:

[SAIDAS](#Rn21) \(RN21\) – [TOTAL DAS ENTRADAS](#Rn24) \(RN24\)

# <a id="_Quadro_VAF_-"></a><a id="_Toc139647371"></a>Quadro VAF \- Detalhamento de Outras Entradas 

## <a id="_Toc139647372"></a>7\.1 – Layout

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                           VAF \- Detalhamento de Outras Entradas                                  |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                       PRODUTOS AGROPECUÁRIOS                                     |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|12345 – JUIZ DE FORA                                                                       2466018|

|012010 – BELO HORIZONTE                                                                    3240005|

|01119 – OURO PRETO                                                                              12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                  GERAÇÃO DE ENERGIA ELÉTRICA                                     |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|12345 – JUIZ DE FORA                                                                       2466018|

|012010 – BELO HORIZONTE                                                                    3240005|

|01119 – OURO PRETO                                                                              12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                       TRANSPORTE TOMADO                                          |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|12345 – JUIZ DE FORA                                                                       2466018|

|012010 – BELO HORIZONTE                                                                    3240005|

|01119 – OURO PRETO                                                                              12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                                       COOPERATIVAS                                               |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|12345 – JUIZ DE FORA                                                                       2466018|

|012010 – BELO HORIZONTE                                                                    3240005|

|01119 – OURO PRETO                                                                              12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                           PRESTAÇÃO DE SERVIÇO DE TRANSPORTE RODOVIÁRIO                          |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|XXXXX                                                                                      2466018|

|YYYYYYYY                                                                                   3240005|

|ZZZZZZZZZZZZZZZZ                                                                                12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                          OUTRAS ENTRADAS A DETALHAR POR MUNICÍPIO                                |

|                        MUNICIPIO                                                    VALOR        |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|12345 – JUIZ DE FORA                                                                       2466018|

|012010 – BELO HORIZONTE                                                                    3240005|

|01119 – OURO PRETO                                                                              12|

|TOTAL                                                                                      3240017|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

## <a id="_7.2_–_Gravação"></a><a id="_Toc139647373"></a>7\.2 – Gravação dos Campos

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Produtos Agropecuários__

__\(Município e Valor\)__

\(RN117\)

7\.1\.117\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Produtos\_Agropecuarios”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.117\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.117\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.117\.4 \- Os valores devem ser informados em conformidade com o disposto no subitem 3\.1 da Resolução nº 5\.369, de 2020\.

7\.1\.117\.5 \- O totalizador é a soma dos valores por município\.

7\.1\.117\.6 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 116\.

7\.1\.117\.7 \- Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Produtos\_Agropecuarios”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Produtos Agropecuários__

__\(Total\)__

\(RN116\)

7\.1\.116\.1 \- Valor da regra RN84\.

7\.1\.116\.2 \- Regra aplicável aos tipos: Regular e Especial\.

Total do valor apresentado para Produtos Agropecuários\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Produtos\_Agropecuarios”\.

__Geração de Energia Elétrica__

__\(Município e Valor\)__

\(RN119\)

7\.1\.119\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Geracao\_de\_Energia\_Eletrica”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.119\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.119\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.119\.4 \- Os valores devem ser informados em conformidade com o disposto no subitem 3\.5 da Resolução nº 5\.369, de 2020\.

7\.1\.119\.5 \- O totalizador é a soma dos valores por município\.

7\.1\.119\.6 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 118\.

7\.1\.119\.7 \- Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Geracao\_de\_Energia\_Eletrica”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Geração de Energia Elétrica__

__\(Total\)__

\(RN118\)

7\.1\.118\.1 \- Valor da RN85\.

7\.1\.118\.2 \- Regra aplicável aos tipos: Regular e Especial\.

Total do valor apresentado para Geração de Energia Elétrica\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando o critério:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Geracao\_de\_Energia\_Eletrica”\.

__Transporte Tomado__

__\(Município e Valor\)__

\(RN121\)

7\.1\.121\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Transporte\_Tomado”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.121\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.121\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.121\.4 \- Os valores devem ser informados em conformidade com o disposto no subitem 3\.2 da Resolução nº 5\.369, de 2020\.

7\.1\.121\.5 \- O totalizador é a soma dos valores por município\.

7\.1\.121\.6 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 120\.

7\.1\.121\.7 \- Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Transporte\_Tomado”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Transporte Tomado__

__\(Total\)__

\(RN120\)

7\.1\.120\.1 \- Valor da RN112\.

7\.1\.120\.2 \- Regra aplicável aos tipos: Regular e Especial\.

Total do valor apresentado para Transporte Tomado\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Transporte\_Tomado”\.

__Cooperativas__

__\(Município e Valor\)__

\(RN123\)

7\.1\.123\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Cooperativas”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.123\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.123\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.123\.4 \- Os valores devem ser informados em conformidade com o disposto no subitem 3\.3 da Resolução nº 5\.369, de 2020\.

7\.1\.123\.5 \- O totalizador é a soma dos valores por município\.

7\.1\.123\.6 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 122\.

Não surtiu efeitos \- Redação original:

“7\.1\.123\.6 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 120\.”

7\.1\.123\.7 \- Regra aplicável aos tipos: Regular e Especial\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Cooperativas”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Cooperativas__

__\(Total\)__

\(RN122\)

7\.1\.122\.1 \- Valor da RN114\.

7\.1\.123\.2 \- Regra aplicável aos tipos: Regular e Especial\.

Total do valor apresentado para Cooperativas\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Cooperativas”\.

__Prestação de Serviço de Transporte Rodoviário__

__\(Município e Valor\)__

\(RN125\)

7\.1\.125\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.125\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.125\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.125\.4 \- Os valores devem ser informados em conformidade com o disposto no subitem 3\.4 da Resolução nº 5\.369, de 2020\.

7\.1\.125\.5 \- O totalizador é a soma dos valores por município e não é editável\.

7\.1\.125\.6 \- Ocorrendo a edição de município\(s\) e valor\(es\) pelo contribuinte, o valor do totalizador deverá ser igual ao valor do campo 124\.

7\.1\.125\.7 \- Regra aplicável ao tipo: Transportador\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

__Prestação de Serviço de Transporte Rodoviário__

__ \(Total\)__

\(RN124\)

7\.1\.124\.1 \- Valor do __campo 23__ DAMEF\.

7\.1\.124\.2 \- Regra aplicável ao tipo: Transportador\.

Total do valor apresentado para Prestação de Serviço de Transporte Rodoviário\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Prestacao\_de\_Servico\_de\_Transporte\_Rodoviario”\.

Obs: A regra de preenchimento deste campo não se baseia na regra RN124 da Portaria 175/2020, pois esta é o próprio campo OUTRAS ENTRADAS, que já é demonstrado no Quadro VAF \([tópico 6](#_Quadro_VAF)\)\.

Este campo apresenta o total do valor da Prestação de Serviço de Transporte Rodoviário\.

O cliente deverá comparar o valor total da da Prestação de Serviço de Transporte Rodoviário com o valor do campo 23 \- VAF \- OUTRAS ENTRADAS\. Caso sejam diferentes, proceder o rateio conforme explicado na regra RN125a \(veja abaixo\)\. 

\(RN125a\)

7\.1\.125\.8\.1 \- Este campo tem por finalidade ajustar os valores por município porventura informados imprecisamente no Registro 1400 da EFD, de modo que o somatório de todos os municípios corresponda ao VAF apurado, mantendo\-se a proporcionalidade quanto aos valores informados no Registro 1400\.

7\.1\.125\.8\.2 \- Para cada valor por município informado no campo 125, dividir pelo valor total da RN125 e multiplicar o resultado pelo valor da RN124\.

7\.1\.125\.8\.3 \- Os valores são calculados considerando 10 casas decimais\.

7\.1\.125\.8\.4 \- Os municípios e respectivos valores não são editáveis\.

7\.1\.125\.8\.5 \- O totalizador é a soma dos valores por município e não é editável\.

7\.1\.125\.8\.6 \- Regra aplicável ao tipo: Transportador

Não estamos implementando a regra RN125a\. Cabe ao cliente comparar o valor do campo OUTRAS ENTRADAS do quadro VAF \([tópico 6](#_Quadro_VAF)\) com o total do valor da Prestação de Serviço de Transporte Rodoviário \(campo acima\)\. 

Caso haja divergência, o cliente fará o rateio descrito na RN125a no próprio sistema da SEFAZ\-MG \(Sistema Integrado de Administração da Receita Estadual – SIARE\)\.

__Outras Entradas a Detalhar por Município__

__\(Município e Valor\)__

\(RN129\)

7\.1\.129\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Outras\_Entradas\_a\_Detalhar\_por\_Município”, agrupado por código do município cujo campo é o 3 \(MUN\)\.

7\.1\.129\.2 \- Os municípios são disponíveis para edição pelo contribuinte\.

7\.1\.129\.3 \- Os valores agrupados por município são disponíveis para edição pelo contribuinte\.

7\.1\.129\.4 \- Na hipótese de o contribuinte editar os campos, informando município\(s\) e valor\(es\), observar, no que couber, os critérios dispostos no subitem 3\.6 da Resolução nº 5\.369, de 2020\.

7\.1\.129\.5 \- O totalizador é a soma dos valores por município\.

7\.1\.129\.5 \- O totalizador não é editável e seu valor deverá ser igual ao do campo 128\.

7\.1\.129\.6 \- Regra aplicável ao tipo: Especial\.

Recuperar o __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Outras\_Entradas\_a\_Detalhar\_por\_Municipio”\.

Totalizar o valor por Código de Município\.

Apresentar no relatório a relação dos valores totalizados para cada município \(demonstrar cod \+desc do município\)\.

Os campos do registro 1400 mencionados nesta regra \(Valor Total, Código da Tabela de Itens p/ o Índice de Participação dos Municípios\) são referentes à tela de Manutenção do 1400, disponível no módulo Sped >> EFD – Escrituração Fiscal Digital, menu Geração >> Manutenção >> Registro 1400\.

<a id="Rn128"></a>__Outras Entradas a Detalhar por Município__

__ \(Total\)__

\(RN128\)

7\.1\.128\.1 \- Somar campo 4 \(VALOR\) do Registro 1400 da EFD onde o campo 2 \(COD\_ITEM\_IPM\) for igual a “Outras Entradas a Detalhar por Município”\.

7\.1\.128\.2 \- Campo não editável\.

7\.1\.128\.3 \- Regra aplicável ao tipo: Especial\.

Total do valor apresentado para Outras Entradas a Detalhar por Município\.

Somatório do __Valor Total__ \(VLR\_Total\) dos Registros 1400, de acordo com regras descritas nos tópico [2\.13](#_2.13_–_Recuperação) \(1400\), adicionando os critérios:

- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) = “Outras\_Entradas\_a\_Detalhar\_por\_Municipio”\.

<a id="Rn126"></a>__MUDANÇA DE MUNICÍPIO__

__\(Total\)__

RN126

7\.1\.126\.1 \- Considerar o valor resultante da RN147 dividido por doze e multiplicar pelo número de meses no município até a mudança: \(RN147 / 12\) \* nº de meses até a mudança\.

7\.1\.126\.2 \- Se o valor for negativo, atribuir zero\.

7\.1\.126\.3 \- Atribuir ao município anterior à mudança valor proporcional ao número de meses em que o contribuinte esteve nele estabelecido\.

Para a proporção, o mês em que ocorreu a mudança será considerado para o município anterior à mudança\. 7\.1\.126\.4 \- Regra aplicável ao tipo: Especial\.

RN147 = RN21 \- RN22 \- RN146\.

RN146 = RN44 \+ RN45 \+ RN46 \+ RN47 \+ RN128

Recuperação da Tela de Manutenção dos Dados Iniciais da VAF – campo “Mês em que o Estabelecimento mudou de Município”\.

Menu: DAMEF\-EFD FISCAL >> Dados Iniciais

Segundo a Portaria 175/20, esse campo deve ser preenchido com:

\(RN147 / 12\) \* nº de meses até a mudança

Onde:

- RN147 = RN21 \- RN22 \- RN146\.
- RN146 = RN44 \+ RN45 \+ RN46 \+ RN47 \+ RN128
- no de meses até a mundação = campo “Mês em que o Estabelecimento mudou de Município” da tela Dados Iniciais\.

Cada uma das regras acima \(RN21, RN22\.\.\.\) se refere a um campo demonstrado nos quadros desse relatório\. Segue a identificação das regras x campos:

\- RN21 : [SAÍDAS](#Rn21) do Quadro VAF \(tópico [6\.2](#_Quadro_VAF)\);

\- RN22: [ENTRADAS](#Rn22) do Quadro VAF\(tópico [6\.2](#_Quadro_VAF)\);

\- RN44: [Entradas \- Produtos Agropecuários/ Hortifruitgranjeiros](#Rn44) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN45: [Entradas – Geração Energia Elétrica p/ Consumo Próprio](#Rn45)  do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\);

\- RN46: [Saídas \- Transporte Tomado](#Rn46) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

\- RN47: [Saídas – Cooperativas](#Rn47) do Quadro Resumo das Entradas e Saídas \(tópico [4\.2](#_4.2_–_Gravação)\); 

 \- RN128: [Outras Entradas a Detalhar por Município \(Total\)](#Rn128) deste quadro\.

RN127

\(VAF \- DETALHAMENTO DE OUTRAS ENTRADAS \- MUDANÇA DE MUNICÍPIO\) 

Campo 126 da DAMEF

7\.1\.127\.1 \- Total do valor da RN126, precedida do código \(SEF\) e nome do município anterior à mudança\.

7\.1\.127\.2 \- Regra aplicável ao tipo: Especial\.

Não estamos implementando a regra RN127, pois não gera valor objetivando conferência da DAMEF gerada pelo sistema SIARE da Receita Estadual\. 

\(RN130\)

\(DETALHAMENTO DE OUTRAS ENTRADAS \- RESUMO POR MUNICÍPIO\)

7\.1\.130\.1 \- Somar os valores por município das regras conforme a seguinte fórmula: RN117 \+ RN119 \+ RN121 \+ RN123 \+ RN127 \+ RN129\.

7\.1\.130\.2 \- Valor deverá ser igual ao valor do campo 23\.

7\.1\.130\.3 \- Regra aplicável aos tipos: Regular e Especial\.

Não estamos implementando esta regra por dois motivos:

\- Se trata apenas de uma totalização por município dos valores já apresentados no quadro de Detalhamento de Outras Entradas\. Ou seja, o total por município dos dos valores de Produtos Agropecuários \(RN117\), Geração de Energia Elétrica \(RN119\), Transporte Tomado \(RN121\), Cooperativas \(RN123\), Outras Entradas a Detalhar por Município \(RN129\) e RN127\.

\- Como não geramos a RN127, o valor calculado por nós não bateria com o calculado pelo sistema SIARE da Receita Estadual\. 

\- Como a RN130 não leva em consideração o Prestação de Serviço de Transporte Rodoviário \(RN125\), isso poderia ser objeto de dúvidas, parecendo um erro\.

# <a id="_Quadro_Totalização_do"></a><a id="_Toc139647374"></a>Quadro Totalização do Inventário 

\[MFS\-45264\]

## <a id="_Toc139647375"></a>8\.1 – Layout

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|                           Totalização do Inventario                                              |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|DESCRIÇÃO                                                                               VALOR     |

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|Inventário Inicial                                                                         2466018|

|Inventário Final                                                                           3240005|

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

## <a id="_Toc139647376"></a>8\.2 – Gravação dos Campos

__Campo__

__Regra do Fisco \(Portaria 175/2020\)__

__Regra de preenchimento__

__Inventário Inicial__

\(RN48\)

7\.1\.48\.1 \- Campo 3 \(VL\_INV\) do Registro H005 da EFD\.

7\.1\.48\.2 \- Buscar a informação na EFD de fevereiro do ano base, Campo 2 \(DT\_INV\) do Registro H005 da EFD, que é a referente a dezembro do ano\-base\. No Campo 4 \(MOT\_INV\) deverá ser código “01”, ou seja, só aplica o código “01” para o campo 48\.

7\.1\.48\.3 \- Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar o __Valor Total__ \(VLR\_TOT\) do Inventário \(SAFX52 campo 14\), de acordo com regras descritas no tópico [2\.14](#_2.14_–_Recuperação) \(H005\)\.

Sumarizar o “Valor Total”, consolidando por Data do Inventário\.

Apresentar o Valor Total que foi consolidado para a Data do Inventário Inicial\.

__Inventário Final__

\(RN49\)

7\.1\.49\.1 \- Campo 3 \(VL\_INV\) do Registro H005 da EFD\.

7\.1\.49\.2 \- Buscar a informação na EFD de fevereiro do ano subsequente ao ano\-base \(ano\-base \+1\), Campo 2 \(DT\_INV\) do Registro H005 da EFD, que é a referente a dezembro do ano\-base\. No Campo 4 \(MOT\_INV\) deverá ser código “01” e o Campo 02 \(DT\_INV\) deverá ter o valor “3112AAAA” onde AAAA corresponde ao ano\-base\.

7\.1\.49\.3 \- Quando a empresa encerra as atividades a informação de estoque constará do mês de encerramento, normalmente na última EFD entregue\. A informação de encerramento de atividade será identificada no Campo 4 \(MOT\_INV\) código “03”\.

7\.1\.49\.4 \- Regra aplicável aos tipos: Regular, Transportador e Especial\.

Recuperar o __Valor Total__ \(VLR\_TOT\) do Inventário \(SAFX52 campo 14\), de acordo com regras descritas no tópico [2\.14](#_2.14_–_Recuperação) \(H005\)\.

Sumarizar o “Valor Total”, consolidando por Data do Inventário\.

Apresentar o Valor Total que foi consolidado para a Data do Inventário Final\.

# <a id="_Relatório_de_Conferência"></a><a id="_Toc139647377"></a>Relatório de Conferência  

A geração da VAF\-MG disponibiliza um relatório em arquivo Excel, demonstrando documento a documento que entrou na composição dos valores apresentados nos quadros:

\- Quadro das Operações e Prestações de Entradas e Saídas

\- Quadro Resumo das Entradas e Saídas

\- Quadro de Exclusão do VAF

\- Quadro VAF

A regra de recuperação desses documentos está definida nos tópicos 2\.1, 2\.2, 2\.3, 2\.3\.1, 2\.3\.2, 2\.3\.3, 2\.4, 2\.5, 2\.5\.1, 2\.5\.2, 2\.5\.3, 2\.6, 2\.7, 2\.8, 2\.9, 2\.10, 2\.11, 2\.12, 2\.13, 2\.14\.

Este relatório é gerado quando o flag “Gerar Relatório com Detalhamento Nota a Nota em arquivo xls” está marcado na tela de geração\. Caso selecionado, é gerado um arquivo para cada estabelecimento selecionado na tela de geração\.

	1

## <a id="_Toc139647378"></a>9\.1 – Layout

Este é um esboço do relatório a ser gravado em arquivo excel\.  O conjunto total de campos que compõe o relatório está descrito no tópico 8\.2\.

|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|

|  Empresa |ESTAB | Exercício | Registro |Data      |Num Docto|CFOP | Modelo | Tipo Movto | Valor Contabil | Vlr ICMSS| Vlr IPI| blá blá blá | 

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|12121212 |1101 |  55    | ENTRADA    |            0,00|      0,00|    0,00|                   

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|13333333 |2151 |  55    | ENTRADA    |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|14444444 |3201 |  55    | ENTRADA    |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|12121212 |5101 |  02    | SAÍDA      |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|12121212 |6111 |  06    | SAÍDA      |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|12121212 |5151 |  06    | SAÍDA      |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C190     |dd/mm/aaaa|12121212 |5151 |  06    | SAÍDA      |            0,00|      0,00|    0,00|

|  xxx     |xxxxxx| AAAA      | C197     |dd/mm/aaaa|12121212 |5151 |  06    | SAÍDA      |            0,00|      0,00|    0,00|

                                          

## <a id="_Toc139647379"></a>9\.2 – Regra de Geração do Relatório

Cada tipo de Registro da EFD\-Fiscal apresentado na coluna “Registro” possui sua especifidade quanto ao preenchimento das demais colunas\.

Coluna do Relatório

Regra de Preenchimento

Empresa

Empresa de login\.

Estab

Estabelecimento selecionado na tela de Geração

Exercício

Ano exercício informado na tela de Geração\.

Registro

Preencher com:

\- “C190”: para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- “C590”: para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- “D590”: para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- “D190”: para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme regra descrita no tópico [2\.6](#_2.6_–_Recuperação)\.

\- “D300”: para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- “D410”: para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- “C590”: para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- “C690”: para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- “D590”: para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- “D690”: para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- “C790”: para os Registros do Arquivo Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- “D696”: para os Registros do Arquivo Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- “C490”: para os Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- “D390”: para os Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- “C197”: para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

\- “E115”: para os Registros E115 \(Informações Adicionais da Apuração \- Valores Declaratórios\) recuperados conforme regra descrita no tópico [2\.12](#_2.12_–_Recuperação)\.

\- “1400”: para os Registros 1400 recuperados conforme regra descrita no tópico [2\.13](#_2.13_–_Recuperação)\.

MFS\-45264

\- “H005”: para os Registros de Inventário recuperados conforme regra descrita no tópico [2\.14](#_2.14_–_Recuperação)\.

Os registros de inventários serão demonstrados no relatório de conferência agrupados por Data do Inventário, Indicador e Código do Produto\.

Data

Preencher com:

\- Data Fiscal da X07 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Data Fiscal da X07 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Data Fiscal da X07 para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- Data Fiscal da X07 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme tópico [2\.6](#_2.6_–_Recuperação)\.

\- Data Fiscal da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- Data Fiscal da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- Data Fiscal da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Data Fiscal da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Data Fiscal da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Data Fiscal da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Último dia do Mês/Ano dos Registros do Arquivo do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- Último dia do Mês/Ano dos Registros do Arquivo do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- Data Emissão da X993 dos Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- Data Emissão da X993 dos Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- Data Fiscal da X07 para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

\- Data Inicial da Tabela dos Registros E115/1925 \(Valores Declaratórios\) recuperada conforme regra descrita no tópico [2\.12](#_2.12_–_Recuperação)\.

\- Data Inicial da Tabela dos Registros 1400 recuperados conforme regra descrita no tópico [2\.13](#_2.13_–_Recuperação)\.

MFS\-45264

\- Data do Inventário da X52, para os registros de Inventário recuperados conforme regra descrita no tópico [2\.14](#_2.14_–_Recuperação)\.

Os registros de inventários serão demonstrados no relatório de conferência agrupados por Data do Inventário, Indicador e Código do Produto\.

Num Docto

Preencher com:

\- Num Doc/Fis da X07 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Num Doc/Fis da X07 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Num Doc/Fis da X07 para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- Num Doc/Fis da X07 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme tópico [2\.6](#_2.6_–_Recuperação)\.

\- Num Doc/Fis da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- Num Doc/Fis da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- Num Doc/Fis da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Num Doc/Fis da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Num Doc/Fis da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Num Doc/Fis da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Num COO da X993 dos Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- Num COO da X993 dos Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- Num Doc/Fis da X07 para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

CFOP

Preencher com:

\- Cod\. CFO da X07/X08/X09 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Cod\. CFO da X07/X08/X09 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Cod\. CFO da X07/X08        para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- Cod\. CFO da X07/X08/X09 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados no tópico [2\.6](#_2.6_–_Recuperação)\.

\- Cod\. CFO da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- Cod\. CFO da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- Cod\. CFO da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Cod\. CFO da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Cod\. CFO da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Cod\. CFO da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Cód\. CFO dos Registros de Detalhamento do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- Cód\. CFO dos Registros de Detalhamento do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- Cód\. CFO da X994 dos Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- Cód\. CFO da X994 dos Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

Modelo 

Preencher com:

\- Cod\. Modelo da X07 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Cod\. Modelo da X07 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Cod\. Modelo da X07 para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- Cod\. Modelo da X07 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme tópico [2\.6](#_2.6_–_Recuperação)\.

\- Cod\. Modelo da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- Cod\. Modelo da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- Cod\. Modelo da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Cod\. Modelo da X42 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Cod\. Modelo da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Cod\. Modelo da X42 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Cod\. Modelo dos Registros do Arquivo do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- Cod\. Modelo dos Registros do Arquivo do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- Cod\. Modelo NF do Equipamento ECF da X2087 dos Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- Cod\. Modelo NF do Equipamento ECF da X2087 dos Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- Cod\. Modelo da X07 para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

Tipo Movto

Preencher com:

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme tópico [2\.6](#_2.6_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- fixo = “Saída” para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- fixo = “Saída” para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- fixo = “Saída” para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- fixo = “Saída” para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- fixo = “Saída” para os Registros do Arquivo do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- fixo = “Saída” para os Registros do Arquivo do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- fixo = “Saída” para Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- fixo = “Saída” para Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- “Entrada” ou “Saída”, com base no campo Movto E/S da X07 para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

Valor Contábil

Preencher com:

\- Valor Total do Documento Fiscal da X07 ou Valor Contábil Item da X08  ou Valor Total do Serviço da X09 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Valor Total do Documento Fiscal da X07 ou Valor Contábil Item da X08  ou Valor Total do Serviço da X09 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Valor Total do Documento Fiscal da X07 ou Valor Contábil Item da X08 para os documentos fiscais de entrada de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.4](#_2.4_–_Recuperação)\.

\- Valor Total do Documento Fiscal da X07 ou Valor Contábil Item da X08  ou Valor Total do Serviço da X09 para os documentos fiscais de modelos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 67, 63 recuperados conforme tópico [2\.6](#_2.6_–_Recuperação)\.

\- Valor Total do Documento Fiscal da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.9](#_2.9_–_Recuperação)\.

\- Valor Total do Documento Fiscal da X07 para os documentos fiscais de modelos 13, 14, 15, 16 recuperados conforme regra descrita no tópico [2\.10](#_2.10_–_Recuperação)\.

\- Valor do Serviço \- Valor do desconto \+ Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Valor do Serviço \- Valor do desconto \+ Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Valor do Serviço \- Valor do desconto \+ Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Valor do Serviço \- Valor do desconto \+ Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Valor do Serviço dos Registros de Detalhamento do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- Valor do Serviço dos Registros de Detalhamento do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

\- Valor Total Líquido da X994 dos Cupons Fiscais de modelos 02, 2D, 60 recuperados conforme regra descrita no tópico [2\.7](#_2.7_–_Recuperação)\.

\- Valor Total Líquido da X994 dos Cupons Fiscais de modelos 13, 14, 15, 16 e 2E recuperados conforme regra descrita no tópico [2\.8](#_2.8_–_Recuperação)\.

\- Valor Total  \(VLR\_TOTAL\) da Tabela dos Registros 1400 recuperados conforme regra descrita no tópico [2\.13](#_2.13_–_Recuperação)\.

Valor do Serviço

Preencher com:

\- Valor do Serviço da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Valor do Serviço da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Valor do Serviço da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Valor do Serviço da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

\- Valor do Serviço do Registro de Detalhamento do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

\- Valor do Serviço dos Registros de Detalhamento do Convênio 115 de modelos 21, 22 recuperados conforme regra descrita no tópico [2\.5\.3](#_2.5.3_Recuperação_das)\.

Valor do Desconto

Preencher com:

\- Valor do Desconto da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Valor do Desconto da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Valor do Desconto da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Valor do Desconto da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

Valor Outras Despesas

Preencher com:

\- Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.1](#_2.5.1_Recuperação_das)\.

\- Valor Outras Despesas da X43 para os documentos fiscais de saída \(Utilities\) de modelos 21, 22 recuperados conforme regra do tópico [2\.5\.2](#_2.5.2_Recuperação_das)\.

Valor do ICMSS

Preencher com:

\- Valor do ICMS\-ST da X07 ou Valor do ICMS\-ST da X08 para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

\- Valor do ICMS\-ST da X07 ou Valor do ICMS\-ST da X08 para os documentos fiscais de entrada de modelos 06, 66 recuperados conforme regra descrita no tópico [2\.2](#_2.2_–_Recuperação)\.

\- Valor do ICMS\-ST da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.1](#_2.3.1_Recuperação_das)\.

\- Valor do ICMS\-ST da X43 para os documentos fiscais de saída \(Utilities\) de modelos 06, 66 recuperados conforme regra do tópico [2\.3\.2](#_‘2.3.2_Recuperação_das)\.

\- Valor do ICMS\-ST do Registro de Detalhamento do Convênio 115 de modelos 06 recuperados conforme regra descrita no tópico [2\.3\.3](#_2.3.3_Recuperação_das)\.

Valor do IPI

Preencher com:

\- Valor do IPI da X07 ou Valor do IPI da X08  para os documentos fiscais de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.1](#_2.1_–_Recuperação)\.

Valor do ICMS

Preencher com:

\- Valor do ICMS da X113 para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

Código do Ajuste \(C197\)

Preencher com:

\-Código do Ajuste \(COD\_AJUSTE\_SPED\) para os Ajustes/Outros valores do Lançamento Fiscal das notas de modelos 01, 1B, 04, 55, 65 recuperados conforme regra descrita no tópico [2\.11](#_2.11_–_Recuperação)\.

Valor da Informação Adicional \(E115\)

Preencher com:

\- Valor da Informação Adicional  da Tabela dos Registros E115/1925 \(Valores Declaratórios\) recuperada conforme regra descrita no tópico [2\.12](#_2.12_–_Recuperação)\.

 Código da Informação Adicional \(E115\)

Preencher com:

\- Código da Informação Adicional  da Tabela dos Registros E115/1925 \(Valores Declaratórios\) recuperada conforme regra descrita no tópico [2\.12](#_2.12_–_Recuperação)\.

Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(1400\) \(COD\_ITEM\_PART\_MUN\)

\- Código da Tabela de Itens p/ o Índice de Participação dos Municípios \(COD\_ITEM\_PART\_MUN\) dos Registros 1400 recuperados conforme regra descrita no tópico [2\.13](#_2.13_–_Recuperação)\.

Munícípio \(1400\)

\- Código e Descrição do Município dos Registros 1400 recuperados conforme regra descrita no tópico [2\.13](#_2.13_–_Recuperação)\.

Produto do Inventário \(ind\-cod\)

MFS\-45264

Preencher com o Indicador \+ “\-“ \+ Código do Produto da X52, para os registros de Inventário recuperados conforme regra descrita no tópico [2\.14](#_2.14_–_Recuperação)\.

Os registros de inventários serão demonstrados no relatório de conferência agrupados por Data do Inventário, Indicador e Código do Produto\.

Valor Total do Inventário

MFS\-45264

Preencher com o __Valor Total__ \(VLR\_TOT\) do Inventário \(SAFX52 campo 14\), recuperado de acordo com regras descritas no tópico [2\.14](#_2.14_–_Recuperação) \(H005\)\.

O “Valor Total” apresentado deve ser consolidando por Data do Inventário, Indicador e Código do Produto\.

= = = = = =

 

