# SPED_Fiscal_Regras_BlocoG_OutrasOrigens

> Fonte: SPED_Fiscal_Regras_BlocoG_OutrasOrigens.doc

Quadro de Revisões


Data	OS / Chamado	Descrição 	Responsável		12/05/2010	OS2931-B6	Criação do documento contendo as regras para a geração do Bloco G do SPED Fiscal a partir das tabelas SAFX133, SAFX134, SAFX135 e SAFX136.	Marcos Roberto de Oliveira		28/07/2010	OS2931-B6	Alteração do requisito para contemplar as novas regras de acordo com o Guia Prático da versão 2.0.1.	Marcos Roberto de Oliveira		01/10/2010	OS2931-B6	Alteração do requisito para contemplar as novas regras de acordo com o Guia Prático da versão 2.0.2	Marcos Roberto de Oliveira		25/11/2010	OS2931-B6	Inclusão da regra do campo Número das Parcelas do registro 0300 para considerar a parametrização do módulo ICMS	Marcos Roberto de Oliveira		09/10/2012
	OS3762	Inclusão da regra do campo Número das Parcelas do registro 0300 para considerar a SAFX13.	Vanessa W. Bravo		09/04/2015	OS4747	Inclusão da regra para considerar o parâmetro "Considerar o Indicador no Código do Participante" na geração do G130.	Marcos G. de Paula		10/12/2019	MFS31420	Essa MFS tem como objetivo incluir os campos novos nos registros G130 e G140	Andréa Rocha		12/03/2020	MFS34966	Alteração da geração do Registro G140	Andréa Rocha		06/02/2023	MFS435439	Inclusão de tratamento do campo de DT_FIN, para considerar o novo campo de DAT_ENCERRAMENTO da tabela de Inscrição Estadual para os clientes que encerrarem a Inscrição Estadual. G110.	Rogério Ohashi		



Bloco 0 – Abertura, Identificação e Referências

Registro 0300 – Cadastro de Bens ou Componentes do Ativo Imobilizado

RN0300-07	Deverá ser gravado nesse campo a quantidade de parcelas a serem apropriadas. O número de parcelas pode variar de acordo com alguma legislação específica de cada UF. Geralmente o total de parcelas a ser apropriada é 48.

Para que seja gravada a quantidade correta de parcelas a ser apropriada, o sistema deverá recuperar a informação do campo “Periodicidade” da tela de parametrização dos livros por Estabelecimento. Essa parametrização está presente no módulo Controle de Obrigações Estaduais, menu: Obrigações >> Obrigações Fiscais >> Por Estabelecimento

Caso o campo “Periodicidade” esteja selecionado com a opção “Mensal”, gravar “48”.
Caso o campo “Periodicidade” esteja selecionado com a opção “Quinzenal”, gravar “96”.
Caso o campo “Periodicidade” esteja selecionado com a opção “Decêndio”, gravar “144”.

Caso o campo esteja selecionado com uma opção diferente das informadas acima, gravar “48”.

[ALTERADA – OS3762]

Deverá ser gravada nesse campo a quantidade de parcelas a serem apropriadas. A informação deverá ser recuperada da SAFX13, campo Nº Parcelas a serem apropriadas (SPED Fiscal – Informações para o Bloco G).
Quando o campo Nº Parcelas a serem apropriadas (SPED Fiscal – Informações para o Bloco G) estiver preenchido, a regra acima deve ser desconsiderada, e quando não estiver preenchida, a regra acima deve ser considerada.
		

Bloco G – Controle do Crédito de ICMS do Ativo Permanente – CIAP

Registro G110 – ICMS Ativo Permanente – CIAP

RNG110	Os dados deste registro não serão gerados com base nos valores calculados pelo módulo Ativo Permanente. Essas informações serão recuperadas a partir das seguintes tabelas SAFX (tabelas criadas através da OS2931-B4):

SAFX133
SAFX134
SAFX135
SAFX136

O usuário deverá carregar as tabelas SAFX com essas informações e posteriormente executar a importação desses dados nas tabelas temporárias (SAFX) para as tabelas definitivas (X).

A nomenclatura das tabelas definitivas será definida no documento de A&D da OS2931-B4.

Após essa importação o sistema deverá verificar os seguintes pontos para geração do registro G110:

Verificar se o parâmetro “Gerar os registros a partir de valores não calculados pelo módulo Ativo Permanente” está selecionado na tela de Dados Iniciais do módulo EFD – Escrituração Fiscal Digital (menu Parâmetros >> Dados Iniciais). Caso positivo a geração será realizada através desse documento. Caso negativo, a geração será realizada com os valores calculados pelo módulo Ativo Permanente (vide documento Sped_Fiscal_Regras.doc).
Após identificar que o parâmetro informado no item anterior está selecionado, o sistema verifica o período informado da apuração do ICMS (registro E100) para o estabelecimento selecionado para geração. Caso as informações estejam de acordo, o sistema realiza a geração do registro G110. 

OBS 1: como a geração do Bloco G possui os valores calculados através de outras origens, o cliente deverá popular essas tabelas mensalmente (SAFX133, SAFX134, SAFX135 e SAFX136).
OBS 2: deverá ser gerado apenas 1 registro G110 por período de apuração, ou seja, no arquivo.		RNG110-01	Campo REG

Gravar no campo 01 – REG o texto fixo “G110”.		RNG110-02	Campo DT_INI

Gravar no campo 02 – DT_INI a data inicial do periodo de apuração do CIAP. A data deve ser a mesma do campo DT_INI do registro E100 correspondente.		RNG110-03	Campo DT_FIN

Gravar no campo 03 – DT_FIN a data final do periodo de apuração do CIAP. A data deve ser a mesma do campo DT_FIM do registro E100 correspondente.

[ALTERAÇÃO-MFS435439] Tratamento da Regra para Inscrição Estadual Encerrada

Tratamento na geração do campo de DT_FIN para os clientes que encerrarem a Inscrição Estadual da UF do próprio Estabelecimento, nesse caso o sistema deverá consultar o campo de Data de Encerramento (DAT_ENCERRAMENTO) da tabela REGISTRO_ESTADUAL, e segui conforme a Regra abaixo:  

Tratamento:

Se o campo de DAT_ENCERRAMENTO da tabela REGISTRO_ESTADUAL estiver preenchido;
   E o campo de UF da tabela REGISTRO_ESTADUAL for igual ao campo de UF do Estabelecimento;
   Preencher o campo de DT_FIN com o campo de DAT_ENCERRAMENTO da tabela REGISTRO_ESTADUAL.

Obs.: Para esse campo ser considerado, a data de encerramento deverá estar entre o período de referência da geração.
		RNG110-04	Campo SALDO_IN_ICMS

Gravar no campo 04 – SALDO_IN_ICMS a informação contida no campo “Saldo Inicial de ICMS do Ativo Permanente” da tabela SAFX133. 		RNG110-05	Campo SOM_PARC

Gravar no campo 05 – SOM_PARC a informação contida no campo “Somatório das parcelas passíveis de apropriação” da tabela SAFX133.		RNG110-06	Campo VL_TRIB_EXP

Gravar no campo 06 – VL_TRIB_EXP a informacao contida no campo “Valor Total das Saídas Tributadas e Saídas para Exportação” da tabela SAFX133.		RNG110-07	Campo VL_TOTAL

Gravar no campo 07 – VL_TOTAL a informação contida no campo “Valor Total das Saídas” da tabela SAFX133. 		RNG110-08	Campo IND_PER_SAI

Gravar no campo 08 – IND_PER_SAI a informação contida no campo “Índice de Participação do valor do somatório das saídas tributadas e saídas para exportação no valor total de saídas” da tabela SAFX133. 		RNG110-09	Campo ICMS_APROP

Gravar no campo 09 – ICMS_APROP a informação contida no campo “Valor de ICMS a ser apropriada” da tabela SAFX133.		RNG110-10	Campo SOM_ICMS_OC

Gravar no campo 10 – SOM_ICMS_OC a informação contida no campo “Valor de Outros Créditos de ICMS a ser apropriado na apuração do ICMS” da tabela SAFX133.		
Registro G125 – Movimentação de Bem ou Componente do Ativo Imobilizado

RNG125	Deverão ser gerados tanto registros quanto forem necessários para o registro G110. A relação é de 1:N.

Devem ser recuperados as informações da tabela SAFX134 para a empresa, estabelecimento e período informados.		RNG125-01	Campo REG

Gravar no campo 01 – REG o texto fixo “G125”.		RNG125-02	Campo COD_IND_BEM

Gravar no campo 02 – COD_IND_BEM a informação que estiver contida no campo “Código do Bem” e “Código do Incorporador“ da tabela SAFX134. A informação deve ser concatenada através de um “-“. Exemplo: 01-0200 onde 01 é o Código do Bem e 0200 é o Código do Incorporador.

Para cada bem informado nesse campo deverá ser gerado um registro do tipo 0300 com as informações cadastrais do mesmo. As regras são as mesmas existentes no documento “Sped_Fiscal_Regras.doc”.		RNG125-03	Campo DT_MOV

