# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C180_C185

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST_C180_C185.docx
- **Modificado:** 2024-07-02
- **Tamanho:** 139 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Processamento do Cálculo ICMS\-ST – Registros C180 e C185

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

Inclusão da recuperação das notas de devolução na geração do registro C185, conforme a resposta de orientação da SEFAZ\-MG, para as notas fiscais de Fato Gerador Presumido Não Realizado\.

Andréa Rocha

24/08/2021

MFS\-71205

RP03: Registro C180:

Alteração na regra de preenchimento do campo 18 \- VLR\_UNIT\_CONV da X296\_info\_compl\_st\_itens\_merc

Andréa Rocha

03/09/2021

MFS\-58456

Inclusão do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Tela de Geração e tratamento na geração dos registros C180, C186, H030, Cálculo do Valores Médios do Inventário e Cálculo da Média Ponderada do Diária Produto\.

Liliane Assaf

06/10/2021

MFS\-73772

Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada e suas devoluções, na geração do registro C180\.

Andréa Rocha

28/10/2021

MFS74901

Alteração do preenchimento do campo código do motivo para a operação de “Devolução de Entrada Interestadual”\.

Andréa Rocha

13/12/2021

MFS76604

Alteração do preenchimento do campo 15\- VL\_UNIT\_ICMS\_ST\_CONV\_REST do registro C185, para seguir a regra do guia prático para a não ocorrência do fato gerador presumido\.

Andréa Rocha

28/12/2021

MFS78490

Alteração do preenchimento do campo 02\-COD\_RESP\_RET do registro C180, para o código 3\-Próprio declarante\.  Essa alteração está sendo feito com base na reunião de alinhamento feita com a área de informação\.

Andréa Rocha

28/12/2021

MFS78492

Alteração do preenchimento do campo 05\-VL\_UNIT\_CONV do registro C180\.  Essa alteração está sendo feito com base na reunião de alinhamento feita com a área de informação\.

Andréa Rocha

28/12/2021

MFS77170

Alteração do preenchimento do campo 16\-VL\_UNIT\_FCP\_ST\_CONV\_REST do registro C185, para a situação de não ocorrência do fato gerador presumido\.

Andréa Rocha

15/09/2022

MFS93821

Alteração da regra de recuperação das notas de entrada para a geração do registro C180\.  Devem ser recuperadas todas as notas de entrada existentes no mês, sem limitar à quantidade do saldo de inventário do mês\.

Andréa Rocha

30/09/2022

MFS94229

Alteração da regra de preenchimento do campo 10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV das notas de saída para a geração do registro C185\.  O cálculo do campo passará a considerar a alíquota do FCP, além da alíquota interna do produto\.

Andréa Rocha

05/10/2022

MFS94486

Alteração da regra de preenchimento do campo 16 \- VL\_UNIT\_FCP\_ST\_CONV\_RES das notas de saída para a geração do registro C185\.  O cálculo do valor passará a ser feito utilizando a base de cálculo do ICMS\-ST, em vez de utilizar o valor unitário do ICMS\-ST, conforme verificado com a área de informação\.

Andréa Rocha

05/10/2022

MFS94488

Alteração da regra de preenchimento do campo 18 \- VL\_UNIT\_FCP\_ST\_CONV\_COMPL das notas de saída para a geração do registro C185\.  O cálculo do valor passará a ser feito utilizando a base de cálculo do ICMS\-ST, em vez de utilizar o valor unitário do ICMS\-ST, conforme verificado com a área de informação\.

Andréa Rocha

05/12/2022

MFS97773

Alteração na geração do registro C185\. Passar a preencher os campos 12, 13, 14 para Código Motivo MG000 a partir de Janeiro de 2023\.

Liliane Assaf

06/02/2023

MFS509134

Alteração da regra de preenchimento do campo 05 \- VL\_UNIT\_CONV do registro C180\.  O cálculo do campo passará a desconsiderar o valor do IPI não escriturado, conforme verificado com a área de informação\.

Andréa Rocha

07/03/2023

MFS511653

