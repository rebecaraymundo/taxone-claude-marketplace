# RNG-D_V18

> Fonte: RNG-D_V18.doc

Regras de Recuperação para os registros do bloco D:
Registro D001 – Abertura do Bloco
RNG-D001	Deve ser gerado um registro por arquivo.		RND001-02	Campo IND_MOV:

Gravar "0" se existir movimentação a ser gerada no bloco D no período informado na tela de geração, senão gravar ‘’1’’.		
Registro D010 – Identificação do Estabelecimento
RNG-D010	CH27235/2013
Gerar um registro D010 para cada CNPJ de estabelecimento que possua movimentação nos registros do bloco D.

As movimentações do bloco D devem ser geradas imediatamente abaixo do registro D010 do CNPJ do estabelecimento correspondente.

* Foi incluída observação para gerar por CNPJ do estabelecimento por conta de situações onde a empresa tem mais de um estabelecimento com o mesmo CNPJ. Neste caso, deve ser gerado apenas um A010 por CNPJ e as movimentações serão vinculadas abaixo do CNPJ.
		
Registro D100 - Aquisição de Serviços de Transporte
Nota Fiscal de Serviço de Transporte (Código 07),
Conhecimentos de Transporte Rodoviário de Cargas (Código 08),
Conhecimentos de Transporte de Carga avulso (Código 8B),
Conhecimento de Transporte Aquaviário de Cargas (Código 09),
Conhecimento Aéreo (Código 10), 
Conhecimento de Transporte Ferroviário de Cargas (Código 11),
Conhecimento de Transporte Multimodal de Cargas (Código 26),
Nota Fiscal de Transporte Ferroviário de Carga (Código 27),e
Conhecimento de Transporte Eletrônico – Cte (Código 57),e
Bilhete de Passagem Eletrônico - BP-e (Código 63) e
Conhecimento de Transporte Eletrônico p/Outros Serviços – Cte OS (Código 67). 

RNG-D100	Nesse registro devem ser gravadas as notas (SAFX07) que atendam aos critérios abaixo:

Modelo: (campo 13 da SAFX07)
	Igual a “07”, “08”, “8B”, “09”, “10”, “11”, “26”, “27”, “57”, “63” ou “67”

Alteração MFS12767: Inclusão do modelo 67. Conforme orientação do GP, este modelo de documento fiscal foi instituído pelo Ajuste SINIEF nº 10, de 2016, e deve ser utilizado parar os fatos geradores a partir de 01 de julho de 2017.

Alteração MFS-19270: Inclusão do modelo 63. Conforme orientação do GP de vrs 1.26 sem publicação de ato legal, apenas orientação da Receita Federal em 21/06/2018 de acordo com a disponibilização do PVA 3.00.

Movimento Entrada/Saída: (campo 03 da SAFX07)
	Diferente de “9”

Crédito/Contribuição Extemporânea: (campo novo da SAFX08) 
	Somente documentos não extemporâneos (campo novo = “N”)

SE for um documento fiscal emitido por terceiros (campo 03 da SAFX07 igual a “1”)
	Classificação: (campo 12 da SAFX07)
	Igual a “1 – Mercadoria” ou “4 – Conhecimento de Frete”

SE for um documento fiscal de emissão própria (campo 03 da SAFX07 igual a “2”, “3”, “4” ou “5”)
	Classificação: (campo 12 da SAFX07)
	Igual a “1 – Mercadoria” ou “4 – Conhecimento de Frete”

 [ALTERAÇÃO – CH28382 / CH6594/2015 / OS4816]
Data de Lançamento PIS/COFINS: o campo Data do Lançamento (campo 247 - DAT_LANC_PIS_COFINS da SAFX07 ou campo 196 - DAT_LANC_PIS_COFINS da SAFX08)* deve estar preenchido com uma data que esteja entre a Data Inicial e Data Final de geração do arquivo.

