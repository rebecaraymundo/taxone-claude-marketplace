# MTZ_ECD_Versao_Leiaute_400

- **Fonte:** MTZ_ECD_Versao_Leiaute_400.docx
- **Modificado:** 2020-12-17
- **Tamanho:** 137 KB

---

THOMSON REUTERS

ECD

Atualização da Geração do Arquivo para atender ao Leiaute 4\.00

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-2473

Marcos G\. de Paula

Atualização das Informações do arquivo da ECD para atender à versão 4\.00 do Leiaute da ECD\.

MFS\-2632

Marcos G\. de Paula

Atualização das Informações do arquivo da ECD para atender à versão 4\.00 do Leiaute da ECD, incluindo ajustes para o cenário de empresas com Moeda Funcional\.

MFS\-3700

Marcos G\. de Paula

Atualização das Informações do arquivo da ECD para atender à versão 4\.00 do Leiaute da ECD, incluindo ajustes para o cenário de empresas com Moeda Funcional, conforme reposicionamento do fisco\.

MFS\-4347

Marcos G\. de Paula

Ajuste das descrições para o registro I020, cenário de Moeda Funcional\.

MFS\-4727

Marcos G\. de Paula

Definição da regra de ordenação do registro I200\.

MFS\-4878

Marcos G\. de Paula

Atualização das Informações dos demonstrativos da ECD \(Registros J100 e J150\) para atender o cenário de empresas com Moeda Funcional\.

CH15903\_2015

Julyana Perrucini

Este documento tem como objetivo tratar o preenchimento do campo NOME dos Registros 0000, I030 e J900, para considerar a Razão Social Complementar do Estabelecimento\.

CH17104\_2016

Lara Aline

Este documento tem como objetivo ajustar regra de ordenação do I550 incluindo os campos Data do Lançamento Contábil e Número de Lançamento pela ordem crescente\.

CH9864\_2017

Lara Aline

Ajuste no nome dos campos para o registro I020\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral__

Este documento tem como objetivo demonstrar as alterações da versão 4\.00 do leiaute da ECD em relação à versão 2\.00\. Este novo leiaute será obrigatório a partir do ano\-calendário 2015\.

Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão\.

Quando a empresa tem movimentação contábil em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) os registros pré\-existentes I020, I155, I157, I200, I250, I310 e I355, J100 e J150 terão a sua regra de geração alterada, conforme regras que serão detalhadas neste documento\. Observar que estas alterações se aplicam __somente às empresas que têm Movimentação em Moeda Funcional__\. Para aquelas que não têm este cenário, a __geração não deve ser alterada__\.

Basicamente o que altera é a inclusão de novas colunas para discriminação dos valores\. Estas colunas serão incluídas para que sejam demonstrados os valores em moeda funcional\. O novo layout determinou uma inversão dos valores, de modo que, as colunas já existentes nos registros passam a demonstrar os valores em moeda funcional e as novas, os valores em moeda corrente que eram demonstrados nas colunas antigas\.

Para o BP e DRE o impacto se dá na consolidação que realizamos para composição dos demonstrativos, pois também deverão refletir o valor em moeda funcional\.

MFS\-2473

MFS\-2632

MFS\-3700

__Alterações Registro 0000__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0000\-05

__Registro 0000 – Campo 05 – NOME__

__\[ALTERADA \- CH15903\_2016\]__

Este campo deve ser preenchido com o conteúdo do campo RAZAO\_SOCIAL ou do campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO\.

__Tratamento:__

- Se o campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO estiver preenchido, considerar o conteúdo dele na geração do campo desconsiderando o conteúdo do campo RAZAO\_SOCIAL, caso não esteja preenchido, buscar o conteúdo do campo RAZAO\_SOCIAL normalmente\.

__Observação:__ No campo RAZAO\_SOCIAL\_COMPL o usuário pode informar a razão social dos estabelecimentos que tenham mais do que 100 posições \(tamanho do campo “Razão Social” original do Mastersaf\)\. Esta informação será utilizada apenas quando preenchida, nas obrigações fiscais que permitam mais que 100 caracteres no preenchimento desta informação\.

CH15903\_2016

RN0000\-20

__Registro 0000 – Campo 20 – IDENT\_MF__

Este campo existe a partir da versão 4\.00\. Inicialmente será gerado com conteúdo fixo: “N”

Será gerado conforme parâmetro “ECD com Movimentação em Moeda Funcional” da tela de Dados Iniciais \(menu Parâmetros\):

Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”\.

Se o parâmetro estiver selecionado, será gerado com conteúdo “S”\.

MFS\-2473

MFS\-2632

__Alterações Registro I010__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI010\-03

__Registro I010 – Campo 03 – COD\_VER\_LC__

Para a versão 4\.00, será gerado com o código “4\.00”\.

MFS\-2473

__Alterações Registro I020__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI020\-00

__Registro I020 – Regra Geral__

Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00”, o registro I020 – Campos Adicionais, deve ser gerado no arquivo conforme estrutura definida na tabela “Conteúdo do Registro I020” abaixo indicada\.

Para cada linha do registro a ser gerada indicada na tabela deve ser verificada a obrigatoriedade de geração em relação ao Tipo de Livro \(colunas Livro ECD\) indicado na geração\. Somente devem ser geradas as linhas pertinentes ao Tipo de Livro correspondente\.

Na geração padrão podemos gerar o registro I020 incluindo campos adicionais nos registros I200 e I250, afetados por este processo\. Caso o usuário tenha realizado alguma parametrização para geração de campos adicionais em um destes registros \(menu Parâmetros >> Registro I020 – Campos Adicionais\), no momento da geração o campo “Sequencial do Campo Adicional” indicado pelo usuário deve ser alterado, de forma que os campos adicionais indicados pelo usuário sejam demonstrados após os campos definidos no layout indicados na tabela abaixo\. Deverá ser seguida a sequência após o último campo definido no layout padrão indicado abaixo\.

Exemplo:

Se o usuário parametrizou:

__01 \- REG__

__02 \- REG\_COD__

__03 \- NUM\_AD__

__04 \- CAMPO__

__05 \- DESCRIÇÃO__

__06 \- TIPO__

I020

I200

06

XPTO\_1

Campo de Teste 1\.

N

I020

I200

07

XPTO\_2

Campo de Teste 2\.

N

I020

I200

08

XPTO\_3

Campo de Teste 3\.

C

No arquivo deve ser gerado:

__01 \- REG__

__02 \- REG\_COD__

__03 \- NUM\_AD__

__04 \- CAMPO__

__05 \- DESCRIÇÃO__

__06 \- TIPO__

I020

I200

06

VL\_LCTO\_MF

Valor do lançamento em moeda que não reflita os efeitos da moeda funcional\.

N

I020

I200

06 07

XPTO\_1

Campo de Teste 1\.

N

I020

I200

07 08

XPTO\_2

Campo de Teste 2\.

N

I020

I200

08 09

XPTO\_3

Campo de Teste 3\.

C

__IMPORTANTE__: este reposicionamento dos campos reflete também no registro que recebe o campo adicional\. Neste exemplo, o registro I200, que deve ser gerado com a estrutura de campos adicionais demonstrada no registro I020\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro I020 não tenha sido selecionado, retornar a mensagem no log: “Empresa obrigada a demonstrar movimentações Contábeis em Moeda Funcional, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro I020 – Campos Adicionais”\.

__Conteúdo do Registro I020__

__Livro ECD__

__01 \- REG__

__02 \- REG\_COD__

__03 \- NUM\_AD__

__04 \- CAMPO__

__05 \- DESCRIÇÃO__

__06 \- TIPO__

__G__

__R__

__A__

__B__

I020

I155

10

VL\_SLD\_INI\_MF

Valor do saldo inicial do período em moeda que não reflita os efeitos da moeda funcional\.

Valor do saldo inicial do período em moeda funcional, convertida para reais\.

N

X

X

X

X

I020

I155

11

IND\_DC\_INI\_MF

Indicador da situação do saldo inicial em moeda que não reflita os efeitos da moeda funcional: D \- Devedor; C \- Credor\.

Indicador da situação do saldo inicial em moeda funcional: D \- Devedor; C \- Credor\.

C

X

X

X

X

I020

I155

12

VL\_DEB\_MF

Valor total dos débitos do período em moeda que não reflita os efeitos da moeda funcional\.

Valor total dos débitos do período em moeda funcional, convertida para reais\.

N

X

X

X

X

I020

I155

13

VL\_CRED\_MF

Valor total dos créditos do período em moeda que não reflita os efeitos da moeda funcional\.

Valor total dos créditos do período em moeda funcional\.

N

X

X

X

X

I020

I155

14

VL\_SLD\_FIN\_MF

Valor do saldo final do período em moeda que não reflita os efeitos da moeda funcional\.

Valor do saldo final do período em moeda funcional, convertida para reais\.

N

X

X

X

X

I020

I155

15

IND\_DC\_FIN\_MF

Indicador da situação do saldo final em moeda que não reflita os efeitos da moeda funcional: D \- Devedor; C \- Credor\.

Indicador da situação do saldo final em moeda funcional: D \- Devedor; C \- Credor\.

C

X

X

X

X

I020

I157

06

VL\_SLD\_INI\_MF

Valor do saldo inicial do período em moeda que não reflita os efeitos da moeda funcional\.

Valor do saldo inicial do período em moeda funcional, convertida para reais\.

