# MTZ_Tela_Demonstrativo_Apuracao_por_Tipo_Contribuicao

- **Fonte:** MTZ_Tela_Demonstrativo_Apuracao_por_Tipo_Contribuicao.docx
- **Modificado:** 2020-07-29
- **Tamanho:** 79 KB

---

THOMSON REUTERS

Matriz da tela/relatório Demonstrativo da Apuração por Tipo de Contribuição 

__Localização:__

__Módulo__: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

__Menu__:      Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Contribuição

                 Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Contribuição

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3169\-GE13D

Telas de Emissão do Relatório Demonstrativo da Apuração e alteração da tela Geração dos Registros

Criação das telas de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Crédito’’ e ‘’Por Tipo de Contribuição’’\. Também na tela de Geração dos Registros a inclusão do parâmetro ‘’Gerar Relatórios Demonstrativos da Apuração no Período Informado’’

OS3631

Telas de Emissão do Relatório Demonstrativo da Apuração 

Alteração da tela de Emissão do Relatório Demonstrativo da Apuração ‘’Por Tipo de Contribuição’’ – inclusão dos filtros Cód\. Situação Tributária e Cód\. Registro\.

OS4316\-B

Marcos G\. de Paula

Duplicação da tela e relatório com seleção da apuração por SCP\.

MFS\-20227

Julyana Perrucini

Inclusão dos campos “Vlr Tot\. Ajustes Acréscimo BC”, “Vlr Tot\. Ajustes Redução BC” e “Vlr BC da Contribuição” nos registros M210, e M610 

Os registros filhos dos M210, e M610 hoje não são apresentados no relatório\. Logo os novos registros filhos M215 e M615 não serão demonstrados no relatório\.

MFS37761

Liliane V\. Assaf

Para o TAX ONE habilitar apenas a opção sintético, pois o relatório analítico passa a ser disponibilizado na opção de menu “Relatórios 🡪 Demonstrativo da Apuração \(Crédito / Contribuição / Natureza da Receita\)”

Sumário

