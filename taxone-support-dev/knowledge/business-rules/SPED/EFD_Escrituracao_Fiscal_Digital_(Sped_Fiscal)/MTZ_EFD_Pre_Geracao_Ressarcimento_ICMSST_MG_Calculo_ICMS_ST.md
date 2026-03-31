# MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST

- **Fonte:** MTZ_EFD_Pre_Geracao_Ressarcimento_ICMSST_MG_Calculo_ICMS_ST.docx
- **Modificado:** 2025-11-21
- **Tamanho:** 176 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Processamento do Cálculo ICMS\-ST

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

24/08/2021

MFS\-71202

Alteração da regra de recuperação das notas fiscais de entrada para cálculo do valor médio do inventário\.  As notas fiscais que não possuírem pelo menos um dos valores de ICMS \(Valor de ICMS, Valor ICMS\-ST, Base ICMS\-ST, FECP ICMS\-ST\) preenchido, serão desconsideradas do cálculo\.

Andréa Rocha

03/09/2021

MFS\-58456

Inclusão do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” na Tela de Geração e tratamento na geração dos registros C180, C186, H030, Cálculo do Valores Médios do Inventário \(RP00A\) e Cálculo da Média Ponderada do Diária Produto \(RP00B\)\.

Liliane Assaf

05/10/2021

MFS\-73772

Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada e suas devoluções, no cálculo da média ponderada e no cálculo da média do inventário\.

Andréa Rocha

29/10/2021

MFS\-74069

Inclusão de um parâmetro para indicar se deve ser gerado o log de erro de produto sem inventário, somente para produtos com movimentação\.

Andréa Rocha

17/11/2021

MFS\-74991

Inclusão de um parâmetro para indicar se deve ser gerado o registro de inventário \(SAFX52\), para os produtos que tem movimentação no mês e não tem saldo de inventário do mês anterior\.

Andréa Rocha

17/12/2021

MFS\-77698

Alteração no cálculo dos valores médios do inventário \(estoque anterior\)\.

Andréa Rocha

01/04/2022

MFS\-82924

Alteração da regra de recuperação das notas fiscais de entrada para o cálculo da média ponderada\.  As notas fiscais que não possuírem pelo menos um dos valores de ICMS \(Valor de ICMS, Valor ICMS\-ST, Base ICMS\-ST, FECP ICMS\-ST\) preenchido, serão desconsideradas do cálculo\.  Será feito o mesmo tratamento já adotado pelo cálculo do valor médio do inventário \(MFS\-71202\)\.

Andréa Rocha

11/04/2022

MFS\-84145

Alteração no cálculo dos valores médios do inventário para o campo Valor de ICMS\-ST Médio, para abater o valor do FECEP Médio incluído no valor do ICMS\-ST Médio, quando a origem dos dados for da tabela do Inventário por Produto

Andréa Rocha

03/06/2022

MFS\-86641

Inclusão do preenchimento da conta contábil para a geração do registro de inventário \(SAFX52\), para os produtos que tem movimentação no mês e não tem saldo de inventário do mês anterior\.

Andréa Rocha

07/03/2023

MFS511653

Criação check\-box “Gerar Relatórios de Conferência” na tela da pré\-geração e aplicação na geração do Relatório de Conferência do Cálculo da Média Ponderada \(vide [RP00B](#RP00B)\)\. Criação do Relatório de Conferência do Cálculo da Média do Inventário \([RP00A](#RP00A)\)

Liliane Assaf

06/12/2023

MFS591080

Tratamento das Incorporações de Empresas/Estabelecimentos no Cálculo dos Valores Médios do Inventário e alteração seu relatório de conferência\. \([RP00A](#RP00A)\)

Liliane Assaf

09/08/2024

MFS665846

Inclusão do tratamento do valor do FCP retido \(FECEP Regime Fonte\) na geração dos registros C180,  C186, e no Cálculo do Valores Médios do Inventário\.  As regras para os registros C181 e C185 não serão alteradas, porque os seus valores vêm da tabela da média ponderada\.

Andréa Rocha

21/11/2025

MFS977849

Inclusão de um parâmetro para definir se o valor do FECEP está embutido nos valores de ICMS não destacado e não escriturado\.  Esse parâmetro está sendo criado separado do parâmetro “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)”, porque o parâmetro já existente está vinculado a atualização do DATA MART, e os campos de ICMS não destacado e não escriturado não são gravados com o valor do FECEP embutido durante a equalização\.

Andréa Rocha

# <a id="_Toc462320892"></a><a id="_Toc27038220"></a><a id="_Toc37749427"></a>INTRODUÇÃO* *

Criar o processamento de cálculo de ICMS\-ST das notas de mercadoria dos estabelecimentos de Minas Gerais\. Esse cálculo será acionado através da tela Cálculo ICMS\-ST \(Minas Gerais\), onde é possível selecionar os registros do Sped Fiscal que a rotina realizará a pré\-geração:

- Se selecionar os registros C180 ou C185, a rotina irá alimentar a tabela x296\_info\_compl\_st\_itens\_merc\.
- Se selecionar os registros C181 ou C186, a tabela alimentada será a X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV\.
- Se escolhido o registro C330, a tabela alimentada será a x299\_inf\_comp\_st\_res\_mod\_02\.
- Se escolhido o registro C430 a tabela será a x302\_inf\_comp\_st\_res\_it\_ecf\.
- Se escolhido o registro 1250/1255 a tabela será a x304\_saldo\_cons\_res\_comp\_icms \(quando não for encontrado nenhum erro\)\.
- Se escolhido o registro C195/C197 as tabelas X112\_OBS\_DOCFIS e X113\_AJUSTE\_APUR serão alimentadas para as devoluções de Saída que geraram C181 com códigos MG600 e MG800\.

A pré\-geração é uma opção para os clientes que não querem carregar as informações através da importação das respectivas tabelas SAFX296\- Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\), SAFX299 \- Informações Complementares das Operações Sujeitas ao ST \(C330\), SAFX302\-\- Informações Complementares das Operações Sujeitas ao ST \(C430\) e SAFX304 \- Saldo Consolidado da Restituição/Complemento de ICMS \(1250/1255\)\. 

Para os registros de saída \(C185, C330 e C430\), o usuário deve ter previamente cadastrado os motivos de complemento e restituição \(MG300, MG100 e MG200\) na tela “Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\), localizada em MasterSAF\-DWàBásicos àData Warehouse à Manutenção à  Cadastros à Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\), para que as informações do cálculo sejam gravadas corretamente na tabela\.

Este processo também contempla o cálculo dos campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO da x52\_invent\_produto, que serão utilizados para a geração do registro H030\. Se existir informação nestes campos \(via importação ou digitação\), o cálculo só será realizado se a opção ‘Sobrepor os valores calculados na tabela de inventário \(Registro H030\)’ estiver marcada\. Caso contrário, o registro de inventário não será atualizado pelo processo\. Todos os registros de inventário que passarem pelo processo de cálculo, ficaram identificados que foram alterados pelo sistema\.

__\[MFS74991\]__ Inclusão da geração do registro de inventário na SAFX52\.

Quando o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário” estiver marcado, serão gerados os registros de inventário com a quantidade e os valores zerados na SAFX52, somente para os produtos que não tem inventário e tem movimentação de notas no período da geração\.

As informações que foram calculadas por essa rotina, serão utilizadas para a geração dos respectivos registros do SPED FISCAL\.

__Base Legal__:

- Manual de Escrituração – Complemento e Restituição do ICMS ST – Aspecto Quantitativo
-  Manual de Escrituração – Restituição do ICMS ST – Fato Gerador Presumido Não Realizado __\[MFS\-47079\]__
- Anexo XV do RICMS/02, Subseções IV \(artigos 22 a 31\) e IV\-A \(artigos 31\-A a 31\-J\)

O Manual do Aspécto Quantitativo trata as notas de saídas internas para consumidor final \(artigos 31\-A a 31\-J\) e o Manual do Fato gerador Presumido não realizado trata três operações de notas de saídas \(artigos 22 a 31\):

I \- saída para outra unidade da Federação

II \- saída amparada por isenção ou não\-incidência;

III \- perecimento, furto, roubo ou qualquer outro tipo de perda

# <a id="_Toc27038221"></a><a id="_Toc37749428"></a>DOCUMENTOS DE REFERÊNCIA

*MTZ\-EFD\_Tela\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_NCM\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Produtos\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Saida\_CFOP\.docx*

*MTZ\-EFD\_Parametrizacao\_Ressarcimento\_ICMSST\_Saida\_Natureza\_Operacao\.docx*

# DOCUMENTOS DA PRE\-GERAÇÃO 

*A especificação da Pré\-Geração foi criada em um único arquivo \(MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx\)\. Mas com o tempo este documento ficou bastante grande, dificultando sua manutenção\. Sendo assim, segregamos as regras nos seguintes documentos:*

- *MTZ\_EFD\_Pre\_Geracao\_Ressarcimento\_ICMSST\_MG\_Calculo\_ICMS\_ST\.docx*

*Documento principal, contém as seguintes regras: RP00 – regra geral, *[RP00A](#RP00A)*\- regra de cálculo para Valores Médios do Inventário e *[RP00B](#RP00B)*\- Regra da Média Ponderada dos Valores Médios do Produto no Período\.*

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

RP00

Esta funcionalidade tem o propósito de calcular os valores de ST para os itens de mercadoria que estão sujeitos ao ICMS\-ST para a UF de MG\. 

Este cálculo será executado através da tela de Cálculo ICMS\-ST, localizada no Menu: SPED, Módulo: Escrituração Fiscal Digital à Pré\-Geraçãoà Ressarcimento ICMS\-ST \(Específico MG\) , quando preenchido os parâmetros obrigatórios e acionado o Botão Executar\.

Para o processamento do cálculo, serão consideradas as informações dos parâmetros da tela \(Período, UF e estabelecimento\), além da recuperação de itens de Notas de Entrada, Saída e o Inventário, dos Produtos, NCMs, CFOPs e ou Natureza de Operações cadastrados nas telas de parametrização existentes no caminho Menu SPED, Módulo: Escrituração Fiscal Digital à Parâmetros à Ressarcimento ICMS\-ST\.

Como pré\-requisito, para a geração do cálculo dos registros de saída \(C185, C330 ou C430\) , também será necessário ter efetuado o cadastro dos códigos de motivo de restituição ou complemento \(MG000, MG100, MG300 e MG200\) na tela “Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\), localizada em MasterSAF\-DWàBásicos àData Warehouse à Manutenção à  Cadastros à Códigos de Motivo de Restituição/Complementação de ICMS \(SPED FISCAL\), para que as informações do cálculo sejam gravadas corretamente na tabela\.