N

X

X

 

X

I020

I157

07

IND\_DC\_INI\_MF

Indicador da situação do saldo inicial em moeda que não reflita os efeitos da moeda funcional: D \- Devedor; C \- Credor\.

Indicador da situação do saldo inicial em moeda funcional: D \- Devedor; C \- Credor\.

C

X

X

 

X

I020

I200

06

VL\_LCTO\_MF

Valor do lançamento em moeda que não reflita os efeitos da moeda funcional\.

Valor do lançamento em moeda funcional, convertida para reais\.

N

X

X

X

 

I020

I250

10

VL\_DC\_MF

Valor da partida em moeda que não reflita os efeitos da moeda funcional\.

Valor da partida em moeda funcional, convertida para reais\.

N

X

X

X

 

I020

I250

11

IND\_DC\_MF

Indicador da natureza da partida em moeda que não reflita os efeitos da moeda funcional: D \- Débito; C \- Crédito\.

Indicador da natureza da partida em moeda funcional: D \- Débito; C \- Crédito\.

C

X

X

X

 

I020

I310

06

VAL\_DEB\_MF

Total dos débitos do dia em moeda que não reflita os efeitos da moeda funcional\.

Total dos débitos do dia em moeda funcional, convertida para reais\.

N

 

 

 

X

I020

I310

07

VAL\_CRED\_MF

Total dos créditos do dia em moeda que não reflita os efeitos da moeda funcional\.

Total dos créditos do dia em moeda funcional, convertida  para reais\.

N

 

 

 

X

I020

I355

06

VL\_CTA\_MF

Valor do saldo final antes do lançamento de encerramento em moeda  que não reflita os efeitos da moeda funcional\.

Valor do saldo final antes do lançamento de encerramento em moeda funcional, convertida para reais\.

N

X

X

 

X

I020

I355

07

IND\_DC\_MF

Indicador da situação do saldo final em moeda que não reflita os efeitos da moeda funcional: D \- Devedor; C \- Credor\.

Indicador da situação do saldo final em moeda funcional: D \- Devedor; C \- Credor\.

C

X

X

 

X

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

MFS\-4347

CH9864\_2017

__Alterações Registro I030__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI030\-06

__Registro I030 – Campo 06 – NOME__

__\[ALTERADA \- CH15903\_2016\]__

Este campo deve ser preenchido com o conteúdo do campo RAZAO\_SOCIAL ou do campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO\.

__Tratamento:__

- Se o campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO estiver preenchido, considerar o conteúdo dele na geração do campo desconsiderando o conteúdo do campo RAZAO\_SOCIAL, caso não esteja preenchido, buscar o conteúdo do campo RAZAO\_SOCIAL normalmente\.

__Observação:__ No campo RAZAO\_SOCIAL\_COMPL o usuário pode informar a razão social dos estabelecimentos que tenham mais do que 100 posições \(tamanho do campo “Razão Social” original do Mastersaf\)\. Esta informação será utilizada apenas quando preenchida, nas obrigações fiscais que permitam mais que 100 caracteres no preenchimento desta informação\.

CH15903\_2016

__Alterações Registro I155__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI155\-00

__Registro I155 – Regra geral__

__Origem da Informação__: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo, SAFX102 \- Arquivo de Saldos Mensais Auxiliar, SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional e SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

__Regra de geração__: Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00”, a estrutura do registro I155 será gerada conforme definida neste documento e considerando, além das tabelas já utilizadas atualmente, as tabelas de movimentação em Moeda Funcional indicadas no item “Origem da Informação”\.

Devem ser respeitadas as regras atuais de recuperação dos registros, demonstrando o I155 como filho do I150 e recuperando os saldos cuja data da operação compreenda o período demonstrado no registro pai\. 

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”\.

Para geração dos saldos dos Livros Geral, Resumido e Balancete, devem ser considerados registros das tabelas SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo, SAFX226 \- Saldo Contábil em Moeda Funcional e SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional, sendo que, registros das SAFX80 e SAFX227 somente devem ser considerados se a opção “Omitir informações de Centro de Custo em Lançamentos Contábeis e Saldos” não estiver selecionada\. Se esta opção estiver selecionada, considerar os registros carregados nestas tabelas e caso exista nas tabelas SAFX02 e SAFX226 registros da mesma empresa, estabelecimento, período e conta, desprezar os registros correspondentes das SAFX02 e SAFX226 e considerar somente o informado nas SAFX80 e SAFX227\.

Para geração dos saldos do Livro Auxiliar, devem ser considerados registros das tabelas SAFX102 \- Arquivo de Saldos Mensais Auxiliar e SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional, considerando registros cuja conta contábil tenha sido parametrizada na tela de Livros Auxiliares ao Diário \(menu parâmetros\) para o Livro selecionado na tela de geração do meio magnético\.

Tanto as tabelas de movimentação normal quanto as de movimentação em moeda funcional devem servir de base para geração deste registro\. Podemos ter situação onde teremos valores em moeda funcional, mas não teremos em moeda corrente \(o contrário também é possível\), neste caso, as colunas no registro onde os valores em moeda corrente seriam demonstrados serão apresentados zerados\.

__Agrupamento__: campos 02 – COD\_CTA e 03 – COD\_CCUS

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

RNI155\-01

__Registro I155 – Campo 01 – REG__

Texto fixo: “I155”\.

MFS\-2632

RNI155\-02

__Registro I155 – Campo 02 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o código da conta contábil\. Este código deve ter seu cadastro apresentado no registro I050\.

MFS\-2632

RNI155\-03

__Registro I155 – Campo 03 – COD\_CCUS__

Considerando a Origem da Informação, demonstrar aqui o código do centro de custo\. Este código deve ter seu cadastro apresentado no registro I100\.

MFS\-2632

RNI155\-04

__Registro I155 – Campo 04 – VL\_SLD\_INI__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-05

__Registro I155 – Campo 05 – IND\_DC\_INI__

Considerar o Resultado apurado para a coluna Saldo inicial\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

RNI155\-06

__Registro I155 – Campo 06 – VL\_DEB__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Débitos registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Débitos registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-07

__Registro I155 – Campo 07 – VL\_CRED__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Créditos registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Créditos registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-08

__Registro I155 – Campo 08 – VL\_SLD\_FIN__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Final registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Final registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-09

__Registro I155 – Campo 09 – IND\_DC\_FIN__

Considerar o Resultado apurado para a coluna Saldo Final\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

RNI155\-10

__Registro I155 – Campo 10 – VL\_SLD\_INI\_AUX__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-11

__Registro I155 – Campo 11 – IND\_DC\_INI\_AUX__

Considerar o Resultado apurado para a coluna Saldo inicial\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

RNI155\-12

__Registro I155 – Campo 12 – VL\_DEB\_AUX__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Débitos registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Débitos registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-13

__Registro I155 – Campo 13 – VL\_CRED\_AUX__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Créditos registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Total de Créditos registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-14

__Registro I155 – Campo 14 – VL\_SLD\_FIN\_AUX__

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Final registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX226 \- Saldo Contábil em Moeda Funcional, SAFX227 \- Saldo Contábil por Centro de Custo em Moeda Funcional ou SAFX229 \- Saldo Contábil Auxiliar em Moeda Funcional\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Respeitando a regra de seleção, neste campo será demonstrada a consolidação do Valor do Saldo Final registrado em uma das tabelas de Movimentação Contábil padrão: SAFX02 \- Arquivo de Saldos Mensais, SAFX80 \- Arquivo de Saldos Contábeis para Centro Custo ou SAFX102 \- Arquivo de Saldos Mensais Auxiliar\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI155\-15

__Registro I155 – Campo 15 – IND\_DC\_FIN\_AUX__

Considerar o Resultado apurado para a coluna Saldo Final\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

__Alterações Registro I157__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI157\-00

__Registro I157 – Regra Geral__

__Origem da Informação__: SAFX188 \- Transferência de Saldos de Plano de Contas Anterior, SAFX189 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo, SAFX230 \- Transferência de Saldos de Plano de Contas Anterior em Moeda Funcional e SAFX231 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional\.

__Regra de geração__: Este registro é filho do I155\. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado\.

__Agrupamento__: campos 02 – COD\_CTA e 03 – COD\_CCUS

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

RNI157\-01

__Registro I157 – Campo 01 – REG__

Texto fixo: “I157”\.

MFS\-2632

RNI157\-02

__Registro I157 – Campo 02 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o código da Conta Contábil do Lançamento do Plano de Contas Anterior\. Este código deve ter seu cadastro apresentado no registro I050\.

MFS\-2632

RNI157\-03

__Registro I157 – Campo 03 – COD\_CCUS__

Considerando a Origem da Informação, demonstrar aqui o código do Centro de Custo do Plano de Contas Anterior\. Este código deve ter seu cadastro apresentado no registro I100\.

MFS\-2632

RNI157\-04

__Registro I157 – Campo 04 – VL\_SLD\_INI__

Neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação Contábil padrão: SAFX188 \- Transferência de Saldos de Plano de Contas Anterior ou SAFX189 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX230 \- Transferência de Saldos de Plano de Contas Anterior em Moeda Funcional ou SAFX231 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI157\-05

__Registro I157 – Campo 05 – IND\_DC\_INI__

Considerar o Resultado apurado para a coluna Saldo Inicial\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