Criação do Relatório de Conferência do registro C185 \(vide [RP06](#RP06)\)

Liliane Assaf

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc37749427"></a>INTRODUÇÃO* *

Este documento contém as regras de geração dos registros C180 e C185\.

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

<a id="RP01_RecuperacaoC180"></a>RP01

Quando o parâmetro __*C180 – Entrada de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\)*__* estiver marcado na tela:* Todos os cálculos realizados por este processo serão armazenados na tabela x296\_info\_compl\_st\_itens\_merc, referente às entradas e serão utilizados para a geração do registro C180 do SPED FISCAL\.

 __Origem dos dados__: \- Parametrização de Produtos 

                                  \- Parametrização de NCM’s; 

                                \- Parametrização de CFOP ou CFOP/Natureza de Operação; 

                                  \- Tabelas dos Documentos Fiscais \(SAFX07/SAFX08\); 

                                  \- Tabela de Inventário \(SAFX52\)

 

O objetivo desta geração é calcular as informações de notas de entrada, dos produtos sujeitos ao ICMS\-ST para a tabela x296\_info\_compl\_st\_itens\_merc

__\[MFS93821\]__ Alteração da regra de recuperação das notas de entrada para passar a recuperar todas as notas de entrada que se encontram no mês da geração, sem limitar à quantidade do saldo de inventário do mês\.

__\[MFS73772\] __Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada

 

<a id="RP03_tabela_registros_c180_c185"></a><a id="Criterios_Notas_Entradas_RP001"></a>__Critérios da recuperação das Notas Fiscais: __ 

 

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Entrada;
- Somente notas *não canceladas* e que não sejam de devolução; 

\(27/05/2020:  Feito consulta com a SEFAZ sobre considerar ou não as notas de devolução\)\.

- Somente notas *com itens*; 
- Modelo – somente os documentos de modelo = __*01, 1B, 04, 55 e 65*__;    
- [Produto ou NCM \(sujeito ao ICMS\-ST\)\*\*](#ProdutoouNCMsujeitosaICMSST)
- CFOP ou CFOP/Natureza de Operação parametrizado para “Entrada \(e Devolução\)”;

<a id="SituacaoEspecial"></a>__\* Situação Especial__

Quando uma das datas \(Data Cisão, Data Fusão ou Data Incorporação\) estiver preenchida na tabela de estabelecimento e esta data compreender o período da geração do cálculo\. A data do evento \(situação especial\) consiste na data indicada nestes campos\.

<a id="ProdutoouNCMsujeitosaICMSST"></a>\*\* __Produto ou NCM \(sujeito ao ICMS\-ST\)__

O produto do item ou inventário deve constar na parametrização do Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà Produto ou parametrizado a NCM no Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-STà NCM\. 

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\. 

A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma: 

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”; 

Recuperando Itens de Documentos de Entrada \(Utilizadas para a Geração do Registro C180 da EFD\) sem verificar a existência de estoque:

Considerar todas as notas fiscais de entrada do período, conforme regras indicadas nos [critérios da recuperação de notas fiscais](#Criterios_Notas_Entradas_RP001), para os produtos ou NCMs parametrizados \(sujeitos ao ICMS\-ST\) e CFOPs parametrizados\.

Verificar a [RP03](#RP03_gravacao) \(gravação das informações\)

__Validações__

Considerar as validações na RP05 \([Mensagens que devem ser apresentadas no Log do processamento](#RP05_GERAL) e [Mensagens que devem ser apresentadas no Log do processamento \(C180/C185\)\)](#RP05_GERAL_c180e185)

MFS\-33977

MFS\-38251

MFS47248

MFS\-73772

MFS\-93821

<a id="RP02_Regras185_precomedio_conversao"></a>RP02

Quando o parâmetro __*C185 –Saída de mercadorias sujeitas à substituição tributária \(01,1B, 04, 55 e 65\)*__*,* estiver marcado na tela: Todos os cálculos realizados por este processo serão armazenados na tabela x296\_info\_compl\_st\_itens\_merc, referente aos campos de saída e serão utilizados para a geração do registro C185 do SPED FISCAL\.

## 1 – Recuperação das Notas Fiscais de Saídas \(norm\_dev = ‘1’/ movto\_e\_s = ‘9’\)

<a id="RP02_CRIT_NOTAS_SAIDA"></a>__Critérios da recuperação das Notas Fiscais de Saídas Interna para Consumidor Final: __ 

 

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Saída;
- Somente notas *não canceladas *e que não sejam de devolução; 

\(27/05/2020:Feito consulta com a SEFAZ sobre considerar ou não as notas de devolução\)

- Somente notas *com itens*; 
- Modelo somente modelos de notas 01,1B, 04, 55 e 65    
- Produto ou NCM \(sujeito ao ICMS\-ST\)\*\* 
- CFOP ou CFOP/Natureza de Operação parametrizado para “Saída Interna para Consumidor Final \(e Devoluções\) \(art 31\-A \- Anexo XV do RICMS/02\)” \[MFS47079\]

\[MFS47079\]

__Critérios da recuperação das Notas Fiscais de Saídas de Fato Gerador Presumido Não Realizado: __ 

 

\[MFS70215\] Inclusão da recuperação das notas de devolução interestadual, conforme orientação da SEFAZ\-MG

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Saída;
- Somente notas *não canceladas *e que não sejam de devolução; 
- Considerar somente as notas de devolução interestadual \(NORM\_DEV = “2”\), que tenham o CFOP ou CFP/Natureza de Operação parametrizado para a operação: Devolução de Entrada Interestadual; 
- Somente notas *com itens*; 
- Modelo somente modelos de notas 01,1B, 04, 55 e 65    
- Produto ou NCM \(sujeito ao ICMS\-ST\)\*\* 
- CFOP ou CFOP/Natureza de Operação parametrizado para as operações:
	- Saída para Outras Unidade da Federação  \(art 23 \- Anexo XV do RICMS/02\)
	- Saída com Isenção ou não Incidência \(art 23 \- Anexo XV do RICMS/02\)
	- Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda \(art 23 \- Anexo XV do RICMS/02\)

 

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

Verificar a [RP03](#RP03_gravacao) \(gravação das informações\)

__Atenção:__ Como pré\-requisito, para a gravação do cálculo dos registros de saída, será necessário ter efetuado o cadastro dos códigos de motivo de restituição ou complemento \(MG000, MG100 e MG300\) na tela “Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\), localizada em MasterSAF\-DWàBásicos àData Warehouse à Manutenção  Cadastros à Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\)\.

__Validações__

Considerar as validações na RP05 \([Mensagens que devem ser apresentadas no Log do processamento](#RP05_GERAL) e [Mensagens que devem ser apresentadas no Log do processamento \(C180/C185\)\)](#RP05_GERAL_c180e185)

MFS\-33977

MFS\-38251

MFS\-39378

MFS47079

MFS47248

MFS\-67654

MFS\-

70215

<a id="RP03_gravacao"></a>RP03

Gravar os registros na tabela x296\_info\_compl\_st\_itens\_merc, conforme regras indicadas nos respectivos campos indicado na tabela abaixo, \(considerando __cada item de documento de entrada__ que foi recuperado na [RP01](#RP01_RecuperacaoC180)\), __para os registros C180__\. __Para os registros C185__, apresentar __APENAS__ os itens de nota de saída de modelo igual a __01,1B, 04, 55 e 65__, que foram recuperados na [RP02](#RP02_Regras185_precomedio_conversao)\.

Os registros destacados em cinza, trata\-se dos campos chaves dos itens das notas recuperados\. Os destacados em verde serão utilizados para a geração do registro C180 e os em azul, para a geração do C185\.

Os dados calculados e gravados podem ser consultados na tela:  Menu Básicos, Módulo: DW, item Manutenção à Documento Fiscal à Novo Documento Fiscal à Documento Fiscal de Mercadoria

Na opção “Informações Complementares Oper\. ST \(Sped Fiscal\)” da aba “Item Mercadoria”\.

__\(Tabela de Gravação dos Registros C180 e C185\)__

Tabela

Obr

Item

Nome do Campo/Layout

Regra

X296

\(\*\)

1

COD\_EMPRESA

Considerar a informação do campo 01\-COD\_EMPRESA do documento recuperado da SAFX08\.

X296

\(\*\)

2

COD\_ESTAB

Considerar a informação do campo 02\-COD\_ESTAB do documento recuperado da SAFX08\.

X296

\(\*\)

3

DATA\_FISCAL

Considerar a informação do campo 03\-DATA\_FISCAL do documento recuperado da SAFX08\.

X296

\(\*\)

4

MOVTO\_E\_S

Considerar a informação do campo 04\-MOVTO\_E\_S do documento recuperado da SAFX08\.

X296

\(\*\)

5

NORM\_DEV

Considerar a informação do campo 05\-NORM\_DEV do documento recuperado da SAFX08\.

X296

\(\*\)

6

COD\_DOCTO

Considerar a informação do campo 06\-COD\_DOCTO do documento recuperado da SAFX08\.

X296

\(\*\)

7

IND\_FIS\_JUR

Considerar a informação do campo 07\-IND\_FIS\_JUR do documento recuperado da SAFX08\.

X296

\(\*\)

8

COD\_FIS\_JUR

Considerar a informação do campo 08\-COD\_FIS\_JUR do documento recuperado da SAFX08\.

X296

\(\*\)

9

NUM\_DOCFIS

Considerar a informação do campo 09\-NUM\_DOCFIS do documento recuperado da SAFX08\.

X296

 

10

SERIE\_DOCFIS

Considerar a informação do campo 10\-SERIE\_DOCFIS do documento recuperado da SAFX08\.

X296

 

11

SUB\_SERIE\_DOCFIS

Considerar a informação do campo 11\-SUB\_SERIE\_DOCFIS do documento recuperado da SAFX08\.

X296

\(\*\)

12

IND\_PRODUTO

Considerar a informação do campo 13\-IND\_PRODUTO do documento recuperado da SAFX08\.

X296

\(\*\)

13

COD\_PRODUTO

Considerar a informação do campo 14\-COD\_PRODUTO do documento recuperado da SAFX08\.

X296

\(\*\)

14

COD\_UND\_PADRAO

Considerar a informação do campo 17\-COD\_UND\_PADRAO do documento recuperado da SAFX08\.

X296

\(\*\)

15

NUM\_ITEM

Considerar a informação do campo 18\-NUM\_ITEM do documento recuperado da SAFX08\.

X296

\(\*\)

16

QTD\_CONV

Considerar a informação do campo Quantidade Convertida, conforme regra indicada na RP01 ou RP02

X296

\(\*\)

17

COD\_MEDIDA

Considerar a informação do campo COD\_MEDIDA convertida, conforme regra indicada na RP01 ou RP02\.

X296

\(\*\)

18

VLR\_UNIT\_CONV

__05\-VL\_UNIT\_CONV \(Layout C180\)__

__09\-VL\_UNIT\_CONV \(Layout C185\)__

Considerar o campo 27\-VLR\_UNIT do item do documento recuperado da SAFX08\.

__\[MFS\-46686\]:__

Com base nas orientações de preenchimento dos campos 05 do C180 e 09 do C185 descritas no Guia Prático do Sped Fiscal, e com aval do nosso Setor de Informação, esse campo deve ser preenchido com o valor unitário líquido\. O campo 27 da SAFX08 é o valor unitário bruto\.  O valor unitário líquido é calculado através do valor contábil dividido pela quantidade convertida\. 

__\[MFS57863\]__

Dando continuidade ao ajuste realizado na MFS\-46686, no registro C180, o campo deve ser o valor líquido não incluindo o ICMS\-ST\. Por isso estamos ajustando essa regra para que, caso da nota de Entrada, subtrair o valor do ICMS\-ST\.

__\[MFS71205\]__

Dando continuidade ao ajuste realizado na MFS\-57863, no registro C180, o campo deve ser o valor líquido, não incluindo o ICMS\-ST, mas somente quando o campo IND\_RESP\_RET\_ENT \(COD\_RESP\_RET\) igual a “1” \(Remetente Direto\) ou “3” \(Próprio Declarante\)\.

__\[MFS78492\]__

Dando continuidade ao ajuste realizado na MFS\-71205, no registro C180, o campo deve ser o valor líquido, não incluindo o ICMS\-ST, mas somente quando o campo IND\_RESP\_RET\_ENT \(COD\_RESP\_RET\) igual a “1” \(Remetente Direto\)\. Quando o responsável é o próprio declarante \(COD\_RESP\_RET=3\), o valor do ICMS\-ST não compõe o valor contábil, portanto não deve ser deduzido\.

__\[MFS509134\]:__

Com base na resposta da SEFAZ\-MG recebida pelo Setor de Informação referente ao campo 05 do C180, o campo deve ser o valor líquido não incluindo o valor do IPI não escriturado\. Por isso, estamos ajustando essa regra para que, no caso da nota de Entrada, deve\-se subtrair o valor do IPI\.

Sendo assim o campo VLR\_UNIT\_CONV passa a ser:

- Para notas fiscais de Saída \(C185\)

  VLR\_UNIT\_CONV = Valor Contábil / QTD\_CONV

- Para notas fiscais de Entrada \(C180\)

  Se COD\_RESP\_RET = “1” 

      VLR\_UNIT\_CONV = \(Valor Contábil – Valor do ICMS\-ST 

                                         – IPI não escriturado\) / QTD\_CONV

  Senão \(COD\_RESP\_RET = “2 ou “3”\)

      VLR\_UNIT\_CONV = \(Valor Contábil – IPI não escriturado\) / 

                                         QTD\_CONV

Onde:

- COD\_RESP\_RET: campo 20\-IND\_RESP\_RET\_ENT da X296;
- Valor Contábil: item 64 \- VLR\_CONTAB\_ITEM da SAFX08;
- Valor do ICMS\-ST pode ser um dos quatro campos da SAFX08:
- IPI não escriturado: campo 81\-VLR\_IPI\_NDESTAC:

Se campos “61\-BASE\_SUB\_TRIB\_ICMS” e 

                    “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

      Considerar o Campo 52\-VLR\_SUBST\_ICMS\.

Senão: 

      Se campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “145\-   VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos:

            Considerar o Campo 145 \- VLR\_ICMSS\_N\_ESCRIT\. 

      Senão:

            Se campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                               “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos: 

                  Considerar o Campo 133\- VLR\_ICMSS\_NDESTAC\.

            Senão

                  Se campos “106\- VLR\_BASE\_ICMS\_ORIG” e 

                                    “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos:

                        Considerar o Campo 107\- VLR\_TRIB\_ICMS\_ORIG

                  Senão

                        Considerar Valor do ICMS\-ST = Zero\.

X296

 

19

VLR\_ICMS\_CONV

__06\-VL\_UNIT\_ICMS\_OP\_CONV \(Layout C180\)__

__10\-VL\_UNIT\_ICMS\_NA\_OPERACAO\_CONV \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado, não preenchendo esse campo na X296\.

\[__MFS94229__\]:Inclusão da alíquota do FCP somada à alíquota interna no cálculo do valor das notas de saída

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realizado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

\[MFS\-67654\]

Se campo 24 – COD\_MOTIVO\_SAI igual a __MG000__, então:

   Não preencher esse campo\.

Senão

__  \[MFS47958\]__

  Se o campo “__%Redução BC__” da parametrização de Produto ou 

  NCM está preenchido com valor > 0, então:

      Este campo será gerado da seguinte forma:

      \[\(Valor Contábil – \(Valor Contábil \* “%Redução BC” / 100\)\) \* 

     Aliquota / 100\]/quantidade do item recuperado\(convertida\)

  Senão:

     Este campo será gerado da seguinte forma:

     \[\(Valor Contábil\) \* Aliquota / 100\]/quantidade do item   

     recuperado \(convertida\)

Onde:

- Valor Contábil: item 64 da SAFX08;
- Alíquota = Alíquota Interna \+ Alíquota FCP da parametrização de Produto ou NCM sujeito ao ICMS\-ST\.
- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST\.
- Para as notas fiscais de Entrada:

__\[MFS47958\]__

Este campo deve ser preenchido com:

Valor do ICMS/quantidade do item recuperado \(convertida\)

Onde:

Valor do ICMS pode ser um dos três campos da SAFX08, dependendo do campo que estiver preenchido\. Veja:

Preencher com o campo __“43\-Valor ICMS”__, se preenchido, ou  campo __“80\-ICMS não Escriturado”__, se preenchido, ou campo  __“225\-Valor ICMS Não Destacado”__, se preenchido\.

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado, deixar este campo vazio\.

X296

 

20

IND\_RESP\_RET\_ENT

__02\-COD\_RESP\_RET \(Layout\)__

Este campo será preenchido de acordo com os campos 131\- Indicador de ICMS\-ST e 132 – Situação Especial – Substituição Tributária que estiver preenchido na SAFX08 \(referente ao item de entrada recuperado\)\. De acordo com as regras abaixo:

__\[MFS78490\] __Alteração do tratamento para o código 3\-Próprio Declarante, que passa a considerar o campo 132 com conteúdo igual a “2” também

Se campo “132 – Situação Especial – Substituição Tributária” igual a ‘1’ ou ‘2’:O campo será preenchido com o valor igual a “3” – Próprio Declarante

Senão

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘1’: O campo será preenchido com o valor igual a “1” – Remetente Direto

     Se campo “131\- Indicador de ICMS\-ST” igual a ‘2’: O campo será preenchido com o valor igual a “2” – Remetente Indireto

Atenção: Este campo só deve ser preenchido se atender as regras da RP01\.

X296

 

21

VLR\_UNIT\_BC\_ICMSS\_ENT

__07\-VL\_UNIT\_BC\_ICMS\_ST\_CONV \(Layout C180\)__

Considerar o resultado da expressão de acordo com as regras abaixo:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então considere: 

61\-BASE\_SUB\_TRIB\_ICMS \(do item de entrada recuperado\) / QTD\_CONV \(calculado RP01\)

Senão: 

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos ou se 

campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então considere:

144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT \(do item de entrada recuperado\) / QTD\_CONV \(calculado RP01\) 

Senão:

Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então considere:

106 \- VLR\_BASE\_ICMS\_ORIG \(do item de entrada recuperado\) / QTD\_CONV \(calculado RP01\)

Validação

Considerando os campos 61\-BASE\_SUB\_TRIB\_ICMS , 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT, 106 \- VLR\_BASE\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário BC ICMS\-ST Conv\. \(Entradas\) foi gerado com zero, pois existe mais de um campo de Base de ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP01\.

X296

 

22

VLR\_UNIT\_ICMSS\_CONV\_ENT

__08\-VL\_UNIT\_ICMS\_ST\_CONV \(Layout C180\)__

Considerar o resultado da expressão, de acordo com as regras abaixo: 

\(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

O preenchimento do campo seria:

 \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV

Mas deve\-se tratar o caso do Valor do ICMS\-ST já conter o FECEP\-ST, para que este não seja somado duas vezes\. 

Como premissa, a tabela DATAMART já contém o FECEP\-ST embutido no campo 52\-ICMS\-ST, pois na equalização do DATA MART, os clientes são orientados a marcar o parâmetro indicado p/ somar FECEP ao ICMS/ICMS\-ST, quando o FECEP não “nasce” embutido ao ICMS/ICMS\-ST nas tabelas “normais” X07/X08\. 

Quanto às tabelas “normais”, o FECEP pode ou não estar embutido campo 52\-ICMS\-ST via importação da SAFX08, por isso existe o parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” da tela de geração\.

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST 

      nos itens \(SAFX08\)” foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o

             __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV 

Senão:

                  Preencher com:

                    \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST

      nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  

             \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o  

__     Valor do ICMS\-ST__ \(\*\):

           Preencher com: \(Valor do ICMS\-ST\) / QTD\_CONV

     Senão

           Preencher com:

          \(Valor do ICMS\-ST \+ Valor do FECEP\-ST\) / QTD\_CONV

Onde:

- Valor do FECEP\-ST:  Campo 140\-VLR\_FECP\_ICMS\_ST da SAFX08
- QTD\_CONV: Quantidade Convertida calculada na RP01
- \(\*\) __Valor do ICMS\-ST__: é oriundo de um dos quatro campos SAFX08, dependendo de qual esteja preenchido :

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, 

    então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, 

        então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                              “107\- VLR\_TRIB\_ICMS\_ORIG” estiverem 

            preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG\.

Validação

Considerando os campos 52\-VLR\_SUBST\_ICMS, 145 \- VLR\_ICMSS\_N\_ESCRIT, 133\- VLR\_ICMSS\_NDESTAC , 107\- VLR\_TRIB\_ICMS\_ORIG, se no mesmo item de nota, dois ou mais desses campos estiverem preenchidos, gravar  zero neste campo e exibir a mensagem no log :” O campo Valor Unitário ICMS\-ST Conv\.  \(Entradas\) foi gerado com zero, pois existe mais de um campo de Valor ICMS – ST com valor preenchido na nota”\. 

No log deve constar esses campos com os respectivos valores e os campos identificadores da nota\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP01\.

X296

 

23

VLR\_UNIT\_FCP\_CONV\_ENT

__09\-VL\_UNIT\_FCP\_ST\_CONV \(Layout C180\)__

Considerar o resultado da expressão: Campo 140 \-VLR\_FECP\_ICMS\_ST \(do item de entrada recuperado\) / QTD\_CONV \(calculado na RP01\)

Atenção: Este campo só deve ser preenchido se atender as regras da RP01\.

X296

24

COD\_MOTIVO\_SAI

__06\-COD\_MOT\_REST\_COMPL \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado, preenchendo esse campo na X296 com de\.

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realiado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

__\[MFS\-67654\]: __

Alteramos a regra para utilizarmos como comparação os próprios valores de ICMS e ICMS\-ST de Saída e Entrada, em substituição as BC\-Entrada e BC\-Saída\. RS já sofreu essa alteração\. Motivo: No C181 a regra pela comparação de Bases não dá pra ser feita, pois as devoluções cujas saídas são de períodos anteriores, os valores médios \(entradas\) são recuperados da X296, que não possui o base\-st\.

 

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+  

      VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

      VLR\_ICMS\_CONV > 0 \(entrada > saída = ressarcimento\) então:

   A saída obteve Restituição;

   Preencher com “__MG100__”\. 

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

     VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \- 

     VLR\_ICMS\_CONV < 0 \(entrada < saída = complemento\) então:

   A saída obteve Complemento;

   Preencher com “__MG300__”\.  

Se \(VLR\_UNIT\_ICMS\_ESTQ\_SAI \+ 

     VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) – 

     VLR\_ICMS\_CONV = 0 \(entrada = saída\) então: \(\*\*\)

    A saída não teve nem Restituição nem Complemento\.

    Preencher com __MG000__\.

OBS: A nota com motivo __MG000__, passa a ser gerada no arquivo, uma vez que a devolução de saída com MG500 é gerado no C181\.

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado, esse campo deve ser preenchido com __MG200__\.

__\[MFS74901\]__ Preenchimento para a operação “Devolução de Entrada Interestadual”

- Para notas fiscais que tenham o CFOP ou CFP/Natureza de Operação parametrizado para a operação “Devolução de Entrada Interestadual de Saída”, esse campo deve ser preenchido com __MG200__\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

25

VLR\_UNIT\_ICMS\_OPER\_SAI

__11\-VL\_UNIT\_ICMS\_OP\_CONV \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado, não preenchendo esse campo X296\.

\[MFS\-67654\]__:__

Se campo 24 – COD\_MOTIVO\_SAI igual a MG100 ou MG300 ou MG200 ou MG000 deixar este campo vazio\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

26

VLR\_UNIT\_ICMS\_ESTQ\_SAI

__12\-VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV \(Layout C185\)__

\[MFS\-67654\]__:__

__\[MFS97773\]: MG000 passa a preencher o campo 12, 13 e 14 do C185__

Se campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ e período da geração é anterior a Jan/2023 então:

   Não preencher esse campo\.

Senão:

Preencher com o “Valor Médio Unitário do ICMS” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\), conforme tópico 2 da RP02, para o Produto na Data de Emissão da nota de saída\. 

    \(campo VLR\_UNIT\_ICMS\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

27

VLR\_UNIT\_ICMSS\_ESTQ\_SAI

__13\-VL\_UNIT\_ICMS\_ST\_ESTOQUE\_CONV \(Layout C185\)__

\[MFS\-67654\]__:__

__\[MFS97773\]: MG000 passa a preencher o campo 12, 13 e 14 do C185__

Se campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ e período da geração é anterior a Jan/2023 então:

   Não preencher esse campo\.

Senão:

Preencher com “Valor Médio Unitário do ICMS\-ST c/ FECEP” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\), conforme tópico 2 da RP02, para o Produto na Data de Emissão da nota de saída\. 

   \(campo VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

28

VLR\_UNIT\_FCP\_ESTQ\_SAI

__14\- VL\_UNIT\_FCP\_ICMS\_ST\_ESTOQUE\_CONV \(Layout C185\)__

\[MFS\-67654\]__:__

__\[MFS97773\]: MG000 passa a preencher o campo 12, 13 e 14 do C185__

Se campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ e período da geração é anterior a Jan/2023 então:

   Não preencher esse campo\.

Senão:

Preencher com “Valor Médio Unitário do FECEP\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_MG\_RS\_MEDIA\_POND\), conforme tópico 2 da RP02, para o Produto na Data de Emissão da nota de saída\. 

    \(campo VLR\_UNIT\_FECEP\_ST\_FIM\_MP da EST\_ST\_MG\_MEDIA\_POND\);

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

29

VLR\_UNIT\_ICMSS\_REST\_SAI

__15\-VL\_UNIT\_ICMS\_ST\_CONV\_REST \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado\.

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realiado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

__Se__ o campo 24 – COD\_MOTIVO\_SAI for igual a __MG100__, preencher com o resultado da expressão:

\(campo 26 \- VLR\_UNIT\_ICMS\_ESTQ\_SAI \) \+

\(campo 27 \- VLR\_UNIT\_ICMSS\_ESTQ\_SAI\) \-

\(campo 19 \- VLR\_ICMS\_CONV\)

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG300__ deixar este campo vazio\. 

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ deixar este campo vazio\. 

__ __

__\[MFS76604\] __Alteração do preenchimento do campo para seguir a regra do guia prático, para a não ocorrência do fato gerador presumido\.

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado, esse campo deve ser preenchido com:

\(campo 26 \- VLR\_UNIT\_ICMS\_ESTQ\_SAI \) \+ 

\(campo 27 \- VLR\_UNIT\_ICMSS\_ESTQ\_SAI\)

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

30

VLR\_UNIT\_FCP\_REST\_SAI

__16\-VL\_UNIT\_FCP\_ST\_CONV\_REST \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado\.

\[__MFS94486__\] Alteração do cálculo para passar a ser feito utilizando a base de cálculo do ICMS\-ST, em vez de utilizar o valor unitário do ICMS\-ST, para as notas fiscais de Saída interna para Consumidor Final\.

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realiado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

__Se__ o campo 24 – COD\_MOTIVO\_SAI for igual a __MG100__ e o campo 28 \-  VLR\_UNIT\_FCP\_ESTQ\_SAI maior que zero, preencher com o resultado da expressão: 

\(campo 29\- VLR\_UNIT\_ICMSS\_REST\_SAI \* alíquota de FCP\)

\(VLR\_UNIT\_BC\_ST\_FIM\_MP – Valor Unitário Venda\) \* 

alíquota do FCP

__               __

__               Obs\.:  __Se o resultado da diferença entre os dois campos der um 

                           valor negativo, preencher com zero\.

__               Onde: __

\- VLR\_UNIT\_BC\_ST\_FIM\_MP = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_MG\_RS\_MEDIA\_POND\), conforme tópico 2 da RP02, para o Produto na Data de Emissão da nota de saída;

 

 \- Valor Unitário Venda = \[\(Valor Contábil – \(Valor Contábil \* “%Redução BC” / 100\)\)\] /quantidade do item recuperado\(convertida\)

- Valor Contábil: item 64 da SAFX08;
- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG300__ deixar este campo vazio\.

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ deixar este campo vazio\. 

__\[MFS77170\] __Alteração do preenchimento do campo para seguir a regra do guia prático, para a não ocorrência do fato gerador presumido

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado \(MG200\), esse campo deve ser preenchido com:

\(campo 28\- VLR\_UNIT\_FCP\_ESTQ\_SAI  

__Como identificar a Alíquota FCP:__

Considerar a alíquota FCP existente na parametrização de Produto ou NCM sujeito ao ICMS\-ST\. A alíquota ao ser aplicada nas expressões acima, deve ser divida por 100\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

31

VLR\_UNIT\_ICMSS\_COMPL\_SAI

__17 – VL\_UNIT\_ICMS\_ST\_CONV\_COMPL \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado, não preenchendo esse campo na X296\.

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realiado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

__Se__ o campo 24 – COD\_MOTIVO\_SAI for igual a __MG300__, preencher com o resultado da expressão: 

\(campo 19\-VLR\_ICMS\_CONV\) \- 

\(campo 26\- VLR\_UNIT\_ICMS\_ESTQ\_SAI\) \-

\(campo 27\-VLR\_UNIT\_ICMSS\_ESTQ\_SAI\)

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG100__ deixar este campo vazio\.

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ deixar este campo vazio\. 

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado, deixar este campo vazio\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

X296

32

VLR\_UNIT\_FCP\_COMPL\_SAI

__18 – VL\_UNIT\_FCP\_ST\_CONV\_COMPL \(Layout C185\)__

\[__MFS47079__\]:

Cria tratamento para as notas fiscais de Saída de Fato Gerador Presumido Não Realizado, não preenchendo esse campo na X296\.

\[__MFS94488__\] Alteração do cálculo para passar a ser feito utilizando a base de cálculo do ICMS\-ST, em vez de utilizar o valor unitário do ICMS\-ST, para as notas fiscais de Saída interna para Consumidor Final\.

Esse campo possui regras diferenciadas no que diz respeito às notas fiscais de saídas interna para consumidor final e fato gerador presumido não realizado\. Veja:

- Para as notas fiscais de Saída interna para Consumidor Final:

__Se__ o campo 24 – COD\_MOTIVO\_SAI for igual a __MG300__ e o campo 28 \- VLR\_UNIT\_FCP\_ESTQ\_SAI maior que zero, preencher com o resultado da expressão: 

\(campo 31\- VLR\_UNIT\_ICMSS\_COMPL\_SAI \* alíquota de FCP\)

\(Valor Unitário Venda \- VLR\_UNIT\_BC\_ST\_FIM\_MP\) \* 

alíquota do FCP

__               __

__               Obs\.:  __Se o resultado da diferença entre os dois campos der um 

                           valor negativo, preencher com zero\.

__               Onde: __

\- VLR\_UNIT\_BC\_ST\_FIM\_MP = “Valor Médio Unitário da Base de Cálculo do ICMS\-ST” recuperado do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_MG\_RS\_MEDIA\_POND\), conforme tópico 2 da RP02, para o Produto na Data de Emissão da nota de saída;

 

 \- Valor Unitário Venda = \[\(Valor Contábil – \(Valor Contábil \* “%Redução BC” / 100\)\)\] /quantidade do item recuperado\(convertida\)

- Valor Contábil: item 64 da SAFX08;
- %Redução BC da parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

__Como identificar a Alíquota FCP:__

Considerar a alíquota FCP existente na parametrização de Produto ou NCM sujeito ao ICMS\-ST\.

A alíquota recuperada deve ser divida por 100\.

\[MFS\-67654\]__:__

Validação:

Se o resultado da expressão acima for negativo, gravar zero e exibir a mensagem no log: 

“O resultado do cálculo: ‘Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\)’ \* ‘Alíquota FCP’ ficou negativo,  por isso, o campo ‘Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\)’ foi gravado com zero”\.

Apresentar no log, as informações para conseguir identificar o item da nota\.

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG100__ deixar este campo vazio\.

\[MFS\-67654\]__:__

__Se__ o campo 24 – COD\_MOTIVO\_SAI igual a __MG000__ deixar este campo vazio\. 

- Para notas fiscais de Saída de Fato Gerador Presumido Não Realizado, deixar este campo vazio\.

Atenção: Este campo só deve ser preenchido se atender as regras da RP02\.

MFS\-33977

MFS47079

MFS47958

MFS\-67654

MFS\-71205

MFS\-58456

RP04

Todos os registros gravados na tabela x296\_info\_compl\_st\_itens\_merc, através deste processo [\(RP03\)](#RP03_tabela_registros_c180_c185), devem ser identificados que foram calculados pelo sistema, pois os registros importados \(SAFX296\) não podem ser alterados \(por esse processo\)\. 

<a id="Sugestao_Ind_Gravacao"></a>__Sugestão:__ utilizar o campo ind\_gravacao, com os domínios 

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema / Atualizado por Digitação

O domínio 7 deve ser considerado, quando o usuário ajustar uma informação que foi calculada pelo sistema\.

__Domínio completo do campo ind\_gravacao:__

		

Tipo/tamanho: CHAR\(1\)

Valores padrão do campo:

1\.  Incluído por Importação

2\.  Atualizado por Importação

3\.  Incluído por Importação / Atualizado por Digitação

4\.  Incluído por Digitação

5\.  Incluído por Digitação / Atualizado por Digitação

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema  / Atualizado por Digitação

8\. Gerado pelo Sistema  / Atualizado por Importação

<a id="RP04_Dominio_Registros_Importados"></a>__Serão considerados registros oriundos de Importação os domínios:__

1\.  Incluído por Importação  
2\.  Atualizado por Importação  
3\.  Incluído por Importação / Atualizado por Digitação  
 

MFS\-33977

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
- Se for encontrado o registro de inventário na tabela x52\_invent\_produto, para a realização do cálculo, e não foram encontradas notas de entrada suficientes para compor a quantidade deste inventário, realizar o cálculo deste produto com a quantidade encontrada e exibir a mensagem: “Não foram encontradas notas de entrada suficientes para atingirmos a quantidade do inventário\. As notas de entrada foram consultadas até: << informar a data preenchida no campo ‘Pesquisar Notas de Entrada até’”\. Favor rever esta situação\.” O log deve demonstrar as informações necessárias para permitir a identificação inventário, exibindo o estabelecimento, a data, produto,indicador, etc\)\.

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

<a id="RP06"></a>RP06

Relatório de Conferência do Registro C185:

Gerar um arquivo Excel com as notas de saída geradas pelo processo\.

Nome do arquivo: Relatorio\_Conferencia\_C185\_mm\_aaaa\_cod\_estab\.csv

Para isso fazer uma leitura na tabela __x296\_info\_compl\_st\_itens\_merc__ com os seguintes critérios:

\- empresa de login;

\- estabelecimento selecionado na tela de geração;

\- data fiscal compreendida no Período informado na tela de Geração;

\- Movimento E/S = ‘9’ \- Saída

Ordenar as notas pelos campos: empresa, estabelecimento, data fiscal, número do documento fiscal, número do item de mercadoria\.

O relatório deve ser composto pelos seguintes campos:

- 'Cod Empresa': Preencher com COD\_EMPRESA
- 'Cod Estab': Preencher com COD\_ESTAB
- 'Dt Fiscal': Preencher com DATA\_FISCAL
- 'E/S': Preencher com MOVTO\_E\_S
- 'Norm/Dev': Preencher com NORM\_DEV
- 'Cod Docto': Preencher com COD\_DOCTO
- 'Ind Fis/Jur Cod Fis/Jur': Preencher com IND\_FIS\_JUR \- COD\_FIS\_JUR 
- 'Num Docfis': Preencher com NUM\_DOCFIS
- 'Serie': Preencher com SERIE\_DOCFIS
- 'SubSerie': Preencher com SUB\_SERIE\_DOCFIS
- 'Num Item': Preencher com NUM\_ITEM
- 'Qtde Conv \(C185\-07\)': Preencher com QTD\_CONV
- 'Medida \(C185\-08\)': Preencher com COD\_MEDIDA
- 'Vlr Unit Conv \(C185\-09\)': Preencher com VLR\_UNIT\_CONV
- 'Vlr Unit ICMS Operação Conv \(C185\-10\)': Preencher com VLR\_ICMS\_CONV;
- 'Cod Motivo \(C185\-06\)': Preencher com COD\_MOTIVO\_SAI;
- 'Vlr Unit ICMS Op Conv \(C185\-11\)': Preencher com VLR\_UNIT\_ICMS\_OPER\_SAI;
- 'Vlr Unit ICMS Estoque Conv \(C185\-12\)': Preencher com VLR\_UNIT\_ICMS\_ESTQ\_SAI;
- 'Vlr Unit ICMS\-ST Estoque Conv \(C185\-13\)': Preencher com VLR\_UNIT\_ICMSS\_ESTQ\_SAI; 
- 'Vlr Unit FCP\-ST Estoque Conv \(C185\-14\)': Preencher com VLR\_UNIT\_FCP\_ESTQ\_SAI;
- 'Vlr Unit ICMS\-ST Conv Rest \(C185\-15\)': Preencher com VLR\_UNIT\_ICMSS\_REST\_SAI;  
- 'Vlr Unit FCP\-ST Conv Rest \(C185\-16\)': Preencher com VLR\_UNIT\_FCP\_REST\_SAI;  
- 'Vlr Unit ICMS\-ST Conv Compl \(C185\-17\)': Preencher com VLR\_UNIT\_ICMSS\_COMPL\_SAI;  
- 'Vlr Unit FCP\-ST Conv Compl \(C185\-18\)': Preencher com VLR\_UNIT\_FCP\_COMPL\_SAI;  
- 'Ind Produto \(SAFX2013\-01\) Cod Produto \(SAFX2013\-02\)': Preencher com IND\_PRODUTO – COD\_PRODUTO; 
- 'Medida Produto \(SAFX2013\-14\)': Preencher com COD\_MEDIDA cadastrada para o produto na SAFX2013;
- 'NCM Produto \(SAFX2013\-05\)': Preencher com COD\_NBM cadastrado para o produto da SAFX2013; 
- 'CEST Produto \(SAFX2013\-54\)': Preencher com COD\_CEST cadastrado para o produto da SAFX2013;
- '%Redução BC \(Parametrização Produto\)': Preencher com PRC\_REDUCAO\_BC parametrizado para o produto; 
- 'Alíq\. Interna \(Parametrização Produto\)': Preencher com ALIQ\_INTERNA parametrizado para o produto;
- 'Alíq\. FCP \(Parametrização Produto\)': Preencher com ALIQ\_FCP parametrizado para o produto;  
- 'Qtde Item \(SAFX08\-24\)': Preencher com QUANTIDADE do item de mercadoria da NF;  
- 'Qtde Conv Item \(SAFX08\-137\)': Preencher com QUANTIDADE\_CONV do item de mercadoria da NF  
- 'Medida Item \(SAFX08\-25\)': Preencher com COD\_MEDIDA do item de mercadoria da NF;  
- 'Fator Conv \(Cadastro Conversão Medida\)': Preencher com Fator de Conversão aplicado à quantidade, conforme explicado na RP02\.
- 'Vlr Contabil Item \(SAFX08\-64\)': Preencher com VLR\_CONTAB\_ITEM do item de mercadoria da NF;  
- 'Vlr Unit BC ICMS Operação Conv \(Vlr Contábil c/ %Redução BC\)': Preencher com \(Valor Contábil – \(Valor Contábil \* “%Redução BC” / 100\);

MFS511653

