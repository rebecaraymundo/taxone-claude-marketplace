# MTZ_ECD_Versao_Leiaute_10.0.0

> Fonte: MTZ_ECD_Versao_Leiaute_10.0.0.doc

THOMSON REUTERS

ECD

Atualização da Geração do Arquivo para atender ao Leiaute 10.00


DOCUMENTO DE REQUISITO

OS/CH	Nome	Descrição		MFS-8216	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD.		MFS-8620	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD.		CH21396/2016	Lara Aline	Ajuste na geração do campo 02 - COD_CTA_RES do I015 para os livros auxiliares (A e Z).		MFS-9689	Lara Aline	Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. De acordo com as orientações do PVA versão 4.0.0.		MFS9809/
CH2989/2017	Andrea Rocha	Atualização das informações do bloco K		MFS10727	Lara Aline	Ajuste na regra do Campo 02 – COD_PLAN_REF do Registro I051.		MFS-10358	Lara Aline	Atualização das Informações do arquivo da ECD para atender o Bloco K na versão 5.00 do Leiaute da ECD.		CH8476_2017 (MFS-10940)	Julyana Perrucini	Alteração da regra de preenchimento do campo 03 do Registro J930.		MFS-13062	Julyana Perrucini	Este documento tem como objetivo criar parametrização na tela de Dados para que o usuário possa informar como deseja gerar o Registro I015, se pela conta parametrizada em Livros Auxiliares ao Diário sem associação da conta analítica com a sintética ou se pela associação da conta analítica com a conta sintética.		MFS15525	João Henrique	Este documento tem como objetivo realizar a primeira parte das atualizações do SPED Contábil nos registros I010, J100, J150 e J210.		MFS15698	João Henrique	Este documento tem como objetivo realizar a segunda parte das atualizações do SPED Contábil. Nos registros J100, J150 e J210 será incluído o campo com a informação das Notas Explicativas através da SAFX257 ou da Tela de Manutenção das Notas Explicativas dos Demonstrativos Contábeis.		MFS11946	João Henrique	Esse documento tem como objetivo criar a regra de preenchimento do código do participante para os registros 0150 e 0180 quando a empresa não possui movimentação contábil. 		MFS17214	João Henrique	Esse documento tem como objetivo realizar o tratamento no preenchimento do campo 08 PER_CONS do registro K100 do ECD.		MFS17883	João Henrique	Essa atualização legal tem como objetivo atender o Ato ADE Cofis nº27/2018. As alterações são nos registros I051, J100. J150, J210.		MFS18238	João Henrique	Essa alteração tem como finalidade mapear diversas contas de empresas controladas a uma determinada conta analítica do plano de contas.		MFS23322	João Henrique	Essa demanda tem como objetivo realizar a segunda parte das atualizações do SPED Contábil 2019 nos registros I010 e I200 em relação a geração do arquivo magnético.		MFS22414	João Henrique	Essa demanda tem como objetivo realizar a terceira parte das atualizações do SPED Contábil 2019 referente ao bloco J – Demonstrações Contábeis.		MFS26093	Andréa Rocha	Essa demanda tem como objetivo criar a regra para a geração do registro J005.		MFS-31598	Jorge Neto	Geração dos registros do bloco K somente em dezembro		MFS-29278	Alessandra Cristina Navatta	Ajustar as regras da recuperação das demonstrações contábeis, considerando a nova solução criada nas demandas da reestruturação da ECD (tela Geração das Demonstrações Contábeis).		MFS-32554	Alessandra Cristina Navatta	Atualização Leiaute 8 - Criação do Leiaute 8 na tela de Geração e Registro I010 ( RN00 e RNI010-03).		MFS-32555	Alessandra Cristina Navatta	Inclusão de três campos no registro 0000, para o atendimento ao leiaute 8.00 (RN0000-21, RN0000-22 e RN0000-23).		MFS-32556	Alessandra Cristina Navatta	Atualização Leiaute 8 - Atualização do Registro I051: Plano de Contas Referencial

Exclusão do Campo 02 – COD_PLAN_REF do Registro I051 (RNI051-02).
		MFS-32557	Alessandra Cristina Navatta	Atualização Leiaute 8 - Atualização do Registro J150: Demonstração do Resultado do Exercício (DRE) (RNJ150-02, RNJ150-04, RNJ150-06, RNJ150-08, RNJ150-09, RNJ150-10, RNJ150-11, RNJ150-12, RNJ150-13).		MFS33331	Andréa Rocha	Alteração da regra do campo 20 do registro 0000.		MFS-35407	Alessandra Cristina Navatta	Gerar as demonstrações contábeis no arquivo, se as mesmas foram processadas na tela de demonstração contábil (considerando o período da geração do arquivo) e se as mesmas estiverem geradas e selecionadas no perfil de geração. 		MFS-43186	Alessandra Cristina Navatta	Permitir também a geração dos registros do bloco K na data da situação especial.		MFS-48442	Alessandra Cristina Navatta	Atualização Leiaute 9 - Criação do Leiaute 9 na tela de Geração e Registro I010 (RN00 e RNI010-03).		MFS-58029	Andréa Rocha	Inclusão da documentação da regra do campo 3 do registro I050.		MFS-58158	Alessandra Cristina Navatta	Inclusão de validação para campos de valor que ultrapassar a quantidade de 16 inteiros (RN00)		MFS-62532	Rogério Ohashi	Correção na geração dos Registros I155, para não considerar os lançamentos dos Saldos no arquivo Meio Magnético, se a conta contábil estiver inativada. (RNI155-00).		MFS-62417	Rogério Ohashi	Alteração na regra do parâmetro “Gerar Plano de Contas” da Aba Dados Iniciais, referente as opções: “Somente contas movimentadas no ano da geração” e “Somente contas + centro de custo movimentados no ano da geração”, que passam a considerar o Ano Completo e não mais “até a Data de geração”.
		MFS-64587	Rogério Ohashi	Alteração na geração dos Registros I155, para não considerar os lançamentos dos Saldos no arquivo Meio Magnético, se a conta contábil estiver inativada e não houver a mesma conta com validade anterior como campo   Ativa. (RNI155-00).		MFS-64717	Rogério Ohashi	Inclusão da documentação da regra do campo 19 do Registro 0000.		MFS-64717	Rogério Ohashi	Ajustes na geração dos Campos 08 – VL_CTA_INI e 10 – VL_CTA_FIN referente ao Balanço Patrimonial (Registro J100 da ECD) - Saldos por Moeda Funcional.		MFS-65781	Rogério Ohashi	Ajustes na regra de geração do Campo 11 – IND_SIT_ESP, retirando os códigos de situação especial ‘0’, ‘5’ e ‘6’, não existentes na Tabela de Situação Especial da Receita Federal (Códigos válidos: “1 – Cisão”, “2 – Fusão”, “3 – Incorporação”, “4 – Extinção”)		MFS-66158	Rogério Ohashi	Correção na regra de geração dos Registros do Bloco K, as contas contábeis utilizadas nas escriturações contábeis consolidadas, devem ser informados nos Registro I050 e I051. 		MFS-67621	Rogério Ohashi	Alteração da regra na geração dos Registros J100 - Campo 12, J150 - Campo 13 e J210 – Campo 09, (NOTA_EXP_REF) para recuperar as informações do Campo 07, da Tabela SAFX257, conforme orientação do Manual do Guia Prático.		MFS-68575	Rogério Ohashi	Tratamento da regra de geração do Registro I050 e filhos para considerar o parâmetro “Ordenar Plano de Contas p/ Indicador de Natureza” da tela de Dados Iniciais. (RNI050-00)		MFS-76512	Alessandra Cristina Navatta	Atualização Leiaute 10 - Criação do Leiaute 10.00 na tela de Geração e Registro I010 (RN00 e RNI010-03).

*Atenção: *Conforme alinhamento em planning, não integrar as alterações no produto, pois, ainda o layout não foi disponibilizado pelo governo. A solução inicialmente, só será desenvolvida e testada no produto DW.Também não foi escopo da demanda ajustar os manuais do produto, pois, não sabemos de fato a versão disponibilizada pela Receita.
		MFS-83352	Rogério Ohashi	Correção na regra de geração dos Registros do Bloco K, as contas contábeis utilizadas nas escriturações contábeis consolidadas, devem ser informados nos Registro I050 e I051, se a Empresa Participante não for o próprio declarante da ECD.		MFS-414780	Rogério Ohashi	Tratamento na geração dos Registros I015, I050 e filhos para serem desconsiderados caso não estiverem parametrizados na Tela de “Livros Auxiliares ao Diário”.		MFS-532288	Rogério Ohashi	Readequação da Regra para Geração do arquivo Meio Magnético para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, recuperando o Saldo das Tabelas SAFX02/SAFX226 e SAFX80/SAFX227, da mesma conta contábil para o mesmo período.		MFS-HYPERLINK "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/837670" \o "https://dev.azure.com/tr-ggo/mastersaf%20fiscal%20solutions/_workitems/edit/837670" \t "_blank"837670	Rogério Ohashi	Alteração na Regra de geração do Registro J215, para gerar somente se houver movimentação no Registro J210, conforme orientação do Manual do Guia Prático.		MFS-843628	Rogério Ohashi 	Alteração na Regra de geração do Registro 0000, para os campos 06 – CNPJ e 18 - COD_SCP, alterando a regra de geração entre os campos, conforme orientação do Manual do Guia Prático.		
REGRAS DE NEGÓCIO


CÓD	DESCRIÇÃO	OS/CH		RN00	Regra Geral

Este documento tem como objetivo demonstrar as alterações da versão 10.00 do leiaute da ECD em relação à versão9.00. Este novo leiaute será obrigatório a partir do ano-calendário 2021.

Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão.

Ao efetuar a geração, se algum registro for gerado com campo de valor com mais de 16 posições na parte dos inteiros, exibir a mensagem no log por registro. “Campo de valor com tamanho inválido. Favor rever este cenário, pois, o tamanho do campo excede o especificado no manual do PVA.” Apresentar na mensagem, a linha que foi identificada a situação.
	MFS-48442
MFS-58158
MFS-76512		

Alterações Registro 0000

CÓD	DESCRIÇÃO	OS/CH		RN0000-06	

Registro 0000 – Campo 06 – CNPJ – Específico para Empresas por SCP

[ALTERAÇÃO- MFS-843628] Alteração geração do CNPJ do Sócio Ostensivo (SCP)

Para as empresas que operam sob o regime de Sociedade em Conta de Participação (SCP), é necessário preencher este campo com o CNPJ do sócio ostensivo, conforme orientação do Manual do Guia Prático. A recuperação dessa informação deverá ser realizada conforme regra abaixo: 

   Se o campo "Tipo de ECD" no menu Parâmetros > Dados Iniciais esteja preenchido com "ECD da SCP", então

     Recuperar a informação do CNPJ do Sócio Ostensivo no caminho: Data Warehouse > Manutenção > Cadastros > Cadastro por SCP > COD_SCP.

  Se o campo IND_TIPO_ECD da tabela SPED_DADOS_INI estiver preenchida igual “2”
   Gravar com o campo COD_SCP da tabela X2057_COD_SCP
  Senão gravar com o campo CGC da tabela ESTABELECIMENTO
	MFS-843628		RN0000-11	Registro 0000 – Campo 11 – IND_SIT_ESP