RNI157\-06

__Registro I157 – Campo 06 – VL\_SLD\_INI\_AUX__

Neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX230 \- Transferência de Saldos de Plano de Contas Anterior em Moeda Funcional ou SAFX231 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

Neste campo será demonstrada a consolidação do Valor do Saldo Inicial registrado em uma das tabelas de Movimentação Contábil padrão: SAFX188 \- Transferência de Saldos de Plano de Contas Anterior ou SAFX189 \- Transferência de Saldos de Plano de Contas Anterior por Centro de Custo\.

Para a realização da consolidação, considerar a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “D” __menos__ a soma dos registros cujo Valor do Saldo Inicial tenha Ind\. D/C do SI igual a “C”\. Demonstrar sempre o valor positivo\.

*Obs\.: estou considerando a consolidação como padrão por conta da geração por estabelecimento centralizado, que considera também os dados dos centralizadores\. No caso de uma geração descentralizada, mesmo que aplicada esta regra, não causaria impacto\.*

MFS\-2632

MFS\-3700

RNI157\-07

__Registro I157 – Campo 07 – IND\_DC\_INI\_AUX__

Considerar o Resultado apurado para a coluna Saldo Inicial\. Se o valor apurado for maior ou igual a zero, gerar neste campo o conteúdo “D”\. Se for menor que zero, gerar neste campo o conteúdo “C”\.

MFS\-2632

__Alterações Registro I200__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI200\-00

__Registro I200 – Regra Geral__

__Origem da Informação__: SAFX01 \- Arquivo Contábil, SAFX101 \- Arquivo Contábil Auxiliar, SAFX225 \- Lançamento Contábil em Moeda Funcional e SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional

__Regra de geração__: Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00”, a estrutura do registro I200 será gerada conforme definida neste documento e considerando, além das tabelas já utilizadas atualmente, as tabelas de movimentação em Moeda Funcional indicadas no item “Origem da Informação”\.

Devem ser respeitadas as regras atuais de recuperação dos registros, demonstrando o I155 como filho do I150 e recuperando os saldos cuja data da operação compreenda o período demonstrado no registro pai\. 

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”\.

Para geração dos lançamentos dos Livros Geral e Resumido, devem ser considerados registros das tabelas SAFX01 \- Arquivo Contábil e SAFX225 \- Lançamento Contábil em Moeda Funcional\.

Para geração dos lançamentos do Livro Auxiliar, devem ser considerados registros das tabelas SAFX101 \- Arquivo Contábil Auxiliar e SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional, considerando registros cuja conta contábil tenha sido parametrizada na tela de Livros Auxiliares ao Diário \(menu parâmetros\) para o Livro selecionado na tela de geração do meio magnético\.

Tanto as tabelas de movimentação normal quanto as de movimentação em moeda funcional devem servir de base para geração deste registro\. Podemos ter situação onde teremos registros em moeda funcional, mas não teremos nas tabelas de moeda corrente \(o contrário também é possível\), neste caso, as colunas no registro onde os valores em moeda corrente seriam demonstrados serão apresentados zerados\.

__Agrupamento__: campos 02 – NUM\_LCTO e 03 – DT\_LCTO

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

__Ordenação__: campos 03 – DT\_LCTO \(ordem cronológica\) e 02 – NUM\_LCTO

MFS\-2632

MFS\-4727

RNI200\-01

__Registro I200 – Campo 01 – REG__

Texto fixo: “I1200”\.

MFS\-2632

RNI200\-02

__Registro I200 – Campo 02 – NUM\_LCTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Número do Lançamento\.

MFS\-2632

RNI200\-03

__Registro I200 – Campo 03 – DT\_LCTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data da Operação\.

MFS\-2632

RNI200\-04

__Registro I200 – Campo 04 – VL\_LCTO__

Será resultado da somatória do campo 04 – VL\_DC do registro filho I250, considerando registros cujo campo 05 – IND\_DC seja igual a “D”\.

MFS\-2632

RNI200\-05

__Registro I200 – Campo 05 – IND\_LCTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Tipo do Lançamento\.

MFS\-2632

RNI200\-06

__Registro I200 – Campo 06 – VL\_LCTO\_AUX__

Será resultado da somatória do campo 04 – VL\_DC\_AUX do registro filho I250, considerando registros cujo campo 05 – IND\_DC seja igual a “D”\.

MFS\-2632

__Alterações Registro I250__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI250\-00

__Registro I250 – Regra Geral__

__Origem da Informação__: SAFX01 \- Arquivo Contábil, SAFX101 \- Arquivo Contábil Auxiliar, SAFX225 \- Lançamento Contábil em Moeda Funcional e SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional

__Regra de geração__: Este registro é filho do I200\. Nele serão detalhadas as informações dos Lançamentos Contábeis cujos valores foram consolidados no registro pai\. Para cada Número de Lançamento informado no registro pai demonstraremos aqui o detalhe da informação\.

__Agrupamento__: 

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

RNI250\-01

__Registro I250 – Campo 01 – REG__

Texto fixo: “I1250”\.

MFS\-2632

RNI250\-02

__Registro I250 – Campo 02 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o código da Conta Contábil\. Este código deve ter seu cadastro apresentado no registro I050\.

MFS\-2632

RNI250\-03

__Registro I250 – Campo 03 – COD\_CCUS__

Considerando a Origem da Informação, demonstrar aqui o código do Centro de Custo\. Este código deve ter seu cadastro apresentado no registro I100\.

Se a opção “Omitir informações de Centro de Custo em Lançamentos Contábeis e Saldos” da tela de Dados Iniciais \(menu Parâmetros\) estiver selecionada, não gerar conteúdo neste campo\.

MFS\-2632

RNI250\-04

__Registro I250 – Campo 04 – VL\_DC__

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil ou SAFX101 \- Arquivo Contábil Auxiliar\.

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI250\-05

__Registro I250 – Campo 05 – IND\_DC__

Neste campo será demonstrado o Débito/Crédito do Lançamento Contábil registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil ou SAFX101 \- Arquivo Contábil Auxiliar\.

Neste campo será demonstrado o Débito/Crédito do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI250\-06

__Registro I250 – Campo 06 – NUM\_ARQ__

Considerando a Origem da Informação, demonstrar aqui o número do Arquivamento\.

MFS\-2632

RNI250\-07

__Registro I250 – Campo 07 – COD\_HIST\_PAD__

Considerando a Origem da Informação, demonstrar aqui o código do Histórico Padrão\. Este código deve ter seu cadastro apresentado no registro I075\.

MFS\-2632

RNI250\-08

__Registro I250 – Campo 08 – HIST__

Considerando a Origem da Informação, demonstrar aqui o conteúdo do campo Histórico Complementar\.

MFS\-2632

RNI250\-09

__Registro I250 – Campo 09 – COD\_PART__

Considerando a Origem da Informação, demonstrar aqui a concatenação dos campos Indicador da Pessoa Física/Jurídica \+ “\-“ \+ Código da Pessoa Física/Jurídica\. Este código deve ter seu cadastro apresentado no registro 0150\.

MFS\-2632

RNI250\-10

__Registro I250 – Campo 10 – VL\_DC\_AUX__

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional\.

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil ou SAFX101 \- Arquivo Contábil Auxiliar\.

MFS\-2632

MFS\-3700

RNI250\-11

__Registro I250 – Campo 11 – IND\_DC\_AUX__

Neste campo será demonstrado o Débito/Crédito do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX228 \- Lançamento Contábil Auxiliar em Moeda Funcional\.

Neste campo será demonstrado o Débito/Crédito do Lançamento Contábil registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil ou SAFX101 \- Arquivo Contábil Auxiliar\.

MFS\-2632

MFS\-3700

__Alterações Registro I310__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI310\-00

__Registro I310 – Regra Geral__

__Origem da Informação__: SAFX01 \- Arquivo Contábil e SAFX225 \- Lançamento Contábil em Moeda Funcional

__Regra de geração__: Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00”, a estrutura do registro I310 será gerada conforme definida neste documento e considerando, além das tabelas já utilizadas atualmente, as tabelas de movimentação em Moeda Funcional indicadas no item “Origem da Informação”\.

Devem ser respeitadas as regras atuais de recuperação dos registros, demonstrando o I310 como filho do I300 e recuperando os lançamentos cuja data da operação seja a mesma demonstrada no registro pai\. 

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”\.

Este registro será gerado apenas para Livro tipo Balancete\.

Tanto as tabelas de movimentação normal quanto as de movimentação em moeda funcional devem servir de base para geração deste registro\. Podemos ter situação onde teremos valores em moeda funcional, mas não teremos em moeda corrente \(o contrário também é possível\), neste caso, as colunas no registro onde os valores em moeda corrente seriam demonstrados serão apresentados zerados\.

__Agrupamento__: campos 02 – COD\_CTA e 03 – COD\_CCUS

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

RNI310\-01

__Registro I310 – Campo 01 – REG__

Texto fixo: “I310”\.

MFS\-2632

RNI310\-02

__Registro I310 – Campo 02 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o código da Conta Contábil\. Este código deve ter seu cadastro apresentado no registro I050\.

MFS\-2632

RNI310\-03

__Registro I310 – Campo 03 – COD\_CCUS__

Considerando a Origem da Informação, demonstrar aqui o código do Centro de Custo\. Este código deve ter seu cadastro apresentado no registro I100\.

