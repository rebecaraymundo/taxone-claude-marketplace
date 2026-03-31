# RNG-C_V45

- **Fonte:** RNG-C_V45.docx
- **Modificado:** 2026-03-11
- **Tamanho:** 212 KB

---

Quadro de Revisões

__                                                __

__Data__

__OS / Chamado__

__Descrição  __

__Responsável__

27/05/2020

MFS\-37412

RNC170\-08: Passar a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08, no preenchimento do campo 08 – VL\_DESC do C170\.

Liliane Assaf

14/12/2020

MFS\-48809

RNC191\-06: Passar a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08, no preenchimento do campo 06 – VL\_DESC do C191\.

RNC195\-06: Passar a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08, no preenchimento do campo 06 – VL\_DESC do C195\.

Alessandra Crisitna Navatta

15/03/2021

MFS\-58212

Alteração da regra do registro C110\.  Inclusão do tratamento para usuários que não têm que gerar o registro C110, mas precisam gerar o registro C111\. Foi definido um parâmetro no cadastro da observação para indicar quando a observação não deve ser gerada no registro C110, ou seja, o registro C110 não deve ser gerado\.

Andréa Rocha

14/04/2021

MFS63121

### Ajuste na regra do campo 07 do registro C100<a id="_Toc20813652"></a>, para cenários de documentos com modelo ‘55’ ou ‘65’\.

Alessandra Cristina Navatta

14/04/2021

MFS66994

### Ajuste na regra do campo 07 do registro C100, para cenários de documentos com modelo ‘55’ ou ‘65’\.\( Este campo deve ser gerado com ‘000’, mas caso seja menor do que o esperado preencher com zeros à esquerda\)\.

Rogério Ohashi

22/09/2021

MFS73007

### Correção na geração dos Registros C100, Campo 16 e C170, Campo 07, de acordo com o manual da EFD\-PIS/COFINS, nos casos em que o informante não tenha direito ao crédito, os valores de ICMS/ST e/ou IPI devem ser adicionados \(somados\) ao valor das mercadorias\. \(Equiparação de Regra alterada na EFD ICMS/IPI\)\.

Rogério Ohashi

28/03/2022

MFS82775

### Alteração da regra do registro C100 para utilizar o novo parâmetro “Considerar Notas Fiscais de Saídas Canceladas – Modelo 55” para considerar na geração, se marcado, as Notas Fiscais canceladas de Saídas \(Modelo 55\)

Rogério Ohashi

14/04/2022

MFS84537

### Inclusão do Campo de CHV\_NFE do registro C100 para Notas Fiscais Canceladas, modelo 55\.

Rogério Ohashi

29/04/2022

MFS83273

### Inclusão de tratamento para o Campo 21 \- COD\_ENQ do registro C170, para não ser preenchido se o Campo 174 \- COD\_ENQUAD\_IPI da tabela SAFX08 estiver vazio\.

Rogério Ohashi

17/05/2022

MFS84559

### Alteração da regra de geração dos registros C100/C170 e C190 e filhos \(RNG\-C190\) para utilizar o novo parâmetro “*Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas*” para GERAR, se marcado, as Notas Fiscais de Devolução de Compras, __*Posterior*__ a Data de Escrituração da Nota Fiscal de Entrada\. 

Rogério Ohashi

07/07/2022

MFS89495

Correção na geração dos Registros C100 \(campo 16\) e C170 \(campo 07\), de acordo com o manual da EFD\-ICMS/IPI somente para notas fiscais de entrada, nos casos em que o informante não tenha direito ao crédito, os valores de ICMS/ST e/ou IPI devem ser adicionados \(somados\) ao valor das mercadorias\.  Para notas fiscais de saída será utilizada a forma de gerar anterior à alteração da MFS73007\.

Andréa Rocha

10/11/2022

MFS96955

Alteração na geração dos Registros C100 \(campo 16\) e C170 \(campo 07\), para recuperar a informação do Campo 145 \- VLR\_ICMSS\_N\_ESCRIT da tabela SAFX08, nos casos em que o informante não tenha direito ao crédito, os valores de ICMS/ST e/ou IPI devem ser adicionados \(somados\) ao valor das mercadorias\. 

Rogério Ohashi

12/06/2023

MFS536991

Readequação da Regra de geração do Registro C170 \(campo 08 – VL\_DESC e campo 15 – VL\_ICMS\) para considerar o parâmetro “*Gerar Valor de Exclusão no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159*”\.

Rogério Ohashi

19/12/2023

MFS\-596091

Objetivo desse documento é tratar o campo 12 COD\_NAT, do Registro C170 \(Complemento do Documento \- Itens do Documento\), referenciado no \(campo 02 do Registro 0400 da Tabela de Natureza da Operação/Prestação\)\.

Rosemeire Santos

14/06/2024

MFS\-642118

Alteração na regra de geração do campo 07 \- EX\_IPI dos registros C180 e C190\. Será considerada a informação do campo 09\-EX\_IPI da SAFX2043, quando este estiver preenchido\.

Alessandra Navatta

21/08/2024

MFS\-671016

Este documento, tem o objetivo de readequar regras nos campos 8 e 15 do registro C170\.

Denilson André Santos

09/03/2026

MFS\-1064883

Registro C170: esclarecimento sobre a necessidade de preencher o campo “base de cálculo” do PIS e da COFINS, mesmo em caso de alíquota zero\.

Lyene Benvenutti

09/03/2026

MFS\-1063329

Alteração das regras dos campos 28\-VL\_PIS\_ST e 29\-VL\_COFINS\_ST do regsitro C100 para retirar a utilização do Código da Situação Tributária PIS e COFINS, para utilizar somente Código da Situação Tributária PIS\-ST e COFINS\-ST\.  Essa alteração foi alinhada com a Rose, os campos de valores referentes ao ST, só vão utilizar os campos específicos de ST da nota fiscal\.

Andréa Rocha

__LEGENDA: ALTERADO NO Sprint\_Correcoes\_Pos\_PVA__

__Regras de Recuperação para os registros do bloco C:__

__Registro C001 – Abertura do Bloco__

__RNG\-C001__

Deve ser gerado um registro por arquivo\.

__RNC100\-02__

Campo IND\_MOV:

Gravar "0" se existir movimentação a ser gerada no bloco C no período informado na tela de geração, senão gravar ‘’1’’\.

__Registro C010 – Identificação do Estabelecimento__

__RNG\-C010__

CH27235/2013

Gerar um registro C010 para cada CNPJ de estabelecimento que possua movimentação nos registros do bloco C\.

As movimentações do bloco C devem ser geradas imediatamente abaixo do registro C010 do CNPJ do estabelecimento correspondente\.

\* *Foi incluída observação para gerar por CNPJ do estabelecimento por conta de situações onde a empresa tem mais de um estabelecimento com o mesmo CNPJ\. Neste caso, deve ser gerado apenas um A010 por CNPJ e as movimentações serão vinculadas abaixo do CNPJ\.*

__RNC010\-03__

Campo IND\_ESCRI:

Verificar o parâmetro “Indicador da apuração, na escrituração das operações por NF\-e e ECF”, informado na tela de Dados Iniciais:

Se indicador = Apuração com base nos registros de consolidação das operações por NF\-e \(C180 e C190\) e por ECF \(C490\);

      Gravar “1”