Este campo será gerado somente quando há situação especial, cenário identificado através do Cadastro do Estabelecimento (Módulo Parâmetros / Menu Preliminares > Empresa/Estabelecimento) do estabelecimento que está gerando o arquivo (centralizador, quando a geração é centralizada e o próprio estabelecimento descentralizado, quando a geração é descentralizada).

Para saber se ocorreu situação especial, verificar se, para o período parametrizado, há no cadastro do estabelecimento selecionado um dos campos que indicam data de situação especial preenchido com a mesma data inicial ou se o primeiro dia da Data Inicial for diferente de ‘01’ e a data de situação especial for igual a Data Inicial – 1 (último dia do mês anterior) parametrizada para geração do arquivo, considerando:

Se o campo “Data Cisão” estiver com a mesma data informada no campo Data Final de geração, Ou
  Se o dia da Data Inicial (DD) <> de ’01’ E “Data Cisão” estiver com a mesma data no campo Data Inicial -1, este campo será gerado com conteúdo “1”.

Se o campo “Data Fusão” estiver com a mesma data informada no campo Data Final de geração, Ou
  Se o dia da Data Inicial (DD) <> de ’01’ E “Data Fusão” estiver com a mesma data no campo Data Inicial -1, este campo será gerado com conteúdo “2”.

Se o campo “Data Incorporação” estiver com a mesma data informada no campo Data Final de geração, Ou
  Se o dia da Data Inicial (DD) <> de ’01’ E “Data Incorporação” estiver com a mesma data no campo Data Inicial -1, este campo será gerado com conteúdo “3”.

Se o campo “Data Encerramento” estiver com a mesma data informada no campo Data Final de geração, Ou
  Se o dia da Data Inicial (DD) <> de ’01’ E “Data Encerramento” estiver com a mesma data no campo Data Inicial -1, este campo será gerado com conteúdo “4”.

[ALTERAÇÃO-MFS-65781] Atualização códigos Tabela de Situação Especial

Tratamento: Retirar a regra para os códigos “0”, “5” e “6”

Se o campo “Data Inicio de Validade” estiver com a mesma data informada no campo Data Inicial de geração, este campo será gerado com conteúdo “0”.

Se o campo “Data Transformação” estiver com a mesma data informada no campo Data Final de geração, este campo será gerado com conteúdo “5”.

Se o campo “Data Transf. de Sede” estiver com a mesma data informada no campo Data Final de geração, este campo será gerado com conteúdo “6”.

Se nenhum dos campos for informado, este campo não deve ser preenchido. Esta regra atende a todas as versões de layout existentes para o arquivo da ECD.

[Alterada - MFS-41465] Se no cadastro do estabelecimento, pelo menos um dos campos “Data Cisão” “Data Fusão”, “Data Incorporação”, “Data Encerramento”, “Data Transformação” e ou Data Transf. de Sede”, estiver informado, e a data inicial de geração do arquivo for diferente da data do evento, indicada em um destes campos do cadastro do estabelecimento, este campo não deve ser preenchido.
	


MFS-41465
MFS-65781		RN0000-12	Registro 0000 – Campo 12 – IND_SIT_INI _PER 


Campo 12 – Indicador do Início do período
- Preencher com:

[ALTERADA – CH28587_2014]
0 - Normal (Início no primeiro dia do ano);
1 - Abertura;
2 - Resultante de Cisão/Fusão ou remanescente de Cisão ou realizou Incorporação;
3 - Início da obrigatoriedade da entrega da ECD no curso do ano-calendário
4 - Resultante de Transferência de Sede

Usar as seguintes regras:

[ALTERADA – CH2535_2018]
Caso estiver preenchido um dos campos 66 “DATA_CISAO”, 67 “DATA_FUSAO”, 68 “DATA_INCORPORACAO” da tabela de Estabelecimento verificar:
- Se a data inicial da geração do meio magnético corresponder ao primeiro dia do mês, o sistema gerará para o arquivo nesse campo a indicação "0"; 
[ALTERADA – MFS-41465]
- Se a data inicial da geração do meio magnético corresponder a qualquer outro dia do mês a data imediatamente posterior a indicada em um destes campos, o sistema gerará para o arquivo nesse campo a indicação "2";

Se estiver preenchido o campo Data Transf. de Sede - 95 “DAT_TRANS_SEDE” da tabela Estabelecimento se a data estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "4";

Caso a data de inicio da atividade e uma das outras datas citadas acima estiverem preenchidas e compreendidas no período considerar sempre a maior data (que deverá ser a data referente à Cisão, Fusão, Incorporação, Encerramento ou Transf. de Sede).

Se o flag indicador de obrigatoriedade de entrega de ECD na tela de geração estiver selecionado, o sistema gerará para o arquivo nesse campo a indicação "3";

Se estiver preenchido o campo 45 "Data de Inicio da Atividade" da tabela Estabelecimento e a data estiver compreendida no mesmo período de geração do meio magnético, o sistema gerará para o arquivo nesse campo a indicação "1";

Se nenhum dos campos de data (da tabela estabelecimento) citados estiver preenchido, ou se essas datas não estiverem compreendidas no período da geração do meio magnético e se o flag indicador de obrigatoriedade de entrega de ECD na tela de geração não estiver selecionado, deve ser verificado o Campo Data Inicial da Tela de geração do meio magnético, se a mesma estiver preenchida com o período de 01/01 (DD/MM), o sistema gerará para o arquivo nesse campo a indicação "0";

Critério de desempate: situações especiais ‘2’, transferência de sede ‘4’, inicio da obrigatoriedade ‘3’, abertura ‘1’ e escrituração normal ‘0’.

Obs: Campo de Preenchimento Obrigatório. 
	MFS-41465		RN0000-13	Registro 0000 – Campo 13 – IND_NIRE

Campo 13 – Indicador de Existência de NIRE

Preencher com ‘0’ se o campo NIRE da tabela REGISTRO_ESTADUAL referente ao estabelecimento selecionado na tela de geração não estiver preenchido.

Preencher com ‘1’ se o campo NIRE da tabela REGISTRO_ESTADUAL referente ao estabelecimento selecionado na tela de geração estiver preenchido.

Obs: Campo de preenchimento Obrigatório

	OS3835		RN0000-14	Registro 0000 – Campo 14 – IND_FIN_ESC

Indicador de Finalidade de Escrituração

Preencher com ‘0’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘0 – Original’;
Preencher com ‘1’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘1 – Substituta’

Campo de preenchimento obrigatório. 
	MFS-8216		RN0000-16	[EXCLUÌDO] Registro 0000 – Campo 16 – NIRE_SUBST.

Este campo foi excluído a partir do layout da versão 5.00. 

Importante: Deverá ser reposicionada a numeração dos campos posteriores.	MFS-8216		RN0000-18	
Registro 0000 – Campo 18 – COD_SCP– Específico para Empresas por SCP

[ALTERAÇÃO- MFS-843628] Alteração geração do CNPJ do Sócio Ostensivo (SCP)

Para as empresas que operam sob o regime de Sociedade em Conta de Participação (SCP), é necessário preencher este campo com o CNPJ da SCP, conforme orientação do Manual do Guia Prático. A recuperação dessa informação deverá ser realizada conforme regra abaixo: 

   Se o campo "Tipo de ECD" no menu Parâmetros > Dados Iniciais esteja preenchido com " ECD da SCP ", então

     Recuperar a informação do CNPJ do Estabelecimento no caminho: Parâmetros > Preliminares > Empresa/Estabecimento > CNPJ.

  Se o campo IND_TIPO_ECD da tabela SPED_DADOS_INI estiver preenchida igual “2”
   Gravar com o campo CGC da tabela ESTABELECIMENTO
    Senão gravar nulo
	MFS-843628		RN0000-19	Registro 0000 – Campo 19 – IDENT_MF

Identificação de moeda funcional: Indica que a escrituração abrange valores com base na moeda funcional (art. 287 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017). 

Este campo será preenchido conforme parâmetro na tela de Dados Iniciais no caminho: SPED >> ECD - Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais.
    
    [  ] ECD com Movimentação em Moeda Funcional

    - Quando marcado – Na geração do arquivo magnético o Campo 19 – IDENT_MF será preenchido com “S”
    - Quando desmarcado – Na geração do arquivo magnético Campo 19 – IDENT_MF será preenchido com “N”.
	MFS64717		RN0000-20	Registro 0000 – Campo 20 – IND_ESC_CONS

Este campo existe a partir da versão 5.00. Inicialmente será gerado com conteúdo fixo: “N”

Será gerado conforme parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros):
    Se o referido parâmetro estiver desmarcado
         Será gerado com conteúdo “N”.

[MFS33331]
    Se o parâmetro estiver marcado e o campo 11 – IND_SIT_ESP estiver vazio e o mês final da geração for igual a dezembro ou  se o campo 11 – IND_SIT_ESP estiver preenchido e a data final da geração for igual a data da situação especial.
          Será gerado com conteúdo “S”
    Senão 
          Será gerado com conteúdo “N”.	MFS-8216
MFS-10358
MFS-33331
MFS-43186		RN0000-21	Registro 0000 – Campo 21 – IND_CENTRALIZADA

Este campo deve ser gerado a partir da versão 8.00.

Será gerado ‘0’, se na tela de geração do meio magnético o estabelecimento que está processando o arquivo for centrazador, caso seja descentralizador, gerar ‘1’.
	MFS-32555		RN0000-22	Registro 0000 – Campo 22 – IND_MUDANC_PC

Este campo deve ser gerado a partir da versão 8.00.

Será gerado ‘0’, se na tela de geração do meio magnético o parâmetro ‘Houve Mudança no Plano de Contas’ estiver desmarcado, caso contrário, preencher com ‘1’.
	MFS-32555		RN0000-23	Registro 0000 – Campo 23 – COD_PLAN_REF


Este campo deve ser gerado a partir da versão 8.00.

Será gerado de acordo com a informação cadastrada na tela de Dados Iniciais no campo Entidade Responsável pelo Plano Referencial. Preencher com:

‘1’, se o campo estiver preenchido com ‘PJ em Geral’ 
‘2’ se o campo estiver preenchido com ‘PJ em Geral – Lucro Presumido’
‘3’ se o campo estiver preenchido com ‘Financeiras’ 
‘4’ se o campo estiver preenchido com ‘Seguradoras‘
‘5’ se o campo estiver preenchido com ‘Imunes e Isentas em Geral’ 
‘6’ se o campo estiver preenchido com ‘Financeiras - Imunes e Isentas’
‘7’ se o campo estiver preenchido com ‘Seguradoras - Imunes e Isentas’
‘8’ se o campo estiver preenchido com ‘Entidades Fechadas de Previdência Complementar’ 
‘9’ se o campo estiver preenchido com ‘Partidos Políticos’ 
‘10’ se o campo estiver preenchido com ‘Financeiras – Lucro Presumido’
 	MFS-32555		