Se a opção “Omitir informações de Centro de Custo em Lançamentos Contábeis e Saldos” da tela de Dados Iniciais \(menu Parâmetros\) estiver selecionada, não gerar conteúdo neste campo\.

MFS\-2632

RNI310\-04

__Registro I310 – Campo 04 – VAL\_DEBD__

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “D” registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil\.

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “D” registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI310\-05

__Registro I310 – Campo 05 – VAL\_CREDD__

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “C” registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil\.

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “C” registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI310\-06

__Registro I310 – Campo 06 – VAL\_DEBD\_AUX__

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “D” registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional\.

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “D” registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil\.

MFS\-2632

MFS\-3700

RNI310\-07

__Registro I310 – Campo 07 – VAL\_CREDD\_AUX__

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “C” registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional\.

Neste campo será demonstrada a somatória do Valor do Lançamento Contábil que tenham Ind\. Débito/Crédito igual a “C” registrado em uma das tabelas de Movimentação Contábil padrão: SAFX01 \- Arquivo Contábil\.

MFS\-2632

MFS\-3700

__Alterações Registro I355__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI355\-00

__Registro I355 – Regra Geral__

__Origem da Informação__: SAFX01 \- Arquivo Contábil, SAFX225 \- Lançamento Contábil em Moeda Funcional, SAFX169 \- Saldo Antes do Encerramento e SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

__Regra de geração__: Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00”, a estrutura do registro I355 será gerada conforme definida neste documento e considerando, além das tabelas já utilizadas atualmente, as tabelas de movimentação em Moeda Funcional indicadas no item “Origem da Informação”\.

Devem ser respeitadas as regras atuais de recuperação dos registros, demonstrando o I355 como filho do I350 e recuperando os lançamentos cuja data da operação seja a mesma demonstrada no registro pai\. Se o parâmetro “Saldo Antes do Encerramento \(SAFX169\)” da tela de Dados Iniciais \(menu Parâmetros\) não estiver selecionado, considerar como origem somente as tabelas SAFX01 \- Arquivo Contábil e SAFX225 \- Lançamento Contábil em Moeda Funcional, recuperando somente registros que tenham o Tipo de Lançamento igual a E – Encerramento\. Se o referido parâmetro estiver selecionado, considerar como origem somente as tabelas SAFX169 \- Saldo Antes do Encerramento e SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

Se se tratar de uma geração através de um estabelecimento centralizador, devem ser recuperados dados do centralizador e de seus centralizados e os registros consolidados, conforme campos definidos no item “Agrupamento”\.

Este registro será gerado apenas para Livro tipo Geral, Resumido e Balancete\.

Tanto as tabelas de movimentação normal quanto as de movimentação em moeda funcional devem servir de base para geração deste registro\. Podemos ter situação onde teremos valores em moeda funcional, mas não teremos em moeda corrente \(o contrário também é possível\), neste caso, as colunas no registro onde os valores em moeda corrente seriam demonstrados serão apresentados zerados\.

__Agrupamento__: campos 02 – COD\_CTA e 03 – COD\_CCUS

Quando a empresa __não tem__ movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __não selecionado__ na tela de Dados Iniciais – menu Parâmetros\), a geração deste registro se mantém inalterada\.

Observar que o relatório de conferência do registro deve ser ajustado para demonstrar os novos campos criados no registro no cenário de moeda funcional\.

MFS\-2632

RNI355\-01

__Registro I355 – Campo 01 – REG__

Texto fixo: “I355”\.

MFS\-2632

RNI355\-02

__Registro I355 – Campo 02 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o código da Conta Contábil\. Este código deve ter seu cadastro apresentado no registro I050\.

MFS\-2632

RNI355\-03

__Registro I355 – Campo 03 – COD\_CCUS__

Considerando a Origem da Informação, demonstrar aqui o código do Centro de Custo\. Este código deve ter seu cadastro apresentado no registro I100\.

Se a opção “Omitir informações de Centro de Custo em Lançamentos Contábeis e Saldos” da tela de Dados Iniciais \(menu Parâmetros\) estiver selecionada, não gerar conteúdo neste campo\.

MFS\-2632

RNI355\-04

__Registro I355 – Campo 04 – VL\_CTA__

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda padrão: SAFX01 \- Arquivo Contábil ou SAFX169 \- Saldo Antes do Encerramento\.

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI355\-05

__Registro I355 – Campo 05 – IND\_DC__

Neste campo será demonstrado o conteúdo invertido do campo Ind\. Débito/Crédito \(se “C”, gera “D”; se “D”\. gera “C”\) do que foi registrado na SAFX01 \- Arquivo Contábil ou o conteúdo do campo Ind\. Débito/Crédito registrado na tabela SAFX169 \- Saldo Antes do Encerramento\.

Neste campo será demonstrado o conteúdo invertido do campo Ind\. Débito/Crédito \(se “C”, gera “D”; se “D”\. gera “C”\) do que foi registrado na SAFX225 \- Lançamento Contábil em Moeda Funcional ou o conteúdo do campo Ind\. Débito/Crédito registrado na tabela SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

MFS\-2632

MFS\-3700

RNI355\-06

__Registro I355 – Campo 06 – VL\_CTA\_AUX__

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda Funcional: SAFX225 \- Lançamento Contábil em Moeda Funcional ou SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

Neste campo será demonstrado o Valor do Lançamento Contábil registrado em uma das tabelas de Movimentação em Moeda padrão: SAFX01 \- Arquivo Contábil ou SAFX169 \- Saldo Antes do Encerramento\.

MFS\-2632

MFS\-3700

RNI355\-07

__Registro I355 – Campo 07 – IND\_DC\_AUX__

Neste campo será demonstrado o conteúdo invertido do campo Ind\. Débito/Crédito \(se “C”, gera “D”; se “D”\. gera “C”\) do que foi registrado na SAFX225 \- Lançamento Contábil em Moeda Funcional ou o conteúdo do campo Ind\. Débito/Crédito registrado na tabela SAFX232 \- Saldo Antes do Encerramento em Moeda Funcional\.

Neste campo será demonstrado o conteúdo invertido do campo Ind\. Débito/Crédito \(se “C”, gera “D”; se “D”\. gera “C”\) do que foi registrado na SAFX01 \- Arquivo Contábil ou o conteúdo do campo Ind\. Débito/Crédito registrado na tabela SAFX169 \- Saldo Antes do Encerramento\.

MFS\-2632

MFS\-3700

__Alterações Registro J100__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ100\-00

__Registro J100 – Regra Geral para o Cenário de Moeda Funcional__

Critérios para geração do Balanço Patrimonial em Moeda Funcional:

O registro J100 é um agrupamento de informações por Código de Aglutinação \(campo 02 – COD\_AGL\) e ele é gerado sempre que na tela de geração do Meio Magnético está selecionada a opção “Balanço Patrimonial”\. Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __E__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00” __E__ o parâmetro “Gerar Balanço Patrimonial e DRE com base nos valores de Moeda Funcional” \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\), o registro J100 que atualmente considera informações da tabela SAFX02 \- Arquivo de Saldos Mensais, deverá ser gerado com base nos saldos registrados na tabela SAFX226 \- Saldo Contábil em Moeda Funcional, respeitando as mesmas regras de consolidação por código de aglutinação existentes\.

Neste contexto, teremos:

- __Origem das Informações__: SAFX226 \- Saldo Contábil em Moeda Funcional
- __Regra de Seleção__: para composição do Registro J100 – Balanço Patrimonial, que será gerado com valores em moeda funcional \(observar critérios indicados acima\) deverão ser considerados os registros da tabela SAFX226 – Saldo Contábil em Moeda Funcional da empresa e estabelecimento \(ou estabelecimentos, para o caso de geração centralizada\) parametrizados na geração, cuja Data da Operação \(campo 04 \- DATA\_OPERACAO\) compreenda os períodos \(mês e ano\) indicados nos campos 02 – DT\_INI e 03 – DT\_FIN do registro J005, pai do registro J100 e cujo campo Conta Contábil \(campo 03 \- COD\_CONTA\) esteja preenchido com o Código de Conta Contábil parametrizado na tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\)\.

Na composição do registro os valores serão totalizados por Código de Aglutinação \(campo 02 – COD\_AGL\), onde, cada Código de Aglutinação receberá os valores das contas contábeis associadas a ele através da tela de “Selecionar Contas da Empresa para Apuração” \(acessado através da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial, menu Manutenção\)\.

Então, temos o seguinte exemplo:

__Cód\. Aglutinação__

__Classificação__

__Contas Associadas__

__Saldo__

__Indicador__

__2\.1\.1__

__Subtotalizador/Totalizador__

__>>>>>>>>>>>>>>>>>>__

__500,00__

__D__

*Por ser um “Subtotalizador/Totalizador”, agrupa informações dos Cód\. Aglutinação “2\.1\.1\.1” e “2\.1\.1\.2”, por consequência, considera as contas parametrizadas nestes códigos para composição do seu valor\. Não permite associação com conta contábil\.*

1\.00\.00\.00\.01

2000,00

D

1\.00\.00\.00\.02

3000,00

C

1\.00\.00\.00\.03

1500,00

D

__2\.1\.1\.1__

__Ativo__

__>>>>>>>>>>>>>>>>>>__

__1000,00__

__C__

