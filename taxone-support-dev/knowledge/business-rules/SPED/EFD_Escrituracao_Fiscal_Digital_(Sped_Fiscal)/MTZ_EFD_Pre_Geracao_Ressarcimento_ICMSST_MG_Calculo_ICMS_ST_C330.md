# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C330

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C330.docx
- **Modificado:** 2021-07-28
- **Tamanho:** 123 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Processamento do Cálculo ICMS\-ST – Registro C330

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

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc37749427"></a>INTRODUÇÃO* *

Este documento contém as regras de geração do registro C330\.

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

RP06

Quando o parâmetro __*C330 –Saída de mercadorias sujeitas à substituição tributária \(02\) *__estiver marcado na tela: Todos os cálculos realizados por este processo serão armazenados na tabela x299\_inf\_comp\_st\_res\_mod\_02, referente à saída e serão utilizados para a geração do registro C330 do SPED FISCAL\.

## 1 – Recuperação das Notas Fiscais de Saídas \(norm\_dev = ‘1’/ movto\_e\_s = ‘9’\)

__Critérios da recuperação das Notas Fiscais de Saídas Interna para Consumidor Final: __ 

 

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Saída;
- Somente notas *não canceladas *e que não sejam de devolução; 

\(27/05/2020:Feito consulta com a SEFAZ sobre considerar ou não as notas de devolução\)

- Somente notas *com itens*; 
- Modelo somente modelos de notas 02  
- Classificação do Documento Fiscal = “1”
- Produto ou NCM \(sujeito ao ICMS\-ST\)\*\* 
- CFOP ou CFOP/Natureza de Operação parametrizado para “Saída Interna para Consumidor Final \(e Devoluções\) \(art 31\-A \- Anexo XV do RICMS/02\)” \[MFS47079\]

\*\* __Produto ou NCM \(sujeito ao ICMS\-ST\)__

O produto do item deve constar na parametrização do Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà Produto ou parametrizado a NCM no Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà NCM\.

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma:

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”;

__\*\*\* Conversão de Unidade, para encontrar a Quantidade Convertida \(SAFX08\):__

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria Quantidade do Item da nota \(SAFX08\);

__Senão __

    \[MFS47248\]

     __Se__ existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\):

 Nesse caso o campo será preenchido com a quantidade convertida recuperada do campo “137\-Quantidade Convertida”;

     __Senão         __

Neste caso a quantidade do item da nota será convertida para a unidade de medida do cadastro do produto, utilizando o fator de conversão obtido nas tabelas de Conversão de Medida\.

Assim, será a multiplicação dos seguintes campos:

          \[Quantidade do item da nota \(SAFX08\) \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisar o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, o item será identificado no [log \(RP05\),](#LOG_NOTA) e o cálculo não será realizado\.

Este registro é um agrupamento, por itens de mercadoria, da consolidação diária dos valores das notas fiscais de venda ao consumidor não emitidas por ECF agrupados no registro C320\.

Este registro é filho do C321, para cada registro C321 pode ocorrer 1 apenas um registro C330\.

 

Agrupamento 1 é o agrupamento diário das notas fiscais de venda ao consumidor em ordem crescente\.  A quebra do registro ocorrerá cada vez que diferenciar um item do agrupamento final 3 \(é necessário efetuar todos os agrupamentos \(1, 2 e 3\) citados abaixo:\)

__Agrupamento 1 \(Utilizado no C300\):__

Fazer uma consolidação das notas de saída \(diária\), considerando as informações abaixo para o agrupamento:

- 
	- Data de Emissão,
	- Modelo de Documento,
	- Série do Documento Fiscal,
	- Subsérie do Documento Fiscal,
	- Conta Contábil

__Agrupamento 2 \(Utilizado no C320\):__

- 
	- __CST\_ICMS__  
	- __CFOP__ \- Código Fiscal,
	- __ALIQ\_ICMS__ – Alíquota ICMS, 

__Agrupamento 3 \(utilizado no C321\):__

- 
	- 
		- __COD\_ITEM – __Código do item
		- __UNID – __Unidade do item

Após efetuar o agrupamento final \(todos os agrupamentos indicados em 1,2,3 e nesta ordem\), fazer o somatório de todos os valores dos itens recuperados e que serão utilizados para dar sequência com o cálculo \(indicado no item Restituição/Complemento na RP02\)\. 

## 2 \- Recuperação dos Valores Unitários Médios referenciados pela SAÍDA

MFS\-67654

Vamos recuperar os Valores Médios Unitário do dia da saída, da tabela de Média Ponderada \(__EST\_ST\_MG\_MEDIA\_POND__\), calculados na \([RP00B](#RP00B)\)\. 

              

Consultar a Tabela de Média Pondera \(__EST\_ST\_MG\_MEDIA\_POND__\) com os seguintes critérios:

\- Empresa login;

\- Estabelecimento selecionado na tela de geração;

\- Data = Data de Emissão da Nota fiscal de Saída \(SAFX07\);

\- Produto = Produto do item da Nota de Saída;

Recuperar os Valores Médios:

\- Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\);

\- Valor Médio Unitário do ICMS\-ST c/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP\); 

\- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\);

\- Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP\);

