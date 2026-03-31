# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C186

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C186.docx
- **Modificado:** 2025-11-21
- **Tamanho:** 128 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Processamento do Cálculo ICMS\-ST – Registro C186

__Localização__: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré\-Geraçãoà Ressarcimento ICMS\-ST \(Específico MG\) à Cálculo ICMS\-ST 

Sumário

[1\.	CONTROLE DE ALTERAÇÕES	2](#_Toc37749426)

[2\.	INTRODUÇÃO	3](#_Toc37749427)

[3\.	DOCUMENTOS DE REFERÊNCIA	3](#_Toc37749428)

[4\.	DEFINIÇÃO DAS REGRAS	4](#_Toc37749429)

# <a id="_Toc462320891"></a><a id="_Toc27038219"></a><a id="_Toc37749426"></a>CONTROLE DE ALTERAÇÕES

__Data__

__Demanda__

__Descrição__

__Autor__

17/03/2020

MFS\-33977

Criação do processamento de cálculo das informações de ICMS\-ST para a geração dos registros C180/C185 da EFD\. \(RP00,RP01, RP02,RP03,RP04 e RP05\)

Alessandra Cristina Navatta

03/04/2020

MFS\-35339

Inclusão do cálculo para a geração do registro C430 da EFD\. \(RP00, RP05, RP09, RP10, RP11\)

Alessandra Cristina Navatta

07/04/2020

MFS\-35340

Inclusão do cálculo para a geração do registro 1250 e 1255 da EFD\. \(RP00, RP05, RP012, RP13, RP14, RP18\)

Alessandra Cristina Navatta

16/04/2020

MFS\-36146

Inclusão do cálculo para a geração do registro H030 da EFD\. \(RP00, RP05, RP015, RP16, RP17 e RP18\)

Alessandra Cristina Navatta

12/06/2020

MFS\-38251

[DW \- SPED \- EFD Fiscal \- Declaração de Informações Complementares sujeitas à ST \- MG \- Ajustes para mercadorias em mais de um estoque](http://ent.jira.int.thomsonreuters.com/browse/MFS-38251) \(RP01,RP02\)

Alessandra Cristina Navatta

25/06/2020

MFS\-39378

Ajustes realizados na demanda:

\- Considerar na RP02, a data limite para a recuperação das notas de entrada, ‘campo ‘Pesquisar Notas de Entrada até’\)\. Esta data afeta os registros C185, C330, C430 e H030\) e foi criada na tela Ressarcimento ICMS\-ST \(Específico MG\)\.

\- Criação de log para os registros de Saída \(C185, C330 e C430\) e o de inventário \(H030\) \- RP05;

\- Considerar na recuperação das notas de entrada, para os registros de saída C185, C330, C430 e o de inventário H030, o campo para o cenário de ICMS Não destacado – \(RP02\)\.

Alessandra Cristina Navatta

25/03/2020

08/07/2020

MFS\-35337

Inclusão do cálculo para a geração do registro C330 da EFD\. \(RP00, RP05, RP06, RP07 e RP08\)\.

Foi necessário considerar na recuperação das notas de saída o mesmo agrupamento que é realizado para os registros C321 \(detalhes em RP06\)

Alessandra Cristina Navatta

27/11/2020

MFS46686

RP03: Registros C180, C185:

Alteração na regra de preenchimento do campo 18 \- VLR\_UNIT\_CONV da x296\_info\_compl\_st\_itens\_merc

Liliane Assaf

30/11/2020

MFS47079

Inclusão do tratamento das notas de saídas para fatos geradores presumidos não realizados\. Antes desta MFS, essa rotina contemplava apenas Saídas internas pra Consumidor Final, com regras baseadas no manual do Aspécto Quantitativo\.

Segundo o Anexo XV do RICMS/02 \(artigos 22 a 31\), as notas fiscais de saídas de fato gerador presumido não realizado são operações de:

I \- saída para outra unidade da Federação

II \- saída amparada por isenção ou não\-incidência;

III \- perecimento, furto, roubo ou qualquer outro tipo de perda

Nas operações de saídas de fato gerador presumido não realizado, o contribuinte emissor da nota de saída terá direito a __ressarcimento__\. 

Fazendo um comparativo com as notas fiscais de saídas de operações internas para consumidor final, essas podem gerar __ressarcimento__ ou __complemento__, dependendo de qual seja o maior valor, o da entrada ou da saída, e são apresentadas no registro C185 com código do motivo MG100 ou MG300\.

Para notas de saídas de fato gerador presumido não realizado o fisco estabeleceu que sempre haverá __ressarcimento__ baseado no valor médio ponderado imposto das entradas, independente de qual valor tenha sido maior \(entrada ou saída\)\. Essas notas serão apresentadas no registro C185 com código do motivo MG200\.

A solução já utiliza as parametrizações por CFOP e CFOP/Natureza da Operação para identificar as saída sujeitas a ICMS\-ST\. Mas esta está sendo alterada para que o relacionamento dos CFOP e Naturezas da Operação sejam feitos por operação:

\- Saída Interna para Consumidor Final \(art 31\-A \- Anexo XV do RICMS/02\)

 \- Saída para Outras Unidade da Federação  \(art 23 \- Anexo XV do RICMS/02\)

 \- Saída com Isenção ou não Incidência \(art 23 \- Anexo XV do RICMS/02\)

 \- Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda \(art 23 \- Anexo XV do RICMS/02\)

Com base nessa parametrização, a pré\-geração irá aplicar os tratamentos específicos na geração do C185: 

- para Saída Interna para Consumidor Final \(art 31\-A \- Anexo XV do RICMS/02\) com base no Manual Aspécito Quantitativo;
- para Saídas de fator gerador presumido não realizado, com base no “Manual de Escrituração – Restituição do ICMS ST – Fato Gerador Presumido Não Realizado”\.

Liliane Assaf

08/12/2020

MFS47958

RP02, RP03: Alteração na regra de preenchimento do campo 19\-VLR\_ICMS\_CONV da X296, para considerar o % de Redução de BC parametrizado no produto ou NCM\. 

Essa solicitação veio do Carrefour e em call com CAN, foi dado aceite para realizarmos a alteração\.

Carrefour pediu alteração no campo 10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV do C185, para usar o "% de Redução de BC”\. 

No no 06 \- VL\_UINT\_ICMS\_OP\_CONV do C180 faremos uso dos campos de Valores de ICMS da SAFX08 \(43, 80, 225\), que foi solicitado em call dia 14/12\.

Link da gravação:

01/12: [https://web\.microsoftstream\.com/video/ecc22357\-1f2f\-417e\-9661\-a6e487dd5b15](https://web.microsoftstream.com/video/ecc22357-1f2f-417e-9661-a6e487dd5b15)

14/12:

Liliane Assaf

09/12/2020

MFS47248

RP01, RP02: Utilização do campo 137 – Quantidade Convertida da SAFX08, na geração dos registros C180 e C185\.

Liliane Assaf

04/01/2021

MFS57863

__RP03: Registro C180 – VLR\_UNIT\_CONV:__

Alteração na regra de preenchimento do campo 18 \- VLR\_UNIT\_CONV da x296\_info\_compl\_st\_itens\_merc, para subtrair o valor do ICMS\-ST \(notas de entradas\)\.

Link da gravação do call com Carrefour em 22/12: [https://web\.microsoftstream\.com/video/f2cd7ef3\-db6d\-4dae\-ba40\-5a1c3b4e5e06](https://web.microsoftstream.com/video/f2cd7ef3-db6d-4dae-ba40-5a1c3b4e5e06)

                                                                em 04/01: [https://web\.microsoftstream\.com/video/a3a4ea77\-2e36\-4e67\-b6c9\-d202c778e60f](https://web.microsoftstream.com/video/a3a4ea77-2e36-4e67-b6c9-d202c778e60f) \(no 36min\)

Base Legal: Guia Prático do Sped Fiscal: Registro C180, explicação do campo 05:

__“Campo 05 __\(VL\_UNIT\_CONV\) – __Preenchimento__: informar o valor unitário líquido do item/produto \(considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto\)\. O valor unitário do campo 05 não inclui o ICMS ST na aquisição de participante substituto ou nas hipóteses em que o informante é responsável pela substituição\.”

Liliane Assaf

09/06/2021

MFS\-67654

Alteração no Cálculo das Médias Diárias \+ relatório \([RP00B](#RP00B)\)

Ajuste na regra de ressarcimento/complemento dos registros:

\-  C185 \(RP02, RP03, RP05\) – passar a considerar o novo Cálculo da Média Ponderada e passa a gerar o código motivo MG000\.

\-  C330 \(RP06, RP07\)

\-  C430 \(RP09, RP10\)

Base Legal: Manual Aspecto Quantitativo versão 05 – 2021 e Manual Fato Gerador Presumido Não Realizado versão 02 – 2021\.

Liliane Assaf

09/06/2021

MFS\-62563

Inclusão do registro C181 \(geração e relatório\) \(RP18\)

Base Legal: Manual Aspecto Quantitativo versão 05 – 2021 e Manual Fato Gerador Presumido Não Realizado versão 02 – 2021\.

         

Liliane Assaf

18/06/2021

MFS\-67660

Alteração no 1255 – RP13\.

Base Legal: Manual Aspecto Quantitativo versão 05 – 2021 e Manual Fato Gerador Presumido Não Realizado versão 02 – 2021\.

Liliane Assaf

18/06/2021

MFS\-64570

Inclusão do registro C186 \(geração e relatório\) \(RP19\)

Base Legal: Manual Aspecto Quantitativo versão 05 – 2021 e Manual Fato Gerador Presumido Não Realizado versão 02 – 2021\.

Liliane Assaf

27/07/2021

MFS\-67658

Inclusão da geração dos registros C195/C197 e Lançamentos na Apuração do ICMS\-ST  

Base Legal: Manual Aspecto Quantitativo versão 05 – 2021 e Manual Fato Gerador Presumido Não Realizado versão 02 – 2021\.

Liliane Assaf

19/08/2021

MFS\-70215

Inclusão da regra para desconsiderar as notas de devolução interestadual que serão geradas no registro C185, conforme a resposta de orientação da SEFAZ\-MG\.

Andréa Rocha

03/09/2021

MFS\-58456

Inclusão do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Tela de Geração e tratamento na geração dos registros C180, C186, H030, Cálculo do Valores Médios do Inventário e Cálculo da Média Ponderada do Diária Produto\.

Liliane Assaf

06/10/2021

MFS\-73772

Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada e suas devoluções, na geração do registro C186\.

Andréa Rocha

07/03/2023

MFS511653

Criação check\-box “Gerar Relatórios de Conferência” na tela da pré\-geração e aplicação na geração do relatório do registro C186 \(vide RP19\)

Liliane Assaf

09/08/2024

MFS665846

Inclusão do tratamento do valor do FCP retido \(FECEP Regime Fonte\) na geração dos registros C180,  C186, e no Cálculo do Valores Médios do Inventário\.  As regras para os registros C181 e C185 não serão alteradas, porque os seus valores vêm da tabela da média ponderada\.

Andréa Rocha

19/11/2025

MFS977849

Inclusão de um parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado\.  Esse parâmetro está sendo criado separado do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)”, porque o parâmetro já existente está vinculado a atualização do DATA MART, e os campos de ICMS não destacado e não escriturado não são gravados com o valor do FECEP embutido durante a equalização\.

Andréa Rocha

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc37749427"></a>INTRODUÇÃO* *

Este documento contém as regras de geração do registro C186\.

# <a id="_Toc27038221"></a><a id="_Toc37749428"></a>DOCUMENTOS DE REFERÊNCIA

*MTZ\-EFD\_Tela\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_NCM\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Produtos\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Saida\_CFOP\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Saida\_Natureza\_Operacao\.docx*

# DOCUMENTOS DA PRE\-GERAÇÃO 

*A especificação da Pré\-Geração foi criada em um único arquivo \(MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx\)\. Mas com o tempo este documento ficou bastante grande, dificultando sua manutenção\. Sendo assim, segregamos as regras nos seguintes documentos:*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx*

*Documento principal, contém as seguintes regras: RP00 – regra geral, RP00A \- regra de cálculo para Valores Médios do Inventário e RP00B \- Regra da Média Ponderada dos Valores Médios do Produto no Período\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C180\_C185\.docx*

*Documento que contém as regras de geração dos registros C180 e C185 \(RP01, RP02, RP03, RP04, RP05\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C330\.docx*

*Documento que contém as regras de geração dos registros C330 \(RP05, RP06, RP07, RP08\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C430\.docx*

*Documento que contém as regras de geração dos registros C430 \(RP05, RP09, RP10, RP11\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_1250\_1255\.docx*

*Documento que contém as regras de geração dos registros 1250/1255 \(RP05, RP12, RP13, RP14\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_H030\.docx*

*Documento que contém as regras de geração dos registros H030 \(RP05, RP15, RP16, RP17\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C181\.docx*

*Documento que contém as regras de geração dos registros C181 \(RP18\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C186\.docx*

*Documento que contém as regras de geração dos registros C186 \(RP19\)\.*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\_C195\_C197\_Lancto\_P9\_ST\.docx*

*Documento que contém as regras de geração dos registros C195, C197 e lançamentos complementares na Apuração do ICMS\-ST\.*

# <a id="_Toc27038222"></a><a id="_Toc37749429"></a>DEFINIÇÃO DAS REGRAS

__Número__

__Regra__

__Demanda__

RP19

MFS\-64570

Quando o parâmetro __*C186 – Devoluções de Entradas de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\)*__* estiver marcado na tela:* Todos os cálculos realizados por este processo serão armazenados na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV, referente às devoluções de entradas e serão utilizados para a geração do registro C186 do SPED FISCAL\.

O objetivo desta geração é calcular as informações de notas de devolução de entradas, dos produtos sujeitos ao ICMS\-ST, e para isso além da nota de devolução, também deve ser recuperado o documento de entrada referenciado pela devolução\.

A Devolução de Entrada é uma nota de saída carregada na SAFX07/SAFX08\.

A nota de entrada que está sendo devolvida, também está carregada na SAFX07/SAFX08\. 

A associação da nota de devolução com a nota de entrada é feita utilizando os campos de referência da SAFX08 \(117, 118, 119, 102\) são preenchidos com os dados de identificação da nota fiscal de entrada;

*Observação:*

*Não estamos utilizando a tabela de referência SAFX192, pois ela não tem tratamento para devolução de entradas \(o campo “Tipo de Referência” não tem opção de “Devolução \(Saída\) x Documentos de Origem \(Entradas\)\)\.*

*O ressarcimento PR, RS está trabalhando da mesma forma, ou seja, devoluções de entrada com a SAFX08 e devoluções de saídas com a SAFX192 ou SAFX08*\.

__Pré\-Requisito__:

1\) Código do Motivo__ MG400__ deve existir no cadastro do   módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação do ICMS \(SPED FISCAL\) – tabela DWT\_COD\_MOTIVO\_SPED\.

Caso não esteja cadastrado dar mensagem e abortar a geração do registro C186\.

Código MG400 de Motivo de Restituição/Complementação do ICMS não cadastrado, por isso a pré\-geraçao do C186 não será realizada\.

Favor realizar o cadastro no módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação do ICMS \(SPED FISCAL\)\. Favor verificar o manual/help\.

2\) Não pode existir devoluções de entradas inseridas via importação:

Fazer uma consulta na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “2”\);

\- Nota de Saída \(MOVTO\_E\_S = “9”\);

\- IND\_GRAVACAO <> '0', '6','7','8'\. \(caso que foi incluído via digitação ou importação\) então:

Caso a consulta acima retorne registro, dar mensagem e abortar a geração do registro C186\.:

“Existem notas de devolução de entradas importadas através da SAFX308 \- Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\) para o período, por isso a pré\-geraçao do C186 não será realizada\.”

## 1 – Recuperação das Notas Fiscais de Devolução \(norm\_dev = ‘2’/ movto\_e\_s = ‘9’\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__Critérios da recuperação das Notas Fiscais de Devolução: __

__\[MFS70215\]__ Desconsiderar as notas de devolução interestadual parametrizadas para Fato Gerador Presumido Não Realizado, pois estas notas vão ser geradas no registro C185\.

__\[MFS73772\] __ Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada\.

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal – data enquadrada no período informado em tela;
- Nota fiscal de devolução \(NORM\_DEV = “2”\);
- Nota de Saída \(MOVTO\_E\_S = “9”\);
- Modelo = 01, 1B, 04, 55, 65 
- Somente notas *não canceladas*;
- Somente notas *com itens*;
- Produto ou NCM \(sujeito ao ICMS\-ST\)\*\*; 
- CFOP ou CFOP/Natureza de Operação parametrizado para “Entrada \(e Devolução\)”;
- Desconsiderar as notas de devolução interestadual \(NORM\_DEV = “2”\), que tenham o  CFOP ou CFOP/Natureza de Operação parametrizado para Fato Gerador Presumido Não Realizado no registro C185, para a seguinte operação: 

\- Devolução de Entrada Interestadual;

\*\* __Produto ou NCM \(sujeito ao ICMS\-ST\)__

O produto do item deve constar na parametrização do Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà Produto ou parametrizado a NCM no Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà NCM\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma: 

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”; 

Recuperar as seguintes informações da nota de devolução \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de devolução;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

Para cada item de mercadoria da nota de devolução vamos recuperar a\(s\) nota\(s\) de entradas\(s\) devolvida\(s\)\.

Buscar a entrada a partir dos campos de referência da SAFX08 \(117, 118, 119, 102\)\.

Caso esses campos não estejam preenchidos, exibir a seguinte mensagem no log e não gravar a nota de devolução na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV:

*         “Registro C186: Nota de Devolução de entrada não considerada na geração, pois não existe referência para operação de origem\.*

*          Favor informar a entrada que está sendo devolvida utilizando os campos de referência da SAFX08 \(117, 118, 119, 102\)\.”*

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

## 2 – Recuperação das Notas Fiscais de Entradas referenciadas pela Devolução \(norm\_dev = 1 /movto\_e\_s <> 9\)

Para cada item de mercadoria da nota de devolução recuperada conforme tópico 1, vamos recuperar as notas de entradas devolvidas, referenciadas pela nota de devolução\. 

__Recuperação das entradas referenciadas pela SAFX08:__

Caso o item de mercadoria da nota de devolução possua os campos 117, 118, 119, 102 \(SAFX08\) preenchidos, recuperar o documento de referência \(nota de entrada devolvida\), a partir dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução

\- Estabelecimento      = Código do estabelecimento da nota de devolução

\- Movimento E/S        = deve ser uma nota de entrada \(MOVTO\_E\_S <> “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = mesma pessoa fis/jur da nota de devolução

\- Número                    = campo “117\-Número do Documento Fiscal de Referência” da nota de devolução

\- Série                         = campo “118\-Série do Documento Fiscal de Referência “da nota de devolução

\- Subsérie                  = campo “119\-Subsérie do Documento Fiscal de Referência “da nota de devolução

\- Data de Emissão     = campo “102\-Data DI / Data Doc Refer” da nota de devolução

\- Produto                    = produto do item da nota de devolução \(grupo,indicador e código\); 

Recuperar as seguintes informações da nota de entrada referenciada \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de entrada referenciada;

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de entrada será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__OBS__: O uso dos campos de referência da SAFX08 da nota de devolução para identificar a nota de entrada, espera\-se que apenas um item da nota de entrada seja recuperado\. Mas, caso seja encontrado mais de um item da nota de entrada para o produto devolvido, todos serão gravados na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\.  

O correto é utilizar os campos de referência da SAFX08 da nota de devolução quando apenas um item da nota de entrada está relacionado ao produto devolvido\. Caso mais de um item de entrada esteja relacionado ao produto devolvido, deve\-se utilizar a SAFX192\. E caso esse cenário existir, devemos alterar a Geração da Devolução da Entrada para trabalhar também com a SAFX192\. 

Crítica a ser realizada:

Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log: 

   “*Registro C186: Nota de Devolução de entrada não considerada na geração, pois a nota de entrada original referenciada no item da nota não foi encontrada na base de dados\.”*\. 

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

## 3 – Gravação dos Dados na tabela x308\_info\_compl\_st\_it\_merc\_dev

Os documentos fiscais de Devolução recuperados serão gravados__ item a item__, com todas as referências para as notas fiscais de entradas devolvidas, conforme definido a seguir\.

Gravar a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com IND\_GRAVACAO = ‘6’;

PK

Item

SAFX308

Campo

Regra de Preenchimento

__*Campos do layout da SAFX308 \(Item da nota de devoução com item da nota de entrada objeto da devolução\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Devolução da Entrada \(SAFX07\) 

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Devolução da Entrada \(SAFX07\)

\(\*\)

03

Data Escrita Fiscal \(NF Devolução\)

DATA\_FISCAL

Data fiscal da nota de Devolução da Entrada \(SAFX07\)

\(\*\)

04

Movimento Entrada / Saída \(NF Devolução\)

MOVTO\_E\_S

Indicador do movimento da nota de Devolução da Entrada \(SAFX07\)

\(\*\)

05

Normal ou Devolução \(NF Devolução\)

NORM\_DEV

Indicando de Normal/Devolução da nota de Devolução da Entrada \(SAFX07\)

\(\*\)

06

Tipo do Documento \(NF Devolução\)

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Devolução da Entrada\.

\(\*\)

07

08

Pessoa Física/Jurídica \(NF Devolução\)

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Devolução da Entrada \(SAFX07\)

\(\*\)

09

Número do Documento Fiscal \(NF Devolução\)

NUM\_DOCFIS

Número do documento fiscal da Devolução da Entrada\.

 \(\*\)

10

Série do Documento Fiscal \(NF Devolução\) \(NF Devolução\)

SERIE\_DOCFIS

Série do documento fiscal da Devolução da Entrada\.

 \(\*\)

11

Subsérie do Documento Fiscal \(NF Devolução\)

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal da Devolução da Entrada

\(\*\)

12 13 14 15

Identificador do Item \(NF Devolução\)

DISCRI\_ITEM

Campo identificador do item de mercadoria da Devolução da Entrada 

\(DISCR\_ITEM da X08\_ITENS\_MERC\)\.

\(\*\)

16

Espécie do Documento de Referência da Devolução

ESPECIE\_DOCTO\_DEV

Preencher com:

   1\-Nota Fiscal \(SAFX07/08\)

A identificação do documento fiscal de referência, é feita através dos campos 17 ao 30, e dependendo da espécie do documento, devem ser preenchidos, obrigatoriamente, os seguintes campos:  
Se opção = 1, devem ser preenchidos os campos 17 ao 23, e o campo 30;  
Se opção = 2, devem ser preenchidos os campos  24, 25, 26, 27 e 30;  
Se opção = 3, devem ser preenchidos os campos 27, 28, 29 e 30\.  


 \(\*\)

17

Número do Documento Fiscal de Referência \(NF Entrada\)

NUM\_DOCFIS\_REF

Preencher com:

   Número da nota fiscal de entrada referenciada pela devolução, conforme tópico 2\.

 \(\*\)

18

Série do Documento Fiscal de Referência \(NF Entrada\)

SERIE\_DOCFIS\_REF

Preencher com:

   Série da nota fiscal de entrada referenciada pela devolução, conforme tópico 2\.

 \(\*\)

19

Subsérie do Documento Fiscal de Referência \(NF Entrada\)

SUB\_SERIE\_DOCFIS\_REF

Preencher com:

   Subsérie da nota fiscal de entrada referenciada pela devolução, conforme tópico 2\.

 \(\*\)

20

Tipo do Documento de Referência \(NF Entrada\)

COD\_DOCTO\_REF

\(IDENT\_DOCTO\_REF\)

Preencher com:

Tipo do documento fiscal da nota fiscal de entrada referenciada pela devolução, de acordo com a Tabela de Tipos de Documentos \(SAFX2005\)\.

 \(\*\)

21

Data Escrita Fiscal do Documento de Referência

DATA\_FISCAL\_REF

Preencher com:

  Data da Fiscal da nota fiscal de entrada referenciada pela devolução, conforme tópico 2\.

 \(\*\)

22

23

Pessoa Física/Jurídica do Documento de Referência \(NF Entrada\)

IND\_FIS\_JUR\_REF/ COD\_FIS\_JUR\_REF

\(IDENT\_FIS\_JUR\_REF\)

Preencher com:

Pessoa física/jurídica da nota fiscal de entrada referenciada pela devolução, de acordo com a Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\.

 \(\*\)

24

Modelo do Cupom Fiscal de Referência

COD\_MODELO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

 \(\*\)

25

Número do Caixa do Cupom Fiscal de Referência

COD\_CAIXA\_ECF\_REF

\(IDENT\_CAIXA\_ECF\)

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

 \(\*\)

26

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência

NUM\_COO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

 \(\*\)

27

Data de Emissão do Cupom Fiscal de Referência

DATA\_EMISSAO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

 \(\*\)

28

Número do Equipamento SAT do Cupom Fiscal de Referência

NUM\_EQUIP\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado

\(\*\) 

29

Número do Cupom Fiscal do Referência 

NUM\_CUPOM\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal referenciado 

\(\*\)

30

Número do Item do Documento de Referência \(NF Entrada\)

NUM\_ITEM\_DOC\_REF

Número do Item da nota fiscal de entrada referenciada pela devolução, conforme tópico 2\.

31

Código Motivo

Campos da EFD correspondentes: 02 do C181 e 06 do C186\.

COD\_MOTIVO

Preencher com: __MG400__

32

Quantidade Convertida

Campos da EFD correspondentes: 03 do C181 e 07 do C186\.

QTD\_CONV

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Entrada \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV_ENT)\)”

Ver [__*Detalhamento da Nota de Devolução*__](#Detalha_NF_DEV_ENT)

33

Unidade de Medida

Campos da EFD correspondentes: 04 do C181 e 08 do C186\.

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Devolução da Entrada\.

\.

 

34

Valor Unitário Conv

Campos da EFD correspondentes: 12 do C181 e 15 do C186\.

VLR\_UNIT\_CONV

Preencher com:

  \(VLR\_CONTAB\_ITEM \- Valor do ICMS\-ST\) / QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada, conforme tópico 2:

- VLR\_CONTAB\_ITEM é o campo 64\-Valor Contabil \(SAFX08\) do Item da nota de Entrada referenciada;
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”
- Valor do ICMS\-ST é oriundo de um dos quatro campos SAFX08 do Item da nota de Entrada referenciada, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__\.](#Detalha_NF_ENT)

__Obs__: O valor do ICMS\-ST está sendo subtraído do valor contábil com base na orientação do Guia Prático do Sped Fiscal, do registro da entrada C180: 

*“Campo 05 \(VL\_UNIT\_CONV\) – *__*Preenchimento*__*: informar o valor unitário líquido do item/produto \(considerando descontos e acréscimos incondicionais aplicados sobre o valor bruto\)\. O valor unitário do campo 05 não inclui o ICMS ST na aquisição de participante substituto ou nas hipóteses em que o informante é responsável pela substituição\.”*

Essa interpretação foi confirmada com nossa Área de Informação \(CAN\) juntamente com o Carrefour\.

 

35

Valor Unitário ICMS OP Conv

Campos da EFD correspondentes: 17 do C181 e 16 do C186

VLR\_ICMS\_CONV

Preencher com:

 Valor do ICMS / QTD\_CONV\_NF\_ENT 

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do ICMS é oriundo de um dos três campos SAFX08, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_ENT)\.

 

36

Valor Unitário Base ICMS ST Conv da Entrada

Campo da EFD correspondente: 17 do C186\.

VLR\_UNIT\_BC\_ICMSS\_ENT

Preencher com:

 Valor da BC\-ST / QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                        “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e

                            “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_ENT)\.

 

37

Valor Unitário ICMS ST Conv da Entrada

Campo da EFD correspondente: 18 do C186\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

Preencher com:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

\[__MFS665846__\] Tratamento do campo FECEP Regime Fonte

O preenchimento do campo seria:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/ QTD\_CONV\_NF\_ENT

Mas deve\-se tratar o caso do Valor do ICMS\-ST já conter o FECEP\-ST, para que este não seja somado duas vezes\. 

Como premissa, a tabela DATAMART já contém o FECEP\-ST embutido no campo 52\-ICMS\-ST, pois na equalização do DATA MART, os clientes são orientados a marcar o parâmetro para somar FECEP ao ICMS/ICMS\-ST, quando o FECEP não “nasce” embutido ao ICMS/ICMS\-ST nas tabelas “normais” X07/X08\. 

Quanto às tabelas “normais”, o FECEP pode ou não estar embutido campo 52\-ICMS\-ST via importação da SAFX08, por isso existe o parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” \)” da tela de geração\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

      itens \(SAFX08\)” foi marcado, então:

          Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP Regime Fonte\) / QTD\_CONV\_NF\_ENT 

__          __Senão:

                  Preencher com: 

                 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/   QTD\_CONV\_NF\_ENT

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos 

      itens \(SAFX08\)” não foi marcado, então:

           Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/ QTD\_CONV\_NF\_ENT

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o __Valor do ICMS\-ST__ \(\*\):

           Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP Regime Fonte\) / QTD\_CONV\_NF\_ENT

     Senão

           Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/ QTD\_CONV\_NF\_ENT

__\[MFS977849\]__ Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado 

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\) ou DATAMART, então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” foi marcado, então:

          Se for considerado o “145\- VLR\_ICMSS\_N\_ESCRIT” ou “133\- VLR\_ICMSS\_NDESTAC” p/ __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP Regime Fonte\) / QTD\_CONV\_NF\_ENT 

__          __Senão:

                  Preencher com: 

                 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/   QTD\_CONV\_NF\_ENT

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” não foi marcado, então:

           Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)/ QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- Valor do FECEP Regime Fonte:  Campo 141\- VLR\_FECP\_FONTE da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

__OBS__: não estamos tratando o caso do FECEP\-ST já estar embutido no Valor do ICMS\-ST\.

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_ENT)\.

 