Gravar no campo 03 – DT_MOV a informação que estiver contida no campo “Data da Movimentação” da tabela SAFX134. 		RNG125-04	Campo TIPO_MOV

Gravar no campo 04 – TIPO_MOV a informação que estiver contida no campo “Tipo da Movimentação” da tabela SAFX134.		RNG125-05	Campo VL_IMOB_ICMS_OP

Gravar no campo 05 – VL_IMOB_ICMS_OP a informação que estiver contida no campo “Valor do ICMS da Operação Própria na entrada do bem ou componente” da tabela SAFX134.		RNG125-06	Campo VL_IMOB_ICMS_ST

Gravar no campo 06 – VL_IMOB_ICMS_ST a informação que estiver contida no campo “Valor do ICMS da Oper. por Sub. Tributária na entrada do bem ou componente” da tabela SAFX134. 		RNG125-07	Campo VL_IMOB_ICMS_FRT

Gravar no campo 07 – VL_IMOB_ICMS_FRT a informação que estiver contida no campo “Valor do ICMS sobre Frete do Conhecimento de Transporte na entrada do bem ou componente” da tabela SAFX134. 		RNG125-08	Campo VL_IMOB_ICMS_DIF

Gravar no campo 08 – VL_IMOB_ICMS_DIF a informação que estiver contida no campo “Valor do ICMS - Diferencial de Alíquota, conforme Doc. de Arrecadação, na entrada do bem ou componente” da tabela SAFX134. 		RNG125-09	Campo NUM_PARC

Gravar no campo 09 – NUM_PARC a informação que estiver contida no campo “Número da parcela do ICMS” da tabela SAFX134. 		RNG125-10	Campo VL_PARC_PASS

Gravar no campo 10 – VL_PARC_PASS a informação que estiver contida no campo “Valor da parcela de ICMS passível de apropriação - antes da aplicação da participação percentual do valor das saídas tributadas/exportação sobre as saídas totais” da tabela SAFX134. 		
Registro G126 – Outros Créditos CIAP

RNG126	Deverão ser gerados tanto registros quanto forem necessários para o registro G125. A relação é de 1:N.

Devem ser recuperados as informações da tabela SAFX136 para a empresa, estabelecimento e período informados.		RNG126-01	Campo REG

Gravar no campo 01 – REG o texto fixo “G126”.		RNG126-02	Campo DT_INI

Gravar no campo 02 – DT_INI a data inicial do periodo de apuração do CIAP. A data deve ser a mesma do campo DT_INI do registro E100 correspondente.		RNG126-03	Campo DT_FIM

Gravar no campo 03 – DT_FIM a data final do periodo de apuração do CIAP. A data deve ser a mesma do campo DT_FIM do registro E100 correspondente.		RNG126-04	Campo NUM_PARC

Gravar no campo 04 – NUM_PARC a informação que estiver contida no campo “Número da Parcela do ICMS” da tabela SAFX136.		RNG126-05	Campo VL_PARC_PASS

Gravar no campo 05 – VL_PARC_PASS a informação que estiver contida no campo “Valor do ICMS passível de apropriação” da tabela SAFX136.		RNG126-06	Campo VL_TRIB_OC

Gravar no campo 06 – VL_TRIB_OC a informação que estiver contida no campo “Valor das saídas tributadas e para exportação” da tabela SAFX136.		RNG126-07	Campo VL_TOTAL

Gravar no campo 07 – VL_TOTAL a informação que estiver contida no campo “Valor total das saídas” da tabela SAFX136.		RNG126-08	Campo IND_PER_SAI

Gravar no campo 08 – IND_PER_SAI a informação que estiver contida no campo “Índice de Participação” da tabela SAFX136.		RNG126-09	Campo VL_PARC_APROP

Gravar no campo 09 – VL_PARC_APROP a informação que estiver contida no campo “Valor de Outros Créditos a ser apropriado” da tabela SAFX136.		



Registro G130 – Identificação do Documento Fiscal

RNG130	Deverão ser gerados tanto registros quanto forem necessários para o registro G125. A relação é de 1:N. 

Devem ser recuperados as informações da tabela SAFX135 para a empresa, estabelecimento e período informados.		RNG130-01	Campo REG

Gravar no campo 01 – REG o texto fixo “G130”.		RNG130-02	Campo IND_EMIT

Gravar no campo 02 – IND_EMIT a informação que estiver contida no campo “Indicador do Emitente” da tabela SAFX135. 		RNG130-03	Campo COD_PART