Alterações Registro 0150

CÓD	DESCRIÇÃO	OS/CH		RN0150-02	Registro 0150 – Campo 02 – COD_PART

Se o parâmetro “Gerar Código do Participante (SAFX39) ” estiver marcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais):

Buscar o  GRUPO_ESTAB da tabela RELAC_TAB_GRUPO com maior validade inicial.

A rotina de geração deverá verificar os registros da SAFX39 - Identificação do Relacionamento e realizar a seguinte validação: Verificar se os registros da tabela em que a DT_INI_REL for <= que a data final do arquivo ECD E a DT_FIN_REL for > = a data inicial do arquivo ECD OU for ‘nula’ <= que a data final de geração do arquivo da ECD.

Através da maior data de validade, buscar o IDENT_FIS_JUR que possua o mesmo Grupo, COD_FIS_JUR e IND_FIS_JUR,  demais informações na SAFX04 para geração dos registros 0150.

Caso não possua registros na SAFX04, o sistema não irá gerar o registro 0150.

Se o parâmetro “Gerar Código do Participante (SAFX39) ” estiver desmarcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais) a regra de geração deve se manter inalterada, gerando a partir do participante movimentado (na SAFX01).	
MFS-11946		


Alterações Registro 0180

CÓD	DESCRIÇÃO	OS/CH		RN0180-02	Registro 0180 – Campo 03 – COD_REL

Se o parâmetro “Gerar Código do Participante (SAFX39)” estiver marcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais), o sistema deverá recuperar o código  de relacionamento
do participante da SAFX39 localizado tela de cadastro da Pessoa Física/Jurídica onde a DT_INI_REL for <= que a data final do arquivo ECD E a DT_FIN_REL for > = a data inicial do arquivo ECD OU for ‘nula’ <= que a data final de geração do arquivo da ECD.

Se o parâmetro “Gerar Código do Participante (SAFX39)” estiver desmarcado na tela de Dados Iniciais (SPED >> ECD – Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais) a regra de geração deve se manter inalterada, gerando a partir do participante movimentado (na SAFX01).
	
MFS-11946		

Alterações Registro I010

CÓD	DESCRIÇÃO	OS/CH		RNI010-03	Registro I010 – Campo 03 – COD_VER_LC

Para a versão 5.00, será gerado com o código “5.00”. 
Para a versão 6.00, será gerado com o código “6.00”. Essa atualização se faz necessária a partir do ano calendário de 2017.
Para a versão 7.00, será gerado com o código “7.00”. Essa atualização se faz necessária a partir do ano calendário de 2018.
Para a versão 8.00, será gerado com o código “8.00”. Essa atualização se faz necessária a partir do ano calendário de 2019.
Para a versão 9.00, será gerado com o código “9.00”. Essa atualização se faz necessária a partir do ano calendário de 2020.
Para a versão 10.00, será gerado com o código “10.00”. Essa atualização se faz necessária a partir do ano calendário de 2021.


	MFS-8216
MFS-15525
MFS23322
MFS-32554
MFS-48442
MFS-76512		
Alterações Registro I015

CÓD	DESCRIÇÃO	OS/CH		RNI015-02	Registro I015 – Campo 02 – COD_CTA_RES

[ALTERADA – MFS-13062]
Se a opção “Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário”, localizada na aba Dados Iniciais da tela Dados Iniciais do item de menu Parâmetros da ECD, estiver desmarcada, então:

Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta sintética (campo COD_CONTA_SINT da SAFX2002) associada à conta analítica movimentada encontrada, nesse caso será gerada sempre a primeira conta sintética encontrada. Exemplo:

Conta
Tipo
Conta Pai
Nível


1.1.1
S

1


1.1.1.01
S
1.1.1
2


1.1.1.01.0001
A
1.1.1.01
3


1.1.1.01.0001.01
A
1.1.1.01.0001
4


------\\------


Livros Auxiliares ao Diário
1.1.1.01.0001


Auxiliar


Como deve ser gerado:


I015 - 1.1.1.01


I050 - 1.1.1


I050 - 1.1.1.01


I050 - 1.1.1.01.0001


No caso do exemplo acima para a conta analítica 1.1.1.01.0001 está associada a conta sintética 1.1.1.01, que será gerado no registro I015 para os livros ‘A’ ou ‘Z’.

Obs.: Para os outros Livros a geração desse campo continua conforme o padrão, ou seja, gerando a conta analítica movimentada encontrada.

Se a opção “Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário”, localizada na aba Dados Iniciais da tela Dados Iniciais do item de menu Parâmetros da ECD, estiver marcada, então:

Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta contábil parametrizada em Livros Auxiliares ao Diário, localizada no item de menu Parâmetros da ECD, sem a necessidade de associar a conta sintética.

[ALTERADA-MFS-414780] Tratamento p/ contas não parametrizadas “Livros Auxiliares ao Diário”

Para os Livros auxiliares “A” ou “Z”, o sistema deverá considerar os Registros I015, I050 e filhos, somente, se as contas estiverem parametrizadas na tela de parâmetro “Livros Auxiliares ao Diário”, respeitando o cadastro por “Livro” + “Tipo de Livro”, (Registro I012). 
Ou
  Se a conta estiver parametrizado na tela de parâmetro “Livros Auxiliares ao Diário”, e não for identificado movimento/ou saldo para conta;
        Desconsiderar a conta do arquivo meio magnético. 

Obs¹: A geração deverá respeitar o parâmetro “Gerar Plano de Contas”, na Aba Dados Iniciais.
Obs²: O mesmo tratamento deverá ser aplicado para os Registros I500 e filhos (Registros que são utilizados exclusivamente para escriturações do tipo “Z” são: I500, I510, I550 e I555).

	CH21396_2016
MFS-13062
MFS-414780		
Alterações Registro I050

CÓD	DESCRIÇÃO	OS/CH		RNI050-00	Registro I050

Aba Dados Iniciais – Gerar Plano de Contas

[ALTERADA – MFS-62417]

Tratamento:

Alterar regra das opções:

- Somente contas movimentadas no ano da geração;
- Somente contas + centro de custo movimentados no ano da geração.

Caso uma dessas opções seja selecionado o programa deverá pesquisar se houve movimentação de lançamentos ou saldos:

   - Pesquisar o período completo de janeiro a dezembro das tabelas de lançamentos e/ou saldos;
      Se encontrar gravar a conta no Registro I050 para todos os meses;
        Senão desconsiderar a conta do arquivo meio magnético.

[ALTERADA - MFS-68575] Tratamento p/ considerar o parâmetro “Ordenar Plano de Contas p/ Indicador de Natureza”

Aba Dados Iniciais – Ordenar Plano de Contas p/ Indicador de Natureza

Na geração do Meio Magnético o sistema deverá considerar o parâmetro “Ordenar Plano de Contas p/ Indicador de Natureza”, e seguir conforme regras abaixo:

Parâmetro Desmarcado: O sistema deverá gerar os Registros I050 e filhos conforme regra atual ordenando pelo Campo COD_CONTA da tabela X2002_PLANO_CONTAS.

Parâmetro Marcado: O sistema deverá gerar os Registros I050 e filhos passando a considerar na ordenação o Campo IND_NATUREZA e o Campo COD_CONTA da tabela X2002_PLANO_CONTAS.

Default: Desmarcado.
	

MFS-62417
MFS-68575
MFS-414780		RNI050-03	Registro I050 – Campo 03 – COD_NAT

Será gerado com o conteúdo do campo 7-Indicador de Natureza da SAFX2002. 

Será preenchido de acordo com:
Se Indicador de Natureza = “0”
     Preencher com “05”
Se Indicador de Natureza = “1”
     Preencher com “01”
Se Indicador de Natureza = “2”
     Preencher com “02”
Se Indicador de Natureza = “3”
     Preencher com “04”
Se Indicador de Natureza = “4”
     Preencher com “04”
Se Indicador de Natureza = “5”
     Preencher com “09”
Se Indicador de Natureza = “6”
     Preencher com “09”
Se Indicador de Natureza = “7”
     Preencher com “03”
Se Indicador de Natureza = “8”
     Preencher com “04”
Se Indicador de Natureza = “9”
     Preencher com “09”

Obs.: A regra foi definida conforme está sendo feita a geração.  A MFS58029 foi aberta apenas para documentar a regra.

[ALTERADA-MFS-414780] Tratamento p/ contas não parametrizadas “Livros Auxiliares ao Diário”

Para os Livros auxiliares “A” ou “Z”, o sistema deverá considerar o Registro I050 e filhos, somente, se as contas estiverem parametrizadas na tela de parâmetro “Livros Auxiliares ao Diário”, respeitando o cadastro por “Livro” + “Tipo de Livro”, (Registro I012). 
Ou
  Se a conta estiver parametrizado na tela de parâmetro “Livros Auxiliares ao Diário”, e não for identificado movimento/ou saldo para conta.
        Desconsiderar a conta do arquivo meio magnético. 

Obs: A geração deverá respeitar o parâmetro “Gerar Plano de Contas”, na Aba Dados Iniciais.
		

Alterações Registro I051

CÓD	DESCRIÇÃO	OS/CH		RNI051-02	Registro I051 – Campo 02 – COD_PLAN_REF

A partir da versão 5.00 nesse campo foi incluído um novo Código da Entidade “10- Financeiras – Lucro Presumido” e foi alterado o tamanho do campo para 2 posições.

A partir da versão 5.00 este registro será gerado apenas quando o Código da Entidade for igual a “1 - PJ em Geral”, ”2 - PJ em Geral - Lucro Presumido”, “3 – Financeiras”, “4 – Seguradoras”, “5 - Imunes e Isentas em Geral”, “6 - Financeiras - Imunes e Isentas”, “7 - Seguradoras - Imunes e Isentas”, “8 - Entidades Fechadas de Previdência Complementar”, “9 - Partidos Políticos”. ou “10- Financeiras – Lucro Presumido/ Secretaria da Receita Federal” ou “10 – Financeiras – Lucro Presumido”, (obs. A partir de 2015)


Caso o usuário não tenha realizado parametrização para uma destas entidades indicadas acima em Dados Iniciais e/ou Plano de Contas Referencial X Plano de Contas Empresa e esteja gerando a versão 5.00 do Leiaute, será demonstrada uma mensagem no log: “A partir da versão 5.00 do leiaute não serão válidas as Contas Referenciais de entidade 00-SUSEP ou 20- Banco Central do Brasil (COSIF)”.


A partir da versão 8.00 do leiaute, este campo não deve ser mais gerado. Ele foi inserido no registro 0000 – campo 23 - COD_PLAN_REF
	MFS8620
MFS10727
MFS17883
MFS32556		

Alterações Registro I052