Vale ressaltar que as informações da tabela x296\_info\_compl\_st\_itens\_merc, são utilizadas para a geração do SPED FISCAL \(registros C180, C185\), da tabela  x299\_inf\_comp\_st\_res\_mod\_02, para a geração do registro C330, da  x302\_inf\_comp\_st\_res\_it\_ecf utilizada para gerar o registro de cupom fiscal C430 e  da x304\_saldo\_cons\_res\_comp\_icms para a geração dos registros 1250 e 1255 porém, cada UF pode determinar como devem ser apresentados esses registros e poderão ter regras específicas\. Devido a existência dessas regras específicas, para atendimento à Minas Gerais \(escopo inicial definido\), neste momento, este cálculo não atenderá outras UFs\.

Caso já exista informações nas tabelas \(registros importados através da SAFX296, SAFX299, SAFX302 ou SAFX304\), para o período processado, não iremos executar o processo de cálculo\. A rotina de cálculo apenas será executada se não houver registro no período ou se o registro existente foi gerado pelo próprio processo de cálculo \(neste caso, todos os registros serão sobrepostos/recalculados\)\. 

Este processo também contempla o cálculo dos campos 21\-VLR\_ICMS\_MEDIO, 22\-VLR\_ICMSS\_MEDIO, 43\-VLR\_BASE\_ICMSS\_MEDIO e 44\-VLR\_FCP\_MEDIO da x52\_invent\_produto, que serão utilizados para a geração do registro H030\. Se existir informação nestes campos \(via importação ou digitação\), o cálculo só será realizado se a opção ‘Sobrepor os valores calculados na tabela de inventário \(Registro H030\)’ estiver marcada\. Caso contrário, o registro de inventário não será atualizado pelo processo\. Todos os registros de inventário que passarem pelo processo de cálculo, ficarão identificados que foram alterados pelo sistema\.

__\[MFS74991\]__ Inclusão da geração do registro de inventário na SAFX52\.

Quando o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário” estiver marcado, serão gerados os registros de inventário com a quantidade e os valores zerados na SAFX52, somente para os produtos que não tem inventário e tem movimentação de notas no período da geração\.

__Ordem de execução dos processos:__

\[MFS\-62563: Inclusão do C181

MFS\-64570: Inclusão do C186

MFS\-67658: Inclusão dos registros C195/C197

1. Cálculo dos Valores Médios do Inventário \([RP00A](#RP00A)\) e Cálculo dos Valores Médios Diário dos Produtos do Período \([RP00B](#RP00B)\)
2. H030 \- Inventário das mercadorias sujeitas ao regime de substituição tributária à depende do Cálculo dos Valores Médios do Inventário
3. C180 \- Entrada de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\) \(RP01\)
4. C185 \- Saída de mercadorias sujeitas à substituição tributária \(01, 1B, 04,55 e 65\) à depende do Cálculo dos Valores Médios Diário dos Produtos do Período
5. C181 – Devolução de Saída mercadorias sujeitas à substituição tributária \(01, 1B, 04,55 e 65\) à  depende do Cálculo dos Valores Médios Diário dos Produtos do Período
6. C186 – Devolução de Entrada de mercadorias sujeitas à substituição tributária \(01, 1B, 04, 55 e 65\)
7. C195/C197 – Observações da Nota Fiscal e Ajustes do Lançamento Fiscal
8. 1250/1255 \- Saldos de restituição, ressarcimento e complementação do ICMS à deve ser o último registro a ser gerado, pois depende do C185, C330, C430, C181

MFS\-33977

MFS\-35337

MFS\-35339

MFS\-35340

MFS\-36146

MFS47079

MFS\-62563

MFS\-74991

<a id="RP00A"></a>RP00A

__CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\) E VALORES MÉDIOS DIÁRIOS DO PRODUTO DO PERÍODO__

Nota técnica: rotina implementada nas funções CalcMedInv e CalcMedProd da EFD\_CALC\_RESSARC\_MG\_FPROC

Quando um dos parâmetros a seguir estiver marcado na tela, executar os cálculos das médias ponderadas e gravar a tabela de Médias Ponderadas EST\_ST\_MG\_SALDO\_MED\.

- *C185 –Saída de mercadorias sujeitas à substituição tributária \(01,1B, 04, 55 e 65\)*
- *C330 \- Saída de mercadorias sujeitas à substituição tributária \(02\)  *
- *C430 \- Saída de mercadorias sujeitas à substituição tributária \(02, 02D e 60\)*
- *H030 \- Inventário das mercadorias sujeitas ao regime de substituição tributária*
- *C181 – Devolução de Saída de mercadorias sujeitas à substituição tributária \(01,1B, 04, 55 e 65\) \[MFS\-62563\]*

Esses cálculos devem ser realizados antes da geração dos registros H030, C185, C330, C430 e C181\.

__Critérios da recuperação do Inventário \(para cálculo dos valores médios do inventário\):__

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data do Inventário = último dia do período anterior indicado na tela \(Cálculo ICMS\-ST\);
- Campo Motivo do Inventário \(Campo 40 – IND\_MOT\_INV\) = “06”;
- Produto ou NCM \(sujeito ao ICMS\-ST\) \(\*\)

__Critérios da recuperação das Notas Fiscais de Entrada \(para o cálculo dos valores médios do inventário\):  __

 

__\[MFS71202\] __As notas fiscais que não possuírem pelo menos um dos valores de ICMS \(Valor de ICMS, Valor ICMS\-ST, Base ICMS\-ST, FECP ICMS\-ST\) preenchido, serão desconsideradas do cálculo\.

__\[MFS73772\] __Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período do inventário anterior \(período anterior da geração\), até atingir a quantidade do inventário, limitando\-se a data indicada no campo ‘Pesquisar Notas de Entrada até’ na tela; \*\*\*
- Somente notas de Entrada;
- Notas Normais \(NORM\_DEV = ‘1’\);
- Somente notas não canceladas; 
- Somente notas *com itens*; 
- Modelo – todos os modelos;    
- Produto ou NCM \(sujeito ao ICMS\-ST\) \(\*\);
- CFOP ou CFOP/Natureza de Operação parametrizado para “Entrada \(e Devolução\)”;
- Somente as notas que possuírem pelo menos um dos valores de ICMS \(Valor de ICMS ou Valor ICMS\-ST ou Base ICMS\-ST ou FECP ICMS\-ST\) utilizado no cálculo preenchido, que são os campos de valores definidos no Passo2 \(ex\.: VALOR ICMS: 43\-VLR\_ICMS ou 80 \- VLR\_ICMS\_NDESTAC ou 225\-Valor ICMS Não Destacado\)

\(\*\) __Produto ou NCM \(sujeito ao ICMS\-ST\)__

Em todos os casos, a data de validade da parametrização deve estar de acordo com o período informado na tela da geração\.

A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma:

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

\- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”;

Na recuperação das notas de períodos anteriores, se o parâmetro ‘Utilizar somente DATA MART p/ períodos anteriores’ estiver marcado considerar os registros que estão na tabela DWT\. Caso desmarcado, a recuperação, deve ser feita com base na tabela definitiva \(X\)\.

<a id="CALC_MED_INV"></a>__CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\):__

Nota técnica: rotina implementada na função __CalcMedInv__ da EFD\_CALC\_RESSARC\_MG\_FPROC

Para cada produto sujeito ao ICMS\-ST que tiver parametrizado, calcular os Valores Unitários Médios do Inventário anterior e gravar na tabela de Médias Ponderadas EST\_ST\_MG\_SALDO\_MED, conforme detalhado abaixo:

Se existir mais de um registro de inventário para o mesmo produto, período e Motivo do Inventário \(Campo 40 – IND\_MOT\_INV\) = “06”, recuperar o registro com GRUPO\_CONTAGEM = ‘1’ e ‘2’ e somar as quantidades desses registros, caso a unidade de medida dos mesmos seja igual \(para encontrar as notas de entrada que compõe esta quantidade\)\. Se a unidade de medida destes registros for diferente, não considerar esses registros para o produto \(não calcular os preços médios destes inventários\) [e exibir a mensagem no log \(conforme detalhado na RP05\) indicando que a situação deve ser revista\.](#RP05_GERAL_inventarios_unidades_dif) 

__\[MFS84145\] __Alteração no cálculo do campo Valor de ICMS\-ST Médio, para abater o valor do FECEP Médio quando a origem dos dados for da SAFX52

Na recuperação do estoque, se os campos de valores médios \(21\- VLR\_ICMS\_MEDIO, 22\- VLR\_ICMSS\_MEDIO, 43 \- VLR\_BASE\_ICMSS\_MEDIO, 44 – VLR\_FCP\_MEDIO da safx52\) estiverem preenchidos, recuperar os Valores Médios do Inventario e gravar a tabela de Média Ponderada \(EST\_ST\_MG\_SALDO\_MED\), conforme a seguir:

- Valor Médio do ICMS = campo 21\-  VLR\_ICMS\_MEDIO;
- Valor Médio do ICMS\-ST = campo 22 \- VLR\_ICMSS\_MEDIO  \- campo 44 \-  VLR\_FCP\_MEDIO \(__\*\*\)__;
- Valor Médio do ICMS\-ST c/ FECEP =  campo 22 \- VLR\_ICMSS\_MEDIO;  
- Valor Médio da Base do ICMS\-ST = campo 43\- VLR\_BASE\_ICMSS\_MEDIO;
- Valor Médio do FECEP\-ST = campo 44 \-  VLR\_FCP\_MEDIO\.

\(\*\*\) Quando o resultado do cálculo do Valor do ICMS\-ST médio \- Valor FECEP Médio, resultar em um valor negativo, será gravada a seguinte mensagem de erro no log:  
 *“Cálculo da Média do Inventário: Valor do ICMS\-ST Calculado Inicial gerado a partir da subtração dos campos <Valor ICMS\-ST Médio> pelo <Valor Fecep Médio> do Inventário, resultou em valor negativo\.  Favor rever o Inventário do Produto \(SAFX52\) de forma a adicionar o Fecep ao valor do ICMS\-ST carregado no campo <Valor ICMS\-ST Médio>\.”*

Dados de Identificação: Empresa: xxx \- Estab: xx – Período: 99/99/9999 \- Produto\(ind/cód\) x\-xxx

Na recuperação do estoque, os campos de valores médios \(21\- VLR\_ICMS\_MEDIO, 22\- VLR\_ICMSS\_MEDIO, 43 \- VLR\_BASE\_ICMSS\_MEDIO da safx52\) se pelo menos um desses campos não estiver preenchido, devemos calcular os valores médio do estoque a partir das notas de entrada de períodos anteriores\. Ao efetuar o cálculo, se for encontrado qualquer valor nos campos citados anteriormente e o mesmo divergir com o calculado \(neste processo\), devemos considerar o valor calculado e não o existente na tabela, [neste cenário, iremos exibir a mensagem no log \(RP05\)](#LOG_Valor_Medio)

Caso, na base for recuperado mais de um registro de estoque \(por produto e período\) e se um dos registros não possuir os valores citados acima calculado, deve ser calculado o valor médio referente aos dois registros\. Isso significa que deve ser considerada a somatória da quantidade dos inventários para recuperar as notas de entrada que atinjam essa somatória\. 

Procedimentos:

Passo1\) Recuperar as entradas \(a partir do mês anterior a geração, limitado a data indicada na tela, no campo ‘Pesquisar Notas de Entrada até’\) até atingir a quantidade do estoque \(da mais atual até a mais antiga\)\. Lembrando que as quantidades das entradas e do estoque quando não estão na mesma unidade de medida do produto sofrem conversão, [Conforme regra de conversão](#Conversao_unidade_SAFX08) descrita na RN01\.

__\[MFS591080\]__ Tratamento das Incorporações de Empresas/Estabelecimentos:

Se o total da quantidade em estoque não for atingido na busca pelas notas de entrada para a empresa e o estabelecimento da geração, deve ser verificado se o parâmetro para buscar as notas nas empresas incorporadas está marcado na tela da geração: 

     Se o parâmetro “Considerar as notas fiscais da empresa incorporada” estiver marcado:

           Considerar as notas da empresa/estabelecimento cadastradas como incorporadas na tela de Relação de Empresa 

           Incorporadora x Incorporada\*\* para a empresa/estabelecimento da geração \(incorporadora\), para recuperar as notas de  

           entrada para atingir a quantidade em estoque do produto

    Senão

          Considerar somente as notas fiscais da empresa e estabelecimento selecionados para a geração\.

\*\* Módulo Parâmetros, item Preliminares à Relação de Empresa Incorporadora x Incorporada

OBS: Não estamos tratando o cenário de Cadastros de Produtos distintos entre as empresas incorporadora e incorporadas\. Ou seja, os produtos entre essas empresas devem ser identificados pelo mesmo grupo, indicador e código do produto\.  A Lasa que foi o cliente que abriu essa demanda, poissui cadastros iguais entre as empresas participantes da incorporação\. Se os cadastros fossem diferentes, teríamos que criar uma espécie de dexpara entre os cadastros dos produtos da empresa incorporadora para com os das empresas incorporadas\.

__\[MFS77698\]__ Alteração no passo 2 do cálculo dos valores médios do inventário para retirar o cálculo do valor unitário por nota\.  Os valores serão totalizados e divididos pelo total da quantidade\.

Passo2\) Calcular os Valores unitários do ICMS, ICMS\-ST, ICMS\-ST c/ FECEP, Base do ICMS\-ST e FECEP\-ST para cada item da nota de entrada tratando de forma diferenciada entradas normais e a devoluções:

Calcular os valores unitários do ICMS, ICMS\-ST,  ICMS\-ST c/ FECEP, Base do ICMS\-ST e FECEP\-ST considerando VALOR ICMS/QTDE, VLR ICMS\-ST/QTDE,  \(VLR ICMS\-STc/FECEP\)/QTDE, BC\-ST/QTDE e FECEP\-ST/QTDE, onde os valores são oriundos da SAFX08: 

Passo 2\) Totalizar os Valores do ICMS, ICMS\-ST, ICMS\-ST c/ FECEP, Base do ICMS\-ST, FECEP\-ST e quantidade de todas as notas de entrada recuperadas, tratando de forma diferenciada entradas normais e devoluções:

Todos os campos totalizados são oriundos da SAFX08: 

- __VALOR ICMS__:

Preencher com: 43\-VLR\_ICMS ou 80 \- VLR\_ICMS\_NDESTAC ou __“225\-Valor ICMS Não Destacado”__,  \(conforme regras abaixo\):

__\[MFS47958\]__

Se campo 43\-VLR\_ICMS estiver preenchido, considerar o campo ‘43\-VLR\_ICMS, ’senão:

Se o campo 80 – VLR\_ICMS\_NDESTAC estiver preenchido, considerar o campo 80 –  VLR\_ICMS\_NDESTAC, ’senão:

Se o campo __“225\-Valor ICMS Não Destacado”__, estiver preenchido, considerar o campo __“225\-Valor ICMS Não Destacado”\.__

- __BC\-ST__: 

Preencher com: 61\-BASE\_SUB\_TRIB\_ICMS ou 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT ou 106\-VLR\_BASE\_ICMS\_ORIG \(conforme regras abaixo\):

                       Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

Considerar os campos “61\-BASE\_SUB\_TRIB\_ICMS” da SAFX08\.

                      Senão

                          Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT da SAFX08\.

                         Senão

                             Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então: 

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” da SAFX08 

                            Senão

Se campo “106\-VLR\_BASE\_ICMS\_ORIG” e “107\-VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então: 

Considerar o campo “106\-VLR\_BASE\_ICMS\_ORIG” da SAFX08\.

- __VLR ICMS\-ST__: \(valor a ser utilizado no Cálculo da Média Ponderada do Período na RP00B\) 

Preencher com:

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  __Valor do ICMS\-ST__ \(\*\):

    Preencher com:   \(Valor do ICMS\-ST\- Valor do FECEP\-ST\) 

Senão:

                  Preencher com: \(Valor do ICMS\-ST\) 

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  \(Valor do ICMS\-ST\) 

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o__  Valor do ICMS\-ST__ \(\*\):

           Preencher com:  \(Valor do ICMS\-ST \- Valor do FECEP\-ST\) 

     Senão

           Preencher com: \(Valor do ICMS\-ST\) 

__               \[MFS977849\]__ Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado 

              Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\) ou DATAMART, então:

                    Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” foi marcado, 

                     então:

                        Se for considerado o “145\- VLR\_ICMSS\_N\_ESCRIT” ou “133\- VLR\_ICMSS\_NDESTAC” p/ __Valor do ICMS\-ST__ \(\*\):

                 Preencher com: \(Valor do ICMS\-ST \- Valor do FECEP\-ST\) 

__                       __Senão:

                              Preencher com: \(Valor do ICMS\-ST\)

              Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” não foi marcado, 

              então:

                    Preencher com: \(Valor do ICMS\-ST\)

Onde:

__\- Valor do ICMS\-ST__ \(\*\): Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

__\- __Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.

              \[__MFS665846__\] Tratamento do campo FECEP Regime Fonte, que deve ser somado ao valor do ICMS\-ST independente do valor do FECEP\-ST

- __ICMS\-ST c/ FECEP__ \(valor a ser utilizado na geração do H030\)

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  __Valor do ICMS\-ST__ \(\*\):

    Preencher com:   \(Valor do ICMS\-ST\+  Valor do FECEP Regime Fonte\)   

Senão:

                  Preencher com: \(Valor do ICMS\-ST\+ Valor do FECEP\-ST \+  Valor do FECEP Regime Fonte\)

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  \(Valor do ICMS\-ST\+ Valor do FECEP\-ST \+  Valor do FECEP Regime Fonte\)

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o__  Valor do ICMS\-ST__ \(\*\):

           Preencher com:  \(Valor do ICMS\-ST\+  Valor do FECEP Regime Fonte\)

     Senão

           Preencher com: \(Valor do ICMS\-ST\+ Valor do FECEP\-ST \+  Valor do FECEP Regime Fonte\) 

__              \[MFS977849\]__ Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado 

              Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\) ou DATAMART, então:

                 Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” foi marcado, então:

                      Se for considerado o “145\- VLR\_ICMSS\_N\_ESCRIT” ou “133\- VLR\_ICMSS\_NDESTAC” p/ __Valor do ICMS\-ST__ \(\*\):

               Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP Regime Fonte\) 

__                      __Senão:

                            Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)

               Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” não foi marcado, 

               então:

                     Preencher com: \(Valor do ICMS\-ST \+ Valor do FECEP\-ST \+ Valor do FECEP Regime Fonte\)

Onde:

__\- Valor do ICMS\-ST__ \(\*\): Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

__\- __Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.

- 140\-VLR\_FECP\_ICMS\_ST\.
- QTDE: 24\- Quantidade ou 137\- Quantidade convertida [Conforme regra de conversão](#Conversao_unidade_SAFX08) descrita na RN01

__\[MFS77698\]__ Alteração do cálculo dos valores médios do inventário para retirar o cálculo do valor unitário por nota\.  Os valores serão totalizados e divididos pelo total da quantidade\.

Passo 3\) Calcular os Valores Médios Unitários do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do Inventario \(estoque anterior\):

- Valor Médio Unitário do ICMS = somatório dos valores Unitários de ICMS das notas dividido pelo número de itens de notas recuperadas\.
- Valor Médio Unitário do ICMS\-ST = somatório dos valores unitários de ICMS\-ST das notas dividido pelo número de itens de notas recuperadas\. 

\(valor a ser utilizado no Cálculo da Média Ponderada do Período na RP00B\)

__MFS\-58456: __

- Valor Médio Unitário do ICMS\-ST c/ FECEP = somatório dos valores unitários de ICMS\-ST c/ Fecep das notas dividido pelo número de itens de notas recuperadas\. 

\(valor a ser utilizado na geração do H030\)

- Valor Médio Unitário da Base do ICMS\-ST = somatório dos valores unitários de BC ICMS\-ST das notas dividido pelo número de itens de notas recuperadas\.
- Valor Médio Unitário do FECEP\-ST = somatório dos valores unitários de FECEP\-ST das notas dividido pelo número de itens de notas recuperadas 

Passo 3\) Calcular os Valores Médios do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do Inventario \(estoque anterior\):

- Valor Médio do ICMS = somatório dos valores de ICMS das notas dividido pela quantidade total das notas\.
- Valor Médio do ICMS\-ST = somatório dos valores de ICMS\-ST das notas dividido pela quantidade total das notas 
- Valor Médio do ICMS\-ST c/ FECEP = somatório dos valores de ICMS\-ST c/ Fecep das notas dividido pela quantidade total das notas 
- Valor Médio da Base do ICMS\-ST = somatório dos valores de BC ICMS\-ST das notas dividido pela quantidade total das notas\.
- Valor Médio do FECEP\-ST = somatório dos valores de FECEP\-ST das notas dividido pela quantidade total das notas\.

Passo 4\) Gravar os Valores Médios do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do __estoque anterior __tabela de Média Ponderada \(EST\_ST\_MG\_SALDO\_MED\)\.

__\[MFS511653\]__: Criação do Relatório de Conferência dos Valores Médios do Inventário:

Passo 5\) Relatório de Conferência dos Valores Médios do Inventário:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, gerar um arquivo excel para conferência dos valores médios calculados para os produtos do inventário\.

Nome do arquivo: Relatório\_Conferencia\_Calculo\_Media\_Inventário\_mm\_aaaa\_cod\_estab\.csv

O relatório deve ser composto pelos seguintes registros:

Para cada produto sujeito a ST considerado no cálculo:

\- UM registro demonstrando a quantidade do inventário e os valores unitários médios calculados, que foram gravados na tabela EST\_ST\_MG\_SALDO\_MED\.

\- um ou mais registros correspondentes às notas de entrada consideradas no cálculo\.

Abaixo estão discriminados por cores, os campos que serão gravados para as notas e para o inventário:

\- Em azul: campos que devem ser preenchidos apenas para os registros de notas de entrada

\- Em verde: campos que devem ser preenchidos para o registro de inventário 

\- Em preto: campos que devem ser preenchidos para todos os registros \(notas e inventário\)\.

__\[MFS591080\]__ Tratamento das Incorporações de Empresas/Estabelecimentos

__Código da empresa__

Empresa de login

__Código do estabelecimento__

Estabelecimento informado na tela de geração\.

__Período \(mês e ano\)__

Período informado na tela de geração\.

__Produto \(ind\-cod\)__

Indicador \+ \- \+ Código do produto da Nota de entrada recuperada \(campo 13 e 14 \- SAFX08\)\.

__Data Inventário__

Data do Inventario recuperado \(último dia do mês anterior ao que está sendo processado\)

__Cod Empresa do Doc Fiscal__

Codigo da Empresa da Nota de Entrada \(campo 01 \- SAFX08\)

__Cod Estab do Doc Fiscal__

Codigo do Estabelecimento da Nota de Entrada \(campo 01 \- SAFX08\)

__Data Fiscal __

Data Fiscal da Nota de entrada considerada no cálculo \(campo 03 \- SAFX08\)\.

__Tipo do Documento__

Tipo Documento da Nota de entrada considerada no cálculo \(campo 06 \- SAFX08\)\.

__Número do Documento__

Número da Nota de entrada considerada no cálculo \(campo 09 \-SAFX08\)\.

__Série do Documento__

Série da Nota de entrada considerada no cálculo \(campo 10 \-SAFX08\)\.

__Subsérie do Documento__

Subsérie da Nota de entrada considerada no cálculo \(campo 11 \-SAFX08\)\.

__Pessoa Fis/Jur \(ind\-cod\)__

Indicador \+ \- \+ Código da Pessoa Fis/Jur da Nota de entrada considerada no cálculo \(campo 07 e 08 \-SAFX08\)\.

__Número do Item__

Número do item da Nota de entrada considerada no cálculo \(campo 18 \-SAFX08\)\.

__Medida do Produto__

Unidade de Medida do Cadastro do Produto \(campo 14 – SAFX2013\)

__Medida da Nota__

Unidade de Medida da Nota de entrada considerada \(campo 25 \-SAFX08\)\.

__Quantidade Estoque__

Quantidade recuperada do inventário já convertida para a Unidade de Medida do Produto

__Quantidade da nota__

Quantidade da Nota de entrada recuperada \(campo 24 \-SAFX08\)\.

__Quantidade da nota Convertida__

Quantidade da Nota de entrada recuperada, convertida para unidade de medida do produto\.

__Valor do ICMS da nota__

“*Valor ICMS*” da Nota de entrada, conforme explicado no passo 2\.

__Valor do ICMS\-ST da nota \(sem fecep\)__

*“Valor ICMS\-ST*” da Nota de entrada, conforme explicado no passo 2\.

__Valor do ICMS\-ST da nota \(com fecep\)__

*“Valor ICMS\-ST c/ FECEP*” da Nota de entrada, conforme explicado no passo 2\.

__Valor da Base ICMS\-ST da nota__

*“Valor BC\-ST*” da Nota de entrada, conforme explicado no passo 2\.

__Valor do FECEP\-ST da nota __

“*Valor FECEP\-ST *” da Nota de entrada, conforme explicado no passo 2\.

__Valor Médio Unitário do ICMS__

Valor Unitário Médio do ICMS calculado para o produto e gravado na EST\_ST\_MG\_SALDO\_MED \(vide passo 3\)\.

__Valor Médio Unitário do ICMS\-ST s/ FECEP __

Valor Unitário Médio do ICMS\-ST sem Fecep calculado para o produto e gravado na EST\_ST\_MG\_SALDO\_MED \(vide passo 3\)\.

__Valor Médio Unitário do ICMS\-ST c/ FECEP __

Valor Unitário Médio do ICMS\-ST com Fecep calculado para o produto e gravado na EST\_ST\_MG\_SALDO\_MED \(vide passo 3\)\.

__Valor Médio Unitário da Base de Cálculo do ICMS\-ST__

Valor Unitário Médio da Base do ICMS\-ST calculado para o produto e gravado na EST\_ST\_MG\_SALDO\_MED \(vide passo 3\)\.

__Valor Médio Unitário do FECEP\-ST__

Valor Unitário Médio do FECEP\-ST calculado para o produto e gravado na  EST\_ST\_MG\_SALDO\_MED \(vide passo 3\)\.

__Exemplo:__

Inventário sem os valores médios \(Apenas um registro de Inventário\):

__DATA__

__Produto__

__QTD__

__Valor ICMS Médio__

__Base ICMS\-ST Médio__

__Valor ICMS\-ST Médio __

__Valor FECP\-ST__

__Médio__

31/12

Caneta

100

\-

\-

\-

Notas Fiscais de Entrada até atingir a quantidade do Inventário:

Material Caneta

QTD

Saldo da QTD

Valor do ICMS

Valor da BC do ICMS ST

Valor do ICMS ST

Valor do FCP

Nota Fiscal de entrada de 30/12

50

50

100,00

500,00

100,00

50,00

Nota Fiscal de entrada de 29/12

25

75

50,00

250,00

50,00

25,00

Nota Fiscal de entrada de 28/12

25

__100__

50,00

250,00

50,00

25,00

Inventário anterior após calcular os preços médios:

Material Caneta

QTD

Saldo da QTD

Valor médio do ICMS OP

Valor médio da BC do ICMS ST

Valor médio do ICMS ST

Valor médio do FCP

Inventário de 31/12

100

100

2,00

10,00

2,00

1,00

<a id="CALC_MED_PROD"></a>__CÁLCULO DOS VALORES MÉDIOS DIÁRIOS DO PRODUTO DO PERÍODO__

\[MFS\-67654\] A partir dessa MFS este cálculo não será mais realizado\. Foi substituído pelo cálculo da Média Ponderada definido na regra [RP00B](#RP00B)\. 

Nota técnica: rotina implementada na função CalcMedProd da EFD\_CALC\_RESSARC\_MG\_FPROC\.

Após calcular os Valores Médios Unitários do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do inventário \(__estoque anterior__\), vamos calcular os valores médios unitários de todos os dias do período da geração e  gravar na tabela de Médias Ponderadas EST\_ST\_MG\_SALDO\_MED\.

Ao final desse processo, para cada produto sujeito a ST, teremos um registro do inventário \(estoque anterior\) \+ um registro para cada dia do período da geração na tabela de Médias Ponderadas EST\_ST\_MG\_SALDO\_MED\. Veja: 

\- Último dia do Mês anterior c/ Valores Médios Unitários do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do inventário;

\- Dia 01 do mês da geração c/ Valores Médios Unitários __Provisórios__ do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do DIA 01;

\- Dia 02 do mês da geração c/ Valores Médios Unitários __Provisórios__ do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do DIA 02;

\.\.\.\.

\- Último dia do mês da geração c/ Valores Médios Unitários __Provisórios__ do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do último DIA  

Exemplo: se a geração foi do mês de janeiro, 32 registros por produto\.

OBS: A tabela armazena os Valores Médios Unitários __Provisórios__ dos dias do mês\. 

Os Valores Médios Unitários que serão utilizados na geração do C185, C181, C330, C430 __não__ são os Valores Médios Unitários __Provisórios__ do dia, e sim os Valores Médios Unitários __Definitivos__ \(__Valores Médios Diários do Produto__\), que são calculado no momento da geração de cada um desses registros, a partir de uma nova média realizada com Valores Médios Unitários do Inventário \(ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\) mais os Valores Médios Unitários __Provisórios __do dia 01 até dia da nota de saída\. Ver [RP02](#RP02_Regras185_precomedio_conversao)\.

Procedimentos:

Passo1\) Recuperar as entradas do Período dos produtos sujeitos a ST \(não considerar devoluções\)\.

Passo2\) Calcular os Valores unitários do ICMS, ICMS\-ST, Base do ICMS\-ST e FECEP\-ST para cada nota de entrada tratando de forma diferenciada entradas normais e a devoluções:

Calcular os valores unitários do ICMS, ICMS\-ST, Base do ICMS\-ST e FECEP\-ST considerando VALOR ICMS/QTDE, VLR ICMS\-ST/QTDE, BC\-ST/QTDE e FECEP\-ST/QTDE, onde os valores são oriundos da SAFX08: 

- VALOR ICMS:

43\-VLR\_ICMS ou 80 \- VLR\_ICMS\_NDESTAC ou __“225\-Valor ICMS Não Destacado”__, \(conforme regras abaixo\):

__\[MFS47958\]__

Se campo 43\-VLR\_ICMS estiver preenchido, considerar o campo ‘43\-VLR\_ICMS, ’senão:

Se o campo 80 –  VLR\_ICMS\_NDESTAC estiver preenchido, considerar o campo 80 –  VLR\_ICMS\_NDESTAC, ’senão:

Se o campo __“225\-Valor ICMS Não Destacado”__, estiver preenchido, considerar o campo __“225\-Valor ICMS Não Destacado”\.__

- BC\-ST: 

61\-BASE\_SUB\_TRIB\_ICMS ou 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT ou 106\-VLR\_BASE\_ICMS\_ORIG;

- VLR ICMS\-ST: 

52\-VLR\_SUBST\_ICMS ou 145 \- VLR\_ICMSS\_N\_ESCRIT ou 133\-VLR\_ICMSS\_NDESTAC ou 107\-VLR\_TRIB\_ICMS\_ORIG \(conforme regras abaixo\):

                       Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

Considerar os campos “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” da SAFX08\.

Senão

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT e 145\- VLR\_ICMSS\_N\_ESCRIT” da SAFX08\.

Senão

Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” estiverem preenchidos, então: 

Considerar os campos “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e “133\- VLR\_ICMSS\_NDESTAC” da SAFX08 

Senão