Senão      

      Gravar “2” \(Apuração com base no registro individualizado de NF\-e \(C100 e C170\) e de ECF \(C400\)\.

__ __

__Registro C100 – Notas Fiscais \(Códigos 01, 1B, 04, 55 e 65\)__

__RNG\-C100__

Deve ser gerado um registro C100 para cada documento fiscal \(SAFX07\) que atenda aos critérios abaixo:

__Notas com item:__

__Regra Geral:__

- Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

Igual a “1 – Mercadoria” ou “3 – Mercadoria/Serviço”;

Se o parâmetro __Notas Fiscais de Mercadoria Não Escrituradas__ estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação “7 – Notas Fiscais de Mercadoria não Escrituradas” e que possuam CSTs de PIS e COFINS \(SAFX07 ou SAFX08\) informados\.

- Indicador da Escrituração \(NF\-e e ECF\): \(parâmetro nos dados iniciais da obrigação\)

SE for igual “1 – Apuração com base nos registros consolidados\.\.\.”, considerar NFs cujo Modelo \(campo “13 – Modelo de Documento” da SAFX07\) seja igual a “01”, “1B”, “04” ou 65, sendo que o modelo 65 será considerado __apenas se__ no cadastro do Perfil \(menu: Parâmetros >> Perfil\) o registro C175 __estiver__ selecionado \(OS4474\)

SENÃO, se for igual a “2 – Apuração com base nos registros individualizados\.\.\.”, considerar NFs cujo Modelo \(campo “13 – Modelo de Documento” da SAFX07\) seja igual a “01”, “1B”, “04”, “55” ou 65, sendo que o modelo 65 será considerado __apenas se__ no cadastro do Perfil \(menu: Parâmetros >> Perfil\) o registro C175 __estiver__ selecionado \(OS4474\)

- Campo Crédito/Contribuição Extemporânea \(campo novo da SAFX08/SAFX09\) preenchido com conteúdo igual a “N”, 	Item não extemporâneo\.

__Obs\.:__ Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal \(SAFX08\), considerar o conteúdo desses campos informados na capa do documento \(SAFX07\)\.

- Notas do tipo “Normal” \(campo 04 da SAFX07 = “1 – Normal”\) e, SE for uma “Devolução” \(campo 04 da SAFX07 = “2 – Devolução”\), considerar apenas NFs cujo CFOP \(ou CFOP\+Natureza\) \(campos 22 e 23 da SAFX08/17 e 18 da SAFX09\) estejam relacionados no parâmetro “CFOP x Tipo de Operação” com tipo de operação igual a “Devolução de Venda” ou “Devolução de Compra”\.
- Não serão consideradas NFs sem item\.

\[MFS29621\]

- Não serão consideradas NFs que serão geradas no registro C600, ou seja, as notas que estão parametrizadas para a geração do registro C600 \(Parâmetros à Registro C600 à Por CFOP e Parâmetros à Registro C600 à Por Extensão CFOP\.
- Para um Documento Fiscal de Entrada \(Campo MOVTO\_E\_S <> 9\), além das regras gerais, considerar:

__\[ALTERAÇÃO – CH28382 / CH6594/2015 / CH12871/2015 / OS4816\]__

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.*  
*

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

- __SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS ou CST COFINS \(campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\.

\[__MFS\-1876__\] Além dos CSTs indicados acima, considerar também registros cujo CST PIS ou CST COFINS sejam iguais a “98” ou “99”, desde que o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) esteja parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\)\.

Se o parâmetro for igual a “Sim”, considerar todos os CSTs\.

- Para um Documento Fiscal de Saída \(Campo MOVTO\_E\_S = 9\), além das regras gerais, considerar:

Observar o parâmetro Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de Receita disponível na tela de Dados Iniciais\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Lançamento EFD PIS/COFINS’’__, o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08 ou campo 81 \- DAT\_LANC\_PIS\_COFINS da SAFX09\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Emissão”, o campo Data da Emissão__ \(campo 11 \- DATA\_EMISSAO da SAFX07\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

*Obs\. A Data de Lançamento PIS/COFINS poderá ser menor do que a Data de Emissão, está prevista legalmente esta situação\.*

__*Atenção: *__*O parâmetro “Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de receita” é somente para documentos/operações de saídas, para documento/operações de entradas serão selecionados pela data do PIS e COFINS independentemente deste parâmetro\.*

- Considerar apenas NFs de saída cujo CFOP \(ou CFOP\+Natureza\) \(campos 22 e 23 da SAFX08/17 e 18 da SAFX09\) esteja relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de operação igual a “Geradora de Receita”\.

===///===

__\[ALTERADA – CH27507\_2015\]__

__Tratamentos para notas canceladas:__

- Quando se tratar de NF Cancelada \(campo “30 – Situação da nota = “S”\) somente poderá ser informado os campos IND\_OPER, IND\_EMIT, COD\_MOD, COD\_SIT, SER e NUM\_DOC do registro\.

\[__ALTERAÇÃO\- MFS82775__\] Tratamento na regra para considerar o novo parâmetro ‘__*Considerar Notas Fiscais de Saídas Canceladas – Modelo 55*__’\.

\[__ALTERAÇÃO\- MFS84537__\] Inclusão do Campo de “CHV\_NFE” para as __*Notas Fiscais de Saídas Canceladas – Modelo 55*__’\.

__Parâmetro Desmarcado:__ Se o parâmetro na tela de Dados Iniciais “__*Considerar Notas Fiscais de Saídas Canceladas – Modelo 55*__”, estiver __*desmarcado*__, o sistema deverá seguir conforme a regra original:

- Quando se tratar de Notas Fiscais Eletrônicas \(modelo 55\) Canceladas \(Campo 30 – Situação da Nota = “S” \) estas não deverão ser geradas no arquivo\.
- Não deverão ser informados registros filhos\. 

__Parâmetro Marcado:__ Se o parâmetro na tela de Dados Iniciais “__*Considerar Notas Fiscais de Saídas Canceladas – Modelo 55*__”, estiver __*marcado*__ o sistema deverá considerar na geração as Notas Fiscais \(Modelo 55\), seguindo a regra abaixo:

- Quando se tratar de NF Cancelada \(campo “30 – Situação da nota = “S”\) somente poderá ser informado os campos IND\_OPER, IND\_EMIT, COD\_MOD, COD\_SIT, SER, NUM\_DOC e CHV\_NFE do registro\.
- Não deverão ser informados registros filhos\. 

__Tratamentos para Notas Complementares de Saída:__

Quando se tratar de NF complementar \(campo 125 da SAFX07 igual a “5 \- NF Complementar ou CT\-e de Complemento de Valores”\) de saída, somente deverá ser considerado o documento que possuir no campo “23 – Valor Total do Documento Fiscal” ou “68 – Valor Total Serviços” valor maior que zero\.

\[__OS4316\-A__\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__Atenção:__

Movimento Consolidado da SAFX42/SAFX43 com Modelo = “01”:

- Os documentos da SAFX07 referentes ao movimento consolidado das notas de Utilities \(SAFX42/SAFX43\) *não devem ser considerados* para a geração do C100\. Embora as notas de Utilities tenham os seus modelos específicos \(06, 21, 22, 28 e 29\), este procedimento é necessário enquanto os modelos “28” e “29” ainda não foram oficialmente tratados no Convênio ICMS \(o cliente CEG por exemplo carrega as notas de gás na SAFX42 com modelo = “01”, pois o Convênio ICMS 115 não aceita modelo “28”\);  

Notas/Contas de Fornecimento de Gás \(Entradas\):

- As contas de fornecimento de Gás \(entradas\) emitidas pelas empresas concessionárias *não devem ser consideradas* para a geração do C100\. O motivo é o mesmo descrito acima, o problema do modelo “28” ainda não ter sido oficialmente tratado no Convênio ICMS\. Estas notas serão identificadas pela parametrização de Pessoas Fis/Jur x Ramo de Atividade, que deverá ser = “Fornecedores de Gás Canalizado”;

__Dúvidas: __

1\- Se existirem itens com CST’s diferentes \(um com crédito e um sem crédito\) devemos levar a 	 nota para o arquivo com seus valores totais ou apenas com os valores do item com crédito?

__*Resposta*__*: Será considerado o valor total da NF  *

2\- Quando a empresa opta pelo método de apropriação direta dos créditos \(contabilidade de 	 custos integrada\), a NF deve ser apresentada no registro C100 apenas quando houver de fato a apropriação do crédito referente àquela aquisição? Se sim, a NF será gerada no registro C100 em uma data diferente da data fiscal do documento \(data da apropriação do crédito\), mas não será considerada extemporânea?

__Resposta:* *__*No critério da apropriação direta,*__* *__*a empresa pode apresentar o documento fiscal apenas no mês em que efetivamente for se apropriar o crédito\. No caso dessa situação, o documento fiscal não será considerado como extemporâneo, devendo ser apresentado nos registros do bloco A C, D e F correspondente\.*

	 

3\- As devoluções não possuem tratamento especial:

3\.1\- Estamos considerando que quando houver devolução de venda, a NF de entrada será escriturada normalmente e o campo “Data de Lançamento PIS/COFINS” será preenchido \(mesmo a devolução não representando crédito, e sim abatimento da BC\)\. Está correto o entendimento?

__*Resposta:*__* Sim*\.

3\.2\- Deve haver algum tratamento para as devoluções de compras?

__*Respost*__*a:* *Devo levar as devoluções, mesmo que não tenham crédito\.*

4\- Existe nota fiscal complementar de PIS/COFINS?

__*Resposta*__*: Sim*

*Pendente:*

6\- Na aquisição para o ativo, devemos informar a NF mesmo que não haja crédito nenhum a ser apropriado?

8\- Existem notas com tratamento especial na geração desse registro? Por exemplo, nas operações de venda ambulante o contribuinte emite uma NF com o valor total das mercadorias que estão “indo para a rua”\. A cada venda que acontece, emite\-se uma NF com o valor específico daquela venda, então, teríamos duas notas para a mesma mercadoria\. A NF de saída da mercadoria do estabelecimento não deve ser levada para o arquivo porque não caracteriza receita?

Considerar a tabela de CFOP x receitas – Incluir parametrização para o cliente alterar a lista se necessário\.

__\[MFS84559\] __

__Tratamento para Notas de Devolução de Compras:__

__Parâmetro Marcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas*__”, estiver __*marcado*__ o sistema deverá gerar as informações do Registro C100 conforme regras atuais\.

__Parâmetro Desmarcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas”, *__estiver __des*marcado*__, o sistema deverá desconsiderar as Notas Fiscais de Devolução de Compras, com a data, __*posterior*__ a Nota Fiscal de Entrada, conforme regras abaixo:

- Campo *MOVTO\_E\_S* igual à ‘9’ *\(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- Campo *NORM\_DEV* igual à ‘2’ *\(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- *Campo COD\_SITUACAO\_PIS igual à ‘49’ \(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- Campo *DAT\_LANC\_PIS\_COFINS* ou *DATA\_EMISSAO* > ao Campo *DAT\_DI* \(Considerar Mês/Ano na comparação\)\. *\(DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\); \(Conforme parâmetro na tela de Dados Iniciais Data Emissão ou Data Lançamento PIS e COFINS\)\.*

  

__Obs\.:__ A Data de Lançamento EFD PIS/COFINS ou a Data de Emissão da Nota de Devolução de Compras deverá ser posterior a data de escrituração da Nota Fiscal de Entrada\. 

Exemplo de NF de Devolução de Compras que não deve ser considerada:

Nota fiscal de Devolução de Compra escriturada em __01/2022\.__  
Nota fiscal de Entrada escriturada em __12/2021\.__

__*Atenção: *__Nessas mesmas condições desconsiderar o Registro filho __*C170\.*__

Default: __Marcado__

__Importante:__ No caso da geração dos Registros C190 e filhos \(informações consolidadas\) o intuito é, se o parâmetro estiver *desmarcado*, serão desprezados __todos__ os registros filhos C191, C195, C198 e C199 *referente a NF de Devolução de Compras escriturada, posteriormente a NF de Entrada*, ou seja, as demais Notas serão geradas normalmente, __*exceto*__ se na consolidação do Registro C190 __*houver somente*__ Notas de Devolução de Compras \(data Posterior\), nesse caso o Registro C190 também deverá ser desprezado\.

__RNC100\-02__

Campo IND\_OPER:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se indicador de movimento E/S = 9 à gravar 1 \(Saída\)

Se indicador de movimento E/S <> 9 à gravar 0 \(Entrada\)

__RNC100\-03__

Campo IND\_EMIT:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se indicador de movimento E/S = 1 à gravar 1 \(emissão terceiros\)

Se indicador de movimento E/S = 2,3,4,5,9 à gravar 0 \(emissão própria\)

Se indicador de movimento E/S = 9 e campo “Nota Fiscal de Venda Emitida por Terceiro” selecionado à gravar 1 \(emissão terceiros\) 

__RNC100\-04__

Campo COD\_PART:

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

\[OS4751\] 

Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__RNC100\-05__

Campo COD\_MOD:

Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

__RNC100\-06__

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica, verificar:

     se a nota é avulsa               à gravar “08” \[MFS25010\]

     se a nota foi denegada        à gravar “04”

     se a nota foi  ou inutilizada  à gravar “05”

Se for nota cancelada,

      gravar “02”

Se for nota complementar:

      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc\.\.\.

      gravar “08”

Se a nota não atende a nenhuma das opções anteriores:

      gravar “00”

Pendente:

Dúvida: Será considerada a nota fiscal cancelada, inutilizada e denegada no arquivo?  Perguntar para o Jonathan na reunião\!

__Importante:__ 

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”

A lógica seria a seguinte:

__Se__ nota é eletrônica e foi  \(denegada ou inutilizada ou avulsa\)

        __Se__ nota é avulsa 

              gravar “08”

        __Senão Se__ nota é denegada

              gravar “04”

        __Senão__*  \(é inutilizada\)*

              gravar “05”

# Senão

        __Se__ nota é cancelada

              gravar “02”

              __Senão__

                    __Se__ nota é complementar

                         gravar “06”

                    __Senão__

                         __Se__ nota tem Ato Normativo, Regime Especial etc

                              gravar “08”

                         __Senão__

                             gravar “00”;

  

__Campos da SAFX07 para verificação das regras:__

Nota cancelada à campo “30\-Situação da nota” =  “S”;

Nota complementar à campo “125\-Situação Especial” = “5”;

Nota Eletrônica à campo “13\-Modelo de Documento” =  “57”;

Nota Eletrônica denegada à campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “1” \(denegada\);

Nota Eletrônica inutilizada à campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “2” \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc à o campo “232\-NF Baseada em Regime Especial ou Norma Específica” será = “S”\.

Nota avulsa à campo “13\-Modelo de Documento” = \(“55” ou “65”\) e campo “09\- Série do Documento Fiscal” = “890” a “899” \(890, 891, 892\.\.\.899\);

__RNC100\-07__

Campo SER:

 Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

__\[ALTERAÇÃO\-MFS6312\-MFS66994\] __

Este campo é de preenchimento obrigatório, quando modelo = ‘55’ ou ‘65’ \(campo 13\-modelo de documento da SAFX07\)\. Neste cenário, se o campo 09 – série do documento da SAFX07 estiver sem preenchimento, este campo deve ser gerado com ‘000’, mas caso seja menor do que o esperado preencher com zeros à esquerda\. 

__RNC100\-08__

Campo NUM\_DOC: 

Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

__RNC100\-09__

Campo CHV\_NFE:

Este campo será preenchido com a chave da nota fiscal eletrônica \(campo 226 da SAFX07\)\. Preencher apenas quando se tratar de uma *nota eletrônica* de *emissão própria* e emitida por terceiros, ou seja, quando as seguintes condições foram verdadeiras: \(regra verificada no documento do GT\)

\- modelo = 55 ou 65 \(campo “13\-Modelo de Documento” da SAFX07\)

\- indicador de movimento E/S = 1,2,3,4,5,9 \(campo “03\-Movimento E/S” da SAFX07\)

Nos demais casos, o campo não deverá ser preenchido\.

Regra de preenchimento:

Se \(modelo = 55 ou 65\) *e* \(indicador de movto E/S = 1,2,3,4,5 ou 9\) 

       Se existir a informação na SAFX07 \(campo 226 <> nulo\)

             Preencher o campo com o conteúdo da chave \(utilizar as primeiras 44 posições, seguindo o formato da NF\-e nacional\) 

       Senão

             Gravar mensagem no log de erros, conforme padrão do Sped Fiscal:

Erro1:

Se IND\_EMIT = 0 \(Emissão Própria\): 

O campo CHV\_NFE é de preenchimento obrigatório, e não foi informado

Origem: Campo Chave de Acesso da NF\-e do Documento Fiscal \(SAFX07\)

Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur

Aviso:

Para as gerações até 31/03/2012 emitir a msg abaixo:

Se IND\_EMIT = 1 \(Emissão de terceiros\): 

O campo CHV\_NFE será de preenchimento obrigatório, para as notas eletrônicas emitidas por terceiro, a partir de abril de 2012\.

Origem: Campo Chave de Acesso da NF\-e do Documento Fiscal \(SAFX07\)

Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur

Para as gerações a partir de 01/04/2012

Se IND\_EMIT = 0 ou 1

O campo CHV\_NFE é de preenchimento obrigatório, e não foi informado

Origem: Campo Chave de Acesso da NF\-e do Documento Fiscal \(SAFX07\)

Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur

            Esta é a mensagem de número 32 da planilha de erros Sped\_Fiscal\_Log\_Erros

Senão

        o campo não deverá ser preenchido    ,

Para notas canceladas este campo não deverá ser informado\. 

__RNC100\-10__

Campo DT\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-11__

Campo DT\_E\_S:

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-12__

Campo VL\_DOC:

Somatório do campo “23\-Valor Total da Nota” com o campo “68\-Valor Total Serviços” da SAFX07\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-13__

Campo IND\_PGTO:

A partir do conteúdo do tipo de faturamento \(campo 99\-Tipo de Faturamento da SAFX07\), verificar:

Se tipo faturamento = 1 \(a vista\)               à   gravar  “0”

Se tipo faturamento = 2 \(a prazo\)              à   gravar  “1”

Se tipo faturamento = 3 \(sem pagamento\) à   gravar  “9”

Para notas canceladas este campo não deverá ser informado\.

A partir de 01/Julho/2012, na geração do SPED PIS/COFINS deverá ser considerado a seguinte regra: 

A partir do conteúdo do tipo de faturamento \(campo 99\-Tipo de Faturamento da SAFX07\), verificar:

Se tipo faturamento = 1 \(a vista\)            à   gravar  “0”

Se tipo faturamento = 2 \(a prazo\)            à   gravar  “1”

Se tipo faturamento = 3 \(sem pagamento\) à   gravar “2”

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-14__

Campo VL\_DESC:

Para as notas *sem* itens à o campo deve ser preenchido com o valor do desconto da SAFX07 \(campo 28\-Valor Descontos\);

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-15__

Campo VL\_ABAT\_NT:

Preencher com o campo 233\- Valor do Abatimento não tributado da SAFX07\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-16__

Campo VL\_MERC:

\[__ALTERAÇÃO\- MFS73007 / MFS89495 / MFS96955__\] Tratamento quando houver IPI e/ou ICMS\-ST sem direito ao crédito, somente para notas fiscais de entrada\. Alteração para considerar o Campo 145\- VLR\_ICMSS\_N\_ESCRIT \(ICMS\-ST Não Escriturado\)\.

__Tratamento para notas fiscais de entrada:__

Para notas de Mercadorias à neste caso deve\-se totalizar todos os itens de mercadoria da nota, preencher considerando a somatória dos campos abaixo:

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “145\- VLR\_ICMSS\_N\_ESCRIT”  da  Tabela SAFX08

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “133\- VLR\_ICMSS\_NDESTAC”  da  Tabela SAFX08

Para as notas Mistas Mercadoria/Serviço à neste caso deve\-se totalizar todos os itens de mercadoria e serviço da nota, preencher considerando a somatória dos campos abaixo:

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “145\- VLR\_ICMSS\_N\_ESCRIT”  da  Tabela SAFX08 \+ Campo 14\- VLR\_SERVICO da tabela SAFX09\.

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “133\- VLR\_ICMSS\_NDESTAC”  da  Tabela SAFX08 \+ Campo 14\- VLR\_SERVICO da tabela SAFX09\.

__Tratamento para notas fiscais de saída:__

Para notas de Mercadorias à o campo deve ser preenchido com o Valor dos Produtos e Serviços da SAFX07 \(Campo 28\-Valor do Item\);

Para notas Mistas Mercadoria/Serviço à neste caso deve\-se totalizar o valor do item de todos os itens de mercadoria e serviço da nota, considerando o campo “28\- Preço do Item” da SAFX08 e “14\- Valor Serviço” da SAFX09\.

Aplicar a mesma regra descrita para o campo 14\-VL\_ DESC, considerando os campos do valor do produto ou serviço indicados na <a id="_Hlk41475187"></a>planilha de\-para\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-17__

Campo IND\_FRT

Preencher com a informação do Campo 72\-IND\_TP\_FRETE da SAFX07, caso o campo seja igual a “vazio” preencher com “9” \(Sem frete\)

A partir de 01/Janeiro/2012, na geração do SPED PIS/COFINS deverá ser considerado a seguinte regra:

 	

__*MFS13627*__*: Alterada regra de geração do IND\_FRT devido à alteração do campo “72\-Indicador do Tipo de Frete” da SAFX07, p/atendimento ao Ato Cotepe 48/2017 \(alteração da EFD\)\.*

Se campo 72 da SAFX07 for igual “1\-Frete para Conta do Emitente \(CIF\)”

                                                      ou = “3\-Transporte Próprio por conta do Remetente”,

      Preencher o campo com “0” \(Por conta do emitente\);

Se o campo 72 da SAFX07 for igual “2\-Frete para Conta do Destinatário \(FOB\)”

                                                       ou “4\-Transporte Próprio por conta do Destinatário”, 

     Preencher o campo com “1”\(Por conta do destinatário/remetente\);

Se o campo 72 da SAFX07 for igual “0\-Outros”,

     Preencher o campo com 2 \(Por conta de terceiros\)

Se o campo 72 da SAFX07 for igual “vazio”, 

     Preencher o campo com “9” \(Sem frete\)\.

A partir de 01/Outubro/2017, na geração do SPED PIS/COFINS deverá ser considerado a seguinte regra:

__*MFS\-22693*__*: Atendimento à versão 1\.28 do Guia Prático da EFD – Contribuições\.*

Se campo 72 da SAFX07 for igual “1\-Frete para Conta do Emitente \(CIF\)”

      Preencher o campo com “0” \(Por conta do emitente\);

Se o campo 72 da SAFX07 for igual “2\-Frete para Conta do Destinatário \(FOB\)”

     Preencher o campo com “1”\(Por conta do destinatário/remetente\);

Se o campo 72 da SAFX07 for igual “0\-Outros”,

     Preencher o campo com 2 \(Por conta de terceiros\)

Se o campo 72 da SAFX07 for igual “3\-Transporte Próprio por conta do Remetente”,

     Preencher o campo com 3 \(Por conta do remetente\)

Se o campo 72 da SAFX07 for igual “4\-Transporte Próprio por conta do Destinatário”,

     Preencher o campo com 4 \(Por conta do destinatário\)

Se o campo 72 da SAFX07 for igual “vazio”, 

     Preencher o campo com “9” \(Sem frete\)\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-18__

Campo VL\_FRT:

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-19__

Campo VL\_SEG:

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-20__

Campo VL\_OUT\_DA:

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-21__

Campo VL\_BC\_ICMS :

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo do ICMS da SAFX07 \(campo 51\-Base ICMS\);

Para as notas *com *itens à neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08, sempre que o código de tributação indicar operação tributada \(campo 55 da SAFX08\);

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-22__

Campo VL\_ICMS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do ICMS \(conforme a planilha de\-para\)\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-23__

Campo VL\_BC\_ST:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor da base de cálculo do ICMS\-ST \(conforme a planilha de\-para\)\.

Importante: quando o indicador de ST *não* estiver marcado, o valor *não* deverá ser lançado neste campo, ou seja, para que o valor do ICMS\-ST seja gravado neste campo é necessário que a coluna IND\_CRED\_ICMSS seja = “S”;

O objetivo desta regra é seguir a forma de escrituração da nota, e lançar o valor apenas quando o valor for realmente lançado na apuração do ICMS\-ST \(a apuração do ST só considera as notas que tenham o indicador marcado\)\.

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

__RNC100\-24__

Campo VL\_ICMS\_ST:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do ICMS\-ST \(conforme a planilha de\-para\)\.

Importante: quando o indicador de ST *não* estiver marcado, o valor *não* deverá ser lançado neste campo, ou seja, para que o valor do ICMS\-ST seja gravado neste campo é necessário que a coluna IND\_CRED\_ICMSS seja = “S”;

O objetivo desta regra é seguir a forma de escrituração da nota, e lançar o valor apenas quando o valor for realmente lançado na apuração do ICMS\-ST \(a apuração do ST só considera as notas que tenham o indicador marcado\)\.

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

__RNC100\-25__

Campo VL\_IPI:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do IPI \(conforme a planilha de\-para\)\.

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

__RNC100\-26__

Campo VL\_PIS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do PIS \(conforme a planilha de\-para\)\.

No caso do PIS, ao totalizar os itens deve\-se considerar também os itens de serviço da SAFX09\.

\[__MFS\-1876__\] Não deve ser considerado neste o Valor do PIS dos itens que tenham o CST PIS \(campo 175 da SAFX08\) igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\)\.

\[__CH24846/2014__\] Para registros cujo modelo do documento seja igual a 65 \(NFC\-e\), serão totalizados apenas os valores de PIS \(conforme planilha de\-para\) dos registros que o CST de PIS for diferente de “05” ou “75”\. Quando for igual a “05” ou “75”, este campo não deverá ser informado\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-27__

Campo VL\_COFINS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor da COFINS \(conforme a planilha de\-para\)\.

No caso da COFINS, ao totalizar os itens deve\-se considerar também os itens de serviço da SAFX09\.

\[__MFS\-1876__\] Não deve ser considerado neste o Valor da COFINS dos itens que tenham o CST COFINS \(campo 178 da SAFX08\) igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\)\.

\[__CH24846/2014__\] Para registros cujo modelo do documento seja igual a 65 \(NFC\-e\), serão totalizados apenas os valores de COFINS \(conforme planilha de\-para\) dos registros que o CST de COFINS for diferente de “05” ou “75”\. Quando for igual a “05” ou “75”, este campo não deverá ser informado\.

Para notas canceladas este campo não deverá ser informado\.

__RNC100\-28__

Campo VL\_PIS\_ST:

__\[MFS1063329\] __Retirar a utilização__ __do__ __Código da Situação Tributária PIS, para utilizar somente Código da Situação Tributária PIS\-ST

Para as notas *sem* itens à o campo deve ser preenchido com o Valor Tributo PIS ST da SAFX07 \(campo 157\- VLR\_PIS\_ST\)\. Caso esse campo não esteja preenchido e o Código da Situação Tributária PIS \(249/SAFX07\) estiver preenchido com a opção “5, a informação deve ser recuperada do campo 103\- Valor PIS da SAFX07\. 

Para as notas *com *itens à neste caso deve\-se totalizar o Valor do PIS ST de todos os itens da nota, considerando o campo “122\- Valor Tributo PIS\-ST” da SAFX08, sempre que o código de tributação indicar operação tributada \(campo 55 da SAFX08\)\. Caso esse campo não esteja preenchido e o Código da Situação Tributária PIS \(175/SAFX08\) estiver preenchido com a opção “5, a informação deve ser recuperada do campo 87\-Valor PIS da SAFX08\.

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

__RNC100\-29__

Campo VL\_COFINS\_ST:

__\[MFS1063329\] __Retirar a utilização__ __do__ __Código da Situação Tributária COFINS, para utilizar somente Código da Situação Tributária COFINS\-ST

Para as notas *sem* itens à o campo deve ser preenchido com o Valor Tributo COFINS ST da SAFX07 \(campo 160\- VLR\_COFINS\_ST\)\. Caso esse campo não esteja preenchido e o Código da Situação Tributária COFINS \(campo 250 da SAFX07\) estiver igual a ‘’5’’, a informação deve ser recuperada do campo 105\- Valor COFINS da SAFX07\. 

Para as notas *com *itens à neste caso deve\-se totalizar o Valor Tributo COFINS\-ST de todos os itens da nota, considerando o campo “125\- VLR\_COFINS\_ST” da SAFX08, sempre que o código de tributação indicar operação tributada \(campo 55 da SAFX08\)\. Caso esse campo não esteja preenchido e o Código da Situação Tributária COFINS \(178/SAFX08\) estiver igual a ‘’5’’, a informação deve ser recuperada do campo 89\-Valor COFINS da SAFX08\.

\[__CH24846/2014__\] Para notas canceladas e para registros cujo modelo do documento seja igual a 65 \(NFC\-e\) este campo não deverá ser informado\.

__Registro C110 – Informações Complementares da NF__

__RNG\-C110__

Nesse registro devem ser gravados os registros da SAFX112 relacionados ao documento gerado no registro C100 que atendam aos critérios abaixo:

__\[ALTERADA – MFS3008\]__

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS” e “3 – Ambas as Obrigações”

Tipo de Observação: \(campo “13 – Tipo de Observação” da SAFX112\)

	Igual a “I \- Observação referente às Informações Complementares da Nota”

__\[ALTERADA – MFS58212\] Inclusão do tratamento para não gerar o Registro C110, de acordo com o campo Tipo de Observação do Cadastro da Observação__

Tipo de Observação: \(campo “04 – Tipo de Observação” da SAFX2009\) referente ao Código da Observação da SAFX112

	Diferente de “9 \- Não utilizar no registro C110 \(EFD\-Contribuições\)”

As informações de Observação constantes no campo 03 – TXT\_COMPL deverão ter um tamanho máximo de 255 caracteres\. Caso a informação a ser recuperada possua mais do que 255 caracteres, o restante da informação deve ser “truncado”\.

Dúvidas:

 Criar indicador para diferenciar os processos referenciados do ICMS/IPI dos processos do PIS/COFINS nos registros da SAFX114?

__Resposta__: Criação de um campo para indicar que a observação refere\-se ao EFD PIS/COFINS

__RNC110\-01__

Campo COD\_INF:

Se o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

Se o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

__Registro C111 – Processo Referenciado__

__RNG\-C111__

Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro C100, que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

Dúvidas: Criar indicador para diferenciar os processos referenciados do ICMS/IPI dos processos do PIS/COFINS nos registros da SAFX114?

__Resposta__: Criação de um campo para indicar que o processo refere\-se ao EFD PIS/COFINS 

__Registro C120 – Operações de Importação__

__RNG\-C120__

Neste registro deverão ser gravadas as informações de importação da SAFX49 associadas ao documento fiscal gravado no registro C100 que atendam ao critério abaixo:

Modelo: \(campo “13 – Modelo de Documento” da SAFX07\)

	Igual a “01”, “1B”, “04” ou “55”

Número do Item: \(campo 18 da SAFX08\)

	Igual ao número do item \(campo 13 da SAFX49\) da DI

__Obs\. 1: __Só devem ser considerados na geração desse registro os itens que tenham atendido à regra de geração das notas com item do registro C100\.

__Obs\. 2:__ Para cada nota fiscal podem existir “n” registros na SAFX49, já que as informações são discriminadas por DI e produto, então, o sistema deve agrupar os registros da SAFX49 por número de DI, totalizando os valores de PIS e COFINS, e gravar um registro para cada número de DI existente na X49\.

__Obs\.3:__ Para geração do Registro, C120, o Campo de IND\_PRODUTO e COD\_PRODUTO __não é__ considerado na associação com a SAFX08\.

__RNC120\-02__

Campo COD\_DOC\_IMP:

__*MFS\-25010*__*: Atendimento à versão 1\.29 do Guia Prático da EFD – Contribuições\.*

O código 2 \(Declaração Única de Importação\) só é válido para geração a partir de janeiro de 2019\. Antes desta data, o código não deve ser usado, ou seja, o registro não será gerado para o código 2\.

__RNC120\-03__

Campo NUM\_DOC\_IMP:

__*MFS\-22693*__*: Atendimento à versão 1\.28 do Guia Prático da EFD – Contribuições\.*

Esse campo passa a ter 15 posições e deve ser preenchido com o conteúdo do campo 04\-Número da DI da tabela SAFX49\.

__RNC120\-06__

Campo NUM\_ACDRAW:

\[Alteração – OS 3489\]

O número do Ato Concessório deverá ser concatenado com a Agência, Ano e Dígito do Ato Concessório: Campos 20\-AG\_ATO\_CONCES, 21\-ANO\_ATO\_CONCES, 22\-NUM\_ATO\_CONCES e 23\-DIG\_ATO\_CONCES da tabela SAFX49\.

Conforme critério: AG\_ATO\_CONCES||nvl\(ANO\_ATO\_CONCES,””\)||nvl\(NUM\_ATO\_CONCES,''\)||nvl\(DIG\_ATO\_CONCES,''\)

__Registro C170 – Itens do Documento \(Códigos 01, 1B, 04 e 55\)__

__RNG\-C170__

Gerar um registro para cada item da nota fiscal gravada no registro C100\. Nesse registro devem ser considerados tanto os itens de mercadoria \(SAFX08\), como os itens de serviço \(SAFX09\) das notas conjugadas:

Além de gerar um registro C170 para cada item que tenha atendido às regras de geração das notas com itens do registro C100, deve ser gerado também o registro C170 para todos os demais itens daquele documento fiscal, mesmo que esses outros itens não tenham atendido a regra de geração do registro C100\.

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

\[__OS4191__\]

Quando o campo Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST estiver preenchido e os critérios de geração do registro C170 forem atendidos, deverá ser gerado um registro C170 correspondente a cada item que tenha esta situação, com o objetivo de demonstrar os valores referentes à Substituição Tributária para que os mesmos sejam considerados na apuração\.

Exemplo: em uma nota há um item com CST de PIS igual a 01 e o CST de PIS ST igual a 05\. Neste caso, o item será gerado duas vezes, uma para demonstrar o valor da BC, Alíquota e Valor referente ao CST 01 e outro para demonstrar  a BC, Alíquota e Valor de ST, referente ao CST 05\.

__\[MFS\-1064883\]__

 

__Observação:__  
__ __Nas operações tributáveis, é obrigatório o preenchimento do campo "base de cálculo" do PIS e da COFINS, mesmo quando a alíquota for zero\. O preenchimento deste campo não é exigido nas operações isentas ou não tributadas\.

As regras de geração para demonstração da informação deste item criado para demonstrar os valores de ST serão definidas campo a campo\.

Esta situação irá ocorrer apenas para os documentos gerados a partir da SAFX08\.

		

__*Pendência: *__Incluir na regra geral a verificação do preenchimento do detalhe do documento \(campos de PIS/COFINS\)

Na planilha de\-para está definida a origem dos campos a partir das duas tabelas:

- SAFX08 quando se tratar de item de mercadoria
- SAFX09 quando se tratar de item de serviço \(no caso das notas mistas\)

*Dúvidas: *

*Se uma mesma NF possui item com crédito e item sem crédito, devo levar os dois itens para o arquivo*

__*Resposta*__*: Serão considerados todos os itens do documento fiscal, quando qualquer um dos itens for gerador de crédito, mas se o contribuinte não quiser relacionar os itens que não dão direito a crédito não terá problemas na validação, conforme o email do Jonathan*

__Ver Regra: RNG\-C100__ \(MFS84559 \- Regra de preenchimento NF de Devolução de Compras\)__ __

__RNC170\-02__

\[__OS4191__\] Campo NUM\_ITEM

Para geração da informação do Item que demonstra valores de ST, este campo será uma sequência criada a partir do último número de item \(NUM\_ITEM\) da tabela SAFX08\.

Exemplo: a NF tem 3 itens \(1, 2 e 3\), o primeiro item de ST criado será o 4\. Se houver mais de um item de ST, respeitará a sequência, seguindo para item 5 e 6\.

__RNC170\-03__

Campo COD\_ITEM:

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:

Gravar o código do produto \(SAFX2013\) ou do Bem \(SAFX13\), quando se tratar de item de mercadoria da SAFX08\. Gravar o código ou natureza do serviço \(SAFX2018\), quando se tratar de item de serviço da SAFX09 \(no caso de notas conjugadas\)\.

Aplicar a mesma regra de concatenação já definida no registro 0200: 

Produtos da SAFX2013 à Indicador de Produto \+ "\-" \+ Código do produto

Serviços da SAFX2018 à"S"  \+  "\-"  \+  Código ou Natureza do Serviço

Bens da SAFX13         à "B" \+ "\-" \+ Código do Bem \+ "I" \+ Código Incorporador

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:

Gravar o código do produto \(SAFX2013\) ou do Bem \(SAFX13\), quando se tratar de item de mercadoria da SAFX08\. Gravar o código ou natureza do serviço \(SAFX2018\), quando se tratar de item de serviço da SAFX09 \(no caso de notas conjugadas\)\.

Aplicar a mesma regra já definida no registro 0200: 

Produtos da SAFX2013 à Código do produto

Serviços da SAFX2018 à Código ou Natureza do Serviço

Bens da SAFX13         à  Código do Bem 

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-04__

DESCR\_COMPL

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Descrição Complementar \(DESCRICAO\_COMPL\) do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-05__

Campo QTD

Quando se tratar de uma NF Complementar = 5 \(NF Complementar ou CT\-e de Complemento de Valores \(modelo: 57\)\) \(125/SAFX07\) e o item da NF não possuir Quantidade informada \(24/SAFX08 ou 19/SAFX08\) o campo 05 do registro C170 deverá ser gerado nulo, ou seja, com ||\. 

Caso a situação não seja a descrita acima, o critério de geração atual com 0’s permanece\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Quantidade \(QUANTIDADE\) do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-06__

Campo UNID:

Quando se tratar de item de mercadoria \(SAFX08\) à preencher com a unidade de medida do item, campo “25\-Unidade de Medida” da SAFX08\.

Quando se tratar de item de serviço \(SAFX09\) da nota mista à deve\-se utilizar a unidade = “UN”\. Ao utilizar a unidade “UN” deve\-se ter o cuidado de pesquisar para verificar se já existe alguma unidade deste tipo registrada para o registro “0190\-Identificação das Unidades de Medida”\. Caso já exista alguma unidade identificada com a sigla “UN”, “Un” ou “un”, deve\-se utilizar a primeira encontrada\. Caso ainda não tenha sido identificada nenhuma unidade deste tipo, pode ser utilizada a sigla “UN”, e neste caso, deve\-se gravá\-la no registro 0190\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Unidade de Medida do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-07__

Campo VL\_ITEM:

\[__ALTERAÇÃO\- MFS73007 / MFS89495 / MFS96955__\] Tratamento quando houver IPI e/ou ICMS\-ST sem direito ao crédito, somente para notas fiscais de entrada\. Alteração para considerar o Campo 145 \- VLR\_ICMSS\_N\_ESCRIT  \(ICMS\-ST Não Escriturado\)\.

__Tratamento para notas fiscais de entrada de mercadoria:__

Quando se tratar de item de mercadoria \(SAFX08\) à neste caso deve\-se preencher considerando a somatória dos campos abaixo:

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “145\- VLR\_ICMSS\_N\_ESCRIT”  da  Tabela SAFX08

Campo “28\-VLR\_ITEM” __\+__ Campo” 81\-VLR\_IPI\_NDESTAC” __\+__ Campo “133\- VLR\_ICMSS\_NDESTAC”  da  Tabela SAFX08

__Obs__ Conforme retorno da área de Informação, de acordo com o manual da EFD\-ICMS/IPI, nos casos em que o informante não tenha direito ao crédito, os valores de ICMS/ST e/ou IPI devem ser adicionados ao valor das mercadorias\.

__Tratamento para notas fiscais de saída de mercadoria:__

Quando se tratar de item de mercadoria \(SAFX08\) à preencher com o preço do item \(campo 28\-VLR\_ITEM\)\.

__Tratamento para notas fiscais de serviço:__

Quando se tratar de item de serviço \(SAFX09\) à preencher com o preço do item \(campo 14\-VLR\_SERVICO\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

__RNC170\-08__

Campo VL\_DESC:

\[__ALTERAÇÃO\-MFS536991__\] Tratamento p/ Valor de Exclusão de ICMS na Base de Cálculo de PIS/COFINS, de acordo MP nº 1\.159

__Tratamento:__

__Parâmetro Marcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar Valor de Exclusão de ICMS no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159*__”, estiver __*MARCADO*__*, *preencher conforme regra abaixo: 

Para itens de mercadoria \(SAFX08\): Preencer com o campo 29\-VLR\_DESCONTO

Para itens de serviço \(SAFX09\): Preencher com o campo 21\-VLR\_DESCONTO

__Parâmetro Desmarcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar Valor de Exclusão de ICMS no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159”, *__estiver __*DESMARCADO*__, preencher conforme regra abaixo:

__Para itens de mercadoria \(SAFX08\):__

__\[Readequação feita pela MFS\-671016\] __Tratamento p/ Valor de Exclusão de ICMS na Base de Cálculo de PIS/COFINS, de acordo MP nº 1\.159

__Se__ o campo __VLR\_EXC\_BC\_PIS__ da tabela __DWT\_ITENS\_MERC__ for maior que 0 __então__

      Preencher o campo 8 do registro C170 com: VLR\_DESCONTO \+ VLR\_EXC\_BC\_PIS

__Senão se__ o campo __VLR\_EXC\_BC\_COFINS__ da tabela __DWT\_ITENS\_MERC__ for maior que 0 __então__

      Preencher o campo 8 do registro C170 com: VLR\_DESCONTO \+ VLR\_EXC\_BC\_COFINS

__Senão__

__      __Preencher o campo 8 do registro C170 com: VLR\_DESCONTO \+ 0,00

Fim se   

__Para itens de serviço \(SAFX09\):__

   

     __Preencher__ com o campo 21\-VLR\_DESCONTO

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

\[MFS\-37412\]: alteração no preenchimento do campo, passando a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08\.

__RNC170\-09__

Campo IND\_MOV:

A partir do conteúdo do campo “115\-Indicador de Movimentação Física do Item” do item \(SAFX08\), verificar:

Se indicador = “S” à gravar 0

Se indicador = “N” à gravar 1

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Indicador de Movimentação Física do Item do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-10__

Campo CST\_ICMS

Se item de Serviço, não preencher

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código de Situação Tributária A concatenado com o Código de Situação Tributária B do Item do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-11__

Campo CFOP

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código Fiscal do Item do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__RNC170\-12__

Campo COD\_NAT

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Natureza da Operação do Item do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

\[__ALTERAÇÃO\-MFS596091\] – Tratamento do campo COD\_NAT, para considerar também a situação abaixo:__

__Código da natureza de operação;__

Se o campo “Código da Natureza de Op\. SPED\-FISCAL” da Natureza de Operação \(SAFX2006\) estiver preenchido, então considerar a informação cadastrada neste campo\.

Caso contrário, considerar a informação do campo COD\_NATUREZA\_OP desta mesma tabela\.

__RNC170\-13__

Campo VL\_BC\_ICMS

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

__RNC170\-14__

Campo ALIQ\_ICMS:

__Se__ CST\_ICMS \(campo 10\)  <>  ‘00’ __e__  <> ‘10’ __e __ <> ‘20’  __e__  <> ‘70’

     __e__   VL\_BC\_ICMS \(campo 13\) = 0 ou nulo

     __e__   VL\_ICMS \(campo 15\) = 0 ou nulo

      Gravar zero;

__Senão __

     Gravar normalmente a alíquota conforme os campos descritos na planilha DE\-PARA

\[__OS4191__\] para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

__RNC170\-15__

__Campo VL\_ICMS__

Recuperar a informação do Campo 43\-VLR\_ICMS da tabela DWT\_ITENS\_MERC, 

Se for um Item de Serviço \(DWT\_ITENS\_SERV\), __não preencher__\.

\[__ALTERAÇÃO\-MFS536991__\] Tratamento p/ Valor de Exclusão de ICMS na Base de Cálculo de PIS/COFINS, de acordo MP nº 1\.159

__\[Readequação feita pela MFS\-671016\] __Tratamento p/ Valor de Exclusão de ICMS na Base de Cálculo de PIS/COFINS, de acordo MP nº 1\.159

Se o parâmetro na tela de Dados Iniciais “__*Gerar Valor de Exclusão de ICMS no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159*__”, estiver __*MARCADO, *__verificar:

__Se__ o campo __VLR\_EXC\_BC\_PIS__ da tabela __DWT\_ITENS\_MERC__ for maior que 0 __então__

      Preencher o campo 15 do registro C170, com o valor da coluna VLR\_EXC\_BC\_PIS

__Senão se__ o campo __VLR\_EXC\_BC\_COFINS__ da tabela __DWT\_ITENS\_MERC__ for maior que 0 __então__

      Preencher o campo 15 do registro C170, com o valor da coluna VLR\_EXC\_BC\_COFINS

__Senão__

__      __Preencher o campo 15 do registro C170 com 0,00

__Fim se__

Se o parâmetro na tela de Dados Iniciais “__*Gerar Valor de Exclusão de ICMS no campo 15 \- VL\_ICMS do registro C170 de acordo MP nº 1\.159*__”, estiver __*DESMARCADO,*__ então

      Preencher o campo 15 do registro C170, conforme o tratamento padrão

RNC170\-16

__RNC170\-17__

__RNC170\-18__

Campos VL\_BC\_ICMS\_ST,  ALIQ\_ST  e  VL\_ICMS\_ST:

Se campo “78\-Apropria” da SAFX08  =  “S”  \(IND\_CRED\_ICMSS\)

      Gravar normalmente os valores conforme os campos descritos na planilha DE\-PARA

Senão 

      Os campos não devem ser preenchidos;

Os valores do ICMS\-ST só serão carregados nestes campos quando o ST for considerado na apuração do ST\. Como a apuração só considera os valores do ICMS\-ST quando o indicador é = “S”, os campos também só serão preenchidos nesta situação\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

RNC170\-19

Campo IND\_APUR:

__Este campo deve conter a mesma regra do campo com a mesma nomeação do EFD Fiscal, conforme descrita abaixo__\. 

Este campo identifica se o produto/operação será apurado por mês ou decêndio\. Esta informação depende do tipo de apuração do IPI que o Estabelecimento utiliza \(apuração normal ou apuração da IN SRF 446/2004\), e deve ser obtida a partir do novo campo do cadastro do Estabelecimento \(Tipo de Apuração do IPI\) e da parametrização da IN 446 no módulo do IPI, da seguinte forma:

__Se__ tipo da apuração do IPI = 1 \(Periodicidade única p/todos os produtos \- livro 002\)

      Obter a periodicidade no cadastro da obrigação fiscal 002 \(tabela OBRIGACAO\_FISCAL\)

Senão 

     Neste caso será utilizada a mesma lógica da apuração da IN 446 para identificar se o item

      da nota fiscal será apurado por decêndio ou por mês\. Para isso, aplicar a seguinte regra:

__Para as notas de entrada__:

__Se método de cálculo do crédito das entradas = NCM__

__       Se__ o NCM estiver preenchido \(ou no produto, ou no item da nota fiscal\) \(vide OBS\)

             Se NCM foi parametrizado 

                  Considerar a apuração decendial

             Senão

                  Considerar a apuração mensal

       __Senão__ \(nem o produto, nem o item da nota têm a informação do NCM\)

              Se o CFOP ou CFOP/Nat foi parametrizado no item “Oper\. não identificáveis por NCM”

                  Considerar a apuração decendial

              Senão

                   Considerar a apuração mensal

__ Se método de cálculo do crédito das entradas = NCM/Produto__

__       Se__ o NCM estiver preenchido \(ou no produto, ou no item da nota fiscal\) \(vide OBS\)

             Se NCM __e__ o Produto foram parametrizados  

                  Considerar a apuração decendial

             Senão

                   Considerar a apuração mensal

__      Senão__ \(nem o produto, nem o item da nota têm a informação do NCM\)

              Se o CFOP ou CFOP/Nat foi parametrizado no item “Oper\. não identificáveis por NCM”

                   Considerar a apuração decendial

              Senão

                   Considerar a apuração mensal

__  Se__ __método de cálculo do crédito das entradas = Proporcionalidade__

          Considerar a apuração decendial

          \(neste caso todas as notas de entrada são lançadas nas apurações decendiais\) 

__Para as notas de saída__:

__ Se__ o NCM estiver preenchido \(ou no produto, ou no item da nota fiscal\) \(vide OBS\)

       Se NCM foi parametrizado 

             Considerar a apuração decendial

       Senão

             Considerar a apuração mensal

__ Senão__ \(nem o produto, nem o item da nota têm a informação do NCM\)

       Se o CFOP ou CFOP/Natureza foi parametrizado \(item “Oper\. não identificáveis por NCM”\)               

             Considerar a apuração decendial

       Senão

              Considerar a apuração mensal

A localização da parametrização da IN 446 se encontra no Módulo IPI, nos seguintes menus:

\-ParâmetrosàApur\. IPI\-IN SRF 446/2004àParâmetros Gerais

\-ParâmetrosàApur\. IPI\-IN SRF 446/2004àNCM’s c/apur\. decendial \(entradas e saídas\)

\-ParâmetrosàApur\. IPI\-IN SRF 446/2004à Produtos c/apur\. decendial \(somente entradas\)

\-ParâmetrosàOperações Não Identificáveis por NCM

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado respeitando as mesmas regras já definidas para geração desta informação\.

RNC170\-20

Campo CST\_IPI

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código de Tributação do IPI do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

RNC170\-21

Campo COD\_ENQ

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código do Enquadramento Legal do IPI do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__\[ALTERADA – CH19671\_2017 \(MFS\-14665\)\]__

No momento trataremos para esse campo ser preenchido com o conteúdo fixo “999”, pois o PVA não foi adequado para atender a NT2015\.002 que prevê demais códigos de enquadramento do IPI\. 

*Observação:* Esse código “999” pode significar que foi tributação normal ou outros motivos legais\. 

__\[ALTERADA\-MFS83273\]__

__Tratamento:__

    __Se__ o campo 174 \- COD\_ENQUAD\_IPI \(SAFX08\) estiver ‘vazio’ ou preenchido com ‘@’

       __Não preencher__, informar o campo vazio \(||\)\.

__Senão__

       Preencher o campo com o conteúdo fixo ‘999’\.

__Obs\.:__ No momento trataremos esse campo para ser preenchido com o conteúdo com “999” \(__*se estiver preenchido com qualquer valor diferente de ‘@’*__\), ou preencher o Campo ‘vazio’, \(__*se o campo estiver vazio*__\), pois o PVA não foi adequado para atender a NT2015\.002 que prevê demais códigos de enquadramento do IPI, conforme consulta no “Perguntas Frequentes”, a orientação é que esse campo deve ser informado ‘vazio’ \(||\)\.

*Observação:* Esse código “999” pode significar que foi tributação normal ou outros motivos legais\. 

RNC170\-22

Campo VL\_BC\_IPI

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

RNC170\-23

Campo ALIQ\_IPI

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

RNC170\-24

Campo VL\_IPI

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com valor zerado\.

RNC170\-25

Campo CST\_PIS

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código de Situação Tributária PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-26

Campos 26\-VL\_BC\_PIS:  

Se o campo Venda Cancelada \(campo novo da SAFX07\) for igual ‘’S” e 

- Se VL\_BC\_PIS for maior ou igual a  zero, então este campo devem ser gravado com valores iguais a zero; e os campos QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo VL\_BC\_PIS deve ser gravado com ||\.
- Se VL\_BC\_PIS e ALIQ\_PIS e QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente o valor  da Base de Cálculo do PIS \(86/SAFX08\)\.  Caso esse campo não esteja preenchido e o Código da Situação Tributária PIS \(campo 175 da SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo Base PIS\-ST \(campo 120/SAFX08\)\.

\[__MFS\-1876__\] Quando o CST PIS \(campo 175 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desses campos quando estiverem sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Base de Cálculo do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-27

Campo 27\- ALIQ\_PIS:

Se o campo Venda Cancelada \(campo novo da SAFX07\) for igual ‘’S” e 

-        Se ALIQ\_PIS for maior ou igual a zero, então este campo deve ser gravado com valores maior ou igual a zero; e os campos QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo ALIQ\_PIS deve ser gravado com ||\.
- Se VL\_BC\_PIS e ALIQ\_PIS e QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente o Valor da Alíquota do PIS \(129/SAFX08\)\. Caso esse campo não esteja preenchido e o Código da Situação Tributária PIS \(campo 175/SAFX08\) estiver preenchido com a opção “5””, a informação deve ser recuperada do campo  Valor do PIS\-ST \(campo 121/SAFX08\)

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Alíquota do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-28/29

Campos 28\-QUANT\_BC\_PIS e 29\-ALIQ\_PIS\_QUANT:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S” e 

-  Se QUANT\_BC\_PIS for maior ou igual a zero, então este campo deve ser gravado com valores iguais a zero; e os campos VL\_BC\_PIS e ALIQ\_PIS devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo QUANT\_BC\_PIS deve ser gravado com ||\.
- Se ALIQ\_PIS\_QUANT for maior ou igual a zero, então este campo deve ser gravado com valores iguais ou maiores que zero; e os campos VL\_BC\_PIS e ALIQ\_PIS devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo ALIQ\_PIS\_QUANT deve ser gravado com ||\.
- Se VL\_BC\_PIS e ALIQ\_PIS e QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente os valores conforme os campos descritos na planilha DE\-PARA

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desses campos quando estiverem sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

RNC170\-30

Campo  VL\_PIS:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S”, 

       Esse campo deve ser preenchido com zeros \( 0,00\)

Senão

Gravar normalmente o Valor do PIS \(campo 87 da SAFX08\)\. Caso esse campo não esteja preenchido e o campo Código Situação Tributária PIS \(campo 175 da SAFX08\) estiver igual a ‘’5’’,  a informação deve ser recuperada do campo Valor Tributo PIS\-ST \(campo 122 da SAFX08\)\.

\[__MFS\-1876__\] Quando o CST PIS \(campo 175 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estive sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Valor do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-31

Campo CST\_COFINS

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Código de Situação Tributária COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-32

Campos VL\_BC\_COFINS:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S” e 

- Se VL\_BC\_COFINS for maior ou igual a  zero, então este campo devem ser gravado com valores iguais a zero; e os campos QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo VL\_BC\_COFINS deve ser gravado com ||\.
- Se VL\_BC\_COFINS e ALIQ\_COFINS e QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente o Valor da Base de Cálculo COFINS \(campo 88 da SAFX08\)\. Caso esse campo não esteja preenchido e o campo Código da Situação Tributária \(campo 178/ SAFX08\) estiver preenchido com a opção ‘’5”, a informação deve ser recuperada do campo Base COFINS\-ST \(campo 123/SAFX08\)

\[__MFS\-1876__\] Quando o CST COFINS \(campo 178 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desses campos quando estiverem sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Base de Cálculo da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-33

Campo ALIQ\_COFINS:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S” e 

-        Se ALIQ\_COFINS  for maior ou igual a zero, então este campo deve ser gravado com valores maior ou igual a zero; e os campos QUANT\_BC\_COFINS e ALIQ\_COFNS\_QUANT devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo ALIQ\_COFINS deve ser gravado com ||\.
- Se VL\_BC\_COFINS e ALIQ\_COFINS e QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente o Valor da Alíquota da COFINS \(campo130 da SAFX08\)\. Caso esse campo não esteja preenchido e o campo Código da Situação Tributária  \(campo 78/ SAFX08\) estiver preenchido com a opção “5”,  a informação deve ser recuperada do campo Alíquota da COFINS\-ST \(campo 124/ SAFX08\) 

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Alíquota da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-34/35

Campos QUANT\_BC\_COFINS, ALIQ\_COFINS\_QUANT:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S”, 

- Se QUANT\_BC\_COFINS for maior ou igual a zero, então este campo deve ser gravado com valores iguais a zero; e os campos VL\_BC\_COFINS e ALIQ\_COFINS  devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo QUANT\_BC\_COFINS deve ser gravado com ||\.
- Se ALIQ\_COFINS\_QUANT for maior ou igual a zero, então este campo deve ser gravado com valores iguais ou maiores que zero; e os campos VL\_BC\_COFINS e ALIQ\_COFINS devem ser gravados sem informação, ou seja, ||\. Caso contrário, o campo ALIQ\_COFINS\_QUANT deve ser gravado com ||\.
- Se VL\_BC\_COFINS e ALIQ\_COFINS e QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||\.

Senão

Gravar normalmente os valores conforme os campos descritos na planilha DE\-PARA\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desses campos quando estiverem sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

RNC170\-36

Campo VL\_COFINS:

Se o campo Venda Cancelada \(campo novo da SAFX08\) for igual ‘’S”, 

       Esse campo deve ser preenchido com zeros \( 0,00\)

Senão

Gravar normalmente o Valor da COFINS \(campo 89 da SAFX08\)\. Caso esse campo não esteja preenchido e o Código Situação Tributária COFINS \(178/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo Valor Tributo COFINS\-ST \(campo 125/SAFX08\)

\[__MFS\-1876__\] Quando o CST COFINS \(campo 178 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com o Valor da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

RNC170\-37

Campo COD\_CTA

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será gerado com a Conta Contábil do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido, respeitando as mesmas regras já definidas para geração desta informação\.

__Registro C175 \- Analítico do Documento \(código 65\)__

__RNG\-C175__

\[OS4316\-E\]

__Origem da Informação__: SAFX08 \- Itens Notas Fiscais Mercadorias e Produtos

__Regra de seleção__: este registro será gerado para cada item da nota fiscal gravada no registro C100, restringindo às operações de NFC\-e \(Modelo 65\) e desconsiderando itens de documentos cancelados, onde o COD\_SIT = 02 \(cancelado\)\.

Será gerado apenas se no cadastro do Perfil \(menu: Parâmetros >> Perfil\) o registro C175 __estiver__ selecionado \(OS4474\)

__Agrupamento das Informações__: campos CFOP, CST\_PIS, ALIQ\_PIS, ALIQ\_PIS\_QUANT, CST\_COFINS, ALIQ\_COFINS, ALIQ\_COFINS\_QUANT e COD\_CTA\.

__RNC175\-01__

Campo REG

Será gerada a informação fixa “C175”\.

__RNC175\-02__

Campo CFOP

Será gerado com o conteúdo do campo CFOP \(COD\_CFO\) da SAFX08\.

__RNC175\-03__

Campo VL\_OPR

Será gerado com a somatória do Valor do Item \(VLR\_ITEM\) da SAFX08\. 

__RNC175\-04__

Campo VL\_DESC

Será gerado com a somatória do Valor do Desconto do Item \(VLR\_DESCONTO\) da SAFX08\.

__RNC175\-05__

Campo CST\_PIS

Será gerado com o Código de Situação Tributária PIS \(COD\_SITUACAO\_PIS\) da SAFX08\.

__RNC175\-06__

Campo VL\_BC\_PIS

Considerar a seguinte regra:

Se o campo Código de Situação Tributária PIS \(COD\_SITUACAO\_PIS\) da SAFX08 for igual a “03”, este campo será gerado sem informação \(“||”\)\. Se for diferente, será resultado da somatória do campo BC do PIS \(VLR\_BASE\_PIS\) da SAFX08\.

__RNC175\-07__

Campo ALIQ\_PIS

Considerar a seguinte regra:

Se o campo Código de Situação Tributária PIS \(COD\_SITUACAO\_PIS\) da SAFX08 for igual a “03”, este campo será gerado sem informação \(“||”\)\. Se for diferente, será considerado o conteúdo do campo Alíquota do PIS \(VLR\_ALIQ\_PIS\) da SAFX08\.

__RNC175\-08__

Campo QUANT\_BC\_PIS

Considerar a seguinte regra:

Se o campo Código de Situação Tributária PIS \(COD\_SITUACAO\_PIS\) da SAFX08 for diferente de “03”, este campo será gerado sem informação \(“||”\)\. Se for igual, será resultado da somatória do campo Quantidade da BC do PIS \(QTD\_BASE\_PIS\) da SAFX08\.

__RNC175\-09__

Campo ALIQ\_PIS\_QUANT

Considerar a seguinte regra:

Se o campo Código de Situação Tributária PIS \(COD\_SITUACAO\_PIS\) da SAFX08 for diferente de “03”, este campo será gerado sem informação \(“||”\)\. Se for igual, será considerado o conteúdo do campo Alíquota do PIS em Reais \(VLR\_ALIQ\_PIS\_R\) da SAFX08\.

__RNC175\-10__

Campo VL\_PIS

Será gerado com a somatória do Valor do PIS do Item \(VLR\_PIS\) da SAFX08\.

__RNC175\-11__

Campo CST\_COFINS

Será gerado com o Código de Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) da SAFX08\.

__RNC175\-12__

Campo VL\_BC\_COFINS

Considerar a seguinte regra:

Se o campo Código de Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) da SAFX08 for igual a “03”, este campo será gerado sem informação \(“||”\)\. Se for diferente, será resultado da somatória do campo BC da COFINS \(VLR\_BASE\_COFINS\) da SAFX08\.

__RNC175\-13__

Campo ALIQ\_COFINS

Se o campo Código de Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) da SAFX08 for igual a “03”, este campo será gerado sem informação \(“||”\)\. Se for diferente, será considerado o conteúdo do campo Alíquota da COFINS \(VLR\_ALIQ\_COFINS\) da SAFX08\.

__RNC175\-14__

Campo QUANT\_BC\_COFINS

Considerar a seguinte regra:

Se o campo Código de Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) da SAFX08 for diferente de “03”, este campo será gerado sem informação \(“||”\)\. Se for igual, será resultado da somatória do campo Quantidade da BC da COFINS \(QTD\_BASE\_COFINS\) da SAFX08\.

__RNC175\-15__

Campo ALIQ\_COFINS\_QUANT

Considerar a seguinte regra:

Se o campo Código de Situação Tributária COFINS \(COD\_SITUACAO\_COFINS\) da SAFX08 for diferente de “03”, este campo será gerado sem informação \(“||”\)\. Se for igual, será considerado o conteúdo do campo Alíquota da COFINS em Reais \(VLR\_ALIQ\_COFINS\_R\) da SAFX08\.

__RNC175\-16__

Campo VL\_COFINS

Será gerado com a somatória do Valor da COFINS do Item \(VLR\_COFINS\) da SAFX08\.

__RNC175\-17__

Campo COD\_CTA

Será gerado com o conteúdo do campo Conta Contábil \(COD\_CONTA\) da SAFX08\.

O código aqui informado deve dar origem a um registro 0500\.

__RNC175\-18__

Campo INFO\_COMPL

Este campo será gerado sem informação \(“||”\)\.

__Registro C180 – Consolidação das NF\-e Emitidas pela PJ \(Código 55 e 65\) – Operações de Vendas__

__RNG\-C180__

Esse registro só deve ser gerado quando as vendas feitas através de nota fiscal eletrônica não tiverem sido informadas no registro C100, então:

__SE Indicador da Escrituração \(NF\-e e ECF\):__ \(parâmetro nos dados iniciais da obrigação\)

	Igual a “2 – Apuração com base nos registros individualizados\.\.\.”

	Não gravar dados nesse registro\.

__SE Indicador da Escrituração \(NF\-e e ECF\):__ \(parâmetro nos dados iniciais da obrigação\)

	Igual a “1 – Apuração com base nos registros consolidados\.\.\.”

	Gerar um registro para cada grupo__\*\*__ de notas fiscais \(SAFX07\) que atendam os critérios abaixo:

	Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Igual a “9 – Documento de Saída”

	Normal/Devolução: \(campo 04 da SAFX07\)

		Igual a “1 – Normal”

                                             

	Seleção das Operações Geradoras de Receita: \(parâmetro nos dados iniciais da obrigação\)

                            SE for igual ‘’Data de Lançamento PIS/COFINS’’ \(campo 196 da SAFX08\)

                                                Entre a Data Inicial e Data Final de geração do arquivo

                           SENÃO \(igual ‘’Data de Emissão’’\)   

                                               Data de Emissão: \(campo 11 da SAFX07\)

			        Entre a Data Inicial e Data Final de geração do arquivo

Obs\. A Data de Lançamento PIS/COFINS poderá ser menor do que a Data de Emissão, está prevista legalmente esta situação\.

Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

		Igual a “1 – Mercadoria” , “3 \- Mercadorias e Serviços”,  e Se o parâmetro __Notas Fiscais de Mercadoria Não Escrituradas__ estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação ‘7 – Notas Fiscais de Mercadoria não Escrituradas’, \(campo 12 da safx07\) e que possuam CST´s de PIS e COFINS \(SAFX07 ou 08\)

	Modelo: \(campo “13 – Modelo de Documento” da SAFX07\)

		Igual a “55”

	Crédito/Contribuição Extemporânea: \(campo novo da SAFX08\)

		Somente itens não extemporâneos \(campo novo = “N”\)

	CFOP \(ou CFOP\+Natureza\)__\*__ \(campos 22 e 23 da SAFX08\)

		Relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de

		operação igual a “Geradora de Receita”

\(OS4474\) Se no cadastro do Perfil \(menu: Parâmetros >> Perfil\) o registro C175 __não__ __estiver__ selecionado , gerar neste registro informações de NFC\-e, considerando o seguinte critério de seleção:

	Movimento Entrada/Saída: \(campo 03 da SAFX07\)

		Igual a “9 – Documento de Saída”

	Normal/Devolução: \(campo 04 da SAFX07\)

		Igual a “1 – Normal”

                                             

	Seleção das Operações Geradoras de Receita: \(parâmetro nos dados iniciais da obrigação\)

                            SE for igual ‘’Data de Lançamento PIS/COFINS’’ \(campo 196 da SAFX08\)

                                                Entre a Data Inicial e Data Final de geração do arquivo

                           SENÃO \(igual ‘’Data de Emissão’’\)

                                               Data de Emissão: \(campo 11 da SAFX07\)

			        Entre a Data Inicial e Data Final de geração do arquivo

	Modelo: \(campo “13 – Modelo de Documento” da SAFX07\)

		Igual a “65”

*A escrituração de NCF\-e neste registro depende apenas do registro C175 não estar selecionado no Perfil e não levará em conta o parâmetro “Indicador da Escrituração \(NF\-e e ECF\)” dos Dados Iniciais\.*

__\*__ Devemos considerar que apenas os itens da NF que possuam CFOP \(ou CFOP\+Natureza\) relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de operação igual a “Geradora de Receita” serão considerados nesse registro\.

__\*\*__ O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações dos itens desses documentos \(SAFX08\):

\- Data de Emissão dos Documentos

\- Código do Produto/Bem \(Indicador \+ Código do Produto ou Bem\)

\- Código NBM \(campo 26 da SAFX08\)

__Obs\. 1:__ Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal \(SAFX08\), considerar o conteúdo desses campos informados na capa do documento \(SAFX07\)\.

__Obs\. 2:__ Os movimentos de devolução serão demonstrados no registro C190

__Parâmetro “Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de receita”:__

- __Se por Data de Emissão:__ Se a data selecionada for Data de Emissão, através do parâmetro “Registro A100, 	C100, C180 e C190 – Seleção das Operações Geradoras de Receita” cadastrado em Dados Iniciais, considerar os documentos selecionados para os registros A e C que serão filtrados com base na Data de Emissão compreendida entre a Data Inicial e Data Final de Geração do Arquivo\.

__Tratamento especial para notas complementares de saída:__

Quando se tratar de NF complementar \(campo 125 da SAFX07 igual a “5 \- NF Complementar ou CT\-e de Complemento de Valores”\) de saída, somente deverá ser considerado o documento que possuir no campo “23 – Valor Total do Documento Fiscal” ou “68 – Valor Total Serviços” valor maior que zero\.

\[__OS4191__\]

Quando o campo Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST estiver preenchido em um dos itens considerados no agrupamento deste registro e os critérios de geração do mesmo forem atendidos, deverá ser considerado nos registros filhos do C180, C181 e C185, os valores lançados de ST no agrupamento das informações, com o objetivo de demonstrar os valores referentes à Substituição Tributária para que os mesmos sejam considerados na apuração\.

Exemplo: foram consideradas no agrupamento 3 NFs com as seguintes características:

__Nº NF__

__Cód\. Produto__

__Data Emissão__

__CST Normal__

__CST ST__

__Valor Normal__

__Valor ST__

1234

XPTO

02/02/2014

01

05

1000

500

4567

XPTO

05/02/2014

05

1000

6789

XPTO

07/02/2014

06

05

1000

500

Neste exemplo teremos:

C180 >> DT\_IINICIO 02/02/2014 >> DT\_FIM 07/02/2014 >> PRODUTO XPTO

     C181 >> CST 01 >> Valor 1000

     C181 >> CST 05 >> Valor 2000 *\(1000 Valor Normal NF 4567 \+ 500 Valor ST NF 1234 \+ 500 Valor ST NF 6789\)*

     C181 >> CST06 >> Valor 1000

     C185 >> CST 01 >> Valor 1000

     C185 >> CST 05 >> Valor 2000 *\(1000 Valor Normal NF 4567 \+ 500 Valor ST NF 1234 \+ 500 Valor ST NF 6789\)*

     C185 >> CST06 >> Valor 1000

Esta situação irá ocorrer apenas para os documentos gerados a partir da SAFX08\.

__Parâmetro “Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de receita”:__

- __Se por Data de Emissão:__ Se a data selecionada for Data de Emissão, através do parâmetro “Registro A100, 	C100, C180 e C190 – Seleção das Operações Geradoras de Receita” cadastrado em Dados Iniciais, considerar os documentos selecionados para os registros A e C que serão filtrados com base na Data de Emissão compreendida entre a Data Inicial e Data Final de Geração do Arquivo\.

	

\[__OS4316\-A__\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

Dúvidas: Havendo a situação \(emissão\) de NF modelo 01 ou 1B \(ou modelo 55\*\), um mesmo documento trará valores da competência do ICMS e do ISS segregados por item, como devera se comportar a geração dos registros?

Carregam\-se os valores referentes ao ISS no bloco A e os valores referentes ao ICMS no bloco C? Ou a totalidade dos valores deverá ser escriturada no bloco C\.

__RNC180\-02__

Campo COD\_MOD:

Texto fixo “55”, mesmo que se trate de NFC\-e, modelo 65 \(OS4474\)\.

Preencher com o código do modelo do documento fiscal \(podendo ser 55 ou 65\)\.

__MFS\-34948 \(15/05/2020\):__

__A regra criada pela OS4474 estava baseada na época em que esse campo só aceitava modelo 55\.__

Conforme cita no Guia Pratíco v 1\.33 \(16/12/2019\), até agosto de 2014 o único modelo válido para este campo era o 55, por isso preenchíamos este campo com 55\. 

Mas este campo ja aceita o modelo 65 a e a regra estava desatualizada\.

__RNC180\-03__

Campo DT\_DOC\_INI:

Este campo deve ser preenchido com a data de emissão do primeiro documento fiscal agrupado neste de registro

Para notas canceladas este campo não deverá ser informado\.

__RNC180\-04__

Campo DT\_DOC\_FIN:

Este campo deve ser preenchido com a data de emissão do último documento fiscal agrupado neste registro\.

Para notas canceladas este campo não deverá ser informado\.

__RNC180\-05__

Campo COD\_ITEM:

Este campo deve ser preenchido com o produto \(SAFX2013\) ou Bem \(SAFX13\), informado no item de mercadoria da SAFX08 e com o serviço /natureza \(SAFX2018\), informado no item de serviço da SAFX09 das notas fiscais agrupadas\.

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:

Aplicar a mesma regra de concatenação já definida no registro 0200: 

Quando se tratar de serviço da SAFX2018, ao invés de gravar sempre o código do serviço, deve\-se verificar o novo parâmetro incluído na tela dos “Dados Inicias”, e seguir a regra:

  Se parâmetro = “Código do Serviço” à gravar o código do serviço \(campo 1 da SAFX2018\)

  Se parâmetro = “Natureza do Serviço” à gravar a natureza do serviço \(campo 8 da SAFX2018\)

Produtos da SAFX2013 à Indicador de Produto \+ "\-" \+ Código do produto

Serviços da SAFX2018  à "S"  \+  "\-"  \+  Código ou Natureza do Serviço

Bens da SAFX13         à "B" \+ "\-" \+ Código do Bem \+ "\-I" \+ Código Incorporador

Para notas canceladas este campo não deverá ser informado\.

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:

Quando se tratar de serviço da SAFX2018, ao invés de gravar sempre o código do serviço, deve\-se verificar o novo parâmetro incluído na tela dos “Dados Inicias”, e seguir a regra:

Se parâmetro = “Código do Serviço” à gravar o código do serviço \(campo 1 da SAFX2018\)

Se parâmetro = “Natureza do Serviço” à gravar a natureza do serviço \(campo 8 da SAFX2018\)

Quando se tratar de Bens da SAFX13:

Produtos da SAFX2013 à Código do produto

Serviços da SAFX2018 à Código ou Natureza do Serviço

Bens da SAFX13         à  Código do Bem 

Para notas canceladas este campo não deverá ser informado\.

__RNC180\-06__

Campo NCM:

Este campo deve ser preenchido com o código do NCM \(considerar as 8 primeiras posições\), informado no item de mercadoria da SAFX08 das notas fiscais agrupadas\.

Obs: Os NCM’s devem ser carregados para o campo 05\-COD\_NBM da tabela de produtos, pois o Mastersaf trabalha com a SAFX2043, que contém na verdade os NCM’s\.

Para notas canceladas este campo não deverá ser informado\.

__Alteração da MFS12767:__ A partir da vrs 2\.1\.1 do PVA, liberada em Ago/2017, o campo NCM passou a ser obrigatório\. Por isso, será feito o seguinte procedimento:

Caso o resultado da consolidação, conforme descrito na __RNG\-C180__, não tenha a informação do NCM, será verificado se o produto em questão é um Serviço ou não:

__Se__ o produto em questão for um serviço \(se TIPO\_ITEM gravado no registro 0200 for = “09”\):

     Nesse caso, este campo será gravado com o conteúdo “00”, conforme previsto no Guia Prático vrs 1\.22;

__Senão__

     Nesse caso será gravada a seguinte  mensagem de aviso no log: “*O campo 06\-NCM é obrigatório e não foi*

*     informado\. Verificar os movimentos consolidados para a data de emissão e produto*”\. O log deve informar

     nos dados de identificação a informação da Data de Emissão e do Indicador e Código Produto dos

     movimentos consolidados\.

__RNC180\-07__

Campo EX\_IPI:

Para notas canceladas este campo não deverá ser informado\.

__\[ALTERAÇÃO MFS\-642118\]__ Quando o campo 11\- EX\_IPI da SAFX2043 não estiver preenchido:

Este campo deve ser preenchido com os dois últimos dígitos do NCM nota fiscal agrupada, conforme a tabela básica SAFX2043, com o seguinte critério:

Quando se tratar de um produto da SAFX2013 à Preencher com os dois últimos dígitos do NCM do produto \(posições 9 e 10\)\. Quando estas posições estiverem com brancos, o campo não deve ser preenchido, pois o NCM não tem exceção\.

__\[ALTERAÇÃO MFS\-642118\]__ Quando o campo 11\- EX\_IPI da SAFX2043 estiver preenchido:

Considerar a informação do campo 11 – EX\_IPI da SAFX2043

__RNC180\-08__

Campo VL\_TOT\_ITEM:

Este campo deve ser preenchido com o somatório do valor dos itens \(campo: 28/SAFX08 e 15/SAFX09\) das notas fiscais agrupadas\.

Para notas canceladas este campo não deverá ser informado\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, o Valor do Item de ST não deve ser considerado nesta somatória\.

__Registro C181 – Detalhamento da Consolidação – Operações de Vendas PIS/PASEP__

__RNG\-C181__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C180 com base nas seguintes informações:

\- Código de Situação Tributária PIS: \(campo 175 da SAFX08 e 68/SAFX09\)

\- CFOP: \(campo 22 da SAFX08 e 17/SAFX09\)

\- Alíquota do PIS: \(campo 129 ou 177 da SAFX08  e 47/SAFX09\)

\- Código da Conta Contábil: \(campo 105 da SAFX08 e 52/SAFX09\)

\[__OS4191__\] Quando o campo Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST estiver preenchido em um dos itens considerados no agrupamento, as informações do campo Código Situação Tributária PIS ST e Alíquota do PIS ST devem ser consideradas na composição deste registro, como se fossem um item a mais da NF\.

__RNC181\-04__

Campo VL\_ITEM: 

Este campo deve ser preenchido com a somatória do valor dos itens \(campo: 28/SAFX08 e 15/SAFX09\) das notas fiscais agrupadas no C180 e pela a combinação CST\_PIS, CFOP, Alíquota do PIS e Código da Conta Contábil

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este valor não será considerado\.

__RNC181\-05__

Campo VL\_DESC:

Deve\-se fazer a somatória do valor do Desconto dos itens \(campo: 29/SAFX08 e 21/SAFX09\) das notas fiscais agrupadas no C180 e pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

__\[MFS32069\]__

Deve\-se fazer a somatória do Valor da Exclusão da BC PIS dos itens \(campo: 260/SAFX08\) das notas fiscais agrupadas no C180 e pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

Este campo deve ser preenchido com o somatório dos campos valor do Desconto e Valor da Exclusão da BC PIS\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este valor não será considerado\.

__RNC181\-06__

Campo VL\_BC\_PIS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo do PIS \(86/SAFX08 e 46/SAFX09\) das notas fiscais agrupadas no C180 e pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

Caso o Código Situação Tributária PIS \(175/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo Base PIS\-ST \(campo 120/SAFX08\) caso o mesmo esteja preenchido\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo Base de Cálculo do PIS \(86/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se VL\_BC\_PIS ou ALIQ\_PIS forem maiores que zero, então este campo deve ser gravado com valor igual a zero; e os campos QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_PIS ,ALIQ\_PIS , QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerada a Base de Cálculo do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__RNC181\-07__

Campo ALIQ\_PIS:

Este campo deve ser preenchido com a somatória do Valor da Alíquota do PIS \(129/SAFX08 e 47/SAFX09\) das notas fiscais agrupadas no C180 e pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

Caso o Código Situação Tributária PIS \(175/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo VLR\_ALIQ\_PIS\_ST \(campo 121/SAFX08\)\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo Valor da Alíquota do PIS \(129/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se VL\_BC\_PIS ou ALIQ\_PIS forem maiores que zero, então este campo deve ser gravado com valor da ALIQ\_PIS;  e os campos QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_PIS, ALIQ\_PIS, QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerada a Alíquota do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__RNC181\-08__

Campo QUANT\_BC\_PIS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo do PIS – em quantidade \(176/SAFX08\) das notas fiscais agrupadas no C180 e pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se QUANT\_BC\_PIS ou ALIQ\_PIS\_QUANT forem maiores que zero, então este campo deve ser gravado com valor igual  a zero; e os campos VL\_BC\_PIS e ALIQ\_PIS devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_PIS ,ALIQ\_PIS , QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

__RNC181\-09__

Campo ALIQ\_PIS\_QUANT:

Este campo deve ser preenchido com a somatória do valor da Alíquota do PIS – em Reais \(177/SAFX08\) das notas fiscais agrupadas no C180\- pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil, exceto quando o campo Venda Cancelada \(campo novo da SAFX07\) estiver igual ‘’S”, então, esse campo deve ser preenchido com zero \(0,00\)

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se QUANT\_BC\_PIS ou ALIQ\_PIS\_QUANT forem maiores que zero, então este campo deve ser gravado com valor da ALIQ\_PIS\_QUANT ; e os campos VL\_BC\_PIS e ALIQ\_PIS devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_PIS , ALIQ\_PIS ,QUANT\_BC\_PIS e ALIQ\_PIS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

__RNC181\-10__

Campo VL\_PIS:

Este campo deve ser preenchido com a somatória do valor do PIS dos itens \(87/SAFX08 e 48/SAFX09\) das notas fiscais agrupadas no C180 pela combinação CST PIS, CFOP, Alíquota de PIS e Código da Conta Contábil, exceto quando o campo Venda Cancelada \(campo novo da SAFX07\) estiver igual ‘’S”, então, esse campo deve ser preenchido com zero \(0,00\)

Caso o Código Situação Tributária PIS \(175/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo VLR\_PIS\_ST \(campo 122/SAFX08\)\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo valor do PIS dos itens \(87/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerado o Valor do PIS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__Registro C185 – Detalhamento da Consolidação – Operações de Vendas COFINS__

__RNG\-C185__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C180 com base nas seguintes informações:

\- Código de Situação Tributária COFINS: \(campo 178 da SAFX08 e 69/SAFX09\)

\- CFOP: \(campo 22 da SAFX08 e 17/SAFX09\)

\- Alíquota da COFINS \(campo 130 ou 180 da SAFX08 e 50/SAFX09\)

\- Código da Conta: \(campo 105 da SAFX08 e 52/SAFX09\)

\[__OS4191__\] Quando o campo Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST estiver preenchido em um dos itens considerados no agrupamento, as informações do campo Código Situação Tributária COFINS ST e Alíquota da COFINS ST devem ser consideradas na composição deste registro, como se fossem um item a mais da NF\.

__RNC185\-04__

Campo VL\_ITEM:

Este campo deve ser preenchido com a somatória do valor dos itens \(campo: 28/SAFX08 e 15/SAFX09\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este valor não será considerado\.

__RNC185\-05__

Campo VL\_DESC:

Deve\-se fazer a somatória do valor do Desconto dos itens \(campo: 29/SAFX08 e 21/SAFX09\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP e Alíquota da COFINS e Código da Conta\.

__\[MFS32069\]__

Deve\-se fazer a somatória do Valor da Exclusão da BC COFINS dos itens \(campo: 261/SAFX08\) das notas fiscais agrupadas no C180 e pela combinação CST COFINS, CFOP, Alíquota do COFINS e Código da Conta Contábil\.

Este campo deve ser preenchido com o somatório dos campos valor do Desconto e Valor da Exclusão da BC COFINS\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este valor não será considerado\.

__RNC185\-06__

Campo VL\_BC\_COFINS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo da COFINS \(88/SAFX08 e 49/SAFX09\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil\.

Caso o Código Situação Tributária COFINS \(178/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo Base COFINS\-ST \(campo 123/SAFX08\) caso o mesmo esteja preenchido\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo Base de Cálculo do COFINS \(88/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se VL\_BC\_COFINS ou ALIQ\_COFINS forem maiores que zero, então este campo deve ser gravado com valor igual a zero; e os campos QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_PIS , ALIQ\_PIS , QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerada a Base de Cálculo da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__RNC185\-07__

Campo ALIQ\_COFINS:

Este campo deve ser preenchido com a somatória do valor da Alíquota da COFINS \(130/SAFX08 e 50/SAFX09\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil\.

Caso o Código Situação Tributária COFINS \(178/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo VLR\_ALIQ\_COFINS\_ST \(campo 124/SAFX08\)\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo valor da Alíquota da COFINS \(130/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se VL\_BC\_COFINS ou ALIQ\_ COFINS forem maiores que zero, então este campo deve ser gravado com valor da ALIQ\_ COFINS; e os campos QUANT\_BC\_ COFINS e ALIQ\_ COFINS \_QUANT devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_ COFINS, ALIQ\_ COFINS, QUANT\_BC\_ COFINS e ALIQ\_ COFINS \_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerada a Alíquota da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__RNC185\-08__

Campo QUANT\_BC\_COFINS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo da COFINS – em quantidade \(179/SAFX08\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se QUANT\_BC\_COFINS ou ALIQ\_COFINS\_QUANT forem maiores que zero, então este campo deve ser gravado com valor igual  a zero; e os campos VL\_BC\_COFINS e ALIQ\_COFINS  devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_COFINS ,ALIQ\_COFINS , QUANT\_BC\_COFINS e ALIQ\_COFINS\_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

__RNC185\-09__

Campo ALIQ\_COFINS\_QUANT:

Este campo deve ser preenchido com a somatória do valor da Alíquota da COFINS – em Reais \(89/SAFX08\) das notas fiscais agrupadas no C180, pela a combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil\.

Venda Cancelada:

Se campo 253\- IND\_VENDA\_CANC da SAFX07 estiver igual ‘’S’’ e 

- Se QUANT\_BC\_COFINS ou ALIQ\_ COFINS \_QUANT forem maiores que zero, então este campo deve ser gravado com valor da ALIQ\_ COFINS \_QUANT ; e os campos VL\_BC\_ COFINS e ALIQ\_ COFINS devem ser gravados sem informação, ou seja, ||;
- Se VL\_BC\_ COFINS , ALIQ\_ COFINS ,QUANT\_BC\_ COFINS e ALIQ\_ COFINS \_QUANT forem iguais a zero, então TODOS devem ser gerados com ‘||’\. \(Se esta situação existir em algum cliente ocorrerá erro no validador, que não aceita todos os campos de valores zerados ou sem informação\)\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, este campo será sem informação “||”\.

__RNC185\-10__

Campo VL\_COFINS:

Totalização do valor da COFINS de todos os itens envolvidos na consolidação do registro C180 pela combinação CST COFINS, CFOP, Alíquota de COFINS e Código da Conta Contábil, exceto quando o campo Venda Cancelada \(campo novo da SAFX07\) for igual ‘’S”, então, esse campo deve se preenchido com  zeros \(0,00\)

Caso o Código Situação Tributária COFINS \(178/SAFX08\) estiver preenchido com a opção “5”, a informação deve ser recuperada do campo VLR\_COFINS\_ST \(campo 125/SAFX08\)\. Caso o mesmo não esteja preenchido, a informação deve ser recuperada do campo VLR\_COFINS \(89/SAFX08\) respeitando as regras de consolidação informadas anteriormente\.

Obs\.:

Verificar o documento de Regra Geral \(__RegraGeral\_v18\.doc__\), para a formatação desse campo quando estiver sem preenchimento\.

\[__OS4191__\] Para geração da informação do Item que demonstra valores de ST, neste campo será considerado o Valor da COFINS ST do Item que tem o Código Situação Tributária PIS ST ou Código Situação Tributária COFINS ST preenchido\.

__Registro C188 – Processo Referenciado__

__RNG\-C188__

Nesse registro devem ser gravados os registros da SAFX114 relacionados aos itens de documentos agrupados no registro C180, que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS”

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

Nº Item da NF:

	Deve ser um dos itens agrupados no registro C180 correspondente, ou deve estar em branco\.

Dúvidas:

 1\- Criar indicador para diferenciar os processos referenciados do ICMS/IPI dos processos do PIS/COFINS nos registros da SAFX114?

__Resposta__: Criação de um campo para indicar que o processo refere\-se ao EFD PIS/COFINS

__Registro C190 – Consolidação das NF\-e \(Código 55\) – Operações de Aquisição com Direito a Crédito e Devolução de Compra e Vendas__

__RNG\-C190__

Esse registro só deve ser gerado quando as aquisições e devoluções de compra e vendas forem feitas através de nota fiscal eletrônica, então:

__SE Indicador da Escrituração \(NF\-e e ECF\):__ \(parâmetro nos dados iniciais da obrigação\)

	Igual a “2 – Apuração com base nos registros individualizados\.\.\.”

	Não gravar dados nesse registro\.

__SE Indicador da Escrituração \(NF\-e e ECF\):__ \(parâmetro nos dados iniciais da obrigação\)

	Igual a “1 – Apuração com base nos registros consolidados\.\.\.”

	Gerar um registro para cada grupo__\*__ de notas fiscais \(SAFX07\) que atendam os critérios abaixo:

As NF’s que forem recuperadas de acordo com a regra de preenchimento 1, devem ter seus itens agrupados de acordo com a regra de preenchimento 2 \(abaixo\):

__Regra de preenchimento 1 \(recuperação dos documentos\):__

- Modelo: \(campo 13 da SAFX07\)

	Igual a “55”

- Classificação: \(campo “12 – Classificação do Documento” da SAFX07\)

Igual a “1 – Mercadoria” ,  “3 \- Mercadorias e Serviços”;

Se o parâmetro __Notas Fiscais de Mercadoria Não Escrituradas__ estiver marcado em Dados Iniciais, as notas fiscais de saída com Classificação “7 – Notas Fiscais de Mercadoria não Escrituradas”, \(campo 12 da safx07\) e que possuam CST´s de PIS e COFINS \(SAFX07 ou 08\)

Crédito/Contribuição Extemporânea: \(campo novo da SAFX08\)

	Somente documentos não extemporâneos \(campo novo = “N”\)

SE for uma devolução: \(campo 04 da SAFX07 = “2 – Devolução”\)

	CFOP \(ou CFOP\+Natureza\):__\*\*__ \(campos 22 e 23 da SAFX08\)

		Deve estar relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de operação igual a “Devolução de Venda” ou “Devolução de Compra”

- Para um Documento Fiscal de Entrada \(Campo MOVTO\_E\_S <> 9\), além das regras gerais, considerar:

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.*  
*

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

- __SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS e CST COFINS: \(campos 175 e 178 da SAFX08/68 e 69 da X09\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\. Senão, considerar todos os CSTs\.

\[__MFS\-1876__\] Além dos CSTs indicados acima, considerar também registros cujo CST PIS ou CST COFINS sejam iguais a “98” ou “99”, desde que o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) esteja parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\)\.

Se o parâmetro for igual a “Sim”, considerar todos os CSTs\.

- Para um Documento Fiscal de Saída \(Campo MOVTO\_E\_S = 9\)\*\*, além das regras gerais, considerar:

Observar o parâmetro Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de Receita disponível na tela de Dados Iniciais\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Lançamento EFD PIS/COFINS’’__, o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08 ou campo 81 \- DAT\_LANC\_PIS\_COFINS da SAFX09\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Emissão”, o campo Data da Emissão__ \(campo 11 \- DATA\_EMISSAO da SAFX07\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

*Obs\. A Data de Lançamento PIS/COFINS poderá ser menor do que a Data de Emissão, está prevista legalmente esta situação\.*

__*Atenção: *__*O parâmetro “Registro A100, C100, C180 e C190 \- Seleção das Operações Geradoras de receita” é somente para documentos/operações de saídas, para documento/operações de entradas serão selecionados pela data do PIS e COFINS independentemente deste parâmetro\.*

__\*\*__ Devemos considerar que apenas os itens da NF que possuam CFOP \(ou CFOP\+Natureza\) relacionado no parâmetro “CFOP x Tipo de Operação” com tipo de operação igual a “Devolução de Venda” ou “Devolução de Compra”, serão considerados nesse registro\.

__\*\*\*__ Devemos considerar que se qualquer item da NF possuir CST <> de “70 \- Operação de Aquisição sem Direito a Crédito”, a NF será considera na verificação da regra de preenchimento 2 \(abaixo\)\.

__Regra de preenchimento 2 \(critérios para agrupamento\):__

SE parâmetro “Gera Itens sem Crédito = N”

	Serão considerados no agrupamento apenas os itens que possuam CST <> 70’’,’’71’’, ‘’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’

SENÃO \(parâmetro “Gera Itens sem Crédito = S”\)

	Todos os itens do documento devem ser considerados no agrupamento\.

__\*__ O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações dos itens desses documentos \(SAFX08\):

\- Data de Emissão dos Documentos

\- Código do Produto/Bem \(Indicador \+ Código do Produto ou Bem\)

\- Código NBM \(campo 26 da SAFX08 – Quando se tratar de um Produto ou Bem\)

__Obs\. 1:__ Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal \(SAFX08\), considerar o conteúdo desses campos informados na capa do documento \(SAFX07\)

\.

__Obs\. 2 : __Documentos fiscais de saída que serão gerados neste registro somente devolução de compra\. 

\[__OS4316\-A__\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\. 

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__Regra de preenchimento NF de Devolução de Compras:__

__\[MFS84559\] __

__Tratamento para Notas de Devolução de Compras:__

__Parâmetro Marcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas*__”, estiver __*marcado*__ o sistema deverá gerar as informações do Registro C191, referente a Nota Fiscal de Devolução de Compras conforme regras atuais\.

__Parâmetro Desmarcado:__ Se o parâmetro na tela de Dados Iniciais “__*Gerar NF’s de Devolução de Compras – Posterior a NF’s de Entradas”, *__estiver __*desmarcado*__, o sistema deverá desconsiderar as Notas Fiscais de Devolução de Compras, com a data, __*posterior*__ a Nota Fiscal de Entrada, conforme regras abaixo:

- Campo *MOVTO\_E\_S* igual à ‘9’ *\(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- Campo *NORM\_DEV* igual à ‘2’ *\(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- *Campo COD\_SITUACAO\_PIS igual à ‘49’ \(Tabelas DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\);*
- Campo *DAT\_LANC\_PIS\_COFINS* ou *DATA\_EMISSAO* > ao Campo *DAT\_DI* \(Considerar Mês/Ano na comparação\)\. *\(DWT\_DOCTO\_FISCAL / DWT\_ITENS\_MERC\); \(Conforme parâmetro na tela de Dados Iniciais Data Emissão ou Data Lançamento PIS e COFINS\)\.*

  

__Obs\.:__ A Data de Lançamento EFD PIS/COFINS ou a Data de Emissão da Nota de Devolução de Compras deverá ser posterior a data de escrituração da Nota Fiscal de Entrada\. 

Exemplo de NF de Devolução de Compras que não deve ser considerada:

Nota fiscal de Devolução de Compra escriturada em __01/2022\.__  
Nota fiscal de Entrada escriturada em __12/2021\.__

__*Atenção: *__Nessas mesmas condições desconsiderar os Registros filhos __*C191, C195, C198 e C199\.*__

 

Default: __Marcado__

__Importante:__ No caso da geração dos Registros C190 e filhos \(informações consolidadas\) o intuito é, se o parâmetro estiver *desmarcado*, serão desprezados __todos__ os registros filhos C191, C195, C198 e C199 *referente a NF de Devolução de Compras escriturada, posteriormente a NF de Entrada*, ou seja, as demais Notas serão geradas normalmente, __*exceto*__ se na consolidação do Registro C190 __*houver somente*__ Notas de Devolução de Compras \(data Posterior\), nesse caso o Registro C190 também deverá ser desprezado\.

__RNC190\-03__

Campo DT\_REF\_INI:

E 

Este campo deve ser preenchido com a data de Lançamento PIS/COFINS do primeiro documento fiscal agrupado, neste de registro\.

Para notas canceladas este campo não deverá ser informado\.

__RNC190\-04__

Campo DT\_REF\_FIN:

Este campo deve ser preenchido com a data de Lançamento PIS/COFINS do último documento fiscal agrupado neste registro\.

Para notas canceladas este campo não deverá ser informado\.

__RNC190\-05__

Campo COD\_ITEM:

Este campo deve ser preenchido com o produto \(SAFX2013\) ou Bem \(SAFX13\), informado no item de mercadoria da SAFX08 e com o serviço /natureza \(SAFX2018\), informado no item de serviço da SAFX09 das notas fiscais agrupadas\.

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver marcado:

Aplicar a mesma regra de concatenação já definida no registro 0200: 

Quando se tratar de serviço da SAFX2018, ao invés de gravar sempre o código do serviço, deve\-se verificar o novo parâmetro incluído na tela dos “Dados Inicias”, e seguir a regra:

  Se parâmetro = “Código do Serviço” à gravar o código do serviço \(campo 1 da SAFX2018\)

  Se parâmetro = “Natureza do Serviço” à gravar a natureza do serviço \(campo 8 da SAFX2018\)

Produtos da SAFX2013 à Indicador de Produto \+ "\-" \+ Código do produto

Serviços da SAFX2018  à "S"  \+  "\-"  \+  Código ou Natureza do Serviço

Bens da SAFX13         à "B" \+ "\-" \+ Código do Bem \+ "\-I" \+ Código Incorporador

Para notas canceladas este campo não deverá ser informado\.

Se parâmetro ‘Considerar o Indicador no Código do Item’, na tela de Dados Iniciais estiver desmarcado:

Quando se tratar de serviço da SAFX2018, ao invés de gravar sempre o código do serviço, deve\-se verificar o novo parâmetro incluído na tela dos “Dados Inicias”, e seguir a regra:

Se parâmetro = “Código do Serviço” à gravar o código do serviço \(campo 1 da SAFX2018\)

Se parâmetro = “Natureza do Serviço” à gravar a natureza do serviço \(campo 8 da SAFX2018\)

Quando se tratar de Bens da SAFX13:

Produtos da SAFX2013 à Código do produto

Serviços da SAFX2018 à Código ou Natureza do Serviço

Bens da SAFX13         à  Código do Bem 

Para notas canceladas este campo não deverá ser informado\.

__RNC190\-06__

Campo NCM:

Este campo deve ser preenchido com o código do NCM \(considerar as 8 primeiras posições\), informado no item de mercadoria da SAFX08 das notas fiscais agrupadas\.

Obs: Os NCM’s devem ser carregados para o campo 05\-COD\_NBM da tabela de produtos, pois o Mastersaf trabalha com a SAFX2043, que contém na verdade os NCM’s\.

Para notas canceladas este campo não deverá ser informado\.

__Alteração da MFS12767:__ A partir da vrs 2\.1\.1 do PVA, liberada em Ago/2017, o campo NCM passou a ser obrigatório\. Por isso, será feito o seguinte procedimento:

Caso o resultado da consolidação, conforme descrito na __RNG\-C180__, não tenha a informação do NCM, será verificado se o produto em questão é um Serviço ou não:

__Se__ o produto em questão for um serviço \(se TIPO\_ITEM gravado no registro 0200 for = “09”\):

     Nesse caso, este campo será gravado com o conteúdo “00”, conforme previsto no Guia Prático vrs 1\.22;

__Senão__

     Nesse caso será gravada a seguinte  mensagem de aviso no log: “*O campo 06\-NCM é obrigatório e não foi*

*     informado\. Verificar os movimentos consolidados para a data de emissão e produto*”\. O log deve informar

     nos dados de identificação a informação da Data de Emissão e do Indicador e Código Produto dos

     movimentos consolidados\.

__RNC190\-07__

Campo EX\_IPI:

Para notas canceladas este campo não deverá ser informado\.

__\[ALTERAÇÃO MFS\-642118\]__ Quando o campo 11\- EX\_IPI da SAFX2043 não estiver preenchido:

Este campo deve ser preenchido com os dois últimos dígitos do NCM nota fiscal agrupada, conforme a tabela básica SAFX2043, com o seguinte critério:

Quando se tratar de um produto da SAFX2013 à Preencher com os dois últimos dígitos do NCM do produto \(posições 9 e 10\)\. Quando estas posições estiverem com brancos, o campo não deve ser preenchido, pois o NCM não tem exceção\.

__\[ALTERAÇÃO MFS\-642118\]__ Quando o campo 11\- EX\_IPI da SAFX2043 estiver preenchido:

Considerar a informação do campo 11 – EX\_IPI da SAFX2043

__RNC190\-08__

Campo VL\_TOT\_ITEM:

Este campo deve ser preenchido com o somatório do valor contábil dos itens \(campo: 28/SAFX08 e 15/SAFX09 \) das notas fiscais agrupadas\.

Para notas canceladas este campo não deverá ser informado\.

__Registro C191 – Detalhamento da Consolidação – Operações de Aquisição e Devolução de Compras e Vendas PIS/PASEP__

__RNG\-C191__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C190 com base nas seguintes informações:

\- CPF/CNPJ \(campo 06 da SAFX04\)

\- Código de Situação Tributária PIS: \(campo 175 da SAFX08 e 68/SAFX09\)

\- CFOP: \(campo 22 da SAFX08 e 17/SAFX09\)

\- Alíquota do PIS: \(campo 129 ou 177 da SAFX08  e 47/SAFX09\)

\- Código da Conta Contábil: \(campo 105 da SAFX08 e 52/SAFX09\)

Na ausência do campo CPF/CNPJ \(campo 06 da SAFX04\), ou seja, o campo não estiver preenchido, como é o caso de Exterior, deverá considerar o Código do Participante \(campo 02 de SAFX04\) como critério de consolidação\.

__Ver Regra: RNG\-C190__ \(MFS84559 \- Regra de preenchimento NF de Devolução de Compras\)__ __

__RNC191\-02__

Campo CNPJ\_CPF\_PART

Este campo deve ser preenchido com o CNPJ ou CPF do Participante \(campo 06/SAFX04\)\. Na ausência desta informação, ou seja, o campo não estiver preenchido, deixar como fixo no campo: “99999999999999”, exceto quando o campo País \(campo 21/SAFX04\) for diferente do código ‘105’ – Brasil E o CNPJ ou CPF do Participante \(campo 06/SAFX04\) estiver sem preenchimento, o campo deve ser gerado com brancos\.

Será agrupado pela a combinação: CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC191\-05__

Campo VL\_ITEM:

Este campo deve ser preenchido com a somatória do valor dos itens \(campo: 28/SAFX08 e 15/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC191\-06__

Campo VL\_DESC:

Este campo deve ser preenchido com a somatória do valor dos descontos \(campo: 29/SAFX08 \+ 260\-VLR\_EXC\_BC\_PIS \+ 261\-VLR\_EXC\_BC\_COFINS e 21/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

\[__MFS\-48809__\]: alteração no preenchimento do campo, passando a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08\.

__RNC191\-07__

Campo VL\_BC\_PIS:

Este campo deve ser preenchido com a somatória do Valor da Base de Cálculo do PIS \(campo: 86/SAFX08 e 46/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

\[__MFS\-1876__\] Quando o CST PIS \(campo 175 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

__RNC191\-08__

Campo ALIQ\_PIS:

Este campo deve ser preenchido com a somatória do Valor da Alíquota do PIS \(campo: 129/SAFX08 e 47/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC191\-09__

Campo QUANT\_BC\_PIS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo do PIS – em Quantidade \(176/SAFX08\) das notas fiscais agrupadas no C180, pela a combinação CST PIS, CFOP, Alíquota do PIS e Código da Conta Contábil\.

__RNC191\-10__

Campo ALIQ\_PIS\_QUANT:

Este campo deve ser preenchido com a somatória do valor da Alíquota do PIS – em Reais \(87/SAFX08\) das notas fiscais agrupadas no C180, pela a combinação CST PIS, CFOP, Alíquota da PIS e Código da Conta Contábil

__RNC191\-11__

Campo VL\_PIS

\[__MFS\-1876__\] Quando o CST PIS \(campo 175 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

__Registro C195 – Detalhamento da Consolidação – Operações de Aquisição e Devolução de Compras e Vendas COFINS__

__RNG\-C195__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C190 com base nas seguintes informações:

\- CPF/CNPJ \(campo 06 da SAFX04\)

\- Código de Situação Tributária COFINS: \(campo 178 da SAFX08 e 69/SAFX09\)

\- CFOP: \(campo 22 da SAFX08 e 17/SAFX09\)

\- Alíquota da COFINS \(campo 130 ou 180 da SAFX08 e 50/SAFX09\)

\- Código da Conta: \(campo 105 da SAFX08 e 52/SAFX09\)

Na ausência do campo CPF/CNPJ \(campo 06 da SAFX04\), ou seja, o campo não estiver preenchido, como é o caso de Exterior, deverá considerar o Código do Participante \(campo 02 de SAFX04\) como critério de consolidação\.

__Ver Regra: RNG\-C190__ \(MFS84559 \- Regra de preenchimento NF de Devolução de Compras\)__ __

__RNC195\-02__

Campo CNPJ\_CPF\_PART:

Este campo deve ser preenchido com o CNPJ ou CPF do Participante \(campo 06/SAFX04\)\. Na ausência desta informação, ou seja, o campo não estiver preenchido, deixar como fixo no campo: “99999999999999”, exceto quando o campo País \(campo 21/SAFX04\) for diferente do código ‘105’ – Brasil E o CNPJ ou CPF do Participante \(campo 06/SAFX04\) estiver sem preenchimento, o campo deve ser gerado com brancos\.

Será agrupado pela a combinação:  CPF/CNPJ, CST PIS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC195\-05__

Campo VL\_ITEM:

Este campo deve ser preenchido com a somatória do valor dos itens \(campo: 28/SAFX08 e 15/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST COFINS, CFOP e Alíquota da COFINS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC195\-06__

Campo VL\_DESC:

Este campo deve ser preenchido com a somatória do valor dos descontos \(campo: 29/SAFX08 \+ 260\-VLR\_EXC\_BC\_PIS \+ 261\-VLR\_EXC\_BC\_COFINS e 21/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST COFINS, CFOP e Alíquota da COFINS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

\[__MFS\-48809__\]: alteração no preenchimento do campo, passando a considerar os campos 260 \- VLR\_EXC\_BC\_PIS e 261 \- VLR\_EXC\_BC\_COFINS da SAFX08\.

__RNC195\-07__

Campo VL\_BC\_COFINS:

Este campo deve ser preenchido com a somatória do Valor da Base de Cálculo da COFINS \(campo: 88/SAFX08 e 49/SAFX09\) das notas fiscais agrupadas no C190, pela a combinação: CPF/CNPJ, CST COFINS, CFOP e Alíquota da COFINS e Código da Conta Contábil\.

\[__MFS\-1876__\] Quando o CST COFINS \(campo 178 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

__RNC195\-08__

Campo ALIQ\_COFINS:

Este campo deve ser preenchido com a somatória do Valor da Alíquota da COFINS \(campo: 130/SAFX08 e 50/SAFX09\) das notas fiscais agrupadas no C190, pela combinação: CPF/CNPJ, CST COFINS, CFOP e Alíquota do PIS e Código da Conta Contábil, exceto quando o campo CPF/CNPJ estiver sem preenchimento, considerar o Código por Participante da SAFX04\.

__RNC195\-09__

Campo QUANT\_BC\_COFINS:

Este campo deve ser preenchido com a somatória do valor da Base de Cálculo do PIS – em Quantidade \(179/SAFX08\) das notas fiscais agrupadas no C180, pela combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil\.

__RNC195\-10__

Campo ALIQ\_PIS\_QUANT:

Este campo deve ser preenchido com a somatória do valor da Alíquota do PIS – em Reais \(/SAFX08\) das notas fiscais agrupadas no C180, pela combinação CST COFINS, CFOP, Alíquota da COFINS e Código da Conta Contábil\.

__RNC195\-11__

Campo VL\_COFINS

\[__MFS\-1876__\] Quando o CST COFINS \(campo 178 da SAFX08\) for igual a “98” ou “99” __E__ o CFOP ou CFOP \+ Natureza da NF \(campo 22 ou 22 \+ 23 da SAFX08\) estiver parametrizado na parametrização de Identificador do Tipo de Operação \(menu Parâmetros\) com Tipo de Operação igual a “1 – Devolução de Venda” __E__ que o Produto \(campos 13 e 14 da SAFX08\) ou NCM do Produto indicado NF \(campo 05 da SAFX2013\) tenha sido indicado na Parametrização por Produto ou por NCM \(Parâmetros >> Identificador Devolução de Venda \- Reg\. Cumulativo \(Segmento Cigarro\)\), este campo deve ser gerado com valor zero\.

__Registro C198 – Processo Referenciado__

__RNG\-C198__

Nesse registro devem ser gravados os registros da SAFX114 relacionados aos itens de documentos agrupados no registro C190, que atendam aos critérios abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS”

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

Nº Item da NF:

	Deve ser um dos itens agrupados no registro C190 correspondente, ou deve estar em branco\.

Dúvidas:

 1\- Criar indicador para diferenciar os processos referenciados do ICMS/IPI dos processos do PIS/COFINS nos registros da SAFX114?

__Resposta__: Criação de um campo para indicar que o processo se refere ao EFD PIS/COFINS

__Ver Regra: RNG\-C190__ \(MFS84559 \- Regra de preenchimento NF de Devolução de Compras\)__ __

__Registro C199 – Complemento do Documento – Operações de Importação \(Código 55\)__

__RNG\-C199__

Neste registro deverão ser gravadas as informações de importação da SAFX49 associadas aos documentos fiscais gravados no registro C190 e que atendam aos critérios abaixo:

Número do Item: \(campo 18 da SAFX08\)

	Igual ao número do item \(campo 13 da SAFX49\) da DI

__Obs\. 1: __Só devem ser considerados na geração desse registro os itens que tenham atendido à regra de geração das notas com item do registro C190\.

__Obs\. 2:__ Para cada nota fiscal podem existir “n” registros na SAFX49, já que as informações são discriminadas por DI e produto, então, o sistema deve agrupar os registros da SAFX49 por número de DI, totalizando os valores de PIS e COFINS, e gravar um registro para cada número de DI existente na X49\.

__Obs\.3:__ Para geração do Registro, C199, o Campo de IND\_PRODUTO e COD\_PRODUTO __é__ considerado na associação com a SAFX08\.

__Ver Regra: RNG\-C190__ \(MFS84559 \- Regra de preenchimento NF de Devolução de Compras\)__ __

__RNC199\-02__

Campo COD\_DOC\_IMP:

__*MFS\-25010*__*: Atendimento à versão 1\.29 do Guia Prático da EFD – Contribuições\.*

O código 2 \(Declaração Única de Importação\) só é válido para geração a partir de janeiro de 2019\. Antes desta data, o código não deve ser usado, ou seja, o registro não será gerado para o código 2\.

__RNC199\-03__

Campo NUM\_DOC\_IMP:

__*MFS\-22693*__*: Atendimento à versão 1\.28 do Guia Prático da EFD – Contribuições\.*

Esse campo passa a ter 15 posições e deve ser preenchido com o conteúdo do campo 04\-Número da DI da tabela SAFX49\.

__RNC199\-06__

Campo NUM\_ACDRAW:

Esse campo será a concatenação dos seguintes campos da SAFX49:

\[Alteração – OS 3489\]

Agencia do Ato Concessório \+ Ano do Ato Concessório \+ Nº do Ato Concessório \+ Dígito do Ato Concessório