[1\.	TELA A SER DESENVOLVIDA	1](#_Toc46856087)

[1\.1\.	Diagrama de Casos de Uso	1](#_Toc46856088)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	1](#_Toc46856089)

[1\.1\.1\.1\.1\.	Fluxo Principal	1](#_Toc46856090)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	1](#_Toc46856091)

[2\.	Regras dos Campos	1](#_Toc46856092)

[3\.	Sugestão de Layout	1](#_Toc46856093)

[4\.	Relatório	1](#_Toc46856094)

# <a id="_Toc46856087"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc46856088"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc46856089"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema\.

__Pré\- Condições__

Estar logado no produto MasterSAF DW\.

__Pós\-Condições__

Não se aplica\.

<a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a>

### <a id="_Toc46856090"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc46856091"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc46856092"></a>Regras dos Campos 

__Localização da tela:__ 

	Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

	Menu: Obrigações >> Demonstrativos >> Emissão de relatório Demonstrativo de Apuração >> Por tipo de Contribuição ou Obrigações SCP >> Demonstrativos >> Emissão do Relatório de Demonstrativo da Apuração >> Por Tipo de Contribuição

	As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros\. No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, *Código da SCP\**, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout\.

	Será apresentada uma caixa de seleção para listar as empresas que já foram apuradas e o usuário deverá selecionar para qual deseja emitir o relatório\.

*\*Caso seja gerado por SCP\.*

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Tipo

Texto

S

S

Formato: 

Radio Button Group

Default: 

Habilitado

Sintético

Deve ser informado o tipo de relatório que é emitido\.

__Conteúdo:__

- Analítico 
- Sintético

__Considerações: __

- Se o usuário optar em emitir o Relatório Analítico, após a emissão é apresentado cada documento fiscal gerado no registro A100/A170, C100/C170 e C180/C181/C185 vinculado a composição no detalhamento do tipo de contribuição\. Para os registros C381, C385, C481, C485, C491, C495, C601, C605, D201, D205, D300, D350, D601, D605, F100 e F200 são apresentadas cada linha de registro vinculado à composição no detalhamento do tipo de contribuição\.
- Se o usuário optar em emitir o Relatório Sintético, após emissão é apresentado à totalização dos valores de cada registro vinculado a composição do tipo de contribuição\.
- \[MFS37761\]:

No TAX ONE o relatório Analítico passou a ser gerado através da opção de menu “Relatórios >> Demonstrativo de Apuração \(Crédito/Contribuição/Natureza da Receita\)”\. Desta forma, apenas a opção Sintético fica habilitada para utilização\. No DW as duas opções Sintético e Analítico permanecem habilitadas\.

OS4316\-B

MFS37761

Tipo Contribuição

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

Esse campo é utilizado para filtrar o código da natureza da base de crédito gerado nos registros M210 e M610 que deve ser apresentado no relatório\. 

__Conteúdo:__

01 \- Contribuição não\-cumulativa apurada a alíquota básica 

02 \- Contribuição não\-cumulativa apurada a alíquotas diferenciadas

03 \- Contribuição não\-cumulativa apurada a alíquota por unidade de medida de produto

04 \- Contribuição não\-cumulativa apurada a alíquota básica – Atividade Imobiliária

31 \- Contribuição apurada por substituição tributária

32 \- Contribuição apurada por substituição tributária – Vendas à Zona Franca de Manaus

51 \- Contribuição cumulativa apurada a alíquota básica

52 \- Contribuição cumulativa apurada a alíquotas diferenciadas

53 \- Contribuição cumulativa apurada a alíquota por unidade de medida de produto

54 \- Contribuição cumulativa apurada a alíquota básica – Atividade Imobiliária

OS4316\-B

Cód\. Sit\. Tributária

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

Esse campo é utilizado para filtrar o código da situação tributária referente ao PIS/COFINS gerado nos registros M210 e M610 que deve ser apresentado no relatório\. 

Conteúdo:

< > 	        Opção Branco

01 \- Operação Tributável com Alíquota Básica

02 \- Operação Tributável com Alíquota Diferenciada

03 \- Operação Tributável com Alíquota por Unidade de Medida de Produto

04 \- Operação Tributável Monofásica \- Revenda a Alíquota Zero

05 \- Operação Tributável por Substituição Tributária

06 \- Operação Tributável a Alíquota Zero

07 \- Operação Isenta da Contribuição

08 \- Operação sem Incidência da Contribuição

09 \- Operação com Suspensão da Contribuição

49 \- Outras Operações de Saída

OS3631

Cód\. Registro Utilizado para Detalhar a Apuração

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

Esse campo é utilizado para filtrar o código de registro utilizado para detalhar a apuração\.

Conteúdo:

< > 	        Opção Branco

A100/A170 – Nota Fiscal de Serviço

C100/C170 – Nota Fiscal \(Código 01, 1B, 04\) e NF\-e \(Código 55\)

C180/C181/C185 – Consolidação de Notas Fiscais Eletrônicas Emitidas pela Pessoa Jurídica \(Código 55\) – Operações de Vendas

C380/C381/C385 – Nota Fiscal de Venda a Consumidor \(Código 02\) – Consolidação de Documentos Emitidos

C405/C481/C485 – Redução Z \(Códigos 02 e 2D\)

C490/C491/C495 – Consolidação de Documentos Emitidos por ECF \(Códigos 02, 2D\)

C600/C601/C605 – Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica \(Código 06\), Nota Fiscal/Conta de Fornecimento d’água

C800 – Cupom Fiscal Eletrônico \(Código 59\)

D200/D201/D205 – Resumo da Escrituração Diária – Prestação de Serviços de Transportes \(Códigos 07, 08, 8B, 09, 10, 11, 26, 27 e 57\)

D300 – Resumo da Escrituração Diária \(Código 13, 14, 15, 16 e 18\)

D350 – Resumo Diário de Cupom Fiscal Emitido por ECF \(Códigos 2E, 13, 14, 15 e 16\)

D600/D601/D605 – Consolidação da Prestação de Serviço de Comunicação \(Código 21\) e de Serviço de Telecomunicação \(Código 22\)

F100 – Demais Documentos e Operações Geradoras de Contribuição e Créditos

F200 – Operações da Atividade Imobiliária – Unidade Imobiliária Vendida

OS3631

Registro

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado e Todos Marcados

Deve informar qual o registro da apuração da contribuição abaixo que deve ser apresentado no relatório\. Para identificar os registros vinculados a composição do detalhamento do Tipo de Contribuição é necessário marcar as opções: "M210 e M610’’:

M200 \- Consolidação da Contribuição para o PIS/PASEP do Período

M210 \- Detalhamento da Contribuição para o PIS/PASEP do Período

M600 \- Consolidação da Contribuição para a Seguridade Social \- COFINS do Período 

M610 \- Detalhamento da Contribuição para a Seguridade Social \- COFINS do Período

OS4316\-B

MFS\-20227

# <a id="_Toc46856093"></a>Sugestão de Layout

# <a id="_Toc46856094"></a>Relatório

__Ver documento matriz MTZ\_Relatorio\_de\_Demonstrativo\_da\_Apuracao\_EFD\_PISPASEP\-COFINS\.doc__