CÓD	DESCRIÇÃO	OS/CH		RGI052	Regra Geral

Se os registros J100 E J150 estiverem preenchidos com o indicador 03 – IND_COD_AGL, campos 07 e 08 da SAFX2102 DIFERENTE de ‘T’, o código de aglutinação, campo 02 – COD_ALG deve ser apresentado no registro I052.

Então, são gerados no registro I052 apenas as aglutinações de detalhe:

Balanço Patrimonial – J100
Se o código de aglutinação for classificado como “1 - Ativo” ou “2 - Passivo” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “D”.

Demonstração de Resultado do Exercício – J150
Se o código de aglutinação for classificado como “1 – Receita/Despesa” ou “3 - Receita” ou “4 - Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD, esse campo é preenchido com a opção “D”.
	MFS-22414		
Alterações Registro I053

CÓD	DESCRIÇÃO	OS/CH		RNI053-00	Registro I053 – Regra Geral

Origem das informações: Tela de Subcontas Correlatas (Módulo ECD / Menu Manutenção)

Regra de Seleção: Este registro será gerado sempre que, na tela de Subcontas Correlatas existir algum registro associando a conta contábil informada no I050 as subcontas correlatas que tenham movimentação.

Campo-chave: COD_CNT_CORR

Registro pai / Nível hierárquico: I050 / Nível 4

Ocorrência: vários por plano de Contas

Obs.: As subcontas correlatas são utilizadas para registro das diferenças positivas/negativas de ativo/passivo, serão analíticas e registrarão os lançamentos contábeis das diferenças (efeito p/ controle societário) em último nível.

	OS4745		RNI053-01	Registro I053 – Campo 01 – REG

Informação fixa “I053”.
	OS4745		RNI053-02	Registro I053 – Campo 02 – COD_IDT

Será gerado com o conteúdo do campo Gr. Conta-Subconta da tela de Subconta Correlata.	OS4745		RNI053-03	Registro I053 – Campo 03 – COD_CNT_CORR

Será gerado com o conteúdo do campo Subconta Correlata da tela de Subconta Correlata.

[CH22230/2015] Para o código de conta contábil informado neste campo também deve ser gerado o cadastro correspondente o registro I050.
	OS4745
22230/2015		RNI053-04	Registro I053 – Campo 04 – NAT_SUB_CNT

Será gerado com o conteúdo do campo Natureza da Subconta da tela de Subconta Correlata.

Não deverão ser considerados os códigos de Natureza da Subconta que estejam fora do período de validade na TACES90. 
	MFS-8216		
Alterações Registro I155

CÓD	DESCRIÇÃO	OS/CH		RNI155-00	Registro I155 – Regra geral

Origem da Informação: SAFX02 - Arquivo de Saldos Mensais, SAFX80 - Arquivo de Saldos Contábeis para Centro Custo, SAFX102 - Arquivo de Saldos Mensais Auxiliar, SAFX226 - Saldo Contábil em Moeda Funcional, SAFX227 - Saldo Contábil por Centro de Custo em Moeda Funcional e SAFX229 - Saldo Contábil Auxiliar em Moeda Funcional.

