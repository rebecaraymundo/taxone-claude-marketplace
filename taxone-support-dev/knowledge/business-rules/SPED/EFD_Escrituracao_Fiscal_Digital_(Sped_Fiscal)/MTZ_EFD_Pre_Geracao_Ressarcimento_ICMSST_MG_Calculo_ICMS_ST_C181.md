# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C181

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C181.docx
- **Modificado:** 2023-03-10
- **Tamanho:** 136 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Processamento do Cálculo ICMS\-ST – Registro C181

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

05/12/2022

MFS97773

Alteração na geração do registro C181\. Passar a preencher os campos 13, 14 e 15 para Código Motivo MG500 a partir de Janeiro de 2023\.

Ajuste na regra do campo 16\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV\_SAIDA das notas de devolução de saída para compatibilizar com a regra do campo 10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV do C185, que foi alterada pela MFS94229 para considerar a alíquota do FCP, além da alíquota interna do produto\.

Liliane Assaf

07/03/2023

MFS511653

Criação check\-box “Gerar Relatórios de Conferência” na tela da pré\-geração e aplicação na geração dos relatórios do registro C181 \(vide RP18\)

Liliane Assaf

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc37749427"></a>INTRODUÇÃO* *

Este documento contém as regras de geração do registro C181\.

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

RP18

MFS\-62563

Quando o parâmetro __*C181 – Devoluções de Saídas de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\)*__* estiver marcado na tela:* Todos os cálculos realizados por este processo serão armazenados na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV, referente às devoluções de saídas e serão utilizados para a geração do registro C181 do SPED FISCAL\.

O objetivo desta geração é calcular as informações de notas de devolução de saída, dos produtos sujeitos ao ICMS\-ST, e para isso além da nota de devolução, também deve ser recuperado o documento de saída referenciado pela devolução, que pode ser uma nota fiscal ou um cupom fiscal\.

__Pré\-Requisito__:

1\) Códigos de Motivos__ MG500__, __MG600 e MG800 __devem existir no cadastro do   módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação do ICMS \(SPED FISCAL\) – tabela DWT\_COD\_MOTIVO\_SPED\.

Caso não estejam cadastrados dar mensagem e abortar a geração do registro C181\.

Código XXXXX de Motivo de Restituição/Complementação do ICMS não cadastrado, por isso a pré\-geraçao do C181 não será realizada\.

Favor realizar o cadastro no módulo: Básicos > Data Warehouse, menu: Manutenção > Cadastros > Códigos de Motivo de Restituição/Complementação do ICMS \(SPED FISCAL\)\. Favor verificar o manual/help\.

Onde XXXXX é o código do motivo não cadastrado\.

2\) Não pode existir devoluções de saídas inseridas via importação:

Fazer uma consulta na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com os critérios a seguir:

\- Empresa de login

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal data enquadrada no período informado em tela;

\- Nota fiscal de devolução \(NORM\_DEV = “2”\);

\- Nota de Entrada \(MOVTO\_E\_S <> “9”\);

\- IND\_GRAVACAO <> '0', '6','7','8'\. \(caso que foi incluído via digitação ou importação\) então:

Caso a consulta acima retorne registro, dar mensagem e abortar a geração do registro C181\.:

“Existem notas de devolução de saídas importadas através da SAFX308 – “Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\)” para o período, por isso a pré\-geraçao do C181 não será realizada\.”

## 1 – Recuperação das Notas Fiscais de Devolução \(norm\_dev = ‘2’/ movto\_e\_s <> ‘9’\)

 __Origem dos dados__: \- Parametrização de Produtos 

                                  \- Parametrização de NCM’s; 

                                  \- Tabelas dos Documentos Fiscais \(SAFX07/SAFX08\); 

__Critérios da recuperação das Notas Fiscais de Devolução: __

  

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Entrada \(MOVTO\_E\_S <> “9”\);
- Nota fiscal de devolução \(NORM\_DEV = “2”\);
- Somente notas não canceladas; 
- Somente notas com itens; 
- Modelo – somente os documentos de modelo = 01, 1B, 04, 55 e 65;    
- Produto ou NCM \(sujeito ao ICMS\-ST\) \*\*
- CFOP ou CFOP/Natureza de Operação parametrizado para “Saída Interna para Consumidor Final \(e Devoluções\) \(art 31\-A \- Anexo XV do RICMS/02\)” 

\*\* __Produto ou NCM \(sujeito ao ICMS\-ST\)__

O produto do item deve constar na parametrização do Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà Produto ou parametrizado a NCM no Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà NCM\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma: 

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”; 

Para cada item de mercadoria da nota de devolução vamos recuperar a\(s\) nota\(s\) de saída\(s\) devolvida\(s\)\.

Primeiro buscar a saída a partir dos campos de referência da __SAFX08 __\(117, 118, 119, 102\)\. Caso esses campos não estejam preenchidos, buscar as saídas \(por notas\) referenciadas a partir da __SAFX192__, considerando campo “16\-Tipo de Referência” da SAFX192 = “__1__”\. 