*Contas Contábeis parametrizadas*

1\.00\.00\.00\.01

2000,00

D

1\.00\.00\.00\.02

3000,00

C

__2\.1\.1\.2__

__Ativo__

__>>>>>>>>>>>>>>>>>>__

__1500,00__

__D__

*Contas Contábeis parametrizadas*

1\.00\.00\.00\.03

1500,00

D

- __Registro Pai__: J005 – Demonstrações Contábeis
- __Campos\-Chave__: 02 – COD\_AGL
- __Ordenação__: Considerar informação do campo Ordem da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\) para ordenar o registro no arquivo\.

Esta regra se aplica única e exclusivamente para geração das informações em Moeda Funcional\. As informações já geradas no registro J100, cuja origem é a tabela de Saldo Contábil \(SAFX02\) se mantém inalterada\.

Observar que, uma vez que o usuário faz a opção de gerar o Balanço Patrimonial em Moeda Funcional \(observar critérios indicados acima\), o relatório de conferência gerado no momento da geração do arquivo também deve refletir os valores em Moeda Funcional\.

*Informação adicional: a geração do registro pode ser realizada através do próprio Meio magnético gerado\. Para isso, seria necessário recuperar as informações dos registros de Saldos, I155\.*

 

MFS\-2632

MFS\-3700

MFS\-4878

RNJ100\-01

__Campo 01 – REG__

Será gerado com informação fixa “J100”\.

MFS\-4878

RNJ100\-02

__Campo 02 – COD\_AGL__

Será gerado com a informação do campo Código de Aglutinação da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\)\.

MFS\-4878

RNJ100\-03

__Campo 03 – NIVEL__

Será gerado com a informação do campo Nível da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\)\.

MFS\-4878

RNJ100\-04

__Campo 04 – IND\_GRP\_BAL__

Será gerado com base na informação do campo Classificação da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\), sendo que:

Se o campo estiver preenchido com a opção “Ativo” ou “Subtotalizador/Totalizador Ativo”, será gerado com conteúdo 1 – Ativo;

Se o campo estiver preenchido com a opção “Passivo ou Patrimônio Líquido” ou “Subtotalizador/Totalizador Passivo ou PL”, será gerado com conteúdo 2 – Passivo e Patrimônio Líquido;

MFS\-4878

RNJ100\-05

__Campo 05 – DESCR\_COD\_AGL__

Será gerado com a informação do campo Descrição da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\)\.

MFS\-4878

RNJ100\-06

__Campo 06 – VL\_CTA__

Será resultado da sumarização do valor do Saldo Final \(campo 07 – VLR\_SALDO\_FIM\) da SAFX226, dos registro de saldo selecionados cuja Data da Operação \(campo 04 \- DATA\_OPERACAO\) compreenda o período \(mês e ano\) indicado no campo 03 – DT\_FIN do registro J005, das contas parametrizadas\.

Nesta sumarização devemos considerar também o Indicador da Situação do Saldo Final \(campo 08 \- IND\_SALDO\_FIM\), de modo que podemos consolidar considerando o seguinte cálculo:

Total dos Saldos das Contas parametrizadas cujo campo 08 \- IND\_SALDO\_FIM seja igual a “D” __menos__ Total dos Saldos das Contas parametrizadas cujo campo 08 \- IND\_SALDO\_FIM seja igual a “C”\.

 

O cálculo acima indicado se aplica aos códigos de aglutinação com Classificação igual a “Ativo” ou “Passivo ou Patrimônio Líquido” que tem as contas contábeis associadas\. Para os códigos de aglutinação com Classificação igual a “Subtotalizador/Totalizador”, será aplicado o mesmo cálculo, porém, podemos considerar o valor das contas contábeis associadas aos códigos de aglutinação que foram vinculados ao código Totalizador\.

Deve ser demonstrado sempre o resultado positivo\.

*Informação Adicional: se fossemos considerar as informações do meio magnético para compor o BP, esta informação teria origem no registro I155, campos 14 – VL\_SLD\_FIN\_AUX e 15 – IND\_DC\_FIN\_AUX\.*

MFS\-4878

RNJ100\-07

__Campo 07 – IND\_DC\_BAL__

Este campo é gerado em função do cálculo realizado no campo 06 – VL\_CTA\. Devemos aplicar a seguinte regra:

Se o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “C”\. Se for zero ou positivo, gerar “D”\.

MFS\-4878

RNJ100\-08

__Campo 08 – VL\_CTA\_INI__

Será resultado da sumarização do valor do Saldo Inicial \(campo 05 – VLR\_SALDO\_INI\) da SAFX226, dos registro de saldo selecionados cuja Data da Operação \(campo 04 \- DATA\_OPERACAO\) compreenda o período \(mês e ano\) indicado no campo 02 – DT\_INI do registro J005, das contas parametrizadas\.

Nesta sumarização devemos considerar também o Indicador da Situação do Saldo Inicial \(campo 06 \- IND\_SALDO\_INI\), de modo que podemos consolidar considerando o seguinte cálculo:

Total dos Saldos das Contas parametrizadas cujo campo 06 \- IND\_SALDO\_INI seja igual a “D” __menos__ Total dos Saldos das Contas parametrizadas cujo campo 06 \- IND\_SALDO\_INI seja igual a “C”\.

 

O cálculo acima indicado se aplica aos códigos de aglutinação com Classificação igual a “Ativo” ou “Passivo ou Patrimônio Líquido” que tem as contas contábeis associadas\. Para os códigos de aglutinação com Classificação igual a “Subtotalizador/Totalizador”, será aplicado o mesmo cálculo, porém, podemos considerar o valor das contas contábeis associadas aos códigos de aglutinação que foram vinculados ao código Totalizador\.

Deve ser demonstrado sempre o resultado positivo\.

*Informação Adicional: se fossemos considerar as informações do meio magnético para compor o BP, esta informação teria origem no registro I155, campos 10 – VL\_SLD\_INI\_AUX e 11 – IND\_DC\_INI\_AUX\.*

MFS\-4878

RNJ100\-09

__Campo 09 – IND\_DC\_BAL\_INI__

Este campo é gerado em função do cálculo realizado no campo 08 – VL\_CTA\_INI\. Devemos aplicar a seguinte regra:

Se o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “C”\. Se for zero ou positivo, gerar “D”\.

MFS\-4878

__Alterações Registro J150__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ150\-00

__Registro J150 – Regra Geral para o Cenário de Moeda Funcional__

Critérios para geração da Demonstração de Resultado em Moeda Funcional:

O registro J150 é um agrupamento de informações por Código de Aglutinação \(campo 02 – COD\_AGL\) e ele é gerado sempre que na tela de geração do Meio Magnético está selecionada a opção “Demonstração de Resultado”\. Quando a empresa tem movimentação em Moeda Funcional \(Parâmetro “ECD com Movimentação em Moeda Funcional” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __E__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “4\.00” __E__ o parâmetro “Gerar Balanço Patrimonial e DRE com base nos valores de Moeda Funcional” estiver __selecionado__ na tela de Dados Iniciais \(menu Parâmetros\), o registro J150 que atualmente considera informações do próprio Registro I350, deverá ser gerado com base nos saldos registrados na tabela SAFX225 \- Lançamento Contábil em Moeda Funcional \(ou o próprio I355, conforme avaliação técnica de viabilidade\), respeitando as mesmas regras de consolidação por código de aglutinação existentes\.

Neste contexto, teremos:

- __Origem das Informações__: SAFX225 \- Lançamento Contábil em Moeda Funcional \(ou registro I355, conforme avaliação técnica\)
- __Regra de Seleção__: para composição do Registro J150 – Demonstração de Resultado do Exercício, que será gerado com valores em moeda funcional \(observar critérios indicados acima\) serão considerados os registros da tabela SAFX225 – Lançamento Contábil em Moeda Funcional da empresa e estabelecimento \(ou estabelecimentos, para o caso de geração centralizada\) parametrizados na geração, cuja Data da Operação \(campo 03 \- DATA\_OPERACAO\) compreenda o período \(mês e ano\) imediatamente anterior ao indicado no campo 02 – DT\_INI e no mesmo período \(mês e ano\) indicado no campo 03 – DT\_FIN do registro J005, pai do registro J150 e cujo campo Conta Contábil \(campo 03 \- COD\_CONTA\) ou Conta Contábil \+ Centro de Custo \(campo 09 – CENTRO\_CUSTO\) esteja preenchido com o Código de Conta Contábil ou Conta Contábil \+ Centro de Custo parametrizado na tela “Selecionar Contas da Empresa para Apuração” \(acessado através da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Demonstração de Resultado, menu Manutenção\) e restringindo a seleção a Lançamentos cujo Tipo do Lançamento \(campo 13 – TIPO\_LANCTO\) seja igual a E – Encerramento\.

Na composição do registro os valores serão totalizados por Código de Aglutinação \(campo 02 – COD\_AGL\), onde, cada Código de Aglutinação receberá os valores das contas contábeis ou contas contábeis \+ centros de custo associadas a ele através da tela de “Selecionar Contas da Empresa para Apuração” \(acessado através da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Demonstração de Resultado, menu Manutenção\)\.

Então, temos o seguinte exemplo:

__Cód\. Aglutinação__

__Classificação__

__Contas Associadas__

__Saldo__

__Indicador__

__4\.1\.1__

__Subtotalizador/Totalizador__

__>>>>>>>>>>>>>>>>>>__

__500,00__

__D__

*Por ser um “Subtotalizador/Totalizador”, agrupa informações dos Cód\. Aglutinação “4\.1\.1\.1” e “4\.1\.1\.2”, por consequência, considera as contas parametrizadas nestes códigos para composição do seu valor\. Não permite associação com conta contábil\.*

1\.00\.00\.00\.01

2000,00

D

1\.00\.00\.00\.02

3000,00

C

1\.00\.00\.00\.03

1500,00

D

__4\.1\.1\.1__

__Receita/Despesa__

__>>>>>>>>>>>>>>>>>>__

__1000,00__

__C__

*Contas Contábeis parametrizadas*

1\.00\.00\.00\.01

2000,00

D

1\.00\.00\.00\.02

3000,00

C

__4\.1\.1\.2__

__Receita/Despesa__

__>>>>>>>>>>>>>>>>>>__

__1500,00__

__D__

*Contas Contábeis parametrizadas*

1\.00\.00\.00\.03

1500,00

D

- __Registro Pai__: J005 – Demonstrações Contábeis
- __Campos\-Chave__: 02 – COD\_AGL
- __Ordenação__: Considerar informação do campo Ordem da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Balanço Patrimonial \(menu Manutenção\) para ordenar o registro no arquivo\.

Esta regra se aplica única e exclusivamente para geração das informações em Moeda Funcional, com exceção das regras dos campos 07 – VL\_CTA\_ULT\_DRE e 08 – IND\_VL\_ULT\_DRE, que foram incluídos a partir do layout 4\.00\. As informações já geradas no registro J150 se mantêm inalterada\.

Observar que, uma vez que o usuário faz a opção de gerar a Demonstração de Resultado em Moeda Funcional \(observar critérios indicados acima\), o relatório de conferência gerado no momento da geração do arquivo também deve refletir os valores em Moeda Funcional\.

*Informação adicional: a geração do registro pode ser realizada através do próprio Meio magnético gerado\. Para isso, seria necessário recuperar as informações dos registros de Saldos, I355\.*

  

MFS\-2632

MFS\-3700

MFS\-4878

RNJ150\-01

__Campo 01 – REG__

Será gerado com informação fixa “J150”\.

MFS\-4878

RNJ150\-02

__Campo 02 – COD\_AGL__

Será gerado com a informação do campo Código de Aglutinação da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Demonstração de Resultado \(menu Manutenção\)\.

MFS\-4878

RNJ150\-03

__Campo 03 – NIVEL__

Será gerado com a informação do campo Nível da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Demonstração de Resultado \(menu Manutenção\)\.

MFS\-4878

RNJ150\-04

__Campo 04 – DESCR\_COD\_AGL__

Será gerado com a informação do campo Descrição da tela de Códigos de Aglutinação \(B\. Patrimonial / D\. Resultado / DLPA / DMPL\) / aba Demonstração de Resultado \(menu Manutenção\)\.

MFS\-4878

RNJ150\-05

__Campo 05 – VL\_CTA __

Para geração deste campo considerando valores em Moeda Funcional, devemos considerar a soma do valor do Saldo Auxiliar \(campo 06 \- VL\_CTA\_AUX\) do Registro I355 que tenha o registro pai I350 com data \(campo 02 \- DT\_RES\) do Mês informado na Data Final do registro pai do J150, o J005 \(campo 03 \- DT\_FIN\), sumarizando o valor por conta contábil ou conta \+ centro de custo \(conforme parametrizado na tela “Selecionar Contas da Empresa para Apuração”\) ou então, considerar a informação do campo Valor do Lançamento Contábil \(campo 07 – VLR\_LANCTO da SAFX225\) dos Lançamentos de Encerramento cuja Data da Operação \(campo 03 – DATA\_OPERACAO\) seja do Mês informado na Data Final do registro pai do J150, o J005 \(campo 03 \- DT\_FIN\), mantendo as mesmas regras de agrupamento \(considerar avaliação técnica para definição da melhor origem\)\.

Exemplo: Se o J005 tem o campo 03 \- DT\_FIN informado com 31/12/2016, devemos considerar o saldo do I355 filho do I350 com o campo 02 \- DT\_RES com data de 31/12/2016\.

Nesta sumarização devemos considerar também o Indicador da Situação do Valor \(campo 07 \- IND\_DC\_AUX do I355 ou campo 05 – IND\_DEB\_CRE da SAFX226\), de modo que podemos consolidar considerando o seguinte cálculo:

Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo Indicador de Débito/Crédito seja igual a “D” __menos__ Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo Indicador de Débito/Crédito seja igual a “C”\. 

Deve ser demonstrado sempre o resultado positivo\.

O cálculo acima indicado se aplica aos códigos de aglutinação com Classificação igual a “Receita/Despesa” que tem as contas contábeis ou contas \+ centros de custo associadas\. Para os códigos de aglutinação com Classificação igual a “Subtotalizador/Totalizador”, será aplicado o mesmo cálculo, porém, podemos considerar o valor das contas contábeis ou contas \+ centros de custo associadas aos códigos de aglutinação que foram vinculados ao código Totalizador\.

MFS\-4878

RNJ150\-06

__Campo 06 – IND\_VL__

Este campo é gerado em função do cálculo realizado no campo 05 – VL\_CTA\. Devemos aplicar a seguinte regra:

Se o código de aglutinação for do tipo “Receita/Despesa” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “R”\. Se for zero ou positivo, gerar “D”\.

Se o código de aglutinação for do tipo “Subtotalizador/Totalizador” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “P”\. Se for zero ou positivo, gerar “N”\.

Se for considerada como origem as informações da SAFX225, deve ser aplica a seguinte regra:

Se o código de aglutinação for do tipo “Receita/Despesa” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “D”\. Se for zero ou positivo, gerar “R”\.

Se o código de aglutinação for do tipo “Subtotalizador/Totalizador” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “N”\. Se for zero ou positivo, gerar “P”\.

Esta diferenciação se dá porque, no momento em que geramos o registro I355 fazemos a inversão do Indicador de Débito/Crédito\. Como estamos considerando na regra o Valor do Lançamento de Encerramento direto com seu indicador, esta inversão fará com que os valores da DRE reflitam o demonstrado no registro I355\.

MFS\-4878

RNJ150\-07

__Campo 07 – VL\_CTA\_ULT\_DRE__

Para geração deste campo considerando valores em Moeda Funcional, devemos considerar a soma do valor do Saldo Auxiliar \(campo 06 \- VL\_CTA\_AUX\) do Registro I355 que tenha o registro pai I350 com data \(campo 02 \- DT\_RES\) do Mês imediatamente anterior ao informado na Data Inicial do registro pai do J150, o J005 \(campo 02 \- DT\_INI\), sumarizando o valor por conta contábil ou conta \+ centro de custo \(conforme parametrizado na tela “Selecionar Contas da Empresa para Apuração”\) ou então, considerar a informação do campo Valor do Lançamento Contábil \(campo 07 – VLR\_LANCTO da SAFX225\) dos Lançamentos de Encerramento cuja Data da Operação \(campo 03 – DATA\_OPERACAO\) seja do Mês imediatamente anterior ao informado na Data Inicial do registro pai do J150, o J005 \(campo 02 \- DT\_INI\), mantendo as mesmas regras de agrupamento \(considerar avaliação técnica para definição da melhor origem\)\.

Exemplo: Se o J005 tem o campo 02 \- DT\_INI informado com 01/01/2016, devemos considerar o saldo do I355 filho do I350 com o campo 02 \- DT\_RES com data de 31/12/2015\.

Nesta sumarização devemos considerar também o Indicador da Situação do Valor \(campo 07 \- IND\_DC\_AUX do I355 ou campo 05 – IND\_DEB\_CRE da SAFX226\), de modo que podemos consolidar considerando o seguinte cálculo:

Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo Indicador de Débito/Crédito seja igual a “D” __menos__ Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo Indicador de Débito/Crédito seja igual a “C”\. 

Deve ser demonstrado sempre o resultado positivo\.

O cálculo acima indicado se aplica aos códigos de aglutinação com Classificação igual a “Receita/Despesa” que tem as contas contábeis ou contas \+ centros de custo associadas\. Para os códigos de aglutinação com Classificação igual a “Subtotalizador/Totalizador”, será aplicado o mesmo cálculo, porém, podemos considerar o valor das contas contábeis ou contas \+ centros de custo associadas aos códigos de aglutinação que foram vinculados ao código Totalizador\.

Para geração deste campo, sem considerar Moeda Funcional, devemos considerar a soma do valor do Saldo \(campo 04 \- VL\_CTA\) do Registro I355 que tenha o registro pai I350 com data \(campo 02 \- DT\_RES\) do Mês imediatamente anterior ao informado na Data Inicial do registro pai do J150, o J005 \(campo 02 \- DT\_INI\), sumarizando o valor por conta contábil ou conta \+ centro de custo \(conforme parametrizado na tela “Selecionar Contas da Empresa para Apuração”\)\.

Exemplo: Se o J005 tem o campo 02 \- DT\_INI informado com 01/01/2016, devemos considerar o saldo do I355 filho do I350 com o campo 02 \- DT\_RES com data de 31/12/2015\.

Nesta sumarização devemos considerar também o Indicador da Situação do Saldo Final \(campo 05 \- IND\_DC\), de modo que podemos consolidar considerando o seguinte cálculo:

Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo campo 05 \- IND\_DC seja igual a “D” __menos__ Total dos Saldos das Contas ou Contas \+ Centros de Custo parametrizados cujo campo 05 \- IND\_DC seja igual a “C”\. 

Deve ser demonstrado sempre o resultado positivo\.

O cálculo acima indicado se aplica aos códigos de aglutinação com Classificação igual a “Receita/Despesa” que tem as contas contábeis ou contas \+ centros de custo associadas\. Para os códigos de aglutinação com Classificação igual a “Subtotalizador/Totalizador”, será aplicado o mesmo cálculo, porém, podemos considerar o valor das contas contábeis ou contas \+ centros de custo associadas aos códigos de aglutinação que foram vinculados ao código Totalizador\.

Observar que este campo também deve ser incluído no relatório de conferência gerado no momento da geração do meio magnético\.

MFS\-2473

MFS\-4878

RNJ150\-08

__Campo 08 – IND\_VL\_ULT\_DRE__

Este campo é gerado em função do cálculo realizado no campo 07 – VL\_CTA\_ULT\_DRE\. Devemos aplicar a seguinte regra:

Se o código de aglutinação for do tipo “Receita/Despesa” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “R”\. Se for zero ou positivo, gerar “D”\.

Se o código de aglutinação for do tipo “Subtotalizador/Totalizador” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “P”\. Se for zero ou positivo, gerar “N”\.

Para Moeda Funcional, se for considerada como origem as informações da SAFX225, deve ser aplica a seguinte regra:

Se o código de aglutinação for do tipo “Receita/Despesa” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “D”\. Se for zero ou positivo, gerar “R”\.

Se o código de aglutinação for do tipo “Subtotalizador/Totalizador” e o resultado obtido no cálculo for negativo, devemos gerar neste campo o conteúdo “N”\. Se for zero ou positivo, gerar “P”\.

Esta diferenciação se dá porque, no momento em que geramos o registro I355 fazemos a inversão do Indicador de Débito/Crédito\. Como estamos considerando na regra o Valor do Lançamento de Encerramento direto com seu indicador, esta inversão fará com que os valores da DRE reflitam o demonstrado no registro I355\.

Observar que este campo também deve ser incluído no relatório de conferência gerado no momento da geração do meio magnético\.

MFS\-2473

MFS\-4878

__Definições Registro I500 para Livro Razão Auxiliar das Subcontas__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI500\-00

__Registro I500 – Parâmetros de Impressão e Visualização do Livro Razão Auxiliar com Leiaute Parametrizável__

O Registro I500 tem como finalidade especificar o tamanho da fonte a ser utilizado na impressão do livro “Z”, que é um livro auxiliar com formatação especificada pelo próprio usuário\. Hoje nós temos a geração deste livro de forma customizada por nossos parceiros \(canais\) e apenas importamos um arquivo txt através do item “Livro Razão Auxiliar” do menu Manutenção / módulo ECD e geramos no meio magnético, complementando informações básicas do arquivo\.

A RFB criou um Livro Razão com Layout fixo para demonstração das informações contábeis de Subcontas Correlatas\. Para atender a esta nova solicitação da RFB, criamos a tabela SAFX179 – Razão Auxiliar das Subcontas, onde nossos clientes poderão importar as informações deste livro razão para manter o histórico e futuramente implementaremos processos para geração e validação dos dados desta tabela\.

A finalidade desta atualização é prover a geração dos registros do Livro Razão Auxiliar das Subcontas importado pelo usuário para a SAFX179\.

O livro razão é composto de 4 registros, que são:

- Registro I500: Parâmetros de Impressão e Visualização do Livro Razão Auxiliar com Leiaute Parametrizável;
- Registro I510: Definição de Campos do Livro Razão Auxiliar com Leiaute Parametrizável;
- Registro I550: Detalhes do Livro Razão Auxiliar com Leiaute Parametrizável;
- Registro I555: Totais no Livro Razão Auxiliar com Leiaute Parametrizável;

__IMPORTANTE__: geração do Livro Razão das Subcontas não mudará em nada a geração de outros registros selecionados para o Perfil indicado na geração\. Ele impacta apenas na geração dos registros acima citados, que passam a ser gerados com regra específica definida neste documento\.

__Como regra geral de geração do o Livro Razão Auxiliar das Subcontas teremos:__

- A versão do "Leiaute” parametrizada na tela de geração for a “4\.00” ou superior”; __E__
- Quando o “Tipo de Livro” indicado na tela de geração for igual a “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555\)”; __E__
- Quando o código do “Livro Auxiliar” selecionado na tela de geração estiver indicado na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” \(menu Parâmetros / módulo ECD\); __E__
- Quando o estabelecimento selecionado \(centralizado \+ centralizadores ou apenas o descentralizado\) tiver ao menos um registro na SAFX179 com o mesmo código de estabelecimento e com Data do Lançamento Contábil no mesmo período de geração e com o mesmo código de “Livro Auxiliar” indicado\.