Se campo “106\-VLR\_BASE\_ICMS\_ORIG” e “107\-VLR\_TRIB\_ICMS\_ORIG” estiverem preenchidos, então: 

Considerar o campo “106\-VLR\_BASE\_ICMS\_ORIG” e “107\- VLR\_TRIB\_ICMS\_ORIG” da SAFX08\.

- 140\-VLR\_FECP\_ICMS\_ST\.
- QTDE: 24\- Quantidade ou 137\- Quantidade convertida [Conforme regra de conversão](#Conversao_unidade_SAFX08) descrita na RN01

Passo 3\) Calcular os Valores Médios Unitários__ Provisórios__ \(__médio diário provisório\)__ do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do __DIA__:

               Valor Médio Unitário do ICMS = somatório dos valores unitários de ICMS das notas dividido pelo número de notas recuperadas __no dia__\.

               Valor Médio Unitário do ICMS\-ST = somatório dos valores unitários de ICMS\-ST das notas dividido pelo número de notas recuperadas __no dia__\.

               Valor Médio Unitário do Base do ICMS\-ST = somatório dos valores unitários de BC ICMS\-ST das notas dividido pelo número de notas recuperadas__ no dia__\.

               Valor Médio Unitário do FECEP\-ST = somatório dos valores unitários de FECEP\-ST das notas dividido pelo número de notas recuperadas__ no dia\.__ 

Passo 4\) Gravar os Valores Médios Unitários Provisórios \(__médio diário provisório\)__ do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do __DIA __tabela de Média Ponderada \(EST\_ST\_MG\_SALDO\_MED\)\.