Se o item de mercadoria da nota de devolução não tiver nenhuma das referências para nota de saída preenchidas, exibir a seguinte mensagem no log e não gravar a nota de devolução na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV:

*         “Registro C181: Nota de Devolução de saída não considerada na geração, pois não existe referência para operação de saída original\.*

*          Favor informar as saídas devolvidas na SAFX192 ou utilizar os campos de referência da SAFX08 \(117, 118, 119, 102\)\.”*

                                \(o log deve exibir a identificação do item da devolução para conferência do usuário\)

## <a id="_2.1_–_Recuperação"></a><a id="_Toc72506254"></a><a id="RP19_02"></a>2 – Recuperação das Notas Fiscais de Saídas referenciadas pela Devolução \(norm\_dev = 1 /movto\_e\_s = 9\)

Para cada item de mercadoria da nota de devolução recuperada conforme tópico 1, vamos recuperar as notas de saída devolvidas, referenciadas pela nota de devolução\. Esta referência pode ser de duas maneiras:

1. A nota de saída devolvida está identificada através dos campos de referência da __SAFX08 __\(117, 118, 119, 102\) do item da nota de devolução;
2. As notas de saídas devolvidas estão identificadas através da SAFX192 associado ao item da nota de devolução, considerando campo “16\-Tipo de Referência” da SAFX192 = “__1__”\.

OBS: Só estão sendo considerados os modelos de notas de saída que geram C185 \(01,1B, 04, 55 e 65\), uma vez que o registro C181 de Devolução de Saída determina que a saída, objeto da devolução deva estar escriturada num dos registros C185, C380, C480 ou C815\. Uma vez que o Ressarcimento MG não gera registros C380, C480, C815, então só podemos considerar as saídas escrituradas no C185\.

Abaixo estão definidas as duas formas de recuperar as notas de saída\.

__Recuperação das saídas referenciadas pela SAFX08:__

Caso o item de mercadoria da nota de devolução possua os campos 117, 118, 119, 102 \(SAFX08\) preenchidos, recuperar o documento de referência \(nota de saída devolvida\), a partir dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução

\- Estabelecimento      = Código do estabelecimento da nota de devoluçãounit\_

