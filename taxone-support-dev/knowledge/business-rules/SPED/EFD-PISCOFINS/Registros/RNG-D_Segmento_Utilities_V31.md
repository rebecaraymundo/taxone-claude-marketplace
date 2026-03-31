# RNG-D_Segmento_Utilities_V31

- **Fonte:** RNG-D_Segmento_Utilities_V31.docx
- **Modificado:** 2026-03-18
- **Tamanho:** 89 KB

---

# EFD \- PIS/PASEP\-COFINS – SEGMENTO UTILITIES – V31

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

MFS\-605470

Rogério Ohashi

Alteração da regra do registro C500 para utilizar o novo parâmetro “Considerar valor de ICMS Não Escriturado no Campo 11 \- VL\_ICMS” para considerar o valor de ICMS Não Escriturado na composição do Campo 11 – VL\_ICMS\. 

19/02/2024

MFS\-713153

Rosemeire Santos

Inclusão CHV\_DOC\_E \(Chave do Documento Fiscal Eletrônico\) no Registro D500 

10/07/2025

MFS\-702267

Rafael Fabiano

Inclusão da nota fiscal modelo 62 NFCom nos registros D500 e D600

22/09/2025

MFS\-1042721

Andréa Rocha

Alteração das regras de geração dos campos 12 e 13 do registro D600 para o modelo 62\.  Essas regras devem seguir as mesmas regras definidas para os campos 11 e 12 do registro D750 do SPED\-EFD\.

13/02/2026

MFS\-1069400

Andréa Rocha

Alteração da geração do registro D600 para considerar os itens informativos para o o modelo 62\.

11/03/2026

## REGRAS DE NEGÓCIO

__Registro C500 – Nota Fiscal/Conta de Energia Elétrica \(Código 06\), Nota Fiscal de Energia Elétrica Eletrônica – NF3e \(Código 66\), Nota Fiscal/Conta de Fornecimento D’água Canalizada \(Código 29\), Nota Fiscal/Consumo fornecimento de Gás \(Código 28\) e NF\-e \(Código 55\) – Documentos de Entrada / Aquisição com Crédito__

<a id="_Hlk31188104"></a>__RNG\-C500__

Nesse registro devem ser gravadas as notas fiscais de entradas/aquisições de energia elétrica, gás e água que serão recuperados nas tabelas: SAFX07, SAFX08 e SAFX09\.

Gerar um registro C500 para cada documento fiscal que atenda aos critérios abaixo:

Filtro para as notas de Energia Elétrica:

Modelo: \(campo 13 da SAFX07\)

	Igual a “06”

Classificação: \(campo “12 – Classificação do documento” da SAFX07\) 

              Igual a “1 – Mercadoria” ou “3 – Mercadoria/Serviço’’

Movimento Entrada/Saída:

                 Diferente de “9”

Crédito/Contribuição Extemporânea: \(campo novo da SAFX08/SAFX09\)

	Item não extemporâneo \(campo novo = “N”\)

__ \[ALTERAÇÃO – CH28382 / CH6594/2015 / OS4816\]__

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Para notas fiscais sem item, considerar apenas o critério de seleção da data de lançamento da capa, independente do critério indicado no parâmetro

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

__SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS ou CST COFINS \(campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\. Senão, considerar todos os CSTs\.

Filtro para as __notas fiscais eletrônica__ de Energia Elétrica:

\[MFS31702\] – Inclusão do modelo 66 e do campo 15

Modelo: \(campo 13 da SAFX07\)

	Igual a “55” ou “66”

Classificação: \(campo “12 – Classificação do documento” da SAFX07\) 

              Igual a “1 – Mercadoria” ou “3 – Mercadoria/Serviço’’

Movimento Entrada/Saída:

                 Diferente de “9”

CFOP \(ou CFOP\+Natureza\)__\*\*__ \(campos 22 e 23 da SAFX08\)

Crédito/Contribuição Extemporânea: \(campo novo da SAFX08/SAFX09\)

	Item não extemporâneo \(campo novo = “N”\)

__\[ALTERAÇÃO – CH28382 / CH6594/2015 / OS4816\]__

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Para notas fiscais sem item, considerar apenas o critério de seleção da data de lançamento da capa, independente do critério indicado no parâmetro

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

__SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS ou CST COFINS \(campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\. Senão, considerar todos os CSTs\.

\[__CH7788/2015__\]

__\*\*__ Devemos considerar que apenas os itens da NF que possuam CFOP \(ou CFOP\+Natureza\) relacionado nos parâmetros “Por CFOP” ou “Por Extensão CFOP”\. Se ao menos um dos itens da NF tiver o CFOP parametrizado, este grupo de registros \(C500 e filhos\) será gerado em função deste item, demonstrando informações considerando o item \(ou itens\) com CFOP parametrizado\.

Caminho: SPED → EFD PIS/PASEP – COFINS →Parâmetros → Registro C500→ Por CFOP e Por Extensão CFOP

Filtro para as notas de Gás: 

Modelo: \(campo 13 da SAFX07\)

	Igual a “28”

    OU:        

             SE Pessoa fis/jur \(campo 07 da SAFX07\), estiver parametrizada como ‘’Fornecedores de Gás Canalizado’’, através no módulo DW, menu: Manutenção 🡪 Cadastro de Parâmetro 🡪 Pessoa Física/Jurídica por Ramo de Atividade 

__Obs1__:

\- Independente de modelo utilizado nestas notas, elas deverão ser gravadas com modelo = “28”; 

\- Demais critérios são os mesmos descritos para as notas de Energia Elétrica\.

CH2213\_2018  \- MFS16601

Filtro para as notas de Água: 

Modelo: \(campo 13 da SAFX07\)

	Igual a “29”

      OU:        

            Modelo: \(campo 13 da SAFX07\)

	     Igual a “29”  

                       E 

                          SE a empresa é do segmento de água \(verificar através do CNAE que deve = 4100901,3600601, 3600602\)

__Obs2:__

\- Independente do modelo utilizado nestas notas \(01 ou 29\), considerar para o Sped o código = “29”; 

\- Demais critérios são os mesmos descritos para as notas de Energia Elétrica\.

__Obs 3: __Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal \(SAFX08\), considerar o conteúdo desses campos informados na capa do documento \(SAFX07\)\.

__Importante:__ Se uma determinada nota for parametrizada para ser gerada no C500, a mesma não deve ser considerada no C100 e 190\.

__Atenção:__

__\*Tratamento especial para notas canceladas:__

Quando se tratar de NF cancelada \(campo “30\-Situação da nota” = “S”\) somente poderá ser informado os campos IND\_OPER, campo IND\_EMIT, campo COD\_SIT, campo SER, Campo SUB  e campo NUM\_DOC\. Não deverão ser informados registros filhos\. 

Não deverão ser informados registros filhos\. 

Notas/Contas de Fornecimento de Gás \(Entradas\):

- As contas de fornecimento de Gás \(entradas\) emitidas pelas empresas concessionárias *não devem ser consideradas* para a geração do C100\. O motivo é o mesmo descrito acima, o problema do modelo “28” ainda não ter sido oficialmente tratado no Convênio ICMS\. Estas notas serão identificadas pela parametrização de Pessoas Fis/Jur x Ramo de Atividade, que deverá ser = “Fornecedores de Gás Canalizado”;

Para geração desse registro estamos considerando que não existe devolução desse tipo de nota e não existem notas \(mesmo que complementares\) sem item\.

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__RNC500\-02__

Campo COD\_PART:

Para notas canceladas este campo não deverá ser informado\.

\[OS4751\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__RNC500\-03__

Campo COD\_MOD:

Para notas canceladas este campo deverá ser informado\.

__RNC500\-04__

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica, verificar:

     se a nota foi denegada        🡪 gravar “04”

     se a nota foi  ou inutilizada 🡪 gravar “05”

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

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

A lógica seria a seguinte:

__Se__ nota é eletrônica e foi  \(denegada ou inutilizada\)

        __Se__ nota é denegada

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

Nota cancelada 🡪 campo “30\-Situação da nota” =  “S”;

Nota complementar 🡪 campo “125\-Situação Especial” = “5”;

Nota Eletrônica 🡪 campo “13\-Modelo de Documento” =  “57” e campo “13\-Modelo de Documento” =  “55”;

	

Nota Eletrônica denegada 🡪 campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “1” \(denegada\);

Nota Eletrônica inutilizada 🡪 campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “2” \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc 🡪 o campo “232\-NF Baseada em Regime Especial ou Norma Específica” será = “S”\.

__RNC500\-05__

Campo SER:

Para notas canceladas este campo deverá ser informado\.

__RNC500\-06__

Campo SUB:

Para notas canceladas este campo deverá ser informado\.

__RNC500\-07__

Campo NUM\_DOC:

Este campo deve ser preenchido com o número do documento fiscal \(campo 08/SAFX07\)\. Na ausência desta informação, ou seja, o campo não estiver preenchido, deixar como fixo “000000000”\.

Para notas canceladas este campo deverá ser informado\.

__RNC500\-08__

Campo DT\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RNC500\-09__

Campo DT\_ENT:

Para notas canceladas este campo não deverá ser informado\.

__RNC500\-10__

Campo VL\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RNC500\-11__

Campo VL\_ICMS:

\[__ALTERAÇÃO\-MFS605470__\] Tratamento p/ Valor de ICMS para considerar o valor de ICMS Não Escriturado\.

__Tratamento:__

__Parâmetro Marcado:__ Se o parâmetro na tela de Dados Iniciais “__*Considerar valor de ICMS Não Escriturado no Campo 11 \- VL\_ICMS”, *__estiver __*marcado*__*, *preencher conforme regra abaixo: 

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “43\-Valor do ICMS” da SAFX08 \+ o campo “80\- VLR\_ICMS\_NDESTAC”\.

Para notas canceladas este campo não deverá ser informado\.

__Parâmetro Desmarcado:__ Se o parâmetro na tela de Dados Iniciais __*“Considerar valor de ICMS Não Escriturado no Campo 11 \- VL\_ICMS” *__estiver __*desmarcado*__, preencher conforme regra abaixo: \(Conforme regra atuais\)\.

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “43\-Valor do ICMS” da SAFX08

Para notas canceladas este campo não deverá ser informado\.

__RNC500\-12__

Campo COD\_INF:

__\[MFS605194\] Inclusão da regra para nota de entrada__

__Para notas de entrada__ à Recuperar a informação do campo 178 – Código da Observação da SAFX07\.

Se o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

Se o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

__RNC500\-13__

Campo VL\_PIS:

Para notas canceladas este campo não deverá ser informado\.

__RNC500\-14__

Campo VL\_COFINS:

Aplicar a mesma regra descrita para o campo 11\-VL\_ICMS, considerando os campos do valor da COFINS \(conforme a planilha de\-para\)\.

No caso da COFINS, ao totalizar os itens deve\-se considerar também os itens de serviço da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

<a id="_Hlk31188127"></a>__RNC500\-15__

\[MFS31702\] – Inclusão do modelo 66 e do campo 15

´

Campo CHV\_DOCe

Preencher com o campo 226 \- Chave de Acesso da NF\-Eletrônica da SAFX07\.

Obs\.: Este campo é obrigatório quando o campo COD\_MOD for igual a “66” ou “55”, a partir de 01/01/2020\.

	

__                   Registro C501 \- Complemento da Operação \(Códigos 06, 28, e 29\) – PIS/PASEP__

__RNG\-C501__

Consolidar as informações dos itens dos documentos fiscais que passaram pelas regras de geração do registro C500, de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N” \(parâmetro da tela de geração\)

	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ‘’71’’, ’’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’\.

SENÃO \(parâmetro “Gera Itens sem Crédito = S”\)

	Todos os itens do documento devem ser considerados no agrupamento\.

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária PIS: \(campo 175 da SAFX08/68 da SAFX09\)

\- Código da Natureza da Base de Cálculo do Crédito

\- Alíquota do PIS: \(campo 129 da SAFX08/47 da SAFX09\)

\- Código da Conta Contábil: \(campo 105 da SAFX08/52 da SAFX09\)

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

__RNC501\-02__

Campo CST\_PIS:

Notas com item 🡪 campo 175 da SAFX08 ou campo 68 da SAFX09\.

__RNC501\-03__

Campo VL\_ITEM:

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08 e do campo 15 \(Valor Total do Serviço\) da SAFX09 

__RNC501\-04__

Campo NAT\_BC\_CRED:

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver marcado \(nos dados iniciais\):

Gravar o conteúdo do campo Natureza da Base de Crédito \(campo novo da SAFX08/SAFX09\) informada no documento fiscal

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver desmarcado \(nos dados iniciais\):

Gravar o código da natureza da base de crédito que consta na TACES X “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP \(campo 22 da SAFX08 – campo 17 da SAFX09\) informado no documento fiscal\. 

__*Incluir crítica no log do processo:*__

__*Origem:*__

O novo campo Natureza da Base de Crédito na SAFX08 ou SAFX09 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

__*Mensagem:*__

O campo NAT\_BC\_CRED é de preenchimento obrigatório, quando o parâmetro ’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

__RNC501\-05__

Campo VL\_BC\_PIS:

Notas com item 🡪 somatório do campo 86 da SAFX08 e campo 46 da SAFX09\. Caso não existir informação neste campo, deve gravar zero |0|\.

__RNC501\-06__

Campo ALIQ\_PIS:

Notas com item 🡪 somatório do campo 129 da SAFX08 e campo 47 da SAFX09\. Caso não existir informação neste campo, deve gravar zero |0|\.

__RNC501\-07__

Campo VL\_PIS:

Notas com item 🡪 somatório do campo 87 da SAFX08 e campo 48 da SAFX09\. Caso não existir informação neste campo, deve gravar zero |0|\.

  


__                   Registro C505 \- Complemento da Operação \(Códigos 06, 28, e 29\) – COFINS__

__RNG\-C505__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C500 de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N”: \(parâmetro da tela de geração\)

	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ‘’71’’, ‘’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’

SENÃO \(parâmetro “Gera Itens sem Crédito = S”\)

	Todos os itens do documento devem ser considerados no agrupamento\.

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária COFINS: \(campo 178 da SAFX08/69 da SAFX09\)

\- Código da Natureza da Base de Cálculo do Crédito

\- Alíquota da COFINS \(campo 130 da SAFX08/50 da SAFX09\)

\- Código da Conta: \(campo 105 da SAFX08\-52 da SAFX09\)

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

__RNC505\-02__

Campo CST\_COFINS:

Notas com item 🡪 campo 178 da SAFX08 ou campo 69 da SAFX09\.

__RNC505\-03__

Campo VL\_ITEM:

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08 e do campo 15 \(Valor Total do Serviço\) da SAFX09

__RNC505\-04__

Campo NAT\_BC\_CRED:

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver marcado \(nos dados iniciais\):

Gravar o conteúdo do campo Natureza da Base de Crédito \(campo novo da SAFX08/SAFX09\) informada no documento fiscal

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver desmarcado \(nos dados iniciais\):

Gravar o código da natureza da base de crédito que consta na TACES X “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP \(campo 22 da SAFX08 – campo 17 da SAFX09\) informado no documento fiscal\. 

__*Incluir crítica no log do processo:*__

__*Origem:*__

O novo campo Natureza da Base de Crédito na SAFX08 ou SAFX09 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

__*Mensagem:*__

O campo NAT\_BC\_CRED é de preenchimento obrigatório, quando o parâmetro ’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

__RNC505\-05__

Campo VL\_BC\_COFINS:

Notas com item 🡪 somatório do campo 88 da SAFX08 e campo 49 da SAFX09\. Caso não existir informação neste campo, deve gravar zero |0|\.

__RNC505\-06__

Campo ALIQ\_COFINS:

Notas com item 🡪 somatório do campo 130 da SAFX08 e campo 50 da SAFX09\. Caso não existir informação neste campo, deve gravar zero |0|\.

__RNC505\-07__

Campo VL\_COFINS:

Notas com item 🡪 somatório do campo 89 da SAFX08 e campo 51 da SAFX09\. Caso não existir informação neste, deve gravar zero |0|\.

__Registro C600 – Consolidação Diária de Notas Fiscais/Contas Emitidas de Energia Elétrica \(Código 06\), Nota Fiscal de Energia Elétrica Eletrônica – NF3e \(Código 66\), Nota Fiscal/Conta de Fornecimento D'água Canalizada \(Código 29\) e Nota Fiscal/Conta de Fornecimento de Gás \(Código 28\) \(Empresas Obrigadas ou não Obrigadas ao Convenio ICMS 115/03\) – Documentos de Saída__

__RNC600__ 

Os registros do sub\-bloco “C600” \(C600, C601 e C605\) serão gerados a partir da consolidação das notas fiscais de saída\. A origem destes registros é a mesma do sub\-bloco C500, com a diferença que no C600 o movimento será consolidado;

As notas canceladas também devem ser consideradas na consolidação \(por causa dos campos 07 e 08, que registram a quantidade das notas consolidadas e canceladas por critério de consolidação, ou seja, por modelo, município e demais campo chave da consolidação\)\. Mas os valores destas notas devem ser considerados como zero\.

Caso os campos 07 e 08 sejam iguais, ou seja, quando só for consolidado documentos cancelados, os campos 10 \-  VL\_DOC , 21 \-  VL\_PIS  e 22\-  VL\_COFINS obrigatoriamente devem ser gerados com zero\. Os demais campos se maiores ou iguais a  zero preencher com zero, caso contrário ||\.

Se flag “Geração com base nas informações da SAFX190 e SAFX191” = desmarcado 

Para geração destes registros o movimento da SAFX42 deverá ser consolidado pelos seguintes critérios:

- Modelo 
- Município dos Terminais Faturados \(campo 76 da SAFX42\)
- Série \(campo 07 da SAFX42\)
- Subsérie \(campo 08 da SAFX42\)
- Classe de Consumo \(campo 63 da SAFX42\)

Assim, as notas emitidas no período que tenham o mesmo modelo, município faturado, série/subsérie e classe de consumo irão gerar um único registro C600\.

Critérios de seleção das notas:

       Filtro para as notas de Energia Elétrica: 

__\[MFS33637\] – Inclusão do modelo 66__

- Modelo \(campo “13 – Modelo de Documento”\) = 06 ou “66”;
- Data de Emissão \(campo 03\) \- enquadrada no período de geração
- __CH 10929__ \- Não considerar os itens informativos \(itens da SAFX43 com o campo 10\-Tipo de Item = 1\)

        Filtro para as notas de Gás: 

- \[Modelo \(campo “13 – Modelo de Documento”\) = 28\]    OU

                 \[Modelo \(campo “13 – Modelo de Documento”\) = 01 e Empresa é do segmento 

                 de Gás \(verificar através do CNAE que deve ser = 4020701, 4020702, 3520401 

                 ou 3520402\)\]

- Independente do modelo utilizado nestas notas \(01 ou 28\), considerar para o EDF\-Pis/Cofins o código = “28”; 
- Demais critérios são os mesmos descritos para as notas de Energia Elétrica;

CH2213\_2018  \- MFS16601

        Filtro para as notas de Água: 

- \[Modelo \(campo “13 – Modelo de Documento”\) = 29\]    OU

                 \[Modelo \(campo “13 – Modelo de Documento”\) = 01 e Empresa é do segmento 

                 de Água \(verificar através do CNAE que deve ser = 4100901, 3600601, 3600602\)\]

- Independente do modelo utilizado nestas notas \(01 ou 29\), considerar para o EFD\-Pis/Cofins o código = “29”; 
- Demais critérios são os mesmos descritos para as notas de Energia Elétrica;

\(Obs: o “ou” deve ser utilizado, pois, assim que o modelo 28 for incluído na lista de modelos do Convênio ICMS, os usuários poderão utilizá\-lo\)\.

__\[MFS29621\]__

        Filtro para as notas fiscais da SAFX07/SAFX08/SAFX09:

        \- Modelo \(campo 13 da SAFX07 = “01 ou 55”\)

        \- Classificação \(campo “12 – Classificação do documento” da SAFX07\) igual a “1 – Mercadoria” ou “3   

           – Mercadoria/Serviço’’

         \- Movimento Entrada/Saída \(campo 13 da SAFX07 = “9”\)

         \- Crédito/Contribuição Extemporânea \(campo 197 da SAFX08 = “N” ou campo 82 da SAFX09\): Item não extemporâneo 

         \- Devemos considerar apenas as NFs que possuam CFOP \(ou CFOP\+Natureza\) relacionado nos parâmetros “Por CFOP” ou “Por Extensão CFOP”\. Se ao menos um dos itens da NF tiver o CFOP parametrizado, este grupo de registros \(C600 e filhos\) será gerado em função deste item, demonstrando informações considerando o item \(ou itens\) com CFOP parametrizado\.

Item de menu: SPED → EFD PIS/PASEP – COFINS →Parâmetros → Registro C600→ Por CFOP e Por <a id="_Hlk17106523"></a>Extensão CFOP\.

         Verificar o parâmetro Registro A100, C100, C180, C190 e C600 \- Seleção das Operações Geradoras de Receita disponível na tela de Dados Iniciais:

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Lançamento EFD PIS/COFINS’’__, o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08 ou campo 81 \- DAT\_LANC\_PIS\_COFINS da SAFX09\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

__Se o parâmetro estiver preenchido com conteúdo igual a ‘’Data de Emissão”, o campo Data da Emissão__ \(campo 11 \- DATA\_EMISSAO da SAFX07\) deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

Para geração destes registros o movimento da SAFX07/SAFX08/SAFX09 deverá ser consolidado pelos seguintes critérios:

- Modelo \(campo 13 da SAFX07\)
- Município dos Terminais Faturados \(campo 208 da SAFX07\)
- Série \(campo 09 da SAFX07\)
- Subsérie \(campo 10 da SAFX07\)
- Classe de Consumo \(campo 195 da SAFX07\)

Preencher os campos de acordo com regras especificadas no item “Geração via SAFX190/SAFX191”\.

Deverá gerar uma linha de registro no C600 obedecendo ao critério de seleção das tabelas __SAFX42/43 __ou__ SAFX190__\. Os campos serão preenchidos de acordo com o conteúdo disponibilizado nos campos chaves e demais campos\.

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

RNC600\-02

Campo COD\_MOD:

\(observar critérios de recuperação das notas na regra RNC600\)

\[MFS29621\]

\[MFS33637\] – Inclusão do modelo 66

Notas recuperadas através dos modelos “06” \(EE\) ou “28” \(Gás\) ou “29” \(Água\) ou “55” \(NFe\) ou “66”  \(NF3e\): 

- preencher com o próprio código do modelo \(06, 28, 29, 55 ou 66\);

Notas recuperadas através do modelo “01”:

- Se conta de Gás 🡪 preencher com o código 28;
- Se conta de Água 🡪 preencher com o código 29;

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  o Código do Modelo \(campo 03 da SAFX190\)

RNC600\-06

Campo COD\_CONS:

	

\[Alteração OS 3744\]

 Para as notas fiscais de energia elétrica \(modelo 06\), preencher o campo conforme DE\-PARA abaixo:

Se classe de consumo = '00', '01', '02', '03', '04',’06’ grava registro com informação '06'\.

Se classe de consumo = '20', '21', grava registro com informação '04'\.

Se classe de consumo= '40', '41', grava registro com informação '01'\.

Se classe de consumo= '60', '61', ‘07’ grava registro com informação '07'\.

Se classe de consumo= '70', ‘05’ grava registro com informação '05'\.

Se classe de consumo= '71', grava registro com informação '03'\.

Se classe de consumo= '72',’08’ grava registro com informação '08'\.

Se classe de consumo= '80', grava registro com informação '02'\.

Se classe de consumo= '90', grava registro com informação '90' \(não tem código novo de mesma definição\)\.

Se classe de consumo= '99', grava registro com informação '99' \(não tem código novo de mesma definição\)\.

__Alteração – MFS5904__ \(o De\-Para p/o segmento de EE *não* será mais utilizado\)

Para as notas fiscais de energia elétrica \(__modelo 06 e 55__\), o campo será preenchido normalmente, a partir do conteúdo do campo classe de consumo do documento\.

*Caso a NF seja de água \(modelo 28\) ou gás \(modelo 29\) a classe deve ser aquela informada na NF\.*

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  o Código de Classe de Consumo \(campo 08 da SAFX190\)

RNC600\-07

Campo QTD\_CONS:

Este campo é o contador dos registros que foram consolidados no Registro C600\.

Utilizando o mesmo critério de seleção da RNC600, neste campo deverá ser apresentada a quantidade de documentos fiscais selecionados para o registro\.

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  a Quantidade dos Documentos Consolidados \(campo 10 da SAFX190\)

RNC600\-08

Campo QTD\_CANC:

\[MFS29621\]

Este campo é o contador dos documentos cancelados \(campo 21\- SITUACAO da SAFX42  ou campo 30  SITUACAO da SAFX07  igual a “S”\) que se enquadram da consolidação\.

Utilizando o mesmo critério de seleção da RNC600, neste campo deverá ser apresentada a quantidade de documentos cancelados no registro C600\.

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  a  Quantidade dos Documentos Cancelados \(campo 11 da SAFX190\)

RNC600\-13

Campo VL\_FORN:

\[MFS29621\]

Totalização do valor do produto/serviço \(campo 22 da SAFX07 ou campo 28 da SAFX08 ou campo 14 da SAFX09 ou campo 19 da SAFX43\) dos documentos consolidados de acordo com a RNC600\.

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com o  Valor acumulado do fornecimento \(campo 15 da SAFX190\)

RNC600\-14

Campo VL\_SERV\_NT:

Totalização do valor dos serviços não tributados pelo ICMS dos documentos consolidados de acordo com a RNC600:

Valor das bases isenta/não tributada \+ base outras \+ base de redução dos *itens de mercadoria* da __SAFX43 __\+ valor do serviço dos *itens de serviço* da __SAFX43__:

\[campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras \+ campo 26\-Base de Redução dos itens de mercadoria \(campo 47 = “1”\) \]  \+ \[campo 19\-Valor do Serviço dos itens de serviço \(campo 47 = “2”\) \]

\[MFS29621\]

Notas *sem  *item

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX07__:

\[campos 52 \+ 53 \+ 54\]

Notas *com*  itens 

\(Classificação = “1”\)

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__:

\[ campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\) \]

Notas *mistas* \(itens na X08 e X09\)

\(Classificação = “3”\) 

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__ \+ valor dos itens de serviço da __SAFX09__:

\[campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\)\] da SAFX08  \+  campo 14 da SAFX09

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  o Valor acumulado dos serviços não\-tributados pelo ICMS \(campo 16 da SAFX190\)

RNC600\-15

Campo VL\_TERC:

Totalização do valor de terceiros dos documentos consolidados de acordo com a RNC600\. Totalizar sempre pelos itens, já que as notas de Utilities sempre têm itens\.

Campo 75\-Valor de Terceiros da tabela SAFX43\.

\[MFS29621\]

Campo 215\-Valor de Terceiros  da tabela SAFX07 /164\-Valor de Terceiros  da tabela SAFX08\.

Geração via SAFX190/SAFX191:

Este campo deve ser preenchido com  os Valores cobrados em nome de terceiros \(campo 17 da SAFX190\)

  


__Registro C601 – COMPLEMENTO DA CONSOLIDAÇÃO DIÁRIA \(CÓDIGOS 06, 28 e 29\) – DOCUMENTOS DE SAÍDAS \- PIS/PASEP__

__RNG\-C601__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C600\.

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária PIS: \(campo novo da SAFX43\)

\- Alíquota do PIS: \(campo 79 da SAFX43\)

\- Código da Conta Contábil: \(campo 53 da SAFX43\)

Geração via SAFX07/SAFX08/SAFX09

\- Código de Situação Tributária PIS: \(campo 249 da SAFX07\)

\- Alíquota do PIS: \(campo 164 da SAFX07\)

\- Código da Conta Contábil: \(campo 33 da SAFX07\)

Geração via SAFX190/SAFX191:

\- Código de Situação Tributária PIS: \(campo 11 da SAFX191\)

\- Alíquota do PIS: \(campo 13 da SAFX191\)

\- Código da Conta Contábil: \(campo 19 da SAFX191\)

  
__Apenas notas Canceladas__

Quando no registro pai C600, os campos 07 e 08 sejam iguais, ou seja, quando só for consolidado documentos cancelados, os campos 03\- VL\_ITEM, 04\- VL\_BC\_PIS e 06\- VL\_PIS devem ser gerados com zero\. O campo 05\- ALIQ\_PIS deve ser gerado com o valor da alíquota\.

__Registro C605 – COMPLEMENTO DA CONSOLIDAÇÃO DIÁRIA \(CÓDIGOS  06, 28 e 29\) – DOCUMENTOS DE SAÍDAS – COFINS__

__RNG\-C605__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C600 de acordo com a seguinte regra:

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária COFINS: \(campo novo da SAFX43\)

\- Alíquota da COFINS \(campo 82 da SAFX43\)

\- Código da Conta: \(campo 53 da SAFX43\)

Geração via SAFX07/SAFX08/SAFX09

\- Código de Situação Tributária COFINS: \(campo 250 da SAFX07\)

\- Alíquota da COFINS: \(campo 165 da SAFX07\)

\- Código da Conta Contábil: \(campo 33 da SAFX07\)

Geração via SAFX190/SAFX191:

\- Código de Situação Tributária COFINS: \(campo 15 da SAFX191\)

\- Alíquota da COFINS \(campo 17 da SAFX191\)

\- Código da Conta: \(campo 19 da SAFX191\)

__Apenas notas Canceladas__

Quando no registro pai C600, os campos 07 e 08 sejam iguais, ou seja, quando só for consolidado documentos cancelados, os campos 03\- VL\_ITEM, 04\- VL\_BC\_COFINS e 06\- VL\_COFINS devem ser gerados com zero\. O campo 05\- ALIQ\_COFINS deve ser gerado com o valor da alíquota\.

__Registro D500 \- NF DE COMUNICAÇÃO \(CÓDIGO 21\), NOTA FISCAL DE SERVIÇO DE TELECOMUNICAÇÃO \(CÓDIGO 22\) E NOTA FISCAL DE SERVIÇO DE COMUNICAÇÃO/TELECOMUNICAÇÕES MODELO 62 – AQUISIÇÃO COM DIREITO A CRÉDITO__

__RNG\-D500__

Nesse registro devem ser gravadas as notas fiscais de entradas/aquisições de Comunicação e Serviço Telecomunicação que serão recuperados nas tabelas: SAFX07, SAFX08 e SAFX09\.

Gerar um registro D500 para cada documento fiscal que atenda aos critérios abaixo:

Filtro para as notas de Energia Elétrica:

Modelo: \(campo 13 da SAFX07\)

	Igual a ‘’21, ‘‘22” e “62”

Classificação: \(campo “12 – Classificação do documento” da SAFX07\) 

              Igual a “1 – Mercadoria” ou “3 – Mercadoria/Serviço’’

Movimento Entrada/Saída:

                 Diferente de “9”

Crédito/Contribuição Extemporânea: \(campo novo da SAFX08/SAFX09\)

	Item não extemporâneo \(campo novo = “N”\)

__\[ALTERAÇÃO – CH28382 / CH6594/2015 / OS4816\]__

__Data de Lançamento PIS/COFINS:__ o campo Data do Lançamento \(campo 247 \- DAT\_LANC\_PIS\_COFINS da SAFX07 ou campo 196 \- DAT\_LANC\_PIS\_COFINS da SAFX08\)\* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo\.

\* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 \- Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais\.

__Se no parâmetro indicado for preenchida a opção “Capa NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07\.

__Se no parâmetro indicado for preenchida a opção “Item NF”__, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08\. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada\.

Para notas fiscais sem item, considerar apenas o critério de seleção da data de lançamento da capa, independente do critério indicado no parâmetro

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional\.

*Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada\.*

__SE parâmetro Gera NF’s de Entrada sem Crédito = “Não”__ \(parâmetro da tela de geração\), considerar apenas registros cujo CST PIS ou CST COFINS \(campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07\) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67\. Senão, considerar todos os CSTs\.

__Tratamento especial para notas canceladas:__

Quando se tratar de NF cancelada \(campo “30\-Situação da nota” = “S”\) somente poderá ser informado os campos IND\_OPER, campo IND\_EMIT, campo COD\_SIT, campo SER, Campo SUB e campo NUM\_DOC\. Não deverão ser informados registros filhos\. 

Não deverão ser informados registros filhos\. 

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__RND500\-03__

Campo IND\_EMIT:

A partir do conteúdo do indicador de Entrada/Saída da nota \(campo 03\-Movimento Entrada/Saída da SAFX07\), verificar:

Se indicador de movimento E/S = 1 🡪 gravar 1 \(emissão terceiros\)

Se indicador de movimento E/S = 2,3,4 ou 5 🡪 gravar 0 \(emissão própria\)

__RND500\-04__

Campo COD\_PART:

Para notas canceladas este campo não deverá ser informado\.

\[OS4751\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__RND500\-05__

Campo COD\_MOD:

Para notas canceladas este campo deverá ser informado\.

__RND500\-06__

Campo COD\_SIT:

Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:

Se for nota eletrônica, verificar:

     se a nota foi denegada        🡪 gravar “04”

     se a nota foi  ou inutilizada 🡪 gravar “05”

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

Os testes devem ser executados exatamente nesta prioridade\. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto *não ocorrer*, será gravado o conteúdo “00”\.

A lógica seria a seguinte:

__Se__ nota é eletrônica e foi  \(denegada ou inutilizada\)

        __Se__ nota é denegada

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

Nota cancelada 🡪 campo “30\-Situação da nota” =  “S”;

Nota complementar 🡪 campo “125\-Situação Especial” = “5”;

Nota Eletrônica 🡪 campo “13\-Modelo de Documento” =  “57”;

Nota Eletrônica denegada 🡪 campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “1” \(denegada\);

Nota Eletrônica inutilizada 🡪 campo “13\-Modelo de Documento” =  “57” e o campo “231\-Nfe Denegada/Inutilizada” = “2” \(inutilizada\);

Nota com Ato Normativo, Regime Especial etc 🡪 o campo “232\-NF Baseada em Regime Especial ou Norma Específica” será = “S”\.

__RND500\-07__

Campo SER:

 Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

__RND500\-08__

Campo SUB:

 Para notas canceladas e campo “IND\_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado\.

__RND500\-08__

Campo NUM\_DOC: 

Para notas canceladas e campo “IND\_EMIT” igual a “1”  ou igual “0”, este campo deverá ser informado\.

__RND500\-10__

Campo DT\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RND500\-11__

Campo DT\_A\_P:

Para notas canceladas este campo não deverá ser informado\.

__RND500\-12__

Campo VL\_DOC:

Para notas canceladas este campo não deverá ser informado\.

__RND500\-13__

Campo VL\_DESC:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o valor do desconto da SAFX07 \(campo 28\-Valor Descontos\);

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-14__

Campo VL\_SERV:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o valor do produto da SAFX07 \(campo 22\-VLR\_PRODUTO\)

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “ 28\-Valor do Item” da SAFX08, e “14\-Valor do Serviço” da SAFX09\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-15__

Campo VL\_SERV\_NT: valor dos serviços não tributados pelo ICMS

Para as notas de entrada 🡪__ __este valor será composto pela soma das bases isenta/outras/redução\. Para as notas de mercadoria será a soma destas bases, seja da capa \(notas sem item\), ou dos itens da SAFX08\. Para as notas mistas será a soma dos itens de mercadoria da SAFX08 \+ o valor dos serviços da SAFX09\.

Notas *sem  *item

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX07__:

\[campos 52 \+ 53 \+ 54\]

Notas *com*  itens 

\(Classificação = “1”\)

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__:

\[ campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\) \]

Notas *mistas* \(itens na X08 e X09\)

\(Classificação = “3”\) 

Valor das bases isenta/não tributada \+ base outras \+ base de redução da __SAFX08__ \+ valor dos itens de serviço da __SAFX09__:

\[campos 56 \(se campo 55 = 2 ou 3\)  \+ campo 57 \+ campo 83 \(se campo 82 = 2 ou 3\)\] da SAFX08  \+  campo 14 da SAFX09

Para notas canceladas este campo não deverá ser informado\.

__RND500\-16__

Campo VL\_TERC:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o valor do produto da SAFX07 \(campo 215\-VLR\_TERCEIROS\)

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “164\-Valor de Terceiros” da SAFX08\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-17__

Campo VL\_DA:

Para notas canceladas este campo não deverá ser informado\.

__RND500\-18__

Campo VL\_BC\_ICMS:

Para as notas *sem* itens 🡪 o campo deve ser preenchido com o valor da base de cálculo do ICMS da SAFX07 \(campo 51\-Base ICMS\);

Para as notas *com *itens 🡪 neste caso deve\-se totalizar o valor da base de cálculo de todos os itens da nota, considerando o campo “56\-Base ICMS” da SAFX08, sempre que o código de tributação indicar operação tributada \(campo 55 da SAFX08\)\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-19__

Campo VL\_ICMS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do ICMS \(conforme a planilha de\-para\)\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-20__

Campo COD\_INF:

Se o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita\.

Se o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda\. Esta opção deve estar por default selecionado\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-21__

Campo VL\_PIS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor do PIS \(conforme a planilha de\-para\)\.

Para notas canceladas este campo não deverá ser informado\.

__RND500\-22__

Campo VL\_COFINS:

Aplicar a mesma regra descrita para o campo 22\-VL\_BC\_ICMS, considerando os campos do valor da COFINS \(conforme a planilha de\-para\)\.

Para notas canceladas este campo não deverá ser informado

__RND500\-23__

CHV\_DOC\_E Chave do Documento Fiscal Eletrônico 

Campo 23 – Preenchimento: Informar a chave do documento eletrônico\. Campo existente apenas a partir do período de apuração 01/04/2025, sendo obrigatório quando COD\_MOD for igual a “62” ou “55”\.

__Observação:__ No entanto não temos os modelos 62 e 55 sendo gerado no Bloco D500, então o campo deve ser gerado em branco

D500|0|1|1\-1110006023|21|00|0||77|08042025|17042025|1118,24|0|1118,24|1118,24|0|0|0|0||18,45|84,99||

__     __

__                     Registro D501 \- Complemento da Operação \(Códigos 21 e 22\) – PIS__

__RNG\-D501__

Consolidar as informações dos itens dos documentos fiscais que passaram pelas regras de geração do registro D500, de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N” \(parâmetro da tela de geração\)

	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ‘’71’’, ‘’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’\.

SENÃO \(parâmetro “Gera Itens sem Crédito = S”\)

	Todos os itens do documento devem ser considerados no agrupamento\.

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária PIS: \(campo 175 da SAFX08/68 da SAFX09\)

\- Código da Natureza da Base de Cálculo do Crédito

\- Alíquota do PIS: \(campo 129 da SAFX08/47 da SAFX09\)

\- Código da Conta Contábil: \(campo 105 da SAFX08/52 da SAFX09\)

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

__RND501\-02__

Campo CST\_PIS:

Notas com item 🡪 campo 175 da SAFX08 ou campo 68 da SAFX09\.

__RND501\-03__

Campo VL\_ITEM:

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08 e do campo 15 \(Valor Total do Serviço\) da SAFX09 

__RND501\-04__

Campo NAT\_BC\_CRED:

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver marcado \(nos dados iniciais\):

Gravar o conteúdo do campo Natureza da Base de Crédito \(campo novo da SAFX08/SAFX09\) informada no documento fiscal\.   

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver desmarcado \(nos dados iniciais\):

Gravar o código da natureza da base de crédito que consta na TACES X “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP \(campo 22 da SAFX08 – campo 17 da SAFX09\) informado no documento fiscal\. 

__*Incluir crítica no log do processo:*__

__*Origem:*__

O novo campo Natureza da Base de Crédito na SAFX08 ou SAFX09 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

__*Mensagem:*__

O campo NAT\_BC\_CRED é de preenchimento obrigatório, quando o parâmetro’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

__RND501\-05__

Campo VL\_BC\_PIS:

Notas com item 🡪 somatório do campo 86 da SAFX08 e campo 46 da SAFX09\.

__RND501\-06__

Campo ALIQ\_PIS:

Notas com item 🡪 somatório do campo 129 da SAFX08 e campo 47 da SAFX09\.

__RND501\-07__

Campo VL\_PIS:

Notas com item 🡪 somatório do campo 87 da SAFX08 e campo 48 da SAFX09\.

__         __

__                     Registro D505 \- Complemento da Operação \(Códigos 06, 28, e 29\) – COFINS__

__RNG\-D505__

Consolidar as informações dos itens dos documentos fiscais gerados no registro C500 de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N”: \(parâmetro da tela de geração\)

	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ‘’71’’, ‘’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’\.

SENÃO \(parâmetro “Gera Itens sem Crédito = S”\)

	Todos os itens do documento devem ser considerados no agrupamento\.

O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

\- Código de Situação Tributária COFINS: \(campo 178 da SAFX08/69 da SAFX09\)

\- Código da Natureza da Base de Cálculo do Crédito

\- Alíquota da COFINS \(campo 130 da SAFX08/50 da SAFX09\)

\- Código da Conta: \(campo 105 da SAFX08\-52 da SAFX09\)

Exceto documentos cancelados, onde o COD\_SIT = 02 \(cancelado\) não deverá ser informado registros filhos\. 

__RND505\-02__

Campo CST\_COFINS:

Notas com item 🡪 campo 178 da SAFX08 ou campo 69 da SAFX09\.

__RND505\-03__

Campo VL\_ITEM:

Notas com item 🡪 somatório do campo 64 \(Valor Contábil dos itens\) da SAFX08 e do campo 15 \(Valor Total do Serviço\) da SAFX09

__RND505\-04__

Campo NAT\_BC\_CRED:

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver marcado \(nos dados iniciais\):

Gravar o conteúdo do campo Natureza da Base de Crédito \(campo novo da SAFX08/SAFX09\) informada no documento fiscal\.   

Se o parâmetro “__Considerar a Natureza da Base de Crédito a partir dos Documentos__” estiver desmarcado \(nos dados iniciais\):

Gravar o código da natureza da base de crédito que consta na TACES X “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP \(campo 22 da SAFX08 – campo 17 da SAFX09\) informado no documento fiscal\. 

__*Incluir crítica no log do processo:*__

__*Origem:*__

O novo campo Natureza da Base de Crédito na SAFX08 ou SAFX09 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

__*Mensagem:*__

O campo NAT\_BC\_CRED é de preenchimento obrigatório, quando o parâmetro’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

__RND505\-05__

Campo VL\_BC\_COFINS:

Notas com item 🡪 somatório do campo 88 da SAFX08 e campo 49 da SAFX09\.

__RND505\-06__

Campo ALIQ\_COFINS:

Notas com item 🡪 somatório do campo 130 da SAFX08 e campo 50 da SAFX09\.

__RND505\-07__

Campo VL\_COFINS:

Notas com item 🡪 somatório do campo 89 da SAFX08 e campo 51 da SAFX09\.

__                     Registro D600 – Consolidação Prestação de Serviços \- Comunicação e Telecomunicação \(Códigos “21”, “22” e “62”\)__

__RNG\-D600__

Nesse registro deve ser gravada a consolidação das notas fiscais de saída, com os seguintes critérios:

__\[MFS1069400\] __Alteração da regra para considerar o item informativo para notas da SAFX42/SAFX43 de modelo 62

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = desmarcado 

Selecionar da SAFX42 e SAFX43:

\-Modelo \(campo 13 da SAFX42\)

\-Município dos Terminais Faturados \(campo 76 da SAFX42\)

\-Série \(campo 07 da SAFX42\)

\-Subsérie \(campo 08 da SAFX42\)

\-Tipo da Receita \(campo 65 da SAFX42\)

Assim, as notas emitidas no período que tenham o mesmo modelo, município faturado, série/subsérie e tipo de receita irão gerar um único registro D600\.

Critérios de seleção das notas:

Modelo: \(campo 13 da SAFX42\)

	Igual a “21”, “22” e “62”

Data de Emissão/Escr\. Fiscal: \(campo 03 da SAFX42\)

	Entre a Data Inicial e Data Final de geração do arquivo

Tipo do item: \(campo 10 da SAFX43\)

               Se o modelo do documento \(campo 13 da SAFX42\) for igual a “21” ou “22”

                     Diferente de ‘’1 \- Item Informativo \- Informação não considerada no Convênio 115’’

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = marcado 

Preencher os campos de acordo com regras especificadas no item “Geração via SAFX161/SAFX162”\.

Deverá gerar uma linha de registro no D600 obedecendo ao critério de seleção das tabelas __SAFX42/43 __ou__ SAFX161__\. Os campos serão preenchidos de acordo com o conteúdo disponibilizado nos campos chaves e demais campos\.

OBS: As Notas Fiscais cuja Situação seja “Cancelada” \(campo 21 da SAFX42\) os registros D600 e filhos \(D601 e D605\) não deverão ser gerados\.

\[OS4316\-A\] __Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

__RND600\-02__

Campo COD\_MOD:

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Código do Modelo \(campo 03 da SAFX161\)

__RND600\-03__

Campo COD\_MUN:

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com  o Código do município dos terminais faturados\(campo 5 da SAFX161\)  concatenado com o campo Código UF dos terminais faturados \(campo 4 da SAFX161\)\.

__RND600\-04__

Campo SER:

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com a Série \(campo 05 da SAFX161\)\.

__RND600\-05__

Campo SUB:

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com a Subsérie \(campo 06 da SAFX161\)\.

__RND600\-06__

Campo IND\_REC:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o 95\-IND\_TP\_REC\_PIS\_COFINS – SAFX43

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Tipo de Receita \(campo 07 da SAFX161\)\.

__RND600\-07__

Campo QTD\_CONS:

Esse campo deve ser preenchido com a quantidade de documentos consolidados neste registro, conforme a regra RNGD600

__RND600\-08__

Campo DT\_DOC\_INI:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a data de emissão \(campo 03 da SAFX42\) do primeiro documento fiscal agrupado neste de registro

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com a Data inicial \(campo 08 da SAFX161\)  

__RND600\-09__

Campo DT\_DOC\_FIN:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a data de emissão \(campo 03 da SAFX42\) do último documento fiscal agrupado neste registro

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com a Data Final \(campo 09 da SAFX161\)  

__RND600\-10__

Campo VL\_DOC:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com Valor Total do Documento Fiscal \(campo 17 da SAFX42\), através da totalização do valor total dos documentos consolidados de acordo com a RND600 \(totalizar a partir das capas dos documentos consolidados\)

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor total acumulado na capa dos documentos fiscais \(campo 10 da SAFX161\)  

__RND600\-11__

Campo VL\_DESC:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor do Desconto \(campo 18 VLR\_DESCONTO da SAFX42\), através da totalização do valor do desconto dos documentos consolidados\.

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor acumulado dos descontos \(campo 11 da SAFX161\)\.

__RND600\-12__

Campo VL\_SERV:

__\[MFS1042721\] __Alteração da regra para gerar o valor do serviço conforme o SPED\-EFD, para notas da SAFX42/SAFX43 de modelo 62

Geração via SAFX42/SAFX43:

Se o modelo do documento \(campo 13 da SAFX42\) for diferente de 62

     Este campo deve ser preenchido com o Valor do Serviço \(campo 19 da SAFX43\), através da totalização do valor do produto/serviço dos      

    documentos consolidados\.

Senão \(modelo = 62\)

     Totalização do Valor do Serviço \(19\-Valor dos Serviços \- SAFX43\), apenas as notas com campo COD\_SIT\_TRIB\_B \(campo 33 da SAFX43\)    

      preenchido e diferente de “30” ou “40” ou ”41” ou “50” ou “51” ou “90” considerando o IND\_ADIC\_DESC \(campo 20 da SAFX43\) conforme regra a seguir:

__      Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

            O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__      Senão __

            O sistema deverá __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__      Valor Negativo à  __Quando o cálculo do campo VL\_SERV resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá              

       erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV*__ __*esta com conteúdo inválido       *__

__*      \(valor negativo\)”\.*__

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor acumulado das prestações de serviços tributados pelo ICMS \(campo 12 da SAFX161\)\.

__RND600\-13__

Campo VL\_SERV\_NT:

__\[MFS1042721\] __Alteração da regra para gerar o valor do serviço conforme o SPED\-EFD para notas da SAFX42/SAFX43 de modelo 62

Geração via SAFX42/SAFX43:

Se o modelo do documento \(campo 13 da SAFX42\) for diferente de 62

     Totalização do valor dos serviços não tributados pelo ICMS dos documentos consolidados de acordo com a RND600:

        Valor das bases isenta/não tributada \+ base outras \+ base de redução dos *itens de mercadoria* da __SAFX43 __\+ valor do serviço dos *itens de *    

*         serviço* da __SAFX43__:

        \[campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras \+ campo 26\-Base de Redução dos itens de mercadoria \(campo 47 = “1”\)\]           

        \+ \[campo 19\-Valor do Serviço dos itens de serviço \(campo 47 = “2”\) \]

Senão \(modelo = 62\)

     Preencher com a soma dos valores dos Itens da __SAFX43__:

__     \(a\) __Valor das bases isenta/não tributada \+ base outras dos *itens de mercadoria* __SAFX43 __

__      \+__

__     \(b\) __Valor do serviço dos *itens de mercadoria* da __SAFX43, __

__      \+__

__     \(c\)__ Valor do serviço dos *itens de serviço* da __SAFX43,__

    Onde:

   \- Para __\(a\)__, considerar campos 24\-Base Isenta/Não Tributada \+ campo 25\-Base Outras da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\),    

    apenas quando o campo COD\_SITUACAO\_B \(campo 33 da SAFX43\) preenchido e igual a “30” ou “40” ou ”41” ou “50” ou “51” ou “90”,        

    considerando o  IND\_ADIC\_DESC \(campo 20 da SAFX43\) conforme regra abaixo\. Desconsiderar os itens com “Grupo cClass Nfe” \(campo  

    118 da SAFX43\) = 590\.

    \- Para __\(b\)__, considerar campo 19\-Valor do Serviço da __SAFX43__ dos itens de mercadoria \(campo 47 = “1”\), apenas quando o campo    

    COD\_SITUACAO\_B da tabela __SAFX43__ não estiver preenchido, considerando o IND\_ADIC\_DESC conforme regra abaixo\. Desconsiderar os 

    itens com “Grupo cClass Nfe” \(campo 118 da SAFX43\) = 590\.

    \- Para __\(c\)__ considerar o campo 19\-Valor do Serviço da __SAFX43__ dos itens de serviço \(campo 47 = “2”\) considerando o IND\_ADIC\_DESC 

      conforme regra abaixo\.

