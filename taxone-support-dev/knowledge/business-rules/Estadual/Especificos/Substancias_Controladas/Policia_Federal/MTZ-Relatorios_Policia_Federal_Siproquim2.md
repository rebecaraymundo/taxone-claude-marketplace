# MTZ-Relatorios_Policia_Federal_Siproquim2

- **Fonte:** MTZ-Relatorios_Policia_Federal_Siproquim2.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 82 KB

---

THOMSON REUTERS

Módulo Substâncias Controladas \(Portaria SEF 378/2018 – SC\) 

Relação Mensal dos Movimentos por Classificação de Produto \(Polícia Federal\) 

<a id="_Hlk2155195"></a>__Localização__: Menu Específicos, módulo Substâncias Controladas, <a id="_Hlk24392468"></a>menu Atendimento 🡪 Polícia Federal 🡪 Portaria 240/19 🡪 <a id="_Hlk24453126"></a>Relação Mensal dos Movimentos por Classificação de Produto 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS31706__

Liliane Assaf

Criação do relatório\.

11/11/2019\.\.

Sumário

[1\.	Regras Gerais	2](#_Toc24466221)

[2\.	Layout da Tela	2](#_Toc24466222)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc24466223)

[4\.	Recuperação dos Dados	4](#_Toc24466224)

[5\.	Layout e Preenchimento dos Campos	4](#_Toc24466225)

# <a id="_Toc24466221"></a>Regras Gerais

Este relatório tem por objetivo demonstrar o detalhamento dos movimentos de produtos \(SAFX70\) que são considerados na geração do meio magnético do SIPROQUIM 2\.

Os movimentos aqui demonstrados atendem aos mesmos critérios e regras da geração do meio magnético SIPROQUIM 2\.

# <a id="_Toc24466222"></a>Layout da Tela

Estabelecimento: \[xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \\/\]

Mês/Ano Referência \[MM/AAAA\]

Gerar Registros: 

\[  \] Comercialização Nacional 

\[  \] Comercialização Internacional 

\[  \] Produção

\[  \] Transformação

\[  \] Consumo

\[  \] Fabricação

\[  \] Transporte

\[  \] Armazenamento

Recuperar Informações por: \(o\) Data Movimento

                                              \(  \) Data Emissão

# <a id="_Toc24466223"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

Estabelecimentos

Alfanumérico 

S

S

Lista

Default: sem

Neste campo é exibida a lista de estabelecimentos da Empresa do login para seleção do usuário\.

Apresentar apenas os estabelecimentos que estejam cadastrados para o Tipo de Obrigação = “PF – Polícia Federal”, na Tela de Estabelecimento x Tipo de Obrigação \(tabela SCT\_TP\_OBRIGACAO\)\.

<a id="_Hlk517437550"></a>Mês/Ano Referência

Data

\(mês e ano\) 

S

S

MM/AAAA

Neste campo o usuário informa o período \(mês e ano\) para a geração do arquivo\.

Gerar Registros

Alfanumérico

S

Check\-box

Default: todos os itens desmarcados

Cada opção é um check\-box\. O usuário pode selecionar um ou mais itens\.

🡪 Comercialização Nacional 

🡪 Comercialização Internacional 

🡪 Produção

🡪 Transformação

🡪 Consumo

🡪 Fabricação

🡪 Transporte

🡪 Armazenamento

__Habilitar__ apenas as opções cujos registros estão sendo considerados:

🡪 Comercialização Nacional

🡪 Consumo

🡪 Fabricação

Recuperar Informações por

Alfanumérico 

S

S

RadioButton

Default: Data Emissão

Desabilitado

Este campo é composto pelas seguintes opções:

🡪 Data Movimento

🡪 Data Emissão

Regra:

Caso o parâmetro Comercialização Nacional esteja marcado,

   Habilitar campo

Caso o parâmetro Comercialização Internacional esteja marcado,

  Habilitar o campo 

Caso contrário:

  Desabilitar o campo

# <a id="_Toc506457465"></a><a id="_Toc24466224"></a>Recuperação dos Dados

Será gerado um relatório para o estabelecimento selecionados em tela\.

Origem dos dados:  \- Tabela dos Movimentos dos Produtos \(SAFX70\)

 Critérios da recuperação da movimentação do período:

Mesmos critérios descritos no tópico “__3\.1 Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)”__ do documento matriz “__MTZ\-Geracao\_Meio\_Magnetico\_Policia\_Federal\_Siproquim2__”

Cada registro de movimento de produto será demonstrado individualmente no relatório\.

Esses registros serão organizados de forma agrupada por Classificação de Produto e Código do Tipo de Operação da Obrigação\.

As regras de ordenação e preenchimento das colunas no relatório estão descritas no item a seguir\.

Orientação Técnica:

Utilizar a view SC\_PRE\_V que contempla todos os critérios da recuperação dos movimentos para geração do meio magnético SIPROQUIM 2\.

# <a id="_Toc24466225"></a>Layout e Preenchimento dos Campos 

Layout: vide planilha “__Layout\-Relatorios\-Policia\_Federal\_Siproquim2__”, aba “__Relação Mensal de Movimentos__”\.

Ordenação dos movimentos:

     \- Classificação do Produto

     \- Código do Tipo de Operação da Obrigação

     \- Data Movimento

     \- Número Documento;

     \- Tipo de Operação 

     \-  Produto;

Preenchimento dos campos do relatório:

__Linhas de cabeçalho:__

Primeira linha de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Página do relatório;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Título do relatório \(“Relação Mensal dos Movimentos de Produtos por Classificação de Produto”\); 

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

Período solicitado em tela \(mês e ano\);

__Linha de Agrupamento por Classificação de Produto:__

Classif\. Produto

Código de Classificação de Produto \(COD\_CLASS\_PRD\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

Descrição

Descrição da Classificação de Produto \(DSC\_CLASS\_PRD\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

Código Oficial

Código Oficial da Polícia Federal \(COD\_OFICIAL\_PF\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

Concentração

Concentração \(PERC\_CONCENT\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

Densidade

Densidade \(DENSIDADE\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

Medida

Código de Unidade de medida \(COD\_MEDIDA\) do Cadastro de Classificação do Produto \(SCT\_CLASS\_PRD\)

\(campo COD\_MEDIDA\_CLASS da view SC\_PRE\_V\)

__Linha de Agrupamento por Tipo de Operação da Obrigação \(PF\):__

Tipo de Operação Obrigação \(PF\)

Código \+ Descrição do Tipo de Operação Obrigação \(vide Tela de Cadastro do Tipo de Operação x Tipo Obrigação\)

\(campos COD\_OPER\_OBRIG\_ORIG e DSC\_OPER\_OBRIG da view SC\_PRE\_V\)

__Linhas de detalhamento dos movimentos:__

Data Movimento

Campo “Data Movimento” \(DATA\_MOVTO\) do Movimento do Produto \(SAFX70\)

Data Emissão

Campo “Data Emissão” \(DATA\_EMISSAO\) do Movimento do Produto \(SAFX70\)

Número Documento

Campo “Número do Documento Fiscal” \(NUM\_DOCFIS\) do Movimento do Produto \(SAFX70\)

CNPJ / CPF Pessoa Fis/Jur 

Esta coluna é preenchida com o CNPJ ou CPF do cadastro da pessoa fis/jur do Movimento do Produto \(SAFX70\), da seguinte forma:

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CNPJ

      Preencher o campo com o número do CNPJ devidamente editado \(99\.999\.999/9999\-99\);

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CPF

      Preencher o campo com o número do CPF devidamente editado \(999\.999\.999\-99\);

Se campo “06\-CPF\-CGC” da SAFX04 não preenchido \(nulo\)

      Neste caso, este campo não será preenchido;

\(campo CPF\_CGC da view SC\_PRE\_V\) 

Tipo de Operação

Campo “Tipo Operação” \(TIPO\_OPERACAO\) do Movimento do Produto \(SAFX70\)

Mov\. E/S

Preenchimento de acordo com o campo “Mov\. E/S” \(MOVTO\_E\_S\) do Movimento do Produto \(SAFX70\)\.

\(campo ENTSAI da view SC\_PRE\_V\) 

Preencher com:

 Se o campo ENTSAI da view for ‘E’, então preencher com “Entrada”;

 Se o campo ENTSAI da view for ‘S’, então preencher com “Saída”;

 

Produto \(Gr\-Ind\_cod\)

Campos Grupo \+ Indicador \+ Código do Produto do Movimento do Produto \(SAFX70\)\.

\(campo GRUPO\_PRODUTO, IND\_PRODUTO\_COD\_PRODUTO da view SC\_PRE\_V\)

Qtd

Campo “Quantidade” do Produto \(QTD\_MOVTO\) do Movimento do Produto \(SAFX70\)\.

Unidade de Medida

Código da Medida do Movimento do Produto \(SAFX70\)\.

\(campo COD\_MEDIDA\_X70 da view SC\_PRE\_V\)

Fator de Conversão

Campo “Fator de Conversão” Conversão de Unidade de Medida conforme descrito no tópico “__3\.1 Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)”__ do matriz “__MTZ\-Geracao\_Meio\_Magnetico\_Policia\_Federal\_Siproquim2__”\.

\(campo FATOR da view SC\_PRE\_V\)

Qtd Convertida

Resultado da Multiplicação dos campos “Quantidade do Produto” e “Fator de Conversão”\.

\(campo QTD\_CONV da view SC\_PRE\_V\)

CPF / CNPJ Transportadora

Esta coluna é preenchida com o CNPJ ou CPF do cadastro da Pessoa Fis/Jur Transportadora do Movimento do Produto \(SAFX70\), da seguinte forma:

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CNPJ

      Preencher o campo com o número do CNPJ devidamente editado \(99\.999\.999/9999\-99\);

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CPF

      Preencher o campo com o número do CPF devidamente editado \(999\.999\.999\-99\);

Se campo “06\-CPF\-CGC” da SAFX04 não preenchido \(nulo\)

      Neste caso, este campo não será preenchido;

\(campo CPF\_CGC\_TRANSP da view SC\_PRE\_V\) 

CPF / CNPJ 

Armazém

Esta coluna é preenchida com o CNPJ ou CPF do cadastro da Pessoa Fis/Jur Armazém do Movimento do Produto \(SAFX70\), da seguinte forma:

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CNPJ

      Preencher o campo com o número do CNPJ devidamente editado \(99\.999\.999/9999\-99\);

Se o conteúdo do campo “06\-CPF\-CGC” da SAFX04 for um CPF

      Preencher o campo com o número do CPF devidamente editado \(999\.999\.999\-99\);

Se campo “06\-CPF\-CGC” da SAFX04 não preenchido \(nulo\)

      Neste caso, este campo não será preenchido;

\(campo CPF\_CGC\_ARMAZÉM da view SC\_PRE\_V\) 

Tipo do Frete

Código \+ Descrição do Tipo de Frete \(IND\_TP\_FRETE\) do Movimento do Produto \(SAFX70\)\.

\(campo IND\_TP\_FRETE \+ DSC\_TP\_FRETE da view SC\_PRE\_V\)

__Linha de Total por Tipo de Operação da Obrigação \(PF\):__

Total por Tipo de Operação Obrigação \(PF\)

Código \+ Descrição do Tipo de Operação Obrigação \(vide Tela de Cadastro do Tipo de Operação x Tipo Obrigação\)

\(campos COD\_OPER\_OBRIG\_ORIG e DSC\_OPER\_OBRIG da view SC\_PRE\_V\)

QTD

Total da coluna “QTD”, com base no Mov\. E/S\.

Se “Mov\. E/S” for igual a ‘E’, então soma a quantidade \(QTD\_MOVTO da view SC\_PRE\_V\);

Se “Mov\. E/S” for igual a ‘S’, então subtrai a quantidade \(QTD\_MOVTO da view SC\_PRE\_V\)\.

Apresentar o resultado em valor absoluto\.

QTD Convertida

Total da coluna “QTD Convertida”, com base no Mov\. E/S\.

Se “Mov\. E/S” for igual a ‘E’, então soma a “QTD Convertida” \(QTD\_CONV da view SC\_PRE\_V\)\.

Se “Mov\. E/S” for igual a ‘S’, então subtrai a “QTD Convertida” \(QTD\_CONV da view SC\_PRE\_V\)\.

Apresentar o resultado em valor absoluto\.

= = = = = =