* Para recuperação das notas de entrada considerar o informado no parâmetro “Registro A100, C100, C190, C395, C500, D100 e D500 - Seleção das Operações Geradoras de Crédito / Considerar para filtro da Data de Lançamento do EFD PIS/COFINS” disponível na tela de Dados Iniciais.

Se no parâmetro indicado for preenchida a opção “Capa NF”, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX07.

Se no parâmetro indicado for preenchida a opção “Item NF”, serão selecionados os registros considerando como critério a Data de Lançamento informada na SAFX08. Neste caso, se for identificada alguma NF cuja data não tenha sido preenchida na SAFX08, mas esteja preenchida na SAFX07 e esteja no período, também deve ser considerada.

Para notas fiscais sem item, considerar apenas o critério de seleção da data de lançamento da capa, independente do critério indicado no parâmetro

Observação: Quando houver o preenchimento da data de lançamento na capa e no item da nota fiscal com períodos distintos não haverá tratamento pelo sistema, não pode haver lançamento na capa nesse caso, apenas no item, ou seja, será aceito na geração apenas conteúdo VAZIO ou IGUAL, se houver preenchimento o sistema considerará e a geração estará incorreta, por esse motivo essa orientação será feita ao usuário no manual de layout de importação dos documentos fiscais e no manual operacional.

Exemplo: Data do Lançamento PIS/COFINS 15/07/2013 / Período de Geração: JUL/2013 – Neste exemplo a nota será gerada.

SE parâmetro Gera NF’s de Entrada sem Crédito = “Não” (parâmetro da tela de geração), considerar apenas registros cujo CST PIS ou CST COFINS (campos 175 e 178 da SAFX08, campos 68 e 69 da SAFX09 ou campos 249 e 250 da SAFX07) estejam preenchidos com conteúdo igual a 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 ou 67. Senão, considerar todos os CSTs.