38

Valor Unitário FCP ST Conv da Entrada

Campo da EFD correspondente: 19 do C186\.

VLR\_UNIT\_FCP\_CONV\_ENT

\[__MFS665846__\] Tratamento do campo FECEP Regime Fonte

Preencher com:

\(Valor do FECEP\-ST \+  Valor do FECEP Regime Fonte\) /  QTD\_CONV\_NF\_ENT

Onde os valores são oriundos do item da nota de Entrada referenciada:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.
- Valor do FECEP Regime Fonte:  Campo 141\- VLR\_FECP\_FONTE da SAFX08\.
- QTD\_CONV\_NF\_ENT: “Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \([QTD\_CONV\_NF\_ENT](#QTD_CONV_NF_ENT)\)”

Ver  [__*Detalhamento da Nota de Entrada Referenciada pela Devolução*__](#Detalha_NF_ENT)\.

 

39

Valor Unitário ICMS OP Estoque Conv

Campo da EFD correspondente: 13 do C181\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.  


 

40

Valor Unitário ICMS ST Estoque Conv

Campo da EFD correspondente: 14 do C181\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

 

41

Valor Unitário FCP ICMS ST Estoque Conv

Campo da EFD correspondente: 15 do C181\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

 

42

Valor Unitário ICMS na Operação Conv

Campo da EFD correspondente: 16 do C181\.

VLR\_UNIT\_ICMS\_OPER\_SAI

 Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

 

43

Valor Unitário ICMS ST Conv Rest

Campo da EFD correspondente: 18 do C181\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

 

44

Valor Unitário FCP ST Conv Rest

Campo da EFD correspondente: 19 do C181\.

VLR\_UNIT\_FCP\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

 

45

Valor Unitário ICMS ST Conv Compl

Campo da EFD correspondente: 20 do C181\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

46

Valor Unitário FCP ST Conv Compl

Campo da EFD correspondente: 21 do C181\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

__Detalhamento das Regras:__

<a id="Detalha_NF_DEV_ENT"></a>__Detalhamento da Nota de Devolução__<a id="QTD_CONV_NF_DEV_ENT"></a>

- __Qtde Convertida Calculada para NF de Devolução de Entrada \(safx08\) \(QTD\_CONV\_NF\_DEV\)__

Considerar os campos do item da nota de Devolução de Entrada recuperada no tópico 1:

- Campo 24\-Quantidade \(SAFX08\) 
- Campo 137 – Quantidade Convertida \(SAFX08\)
- Campo 25 – Unidade de Medida \(SAFX08\) 

Calcular a quantidade convertida pela regra a seguir:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C186: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de entrada será gerada no C186 sem informação no campo 07 \- Quantidade Convertida e não irá compor a Média Pondera Móvel dos Valores Unitários do dia DD/MM/YYYY\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

<a id="Detalha_NF_ENT"></a>__Detalhamento da Nota de Entrada Referenciada pela Devolução__

- <a id="QTD_CONV_NF_ENT"></a>__Qtde Convertida Calculada para o Item da NF de Entrada Referenciada \(QTD\_CONV\_NF\_ENT\)__

Considerar os campos do item da nota de entrada, recuperada no tópico 2:

- Campo 24\-Quantidade \(SAFX08\) 
- Campo 137 – Quantidade Convertida \(SAFX08\)
- Campo 25 – Unidade de Medida \(SAFX08\) 

Calcular a quantidade convertida pela regra abaixo:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Entrada Referenciada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[ Quantidade do item da nota \(SAFX08\) \* Fator de Conversão \]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C186: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de Entrada será gerada no C186 sem valores unitários da Mercadoria, do ICMS, BC\-ST, ICMS\-ST e FCP \(campos 15 a 19\)\. Favor rever medida da NF de entrada referenciada pela devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Entrada e da Entrada referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

## 4 \- Gerar relatório a partir da tabela x308\_info\_compl\_st\_it\_merc\_dev

\[MFS511653\]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré\-geração:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, disponibilizar um arquivo Excel com as notas de devolução de entrada consideradas para o registro C186\.

Nome do arquivo: Relatório\_Conferencia\_C186\_mm\_aaaa\_cod\_estab\.csv

Para isso fazer uma leitura na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com os seguintes critérios:

\- empresa de login;

\- estabelecimento selecionado na tela de geração;

\- data fiscal compreendida no Período informado na tela de Geração;

\- Movimento E/S = ‘9’ \(saída\)

Ordenar as notas pelos campos: empresa, estabelecimento, data fiscal, número do documento fiscal, número do item de mercadoria\.

Obs: campos que não devem sair no relatório:

16

Espécie do Documento de Referência da Devolução

ESPECIE\_DOCTO\_DEV

A saída referenciada pela devolução é uma Nota Fiscal, então:

    Preencher com: 1\-Nota Fiscal \(SAFX07/08\)

Nota da SAFX308: 

A identificação do documento fiscal de referência, é feita através dos campos 17 ao 30, e dependendo da espécie do documento, devem ser preenchidos, obrigatoriamente, os seguintes campos:  
Se opção = 1, devem ser preenchidos os campos 17 ao 23, e o campo 30;  
Se opção = 2, devem ser preenchidos os campos  24, 25, 26, 27 e 30;  
Se opção = 3, devem ser preenchidos os campos 27, 28, 29 e 30\.  


24

Modelo do Cupom Fiscal de Referência

COD\_MODELO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\. 

25

Número do Caixa do Cupom Fiscal de Referência

COD\_CAIXA\_ECF\_REF

\(IDENT\_CAIXA\_ECF\)

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

26

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência

NUM\_COO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

27

Data de Emissão do Cupom Fiscal de Referência

DATA\_EMISSAO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

28

Número do Equipamento SAT do Cupom Fiscal de Referência

NUM\_EQUIP\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\. 

29

Número do Cupom Fiscal do Referência 

NUM\_CUPOM\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\.

39

Valor Unitário ICMS OP Estoque Conv

Campo da EFD correspondente: 13 do C181\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.  


40

Valor Unitário ICMS ST Estoque Conv

Campo da EFD correspondente: 14 do C181\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

41

Valor Unitário FCP ICMS ST Estoque Conv

Campo da EFD correspondente: 15 do C181\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

42

Valor Unitário ICMS na Operação Conv

Campo da EFD correspondente: 16 do C181\.

VLR\_UNIT\_ICMS\_OPER\_SAI

 Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

43

Valor Unitário ICMS ST Conv Rest

Campo da EFD correspondente: 18 do C181\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

44

Valor Unitário FCP ST Conv Rest

Campo da EFD correspondente: 19 do C181\.

VLR\_UNIT\_FCP\_REST\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

45

Valor Unitário ICMS ST Conv Compl

Campo da EFD correspondente: 20 do C181\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

46

Valor Unitário FCP ST Conv Compl

Campo da EFD correspondente: 21 do C181\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Saídas\.

MFS\-64570

MFS\-

70215

MFS\-73772