Regra de geração: Quando a empresa tem movimentação em Moeda Funcional (Parâmetro “ECD com Movimentação em Moeda Funcional” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4.00”, a estrutura do registro I155 será gerada conforme definida neste documento e considerando, além das tabelas já utilizadas atualmente, as tabelas de movimentação em Moeda Funcional indicadas no item “Origem da Informação”.

Devem ser respeitadas as regras atuais de recuperação dos registros, demonstrando o I155 como filho do I150 e recuperando os saldos cuja data da operação compreenda o período demonstrado no registro pai. 

Se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”.

Para geração dos saldos dos Livros Geral, Resumido e Balancete, devem ser considerados registros das tabelas SAFX02 - Arquivo de Saldos Mensais, SAFX80 - Arquivo de Saldos Contábeis para Centro Custo, SAFX226 - Saldo Contábil em Moeda Funcional e SAFX227 - Saldo Contábil por Centro de Custo em Moeda Funcional, sendo que, registros das SAFX80 e SAFX227 somente devem ser considerados se a opção “Omitir informações de Centro de Custo em Lançamentos Contábeis e Saldos” não estiver selecionada. Se esta opção estiver selecionada, considerar os registros carregados nestas tabelas e caso exista nas tabelas SAFX02 e SAFX226 registros da mesma empresa, estabelecimento, período e conta, desprezar os registros correspondentes das SAFX02 e SAFX226 e considerar somente o informado nas SAFX80 e SAFX227.

Para geração dos saldos do Livro Auxiliar, devem ser considerados registros das tabelas SAFX102 - Arquivo de Saldos Mensais Auxiliar e SAFX229 - Saldo Contábil Auxiliar em Moeda Funcional, considerando registros cuja conta contábil tenha sido parametrizada na tela de Livros Auxiliares ao Diário (menu parâmetros) para o Livro selecionado na tela de geração do meio magnético.

Tanto as tabelas de movimentação normal quanto as de movimentação em moeda funcional devem servir de base para geração deste registro. Podemos ter situação onde teremos valores em moeda funcional, mas não teremos em moeda corrente (o contrário também é possível), neste caso, as colunas no registro onde os valores em moeda corrente seriam demonstrados serão apresentados zerados.

Agrupamento: campos 02 – COD_CTA e 03 – COD_CCUS

Quando a empresa não tem movimentação em Moeda Funcional (Parâmetro “ECD com Movimentação em Moeda Funcional” não selecionado na tela de Dados Iniciais – menu Parâmetros), a geração deste registro se mantém inalterada.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional.

[ALTERADA-MFS62532 - MFS64587]

Tratamento: Não considerar os lançamentos dos Saldos quando a conta contábil estiver inativada na tabela SAFX2002 (Plano de conta)  
 
      Se a conta contábil da tabela “X2002_PLANO_CONTAS” (Maior Validade), o campo “IND_SITUACAO” estiver preenchido com “I”;
        E se não houver a mesma conta contábil com Data de Validade anterior (cadastrada no Plano de Contas) com o campo “IND_SITUACAO” preenchido com “A”;  
         Então não considerar o Saldo das tabelas SAFX02, SAFX80, SAFX102, SAFX226, SAFX227 e SAFX229 na geração do Registro I155 no arquivo Meio Magnético.

 [ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros I155, recuperando as informações de Saldos das tabelas SAFX02/SAFX102/SAFX226 e SAFX80/SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros I155 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	MFS-2632


MFS-62532
MFS-64587
MFS-532288		

Alterações Registro I200

CÓD	DESCRIÇÃO	OS/CH		RNI200-05	Registro I200 – Campo 05 – IND_LCTO

Neste campo são apresentadas as opções do “Indicador do Tipo de Lançamento”, recuperado através do TIPO_LANCTO.

Regras:
As opções válidas para o campo são:

‘N’ – Lançamento Normal (todos os lançamentos exceto os de encerramento das contas de resultado).
‘E’ – Lançamento de Encerramento de contas de resultado.
‘X’ – Lançamento Extemporâneo – Nova Opção (MFS-22309)

As validações necessárias encontram-se na Importação/Manutenção das SAFX.

Cada SAFX é destinada a um tipo de livro na geração do arquivo da ECD:
SAFX01 - Arquivo ContábilSAFX101 - Arquivo Contábil AuxiliarSAFX225 - Lançamento Contábil em Moeda FuncionalSAFX228 - Lançamento Contábil Auxiliar em Moeda Funcional

Tipo: Alfanumérico
Tamanho: 1 Posição
	MFS23322		RNI200-06	Registro I200 – Campo 06 – DT_LCTO_EXT

Neste campo o usuário informa a Data do Lançamento Extemporâneo, se o “Indicador de Lançamento” estiver preenchido com a opção “X”. As validações necessárias encontram-se na Importação/Manutenção das tabelas:

SAFX01 - Arquivo ContábilSAFX101 - Arquivo Contábil AuxiliarSAFX225 - Lançamento Contábil em Moeda FuncionalSAFX228 - Lançamento Contábil Auxiliar em Moeda Funcional

Tipo: Numérico
Tamanho: 8 Posições
	MFS-22309		
Alterações Registro I250

CÓD	DESCRIÇÃO	OS/CH		RNI250-00	Registro I250 – Regra geral

Origem da Informação: SAFX01 - Arquivo Contábil, SAFX101 - Arquivo Contábil Auxiliar, SAFX225 - Lançamento Contábil em Moeda Funcional, SAFX228 - Lançamento Contábil Auxiliar em Moeda Funcional.

[ALTERADA-MFS523925]

Tratamento: Não considerar os lançamentos contábeis quando a conta contábil estiver inativada na tabela SAFX2002 (Plano de conta)  
 
      Se a conta contábil da tabela “X2002_PLANO_CONTAS” (Maior Validade), o campo “IND_SITUACAO” estiver preenchido com “I”;
        E se não houver a mesma conta contábil com Data de Validade anterior (cadastrada no Plano de Contas) com o campo “IND_SITUACAO” preenchido com “A”;  
         Então não considerar os Lançamentos das tabelas SAFX01, SAFX101, SAFX225, SAFX228 na geração dos Registros I200/I250 no arquivo Meio Magnético.

	MFS523925		Alterações Registro J005

CÓD	DESCRIÇÃO	OS/CH		RNJ005	Regra Geral – Registro J005

[EXCLUÍDA MFS-29278]
O registro J005 somente será gerado se pelo menos um dos parâmetros abaixo estiver marcado na tela de geração do meio magnético:
- Balanço Patrimonial
- Demonstração do Resultado

Obs: Esta regra só deve ser feita a partir da versão 7.00.


[Alteração MFS-29278]:
Recuperar a demonstração de acordo com o campo Período do Arquivo da ECD (tela de Geração das Demonstrações Contábeis). As demonstrações serão recuperadas se o campo do período do arquivo coincidir com o período de geração do meio magnético e o parâmetro Apenas Conferência da tela de geração das demonstrações contábeis, estiver selecionado como ‘Não’. Neste cenário, considerar a informação da geração da demonstração processada. 
[Alteração MFS-35407]
Além das regras de recuperação das demonstrações mencionadas acima, as demonstrações contábeis (bloco J) só devem ser apresentadas no arquivo, se estiverem marcadas no perfil de geração.

No caso do Início de Atividade, o campo “Data Inicio de Atividade” do Cadastro do Estabelecimento que está gerando o arquivo estará preenchido e será uma data contida no ano de geração da obrigação. Neste caso, este campo será gerado com a Data Inicio de Atividade informada no Cadastro do Estabelecimento para o primeiro J005 do arquivo. Para os próximos J005 (se existirem, conforme cenários), considerar os encerramentos do próprio ano de geração.


Observação: A data inicial das demonstrações deve ser a data posterior ao último encerramento do exercício, mesmo que essa data não esteja no período da ECD transmitida. Exemplo: Data do Último Encerramento do Exercício: 31/12/2020 Data Inicial das Demonstrações Contábeis: 01/01/2021.
	MFS-26093
MFS-29278
MFS-35407		Alterações Registro J100

CÓD	DESCRIÇÃO	OS/CH		RNJ100-00	Balanço Patrimonial – Registro J100

Deverá ser gerada uma demonstração contábil de Balanço Patrimonial se:

Na tela de geração das demonstrações contábeis se for marcada a opção Balanço Patrimonial, será considerada a parametrização da tela de Códigos de Aglutinação (B. Patrimonial/D.Resultado/DLPA/DMPL), aba Balanço Patrimonial (campo 6 – Indicador de Aglutinação (IND_BALANCO_DRE) da SAFX2102, igual a “B”), para o estabelecimento que está sendo considerado na geração.

Nesta demonstração, apenas contas com naturezas com indicador igual a 1 - Ativo, 2 - Passivo, 5 - Mutações Ativas, 6 - Mutações Passivas, 7 - Patrimônio Líquido ou 9 – Outros serão aceitas.

Serão considerados os valores dos saldos contábeis (SAFX02, SAFX80, SAFX226 ou SAFX227), das contas indicadas nas contas aglutinadoras (SAFX2103), compreendidos no período indicado na tela de geração da demonstração contábil. 

Para o cálculo serão obtidas as informações da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, consideraremos as informações da SAFX80 ou SAFX227. Na seleção da SAFX80 ou SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

Para recuperar as informações dos Saldos Contábeis, caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil” estiver mercado, o sistema deverá recuperar os valores das tabelas SAFX02/SAFX226 e SAFX80/SAFX227 da mesma conta contábil e período, caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” estiver desmarcado, caso contrário  o cálculo serão obtidas somente das informações da SAFX02/SAFX226.

Em todo o processamento, serão geradas as visões Sintética (nível de contas aglutinadoras) e também a Analítica (nível de contas contábeis) e as informações de moeda corrente e moeda funcional.


Atenção: Não será mais utilizado as informações dos registros I350 para definirmos a periodicidade das demonstrações. Serão consideradas as datas indicadas na tela de Geração das Demonstrações Contábeis. (desta forma será de responsabilidade do cliente indicar a periodicidade que o estabelecimento se enquadra).


Validações Adicionais:

Se a parametrização for encontrada, porém não existir nenhuma conta com saldo para o período, exibir a mensagem na aba de log: A demonstração de Balanço Patrimonial não será gerada, pois não foi encontrado saldos contábeis para o período. Estabelecimento: XXXX.
	


MFS-31020
MFS-532288		RNJ100-02	Registro J100 – Campo 02 – COD_AGL

Nesse campo o sistema preenche com o código da conta aglutinadora campo 03 da SAFX2102. 
	MFS-31020		RNJ100-03	Registro J100 – Campo 03 – IND_COD_AGL


[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira).

Regras:
Se o código de aglutinação for classificado como “1 - Ativo” ou “2 - Passivo” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da SAFX2102, na geração do registro J100 da ECD esse indicador é preenchido com a opção “T”.

Campo Obrigatório.
1 posição – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-22414
MFS-29278		RNJ100-04	Registro J100 – Campo 04 – NIVEL_AGL

Neste campo o sistema preenche com o nivel da conta aglutinadora, indicada no campo “nível” da SAFX2102
	MFS-31020		RNJ100-05	Registro J100 – Campo 05 – COD_ALG_SUP

[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “3 - Subtotalizador/Totalizador do Ativo” ou “4 - Subtotalizador/Totalizador do Passivo ou PL” campo 07 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe” na geração do arquivo magnético da ECD.

Exemplo:


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.


	MFS-22414
MFS-29278		RNJ100-06	Registro J100 – Campo 06 – IND_GRP_BAL

[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador de grupo do balanço campo 07 da SAFX2102. Até o layout 6.0 o campo é gerado da seguinte forma: 
‘1’ – Ativo
‘2’ – Passivo e Patrimônio Líquido
‘3’ – Subtotalizador/Totalizador do Ativo
‘4’ – Subtotalizador/Totalizador do Passivo ou PL


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis e aplicar as regras abaixo:


Regras:
A partir do layout 7.0 na geração do arquivo magnético o sistema deverá preencher da seguinte forma:
Se a opção do campo for igual a ‘1’ ou ‘3’, na geração do arquivo preencher como “A” – Ativo.
Se a opção do campo for igual a ‘2’ ou ‘4’, na geração do arquivo preencher como “P” – Passivo e Patrimônio Líquido.

Campo obrigatório
1 posição
Caractere
	MFS-22414
MFS-29278		RNJ100-07	Registro J100 – Campo 07 – DESCR_COD_AGL

Nesse campo o sistema preenche com a descrição da conta aglutinadora campo 05 da SAFX2102. 
	MFS-31020		RNJ100-08	Registro J100 – Campo 08 – VL_CTA_INI (Moeda Corrente)

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX02/SAFX102 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.


Registro J100 – Campo 08 – VL_CTA_INI (Moeda Funcional)

[ALTERAÇÃO- MFS-64717] Tratamento na geração dos valores de Saldos por Moeda Funcional

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Tratamento:

O sistema deverá considerar os Saldos por Moeda funcional quando o campo “IND_MOEDA_FUNC” da tabela “SPED_DADOS_INI” for igual a “S”.


Observação: Este campo será preenchido conforme parâmetro na tela de Dados Iniciais no caminho: SPED >> ECD - Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais>> ECD com Movimentação em Moeda Funcional.


Os valores que irão compor este campo serão obtidos com base no valor do Saldo Inicial das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data inicial indicada na tela de geração das demonstrações. 

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Inicial das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_INI será obtido com base no resultado gerado no campo VL_CTA_INI. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

	


MFS-31020
MFS-64717
MFS-532288		RNJ100-09	Registro J100 – Campo 09 – IND_DC_CTA_INI (Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX02/ Campo 7 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_INI.

Registro J100 – Campo 09 – IND_DC_CTA_INI (Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo inicial das contas contábeis que foram sumarizados na conta aglutinadora (Campo 6 da SAFX226/ Campo 7 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_INI.

	


MFS-31020		RNJ100-10	Registro J100 – Campo 10 – VL_CTA_FIN (Moeda Corrente)


Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX02 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX80.

Observar que, na seleção da SAFX80 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX02/SAFX102 e SAFX80, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

Registro J100 – Campo 10 – VL_CTA_FIN (Moeda Funcional)

[ALTERAÇÃO- MFS-64717] Tratamento na geração dos valores de Saldos por Moeda Funcional

Neste campo o Sistema deve efetuar o cálculo indicado nas regras abaixo:

Tratamento:

O sistema deverá considerar os Saldos por Moeda funcional quando o campo “IND_MOEDA_FUNC” da tabela “SPED_DADOS_INI” for igual a “S”.


Observação: Este campo será preenchido conforme parâmetro na tela de Dados Iniciais no caminho: SPED >> ECD - Escrituração Contábil Digital >> Parâmetros >> Dados Iniciais>> ECD com Movimentação em Moeda Funcional.

Os valores que irão compor este campo serão obtidos com base no valor do Saldo Final das Contas Contábeis associadas ao código de aglutinação, considerando como período de referência a data final indicada na tela de geração das demonstrações.

Teremos o seguinte cálculo: (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “D”) menos (Somatória do Valor do Saldo Final das Contas Contábeis cujo Ind. De Débito/Crédito seja igual a “C”). Mostrar sempre o valor absoluto.

O campo IND_DC_CTA_FIN será obtido com base no resultado gerado no campo VL_CTA_FIN. 

Estas informações necessárias para o cálculo serão obtidas da SAFX226 quando o campo “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” no cadastro de Dados Iniciais estiver selecionado. Se o parâmetro não estiver selecionado, considerar informações da SAFX227.

Observar que, na seleção da SAFX227 há segregação por centro de custo, mas a totalização deve considerar apenas Conta Contábil.

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J100, recuperando as informações de Saldos das tabelas SAFX226 e SAFX227, considerando a mesma Conta Contábil e período.

Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J100 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	


MFS-31020
MFS-64717
MFS-532288		RNJ100-11	Registro J100 – Campo 11 – IND_DC_CTA_FIN (Moeda Corrente)

Neste campo o sistema preenche com o indicador do saldo finall das contas contábeis que foram sumarizados na conta aglutinadora (Campo 8 da SAFX02/ Campo 11 da SAFX80), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.


Registro J100 – Campo 11 – IND_DC_CTA_FIN Moeda Funcional)

Neste campo o sistema preenche com o indicador do saldo final das contas contábeis que foram sumarizados na conta aglutinadora (Campo 8 da SAFX226/ Campo 9 da SAFX227), conforme cálculo  no campo indicado no campo  VL_CTA_FIN.

	


MFS-31020
		RNJ100-12	Registro J100 – Campo 12 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.

[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J100 com base no IND_BALANCO_DRE = ‘B’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

[ALTERAÇÃO- MFS-67621] Alteração para recuperar o Campo “NUM_REFERENCIA” para geração do Campo 12-NOTA_EXP_REF, conforme orientação do Manual do Guia Prático.

Neste campo o sistema deverá preencher com a informação do Campo  7 – NUM_REFERENCIA da Tabela SAFX257, quando o IND_BALANCO_DRE = ‘B’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).

Obs.: Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.	MFS-15525
MFS-15698
MFS-22414
MFS-29278
MFS-31025
MFS-67621		


Alterações Registro J150

CÓD	DESCRIÇÃO	OS/CH		RNJ150-00	Registro J150 – Regra Geral

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J150, recuperando as informações de Saldos das tabelas SAFX02/SAFX102/SAFX226 e SAFX80/SAFX227, considerando a mesma Conta Contábil e período.


Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J150 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.
	
MFS-532288		RNJ150-02	Registro J150 – Campo 02 – NU_ORDEM


Considerar a informação do campo ‘Ordem’ da demonstração de DRE recuperada gerada na tela de geração das demonstrações contábeis.	
MFS-32557
		RNJ150-04	Registro J150 – Campo 04 – IND_COD_AGL


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o tipo do código de aglutinação das linhas. As opções válidas são:

‘T’ – Totalizador (nível que totaliza um ou mais níveis inferiores da demonstração financeira).
‘D’ – Detalhe (nível mais detalhado da demonstração financeira)

Regras:
Se o código de aglutinação for classificado como “1 – Receita/Despesa” ou “3 - Receita” ou “4 - Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD, esse campo é preenchido com a opção “D”.
Se o código de aglutinação for classificado como “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da SAFX2102, na geração do registro J150 da ECD esse campo é preenchido com a opção “T”.

Campo Obrigatório.
1 posição – Caractere


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

	MFS-22414
MFS-29278
MFS-32557		RNJ150-06	Registro J150 – Campo 06 – COD_ALG_SUP

[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o código de aglutinação sintético/grupo de código de aglutinação de nível superior. 

Regras:
Verificar os códigos de aglutinação parametrizados no campo 10 - EXPRESSAO_ORD que são totalizadores, ou seja, opções “2 - Subtotalizador/Totalizador da DRE” ou “5 - Subtotalizador/Totalizador de Receita” ou “6 - Subtotalizador/Totalizador de Despesa” campo 08 da tabela SAFX2102 para buscar e preencher com a conta de nível superior “Conta Mãe” na geração do arquivo magnético da ECD.

Exemplo:
 EMBED PBrush  

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-32557		RNJ150-08	Registro J150 – Campo 08 –VL_CTA_INI

Considerar a informação do campo VL_CTA_INI da demonstração de DRE recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-32557		RNJ150-09	Registro J150 – Campo 09 – IND_DC_CTA_INI


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador da situação do valor total do código de aglutinação. 

As opções válidas são:
D – Devedor;
C – Credor; 

Regras:
O sistema verifica qual o indicador dos saldos das 2 parcelas:
Se as parcelas são iguais (Débito com Débito, o sistema preenche com “D” ou Crédito com Crédito preenche com “C”), somam-se ou subtraem-se os saldos conforme o operador da expressão. O indicador de débito e crédito final é igual ao das parcelas.

Se as parcelas são diferentes (Débito com Crédito), não importando se a expressão indica soma ou subtração, subtraem-se os valores e o indicador final é o da parcela de maior saldo.
Exemplo: 
Se o saldo da parcela de Débito for > que a parcela do Crédito, o sistema preenche com o indicador “D” para essa aglutinação.
Senão preenche com “C”

Campo Obrigatório.
1 posição – Caractere


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-29278
MFS-32557		RNJ150-10	Registro J150 – Campo 10–VL_CTA_FIN

Considerar a informação do campo VL_CTA_FIN da demonstração de DRE recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-32557		RNJ150-11	Registro J150 – Campo 11 – IND_DC_CTA_FIN

Considerar a informação do campo IND_DC_CTA_FIN da demonstração de DRE recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-32557		RNJ150-12	Registro J150 – Campo 12 – IND_GRP_DRE


[EXCLUÍDA MFS-29278]
Nesse campo o sistema preenche com o indicador de grupo da DRE, as opções válidas são:
‘D’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de despesa represente redução do lucro. 
‘R’ – Linha totalizadora ou de detalhe da demonstração que, por sua natureza de receita represente incremento do lucro. 

O preenchimento do indicador de grupo da DRE é baseado nas opções válidas do campo 08 da SAFX2102. Até o layout 6.0, o campo possui os seguintes valores validos: 
‘1’ – Receita/Despesa
‘2’ – Subtotalizador/ Totalizador da DRE

A partir do layout 7.0, este campo passa a ter os seguintes valores válidos:
‘1’ – Receita/Despesa
‘2’ – Subtotalizador/ Totalizador da DRE
‘3’ – Receita (novo)
‘4’ – Despesa (novo)
‘5’ – Subtotalizador/ Totalizador de Receita (novo)
‘6’ – Subtotalizador/ Totalizador de Despesa (novo)

Regras para geração do indicador:

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘1’ ou ‘2’, o sistema deve verificar se a conta é Credora ou Devedora através do indicador 08– IND_DC_CTA do J150.

Se a aglutinação for “Devedora”, na geração do arquivo magnético do SPED o IND_GRP_DRE é preenchido com ‘D’
Se a aglutinação for “Credora”, na geração do arquivo magnético do SPED o IND_GRP_DRE é preenchido com ‘R’


Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘4’ ou ‘6’, na geração do arquivo magnético da ECD esse campo será preenchido com o valor ‘D’.

Se para o código de aglutinação o indicador de grupo da DRE estiver preenchido com as opções ‘3’ ou ‘5’, na geração do arquivo magnético da ECD esse campo será preenchido com o valor ‘R’.

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis
	MFS-22414
MFS-29278
MFS-32557		RNJ150-13	Registro J150 – Campo 13 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.


[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J150 com base no IND_BALANCO_DRE = ‘D’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

[ALTERAÇÃO- MFS-67621] Alteração para recuperar o Campo “NUM_REFERENCIA” para geração do Campo 13-NOTA_EXP_REF, conforme orientação do Manual do Guia Prático.

Neste campo o sistema deverá preencher com a informação do Campo  7 – NUM_REFERENCIA da Tabela SAFX257, quando o IND_BALANCO_DRE = ‘D’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).

Obs.: Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.
	MFS-15525
MFS-15698
MFS-22414
MFS-29278
MFS-32557
MFS-31025
MFS-67621


		


Alterações Registro J200

CÓD	DESCRIÇÃO	OS/CH		RGJ200	Regra Geral:

De acordo com o manual layout de 2018, o registro J200 não faz parte do leiaute 7.0 do SPED Contábil. Este será inibido do perfil de geração da ECD.
	MFS-22414		
.


Alterações Registro J210

CÓD	DESCRIÇÃO	OS/CH		RNJ210-00	Registro J210 – Regra Geral

[ALTERAÇÃO- MFS-532288] Readequação da Regra para considerar o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”.

Este parâmetro será responsável em definir se o sistema irá gerar ou não os Lançamentos Contábeis/Saldos de Contas Contábeis + Contas Contábeis com Centro de Custos para a mesma Conta Contábil e Período.

Obs.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” esteja selecionado o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”, estará desabilitada, pois o sistema desconsidera os Lançamentos/Saldos por Centro de Custos.

Tratamento:

Parâmetro Marcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “marcado”, o sistema deverá gerar os registros J210, recuperando as informações de Saldos das tabelas SAFX02/SAFX102/SAFX226 e SAFX80/SAFX227, considerando a mesma Conta Contábil e período.


Parâmetro Desmarcado: Caso o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis + Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”. esteja “desmarcado”, o sistema deverá gerar os registros J210 conforme regra original, considerando o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”. 

Default: Desmarcado.

		RNJ210-09	Registro J210 – Campo 09 – NOTA_EXP_REF

Esse campo deverá ser gerado com pipe “||”. A solução será desenvolvida em uma próxima MFS do SPED Contábil 
Observação: Esse campo será gerado a partir da versão 6.00 do ECD.

[EXCLUÍDA MFS-29278]
Recuperar o campo 10 – NOTA_EXP_REF 11 – NOTA_EXP_NUM_REF do registro J210 com base no IND_BALANCO_DRE = ‘L’ OU ‘M’ associados ao código de aglutinação, considerando como período de referência para seleção dos registros o mês e ano da data informada no campo 03 - DT_FIN do registro J005 (desta forma atendemos geração anual, trimestral e semestral) em relação à DAT_DEMONSTRACAO da tabela SAFX257 mais atual, limitado ao final do período de geração do arquivo magnético.

12 posições – Caractere

[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis

[ALTERAÇÃO- MFS-67621] Alteração para recuperar o Campo “NUM_REFERENCIA” para geração do Campo 09-NOTA_EXP_REF, conforme orientação do Manual do Guia Prático.

Neste campo o sistema deverá preencher com a informação do Campo  7 – NUM_REFERENCIA da Tabela SAFX257, quando o IND_BALANCO_DRE = ‘L’ ou ‘M’ e estiver associados ao código de aglutinação selecionada. O período de referência para seleção dos registros é o mês e ano das datas indicadas na geração da demonstração que devem estar compreendidos na DAT_DEMONSTRACAO da tabela SAFX257 (considerar a data mais atual, limitado ao final do período de geração da demonstração).

Obs.: Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis.

	


MFS-22414
MFS-29278
MFS-67621		

Alterações Registro J215

CÓD	DESCRIÇÃO	OS/CH		RNJ215-00	Registro J215 – Regra Geral

[MFS-HYPERLINK "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/837670" \o "https://dev.azure.com/tr-ggo/mastersaf%20fiscal%20solutions/_workitems/edit/837670" \t "_blank"837670] Alteração geração do Registro J215

Considerar na geração o registro J215 somente se houver movimento no registro J210 e o saldo final for superior a zero.


Alteração efetuado com base nas considerações do Time de Legislação

Com base nas informações do registro J210 verifica se que não houve movimento. Neste caso, não deveria ser gerado o registro J215, pois o valor gerado neste registro influência o saldo final do registro J210. Por conta da informação desse registro J215, houve o apontamento de erro pelo PVA pela inconsistência com a regra de validação abaixo:

"Verifica se o saldo final do código de aglutinação – VL_CTA_FIN (Campo 07) – é igual à soma de todos os valores dos fatos contábeis – VL_FAT_CONT (Campo 03) – do registro J215 subtraída do saldo inicial do código de aglutinação – VL_CTA_INI (Campo 05). Se a regra não for cumprida, o PGE do Sped Contábil gera um erro."

	MFS-HYPERLINK "https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/837670" \o "https://dev.azure.com/tr-ggo/mastersaf%20fiscal%20solutions/_workitems/edit/837670" \t "_blank"837670		RNJ215-03	Registro J215 – Campo 03 – DESC_FAT

[EXCLUÍDA MFS-29278]

Nesse campo o sistema preenche com a descrição do fato contábil, campo 03 – DESCRICAO da SAFX2056.

Campo obrigatório.


[Alteração MFS-29278]:

Considerar a informação do campo da demonstração recuperada gerado na tela de geração das demonstrações contábeis


	MFS-22414
MFS-29278		

Alterações Registro J800

CÓD	DESCRIÇÃO	OS/CH		RNJ800-02	Registro J800 – Campo 02 – TIPO_DOC

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado o código conforme opção selecionada pelo usuário no campo “Tipo de documento” na Aba Demonstrações Contábeis dos Dados Iniciais (menu Parâmetros) - quadro ‘Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)’, conforme opções a seguir:

001: Demonstração do Resultado Abrangente do Período 
002: Demonstração dos Fluxos de Caixa 
003: Demonstração do Valor Adicionado 
010: Notas Explicativas 
011: Relatório da Administração 
012: Parecer dos Auditores 
099: Outros
	MFS-8620
MFS-9689
		RNJ800-03	Registro J800 – Campo 03 – DESC_RTF

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)).	MFS-8620
MFS-9689		RNJ800-04	Registro J800 – Campo 04 – HASH_RTF

Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo.	MFS-8620
MFS-9689
		


Novo Registro J801 - Termo de Verificação para Fins de Substituição da ECD

CÓD	DESCRIÇÃO	OS/CH		RNJ801-00	Registro J801 – Regra Geral

Este registro existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.

Origem das informações: Tela de Dados Iniciais – Aba Demonstrações Contábeis (Módulo ECD / Menu Parâmetros > Dados Iniciais)

Regra de Seleção: Este registro será gerado sempre que no quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ na aba Demonstrações Contábeis da tela de Dados Iniciais existir informação de um arquivo RTF.

Campo-chave: ARQ_RTF

Registro pai / Nível hierárquico: J005 / Nível 3

Ocorrência: Um por arquivo
	MFS-8620
MFS-9689		RNJ801-01	Registro J801 – Campo 01 – REG

Informação fixa “J801”.
	MFS-8620		RNJ801-02	Registro J801 – Campo 02 – TIPO_DOC

Nesse registro será gerado o tipo de documento que no caso será 001: Termo de Substituição da ECD.

Valor fixo: 001.

O quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ foi criado justamente para o usuário informar o arquivo de formato RTF que corresponde apenas ao tipo de documento: Termo de Substituição da ECD. 
	MFS-8620		RNJ801-03	Registro J801 – Campo 03 – DESC_RTF

Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)).
	MFS-8620		RNJ801-04	Registro J801 – Campo 04 – COD_MOT_SUBS

Nesse campo o sistema preenche com o código do motivo da substituição, as opções válidas são:

001 – Mudanças de saldos das contas que não podem ser realizadas por meio de lançamentos extemporâneos; 
002 – Alteração de assinatura; 
003 – Alteração de demonstrações contábeis; 
004 – Alteração da forma de escrituração contábil; 
005 – Alteração do número do livro;
099 – Outros; 

Regras:
Se o usuário não informar uma opção de código do motivo da substituição, uma mensagem de alerta é exibida na tela: “O campo Código do Motivo da Substituição é obrigatório de preenchimento, informe uma opção”.
Na geração do campo no arquivo magnético do SPED, o sistema preenche com código, referente aos motivos da substituição: “001”; “002”; “003”; “004”; “005”; “099”.

Campo obrigatório.
Caractere
10 posições
	MFS-22414		RNJ801-05	Registro J801 – Campo 05 – HASH_RTF

Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo.
	MFS-8620		RNJ801-06	Registro J801 – Campo 06 – ARQ_RTF

Será gerada uma sequência de bytes que representem um único arquivo no formato RTF (Rich Text Format).
	MFS-8620		RNJ801-07	Registro J801 – Campo 07 – IND_FIM_RTF

Informação fixa “J801FIM”.
	MFS-8620		

Alterações Registro J930

CÓD	DESCRIÇÃO	OS/CH		RNJ930-03	Registro J930 – Campo 03 – IDENT_CPF_CNPJ

Consultar DE-PARA: DE-PARA _SPED Contábil_Conf.IN RFB nº 926.09.xls.

Tratamento:
Se o campo NUM_CPF da tabela RESP_INFORMACAO não estiver preenchido, será verificada a existência do CNPJ no campo NUM_CPF da tabela RESP_CONTADOR, ambos localizados em Básicos > Parâmetros > Requisitos Legais > Responsável pelas informações.
	CH8476_2017 (MFS-10940)		RNJ930-12	Registro J930 – Campo 12 – IND_RESP_LEGAL

Este campo existe a partir da versão 5.00, porém ele dever ser gerado para todas as versões.

Será gerado conforme parâmetro “Indicação do Representante Legal Junto às Bases da RFB” na Aba Signatários dos Dados Iniciais (menu Parâmetros):
Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”.
Se o parâmetro estiver selecionado, será gerado com conteúdo “S”.
	MFS-8216
MFS-9689		

Alterações Registro J932

CÓD	DESCRIÇÃO	OS/CH		RGJ932-00	Regra Geral para o registro J932

O registro será obrigatório na geração do arquivo da ECD quando:
O campo 14 – do registro 0000 for igual a “1 – Substituta”.
O Código de Qualificação do SPED for igual ‘910’ ou ‘920’.

Exemplo de geração do registro:

J932|TESTEECD|12345678900|CONTADOR/CONTABILISTA RESPONSÁVEL PELO TERMO DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD|910|1SP123456|TESTEECD@GMAIL.COM|2199999999|RJ|RJ/2012/001|31122020|
	MFS-22414		RNJ932-01	Registro J932 – Campo 01 – REG

Nesse campo o sistema preenche com o valor fixo “J932”.
Campo obrigatório.
	MFS-22414		RGJ932-02	Registro J932 – Campo 02 – IDENT_NOM_T

Nesse campo o sistema preenche com o Nome do Signatário do Termo de Verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Nome/Razão Social”.

	MFS-22414		RNJ935-03	Registro J935 – Campo 03 – IDENT_CPF_CNPJ_T

Nesse campo o sistema preenche com o CPF ou CNPJ do assinante do termo de verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CPF/CNPJ”.

Regras:
Se o campo estiver preenchido com 14 posições = Pessoa Jurídica - CNPJ
Se o campo estiver preenchido com 11 posições = Pessoa Física - CPF

Tipo: Caractere
14 posições
	MFS-22414		RNJ935-04	Registro J935 – Campo 04 – IDENT_QUALIF_T

Nesse campo o sistema preenche com a Qualificação do assinante do termo de verificação, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Qualificação [IN 107/2008]”.
	MFS-22414		RNJ935-05	Registro J935 – Campo 05 – COD_ASSIN_T

Nesse campo o sistema preenche com o Código de qualificação do assinante do termo de verificação, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Signatários), campo “ Cod. Qualificação SPED”.

Tipo: Caractere
3 posições
	MFS-22414		RNJ935-06	Registro J935 – Campo 06 – IND_CRC_T

Nesse campo o sistema preenche com o Número de inscrição do contabilista no Conselho Regional de Contabilidade, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CRC/Insc. Estadual”.
	MFS-22414		RNJ935-07	Registro J935 – Campo 07 – EMAIL_T

Nesse campo o sistema preenche com o E-mail do Signatário, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “E-mail”.	MFS-22414		RNJ935-08	Registro J935 – Campo 08 – FONE_T

Nesse campo o sistema preenche com o Telefone do Signatário, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), conectar o campo “DDD e Telefone”.
	MFS-22414		RNJ935-09	Registro J935 – Campo 09 – UF_CRC_T

Nesse campo o sistema preenche com o Indicação da unidade da federação que expediu o CRC, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “CRC UF”.
	MFS-22414		RNJ935-10	Registro J935 – Campo 10 – NUM_SEQ_CRC_T

Nesse campo o sistema preenche com o Número da Certidão de Regularidade Profissional do Contador no seguinte formato: UF/ano/número, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Num. Sequencial do CRC (Formato UF/Ano/Nº) ”.
	MFS-22414		RNJ935-11	Registro J935 – Campo 11 – DT_CRC_T

Nesse campo o sistema preenche com o Data de validade da Certidão de Regularidade Profissional do Contador, localizado em: (Básicos > Parâmetros > Requisitos Legais > Responsável por Informações), campo “Data Validade CRC”.
	MFS-22414		


Alterações Registro J935

CÓD	DESCRIÇÃO	OS/CH		RNJ935-02	Registro J935 – Campo 02 – NI_CPF_CNPJ

Nesse campo o sistema preenche com o documento do auditor independente CPF ou CNPJ, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Auditores Independentes), campo Documento do Auditor Independente”.