__     Se__ o Campo IND\_ADIC\_DESC for igual à ‘__D__’ 

          \- Para __\(a\)__:

            O sistema deverá  __subtrair__ do valor total os Campos 24\-Base Isenta/Não Tributada e campo 25\-Base Outras \- SAFX43\.

           \- Para __\(b\)__ e __\(c\)__:

             O sistema deverá  __subtrair__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__     Senão __

           \- Para __\(a\)__:

            O sistema deverá  __somar__ do valor total os Campos 24\-Base Isenta/Não Tributada e campo 25\-Base Outras \- SAFX43\.

           \- Para __\(b\)__ e __\(c\)__:

           O sistema deverá  __somar__ do valor total o Campo 19\-Valor dos Serviços \- SAFX43\.

__     Valor Negativo à  __Quando o cálculo do campo VL\_SERV\_NT resultar num valor negativo,  o campo deverá ser gravado negativo \(ocorrerá 

     erro no validador\) e gravar uma mensagem de erro no log com a seguinte descrição: __*“O campo VL\_SERV\_NT*__ __*esta com conteúdo     *__

__*     inválido \(valor negativo\)”\.*__

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor acumulado dos serviços não\-tributados pelo ICMS \(campo 12 da SAFX162\)\.

__RND600\-14__

Campo VL\_TERC:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor de Terceiros \(campo 75 da SAFX43\), através da totalização do valor de terceiros dos documentos consolidados

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com Valores cobrados em nome de terceiros \(campo 14 da SAFX161\)\.