\- Movimento E/S        = deve ser uma nota de saída \(MOVTO\_E\_S = “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = mesma pessoa fis/jur da nota de devolução

\- Número                    = campo “117\-Número do Documento Fiscal de Referência” do item da nota de devolução

\- Série                         = campo “118\-Série do Documento Fiscal de Referência“ do item da nota de devolução

\- Subsérie                  = campo “119\-Subsérie do Documento Fiscal de Referência“ do item da nota de devolução

\- Data de Emissão     = campo “102\-Data DI / Data Doc Refer” do item da nota de devolução

\- Produto                    = produto do item da nota de devolução \(grupo,indicador e código\); 

\-  Modelo somente modelos de notas __01,1B, 04, 55 e 65__

Recuperar as seguintes informações da nota de saída referenciada \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de saída referenciada;

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

__OBS__: O uso dos campos de referência da SAFX08 da nota de devolução para identificar a nota de saída, espera\-se que apenas um item da nota de saída seja recuperado\. Mas, caso seja encontrado mais de um item da nota de saída para o produto devolvido, todos serão gravados na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\.  

O correto é utilizar os campos de referência da SAFX08 da nota de devolução quando apenas um item da nota de saída está relacionado ao produto devolvido\. Caso mais de um item de saída esteja relacionado ao produto devolvido, deve\-se utilizar a SAFX192\.

Crítica a ser realizada:

Caso a nota de referência não seja encontrada na base de dados, será gravada a seguinte mensagem no log: 

   “*Registro C181: Nota de Devolução de saída não considerada na geração, pois a nota de saída original referenciada no item da nota não foi encontrada na base de dados\.”*\. 

   \(o log deve exibir a identificação do item da devolução para conferência do usuário \+ campos 117, 118, 119, 102 que identifica a nota de saída referenciada\)

__Recuperação das saídas referenciadas na SAFX192:__

O item de mercadoria da nota de devolução pode ter um ou mais registros na SAFX192 com tipo de 16\-Tipo de Referência” = ‘1’ \- Devolução \(Entrada\) x Documentos de Origem \(Saídas\)\. Recuperar o\(s\) documento\(s\) de referência \(notas de saídas devolvidas\), a partir dos critérios descritos abaixo: 

SAFX192:

\- Campos 1 ao 15 da SAFX192 identificam o item da nota de devolução em questão;

\- Campo “16\-Tipo de Referência” da SAFX192 = “__1__”;

\- Campos 17 ao 23 identificam o item da nota de saída referenciado;

SAFX08:

Para cada documento de referência recuperado da SAFX192 \(identificado pelos campos 17 ao 23\), consultar a SAFX08 dos critérios descritos abaixo: 

\- Empresa                  = Código da empresa da nota de devolução \(campo 01 da SAFX192\)

\- Estabelecimento      = Código do estabelecimento da nota de devolução \(campo 02 da SAFX192\)

\- Movimento E/S        = deve ser uma nota de saída \(MOVTO\_E\_S = “9”\) 

\- Normal/Devolução   = deve ser uma nota normal \(NORM\_DEV = ‘1’\)

\- Pessoa Fis/Jur         = campos 21 e 22 \- Pessoa Física/Jurídica do Documento Fiscal de Referência \(SAFX192\)

\- Número                    = campo 17 \- Número do Documento Fiscal de Referência \(SAFX192\)

\- Série                         = campo 18 \- Série do Documento Fiscal de Referência \(SAFX192\)

\- Subsérie                  = campo 19\-Subsérie do Documento Fiscal de Referência \(SAFX192\)

\- Data Fiscal              = campo 20\- Data da Escrita Fiscal do Documento de Referência \(SAFX192\)

\- Num\. Item               = campo 23 \- Item da Nota Fiscal de Referência \(SAFX192\);

\-  Modelo somente modelos de notas __01,1B, 04, 55 e 65__

Recuperar as seguintes informações da nota de saída referenciada \(SAFX07/SAFX08\):

\- 11 \- Data da Emissão \- DATA\_EMISSAO \(SAFX07\)

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\- Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

\- 64 \- Valor Contábil do Item \- VLR\_CONTAB\_ITEM \(SAFX08\) 

Recuperar quantidade devolvida da SAFX192:

\- 24 \- Quantidade da Devolução

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

Obs\.: 

\- A tabela permite mais de uma nota de referência para um único item da nota de devolução\. Todos todos os itens devem ser gravados na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\. 

\-  A Quantidade da Devolução está expressa na mesma unidade de medida da nota de saída \(25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)\. Ou seja se eu vendi em litros, devolvo em litros\.

## <a id="_2.2_–_Recuperação"></a><a id="_2.3_–_Recuperação"></a><a id="_Toc72506256"></a>3 \- Recuperação dos Valores Unitários Médios referenciados pela SAÍDA objeto da devolução

Com o documento fiscal \(nota fiscal\) de saída, referenciado pela devolução, recuperado no tópico 2, vamos recuperar os valores unitários médios do dia da nota fiscal de saída\.

Se a nota de saída for de período anterior ao da geração, então buscar os valores unitários médios do C185 que está gravado na x296\_info\_compl\_st\_itens\_merc:

Consultar a tabela __x296\_info\_compl\_st\_itens\_merc__ \(C185\), com os dados chave do item de mercadoria da nota de saída e recuperar os campos:

26 \- Valor Unitário ICMS Estoque Conv\. \(Saídas\) \- VLR\_UNIT\_ICMS\_ESTQ\_SAI

27 \- Valor Unitário ICMS\-ST Estoque Conv\. \(Saídas\) \- VLR\_UNIT\_ICMSS\_ESTQ\_SAI

28 \- Valor Unitário FCP\-ST Estoque Conv\. \(Saídas\) \- VLR\_UNIT\_FCP\_ESTQ\_SAI

Valor Médio Unitário do ICMS = VLR\_UNIT\_ICMS\_ESTQ\_SAI

Valor Médio Unitário do ICMS\-ST = VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Valor Médio Unitário do FECEP\-ST = VLR\_UNIT\_FCP\_ESTQ\_SAI

Se a consulta acima não retornarem registro, gravar mensagem de erro no log:

*“Registro C181: Nota de saída objeto de devolução sem dados na tabela SAFX296\- “Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\)”\. A Nota de Devolução de saída será gerada no C181 sem valores unitários de ICMS, ICMS\-ST e FCP\-ST Estoque Conv \(campos 13, 14 e 15\)\. *

*Como solução, inclua os dados faltantes através do módulo Básicos >> Ware House, menu Manutenção>> Documento Fiscal >> Novo Documento Fiscal >> Doc\. Fiscal de Mercadoria \(Versão Anterior\)\. Na aba Item de Mercadoria, escolha a opção de menu “Informações Complementares Oper\. ST \(Sped Fiscal\)”\.*

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\.