Nesta regra, trataremos a geração do Registro I500, visando atender ao formato do livro carregado para a SAFX179\.

O Registro I500 é de Nível Hierárquico – 3, Ocorrência de um \(por arquivo\)\. Para o Livro Razão Auxiliar das Subcontas ele será gerado com a seguinte estrutura:

__01 \- REG__

__02 \- TAM\_FONTE__

I500

4

  

MFS\-2926

__Definições Registro I510 para Livro Razão Auxiliar das Subcontas__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI510\-00

__Registro I510 – Definição de Campos do Livro Razão Auxiliar com Leiaute Parametrizável__

O Registro I510 tem como finalidade especificar os campos que serão utilizados no livro “Z” \(Livro Razão Auxiliar com Leiaute Parametrizável\)\.

Para o Livro Razão Auxiliar das Subcontas, temos as regras básicas de geração definidas na “RNI500\-00”\.

O Registro I510 é de Nível Hierárquico – 3, Ocorrência de vários \(por arquivo\)\. Neste contexto, este registro será gerado com o conteúdo padrão definido pela RFB, que é:

__01 \- REG__

__02 \- NM\_CAMPO__

__03 \- DESC\_CAMPO__

__04 \- TIPO\_CAMPO__

__05 \- TAM\_CAMPO__

__06 \- DEC\_CAMPO__

__07 \- COL\_CAMPO__

I510

NAT\_SUB\_CNT

NATUREZA DA SUBCONTA CORRELATA

C

2

 

11

I510

COD\_SUB\_CNT

CÓDIGO DA SUBCONTA VINCULADA AO ITEM

C

20

 

11

I510

COD\_CCUS

CÓDIGO DO CENTRO DE CUSTOS VINCULADO AO ITEM

C

20

 

11

I510

CNPJ\_INVTD

CNPJ DA INVESTIDA

N

14

 

11

I510

COD\_PATR\_ITEM

CÓDIGO DE IDENTIFICAÇÃO DO ITEM

C

10

 

11

I510

QTD

QUANTIDADE

N

15

0

11

I510

IDENT\_ITEM

IDENTIFICADOR DO ITEM

C

30

 

11

I510

DESCR\_ITEM

DESCRICAO DO ITEM

C

50

 

11

I510

DATA\_RECT\_INI

DATA DO RECONHECIMENTO CONTÁBIL INICIAL DO ITEM

C

8

 

11

I510

SLD\_ITEM\_INI

SALDO INICIAL DA CONTA CONTÁBIL

N

19

2

11

I510

IND\_SLD\_ITEM\_INI

INDICADOR DO SALDO INICIAL

C

1

 

11

I510

REAL\_ITEM

PARCELA DE REALIZAÇÃO DO ITEM

N

19

2

11

I510

IND\_REAL\_ITEM

INDICADOR DA PARCELA DE REALIZAÇÃO

C

1

 

11

I510

SLD\_ITEM\_FIN

SALDO FINAL DA CONTA CONTÁBIL QUE REGISTRA O ITEM

N

19

2

11

I510

IND\_SLD\_ITEM\_INI

INDICADOR DO SALDO FINAL

C

1

 

11

I510

SLD\_SCNT\_INI

SALDO INICIAL DA SUBCONTA REPRESENTATIVA DO ITEM

N

19

2

11

I510

IND\_SLD\_SCNT\_INI

INDICADOR DO SALDO INICIAL

C

1

 

11

I510

DEB\_SCNT

VALOR REGISTRADO A DEBITO NA SUBCONTA

N

19

2

11

I510

CRED\_SCNT

VALOR REGISTRADO A CREDITO NA SUBCONTA

N

19

2

11

I510

SLD\_SCNT\_FIN

SALDO FINAL DA SUBCONTA REPRESENTATIVA DO ITEM

N

19

2

11

I510

IND\_SLD\_SCNT\_FIN

INDICADOR DO SALDO FINAL

C

1

 

11

I510

DATA\_LCTO

DATA DO LANÇAMENTO CONTÁBIL

C

8

 

11

I510

NR\_LCTO

IDENTIFICAÇÃO DO LANÇAMENTO

C

20

 

11

I510

VLR\_LCTO

VALOR DO LANÇAMENTO

N

19

2

11

I510

IND\_VLR\_LCTO

INDICADOR DO VALOR DO LANÇAMENTO

C

1

 

11

I510

IND\_ADOC\_INI

INDICADOR DA ADOÇÃOO INICIAL