__RND600\-15__

Campo VL\_DA

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor Outras Despesas \(campo 18 da SAFX42\), através da totalização do valor de outras despesas dos documentos consolidados

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com Valor acumulado das despesas acessórias \(campo 15 da SAFX161\)\.

__RND600\-16__

Campo VL\_BC\_ICMS

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a Base Tributada \(campo 23 da SAFX43\), através da totalização do valor da base de cálculo do ICMS dos documentos consolidados\.

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor acumulado da base de cálculo do ICMS \(campo 16 da SAFX161\)\.

__RND600\-17__

Campo VL\_ICMS

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor ICMS \(campo 22 da SAFX43\), através da totalização do valor do ICMS dos documentos consolidados\.

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor acumulado do ICMS \(campo 17 da SAFX161\)\.

__RND600\-18__

Campo VL\_PIS

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor PIS \(campo 77 da SAFX43\), através da totalização do valor do PIS dos documentos consolidados\.

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor do PIS/PASEP da capa dos documentos fiscais \(campo 18 da SAFX161\)\.

__RND600\-19__

Campo VL\_COFINS

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor COFINS \(campo 80 da SAFX43\), através da totalização do valor do COFINS dos documentos consolidados\.

Geração via SAFX161/SAFX162:

Este campo deve ser preenchido com o Valor da COFINS da capa dos documentos fiscais \(campo 19 da SAFX161\)\.