A partir da MFS\-67654, não vamos mais utilizar os valores calculados pela [RP00A](#RP00A) \- [__CÁLCULO DOS VALORES MÉDIOS DIÁRIOS DO PRODUTO DO PERÍODO__](#CALC_MED_PROD)\.

__Validações__

Considerar as validações na RP05 \([Mensagens que devem ser apresentadas no Log do processamento](#RP05_GERAL) e [Mensagens que devem ser apresentadas no Log do processamento \(C330\)](#RP05_Inventarios_c330)

MFS\-35337

\[MFS47079\]

MFS\-67654

<a id="RP07_tabela_registros_c330"></a>RP07

Gravar os registros na tabela x299\_inf\_comp\_st\_res\_mod\_02, conforme regras indicadas nos respectivos campos indicado na tabela abaixo\.  __Para os registros C330__, apresentar __APENAS __os itens de nota de saída da SAFX08 de __modelo igual a 02__, que foram recuperados na RP06\.

Os dados calculados e gravados podem ser consultados na tela: Menu Básicos, Módulo: DW, menu Manutenção à Documento Fiscal à Novo Documento Fiscal à Resumo Diário Mod 02 \- Informações Complementares Oper\. ST \(Sped Fiscal\)

__\(Tabela de Gravação dos Registros C330\)__

Tabela

Obr

Item

Nome do Campo/Layout

Regra

X299

\(\*\)

1

COD\_EMPRESA

Considerar a informação do campo 01\-COD\_EMPRESA do documento de saída recuperado da SAFX08\.

X299

\(\*\)

2

COD\_ESTAB

Considerar a informação do campo 02\-COD\_ESTAB do documento de saída recuperado da SAFX08\.

X299

\(\*\)

3

DATA\_EMISSAO

Considerar a informação do campo DATA\_EMISSAO dos documentos de saídas que foram agrupados da SAFX08\.

X299

 

4

SERIE\_DOCFIS

Considerar a informação do campo 10\-SERIE\_DOCFIS dos documentos de saída que foram agupados da SAFX08\.

X299

 

5

SUB\_SERIE\_DOCFIS

Considerar a informação do campo 11\-SUB\_SERIE\_DOCFIS dos documentos de saída que foram agrupados SAFX08\.

X299

\(\*\)

6

NUM\_DOCFIS\_INI

Considerar a informação do campo NUM\_DOCFIS\_INI do documento de saída recuperado da SAFX08 \(Primeiro número de nota que foi considerado no agrupamento \(RP06\)\)\.

X299

\(\*\)

7

NUM\_DOCFIS\_FIN

Considerar a informação do campo NUM\_DOCFIS\_FIN do documento de saída recuperado da SAFX08 \(Último número de nota que foi considerado no agrupamento \(RP06\)\)\.

X299

\(\*\)

8

COD\_SITUACAO\_A

Considerar a informação do campo 30\-COD\_SITUACAO\_A dos documentos de saída que foram agrupados da SAFX08\.

X299

\(\*\)

9

COD\_SITUACAO\_B

Considerar a informação do campo 31\-COD\_SITUACAO\_B do documento de saída que foram agrupados da SAFX08\.

X299

\(\*\)

10

COD\_CFO

Considerar a informação do campo 22\-COD\_CFO do documento de saída que foram agrupados da SAFX08\.

X299

 

11

VLR\_ALIQ\_ICMS

Considerar a informação do campo 42\-VLR\_ALIQ\_ICMS dos documentos de saída que foram agrupados da SAFX08\.

X299

\(\*\)

12

IND\_PRODUTO

Considerar a informação do campo 13\-IND\_PRODUTO dos documentos de saída que foram agrupados da SAFX08\.

X299

\(\*\)

13

COD\_PRODUTO

Considerar a informação do campo 14\-COD\_PRODUTO dos documentos de saída que foram agrupados da SAFX08\.

X299

\(\*\)

14

COD\_MOTIVO

2 \- COD\_MOT\_REST\_COMPL  

__\[MFS\-67654\]:__

Verificar na regra [RP02](#RP02_Restituicao_Complemento), tópico [Restituição/Complemento](#RP02_Restituicao_Complemento),  os valores: ‘Valor unitário da saída da mercadoria’ e ‘Valor Base ICMS\-ST \(Unitário Médio\) dos Itens de Entrada do dia’, para a definição da classificação do motivo, conforme regras abaixo:

Se o valor ‘Valor unitário da saída da mercadoria’  for inferior  ao Valor Base ICMS\-ST Unitário Médio\) dos Itens de Entrada do dia’,__ __calculado conforme__ __[__PrecoMedioDIA__](#PrecoMedioDIA), teremos __restituição__\. O motivo será igual a __MG100\.__

Se o valor ‘Valor unitário da saída da mercadoria’ for superior ao ‘Valor Base ICMS\-ST Unitário Médio’ dos Itens de Entrada do dia’, teremos __complemento__\. O motivo será igual a __MG300 __

Se o valor ‘Valor unitário da saída da mercadoria’ for igual ao ‘Valor Base ICMS\-ST Unitário Médio’ dos Itens de Entrada do dia’, não teremos restituição e nem __complemento__\. Seria o motivo __MG000__, porém Minas, não solicita essa informação, neste caso, __não devemos considerar essas notas de saída na gravação da tabela__\. 

Se \(20\-VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

      21\-VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

     18\- VLR\_UNIT\_ICMS\_OPER\_CONV > 0 

   \(entrada > saída = ressarcimento\) 

então:

    A saída obteve Restituição;

    Preencher com “__MG100__”\. 

Se \(20\-VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

      21\-VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

     18\- VLR\_UNIT\_ICMS\_OPER\_CONV < 0 

     \(entrada < saída = complemento\) 

então:

    A saída obteve Complemento;

    Preencher com “__MG300__”\.  

Se \(20\-VLR\_UNIT\_ICMS\_ESTQ\_CONV \+ 

      21\-VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

     18\- VLR\_UNIT\_ICMS\_OPER\_CONV = 0 

    \(entrada = saída\) 

então:

    A saída não teve nem Restituição nem Complemento\.

    Nesse caso a nota não será considerada na gravação 

    da tabela\.

X299

\(\*\)

15

QTD\_CONV

Quantidade do item \(convertida\)\.

Ver regra de conversão indicada na RP06\. Considerar a quantidade consolidada dos documentos que foram agrupadas\.

X299

\(\*\)

16

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota\.

X299

\(\*\)

17

VLR\_UNIT\_CONV

5 \- VL\_UNIT\_CONV

Considerar o VLR\_UNIT das sequências dos documentos que foram agrupados da SAFX08\.

Atenção: Somar todos os valores unitários das sequências dos itens e dividir pelo número de itens recuperados\.

X299

 

18

VLR\_UNIT\_ICMS\_OPER\_CONV

6 \- VL\_UNIT\_ICMS\_NA\_OPERAÇÃO\_ CONV

Considerar o resultado da expressão: valor do contábil do documento de saída \(64 –VLR\_CONTAB\_ITEM, da SAFX08 multiplicado pela alíquota interna\)/quantidade do item de saída recuperado \(convertida\)\. Considerar os valores de todos os itens que foram agrupados\.

__Como identificar a Alíquota Interna:__

Considerar a alíquota Interna existente na parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

A alíquota recuperada deve ser divida por 100\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. Lembrando que a alíquota não deve ser somada\.

__Se existir Redução de Base de ICMS\-ST, considerar: __

Campo 94 – TRIB\_ICMSS da SAFX08, estiver preenchido com ‘4’, efetuar o seguinte cálculo:

\[\(64 – VLR\_CONTAB\_ITEM – 95 – BASE\_REDU\_ICMSS\) \* alíquota interna\]/quantidade do item de saída\.  Considerar os valores de todos os itens que foram agrupados\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. Lembrando que a alíquota não deve ser somada\.

__Validação:__

Se o valor \( 95 – BASE\_REDU\_ICMSS\) for maior ou igual ao valor \(64 – VLR\_CONTAB\_ITEM\), gravar zero no campo e exibir a mensagem no log: “O Valor da Base de Redução está maior ou igual ao Valor Contábil do Item, por isso, o campo Valor ICMS Convertido foi gerado com zero”\.

Apresentar no log, as informações para conseguir identificar a sequência das nota\.

X299

 

19

VLR\_UNIT\_ICMS\_CONV

7 \- VL\_UNIT\_ICMS\_OP\_CONV

Se campo 14 – COD\_MOTIVO\_SAI igual a MG100 ou MG300 deixar este campo vazio\.

X299

 

20

VLR\_UNIT\_ICMS\_ESTQ\_CONV

8 \- VL\_UNIT\_ICMS\_OP\_ESTOQUE\_ CONV

__\[MFS\-67654\]:__

Considerar o valor unitário médio calculado na RP02, \(__\*\*Valor ICMS UNITARIO Médio\)__,__ calculado conforme __[__PrecoMedioDIA__](#PrecoMedioDIA)__,__ referente ao dia da nota de saída\.  

Preencher com o “Valor Médio Unitário do ICMS” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\), conforme tópico 2 da RP06, para o Produto na Data de Emissão da nota de saída\. 

    \(campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

X299

 

21

VLR\_UNIT\_ICMSS\_ESTQ\_CONV

9 \- VL\_UNIT\_ICMS\_ST\_ESTOQUE\_ CONV

__\[MFS\-67654\]:__

Considerar o valor unitário médio dos campos ICMS ST \+ VLR\_FECP\_ICMS\_ST calculado na RP02,  c__alculado conforme __[__PrecoMedioDIA__](#PrecoMedioDIA), referente ao dia da nota de saída\.  

Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\), conforme tópico 2 da RP06, para o Produto na Data de Emissão da nota de saída\. 

   \(campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

X299

 

22

VLR\_UNIT\_FCPS\_ESTQ\_CONV

10 \- VL\_UNIT\_FCP\_ICMS\_ST\_ ESTOQUE\_CONV

__\[MFS\-67654\]:__

Considerar o valor unitário médio \(__Valor FECP\-ST UNITARIO __

__Médio__\) calculado na RP02, __calculado conforme __[__PrecoMedioDIA__](#PrecoMedioDIA), , referente ao dia da nota de saída\.  

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_MG\_RS\_MEDIA\_POND\), conforme tópico 2 da RP06, para o Produto na Data de Emissão da nota de saída\. 

    \(campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

X299

 

23

VLR\_UNIT\_ICMSS\_REST\_CONV

11 \- VL\_UNIT\_ICMS\_ST\_CONV \_REST

Se o campo 14 – COD\_MOTIVO\_SAI for igual a __MG100__, preencher com o resultado da expressão: 

\(20\-VLR\_UNIT\_ICMS\_ESTQ\_CONV\) \+

\(21\-VLR\_UNIT\_ICMSS\_ESTQ\_CONV\) \- 

\(18\- VLR\_UNIT\_ICMS\_OPER\_CONV\)\.  

Considerar os valores de todos os itens que foram agrupados\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. 

\[MFS\-67654\]__:__

__Validação:__

Se o resultado da expressão acima for negativo, gravar zero e exibir a mensagem no log: 

“O resultado do cálculo: ‘Valor Unitário ICMS Estoque Conv\.’  \+ ‘Valor Unitário ICMS\-ST Estoque Conv\.’ 

 ficou negativo,  por isso, o campo ‘Valor Unitário ICMS\-ST Conv\. Rest\.’ foi gravado com zero”\.

Apresentar no log, as informações para conseguir identificar a sequência das notas\.

Se o campo 14 – COD\_MOTIVO\_SAI igual a MG300, deixar este campo vazio\. 

X299

 

24

VLR\_UNIT\_FCPS\_REST\_CONV

12\-VL\_UNIT\_FCP\_ST\_CONV \_REST

Se o campo 14 – COD\_MOTIVO\_SAI for igual a __MG100__ e o campo 22 \- VLR\_UNIT\_FCPS\_ESTQ\_CONV

 for maior que zero, preencher com o resultado da expressão: \(campo 23\- VLR\_UNIT\_ICMSS\_REST\_CONV \* alíquota de FCP\)\.  

Considerar os valores de todos os itens que foram agrupados\.

__Como identificar a Alíquota FCP:__

Considerar a alíquota FCP existente na parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

A alíquota recuperada deve ser divida por 100\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. Lembrando que a alíquota não deve ser somada\.

\[MFS\-67654\]__:__

__Validação:__

Se o resultado da expressão acima for negativo, gravar zero e exibir a mensagem no log: 

“O resultado do cálculo: ‘Valor Unitário ICMS\-ST Conv\. Rest\.\* ‘Alíquota FCP’ ficou negativo,  por isso, o campo ‘Valor Unitário FCP\-ST Conv\. Rest\.’ foi gravado com zero”\.

Apresentar no log, as informações para conseguir identificar a sequência das notas\.

Se o campo 14 – COD\_MOTIVO\_SAI igual a MG300, deixar este campo vazio\.

X299

 

25

VLR\_UNIT\_ICMSS\_COMPL\_CONV

13 \- VL\_UNIT\_ICMS\_ST\_CONV COMPL

Se o campo 14 – COD\_MOTIVO\_SAI for igual a __MG300__, preencher com o resultado da expressão: 

\(18\- VLR\_UNIT\_ICMS\_OPER\_CONV\) \- 

\(20\-VLR\_UNIT\_ICMS\_ESTQ\_CONV\) \-

\(21\-VLR\_UNIT\_ICMSS\_ESTQ\_CONV\)\.  

Considerar os valores de todos os itens que foram agrupados\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. 

\[MFS\-67654\]__:__

Validação:

Se o resultado da expressão acima for negativo, gravar zero e exibir a mensagem no log: 

“O resultado do cálculo: ‘Valor Unitário ICMS na Oper\. Conv\.’  \- ‘Valor Unitário ICMS Estoque Conv\.’ – ‘Valor Unitário ICMS\-ST Estoque Conv\.’, ficou negativo,  por isso, o campo ‘Valor Unitário ICMS\-ST Conv\. Compl\.’ foi gravado com zero”\.

Apresentar no log, as informações para conseguir identificar a sequência das notas\.

Se o campo 14 – COD\_MOTIVO\_SAI igual a MG100, deixar este campo vazio\.

X299

 

26

VLR\_UNIT\_FCPS\_COMPL\_CONV

14 \- VL\_UNIT\_FCP\_ST\_CONV \_COMPL

Se o campo 14\-COD\_MOTIVO\_SAI for igual a __MG300__ e o campo 22 \- VLR\_UNIT\_FCPS\_ESTQ\_CONV

 for maior que zero, preencher com o resultado da expressão: \(campo 25\- VLR\_UNIT\_ICMSS\_COMPL\_CONV \* alíquota de FCP\)\. Considerar os valores de todos os itens que foram agrupados\.

__Como identificar a Alíquota FCP:__

Considerar a alíquota FCP existente na parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

__Atenção:__ Somar todos os valores citados de cada nota, para efetuar a expressão uma única vez\. Lembrando que a alíquota não deve ser somada\.

\[MFS\-67654\]__:__

__Validação:__

Se o resultado da expressão acima for negativo, gravar zero e exibir a mensagem no log: 

“O resultado do cálculo:  ‘Valor Unitário ICMS\-ST Conv\. Compl\.’ \* ‘Alíquota FCP’ ficou negativo,  por isso, o campo ‘Valor Unitário FCP\-ST Conv\. Compl\.’ foi gravado com zero”\.

Apresentar no log, as informações para conseguir identificar a sequência das notas\.

Se o campo 14\-COD\_MOTIVO\_SAI igual a MG100, deixar este campo vazio\.

MFS\-35337

RP08

Todos os registros gravados na tabela x299\_inf\_comp\_st\_res\_mod\_02, através deste processo [\(RP07\)](#RP07_tabela_registros_c330), devem ser identificados que foram calculados pelo sistema, pois os registros importados \(SAFX299\) não podem ser alterados \(por esse processo\)\.

Considerar a mesma sugestão proposta na RP04 [\(campo ind\_gravacao\)](#Sugestao_Ind_Gravacao)\.

MFS\-35337

RP05

<a id="RP05_GERAL"></a>__Mensagens que devem ser apresentadas no Log do processamento \(qualquer registro\):__

- <a id="LOG_SINTEGRA"></a>Se o período indicado na tela de cálculo for menor que 01/2020, apresentar a mensagem: “O cálculo não foi realizado, pois o período a ser calculado deve ser a partir de janeiro de 2020\. Períodos anteriores a janeiro de 2020 devem ser entregues pelo arquivo Sintegra, Registro 88STITNF”\. 
- Demonstrar no log os registros que sofreram alteração \(já tinham sido calculado e foram reprocessados\)\. Exibir os campos chaves\.
- <a id="LOG_INVENT"></a>Se a Unidade de Medida do produto é diferente da Unidade de Medida do Inventário e não for encontrado registro correspondente na tabela de Conversão de Unidades \(Padrão ou por Produto\) apresentar a mensagem “Conversão de Unidade não cadastrada\.  Unidade do Produto: \(14 – COD\_MEDIDA\), Unidade do Estoque: \(12 – COD\_MEDIDA\), por isso, o cálculo não foi realizado\. 

O log deve demonstrar as informações necessárias para permitir a identificação do inventário, exibindo o estabelecimento, a data, produto, indicador do produto, etc \.\.\.\)

-   <a id="LOG_NOTA"></a>Se a Unidade de Medida do item de saída é diferente da Unidade de Medida do Produto e não for encontrado registro correspondente na tabela de Conversão de Unidades \(Padrão ou por Produto\) apresentar a mensagem “Conversão de Unidade não cadastrada\. Unidade do Item de Saída: \(25 – COD\_MEDIDA/ 137 – QUANTIDADE\_CONV\), Unidade do Item de Entrada: \(25 – COD\_MEDIDA, por isso, o cálculo não foi realizado\.

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, produto,indicador, etc\)\. \[MFS47079\] Aplicável a todas as notas de entradas e saídas\.

- <a id="LOG_Valor_Medio"></a>Ao calcular o valor médio do registro do inventário e existir divergência em algum campo dos valores médios, exibir a mensagem “Foi necessário realizar o cálculo dos valores médios do inventário e encontramos divergências em pelo menos um dos campos: 

Valor ICMS Médio, Valor ICMS\-ST Médio ou Valor Base ICMS\-ST Médio: O log deve demonstrar as informações necessárias para permitir a identificação do inventário, exibindo o estabelecimento, a data, produto, indicador do produto, etc \)\.

- Ao recuperar o inventário de Produtos ou NCMs sujeito ao ICMS\-ST, se nenhum registro possuir motivo 06 \(na tabela de inventário\), apresentar a mensagem por registro e produto/ncm: “Não foi localizado inventário com motivo 06 para os Produtos ou NCMs cadastrados nas telas de Parametrização localizados em SPED / Escrituração Fiscal Digital / Parâmetros /Ressarcimento ICMS\-ST\.
- <a id="RP05_GERAL_inventarios_unidades_dif"></a>Se existir mais de um registro de inventário para o mesmo produto, período e Motivo do Inventário \(Campo 40 – IND\_MOT\_INV\) = “06”, com GRUPO\_CONTAGEM = ‘1’ e ‘2’ e a unidade de medida destes registros for diferente, exibir a mensagem no log: “ O produto possui mais de um registro de inventário, para o mesmo período\. Estes registros estão com unidades diferentes\. Favor rever o cadastro"\.”\. O log deve demonstrar as informações necessárias para permitir a identificação inventário, exibindo o estabelecimento, a data, produto,indicador,grupo de contagem etc\)\.
- Se não existir notas de entrada \(para a realização do cálculo de valores médios do inventário\), para todos os produtos sujeitos ao ICMS\-ST, exibir a mensagem \(para cada produto\): “Não foram encontradas notas de entrada, para conseguirmos realizar o cálculo dos valores médios do registro de inventário\. As notas de entrada foram consultadas até: << informar a data preenchida no campo ‘Pesquisar Notas de Entrada até’”\.O log deve demonstrar as informações necessárias para permitir a identificação inventário, exibindo o estabelecimento, a data, produto,indicador, etc\)\.
- Se for encontrado o registro de inventário  na tabela x52\_invent\_produto, para a realização do cálculo, e não foram encontradas notas de entrada suficientes para compor a quantidade deste inventário, realizar o cálculo deste produto com a quantidade encontrada e exibir a mensagem: “Não foram encontradas notas de entrada suficientes para atingirmos a quantidade do inventário\. As notas de entrada foram consultadas até: << informar a data preenchida no campo ‘Pesquisar Notas de Entrada até’”\. Favor rever esta situação\.” O log deve demonstrar as informações necessárias para permitir a identificação inventário, exibindo o estabelecimento, a data, produto,indicador, etc\)\.

<a id="RP05_GERAL_c180e185"></a>__Mensagens que devem ser apresentadas no Log do processamento \(C180/C185\):__

- Se existir informações no período para a tabela x296\_info\_compl\_st\_itens\_merc \([registros de origem via importação](#RP04_Dominio_Registros_Importados)\), o cálculo não será realizado\. Exibir a mensagem: “Existem dados importados através da SAFX296 – Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\) para o período, por isso, o cálculo não será realizado”\.\[MFS47079\] Aplicável a todas as notas de entradas e saídas\.
- Caso exista dados de Inventário no período e para a geração do registro C180 seja necessário buscar notas de entrada do período anterior a 01/01/2020 \(para compor a quantidade do inventário\), exibir a mensagem: “Conforme orientação do Guia Prático, favor entregar o arquivo Sintegra, Registro 88STITNF\. 

__Trecho do Manual:__ Se as notas fiscais que acobertam o estoque inicial declarado no ‘Bloco H’ tiverem sido escrituradas em data anterior a 01/01/2020, o contribuinte deverá apresentar o Registro 88STITNF do arquivo Sintegra para tais notas”\.

__\[MFS\-67654\]:__

- <a id="RP05_MG000"></a>Se a nota de saída não tiver__ restituição__ e nem __complemento__, exibir a mensagem no Log: “Não foi calculado complemento e nem restituição para o item da nota de saída\. Motivo MG000 não solicita esta informação\.”  

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, produto,indicador, etc\)\.\[MFS47079\] Aplicável apenas as Notas de Saídas Internas a Consumidor Final\.

__\[MFS\-67654\]:__

- Se os Códigos de Motivo de Restituição/Complementação de ICMS MG000, MG100, MG300 e MG200 não estiverem cadastrados\. Dar mensagem orientando para que se realize o cadastro no módulo Básicos > Data Warehouse, menu Manutenção >> Cadastros >> Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\. \[MFS47079\] Aplicável a todas as notas de saídas

<a id="RP05_GERAL_c330"></a>__Mensagens que devem ser apresentadas no Log do processamento \(C330\):__

- Se existir informações no período para a tabela x299\_inf\_comp\_st\_res\_mod\_02 \([registros de origem via importação](#RP04_Dominio_Registros_Importados)\), o cálculo não será realizado\. Exibir a mensagem: “Existem dados importados através da SAFX299 – Informações Complementares das Operações Sujeitas ao ST \(C330\) para o período, por isso, o cálculo não será realizado”\.
- Se o valor unitário da saída da mercadoria for igual a somatória da Base de Cálculo de ICMS\-ST unitária das entradas \(valor médio\), não teremos __restituição__ e nem __complemento__\. Para este cenário, exibir a mensagem no Log: “Não foi calculado complemento e nem restituição para a sequência dos itens da nota de saída\. Motivo MG000 não solicita esta informação\.”

O log deve demonstrar as informações necessárias para permitir a identificação das sequências dos itens dos documentos, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, produto,indicador, etc\)\.

<a id="RP05_GERAL_c430"></a>__Mensagens que devem ser apresentadas no Log do processamento \(C430\):__

- Se existir informações no período para a tabela x302\_inf\_comp\_st\_res\_it\_ecf \([registros de origem via importação](#RP04_Dominio_Registros_Importados)\), o cálculo não será realizado\. Exibir a mensagem: “Existem dados importados através da SAFX302 – Informações Complementares das Operações Sujeitas ao ST \(C430\) para o período, por isso, o cálculo não será realizado”\.
- Se o valor unitário da saída da mercadoria for igual a somatória da Base de Cálculo de ICMS\-ST unitária das entradas \(valor médio\), não teremos __restituição__ e nem __complemento__\. Para este cenário, exibir a mensagem no Log: “Não foi calculado complemento e nem restituição para o item da nota de saída\. Motivo MG000 não solicita esta informação\.”

O log deve demonstrar as informações necessárias para permitir a identificação do item do documento, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, produto,indicador, etc\)\.

- Ao gravar o registro calculado, se não existir informação no campo NUM\_CRZ para este cupom, o mesmo não será gravado na tabela  x302\_inf\_comp\_st\_res\_it\_ecf e a mensagem deve ser exibida: “O registro calculado não foi gravado na tabela, pois não há informação no campo NUM\_CRZ\. ”

O log deve demonstrar as informações necessárias para permitir a identificação do cupom, exibindo o estabelecimento, a data, o modelo, o número do item, produto,indicador, etc\)\.

<a id="RP05_GERAL_1250e1255"></a>__Mensagens que devem ser apresentadas no Log do processamento \(1250/1255\):__

- Se existir informações no período para a tabela x304\_saldo\_cons\_res\_comp\_icms \([registros de origem via importação](#RP04_Dominio_Registros_Importados)\), o cálculo não será realizado\. Exibir a mensagem: “Existem dados importados através da SAFX304 – Saldo Consolidado da Restituição/Complemento de ICMS \(1250/1255\) para o período, por isso, o cálculo não será realizado”\.
- Se não existir informações na tabela x296\_info\_compl\_st\_itens\_merc \(tanto pela importação, manutenção ou até mesmo pelo cálculo\), referente aos campos de saída \(campos 24 ao 32\), exibir a mensagem: Não há dados referente ao registro “c185”: Saída de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\), desta maneira, o cálculo dos registros 1250/1255 não será realizado\.

<a id="RP05_GERAL_h030"></a>__Mensagens que devem ser apresentadas no Log do processamento \(H030\):__

- Se não existir informações na tabela x52\_invent\_produto, para a realização do cálculo, exibir a mensagem: Não há dados na tabela de inventário para o cálculo ser executado\. O inventário recuperado para conseguirmos efetuar o cálculo é o inventário do período anterior ao informado na tela\.

Exibir no log, os registros que não foram atualizados, pois já existiam dados nos campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO e a opção ‘Sobrepor os valores calculados na tabela de inventário \(Registro H030\)’ estava desmarcada\. Neste cenário, exibir a mensagem: Registro não foi atualizado, pois existia valores nos campos de valores médios\.  O log deve demonstrar as informações necessárias para permitir a identificação inventário, exibindo o estabelecimento, a data, produto,indicador, etc\)\.

MFS\-33977

MFS\-35337

MFS\-35339

MFS\-35340

MFS\-39378

\[MFS47079\]

__MFS\-67654__