Regras:
Se o campo estiver preenchido com 14 posições = Pessoa Jurídica - CNPJ
Se o campo estiver preenchido com 11 posições = Pessoa Física - CPF

Campo Obrigatório
Caractere
14 posições 
	MFS-22414		RNJ935-04	Registro J935 – Campo 04 – COD_CVM_AUDITOR

Nesse campo o sistema preenche com o registro do auditor independente na CVM, localizado em: (SPED > ECD – Escrituração Contábil Digital > Dados Iniciais > aba de Auditores Independentes), campo “Registro do Auditor no CVM”.
	MFS-22414		


Inclusão do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016)


CÓD	DESCRIÇÃO	OS/CH		Regra Geral 	Bloco K – Regra Geral

Deverão preencher este bloco as empresas controladoras obrigadas a apresentar demonstrações consolidadas de acordo com a legislação societária (Lei no 6.404/76 e/ou Pronunciamento Técnico CPC 36 – Demonstrações Consolidadas).

[MFS-66158/ MFS-83352] Tratamento na geração dos Registros do Bloco K, para considerar as contas contábeis no Registro I050. 

Tratamento:

Se o Campo CNPJ da tabela X240_INF_EMPRESA_CONS for igual ao Campo CGC da tabela ESTABELECIMENTO (Considerando os 8 primeiros dígitos)
   Preencher os Registros I050 e I051, quando se tratar de contas contábeis informados nos Registros do Bloco K (K210);
     