[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que não tenham o campo Código do SCP preenchido.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento (considerando a regra padrão de seleção) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração.

[OS4316-C] Observar a parametrização de "Dados Iniciais" (menu: Parâmetros >> Dados Iniciais) para geração ou não do registro. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido.

Obs1.: Para CT-e de emissão própria (campo 13 da SAFX07 igual “57” e campo 03 igual “1”), somente deve ser gerado o registro D100, os registros filhos (D101, D105 e D111) não devem ser gerados.

Obs. 2: Se os campos “Crédito/Contribuição Extemporânea” e “Data do Lançamento PIS/COFINS” não estiverem preenchidos no item do documento fiscal (SAFX08), considerar o conteúdo desses campos informados na capa do documento (SAFX07).

Obs3.: Para as notas fiscais que não possuem item de mercadoria, as verificações devem ser feitas com base no CST, Data de Lançamento PIS/COFINS e Crédito/Contribuição Extemporânea de acordo com as informações da capa do documento.

Tratamento especial para notas canceladas:
Quando se tratar de NF cancelada (campo “30-Situação da nota” = “S”) somente poderá ser informado os campos IND_OPER, campo IND_EMIT, campo COD_SIT, campo SER e campo NUM_DOC. Não deverão ser informados registros filhos. 
		RND100-02	Campo IND_OPER:
A partir do conteúdo do indicador de Entrada/Saída da nota (campo 03-Movimento Entrada/Saída da SAFX07), verificar:
Se campo “Movimento Entrada/Saída” <> 9 ( gravar 0 (aquisição)
		RND100-03	Campo IND_EMIT:
A partir do conteúdo do indicador de Entrada/Saída da nota (campo 03-Movimento Entrada/Saída da SAFX07), verificar:

Se campo “Movimento Entrada/Saída” = 1 ( gravar 1 (emissão terceiros)
Se campo “Movimento Entrada/Saída” <> 1 ( gravar 0 (emissão própria)


OBS: Se este campo tiver valor igual a 1 (terceiros), então o campo IND_OPER deve ser igual a 0 (entradas). Se este campo tiver valor igual a 0 (emissão própria), então o campo IND_OPER poderá ser igual a 0 (entradas) ou 1 (prestação).
		RND100-04	Campo COD_PART:
Para notas canceladas este campo não deverá ser informado.

 [OS4751] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais estiver selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador (IND_FIS_JUR) com o Código da PFJ (COD_FIS_JUR), considerando a formatação: Indicador + "-" + Código.
Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ (COD_FIS_JUR).
Para o código aqui informado, será demonstrado o Cadastro no registro 0150.
		RNC100-05	Campo COD_MOD:
Para notas canceladas e campo “IND_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado.		RND100-06	Campo COD_SIT:
Para o preenchimento deste campo deverão ser verificados alguns campos da SAFX07, conforme segue:
Se for nota eletrônica, verificar:
     se a nota foi denegada        ( gravar “04”
     se a nota foi  ou inutilizada ( gravar “05”

Se for nota cancelada,
      gravar “02”

Se for nota complementar:
      gravar “06”

Se nota tem Ato Normativo, Regime Especial etc...
      gravar “08”
Se a nota não atende a nenhuma das opções anteriores:
      gravar “00”

Importante: 
Os testes devem ser executados exatamente nesta prioridade. Assim, o teste deve ser encerrado na primeira regra atendida pela nota, e sempre que isto não ocorrer, será gravado o conteúdo “00”.
A lógica seria a seguinte:
Se nota é eletrônica e foi  (denegada ou inutilizada)
        Se nota é denegada
              gravar “04”
        Senão  (é inutilizada)
              gravar “05”
Senão
        Se nota é cancelada
              gravar “02”
              Senão
                    Se nota é complementar
                         gravar “06”
                    Senão
                         Se nota tem Ato Normativo, Regime Especial etc
                              gravar “08”
                         Senão
                             gravar “00”;
  
Campos da SAFX07 para verificação das regras:

Nota cancelada ( campo “30-Situação da nota” =  “S”;

Nota complementar ( campo “125-Situação Especial” = “5”;

(Alteração MFS12767: Inclusão do modelo 67)
Alteração MFS-19270: Inclusão do modelo 63)

Nota Eletrônica ( campo “13-Modelo de Documento” = “57”, “63” ou “67”;

Nota Eletrônica denegada ( campo “13-Modelo de Documento” = (“57”, “63” ou “67”) e o campo “231-Nfe Denegada/Inutilizada” = “1” (denegada);

Nota Eletrônica inutilizada ( campo “13-Modelo de Documento” = (“57”, “63” ou “67”) e o campo “231-Nfe Denegada/Inutilizada” = “2” (inutilizada);

Nota com Ato Normativo, Regime Especial etc ( o campo “232-NF Baseada em Regime Especial ou Norma Específica” será = “S”.		RND100-07	Campo SER:
Para notas canceladas e campo “IND_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado.		RND100-08	Campo SUB:
 Para notas canceladas e campo “IND_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado.		RND100-09	Campo NUM_DOC:
Para notas canceladas e campo “IND_EMIT” igual a “1” ou igual “0”, este campo deverá ser informado.		RND100-10	Campo: CHV_CTE
Informar neste campo a chave do conhecimento de transporte eletrônico (SAFX07-Campo: 226) se: 
      Tabela: SAFX07
                  Modelo de Documento = 57, 63 ou 67

(Alteração MFS12767: Inclusão do modelo 67)
(Alteração MFS-19270: Inclusão do modelo 63)

            Caso não exista a informação, gravar mensagem no log de erros:
Erro1:
Se IND_EMIT = 0 (Emissão Própria): 
O campo CHV_CTE é de preenchimento obrigatório, e não foi informado
Origem: Campo Chave de Acesso do CT-e do Documento Fiscal (SAFX07)
Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur

Aviso:
Para as gerações até 31/03/2012 emitir a msg abaixo:
Se IND_EMIT = 1 (Emissão de terceiros): 
O campo CHV_CTE será de preenchimento obrigatório, a partir de abril de 2012.
Origem: Campo Chave de Acesso do CT-e do Documento Fiscal (SAFX07)
Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur

Para as gerações a partir de 01/04/2012

Se IND_EMIT = 0 ou 1
O campo CHV_CTE é de preenchimento obrigatório, e não foi informado
Origem: Campo Chave de Acesso da NF-e do Documento Fiscal (SAFX07)
Dados do Registro: Num Docto Fiscal         Série        Dt Emissão      Pessoa Fis/Jur


		RND100-11	Campo DT_DOC:
Para notas canceladas este campo não deverá ser informado.		RND100-12	Campo DT_A_P:
Para notas canceladas este campo não deverá ser informado.		RND100-13	Campo: TP_CT-e
Informar neste campo o tipo do conhecimento de transporte eletrônico se: 
Tabela: SAFX07
             Se Modelo de Documento = (57, 63 ou 67), e
                  (Alteração MFS12767: Inclusão do modelo 67)
                  (Alteração MFS-19270: Inclusão do modelo 63)
                     Se campo “situação especial” = 5 gravar “1”, ou
                             Se campo “situação especial” = B gravar “2”, ou
                                     Se campo “situação especial” = C gravar “3”, ou
                                              Se campo “situação especial” = nulo ou espaços gravar “0”,ou
                                                     Se campo “situação especial” <> 5, B ou C, gravar “0”

Para notas canceladas este campo não deverá ser informado.		RND100-14	Campo: CHV_CTE_REF  
No EFD Fiscal, este campo não é preenchido, e sim gravado sem informação (alteração do GP vrs 1.0.4) 
Para notas canceladas este campo não deverá ser informado.		RND100-15	Campo: VL_DOC
Este campo deve ser preenchido com o valor da nota mais o desconto, ou seja:

Notas sem item ( campo 23 (Valor Total)  +  campo 28  (Desconto) da SAFX07
Notas com item ( total = campo 64 (Valor Contábil)  +  campo 29 (Desconto) dos itens da SAFX08

Para notas canceladas este campo não deverá ser informado.		RND100-16	Campo VL_DESC:
Para as notas sem itens ( o campo deve ser preenchido com o valor do desconto da SAFX07 (campo 28-Valor Descontos);
Para as notas com itens ( neste caso deve-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29-Valor do Desconto” da SAFX08.
Para notas canceladas este campo não deverá ser informado.		RND100-17	Campo: IND_FRT
Gravar o Indicador do Tipo de Frete: 

Se campo “situação especial” = 5 (Campo: 125/SAFX07), gravar = “9”,
        Se campo “situação especial” <> 5 (Campo: 125/SAFX07), e
               Se campo “Indicador do Tipo de Frete” = 0 gravar “0”; ou
                     Se campo “Indicador do Tipo de Frete” = 1 gravar “1”; ou
                            Se campo “Indicador do Tipo de Frete” = 2 gravar “2”; ou
                                      Se campo “Indicador do Tipo de Frete” = nulo/espaço gravar “9”;
Origem da Informação:
Tabela
Descrição do Campo:
Nº do Campo:
Nome do Campo:

SAFX07
Indicador do Tipo de Frete
72
IND_TP_FRETE


A partir de 01/Julho/2012, na geração do SPED PIS/COFINS deverá ser considerado a seguinte regra: 

MFS13627: Alterada regra de geração do IND_FRT devido à alteração do campo “72-Indicador do Tipo de Frete” da SAFX07, p/atendimento ao Ato Cotepe 48/2017 (alteração da EFD).

Se campo 72 da SAFX07 for igual “1-Frete para Conta do Emitente (CIF)”
                                                      ou = “3-Transporte Próprio por conta do Remetente”,
      Preencher o campo com “0” (Por conta do emitente);

Se o campo 72 da SAFX07 for igual “2-Frete para Conta do Destinatário (FOB)”
                                                       ou “4-Transporte Próprio por conta do Destinatário”, 
     Preencher o campo com “1”(Por conta do destinatário/remetente);

Se o campo 72 da SAFX07 for igual “0-Outros”,
     Preencher o campo com 2 (Por conta de terceiros)

Se o campo 72 da SAFX07 for igual “vazio”, 
     Preencher  o campo com “9” (Sem frete).

Para notas canceladas este campo não deverá ser informado.
		RND100-18	Campo: VL_SERV
Este campo deve ser preenchido com o valor total da nota dos serviços, ou seja:
Notas sem item ( campo 23 - Valor Total da SAFX07
Notas com item ( somatório do campo 64 (Valor Contábil dos itens) da SAFX08

Para notas canceladas este campo não deverá ser informado.
		RND100-19	Campo: VL_BC_ICMS
Para as notas sem itens ( o campo deve ser preenchido com o valor da base de cálculo do ICMS da SAFX07 (campo 51-Base ICMS);

Para as notas com itens ( neste caso deve-se totalizar o valor Base ICMS de todos os itens do documento em que o campo “56-Base ICMS” da SAFX08 esteja com o código de tributação igual a “1” operação tributada (campo 55 da SAFX08);

Para notas canceladas este campo não deverá ser informado.
		RND100-20	Campo: VL_ICMS
Para as notas sem itens ( o campo deve ser preenchido com o valor do ICMS da SAFX07 (campo 35-Valor ICMS);
Para as notas com itens ( neste caso deve-se totalizar o valor do ICMS de todos os itens do documento (campo “43- Valor ICMS” da SAFX08).

Para notas canceladas este campo não deverá ser informado.		RND100-21	Campo: VL_NT
Para as notas sem itens ( o campo deve ser preenchido com o valor da Base ICMS Isenta (campo 52) + Base ICMS Outras (campo 53) + Base Redução ICMS (campo 54) da SAFX07;

Para as notas com itens ( neste caso deve-se totalizar o valor Base ICMS de todos os itens do documento se o campo “56-Base ICMS” da SAFX08 estiver com o código de tributação igual a “2” ou “3” (campo 55 da SAFX08) e somar com valor Base Redução ICMS (campo 57 da SAFX08).

Para notas canceladas este campo não deverá ser informado.		RND100-22	Campo COD_INF:
Se o parâmetro “Justificar a esquerda”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da esquerda para direita.
Se o parâmetro “Justificar a direita”, da tela de Dados Iniciais, estiver selecionado, preencher com os 6 caracteres da direita para esquerda. Esta opção deve estar por default selecionado.
Para notas canceladas este campo não deverá ser informado.		RND100-23	Campo COD_CTA:

Preencher a informação do campo 105 COD_CONTA da tabela SAFX08.

Para notas canceladas este campo não deverá ser informado.		
Registro D101 – Complemento do Documento de Transporte (Códigos, 07, 08, 8B, 09, 10,11, 26,27 e 57) PIS/PASEP
RNG-D101	Consolidar as informações dos itens dos documentos fiscais gerados no registro D100 de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N” (parâmetro da tela de geração)
	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ‘’71’’, ‘’72’’,’’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’.
SENÃO (parâmetro “Gera Itens sem Crédito = S”)
	Todos os itens do documento devem ser considerados no agrupamento.


O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

- Indicador da Natureza do Frete 
- Código de Situação Tributária PIS: (campo 175 da SAFX08)
- Natureza da Base de Crédito (campo novo da SAFX08)
- Alíquota do PIS (campo 129 da SAFX08)
- Código da Conta Contábil: (campo 105 da SAFX08)

Obs.: Para os documentos que não possuírem item, considerar a informação destacada na capa (SAFX07)

Exceto documentos cancelados, onde o COD_SIT = 02 (cancelado) não deverá ser informado registros filhos. 
		RND101-02	Campo IND_NAT_FRT:

Notas sem item ( a partir do conteúdo do indicador da Natureza de Frete (novo campo da SAFX07)
Notas com item ( a partir do conteúdo do indicador da Natureza de Frete (novo campo da SAFX08):

Se indicador = Operações de vendas, com ônus suportado pelo estabelecimento vendedor, gravar “0’’
Se indicador = Operações de vendas, com ônus suportado pelo adquirente, gravar ‘’1’’
Se indicador = Operações de compras (bens para revenda, matérias-prima e outros produtos, geradores de crédito, gravar ‘’2’’
Se indicador = Operações de compras (bens para revenda, matérias-prima e outros produtos, não geradores de crédito, gravar ‘’3’’
Se indicador = Transferência de produtos acabados entre estabelecimentos da pessoa jurídica, gravar ‘’4’’
Se indicador = Transferência de produtos em elaboração entre estabelecimentos da pessoa jurídica, ‘’5’’
Se indicador = Outras, gravar ‘’9’’
		RND101-03	Campo VL_ITEM:

Notas sem item ( campo 23 - Valor Total da SAFX07
Notas com item ( somatório do campo 64 (Valor Contábil dos itens) da SAFX08.
		RND101-04	Campo CST_PIS:

Notas sem item ( campo Código da Situação Tributária PIS da SAFX07
Notas com item ( campo 175 (Código da Situação Tributária PIS) da SAFX08.		RND101-05	Campo NAT_BC_CRED:

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver marcado (nos dados iniciais):
Gravar o conteúdo do campo Natureza da Base de Crédito (campo novo/SAFX08) informada no documento fiscal.   

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver desmarcado (nos dados iniciais):
Gravar o código da natureza da base de crédito que consta na TACES X “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP (campo 14 da SAFX07/22 da SAFX08) informado no documento fiscal. 

Incluir crítica no log do processo:
Origem:
O novo campo Natureza da Base de Crédito na SAFX07 ou SAFX08 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

Mensagem:
O campo NAT_BC_CRED é de preenchimento obrigatório, quando o parâmetro’’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja  marcado nos dados iniciais’’

		RND101-06	Campo VL_BC_PIS:

Notas sem item ( campo 102- Valor da Base de Cálculo PIS da SAFX07
Notas com item ( somatório do campo 86 – Valor da Base de Cálculo PIS da SAFX08.		RND101-07	Campo ALIQ_PIS:

Notas sem item ( campo 164- Valor da Alíquota PIS da SAFX07
Notas com item ( somatório do campo 129 – Valor da Alíquota PIS da SAFX08.		RND101-08	Campo VL_PIS:

Notas sem item ( campo 103- Valor do PIS da SAFX07
Notas com item ( somatório do campo 87 – Valor do PIS da SAFX08.
		
Registro D105 – Complemento do Documento de Transporte (Códigos, 07, 08, 8B, 09, 10, 11, 26, 27 e 57) COFINS
RNG-D105	Consolidar as informações dos itens dos documentos fiscais gerados no registro D100 de acordo com a seguinte regra:

SE parâmetro “Gera Itens sem Crédito = N”: (parâmetro da tela de geração)
	Serão considerados no agrupamento apenas os itens que possuam CST <> “70”, ’’71’’, ‘’72’’, ‘’73’’, ‘’74’’, ‘’75’’, ‘’98’’ e ‘’99’’.
SENÃO (parâmetro “Gera Itens sem Crédito = S”)
	Todos os itens do documento devem ser considerados no agrupamento.


O agrupamento das notas fiscais a serem geradas nesse registro deve ser feito com base nas seguintes informações:

- Indicador da Natureza do Frete (campo Indicador da Natureza de Frete/SAFX07 ou SAFX08)
- Código de Situação Tributária COFINS: (campo 178 da SAFX08)
- Natureza da Base de Crédito (campo novo da SAFX08)
- Alíquota da COFINS (campo 130 da SAFX08)
- Código da Conta: (campo 105 da SAFX08)

Obs.: Para os documentos que não possuírem item, considerar a informação destacada na capa (SAFX07)

Exceto documentos cancelados, onde o COD_SIT = 02 (cancelado) não deverá ser informado registros filhos. 
 		RND105-02	Campo IND_NAT_FRT:

Notas sem item ( a partir do conteúdo do indicador da Natureza de Frete (novo campo da SAFX07)
Notas com item ( a partir do conteúdo do indicador da Natureza de Frete (novo campo da SAFX08):

Se indicador = Operações de vendas, com ônus suportado pelo estabelecimento vendedor, gravar “0’’
Se indicador = Operações de vendas, com ônus suportado pelo adquirente, gravar ‘’1’’
Se indicador = Operações de compras (bens para revenda, matérias-prima e outros produtos, geradores de crédito, gravar ‘’2’’
Se indicador = Operações de compras (bens para revenda, matérias-prima e outros produtos, não geradores de crédito, gravar ‘’3’’
Se indicador = Transferência de produtos acabados entre estabelecimentos da pessoa jurídica, gravar ‘’4’’
Se indicador = Transferência de produtos em elaboração entre estabelecimentos da pessoa jurídica, ‘’5’’
Se indicador = Outras, gravar ‘’9’’
		RND105-03	Campo VL_ITEM:

Notas sem item ( campo 23 - Valor Total da SAFX07
Notas com item ( somatório do campo 64 (Valor Contábil dos itens) da SAFX08.
		RND105-04	Campo CST_COFINS:

Notas sem item ( campo Código da Situação Tributária COFINS da SAFX07
Notas com item ( campo 178 (Código da Situação Tributária COFINS) da SAFX08.
		RND105-05	Campo NAT_BC_CRED:

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver marcado (nos dados iniciais):
Gravar o conteúdo do campo Natureza da Base de Crédito (campo novo/SAFX08) informada no documento fiscal.   

Se o parâmetro “Considerar a Natureza da Base de Crédito a partir dos Documentos” estiver desmarcado (nos dados iniciais):
Gravar o código da natureza da base de crédito que consta na TACES “CFOP x Natureza da Base de Crédito”, de acordo com o CFOP (campo 14 da SAFX07/campo 22 da SAFX08) informado no documento fiscal.

Incluir crítica no log do processo:
Origem:
O novo campo Natureza da Base de Crédito na SAFX07 ou SAFX08 esteja sem preenchimento e o parâmetro ‘‘Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

Mensagem:
O campo NAT_BC_CRED é de preenchimento obrigatório, quando o parâmetro’ ’Considerar a Natureza da Base de Crédito a partir dos Documentos” esteja marcado nos dados iniciais’’

		RND105-06	Campo VL_BC_COFINS:

Notas sem item ( campo 104- Valor da Base de Cálculo COFINS da SAFX07
Notas com item ( somatório do campo 88 – Valor da Base de Cálculo COFINS da SAFX08.
		RND105-07	Campo ALIQ_COFINS:

Notas sem item ( campo 130- Valor da Alíquota COFINS da SAFX07
Notas com item ( somatório do campo 50 – Valor da Alíquota COFINS da SAFX08.
		RND105-08	Campo VL_COFINS:

Notas sem item ( campo 105- Valor da COFINS da SAFX07
Notas com item ( somatório do campo 89 – Valor da COFINS da SAFX08.
		
Registro D111 – Processo Referenciado
RNG-D111	Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro D100, que atendam aos critérios abaixo:

Vinculação: (campo ‘’15 – Vinculação da SAFX112)
             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: (campo “14 – Origem do Processo” da SAFX114)
	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”