C

1

 

11

  

MFS\-2926

__Definições Registro I550 para Livro Razão Auxiliar das Subcontas__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI550\-00

__Registro I550 – Detalhes do Livro Razão Auxiliar com Leiaute Parametrizável__

O Registro I550 informa os detalhes do Livro Razão\. No contexto do Livro Razão Auxiliar das Subcontas, devemos respeitar as regras básicas de geração definidas na “RNI500\-00” e demonstrar no I550 o que foi carregado na SAFX179\.

\[MFS\-4640\] Para formatação dos campos deste registro e seu filho \(I555\) deve ser levado em conta o parametrizado nos campos 04 \- TIPO\_CAMPO, 05 \- TAM\_CAMPO e 06 \- DEC\_CAMPO do registro I510\. Se o campo for numérico, levar em conta a quantidade de decimais que é exigida para demonstração, arredondando o valor a ser apresentado, se for necessário\.

O Registro I550 é de Nível Hierárquico – 3, Ocorrência de vários \(por arquivo\)\. Neste contexto, este registro será gerado com a estrutura padrão definida pela RFB, que é:

__Campo__

__Nome do Campo__

__Origem SAFX179__

01

REG

Texto fixo "I550"

02

NAT\_SUB\_CNT

Campo 004 \- Natureza da Subconta Correlata

03

COD\_SUB\_CNT

Campo 005 \- Código da Subconta

*Obs: Este código deve ter seu cadastro apresentado no registro I050\.*

04

COD\_CCUS

Campo 006 \- Código do Centro de Custos

*Obs: Este código deve ter seu cadastro apresentado no registro I100\.*

05

CNPJ\_INVTD

Campo 007 \- CNPJ da Empresa Investida

06

COD\_PATR\_ITEM

Campo 008 \- Código do Item \(ativo/passivo\)

07

QTD

Campo 009 \- Quantidade Inicial do Item

08

IDENT\_ITEM

Campo 010 \- Código Individualizado do Bem

09

DESCR\_ITEM

Campo 011 \- Descrição Resumida do Item

10

DATA\_RECT\_INI

Campo 012 \- Data do Reconhecimento Contábil do Item

11

SLD\_ITEM\_INI

Campo 013 \- Saldo Inicial da Conta que Registrada o Item

12

IND\_SLD\_ITEM\_INI

Campo 014 \- Indicador do Saldo Inicial

13

REAL\_ITEM

Campo 015 \- Realização do Item

14

IND\_REAL\_ITEM

Campo 016 \- Indicador da Realização do Item

15

SLD\_ITEM\_FIN

Campo 017 \- Saldo Final da Conta que Registra o Item

16

IND\_SLD\_ITEM\_INI

Campo 018 \- Indicador do Saldo Final

17

SLD\_SCNT\_INI

Campo 019 \- Saldo Inicial na Subconta Antes do Lançamento Contábil

18

IND\_SLD\_SCNT\_INI

Campo 020 \- Indicador do Saldo Inicial

19

DEB\_SCNT

Campo 021 \- Valor Registrado a Débito na Subconta 

20

CRED\_SCNT

Campo 022 \- Valor Registrado a Crédito na Subconta 

21

SLD\_SCNT\_FIN

Campo 023 \- Saldo Final na Subconta após o Lançamento Contábil\.

22

IND\_SLD\_SCNT\_FIN

Campo 024 \- Indicador do Saldo Final

23

DATA\_LCTO

Campo 025 \- Data do Lançamento Contábil

24

NR\_LCTO

Campo 026 \- Número do Lançamento

25

VLR\_LCTO

Campo 027 \- Valor do Lançamento Contábil

26

IND\_VLR\_LCTO

Campo 028 \- Indicador do Lançamento

27

IND\_ADOC\_INI

Campo 029 \- Indicador de Registro Relativo a Adoção Inicial

__\[ALTERAÇÃO CH17104\_2016\]__

O registro I550 é pai do I555\. Nele estará o detalhe e no I555 uma consolidação, conforme critérios definidos pelo usuário na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” \(menu Parâmetros / módulo ECD\)\. Para correta demonstração da informação o registro I550 deverá ser __ordenado__ pelos campos definidos pelo usuário na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” no item “Tratamento a ser aplicado” como “Agrupador” e pelos campos 23 \- Data do Lançamento Contábil e 24 \- Número do Lançamento por ordem crescente do menor para o maior, para que seja possível demonstrar a cada quebra de critério de agrupamento definido o registro filho I555\.

  

MFS\-2926

CH17104\_2016

__Definições Registro I555 para Livro Razão Auxiliar das Subcontas__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI555\-00

__Registro I555 – Totais no Livro Razão Auxiliar com Leiaute Parametrizável__

O Registro I555 informa os totais dos detalhes demonstrados no I550\. Ele é um registro filho do I550 e será gerado com a mesma estrutura do registro pai \(mesmos campos\), porém, obedecendo as regras definidas na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” \(menu Parâmetros / módulo ECD\), no item “Tratamento a ser aplicado”\.

Considerando as opções disponíveis no item “Tratamento a ser aplicado”, teremos as seguintes regras:

- __Agrupador__: indica se o campo será considerado como agrupador do registro\.
- __Não demonstrar conteúdo__: quando selecionada esta opção, a geração do campo no registro I555 não será demonstrado nenhum conteúdo\. Se não for selecionado nenhum tipo de tratamento para determinado campo, considerar a regra de “Não demonstrar conteúdo”;
- __Sumarizar__: quando selecionada esta opção, será realizada a somatória do valor do campo ao qual o tratamento foi atribuído, considerando os critérios de agrupamento definidos\. Os campos que são acompanhados do Indicador de Débito/Crédito \(013 \- Saldo Inicial da Conta que Registrada o Item, 015 \- Realização do Item, 017 \- Saldo Final da Conta que Registra o Item, 019 \- Saldo Inicial na Subconta Antes do Lançamento Contábil, 023 \- Saldo Final na Subconta após o Lançamento Contábil e 027 \- Valor do Lançamento Contábil\), se tiverem esta opção selecionada, deverão considerar o Indicador do registro para realização da sumarização, calculando a Somatória do Valor a Débito __menos__ a Somatória do Valor a Crédito e demonstrando sempre o valor positivo\. O Indicador de Débito/Crédito sempre deverá ser demonstrado para estes campos e deverá considerar o resultado obtido no cálculo para sua demonstração: se resultado do cálculo for positivo, demonstrará “D”; se negativo, “C”\.
- __Considerar primeiro valor do período__: quando selecionada esta opção, será considerado o valor do registro com Data de Lançamento Contábil menor do período e Número de Lançamento Contábil menor, dentro da menor Data \(quando a data se repetir\), considerando os critérios de agrupamento definidos\. Os campos que são acompanhados do Indicador de Débito/Crédito \(013 \- Saldo Inicial da Conta que Registrada o Item, 015 \- Realização do Item, 017 \- Saldo Final da Conta que Registra o Item, 019 \- Saldo Inicial na Subconta Antes do Lançamento Contábil, 023 \- Saldo Final na Subconta após o Lançamento Contábil e 027 \- Valor do Lançamento Contábil\), se tiverem esta opção selecionada, deverão considerar o Indicador do registro na demonstração da informação, apresentando no campo apropriado o indicador do registro cujo valor foi considerado\.
- __Considerar último valor do período__: quando selecionada esta opção, será considerado o valor do registro com Data de Lançamento Contábil maior do período e Número de Lançamento Contábil maior, dentro da maior Data \(quando a data se repetir\), considerando os critérios de agrupamento definidos\. Os campos que são acompanhados do Indicador de Débito/Crédito \(013 \- Saldo Inicial da Conta que Registrada o Item, 015 \- Realização do Item, 017 \- Saldo Final da Conta que Registra o Item, 019 \- Saldo Inicial na Subconta Antes do Lançamento Contábil, 023 \- Saldo Final na Subconta após o Lançamento Contábil e 027 \- Valor do Lançamento Contábil\), se tiverem esta opção selecionada, deverão considerar o Indicador do registro na demonstração da informação, apresentando no campo apropriado o indicador do registro cujo valor foi considerado\.

Como este registro é filho do I550, será gerado sempre que seu pai atingir um nível que agrupamento que atenda aos critérios de demonstração parametrizados para geração deste registro\. Vide exemplo:

   

MFS\-2926

__Alterações Registro J900__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ900\-05

__Registro J900 – Campo 05 – NOME__

__\[ALTERADA \- CH15903\_2016\]__

Este campo deve ser preenchido com o conteúdo do campo RAZAO\_SOCIAL ou do campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO\.

__Tratamento:__

- Se o campo RAZAO\_SOCIAL\_COMPL da tabela ESTABELECIMENTO estiver preenchido, considerar o conteúdo dele na geração do campo desconsiderando o conteúdo do campo RAZAO\_SOCIAL, caso não esteja preenchido, buscar o conteúdo do campo RAZAO\_SOCIAL normalmente\.

__Observação:__ No campo RAZAO\_SOCIAL\_COMPL o usuário pode informar a razão social dos estabelecimentos que tenham mais do que 100 posições \(tamanho do campo “Razão Social” original do Mastersaf\)\. Esta informação será utilizada apenas quando preenchida, nas obrigações fiscais que permitam mais que 100 caracteres no preenchimento desta informação\.

CH15903\_2016

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