Se a nota de saída for do período da geração, então recuperar os Valores Médios Unitário do dia da saída, da tabela de Média Ponderada \(__EST\_ST\_MG\_MEDIA\_POND__\), calculados na \([RP00B](#RP00B)\)\. 

              

Consultar a Tabela de Média Pondera \(__EST\_ST\_MG\_MEDIA\_POND__\) com os seguintes critérios:

\- Empresa login;

\- Estabelecimento selecionado na tela de geração;

\- Data = Data de Emissão da Nota fiscal de Saída \(SAFX07\) objeto da Devolução;

\- Produto = Produto do item da Nota de Devolução da Saída;

Recuperar os Valores Médios:

\- Valor Médio Unitário do ICMS \(VLR\_UNIT\_ICMS\_FIM\_MP\);

\- Valor Médio Unitário do ICMS\-ST c/ FECEP \(VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP\); 

\- Valor Médio Unitário da Base de Cálculo do ICMS\-ST \(VLR\_UNIT\_BC\_ST\_FIM\_MP\);

\- Valor Médio Unitário do FECEP\-ST \(VLR\_UNIT\_FECEP\_ST\_FIM\_MP\);

Se a consulta acima não retornarem registro, gravar mensagem de erro no log:

*“Registro C181: Não foi possível recuperar o valor unitário médio móvel calculado para DD/MM/YYYY, dia da saída objeto de devolução\. A Nota de Devolução de saída será gerada no C181 sem valores unitários de ICMS, ICMS\-ST e FCP\-ST Estoque Conv \(campos 13, 14 e 15\)\.*

DD/MM/YYYY é Data Fiscal da Nota de Devolução da Saída\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada, exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\.

## 4 – Gravação dos Dados na tabela x308\_info\_compl\_st\_it\_merc\_dev

Os documentos fiscais de Devolução recuperados serão gravados__ item a item__, com todas as referências para as notas fiscais de saídas devolvidas, conforme definido a seguir\.

Gravar a tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com IND\_GRAVACAO = ‘6’;

PK

Item

SAFX308

Campo

Regra de Preenchimento

__*Campos do layout da SAFX308 \(Item da nota de devolução com item da nota/cupom de saída objeto da devolução\)*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Devolução da Saída \(SAFX07\) 

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento da nota de Devolução da Saída \(SAFX07\)

\(\*\)

03

Data Escrita Fiscal \(NF Devolução\)

DATA\_FISCAL

Data fiscal da nota de Devolução da Saída \(SAFX07\) recuperada no tópico 1\.

\(\*\)

04

Movimento Entrada / Saída \(NF Devolução\)

MOVTO\_E\_S

Indicador do movimento da nota de Devolução da Saída \(SAFX07\) recuperada no tópico 1\.

\(\*\)

05

Normal ou Devolução \(NF Devolução\)

NORM\_DEV

Indicando de Normal/Devolução da nota de Devolução da Saída \(SAFX07\) recuperada no tópico 1\.

\(\*\)

06

Tipo do Documento \(NF Devolução\)

COD\_DOCTO 

\(IDENT\_DOCTO\)

Tipo do documento da nota de Devolução da Saída recuperada no tópico 1\.

\(\*\)

07

08

Pessoa Física/Jurídica \(NF Devolução\)

IND\_FIS\_JUR/ COD\_FIS\_JUR

\(IDENT\_FIS\_JUR\)

Pessoa física/jurídica da nota de Devolução da Saída \(SAFX07\) recuperada no tópico 1\.

\(\*\)

09

Número do Documento Fiscal \(NF Devolução\)

NUM\_DOCFIS

Número do documento fiscal da Devolução da Saída recuperada no tópico 1\.

 \(\*\)

10

Série do Documento Fiscal \(NF Devolução\)

SERIE\_DOCFIS

Série do documento fiscal da Devolução da Saída recuperada no tópico1\.

 \(\*\)

11

Subsérie do Documento Fiscal \(NF Devolução\)

SUB\_SERIE\_DOCFIS

Subsérie do documento fiscal da Devolução da Saída recuperada no tópico 1\.

\(\*\)

12 13 14 15

Identificador do Item do Documento Fiscal \(NF Devolução\)

DISCRI\_ITEM

Campo identificador do item de mercadoria da Devolução da Saída 

\(DISCR\_ITEM da X08\_ITENS\_MERC\) recuperada no tópico 1\.

\(\*\)

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


\(\*\) 

17

Número do Documento Fiscal de Referência \(NF Saída\)

NUM\_DOCFIS\_REF

Preencher com Número da nota fiscal de saída referenciada, cfm tópico 2\.

 \(\*\)

18

Série do Documento Fiscal de Referência \(NF Saída\)

SERIE\_DOCFIS\_REF

Preencher com Série da nota fiscal de saída referenciada, cfm tópico 2\.

 \(\*\)

19

Subsérie do Documento Fiscal de Referência \(NF Saída\)

SUB\_SERIE\_DOCFIS\_REF

Preencher com Subsérie da nota fiscal de saída referenciada, cfm tópico 2\.

 \(\*\)

20

Tipo do Documento de Referência \(NF Saída\)

COD\_DOCTO\_REF

\(IDENT\_DOCTO\_REF\)

Preencher com Tipo do documento fiscal da nota fiscal de saída referenciada cfm

   tópico 2, de acordo com a Tabela de Tipos de Documentos \(SAFX2005\)\.

 \(\*\)

21

Data Escrita Fiscal do Documento de Referência \(NF Saída\)

DATA\_FISCAL\_REF

Preencher com Data da Fiscal da nota fiscal de saída referenciada, cfm tópico 2\.

 \(\*\)

22

23

Pessoa Física/Jurídica do Documento de Referência \(NF Saída\)

IND\_FIS\_JUR\_REF/ COD\_FIS\_JUR\_REF

\(IDENT\_FIS\_JUR\_REF\)

Preencher com Pessoa física/jurídica da nota fiscal de saída referenciada, cfm 

    no tópico 2, de acordo com a Tabela de Pessoas Físicas/Jurídicas \(SAFX04\)\.         

 \(\*\)

24

Modelo do Cupom Fiscal de Referência

COD\_MODELO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\. 

 \(\*\)

25

Número do Caixa do Cupom Fiscal de Referência

COD\_CAIXA\_ECF\_REF

\(IDENT\_CAIXA\_ECF\)

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

 \(\*\)

26

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência

NUM\_COO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

 \(\*\)

27

Data de Emissão do Cupom Fiscal de Referência

DATA\_EMISSAO\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal ECF\.

 \(\*\)

28

Número do Equipamento SAT do Cupom Fiscal de Referência

NUM\_EQUIP\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\. 

 \(\*\)

29

Número do Cupom Fiscal do Referência 

NUM\_CUPOM\_REF

Não preencher, pois é referente a devolução de saída por cupom fiscal SAT\.

\(\*\)

30

Número do Item do Documento de Referência \(NF Saída\)

NUM\_ITEM\_DOC\_REF

Preencher com Número do Item da nota fiscal referenciada, cfm tópico 2\.

31

Código Motivo

Campos da EFD correspondentes: 02 do C181 e 06 do C186\.

COD\_MOTIVO

Preencher com:

- MG500 – para devolução de saída sem restituição e sem complemento;
- MG600 – para Estorno de Restituição
- MG800 – para Estorno de Complemento

Regra:

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) então:

   A saída referenciada pela devolução obteve Restituição \(MG100\);

   Preencher com “__MG600__” – Estorno do Ressarcimento\-ST;

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) então:

   A saída referenciada pela devolução obteve Complemento \(MG300\);

   Preencher com “__MG800__” – Estorno do Complemento\-ST;

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI = 0 \(entrada = saída\) então: 

   A saída referenciada pela devolução não teve nem Restituição nem 

   Complemento\.

   Preencher com “__MG500__”