- Retirar regra de geração dos Registros I050 e I051, quando se tratar de contas contábeis informados nos Registros do Bloco K.     

Obs.: As informações referentes as contas contábeis utilizadas nas escriturações contábeis consolidadas, informadas no Registro K210, quando tratar-se de uma “Empresa Participante do mesmo “grupo” do declarante da ECD”, ou seja, o Campo 4 – CNPJ do Registro K100 igual ao Campo 6 – CNPJ do Registro 0000 (8 primeiros dígitos), nesse caso, as contas contábeis movimentadas devem ser geradas também nos Registros I050 e I051.  

 	MFS-66158
MFS-83352		RNK001	Registro K001 – Abertura do Bloco K

A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.

Registro abertura: K001

		RNK001-01	Registro K001 – Campo 1 – REG

Informação fixa “K001”.
	MFS9809		RNK001-02	Registro K001 – Campo 2 – IND_DAD

Indicador de movimento: 
Bloco com dados informados; 
Bloco sem dados informados.

Gravar a informação de acordo com os dados encontrados para esse bloco se houver dados informados gravar = 0 - Bloco com dados informados, se não encontrar dados gravar = 1 - Bloco sem dados informados.

Informação fixa “1”.

Obs.: Como a princípio não atenderemos a geração do Bloco K, o conteúdo deste campo será fixo igual a “1” (Bloco sem dados informados). 
	MFS9809
MFS-10358		RNK030-00	Registro K030 – Regra geral

Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00” e a data final de geração for Dezembro ou quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00” e a escrituração indicar que possui situação especial e a data final de geração for da situação especial, a estrutura do registro K030 será gerada conforme definida neste documento.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K030 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K030 – Período da Escrituração Contábil Consolidada”.


parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros)

Campo-chave: DT_INI 

Registro pai / Nível hierárquico: K030 / Nível 2

Ocorrência: Um por arquivo.

	MFS-10358
MFS-31598
MFS-43186		RNK030-01	Registro K030 – Campo 1 – REG

Informação fixa “K030”.
	MFS-10358		RNK030-02	Registro K030 – Campo 2 – DT_INI

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Inicial do período consolidado.
	MFS-10358		RNK030-03	Registro K030 – Campo 3 – DT_FIN

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final do período consolidado.
	MFS-10358		RNK100-00	Registro K100 – Regra geral

Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K100 será gerada conforme definida neste documento. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K100 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K100 – Relação das Empresas Consolidadas”.

Campo-chave: EMP_COD

Registro pai / Nível hierárquico: K100 / Nível 3

Ocorrência: Vários por arquivo.

	MFS-10358		RNK100-01	Registro K100 – Campo 1 – REG

Informação fixa “K100”. 
	MFS-10358		RNK100-02	Registro K100 – Campo 2 – COD_PAIS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código do País. 
	MFS-10358		RNK100-03	Registro K100 – Campo 3 – EMP_COD

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa Participante.
	MFS-10358		RNK100-04	Registro K100 – Campo 4 – CNPJ