Gravar no campo 03 – COD_PART a informação que estiver contida nos campos “Indicador de Pessoa” e “Código da Pessoa Física/Jurídica” da tabela SAFX135.

[OS4747] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais estiver selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador (IND_FIS_JUR) com o Código da PFJ (COD_FIS_JUR), considerando a formatação: Indicador + "-" + Código.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais NÃO estiver selecionado, este campo será gerado apenas com o Código da PFJ (COD_FIS_JUR).

Para o código aqui informado, será demonstrado o Cadastro no registro 0150.
		RNG130-04	Campo COD_MOD

Gravar no campo 04 – COD_MOD a informação que estiver contida no campo “Código do Modelo do Documento Fiscal” da tabela SAFX135. 		RNG130-05	Campo SERIE

Gravar no campo 05 – SERIE a informação que estiver contida no campo “Série do Documento Fiscal” da tabela SAFX135.		RNG130-06	Campo NUM_DOC

Gravar no campo 06 – NUM_DOC a informação que estiver contida no campo “Número do Documento Fiscal” da tabela SAFX135.		RNG130-07	Campo CHV_NFE_CTE

Gravar no campo 07 – CHV_NFE_CTE a informação que estiver contida no campo “Chave do Documento Fiscal Eletrônico” da tabela SAFX135.		RNG130-08	Campo DT_DOC

Gravar no campo 08 – DT_DOC a informação que estiver contida no campo “Data da emissão do documento fiscal” da tabela SAFX135.		RNG130-09	Campo NUM_DA

[MFS31420]

Nos movimentos de entrada (TIPO_MOV do G125 = ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Gravar no campo 09 – NUM_DA a informação que estiver contida no campo “Número do Documento de Arrecadação” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.		

Registro G140 – Identificação do Item do Documento Fiscal

RNG140	Deverão ser gerados tanto registros quanto forem necessários para o registro G130. A relação é de 1:N.

Devem ser recuperados as informações da tabela SAFX135 para a empresa, estabelecimento e período informados. Vale salientar que embora os registros G130 e G140 sejam separados, as informações pertencem à mesma tabela – SAFX135.		RNG140-01	Campo REG

Gravar no campo 01 – REG o texto fixo “G140”.		RNG140-02	Campo NUM_ITEM

Gravar no campo 02 – NUM_ITEM a informação que estiver contida no campo “Número do Item” da tabela SAFX135.		RNG140-03	Campo COD_ITEM

Gravar no campo 03 – COD_ITEM a informação que estiver contida nos campos “Indicador do Produto” e “Código do Produto” da tabela SAFX135. As informações devem ser gravadas de forma concatenada, separada pelo caracter “-“.

Para cada item informado nesse campo deverá ser gerado um registro do tipo 0200 com as informações cadastrais do mesmo. As regras são as mesmas existentes no documento “Sped_Fiscal_Regras.doc”.		RNG140-04	Campo QTDE

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 04 – QTDE a informação que estiver contida no campo “Quantidade” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.
		RNG140-05	Campo UNID

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 05 – UNID a informação que estiver contida no campo “Unidade de Medida” da tabela SAFX135. 

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC)’:
Não preencher.

Para cada unidade de medida informada nesse campo deverá ser gerado um registro do tipo 0190 com as informações cadastrais do mesmo. As regras são as mesmas existentes no documento “Sped_Fiscal_Regras.doc”.		RNG140-06	Campo VL_ICMS_OP_APLICADO

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 06 – VL_ICMS_OP_APLICADO a informação que estiver contida no campo “Valor ICMS” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.
		RNG140-07	Campo VL_ICMS_ST_APLICADO

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 07 – VL_ICMS_ST_APLICADO a informação que estiver contida no campo “Valor ICMS-ST” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.
		RNG140-08	Campo VL_ICMS_FRT_APLICADO

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 08 – VL_ICMS_FRT_APLICADO a informação que estiver contida no campo “Valor ICMS Frete” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.
		RNG140-09	Campo VL_ICMS_DIF_APLICADO

[MFS31420] Alterada pela [MFS34966]
Nos movimentos de entrada e de saída:
Gravar no campo 09 – VL_ICMS_DIF_APLICADO a informação que estiver contida no campo “Valor ICMS Dif. Aliq” da tabela SAFX135.

Nos movimentos de saída (TIPO_MOV do G125 <> ‘SI’ ou ‘IM’ ou ‘IA’ ou ‘CI’ ou ‘MC’):
Não preencher.