32

Quantidade Convertida

Campos da EFD correspondentes: 03 do C181 e 07 do C186\.

QTD\_CONV

Preencher com a quantidade de devolução convertida\.

- Caso a nota fiscal de saída esteja associada à nota de Devolução pela __SAFX192__:

Preencher com:

“Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) \([QTD\_CONV\_REF\_DEV](#QTD_CONV_REF_DEV)\)” 

- Caso a nota de saída esteja associada à nota de devolução pela __SAFX08__:

Preencher com:

“Qtde Convertida Calculada para NF de Devolução de Saída \(safx08\) \([QTD\_CONV\_NF\_DEV](#QTD_CONV_NF_DEV)\)”

Ver [__*Detalhamento da Nota de Devolução*__](#Detalha_NF_DEV)

33

Unidade de Medida

Campos da EFD correspondentes: 04 do C181 e 08 do C186\.

COD\_MEDIDA

Campo 14 – Unidade de Medida do Cadastro do Produto \(SAFX2013\), do produto pertencente ao item da nota de Devolução da Saída, recuperada no tópico 1\.

 

 

34

Valor Unitário Conv

Campos da EFD correspondentes: 12 do C181 e 15 do C186\.

VLR\_UNIT\_CONV

Preencher com:

    VLR\_UNIT\_CONV = VLR\_CONTAB\_ITEM da SAFX08 / QTD\_CONV\_NF\_SAI

    Onde:

- VLR\_CONTAB\_ITEM é o campo 64\-valor Contabil do Item da nota de saída referenciada;
- QTD\_CONV\_NF\_SAI: “Qtde Convertida Calculada para o Item da NF de Saída Referenciada \([QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI)\)”” 

    Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

 

35

Valor Unitário ICMS OP Conv

Campos da EFD correspondentes: 17 do C181 e 16 do C186

VLR\_ICMS\_CONV

Não preencher\. 

 

36

Valor Unitário Base ICMS ST Conv da Entrada

Campo da EFD correspondente: 17 do C186\.

VLR\_UNIT\_BC\_ICMSS\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.   


 

37

Valor Unitário ICMS ST Conv da Entrada

Campo da EFD correspondente: 18 do C186\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

 

38

Valor Unitário FCP ST Conv da Entrada

Campo da EFD correspondente: 19 do C186\.

VLR\_UNIT\_FCP\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

 

39

Valor Unitário ICMS OP Estoque Conv

Campo da EFD correspondente: 13 do C181\.

VLR\_UNIT\_ICMS\_ESTQ\_SAI

Esse campo será preenchido de acordo com o campo COD\_MOTIVO:

- MG500 – para devolução de saída sem restituição e sem complemento;
- MG600 – para Estorno de Restituição
- MG800 – para Estorno de Complemento

__\[MFS97773\]: MG500 passa a preencher o campo 13, 14 e 15 do C181__

Se COD\_MOTIVO = __MG500__ e período da geração é anterior a Jan/2023 então:

    Não Preencher

Senão:

Preencher com o “Valor Médio Unitário do ICMS” recuperado da “Média Ponderada Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\) ou da X296, conforme tópico 3, para o Produto na Data de Emissão da nota de saída referenciada\. 

    \(campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\) ou

    \(campo VLR\_UNIT\_ICMS\_ESTQ\_SAI da X296\_info\_compl\_st\_itens\_merc\);

  


40

Valor Unitário ICMS ST Estoque Conv

Campo da EFD correspondente: 14 do C181\.

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

Esse campo será preenchido de acordo com o campo COD\_MOTIVO:

- MG500 – para devolução de saída sem restituição e sem complemento;
- MG600 – para Estorno de Restituição
- MG800 – para Estorno de Complemento

__\[MFS97773\]: MG500 passa a preencher o campo 13, 14 e 15 do C181__

Se COD\_MOTIVO = __MG500__ e período da geração é anterior a Jan/2023 então:

    Não Preencher

Senão:

Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado da “Média Ponderada Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\) ou da X296, conforme tópico 3, para o Produto na Data de Emissão da nota de saída referenciada\. 

   \(campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP EST\_ST\_MG\_MEDIA\_POND\) ou

                 \(campo VLR\_UNIT\_ICMSS\_ESTQ\_SAI da X296\_info\_compl\_st\_itens\_merc\);

 

41

Valor Unitário FCP ICMS ST Estoque Conv

Campo da EFD correspondente: 15 do C181\.

VLR\_UNIT\_FCP\_ESTQ\_SAI

Esse campo será preenchido de acordo com o campo COD\_MOTIVO:

- MG500 – para devolução de saída sem restituição e sem complemento;
- MG600 – para Estorno de Restituição
- MG800 – para Estorno de Complemento

__\[MFS97773\]: MG500 passa a preencher o campo 13, 14 e 15 do C181__

Se COD\_MOTIVO = __MG500__ e período da geração é anterior a Jan/2023 então:

    Não Preencher

Senão:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado da “Média Ponderada Móvel dos Valores Unitários” \(EST\_MG\_RS\_MEDIA\_POND\) ou da X296, conforme tópico 3, para o Produto na Data de Emissão da nota de saída referenciada\. 

    \(campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\) ou

    \(campo VLR\_UNIT\_FCP\_ESTQ\_SAI da X296\_info\_compl\_st\_itens\_merc\);

 

42

Valor Unitário ICMS na Operação Conv

Campo da EFD correspondente: 16 do C181\.

VLR\_UNIT\_ICMS\_OPER\_SAI

__MFS97773: Inclusão da Alíquota FCP somada a alíquota interna \-compatibilizar com a regra do campo 10 do C185\.__

Esse campo será preenchido de acordo com o campo COD\_MOTIVO:

- MG500 – para devolução de saída sem restituição e sem complemento;
- MG600 – para Estorno de Restituição
- MG800 – para Estorno de Complemento

Se COD\_MOTIVO = MG500 então:

    Não Preencher

Se COD\_MOTIVO = MG600 ou MG800, então:

    Preencher com   BC\-Saída \* Alíquota / 100

__    __Truncar o resultado acima em 6 decimais\.

Onde:

- Alíquota = Alíquota Interna \+ Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

- \(BC\-Saída\): 

       Para Nota Fiscal de saída referenciada pela devolução:

    “Valor Unitário da BC do ICMS na Operação Conv \([BC\-Saída](#BC_SAIDA)\)”

    Ver  [*Detalhamento da Nota de Saída Referenciada pela Devolução*](#Detalha_NF_SAI)\.

__ __

 

43

Valor Unitário ICMS ST Conv Rest

Campo da EFD correspondente: 18 do C181\.

VLR\_UNIT\_ICMSS\_REST\_SAI

Campo referente ao estorno de Complemento \(COD\_MOTIVO = MG800\), logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Complemento\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) então:

   Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_OPER\_SAI \- 

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \- 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI: valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Senão:

   Não preencher

 

44

Valor Unitário FCP ST Conv Rest

Campo da EFD correspondente: 19 do C181\.

VLR\_UNIT\_FCP\_REST\_SAI

Campo referente ao estorno de Complemento FECEP \(COD\_MOTIVO = MG800\), logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Complemento\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI < 0 \(entrada < saída = complemento\) e 

    campo 41 \- VLR\_UNIT\_FCP\_ESTQ\_SAI maior que zero, então:

   Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_REST\_SAI \* Alíquota FCP / 100

Onde:

- VLR\_UNIT\_ICMSS\_REST\_SAI: valor gravado no campo 43\-Valor Unitário ICMS ST Conv Rest;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

Senão:

   Não preencher

 

45

Valor Unitário ICMS ST Conv Compl

Campo da EFD correspondente: 20 do C181\.

VLR\_UNIT\_ICMSS\_COMPL\_SAI

Campo referente ao estorno de Restituição \(COD\_MOTIVO = MG600\), logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Restituição\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) então:

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

    VLR\_UNIT\_ICMSS\_ESTQ\_SAI – 

    VLR\_UNIT\_ICMS\_OPER\_SAI  

    Onde:

- VLR\_UNIT\_ICMS\_OPER\_SAI: valor gravado no campo 42\-Valor Unitário ICMS na Operação Conv;
- VLR\_UNIT\_ICMS\_ESTQ\_SAI : valor gravado no campo 39\- Valor Unitário ICMS OP Estoque Conv;
- VLR\_UNIT\_ICMSS\_ESTQ\_SAI: valor gravado no campo 40\-Valor Unitário ICMS ST Estoque Conv;

Senão:

   Não preencher

 

46

Valor Unitário FCP ST Conv Compl

Campo da EFD correspondente: 21 do C181\.

VLR\_UNIT\_FCP\_COMPL\_SAI

Campo referente ao estorno de Restituição FECEP \(COD\_MOTIVO = MG600\), logo deve ser preenchido no caso da saída referenciada tenha sido objeto de Restituição\.

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

    VLR\_UNIT\_ICMS\_OPER\_SAI > 0 \(entrada > saída = ressarcimento\) e

    campo 41 \- VLR\_UNIT\_FCP\_ESTQ\_SAI maior que zero, então

    Preencher com o resultado da fórmula:

    VLR\_UNIT\_ICMSS\_COMPL\_SAI \* Alíquota FCP / 100

    Onde:

- VLR\_UNIT\_ICMSS\_COMPL\_SAI: valor gravado no campo 45\-Valor Unitário ICMS ST Conv Compl;
- Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;

Ver [Detalhamento da Parametrização por Produto](#Detalha_Parametrização_Produto)

Senão:

   Não preencher

__Detalhamento das Regras:__

<a id="Detalha_Parametrização_Produto"></a>__Detalhamento da Parametrização do Produto \(por Código, NCM\)__

Recuperar os campos %Redução BC,  Alíquota Interna,  Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada\.

__Atenção__: para busca da Alíquota Interna, Alíquota FCP e %Redução de BC, considerar a parametrização vigente __na Data de Emissão da NF de Saída__ e não a vigente no período da geração\.

Isso porque os cálculos devem bater com os valores apresentados no C185 dessa nota de saída\.

Caso não seja encontradada parametrização do Produto \(menu “Parâmetros à Ressarcimento ICMS\-ST 🡪 Produtos”, ou, “Parâmetros à Ressarcimento ICMS\-ST à NCM”, exibir a seguinte mensagem:

 “*Registro C181: Não foi encontrada Parametrização por Código, NCM ou para o produto da Nota de Devolução de Saída, vigente na Data de Emissão da Saída <DD/MM/AAAA>\. Sem a definição da Alíquota Interna o registro C181 será gerado sem valor unitário de ICMS \(campo 16\)”\.*

Onde: DD/MM/AAAA é a Data de Emissão da NF de Saída\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

<a id="Detalha_NF_DEV"></a>__Detalhamento da Nota de Devolução__

- “__Qtde da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) \(__<a id="QTD_CONV_REF_DEV"></a>__QTD\_CONV\_REF\_DEV\)__”:

Considerar o campo 24 \- Quantidade da Devolução \(QTD\_DEVOL\) da SAFX192, recuperada no tópico 2\.

Calcular a Quantidade da Devolução Convertida Calculada p/ Saída Referenciada \(safx192\) \(QTD\_CONV\_REF\_DEV\) pela regra abaixo:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto 

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 da NF Devolução da Saída \(reg pai\)

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria Quantidade da Devolução da SAFX192 \(QTD\_DEVOL\);

__Senão __

         Nesse caso a quantidade da Devolução \(QTD\_DEVOL\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade da Devolução \(SAFX192\) \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem informação no campo 03 \- Quantidade Convertida\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

*\(essa mensagem não precisa ser dada pois é a mesma já especificada no campo QTD\_CONV\_NF\_DEV\)*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

- __Qtde Convertida Calculada para NF de Devolução de Saída \(safx08\) \(__<a id="QTD_CONV_NF_DEV"></a>__QTD\_CONV\_NF\_DEV\)”:__

Considerar os campos do item da nota de Devolução de saída, recuperada no tópico 1:

- Campo 24\-Quantidade \(SAFX08\) 
- Campo 137 – Quantidade Convertida \(SAFX08\)
- Campo 25 – Unidade de Medida \(SAFX08\) 

Calcular a Quantidade Convertida para NF de Devolução de Saída \(safx08\) \(QTD\_CONV\_NF\_DEV\) pela regra abaixo:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade do item da nota \(SAFX08\) \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem informação no campo 03 \- Quantidade Convertida\. Favor rever medida da NF de devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)\.

   

<a id="Detalha_NF_SAI"></a>__[Detalhamento da Nota de Saída Referenciada pela Devolução](#Detalha_NF_SAI)__

- __Qtde Convertida Calculada para o Item da NF de Saída Referenciada \(__<a id="QTD_CONV_NF_SAI"></a>__QTD\_CONV\_NF\_SAI\)__

Considerar os campos do item da nota de saída, recuperada no tópico 2:

- Campo 24\-Quantidade \(SAFX08\) 
- Campo 137 – Quantidade Convertida \(SAFX08\)
- Campo 25 – Unidade de Medida \(SAFX08\) 

Calcular a Quantidade Convertida Calculada para o Item da NF de Saída Referenciada \(QTD\_CONV\_NF\_SAI\) pela regra abaixo:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)  __

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Saída Referenciada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do

      item da nota;

__Senão __

     Se existir informação no campo “137\-Quantidade Convertida” do item \(SAFX08\)

         Nesse caso, será utilizada a informação da quantidade já convertida do campo “137\-Quantidade Convertida”;

     Senão         

         Nesse caso a quantidade do item \(SAFX08\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade do item da nota \(SAFX08\) \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas será gravada a seguinte mensagem de erro no log:

“*Registro C181: Fator de conversão de medida de XXX para XXX não encontrado\. Nota de Devolução de saída será gerada no C181 sem valores unitários da Mercadoria e ICMS \(campos 12 e 16\)”\. Favor rever medida da NF de saída referenciada pela devolução e Cadastro de Conversão de Unidades de Medida, no módulo DW, menu Manutenção >> Cadastros >> Conversão de Unidades de Medida\.”*

\(O primeiro “XXX” é a unidade do movimento, e o segundo “XXX”, a unidade do cadastro do produto\)\.

O log deve demonstrar as informações necessárias para permitir a identificação do item da Nota de Devolução da Saída e da Saída referenciada exibindo o estabelecimento, a data, o número do documento, pessoa fis/jur, o número do item, etc \.\.\.\)

- __Valor Unitário da BC do ICMS na Operação Conv \(__<a id="BC_SAIDA"></a>__BC\-Saída\)__

Calcular conforme regra:

Se o campo “__%Redução BC__” da parametrização de Produto ou NCM ou CEST está preenchido com valor > 0, então:

  Este campo será gerado da seguinte forma:

  \[\(Vlr Contábil – \(Vlr Contábil \* “%Redução BC” / 100\)\)\]/ QTD\_CONV\_NF\_SAI

Senão:

  Este campo será gerado da seguinte forma:

  \[\(Vlr Contábil\)\] / QTD\_CONV\_NF\_SAI

Onde:

- %Redução BC da parametrização de Produto ou NCM ou CEST sujeito ao ICMS\-ST, vigente na __Data de Emissão da Saída__ referenciada;
- Vl Contábil = 64\-Vlr Contabil do Item da nota fiscal de saída referenciada, recuperada no tópico 2\.
- [QTD\_CONV\_NF\_SAI](#QTD_CONV_NF_SAI): Qtde Convertida Calculada para o Item da Nota de Saída referenciada, recuperada no tópico 2\. 

## 4 – Gerar relatório a partir da tabela x308\_info\_compl\_st\_it\_merc\_dev

\[MFS511653\]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré\-geração:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, disponibilizar um arquivo Excel com as notas de devolução de saída consideradas para o registro C181\.

Nome do arquivo: Relatório\_Conferencia\_C181\_mm\_aaaa\_cod\_estab\.csv

Para isso fazer uma leitura na tabela X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV com os seguintes critérios:

\- empresa de login;

\- estabelecimento selecionado na tela de geração;

\- data fiscal compreendida no Período informado na tela de Geração;

\- Movimento E/S <> ‘9’ \(entrada\)

Ordenar as notas pelos campos: empresa, estabelecimento, data fiscal, número do documento fiscal, número do item de mercadoria\.

Obs: campos a seguir não devem ser demonstrados no relatório:

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

36

Valor Unitário Base ICMS ST Conv da Entrada

Campo da EFD correspondente: 17 do C186\.

VLR\_UNIT\_BC\_ICMSS\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.   


37

Valor Unitário ICMS ST Conv da Entrada

Campo da EFD correspondente: 18 do C186\.

VLR\_UNIT\_ICMSS\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

38

Valor Unitário FCP ST Conv da Entrada

Campo da EFD correspondente: 19 do C186\.

VLR\_UNIT\_FCP\_CONV\_ENT

Não Preencher\. Esse campo da SAFX308 é utilizado nas Devoluções de Entradas\.

No relatório, ao invés de demonstrar o DISCRI\_ITEM da nota de devolução, apresentar o produto \(indicador e  código\) e o número do item:

\(\*\)

12 13 14 15

Identificador do Item do Documento Fiscal \(NF Devolução\)

DISCRI\_ITEM

Campo identificador do item de mercadoria da Devolução da Saída 

\(DISCR\_ITEM da X08\_ITENS\_MERC\) recuperada no tópico 1\.

MFS\-62563