Considerando a Origem da Informação, demonstrar aqui APENAS os primeiros 8 dígitos do conteúdo informado no campo CNPJ da Empresa Participante. 
	MFS-10358		RNK100-05	Registro K100 – Campo 5 – NOME

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nome da Empresa Participante.
	MFS-10358		RNK100-06	Registro K100 – Campo 6 – PER_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Participação Total.
	MFS-10358		RNK100-07	Registro K100 – Campo 7 – EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Ocorrido no Período.
	MFS-10358		RNK100-08	Registro K100 – Campo 8 – PER_CONS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Consolidação no Final Período.
	MFS-10358		RNK100-09	Registro K100 – Campo 9 – DATA_INI_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Início da Consolidação.
	MFS-10358		RNK100-10	Registro K100 – Campo 10 – DATA_FIN_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final da Consolidação.
	MFS-10358		RNK110-00	Registro K110 – Regra geral

Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K110 será gerada conforme definida neste documento. Este registro é filho do K100. 

Este registro é filho do K100. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K110 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K110 – Relação dos Eventos Societários”. 

Campo-chave: Nenhum 

Registro pai / Nível hierárquico: K110 / Nível 4

Ocorrência: Vários por arquivo.
	MFS-10358		RNK110-01	Registro K110 – Campo 1 – REG

Informação fixa “K110”.
	MFS-10358		RNK110-02	Registro K110 – Campo 2 – EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Societário ocorrido no período.
	MFS-10358		RNK110-03	Registro K110 – Campo 3 – DT_EVENTO

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data do Evento Societário.
	MFS-10358		RNK115-00	Registro K115 – Regra geral

Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K115 será gerada conforme definida neste documento.

Campo-chave: Nenhum

Registro pai / Nível hierárquico: K115 / Nível 5

Ocorrência: Vários por arquivo.
	MFS-10358		RNK115-01	Registro K115 – Campo 1 – REG

Informação fixa “K115”.
	MFS-10358		RNK115-02	Registro K115 – Campo 2 – EMP_COD_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa envolvida na operação.
	MFS-10358		RNK115-03	Registro K115 – Campo 3 – COND_PART

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Condição da empresa relacionada à operação.
	MFS-10358		RNK115-04	Registro K115 – Campo 4 – PER_EVT

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual da empresa participante envolvido na operação.
	MFS-10358		RNK200-00	Registro K200 – Regra geral


Origem da Informação: SAFX2002 – Tabela de Plano de Contas

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K200 será gerada conforme definida neste documento. 

Serão consideradas as contas contábeis utilizadas nas escriturações contábeis consolidadas (campo IND_CONTA_CONSOLID = S da SAFX2002) que possuam movimento (SAFX242) no período de consolidação do K030 (SAFX240).

Para a geração do Plano de Contas Consolidado, as informações serão recuperadas da tela de Plano de Contas (menu: Manutenção >> Códigos >> Plano de Contas) do módulo Mastersaf DW.

Para este cenário, deve ser gerado no arquivo as informações do cadastro das contas sintéticas (campo COD_CONTA_SINT da SAFX2002) associada à conta movimentada encontrada (SAFX242) e também o cadastro de todas as outras contas vinculadas, de nível superior, de forma que tenhamos o plano completo. 
Exemplo:
No movimento (SAFX242) temos a conta: 0001.0001.0001.0001, que no cadastro tem:

Código de Conta
Código de Conta Sintética
Nível

0001.0001.0001.0001
0001.0001.0001
4

0001.0001.0001
0001.0001
3

0001.0001
0001
2

0001

1


Neste exemplo, apenas a conta 0001.0001.0001.0001 foi movimentada, porém, no arquivo gerado devem ser demonstradas informações das contas "0001.0001.0001.0001", "0001.0001.0001", "0001.0001" e "0001".

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K200 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K200 – Plano de Contas Consolidado”.

Campo-chave: COD_CTA

Registro pai / Nível hierárquico: K200 / Nível 2

Ocorrência: Vários por arquivo.
	MFS-10358		RNK200-01	Registro K200 – Campo 1 – REG

Informação fixa “K200”.  
	MFS-10358		RNK200-02	Registro K200 – Campo 2 – COD_NAT

Considerando a Origem da Informação, demonstrar aqui o conteúdo de acordo com campo Indicador de Natureza conforme abaixo:

Indicador de Natureza:

Se informado ‘0. Compensação’, gravar ‘05’;
Se informado ‘1. Ativo’, gravar ‘01’;
Se informado ‘2. Passivo’, gravar ‘02’;
Se informado ‘3. Despesa’, gravar ‘04’;
Se informado ‘4. Receita’, gravar ‘04’;
Se informado ‘5. Mutações Ativas ("Variações Patrimoniais" anuais)’, gravar ‘09’;
Se informado ‘6. Mutações Passivas ("Variações Patrimoniais" anuais)’, gravar ‘09’;                                                                                                                                                                                                           Se informado ‘7. Patrimônio Líquido’, gravar ‘03’;                                                                                                                                                                                      Se informado ‘8. Custo’, gravar ‘04’;
Se informado ‘9. Outros’, gravar ‘09’. 
	MFS-10358		RNK200-03	Registro K200 – Campo 3 – IND_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador de Conta.
	MFS-10358		RNK200-04	Registro K200 – Campo 4 – NIVEL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nível.
	MFS-10358		RNK200-05	Registro K200 – Campo 5 – COD_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta.
	MFS-10358
		RNK200-06	Registro K200 – Campo 6 – COD_CTA_SUP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código de Conta Sintética.
	MFS-10358		RNK200-07	Registro K200 – Campo 7 – CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Descrição da Conta.
	MFS-10358		RNK210-00	Registro K210 – Regra geral

Origem da Informação: Manutenção - Mapeamento para Planos de Contas das Empresas Consolidadas

Localizaçao: Menu SPED,  Módulo: ECD - Escrituração Contábil Digital, item de menu Manutenção àð Bloco K àð Mapeamento para Planos de Contas das Empresas Consolidadas

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro  Escriturações Contábeis Consolidadas  selecionado na tela de Dados Iniciais   menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K210 será gerada conforme definida neste documento. 

Se o campo “Código da Conta Consolidadora” estiver preenchido na tabela “SAFX262 - Mapeamento para Plano de Contas das Empresas Consolidadas”, o sistema deverá gerar o registro K210 com a informação preenchida no campo “Código da Conta da Empresa Participante E a partir deste relacionamento com a conta consolidadora inserida, esta deverá ser incluída como “filha” no registro K200.

Senão, manter a geração atual, considerando a Origem da Informação COD_CTA_EMP.

Se opção “Gerar Plano de Contas” dos Dados Iniciais da ECD (Módulo ECD> Parâmetros>Dados Iniciais) for diferente de “Completo” e o Campo COD_EMPRESA da SAFX262 for igual ao código da empresa do Manager, deverá gerar os Registros I050 para as contas constantes no campo COD_CONTA da SAFX262.

Campo-chave: COD_EMP, COD_CTA_EMP

Registro pai / Nível hierárquico: K210 / Nível 4

Ocorrência: Vários por arquivo.
	MFS-10358
MFS-18238		RNK210-01	Registro K210 – Campo 1 – REG

Informação fixa “K210”.
	MFS-10358		RNK210-02	Registro K210 – Campo 2 – COD_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código/Nome da Empresa Participante.
	MFS-10358		RNK210-03	Registro K210 – Campo 3 – COD_CTA_EMP

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta.
	MFS-10358		RNK300-00	Registro K300 – Regra geral

Origem da Informação: SAFX242 - Saldos das Contas Consolidadas.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K300 será gerada conforme definida neste documento.

Serão considerados apenas os saldos das contas consolidadas que pertençam ao período de consolidação informado no K030 (SAFX240).

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K300 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K300 – Saldos das Contas Consolidadas”. 

Campo-chave: COD_CTA

Registro pai / Nível hierárquico: K300 / Nível 3.

Ocorrência: Vários por arquivo.
	MFS-10358		RNK300-01	Registro K300 – Campo 1 – REG

Informação fixa “K300”.
	MFS-10358		RNK300-02	Registro K300 – Campo 2 – COD_CTA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada.
	MFS-10358		RNK300-03	Registro K300 – Campo 3 – VAL_AG

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto aglutinado.
	MFS-10358		RNK300-04	Registro K300 – Campo 4 – IND_VAL_AG

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor aglutinado.
	MFS-10358		RNK300-05	Registro K300 – Campo 5 – VAL_EL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto das eliminações.	MFS-10358		RNK300-06	Registro K300 – Campo 6 – IND_VAL_EL

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK300-07	Registro K300 – Campo 7 – VAL_CS

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto consolidado.
	MFS-10358		RNK300-08	Registro K300 – Campo 8 – IND_VAL_CS 

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor consolidado.
	MFS-10358		RNK310-00	Registro K310 – Regra geral

Origem da Informação: SAFX243 - Empresas Detentoras das Parcelas do Valor Eliminado Total.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K310 será gerada conforme definida neste documento.

Este registro é filho do K300. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K310 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K310 – Empresas Detentoras das Parcelas do Valor Eliminado Total”.

Campo-chave: EMP_COD_PARTE 

Registro pai / Nível hierárquico: K310 / Nível 4.

Ocorrência: Vários por arquivo.
	MFS-10358		RNK310-01	Registro K310 – Campo 1 – REG

Informação fixa “K310”.
	MFS-10358		RNK310-02	Registro K310 – Campo 2 – EMP_COD_PARTE

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa detentora do valor aglutinado que foi eliminado.
	MFS-10358		RNK310-03	Registro K310 – Campo 3 – VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela do valor eliminado total.
	MFS-10358		RNK310-04	Registro K310 – Campo 4 – IND_VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK315-00	Registro K315 – Regra geral

Origem da Informação: SAFX244 - Empresas Contrapartes das Parcelas do Valor Eliminado Total.

Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K315 será gerada conforme definida neste documento.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K315 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K315 – Empresas Contrapartes das Parcelas do Valor Eliminado Total”. 

Campo-chave: EMP_COD_CONTRA, COD_CONTRA

Registro pai / Nível hierárquico: K315 / Nível 5.

Ocorrência: Vários por arquivo.	MFS-10358		RNK315-01	Registro K315 – Campo 1 – REG

Informação fixa “K315”.
	MFS-10358		RNK315-02	Registro K315 – Campo 2 – EMP_COD_CONTRA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa da contrapartida.
	MFS-10358		RNK315-03	Registro K315 – Campo 3 – COD_CONTRA

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada da contrapartida. 
	MFS-10358		RNK315-04	Registro K315 – Campo 4 – VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela da contrapartida do valor eliminado total.
	MFS-10358		RNK315-05	Registro K315 – Campo 5 – IND_VALOR

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado.
	MFS-10358		RNK990	Registro K990 – Encerramento do Bloco K


A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.

Registro encerramento: K990 
	MFS8216
MFS-10358		RNK990-01	Registr