__                     Registro D601 \- Complemento da Operação \(Códigos “21”, “22” e “62”\) – PIS/PASEP__

__RNG\-D601__

Consolidar as informações dos itens dos documentos fiscais gerados no D600, com base nas seguintes informações: 

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = desmarcado 

\- Código da Classificação do Item: \(campo 42 da SAFX43\) 

\- Código de Situação Tributária do PIS \(campo COD\_SITUACAO\_PIS da SAFX43\)

\- Alíquota do PIS \(campo 79 da SAFX43\)

\- Código da Conta \(campo 53 da SAFX43\)  

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = marcado 

Preencher os campos de acordo com regras especificadas no item “Geração via SAFX161/SAFX162”\.

__RND601\-02__

Campo COD\_CLASS:

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Código de classificação \(campo 03 da SAFX162\)\.

__RND601\-03__

Campo VL\_ITEM:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor do Serviço \(campo 19 da SAFX43\)

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com Valor acumulado do item \(campo 04 da SAFX162\)

__RND601\-04__

Campo VL\_DESC:

Geração via SAFX42/SAFX43:

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões PIS”

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor acumulado dos descontos/exclusões da base de cálculo do PIS/PASEP \(campo 12 da SAFX162\)\.

__RND601\-05__

Campo CST\_PIS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Código Situação Tributária PIS \(campo 93 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Código da Situação Tributária referente ao PIS/PASEP \(campo 06 da SAFX162\)\.

__RND601\-06__

Campo VL\_BC\_PIS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor Base de Cálculo PIS \(campo 78 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor da base de cálculo do PIS/PASEP \(campo 07 da SAFX162\)

__RND601\-07__

Campo ALIQ\_PIS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a Alíquota PIS \(campo 79 da SAFX43\)

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com a Alíquota do PIS/PASEP \(campo 08 da SAFX162\)\.

__RND601\-08__

Campo VLR\_PIS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor PIS \(campo 77 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor do PIS/PASEP do item dos documentos fiscais \(campo 09 da SAFX162\)\.

__RND601\-09__

Campo COD\_CTA:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Código da conta analítica contábil \(campo 53 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com Código da conta analítica contábil debitada/creditada \(campo 15 da SAFX162\)\.

__                     Registro D605 \- Complemento da Operação \(Códigos “21”, “22” e “62”\) – COFINS__

__RNG\-D605__

Consolidar as informações dos itens dos documentos fiscais gerados no D600, com base nas seguintes informações: 

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = desmarcado 

\- Código da Classificação do Item: \(campo 42 da SAFX43\) 

\- Código de Situação Tributária da COFINS \(campo COD\_SITUACAO\_COFINS da SAFX43\)

\- Alíquota da COFINS \(campo 82 da SAFX43\)

\- Código da Conta \(campo 53 da SAFX43\)  

Se flag “Geração com base nas informações da SAFX161 e SAFX162” = marcado 

Preencher os campos de acordo com regras especificadas no item “Geração via SAFX161/SAFX162”\.

__RND605\-02__

Campo COD\_CLASS

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Código de classificação \(campo 03 da SAFX162\)\.

__RND605\-03__

Campo VL\_ITEM:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor do Serviço \(campo 19 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor acumulado da COFINS do item \(campo 04 da SAFX162\)\. 

__RND605\-04__

Campo VL\_DESC:

Geração via SAFX42/SAFX43:

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões COFINS”

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor acumulado dos descontos/exclusões da base de cálculo da COFINS \(campo 12 da SAFX162\)\.

__RND605\-05__

Campo CST\_COFINS

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Código Situação Tributária COFINS \(campo 94 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Código da Situação Tributária referente da COFINS \(campo 11 da SAFX162\)\.

__RND605\-06__

Campo VL\_BC\_COFINS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a Base COFINS \(campo 81 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor da Base de cálculo da COFINS \(campo 12 da SAFX162\)\.

__RND605\-07__

Campo ALIQ\_COFINS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com a Alíquota COFINS \(campo 82 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com a Alíquota do COFINS \(campo 13 da SAFX162\)\.

__RND605\-08__

Campo VL\_COFINS:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Valor COFINS \(campo 80 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com o Valor da COFINS do item dos documentos fiscais \(campo 14 da SAFX162\)\.

__RND605\-09__

Campo COD\_CTA:

Geração via SAFX42/SAFX43:

Este campo deve ser preenchido com o Código da conta analítica contábil \(campo 53 da SAFX43\)\.

Geração via SAFX161/SAFX162”:

Este campo deve ser preenchido com Código da conta analítica contábil debitada/creditada \(campo 16 da SAFX162\)\.