*Mais uma vez ressaltando que o cálculo Valores Médios Unitários *__*Definitivos \(Valores Médios Diários do Produto\)*__* são calculados no momento da geração dos registros de Saída \(C185, C330, C430\) e devolução de saída \(C181\) conforme explicado na [RP02](#RP02_Regras185_precomedio_conversao) e que na tabela são armazenados os Valores Médios Unitários do Inventário e os Valores Médios Unitários *__*Provisórios*__* dos dias do mês da geração\.*

Detalhes do Exemplo:

__Médio do Inventário Anterior:__

__DATA__

__Produto__

__QTD__

__Valor ICMS Médio__

__Valor BASE ICMS\-ST Médio__

__Valor ICMS\-ST Médio __

__Valor FECP\-ST__

__Médio__

31/12

Caneta

100

Valor ICMS Médio

Valor Base ICMS\-ST Médio

Valor ICMS\-ST Médio 

Valor FECP\-ST

Médio

Notas de entrada normal

__DATA__

__Nota__

__QTD__

__\*\*Valor ICMS  UNITÁRIO__

__Valor Base ICMS\-ST UNITÁRIO__

__Valor ICMS\-ST__

__UNITÁRIO__

__Valor FECP\-ST__

__UNITÁRIO__

01/01

Nota 01

100

Valor ICMS/qtd da nota

Valor Base ICMS\-ST/qtd da nota

Valor ICMS\-ST/ qtd da nota

Valor FECP\-ST/ qtd da nota

01/01

Nota 02

50

Valor ICMS/qtd da nota

Valor Base ICMS\-ST/qtd da nota

Valor ICMS\-ST/ qtd da nota

Valor FECP\-ST/ qtd da nota

Preço médio diário provisório 

Soma os valores /divide pela quantidade de notas que foram calculadas no dia

Soma os valores /divide pela quantidade de notas que foram calculadas no dia

Soma os valores /divide pela quantidade de notas que foram calculadas no dia

Soma os valores /divide pela quantidade de notas que foram calculadas no dia

__Preço Médio do Dia__

__Preço médio __

__\*\*Valor ICMS UNITARIO Médio__

__Valor Base ICMS\-ST UNITÀRIO Médio__

__Valor ICMS\-ST__

__UNITARIO__

__Médio__

__Valor FECP\-ST__

__UNITARIO__

__Médio__

Inventário

3,33

33,33

3,33

0,33

Dia 01

3,50

35,00

3,50

0,35

__Média do dia 01__

3,41

34,16

3,41

3,41

__Atenção:__ Se não encontrarmos o inventário do período anterior, consideraremos que o produto foi incluído no período da geração, neste caso, só será calculado o custo médio do produto diário com base nas notas de entrada, sem considerar a média do inventário\.

MFS\-71202

MFS\-58456

MFS\-73772

MFS\-77698

<a id="RP00B"></a>RP00B

MFS\-67654:

__NOVO CÁLCULO MÉDIO PODERADO VALORES MÉDIOS DIÁRIOS DO PRODUTO DO PERÍODO__

Gravação da Tabela de “Cálculo da Média Pondera Móvel dos Valores Unitários” \(__EST\_ST\_MG\_MEDIA\_POND\)__

Esse cálculo segue a lógica da Média Ponderada Móvel calculada no Ressarcimento ST RS \(*MTZ\-Ressarc\-RS\-IN087\_2020\_Geracao\_Movimentos\_Cálculo Média Ponderada\.docx*\)\.

__Nota técnica__: Diferentemente do Ressarcimento do RS que mantém os registros de períodos anteriores na EST\_ST\_RS\_MEDIA\_POND, no Ressarcimento de MG pode\-se manter só com os dados do período na a tabela EST\_ST\_MG\_MEDIA\_POND\. Pelos seguintes motivos: 

\- o saldo inicial do primeiro dia 01 do mês será sempre recalculado, não será recuperado da tabela EST\_ST\_MG\_MEDIA\_POND do último dia do mês anterior\.

\- as devoluções de saídas que recuperam os valores médios de períodos anteriores na EST\_ST\_RS\_MEDIA\_POND, não serão consideradas no cálculo de MG\.  

Sendo assim não há necessidade de manter os dados de períodos anteriores na EST\_ST\_MG\_MEDIA\_POND\.

__Visão resumida do Processamento__

O Cálculo deve ser executado dia por dia, em __ordem cronológica__\.

Para cada __produto sujeito ao ICMS\-ST __\(\*\) __e__ __dia__ do mês da geração, executar:

  

1º Passo: Calcular o Saldo Inicial do dia 

2º Passo: Calcular o Total das Entradas do dia

3º Passo: Calcular o Total das Devoluções de Entradas do dia

4º Passo: Calcular o Saldo Final do dia gravando a tabela EST\_ST\_MG\_MEDIA\_POND

\(\*\) __Produto ou NCM \(sujeito ao ICMS\-ST\)__

Produto sujeito ao ICMS\-ST são os produtos cujo CÓDIGO ou NCM esteja parametrizado em uma das opções de menu “Parâmetros à Ressarcimento ICMS\-ST à Produtos”, ou, “Parâmetros à Ressarcimento ICMS\-ST à NCM”, com a data de validade da parametrização acordo com o período informado na tela da geração\. A prioridade na pesquisa da parametrização dos produtos é: por Código, e depois por NCM, da seguinte forma:

\- Caso o produto conste na parametrização por código \(opção “Produtos”\), a parametrização por NCM não precisa ser verificada;

             \- Caso não, é verificado se o NCM do produto \(NCM do cadastro do produto\) consta na parametrização da opção “NCM’s”;

## <a id="_Toc63699479"></a>1º Passo – Calcular o Saldo Inicial do Dia

Para calcular o saldo inicial do dia vamos adotar dois procedimentos, um aplicado ao primeiro dia do mês da geração, e outro para os demais dias do mês:

- __Primeiro Dia do mês da geração:__

Para o __Primeiro Dia__ do mês da geração, realizar duas recuperações:

\- Buscar a Quantidade de Inventário na Tabela do Inventário \(X52\_INVENT\_PRODUTO\) para o último dia do período anterior ao indicado na tela\. Exemplo: se geração é de Fevereiro/2021 buscar o inventário de 31/01/2021\.

\- Buscar os Valores Médios Unitários do ICMS, do ICMS\-ST, da Base do ICMS\-ST e FECEP\-ST do estoque anterior calculados na [RN00A](#RP00A) \- __[CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\)](#CALC_MED_INV) \- __ Passo 3\.

__Critérios da recuperação do Inventário \(X52\_INVENT\_PRODUTO\):__

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data do Inventário = último dia do período anterior ao indicado na tela \(Cálculo ICMS\-ST\);
- Campo Motivo do Inventário \(Campo 40 – IND\_MOT\_INV\) = “06”;
- Produto sujeito ao ST que está sendo considerado para o Cálculo da Média Ponderada

Com a quantidade do inventário e os valores unitários, calcular as seguintes informações que irão compor o Saldo Inicial do dia:

- Qtde total Convetida Inicial: 

Campo 13\-Quantidade de Inventário, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade do inventário __\(\*\)__ = unidade do cadastro do produto __\(\*\*\) __

      __\(\*\)__ unidade do inventário = campo “12\-Unidade de Medida” da SAFX52

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será a própria quantidade do inventário;

__Senão __

         Nesse caso a quantidade do inventário \(SAFX52\) será convertida para a unidade de medida do cadastro do produto;

         \[Quantidade de Inventário \* Fator de Conversão\]

__Sobre a conversão de medida:__

A conversão de medida será efetuada conforme o procedimento padrão, ou seja, utilizando as tabelas de conversão de medidas do Módulo DW \(menu “*Manutenção à Cadastros à Conversão de Unidades de Medida*”\), da seguinte forma:

\- Em primeiro lugar, verifica se existe o fator de conversão na tabela de conversão por produto;

\- Caso não exista, pesquisa o fator na tabela de conversão padrão;

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, será gravada a seguinte mensagem de erro no log:

“*Cálculo da Média Ponderada Móvel: Fator de conversão de medida de XXX para XXX não encontrado\. Não foi possível calcular o Saldo inicial do dia “XX” para o produto\.*

             __\[MFS74069\]__ Tratamento do parâmetro para indicar se deve ser gerado o log de erro de produto sem inventário 

             somente para produtos com movimentação\.

Caso não seja encontrado inventário e o parâmetro “Somente mostrar log de produto sem inventário p/ produtos c/ movimento” estiver desmarcado, e o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário” estiver desmarcado, exibir a seguinte mensagem:

“*Cálculo da Média Ponderada Móvel: Não foi localizado inventário com motivo 06 para os Produtos ou NCMs cadastrados nas telas de Parametrização localizados em: SPED/Escrituração Fiscal Digital/Parâmetros/Ressarcimento ICMS\-ST\. Não será gravada a Média Ponderada deste Produto”*

                         Produto será desconsiderado do cálculo da média poderada\.

__             \[MFS74991\]__ Inclusão da geração do registro de inventário na SAFX52\.

             Caso não seja encontrado inventário e o parâmetro “Somente mostrar log de produto sem inventário p/ produtos c/                

             movimento” estiver marcado ou o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário”                   

             estiver marcado, deve\-se verificar se existem notas fiscais no período da geração com os seguintes critérios:

        Empresa – código da empresa do login; 

        Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 

        Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 

        Somente notas *não canceladas*; 

        Somente notas *com itens*; 

        Modelo somente modelos de notas 01,1B, 04, 55 e 65;    

        Produto ou NCM \(sujeito ao ICMS\-ST\) parametrizados; 

        CFOP ou CFOP/Natureza de Operação parametrizado para alguma destas operações:

                        \- Saída Interna para Consumidor Final \(art 31\-A \- Anexo XV do RICMS/02\) 

                        \- Saída para Outras Unidade da Federação  \(art 23 \- Anexo XV do RICMS/02\) 

                        \- Saída com Isenção ou não Incidência \(art 23 \- Anexo XV do RICMS/02\) 

                        \- Perecimento, Furto, Roubo ou qualquer outro Tipo de Perda \(art 23 \- Anexo XV do RICMS/02\) 

                        \- Devolução de Entrada Interestadual 

                        \- Entrada \(e Devolução\) 

*                     *Se o parâmetro “Somente mostrar log de produto sem inventário p/ produtos c/ movimento” estiver marcado e   

                          existir pelo menos uma nota fiscal no mês nas condições acima, exibir a seguinte mensagem:

“*Cálculo da Média Ponderada Móvel: Não foi localizado inventário com motivo 06 para os Produtos ou NCMs cadastrados nas telas de Parametrização localizados em: SPED/Escrituração Fiscal Digital/Parâmetros/Ressarcimento ICMS\-ST\. Não será gravada a Média Ponderada deste Produto”\.*

Produto será desconsiderado do cálculo da média poderada\.

*                     *Senão \(Parâmetro marcado e sem notas ficais no mês\)

                          Não exibir mensagem de erro\.

                           Produto será desconsiderado do cálculo da média poderada\.

                      Se o parâmetro “Gerar registro de inventário p/ produtos c/ movimento e sem inventário” estiver marcado

                           Gerar um registro de inventário para cada produto que não tem um registro na SAFX52, conforme regras     

                           especificadas na RP00BSafx52\.     

Obs: por questões de performance, apenas 50 logs de produtos sem inventário estão sendo exibidos\.

- Valor do ICMS Calculado Inicial

\[Qtde total Convetida Inicial \* Valor Médio Unitário do ICMS \]

Valor Médio Unitário do ICMS calculado na [RP00A](#RP00A) \- __[CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\)](#CALC_MED_INV) \- __ Passo 3__\.__

- Valor do ICMS\-ST Calculado Inicial 

\[Qtde total Convetida Inicial \* Valor Médio Unitário do ICMS\-ST\]

Valor Médio Unitário do ICMS\-ST calculado na [RP00A](#RP00A) \- __[CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\)](#CALC_MED_INV) \- __ Passo 3__\.__

- Valor Base de Cálculo do ICMS\-ST Calculado Inicial 

\[Qtde total Convetida Inicial \* Valor Médio Unitário da Base ICMS\-ST\]

Valor Médio Unitário da Base ICMS\-ST calculado na [RP00A](#RP00A) \- __[CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\)](#CALC_MED_INV) \- __ Passo 3\.

- Valor FECEP\-ST Calculado Inicial 

\[Qtde total Convetida Inicial \* Valor Médio Unitário FECEP\-ST\]

Valor Médio Unitário FECEP\-ST calculado na [RP00A](#RP00A) \- __[CÁLCULO DOS VALORES MÉDIOS DO INVENTÁRIO \(ESTOQUE ANTERIOR\)](#CALC_MED_INV) \- __ Passo 3\.

- __Segundo Dia do mês da geração em diante:__

Para o __Demais Dias__ do mês da geração, recuperar o saldo final do dia anterior da tabela do “Cálculo da Média Pondera Móvel dos Valores Unitários” \(EST\_ST\_MG\_MEDIA\_POND\) para o produto em questão\. 

     Recuperar as seguintes informações:

- Qtde total Convetida Final \(QTD\_CONV\_FIM\_MP\):
- Valor do ICMS Calculado Final \(VLR\_ICMS\_FIM\_MP\)
- Valor do ICMS\-ST Calculado Final \(VLR\_ICMS\_ST\_FIM\_MP\)
- Valor Base de Cálculo do ICMS\-ST Calculado Final \(VLR\_BC\_ST\_FIM\_MP\)
- Valor FECEP\-ST Calculado Final \(VLR\_FECEP\_ST\_FIM\_MP\)

## <a id="_Toc63699481"></a>2º Passo: Calcular o Total das Entradas do Dia

Baseado nas regras de geração do C180\.

Nesse passo recuperar as entradas do dia conforme critérios a seguir:

__Origem dos dados__: \- Parametrização de Produtos 

                                  \- Parametrização de NCM’s; 

                                  \- Parametrização de CFOP ou CFOP/Natureza de Operação; 

                                  \- Tabelas dos Documentos Fiscais \(SAFX07/SAFX08\); 

__\[MFS73772\] __ Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada

__\[MFS82924\] __ As notas fiscais que não possuírem pelo menos um dos valores de ICMS \(Valor de ICMS, Valor ICMS\-ST, Base ICMS\-ST, FECP ICMS\-ST\) preenchido, serão desconsideradas do cálculo\.

__Critérios da recuperação das Notas Fiscais: __  

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Fiscal – data enquadrada no período informado em tela \(Tela Cálculo ICMS\-ST\); 
- Somente notas de Entrada;
- Somente notas *não canceladas* e que não sejam de devolução; 
- Somente notas *com itens*; 
- Modelo – somente os documentos de modelo = __*01, 1B, 04, 55 e 65*__;    
- Produto sujeito ao ST que está sendo considerado para o Cálculo da Média Ponderada;
- CFOP ou CFOP/Natureza de Operação parametrizado para “Entrada \(e Devolução\)”;
- Somente as notas que possuírem pelo menos um dos valores de ICMS \(Valor de ICMS ou Valor ICMS\-ST ou Base ICMS\-ST ou FECP ICMS\-ST\) utilizado no cálculo preenchido, que são os campos de valores destacadados abaixo 

Calcular as seguintes informações:

- Quantidade Entrada Convertida:

Campo 24\-Quantidade \(SAFX08\) do Item da nota de Entrada, aplicando a conversão, quando necessário\. Veja:

__Se__ unidade da nota __\(\*\)__ = unidade do cadastro do produto __\(\*\*\)__

      __\(\*\)__ unidade da nota = campo “25\-Unidade de Medida” da SAFX08 do Item da NF de Entrada

      __\(\*\*\)__ unidade do produto = campo “14\-Código de Medida” da SAFX2013 

      Nesse caso não há necessidade de conversão, e o campo será gerado a própria quantidade do item da nota;

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

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, a Quantidade Entrada Convertida ficará zerada\. 

Obs, não vamos gerar mensagem de erro no log, pois a mesma já é dada pela geração do C180\.

- Valor do ICMS Calculado para Entrada:

Valor do ICMS é oriundo de um dos três campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- Valor do ICMS\-ST Calculado para Entrada:

Preencher com:

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  __Valor do ICMS\-ST__ \(\*\):

    Preencher com:   \(Valor do ICMS\-ST\- Valor do FECEP\-ST\) 

Senão:

                  Preencher com: \(Valor do ICMS\-ST\) 

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com:  \(Valor do ICMS\-ST\) 

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o__  Valor do ICMS\-ST__ \(\*\):

           Preencher com:  \(Valor do ICMS\-ST \- Valor do FECEP\-ST\) 

     Senão

           Preencher com: \(Valor do ICMS\-ST\)

__             \[MFS977849\]__ Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado 

              Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\) ou DATAMART, então:

                    Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” foi marcado, 

                     então:

                        Se for considerado o “145\- VLR\_ICMSS\_N\_ESCRIT” ou “133\- VLR\_ICMSS\_NDESTAC” p/ __Valor do ICMS\-ST__ \(\*\):

                 Preencher com: \(Valor do ICMS\-ST \- Valor do FECEP\-ST\) 

__                       __Senão:

                              Preencher com: \(Valor do ICMS\-ST\)

              Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” não foi marcado, 

              então:

                    Preencher com: \(Valor do ICMS\-ST\)

 

Onde os valores são oriundos do item da nota de Entrada:

__\- Valor do ICMS\-ST__ \(\*\): Valor do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor do ICMS\-ST = 52\-VLR\_SUBST\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

         Valor do ICMS\-ST = 145\- VLR\_ICMSS\_N\_ESCRIT\.

    Senão:

        Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                         “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

             Valor do ICMS\-ST = 133\- VLR\_ICMSS\_NDESTAC\.

        Senão:

            Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

                 Valor do ICMS\-ST = 107\- VLR\_TRIB\_ICMS\_ORIG

__\- __Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08\.

- Valor Base de Cálculo do ICMS\-ST Calculado para Entrada:

Valor da Base de Cálculo do ICMS\-ST é oriundo de um dos quatro campos do item da nota fiscal de Entrada \(SAFX08\), dependendo de qual esteja preenchido:

Se campo “61\-BASE\_SUB\_TRIB\_ICMS” e “52\-VLR\_SUBST\_ICMS” estiverem preenchidos, então:

   Valor da BC\-ST = 61\-BASE\_SUB\_TRIB\_ICMS\.

Senão: 

    Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                     “145\- VLR\_ICMSS\_N\_ESCRIT” estiverem preenchidos, então:

       Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

    Senão:

       Se campo “144\- VLR\_BASE\_ICMSS\_N\_ESCRIT” e 

                        “133\- VLR\_ICMSS\_NDESTAC” preenchidos, então:

          Valor da BC\-ST = 144 \- VLR\_BASE\_ICMSS\_N\_ESCRIT\.

       Senão:

           Se campo “106\- VLR\_BASE\_ICMS\_ORIG” e 

                             “107\- VLR\_TRIB\_ICMS\_ORIG” preenchidos, então:

               Valor da BC\-ST = 106 \- VLR\_BASE\_ICMS\_ORIG

- Valor FECEP\-ST Calculado para Entrada:

Valor do FECEP\-ST é oriundo do item da nota fiscal de Entrada \(SAFX08\):

Campo 140\-FECEP ICMS\-ST da SAFX08\.

## <a id="_Toc63699482"></a>3º Passo: Calcular o Total das Devoluções de Entradas do Dia

Baseado nas regras de geração do C186\.

Nesse passo recuperar as Devoluções de Entradas do dia conforme critérios a seguir:

## 1 – Recuperação das Notas Fiscais de Devolução \(norm\_dev = ‘2’/ movto\_e\_s = ‘9’\)

__Origem dos dados__: \- Parametrização de Produtos \(por Código, por NCM e por CEST\);

                                  \- Parametrização de CFOP / Natureza de Operação;

                                  \- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais \(DATAMART\)

__\[MFS73772\] __Inclusão da verificação da nova parametrização de CFOP ou CFOP/Natureza para as operações de entrada

__Critérios da recuperação das Notas Fiscais de Devolução: __

- Empresa – código da empresa do login;
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal – data enquadrada no período informado em tela;
- Nota fiscal de devolução \(NORM\_DEV = “2”\);
- Nota de Saída \(MOVTO\_E\_S = “9”\);
- Modelo = 01, 1B, 04, 55, 65 
- Somente notas *não canceladas*;
- Somente notas *com itens*;
- Produto sujeito ao ST que está sendo considerado para o Cálculo da Média Ponderada;
- CFOP ou CFOP/Natureza de Operação parametrizado para “Entrada \(e Devolução\)”;

Recuperar as seguintes informações da nota de devolução \(SAFX07/SAFX08\):

\- Campos de Identificação da Capa e do Item da nota de devolução;

\- 13,14 \- Produto – GRUPO\_PRODUTO, IND\_PRODUTO, COD\_PRODUTO \(SAFX08\)

\- Unidade de Medida do Produto \(SAFX2013\)

\- 24 \- Quantidade \- QUANTIDADE \(SAFX08\)

\-137\-Quantidade Convertida \(SAFX08\)

\- 25 \- Unidade de Medida \- COD\_MEDIDA \(SAFX08\)

Para cada item de mercadoria da nota de devolução vamos recuperar a\(s\) nota\(s\) de entradas\(s\) devolvida\(s\)\.

Buscar a entrada a partir dos campos de referência da SAFX08 \(117, 118, 119, 102\)\.

Caso esses campos não estejam preenchidos, a nota de devolução será desconsiderada do Cálculo da Média Ponderada\.  Não será exibida mensagem no log, pois a mesma já é dada na geração do C186\.

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

O parâmetro “__*Utilizar DATA MART para períodos anteriores*__” determinará se a nota fiscal de saída será recuperada das Tabelas Normais \(X07/X08\), ou das Tabelas DATAMART \(dwt\)\. Caso o parâmetro esteja selecionado, as tabelas DATAMART serão consideradas, caso contrário utilizar as tabelas Normais \(X07/X08\)\.

Caso a nota de referência não seja encontrada na base de dados, a nota de devolução será desconsiderada do Cálculo da Média Ponderada\.  Não será exibida mensagem no log, pois a mesma já é dada na geração do C186\.

Calcular as seguintes informações:

- Quantidade Entrada Referenciada pela devolução Convertida \(__QTD\_CONV\_NF\_ENT\)__:

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

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, a Quantidade Entrada Convertida \(__QTD\_CONV\_NF\_ENT__\) ficará zerada\. 

Obs, não vamos gerar mensagem de erro no log, pois a mesma já é dada pela geração do C186

- Quantidade Devolvida Convertida \(__QTD\_CONV\_NF\_DEV__\)

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

Caso não seja identificado o fator de conversão em nenhuma das duas tabelas, a Quantidade Devolvida Convertida \(__QTD\_CONV\_NF\_DEV__\) ficará zerada\. 

Obs, não vamos gerar mensagem de erro no log, pois a mesma já é dada pela geração do C186

- Valor do ICMS Calculado para Devolução

Preencher com:

 \(Valor do ICMS / QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

Onde:

- Valor do ICMS é oriundo de um dos três campos SAFX08, do item da nota de Entrada referenciada, dependendo de qual esteja preenchido:

Campo “43\-Valor ICMS”, se preenchido, ou

   Campo “80\-ICMS não Escriturado”, se preenchido, ou

       Campo “225\-Valor ICMS Não Destacado”  

- QTD\_CONV\_NF\_ENT: Quantidade Entrada Referenciada pela devolução Convertida \(QTD\_CONV\_NF\_ENT\)
- QTD\_CONV\_NF\_DEV: Quantidade Devolvida Convertida \(QTD\_CONV\_NF\_DEV\)
- Valor do ICMS\-ST Calculado para Devolução 

Preencher com:

 \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

__MFS\-58456: Tratamento do FECEP\-ST quando embutido no ICMS\-ST__

Tratamento do FECEP embutido nos vlrs de ICMS/ICMS\-ST \(aplicado às Entradas e Devoluções de Entradas\):

Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\), então:

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” foi marcado, então:

             Se for considerado o “52\-Valor ICMS Substituição Tributária” p/ o  __Valor do ICMS\-ST__ \(\*\):

    Preencher com: \[\(Valor do ICMS\-ST\- Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT\] \* QTD\_CONV\_NF\_DEV

Senão:

                  Preencher com: \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

      Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS/ICMS\-ST nos itens \(SAFX08\)” não foi marcado, então:

           Preencher com: \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

Se o item de mercadoria foi recuperado das tabelas do DATAMART, então:

     Se for considerado o “52\-Valor ICMS Substituição Tributária” para o __ Valor do ICMS\-ST__ \(\*\):

           Preencher com:  \[\(Valor do ICMS\-ST\- Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT\] \* QTD\_CONV\_NF\_DEV

     Senão

           Preencher com: \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

__              \[MFS977849\]__ Tratamento do FECEP embutido nos valores de ICMS\-ST não escriturado e não destacado 

              Se o item de mercadoria foi recuperado das tabelas “normais” \(X07/X08\) ou DATAMART, então:

                 Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” foi marcado, então:

                      Se for considerado o “145\- VLR\_ICMSS\_N\_ESCRIT” ou “133\- VLR\_ICMSS\_NDESTAC” p/ __Valor do ICMS\-ST__ \(\*\):

                           Preencher com: \[\(Valor do ICMS\-ST\- Valor do FECEP\-ST\)/ QTD\_CONV\_NF\_ENT\] \* QTD\_CONV\_NF\_DEV__                                    __

__                     __Senão:

                            Preencher com: \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

               Se o campo “Vlrs de FECEP estão embutidos nos vlrs de ICMS\-ST não destacado/não escriturado” não foi marcado, 

               então:

       Preencher com: \(Valor do ICMS\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

Onde:

- \(\*\)__Valor do ICMS\-ST__ é oriundo de um dos quatro campos SAFX08, do item da nota de Entrada referenciada, dependendo de qual esteja preenchido:

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

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08, do item da nota de Entrada referenciada\.
- QTD\_CONV\_NF\_ENT: Quantidade Entrada Referenciada pela devolução Convertida \(QTD\_CONV\_NF\_ENT\)
- QTD\_CONV\_NF\_DEV: Quantidade Devolvida Convertida \(QTD\_CONV\_NF\_DEV\)
- Valor Base de Cálculo do ICMS\-ST Calculado para Devolução 

Preencher com:

 \(Valor da BC\-ST / QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

Onde:

- Valor da BC\-ST é oriundo de um dos quatro campos SAFX08, do item da nota de Entrada referenciada, dependendo de qual esteja preenchido:

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

- QTD\_CONV\_NF\_ENT: Quantidade Entrada Referenciada pela devolução Convertida \(QTD\_CONV\_NF\_ENT\)
- QTD\_CONV\_NF\_DEV: Quantidade Devolvida Convertida \(QTD\_CONV\_NF\_DEV\)
- Valor FECEP\-ST Calculado para Devolução

Preencher com:

\(Valor do FECEP\-ST/ QTD\_CONV\_NF\_ENT\) \* QTD\_CONV\_NF\_DEV

Onde:

- Valor do FECEP\-ST é oriundo do campo 140\-FECEP ICMS\-ST da SAFX08, do item da nota de Entrada referenciada\.
- QTD\_CONV\_NF\_ENT: Quantidade Entrada Referenciada pela devolução Convertida \(QTD\_CONV\_NF\_ENT\)
- QTD\_CONV\_NF\_DEV: Quantidade Devolvida Convertida \(QTD\_CONV\_NF\_DEV\)

## 4º Passo: Calcular o Saldo Final do dia

Para cada __Produto__ sujeito ao ICMS\-ST\(\*\), gravar um registro na tabela com os valores calculados no __dia__: Saldo Inicial, Total das Entradas, Total das Devoluções de Entradas e Saldo Final\.

\(\*\) __Produto__ sujeito ao ICMS\-ST\(\*\) são os produtos cujo CÓDIGO ou NCM esteja parametrizado numa mas opções de menu “*Parâmetros à Ressarcimento ICMS\-ST à Produtos*”, __ou__, “*Parâmetros à Ressarcimento ICMS\-ST à NCM*”, com a data de validade da parametrização  acordo com o período informado na tela da geração\.

Observação: Caso as consultas descritas nos passos \(1, 2, 3\) não retornarem registros para o __Produto__ sujeito ao ICMS\-ST\(\*\), gravar a tabela __EST\_ST\_MG\_MEDIA\_POND__ com os campos relacionados zerados\.  Esse passo é importante, pois o mês pode começar sem inventário e movimento, mas no meio do mês pode iniciar um movimento\. A tabela deve possuir um registro para cada dia do mês\.

__PK__

__Campo__

__Regra de Preenchimento__

__Campos para relatório__

\(\*\)

Código da Empresa 

COD\_EMPRESA

Código da empresa da nota de Entrada \(SAFX07\) 

Cod Empresa

\(\*\)

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento do inventário/movimento recuperado nos passos anteriores\.

Cod Estab

\(\*\)

Data 

DATA

Dia que está sendo processado\.

Dia

\(\*\)

Produto

Grupo\_Produto, Ind\_Produto,

Cod\_Produto

Produto sujeito ao ICMS\-ST \(\*\)

Ind Produto

\(SAFX2013\-01\)

Cod Produto \(SAFX2013\-02\)

__Saldo Inicial do Dia__

Qtde total Convertida Inicial

QTD\_CONV\_INI

“Qtde total Convertida Inicial” calculada no 1º Passo;

Qtde Inicial

Valor do ICMS Calculado Inicial

VLR\_ICMS\_INI\_MP

“Valor do ICMS Calculado Inicial” calculado no 1º Passo;

Valor ICMS Inicial

Valor do ICMS\-ST Calculado Inicial

VLR\_ICMS\_ST\_INI\_MP

“Valor do ICMS\-ST Calculado Inicial” calculado no 1º Passo;

Valor ICMS\-ST Inicial

Valor Base de Cálculo do ICMS\-ST Calculado Inicial

VLR\_BC\_ST\_INI\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado Inicial” calculado no 1º Passo;

Valor Base de Cálculo do ICMS\-ST Inicial

Valor FECEP\-ST Calculado Inicial

VLR\_FECEP\_ST\_INI\_MP

“Valor FECEP\-ST Calculado Inicial” calculado no 1º Passo;

Valor FECEP\-ST Inicial

__Entradas do Dia__

Quantidade Entrada Convertida

QTD\_CONV\_ENT\_MP

“Quantidade Entrada Convertida” recuperada no 2º Passo;

Qtde \(Entrada\)

Valor do ICMS Calculado para Entrada

VLR\_ICMS\_ENT\_MP

“Valor do ICMS Calculado para Entrada” recuperado no 2º Passo;

Valor ICMS \(Entrada\)

Valor do ICMS\-ST Calculado para Entrada

VLR\_ICMS\_ST\_ENT\_MP

“Valor do ICMS\-ST Calculado para Entrada” recuperado no 2º Passo;

Valor ICMS\-ST \(Entrada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Entrada

VLR\_BC\_ST\_ENT\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado para Entrada” recuperado no 2º Passo;

Valor Base de Cálculo do ICMS\-ST \(Entrada\)

Valor FECEP\-ST Calculado para Entrada

VLR\_FECEP\_ST\_ENT\_MP

“Valor FECEP\-ST Calculado para Entrada” recuperado no 2º Passo;

Valor FECEP\-ST \(Entrada\)

__Devoluções das Entradas do Dia__

Quantidade Devolvida Convertida 

QTD\_CONV\_DEV\_ENT\_MP

“Quantidade Devolvida Convertida” recuperada no 3º Passo;

Qtde \(Devolução Entrada\)

Valor do ICMS Calculado para Devolução

VLR\_ICMS\_DEV\_ENT\_MP

“Valor do ICMS Calculado para Devolução” recuperado no 3º Passo;

Valor ICMS \(Devolução Entrada\)

Valor do ICMS\-ST Calculado para Devolução

VLR\_ICMS\_ST\_DEV\_ENT\_MP

“Valor do ICMS\-ST Calculado para Devolução” recuperado no 3º Passo;

Valor ICMS\-ST \(Devolução Entrada\)

Valor Base de Cálculo do ICMS\-ST Calculado para Devolução

VLR\_BC\_ST\_DEV\_ENT\_MP

“Valor Base de Cálculo do ICMS\-ST Calculado para Devolução” recuperado no 3º Passo;

Valor Base de Cálculo do ICMS\-ST \(Devolução Entrada\)

Valor FECEP\-ST Calculado para Devolução

VLR\_FECEP\_ST\_DEV\_ENT\_MP

“Valor FECEP\-ST Calculado para Devolução” recuperado no 3º Passo;

Valor FECEP\-ST \(Devolução Entrada\)

__Saldo Final do Dia__

Qtde total Convertida Final

QTD\_CONV\_FIM

QTD\_CONV\_INI \+ QTD\_CONV\_ENT\_MP \- QTD\_CONV\_DEV\_ENT\_MP

Qtde Final

Valor do ICMS Calculado Final

VLR\_ICMS\_FIM\_MP

VLR\_ICMS\_INI\_MP \+ VLR\_ICMS\_ENT\_MP \- VLR\_ICMS\_DEV\_ENT\_MP

Valor ICMS Final

Valor do ICMS\-ST Calculado Final

VLR\_ICMS\_ST\_FIM\_MP

VLR\_ICMS\_ST\_INI\_MP \+ VLR\_ICMS\_ST\_ENT\_MP \- VLR\_ICMS\_ST\_DEV\_ENT\_MP

Valor ICMS\-ST Final

Valor Base de Cálculo do ICMS\-ST Calculado Final

VLR\_BC\_ST\_FIM\_MP

VLR\_BC\_ST\_INI\_MP \+ VLR\_BC\_ST\_ENT\_MP \- VLR\_BC\_ST\_DEV\_ENT\_MP

Valor Base de Cálculo do ICMS\-ST Final

Valor FECEP\-ST Calculado Final

VLR\_FECEP\_ST\_FIM\_MP

VLR\_FECEP\_ST\_INI\_MP \+ VLR\_FECEP\_ST\_ENT\_MP \- VLR\_FECEP\_ST\_DEV\_ENT\_MP

Valor FECEP\-ST Final

__Valores Médios Unitários Calculados do Dia__

Valor Médio Unitário do ICMS

VLR\_UNIT\_ICMS\_FIM\_MP

VLR\_ICMS\_FIM\_MP / QTD\_CONV\_FIM\_MP

Valor Médio Unitário ICMS

Valor Médio Unitário do ICMS\-ST s/ FECEP 

VLR\_UNIT\_ICMS\_ST\_FIM\_MP

VLR\_ICMS\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP

Valor Médio Unitário ICMS\-ST s/ FECEP

Valor Médio Unitário do ICMS\-ST c/ FECEP

VLR\_UNIT\_ICMS\_ST\_FECEP\_FIM\_MP

\(VLR\_ICMS\_ST\_FIM\_MP \+ VLR\_FECEP\_ST\_FIM\_MP\) / QTD\_CONV\_FIM\_MP

Valor Médio Unitário ICMS\-ST c/ FECEP

Valor Médio Unitário da Base de Cálculo do ICMS\-ST

VLR\_UNIT\_BC\_ST\_FIM\_MP

VLR\_BC\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP

Valor Médio Unitário Base de Cálculo do ICMS\-ST

Valor Médio Unitário do FECEP\-ST

VLR\_UNIT\_FECEP\_ST\_FIM\_MP

VLR\_FECEP\_ST\_FIM\_MP / QTD\_CONV\_FIM\_MP

Valor Médio Unitário FECEP\-ST

\[MFS511653\]: Criação do parâmetro “Gerar Relatórios de Conferência” na tela da pré\-geração:

Caso o parâmetro “Gerar Relatórios de Conferência” da tela de pré\-geração seja marcado, gerar um arquivo excel a partir da leitura da tabela __EST\_ST\_MG\_MEDIA\_POND__

Nome do arquivo: Relatório\_Conferencia\_Calculo\_Media\_Ponderada\_mm\_aaaa\_cod\_estab\.csv

MFS\-67654

MFS\-73772

MFS\-74069

MFS\-74991

MFS\-82924

MFS\-977849

RP00B

Safx52

Gravação dos registros na tabela SAFX52 para produtos com movimentação de nota e sem registro de inventário

__Campo X52\_INVENT\_PRODUTO__

__Regra de Preenchimento__

01

Código da Empresa

COD\_EMPRESA

código da empresa do login;

02

Código do Estabelecimento

COD\_ESTAB

código do estabelecimento selecionado para geração;

03

Data do Inventário

DATA\_INVENTARIO

Dia __*imediatamente anterior*__ ao primeiro dia do Período \(Mês/Ano\) informado na Tela de Geração

04

Grupo de Contagem

GRUPO\_CONTAGEM

Preencher com “1”

05

Código de Classificação Fiscal \- NBM

COD\_NBM

Não preencher

06

Indicador do Produto

IND\_PRODUTO

Indicador do Produto 

07

Produto

COD\_PRODUTO

Código do Produto 

08

Unidade Padrão

COD\_UND\_PADRAO

Código de Unidade Padrão do Produto \(campo 20 da SAFX2013\)

09

Almoxarifado

COD\_ALMOX

Não preencher

10

Centro de Custo

COD\_CUSTO

Não preencher

11

Natureza de Estoque

COD\_NAT\_ESTOQUE

Campo “Natureza de Estoque”  informado na Tela de Geração

12

Unidade de Medida

COD\_MEDIDA

Código de Unidade de Medida do Produto  \(campo 14 da SAFX2013\)

13

Quantidade de Inventário

QUANTIDADE

Preencher com zero\.

14

Custo Total

VLR\_TOT

Preencher com zero\.

15

Custo Unitário

VLR\_UNIT

Preencher com zero\.

16

Observação

OBSERVACAO

Não preencher

17

Valor do ICMS

VLR\_ICMS

Preencher com zero\.

18

Código Conta Contábil

COD\_CONTA

__\[MFS86641\] __

Campo “Conta Contábil” informada na Tela de Geração

19

Débito/Crédito

IND\_DEB\_CRE

Não preencher

20

Discriminação

DESCRICAO\_RIPI

Não preencher

21

Valor de ICMS Médio

VLR\_ICMS\_MEDIO

Preencher com zero\.

22

Valor de ICMS\-ST Médio

VLR\_ICMSS\_MEDIO

Preencher com zero\.

23

Inscrição Estadual

INSC\_ESTADUAL

Não preencher

24

Indicador de Pessoa Física/Jurídica

IND\_FIS\_JUR

Não preencher

25

Código de Pessoa Física/Jurídica

COD\_FIS\_JUR

Não preencher

26

Base ICMS

VLR\_BASE\_ICMS

Preencher com zero\.

27

Base Isenta ICMS

VLR\_BASE\_ISENTO

Preencher com zero\.

28

Base Outras de ICMS

VLR\_BASE\_OUTRAS

Preencher com zero\.

29

Base de ICMS\-S

VLR\_BASE\_ICMSS

Preencher com zero\.

30

Código da Observação

COD\_OBSERVACAO

Não preencher

31

Vlr do Custo SAICS

VLR\_CUSTO\_DCA

Preencher com zero\.

32

Indicador do Produto para Rastreabilidade

IND\_PRODUTO\_RASTRO

Não preencher

33

Código do Produto para Rastreabilidade

COD\_PRODUTO\_RASTRO

Não preencher

34

Valor do IPI

VLR\_IPI

Preencher com zero\.

35

Valor do PIS

VLR\_PIS

Preencher com zero\.

36

Valor da COFINS

VLR\_COFINS

Preencher com zero\.

37

Valor de Outros Tributos Não\-Cumulativos

VLR\_TRIB\_NC

Preencher com zero\.

38

Código Situação Tributária “A”

COD\_SITUACAO\_A

Não preencher

39

Código Situação Tributária “B”

COD\_SITUACAO\_B

Não preencher

__40__

__Motivo do Inventário__

__IND\_MOT\_INV__

__Preencher com ‘06’ __

41

Situação Tributária

IND\_SIT\_TRIB

Não preencher

42

Valor Total para o IR

VLR\_IR

Preencher com zero\.

43

Valor Base ICMS\-ST Médio

VLR\_BASE\_ICMSS\_MEDIO

Preencher com zero\.

44

Valor FECEP Médio

VLR\_FCP\_MEDIO

Preencher com zero\.

45 

Indicador de Gravação

IND\_GRAVAÇÃO 

Preencher com ‘6’

MFS\-74991

MFS\-86641

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

