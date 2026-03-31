# RegraGeral_v18

> Fonte: RegraGeral_v18.doc

Regra Geral de Geração do Arquivo da EFD-PIS/COFINS:
RNG1-EFD


	A geração do arquivo da EFD-PIS/COFINS poderá centralizar ou não no estabelecimento matriz os dados de cadastros.

Para definir qual estabelecimento será o centralizador da escrituração e quais serão os estabelecimentos centralizados, o usuário deve realizar a parametrização existente no menu:

EFD-PIS/COFINS > Parâmetros > Centralização da Escrituração

A partir da centralização feita nesse menu, serão aplicadas as seguintes regras ao processo de geração do arquivo:

RN001 - Na tela de geração do arquivo magnético serão apresentados apenas os estabelecimentos centralizadores e os estabelecimentos que não foram centralizados (procedimento que já fazemos na tela de geração do SPED Contábil);

RN002 - Os estabelecimentos centralizadores serão apresentados com o prefixo “Centralizador”, seguido do código e descrição do estabelecimento;

RN003 - Os estabelecimentos que não foram centralizados serão apresentados com o prefixo “Descentralizado”, seguido do código e descrição do estabelecimento.

Se o parâmetro ‘Manter os cadastros Centralizados no Estabelecimento Matriz’ na tela de Dados Iniciais estiver marcado:

RN004 - Geração do arquivo centralizada:
	RN004.1 - No bloco 0 os registros 0000, 0100, 0110 e 0111 serão gerados com as informações/parametrizações do estabelecimento centralizador.
	RN004.2 - O registro 0140 referente ao estabelecimento centralizador será o “pai” de todos os registros 0150, 0175, 0190, 0200, 0205, 0206, 0208, 0400, 0500 e 0600 que forem gerados no arquivo, mesmo que esses registros não sejam referentes a uma movimentação do estabelecimento centralizador;
	RN004.3 - Os registros 0140 referente aos demais estabelecimentos centralizados na escrituração serão gerados após o último registro 0600 e não terão registros “filhos”.
	RN004.4 - O primeiro registro A010 gerado no arquivo será referente ao estabelecimento centralizador, e toda movimentação (referente à esse bloco) desse estabelecimento centralizador será gerada nos registros filhos imediatamente abaixo desse A010.
	RN004.5 - Para cada estabelecimento centralizado, será gerado um registro A010 e toda movimentação (referente à esse bloco) desse estabelecimento centralizado será geradas nos registros filhos imediatamente abaixo desse A010.
	RN004.6 - As regras 004.4 e 004.5 descritas acima também serão aplicadas ao registro C010 e seus filhos, ao registro D010 e seus filhos e ao registro F010 e seus filhos.
	RN004.7 - As informações dos blocos M e 1 serão sempre consolidadas no estabelecimento centralizador.
                RN004.8 – As gerações serão baseadas nas parametrizações existentes de acordo com o Estabelecimento Centralizador conforme (Módulo Parâmetros ( Preliminares ( Centralização de Escrituração de Obrigações Federais), ou seja, para geração dos registros citados nas regras acima, o sistema deverá recuperar as parametrizações do Centralizador. 
                RN004.9 – Para todos os registros de Cadastros (0150, 0190, 0200, 0205, 0206, 0208, 0400, 0450,0500 e 0600) filhos do Registro pai 0140, não considerar quebra por Grupo de Estabelecimentos. Nesse caso a regra para recuperação das informações irá seguir as premissas abaixo:
Recuperar a informação do cadastro correspondente ao Grupo relacionado ao Estabelecimento Matriz onde os códigos correspondentes aos cadastros que tenham a Data de Validade mais atual em relação à Data de geração do Registro.
Caso a informação não exista no Grupo correspondente ao Estabelecimento Matriz, recuperar a mesma do Grupo relacionado ao(s) Estabelecimento(s) centralizado(s) sendo que a informação recuperada deve ser aquela em que os cadastros que tenham a Data de Validade mais atual em relação à Data de geração do Registro.

Caso seja encontrado um mesmo Código em Grupos distintos, deve ser exibida a seguinte mensagem de alerta no Log de Geração dos registros: “Encontrada mais de uma ocorrência para o cadastro <tipo de cadastro> em grupos diferentes, para gravação do registro <código do registro> foi utilizado o cadastro existente no grupo do estabelecimento centralizador da apuração do PIS/COFINS.”

Onde:

                 <tipo de cadastro>             <código do registro>
                 do participante                      0150
                 do item                                   0200
                 da conta contábil                  0500

Além de exibir a mensagem, deverão ser exibidos os Grupos desses Códigos em Duplicidade além dos Registros. Os códigos correspondentes aos cadastros não serão listados nesse momento.


Se o parâmetro ‘Manter os cadastros Centralizados no Estabelecimento Matriz’ na tela de Dados Iniciais estiver desmarcado:

                RN004.10 - No bloco 0 os registros 0000, 0100, 0110 e 0111 serão gerados com as informações/parametrizações do estabelecimento centralizador.
	RN004.11 - O registro 0140 referente ao estabelecimento centralizador será o “pai” de todos os registros 0150, 0175, 0190, 0200, 0205, 0206, 0208, 0400, 0450,0500, 0600 que forem gerados no arquivo, desde que  estejam cadastrados no estabelecimento centralizador;
                Caso não estejam cadastrados no estabelecimento centralizador, o mesmo deverá ser gerado abaixo do estabelecimento que contém o cadastro com exceção dos registros 0500 e 0600.
	RN004.12 - Os registros 0140 referente aos demais estabelecimentos centralizados na escrituração serão gerados após o último registro 0450 e terão registros “filhos”, se o item não esteja cadastrado no estabelecimento centralizador.
	RN004.13 - O primeiro registro A010 gerado no arquivo será referente ao estabelecimento centralizador, e toda movimentação (referente à esse bloco) desse estabelecimento centralizador será gerada nos registros filhos imediatamente abaixo desse A010.
	RN004.14 - Para cada estabelecimento centralizado, será gerado um registro A010 e toda movimentação (referente à esse bloco) desse estabelecimento centralizado será geradas nos registros filhos imediatamente abaixo desse A010.
	RN004.15 - As regras 004.13 e 004.14 descritas acima também serão aplicadas ao registro C010 e seus filhos, ao registro D010 e seus filhos e ao registro F010 e seus filhos.
	RN004.16 - As informações dos blocos M e 1 serão sempre consolidadas no estabelecimento centralizador.
                RN004.17 – As gerações serão baseadas nas parametrizações existentes de acordo com o Estabelecimento Centralizador conforme (Módulo Parâmetros ( Preliminares ( Centralização de Escrituração de Obrigações Federais), ou seja, para geração dos registros citados nas regras acima, o sistema deverá recuperar as parametrizações do Centralizador. 
                RN004.18 – Para os registros de Cadastros (0500 e 0600) filhos do Registro pai 0140, não considerar quebra por Grupo de Estabelecimentos. Nesse caso a regra para recuperação das informações irá seguir as premissas abaixo:
Recuperar a informação do cadastro correspondente ao Grupo relacionado ao Estabelecimento Matriz onde os códigos correspondentes aos cadastros que tenham a Data de Validade mais atual em relação à Data de geração do Registro.
Caso a informação não exista no Grupo correspondente ao Estabelecimento Matriz, recuperar a mesma do Grupo relacionado ao(s) Estabelecimento(s) centralizado(s) sendo que a informação recuperada deve ser aquela em que os cadastros que tenham a Data de Validade mais atual em relação à Data de geração do Registro, neste caso o cadastro ficará abaixo do estabelecimento centralizado.

Caso seja encontrado um mesmo Código em Grupos distintos num mesmo estabelecimento deve ser exibida a seguinte mensagem de alerta no Log de Geração dos registros: “Encontrada mais de uma ocorrência para o cadastro <tipo de cadastro> em grupos diferentes, para gravação do registro <código do registro> foi utilizado o cadastro existente no grupo do estabelecimento centralizador da apuração do PIS/COFINS.”

Além de exibir a mensagem, deverão ser exibidos os Grupos desses Códigos em Duplicidade além dos Registros. Os códigos correspondentes aos cadastros não serão listados nesse momento.
Caso seja encontrado um mesmo Código em Grupos distintos entre estabelecimentos diferentes devem ser gerado um 0150, 0190, 0200, 0205, 0206, 0208, 0400, 0450  abaixo de cada estabelecimento centralizado (0140) ou apenas abaixo do estabelecimento matriz caso  esteja cadastrado no estabelecimento matriz.
A geração dos registros 0500 e 0600 não devem sofrer alteração. Devem ser gerados SEMPRE abaixo do estabelecimento Centralizador.		RNG2-EFD	Formatação dos campos em geral 

Os campos numéricos a serem gerados no arquivo que possuam conteúdo igual a zero ou nulo, devem ser gravados com zero, com exceção dos campos ALIQ_PIS, ALIQ_PIS_QUANT, ALIQ_COFINS, ALIQ_COFINS_QUANT, VL_BC_COFINS,  QUANT_BC_COFINS,  VL_BC_PIS e QUANT_BC_PIS
que devem obedecer à seguinte regra:

A regra abaixo será aplicada para os registros C170, C181, C185, C191, C195, C381, C385, C481, C485 C491, C495 e D350. 
PIS/PASEP:
Se VL_BC_PIS ou ALIQ_PIS forem maiores que zero, então estes campos devem ser gravados com valores maiores ou iguais a zero; e os campos QUANT_BC_PIS e ALIQ_PIS_QUANT devem ser gravados sem informação, ou seja, ||;
Se QUANT_BC_PIS ou ALIQ_PIS_QUANT forem maiores que zero, então estes campos devem ser gravados com valores maiores ou iguais a zero; e os campos VL_BC_PIS e ALIQ_PIS devem ser gravados sem informação, ou seja, ||;
Se VL_BC_PIS e ALIQ_PIS e QUANT_BC_PIS e ALIQ_PIS_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||.
 COFINS:
Se VL_BC_COFINS  ou ALIQ_COFINS  forem maiores que zero, então estes campos devem ser gravados com valores maiores ou iguais a zero; e os campos QUANT_BC_COFINS  e ALIQ_COFINS_QUANT devem ser gravados sem informação, ou seja, ||;
Se QUANT_BC_COFINS  ou ALIQ_COFINS_QUANT forem maiores que zero, então estes campos devem ser gravados com valores maiores ou iguais a zero; e os campos VL_BC_COFINS  e ALIQ_COFINS  devem ser gravados sem informação, ou seja, ||;
Se VL_BC_COFINS  e ALIQ_COFINS  e QUANT_BC_COFINS  e ALIQ_COFINS_QUANT forem iguais a zero, então TODOS devem ser gerados sem informação, ou seja, ||."
Para CST05 e alíquota Zero:
Se todos os campos (ALIQ_PIS, ALIQ_PIS_QUANT, ALIQ_COFINS, ALIQ_COFINS_QUANT, VL_BC_COFINS,  QUANT_BC_COFINS,  VL_BC_PIS, QUANT_BC_PIS,VL_PIS,  VL_COFINS), estiverem zerados na base gerar os campos ALIQ_PIS , ALIQ_COFINS,  VL_BC_COFINS,  VL_BC_PIS, VL_PIS e   VL_COFINS devem ser gerados zerados com ‘|0|’ e os campos ALIQ_PIS_QUANT, ALIQ_COFINS_QUANT,   QUANT_BC_COFINS e QUANT_BC_PIS devem ser gerados com ‘||’

A regra abaixo será aplicada para os registros A100 e A170

Caso o item de serviço (DWT_ITENS_SERV) de PIS os campos deverão ser gravados da seguinte maneira:
Registro A100 – Campo 15 – VL_BC_PIS – Gravar |0|
Registro A170 – Campo 10 – VL_BC_PIS e campo  Gravar |0|

Aplicar a regra abaixo para o registro F100

Se os campos 08 – VL_BC_PIS, 09 – ALIQ_PIS, 10- VL_PIS, 12 – VL_BC_COFINS, 13 – ALIQ_COFINS e 14- VL_COFINS , possuírem conteúdo igual a zero ou nulo, devem ser gravados com zero.

		RNG3-EFD	Quando a empresa estiver enquadrada no Regime de Tributação Lucro Presumido, apenas as receitas serão consideradas.		RNG4-EFD	Se a empresa estiver enquadrada no Regime de Tributação Lucro Presumido e nos regimes de Caixa e Competência Consolidada, os registros dos Blocos A, C e D não devem ser demonstrados no arquivo magnético.		RNG5-EFD	[OS4316-A] Tratamento para Geração de SCPs

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", serão mantidas as regras padrão de seleção dos cadastros definidas na RNG1-EFD e as regras de formatação definidas na RNG2-EFD, porém, a diferença é que será gerado um arquivo para cada SCP cadastrada no Cadastro da SCP e um arquivo para o Sócio Ostensivo.

Quando falamos de SCP, nos referimos a uma Sociedade em Conta de Participação. Trata-se se um contrato entre empresas que se juntam para realização de uma determinada atividade. Neste caso, a empresa majoritária assume a prestação de contas das operações desta SCP perante o fisco.

Neste caso, a empresa majoritária é chamada Sócia Ostensiva. Ela recebe toda a movimentação da SCP e precisará entregar a informação segregada ao fisco.

Na "Geração dos Registros" do menu "Obrigações SCP" a informação de estabelecimento será demonstrada considerando o Cadastro da SCP, pois se uma empresa participa de uma SCP deverá realizar o cadastro. Lá serão demonstradas informações realizando a quebra por estabelecimento e código SCP e no momento da geração, isso será levado em conta.

Deverá ser gerado um arquivo para cada SCP na qual a empresa participa e um arquivo para o Sócio Ostensivo. No arquivo da SCP estarão apenas as movimentações do código de SCP ao qual o estabelecimento está vinculado e no arquivo do Sócio Ostensivo, as informações de movimentação que não tem indicação do Código SCP.

Para tornar esta geração possível, foi incluído o campo Código da SCP nas tabelas que servem de base para geração da obrigação:

SAFX07 - Arquivo de Notas Fiscais
SAFX42 - Capa de Documentos Fiscais de Utilities
SAFX49 - Tabela das Operações de Importação
SAFX05 - Arquivo de Contas a Receber
SAFX991 - Capa Redução Z 
SAFX994 - Detalhe do Cupom Fiscal
SAFX130 - Documentos Fiscais Eletrônicos Denegados ou Inutilizados
SAFX145 - Contribuição Retida na Fonte 
SAFX147 - Demais documentos e Operações Geradoras de crédito
SAFX148 - Bens do Ativo Imobilizado Com Base nos Encargos de Depreciação e no valor de aquisição
SAFX149 - Unidade Imobiliária Vendida
SAFX161 - Prestação de Serviços de Comunicação e de Telecomunicação Consolidadas 
SAFX183 - Demais documentos e Receitas – Lucro Presumido
SAFX185 - Apuração da Contribuição Previdenciária sobre a Receita Bruta – Bloco P
SAFX190 - Fornecimento de Energia Elétrica, Água Canalizada e Gás - Consolidados
SAFX193 - Novas Deduções Diversas

O código foi incluído nas tabelas mestre. Os registros-filho, deverão ser selecionados considerando as informações do pai.

Teremos o seguinte processo para as empresas que participam de SCP como Sócia Ostensiva:
Realiza o Cadastro dos Estabelecimentos que participam da SCP;
Vincula a movimentação indicando o Código da SCP cadastrado;
Gera os registros, obtendo o seguinte resultado:
“1” bloco de informações para o Sócio Ostensivo (considera movimentações sem código de SCP informado);
“1” ou “N” blocos de informação de cada SCP: um para cada código de SCP cadastrada (considera movimentações com código de SCP informado);
Realiza ajustes na apuração, tanto do sócio ostensivo, quanto das SCPs;
Gera, através da Geração do Meio Magnético:
“1” arquivo para o Sócio Ostensivo;
“1” ou “N” arquivos para cada SCP.

[OS4316-C] Na geração por SCP, deverá ser observado o perfil definido na tela de “Dados Iniciais” (menu: Parâmetros >> Dados Iniciais) para geração dos registros, pois foi identificado que uma SCP pode ter um perfil de geração diferente da Sócia Ostensiva e este perfil é definido nesta tela (exemplo: Sócia Ostensiva apura no lucro real e SCP no lucro presumido).

Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo (Código da SCP não informada) como valido também para a SCP para o qual o arquivo está sendo gerado.