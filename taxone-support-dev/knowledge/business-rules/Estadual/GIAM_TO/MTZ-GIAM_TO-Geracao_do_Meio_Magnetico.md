# MTZ-GIAM_TO-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-GIAM_TO-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-01-08
- **Tamanho:** 101 KB

---

#  GIAM TO \- Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2447__

GIAM TO \- Geração do Meio Magnético

Este documento de requisito tem por objetivo realizar a geração do meio magnético GIAM\-TO além de permitir as parametrizações necessárias no módulo\.

__OS3091__

GIAM\-TO \- Atualizacao para a versao 9\.2

Este documento de requisito tem por objetivo realizar as alterações necessárias referente a atualização da GIAM TO para a versão 9\.2\.

__CH81269__

Atualização para a versão 9\.3

Alterados os registros A33, B9, C7, C12 e D10 para o layout da versão 9\.3\.0

__CH99437__

Atualização para a versão 9\.4

Alterados os registros A33 para o layout da versão 9\.4\.0

__CH102650__

Alterada a regra do campo Data de Vencimento do parâmetro Icms a Recolher

Alterada a regra do campo Data de Vencimento do parâmetro Icms a Recolher

__OS3544__

Atualização para a versão 9\.5

Alterados os registros A33, N5, N6, N7, N8, O5, O6, O7, O8 para o layout da versão 9\.3\.0

__CH4518\_2012__

Corrigir a geração da GIAM TO pois o __Segmento N__

 não consolida NF com item e sem item e __Segmento O__ está  trazendo apenas notas canceladas\.

Corrigir a geração da GIAM TO  n e __Segmento O__ está  trazendo apenas notas canceladas\.

__OS3758__

Atualização para a versão 9\.6

Atualização para a versão 9\.6

__CH8820\_2012__

Correção na geração centralizada \- Inclusão de CFOP para tratamento de Não Contribuinte

Correção na geração centralizada \- Inclusão de CFOP para tratamento de Não Contribuinte

__CH6481\_2014__

Ajuste na geração do Segmento M – campo M5

Este documento tem como objetivo alterar a geração do campo M5 – Município de Origem para documentos fiscais com operações interestaduais\.

__MFS6415__

Alterações da Portaria n\. 748, de 17/08/2016\.

Atualização p/a nova vrs 10\.0, conforme alterações da Portaria Sefaz TO n\. 748/2016 

__MFS10301__

Erro de geração campo A14 \- N° CRC contabilista\.

Correção da geração do campo A14 \- N° CRC contabilista\.

__CH14704\_2017 \(MFS\-12589\)__

Ajuste no preenchimento do campo S6\-Código da UF do Segmento S

Este documento tem como objetivo alterar o preenchimento do campo “S6\-Código da UF” do Segmento S \- Especificação do Diferencial de Alíquotas Consumidor Final \(Saídas\) por UF, para considerar o código da UF da Tabela de Alíquotas para UF\.

__CH11196\_2018 \(MFS\-18435\)__

Ajuste na geração do Segmento M – campo M5

Este documento tem como objetivo alterar a geração do campo M5 – Município de Origem para documentos fiscais com operações interestaduais\.

__MFS30712__

Ajuste na geração do Segmento M – campo M5

Este documento tem como objetivo alterar a geração do campo M5 – Município de Origem 

__MFS31278__

Ajuste na geração do Segmento B – Campo B10

Este documento tem como objetivo alterar a geração do campo B10\-Substituição Tributária

__MFS31469__

Ajuste na geração do Segmento D – Campo D11

Este documento tem como objetivo alterar a geração do campo D11\-Substituição Tributária

__MFS31566__

Ajuste na geração do Segmento B e D

Este documento tem como objetivo alterar a geração dos campos B9\-Outras e D10\-Outras

__MFS31589__

Ajuste na geração do Segmento M – campo M5

Este documento tem como objetivo alterar a geração do campo M5 – Município de Origem

__MFS59925__

Ajuste na geração do Segmento B – Notas Fiscais de Serviço\.

Este documento tem como objetivo de Incluir na Tela – Parâmetros p/ Dados Acessórios, a opção “Considerar Notas de Serviço com CFOP’s do Ajuste SINIEF 03/04” __\(RN15\)__, e readequar a regra para considerar as Notas Fiscais de Serviço no Segmento B __\(RGB\-01\)\.__

__MFS63174__

Andréa Rocha

Inclusão de parâmetro para indicar a forma de preencher o campo Número da Nota do Segmento O\.

__MFS574911__

Andréa Rocha

Alteração da regra de preenchimento do campo Município do Segmento N\.

__MFS910409__

Andréa Rocha

Inclusão de um parâmetro para definir o preenchimento da coluna "Outras" do segmento B\.

__MFS1015800__

Lyene Benvenutti

Inclusão de um parâmetro para definir o preenchimento da coluna "Outras" do segmento D\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

O novo módulo “GIAM TO” deve ficar localizado no grupo “Estadual” abaixo do módulo “GIAM RO”\.

__OS2447__

__RN02__

Se o estabelecimento selecionado no Manager não pertencer ao estado do Tocantins \(UF = “TO”\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao estado do Tocantins\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Serão exibidos os botões “Sim” e “Não” \(default\)\. Se o usuário clicar no botão “Sim”, o módulo será aberto normalmente, senão o módulo será fechado\.

__OS2447__

__RN03__

Deverão ser criados os seguintes menus e sub\-menus no módulo GIAM TO:

- Arquivo
	- Salvar Como
	- Visualizar Relatórios
	- Configura Impressão
	- Sair
- Parâmetros
	- Dados Iniciais
	- Parâmetros p/ Dados Acessórios
	- Aquisição com Diferimento do ICMS
		- Por CFOP/Natureza de Operação
	- Parâmetros p/ Segmento M
		- Por CFOP
- Obrigações
	- Dados Mensais da Declaração
	- Diferencial de Alíquota
		- Geração
		- Manutenção
	- ICMS a Recolher
	- Geração do Meio Magnético
- Janela
- Ajuda

__OS2447__

__RN04__

Deverá ser implementado um relatório de conferência para as telas do menu Parâmetros e para as telas de manutenção do menu Obrigações\. O relatório deve conter todos os campos da tela\.

__OS2447__

__RN05__

As telas do menu Parâmetros e Obrigações devem ter as seguintes funcionalidades: Incluir, Abrir, Alterar, Excluir, Relatório e Sair\.

__OS2447__

__RN06__

O campo “Estabelecimento” deverá exibir o estabelecimento selecionado no Manager desde que o mesmo seja do Tocantins\. O campo deverá ficar desabilitado não permitindo que o mesmo seja alterado\.

__OS2447__

__RN07__

Caso não esteja selecionado nenhum estabelecimento, o sistema deve permitir que o usuário selecione no campo o estabelecimento desejado\.

Devem ser exibidos os estabelecimentos que atenderem as seguintes premissas:

- Que estejam licenciados\.
- Que o usuário possua direito de acesso na ferramenta PowerLock\.
- Que pertença ao estado do Tocantins\.

__OS2447__

__RN08__

O campo “Portador de TARE” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores:

“S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__OS2447__

__RN09__

O campo “Nº\. do TARE” deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Portador de TARE” esteja marcado\. O campo deve ser alfanumérico de 20 \(vinte\) posições\.

__OS2447__

__RN10__

O campo “Vencimento do TARE” deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Portador de TARE” esteja marcado\. O campo deve ser do tipo data no formato dd/mm/aaaa\.

__OS2447__

__RN11__

O campo “Tipo de Escrituração” deve ser exibido através de uma listbox e deve exibir em uma lista as opções “Fiscal” e “Contábil”\. Assumir os valores: “F” para a opção “Fiscal” e “C” para a opção “Contábil”\. Por default a opção exibida é “Fiscal”\.

__OS2447__

__RN12__

O campo “Usuário de ECF” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores:

“S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido marcado\.

__OS2447__

__RN13__

O campo “Declarante” deve exibir a pastinha amarela, onde o usuário poderá realizar uma pesquisa para selecionar o declarante responsável\. Recuperar os campos COD\_RESPONSAVEL e NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO\. O campo NOM\_RESPONSAVEL deve ficar desabilitado\.

Utilizar os campos da tabela RESP\_INFORMACAO como filtro da janela de seleção\.

Por default o campo é exibido “em branco”\.

__OS2447__

__RN14__

O campo “Contabilista” deve exibir a pastinha amarela, onde o usuário poderá realizar o filtro de pesquisa para selecionar a informação desejada\. Recuperar os campos COD\_RESPONSAVEL e NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO quando o campo IND\_CATEGORIA for igual a 2, 4 ou 6\. O campo NOM\_RESPONSAVEL deve ficar desabilitado\.

Utilizar os campos da tabela RESP\_INFORMACAO como filtro da janela de seleção\.

Por default o campo é exibido “em branco”\.

__OS2447__

__RN15__

\[ALTERADA \- MFS59925\] Inclusão da opção “Considerar Nota Fiscal de Serviço \(IND\_CONSID\_NF\_SERV\)”

O menu Parâmetros – Parâmetros p/ Dados Acessórios deve chamar a janela genérica utilizada nas demais GIAS, quando temos a geração dos dados acessórios chamada dentro da geração do meio magnético\. A tela deve conter apenas as opções “ICMS Retido/Outras”, “Modelo CIAP”, “Resumo por UF/CFOP” e “Operações c/ Contribuintes Finais” e “Considerar Notas de Serviço com CFOP’s do Ajuste SINIEF 03/04”\. 

__Obs\*__Aproveitar a regra do parâmetro “P\_IND\_CONSID\_NF\_SERV”

__OS2447__

__MFS59925__

__RN16__

A tela Parâmetros – Parâmetros p/ Dados Acessórios deverá armazenar as informações parametrizadas na tabela EST\_PAR\_DADOS\_ACS\.

__OS2447__

__RN17__

O menu Parâmetros – Aquisição com Diferimento do ICMS – por CFOP/Natureza de Operação deve chamar a janela genérica utilizada nas demais GIAS, para a tabela PRT\_EXTCFO\_MSAF\. Utilizar as mesmas regras de tela\.

__OS2447__

__RN18__

O campo “Grupo“ deve exibir o grupo escolhido pelo usuário na tela de Estabelecimento/Grupo/Validade exibida na abertura da tela\. Esse campo deve ser exibido desabilitado\.

__OS2447__

__RN19__

O campo “Tipo” deve exibir a opção “422 – Diferimento do ICMS”\.

__OS2447__

__RN20__

O campo “Extensão CFOP” deve exibir apenas CFOPs/Naturezas de Operação de entrada, ou seja, começados por 1, 2 ou 3\.

__OS2447__

__RN21__

O campo “Período” deve ser informado no formato mm/aaaa\.

__OS2447__

__RN22__

O campo “Saldo Inicial de Caixa” deve vir em branco no formato numérico com 14 \(quatorze\) posições, sendo a máscara 12v2\.

__OS2447__

__RN23__

O campo “Saldo Final de Caixa” deve vir em branco no formato numérico com 14 \(quatorze\) posições, sendo a máscara 12v2\.

__OS2447__

__RN24__

O campo “Houve Mudança de domicílio” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores:

“S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__OS2447__

__RN25__

O campo “Município Anterior” deve exibir a pastinha amarela, onde o usuário poderá selecionar os municípios do estado de Tocantins\. Recuperar os campos COD\_MUNICIPIO e DESCRICAO da tabela MUNICIPIO para o estado de Tocantins\.

O campo DESCRICAO deve ser exibido desabilitado\.

O campo “Município Anterior” deve ser exibido desabilitado\. O mesmo só deve ficar habilitado quando o campo “Houve Mudança de domicílio” estiver marcado\.

__OS2447__

__RN26__

O campo “Data Inicial”, referente ao município anterior, deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Houve Mudança de domicílio” estiver marcado\. O campo deve ser do tipo data no formato dd/mm/aaaa\. Quando o campo estiver habilitado, o mesmo deve ser de preenchimento obrigatório\. Se o campo não estiver preenchido, exibir a seguinte mensagem: “Preencher a data inicial do município anterior”\.

__OS2447__

__RN27__

O campo “Data Final”, referente ao município anterior, deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Houve Mudança de domicílio” estiver marcado\. O campo deve ser do tipo data no formato dd/mm/aaaa\. Quando o campo estiver habilitado, o mesmo deve ser de preenchimento obrigatório\. Se o campo não estiver preenchido, exibir a seguinte mensagem: “Preencher a data final do município anterior”\.

__OS2447__

__RN28__

O campo “Município Atual” deve ser exibido desabilitado\. O campo deve ser preenchido com o município cadastrado no estabelecimento\. Recuperar os campos COD\_MUNICIPIO e DESCRICAO da tabela MUNICIPIO referente ao COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

O campo “Município Atual” só deve ser preenchido quando o campo “Houve Mudança de domicílio” estiver marcado, caso contrário o mesmo deve ficar em branco\.

__OS2447__

__RN29__

O campo “Data Inicial”, referente ao município atual, deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Houve Mudança de domicílio” estiver marcado\. O campo deve ser do tipo data no formato dd/mm/aaaa\. Quando o campo estiver habilitado, o mesmo deve ser de preenchimento obrigatório\. Se o campo não estiver preenchido, exibir a seguinte mensagem: “Preencher a data inicial do município atual”\.

__OS2447__

__RN30__

O campo “Data Final”, referente ao município atual, deve ser exibido desabilitado\. O mesmo só será habilitado caso o campo “Houve Mudança de domicílio” estiver marcado\. O campo deve ser do tipo data no formato dd/mm/aaaa\. Quando o campo estiver habilitado, o mesmo deve ser de preenchimento obrigatório\. Se o campo não estiver preenchido, exibir a seguinte mensagem: “Preencher a data final do município atual”\.

__OS2447__

__RN31__

Na geração do diferencial de alíquota, a geração deverá verificar se o campo “Houve Mudança de domicílio” está marcado\. Se o mesmo estiver marcado, o sistema emitirá a seguinte mensagem: 

“Houve mudança de domicílio dentro do período informado\. A geração será realizada para o período completo\. Informar manualmente o diferencial de alíquota por período do domicílio fiscal de acordo com Dados Mensais da Declaração “

__OS2447__

__RN32__

O campo “Mês/Ano” permitirá a digitação da data no formato mm/aaaa \(mês/ano\)\.

__OS2447__

__RN33__

O campo “Tipo Livro” deve exibir o texto fixo “108 – Registro de Apuracao do ICMS \- P9”\. 

__OS2447__

__RN34__

O campo “Excluir os registros de Diferencial de Alíquota por UF digitados” deve ser exibido desmarcado\. O campo deve assumir os seguintes valores: “Sim”, quando marcado e “Não”, quando desmarcado\. 

Quando o campo estiver marcado, deve\-se realizar a exclusão dos registros digitados na tela Obrigações – Diferencial de Alíquota, quando o campo IND\_DIG\_CALC da tabela EST\_TO\_DIF\_ALIQ\_UF for igual a 1\.

__OS2447__

__RN35__

Devem ser exibidos somente os estabelecimentos que atenderem as seguintes premissas:

- Que estejam licenciados;
- Que o usuário possua direito de acesso na ferramenta PowerLock;

Que pertença ao estado do Tocantins\.

__OS2447__

__RN36__

A geração deverá realizar os seguintes procedimentos:

- Realizar a limpeza dos registros da tabela EST\_TO\_DIF\_ALIQ\_UF que estiverem com o campo IND\_DIG\_CALC igual a 2 ou 3\.
- Realizar a limpeza dos registros da tabela EST\_TO\_DIF\_ALIQ\_UF que estiverem com o campo IND\_DIG\_CALC igual a 1, quando o campo “Excluir os registros de Diferencial de Alíquota por UF digitados” estiver marcado\.
- Realizar o cálculo de diferencial de alíquota do período através da tabela ICT\_DIF\_ALIQ\.

__OS2447__

__RN37__

O campo “Tipo Livro” deve ser exibido desabilitado\. O campo deve ser preenchido com os campos COD\_TIPO\_LIVRO e NOM\_OFICIAL da tabela TIPO\_LIVRO\_FISCAL para o COD\_TIPO\_LIVRO = 108\.

__OS2447__

__RN38__

O campo “Diferencial de Alíquota a recolher do período anterior” deve vir em branco no formato numérico com 14 posições, sendo a máscara 14v2\.

__OS2447__

__RN39__

O campo “Diferencial de Alíquota a recolher do período” deve ser exibido em branco no formato numérico com 14 posições, sendo a máscara 14v2\. Esse campo deve ler e gravar informações no campo VLR\_DIF\_ALIQ\_PER da tabela EST\_TO\_DIF\_ALIQ\.

__OS2447__

__RN40__

O campo “Diferencial de Alíquota a recolher do período” deve ser exibido desabilitado no formato numérico com 17 posições, sendo a máscara 15v2\. Este campo só deve ser preenchido com o valor do diferencial de alíquota do período for maior que R$ 50,00\. 

Esse campo deve realizar e exibir a soma entre o diferencial de alíquota do período anterior e o diferencial de alíquota do período\.

Diferencial de Alíquota a recolher = Diferencial de Alíquota período anterior \+ Diferencial de Alíquota a recolher

__OS2447__

__RN41__

O campo “UF” deve vir em branco no formato alfanumérico com 2 \(duas\) posições\. Esse campo deve exibir o COD\_ESTADO referente ao campo IDENT\_ESTADO da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN42__

O campo “Domicílio Fiscal” deve ser exibido através de um radiobutton\. O campo deve assumir os valores “A” – “Atual” e “B” – “Anterior”\. Por default, o campo deve assumir o valor: “A” – “Atual”\. Esse campo deve ler e gravar informações no campo IND\_DOMICILIO\_FISCAL da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN43__

O campo “Valor Contábil” deve ser exibido em branco no formato numérico com 14 posições, sendo a máscara 14v2\. Esse campo deve ler e gravar informações no campo VLR\_CONTABIL da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN44__

O campo “Base de Cálculo” deve ser exibido em branco no formato numérico com 14 posições, sendo a máscara 14v2\. Esse campo deve ler e gravar informações no campo VLR\_BASE da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN45__

O campo “Diferencial de Alíquota” deve ser exibido em branco no formato numérico com 14 posições, sendo a máscara 14v2\. Esse campo deve ler e gravar informações no campo VLR\_DIF\_ALIQ da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN46__

Quando as informações forem digitadas na tela Obrigações – Diferencial de Alíquota, o sistema deve gravar “1” no campo IND\_DIG\_CALC da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN47__

Quando houver informações geradas pelo livro e o usuário complementar com informações digitadas na tela Obrigações – Diferencial de Alíquota, o sistema deve gravar “3” no campo IND\_DIG\_CALC da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN48__

A tela Obrigações – Diferencial de Alíquota – Manutenção deve ser uma janela do tipo mestre\-detalhes\.

__OS2447__

__RN49__

O campo “__Tipo de ICMS__” deve ser exibido através de uma listbox e deve exibir em uma lista as opções “Normal”, “Diferencial de Alíquota” e “Substituição Tributária”\. O campo deve assumir os seguintes valores: “N” para a opção “Normal”, “D” para a opção “Diferencial de Alíquota” e “S” para “Substituição Tributária”\.

__\[ALTERADA – OS3758\]__

Inclusão da opção “__Complementação de Alíquota”\. __O campo deve assumir o valor “C”\.

Alteração da __MFS6415__:

Inclusão de duas novas opções, e alteração na descrição da opção do diferencial de alíquota, como segue:

      \- Normal

      \- Diferencial de Alíquota \(Entradas\)

      \- Substituição Tributária

      \- Complementação de Alíquota

      \- Diferencial de Alíquota \(Saídas\)

      \- Fundo Combate a Pobreza

As quatro primeiras opções continuam a assumir os valores N, D, S e C, e as novas opções, serão respectivamente F e P\.

__OS2447__

__OS3758__

__MFS6415__

__RN50__

O campo “Data de Vencimento” deve vir em branco e permitir a digitação no formato dd/mm/aaaa\. 

O campo “Data de Vencimento” deve ser preenchido com uma data até o dia 9 \(nove\) do mês seguinte ao da apuração, ou seja: ao preencher o campo “Período”, a regra do campo “Data de Vencimento” deverá ser alterada para aceitar o a data de início e final ao período de referência e também a data posterior ao período de referência, porém limitada ao dia 09 \(nove\) do mês seguinte\.

Exemplo: 

Icms a recolher

Estabelacimento: XXXX\-XX

Período: 05/2011

Tipo de ICMS: Normal

Data de Vencimento: 09/06/2011

Valor do Icms a Recolher: R$\. 100,00

Caso preenchido o campo “Data de Vencimento” diferente a regra acima, emitir a seguinte mensagem de alerta, porém deverá deixar gravar o registro:

“A data de vencimento incorreta para o período de referência informado”

__OS2447/__

__CH102650__

__RN51__

O campo “Valor do ICMS a Recolher” deve vir habilitado, em branco e no formato numérico com 14 \(quatorze\) posições, sendo a máscara 12v2\.

__OS2447__

__RN52__

A tela Obrigações – ICMS a Recolher deve ser uma janela do tipo multi\-registros\.

__OS2447__

__RN53__

O campo “__Versão__” deve ser exibido através de uma listbox\. O campo deve assumir o valor default “9\.4\.0”\.

Alteração __MFS6415__: \(atualização da versão 9\.6 para 10\.0\) 

O campo “Versão” passa a apresentar duas opções na lista: \[ 9\.0\.6 \] e \[ 10\.00 \]

__OS2447/__

__OS3091/__

__CH81269__

__CH99437__

__MFS6415__

__RN54__

O campo “Gerar Dados Acessórios” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores:

“S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido marcado\. 

Quando o campo for marcado, a package de geração deve chamar a geração dos dados acessórios através da procedure SAF\_EST\_RES\_CFO\_UF\.

Quando houver mudança de domicílio a procedure deverá ser chamada para os dois períodos de domicílio fiscal, o anterior e o atual\.

__OS2447__

__RN55__

O campo “Gerar os Valores da Apuração por Classe de Lançamento” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores:

“S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido marcado\. 

Quando o campo for marcado, a package de geração deve chamar a geração dos valores da apuração através da procedure SAF\_EST\_GIA\_INFO\.

__OS2447__

__RN56__

O campo Mês/Ano permitirá a digitação da data no formato mm/aaaa \(mês/ano\)\.

__OS2447__

__RN57__

O campo “Retificadora” deve assumir os seguintes valores:

“Sim”, quando marcado e “Não”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__OS2447__

__RN58__

O campo “Nº\. da Retificação” deve ser exibido desabilitado\. O campo só deve ser habilitado e preenchido quando o campo “Retificadora” estiver marcado\. O campo “Nº\. da Retificação” deve ser numérico de 2 \(duas\) posições\.

__OS2447__

__RN59__

O campo “Gerar Inventário” deve ser exibido através de um checkbox\. O campo deve assumir os seguintes valores: “S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__OS2447__

__RN60__

Logo abaixo no campo “Gerar Inventário” devem ser exibidos os tipos de inventário através de um radiobutton\. Deve apresentar os seguinte valores: “Produto” e “NBM”\. Por default a opção “Produto” deve estar marcada\. Gravar “P” para “Produto” e “N” para “NBM”\. Por default, esse campo deve ser exibido desabilitado e apenas deve ser habilitado quando o campo “Gerar Inventário” estiver marcado\.

__OS2447__

__RN61__

Os campos “Data Inicial Inventário” e “Data Final Inventário” devem aceitar datas no formato dd/mm/aaaa\. Por default, esses campos devem ser exibidos desabilitados e apenas devem ser habilitados quando o campo “Gerar Inventário” estiver marcado\.

__OS2447__

__RN62__

O campo “Gerar Segmento M” deve assumir os seguintes valores:

“Sim”, quando marcado e “Não”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

Quando este campo estiver marcado, deve\-se considerar a geração do segmento M\.

__OS2447__

__RN62\.a__

O campo “Considerar 7 Últimas Posições da Nota Fiscal” deve assumir os seguintes valores:

“Sim”, quando marcado e “Não”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

Quando este campo estiver marcado, deve\-se pegar as 7 Últimas Posições do número da Nota Fiscal  na geração do segmento O\.

__MFS63174__

__RN62\.b__

O campo “Desconsiderar Valor IPI p/ Base Outras – Segmento B” deve ser exibido através de um checkbox\. O campo deve assumir os seguintes valores: “S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado

__MFS910409__

__RN62\.c__

O campo “Desconsiderar Valor IPI p/ Base Outras – Segmento D” deve ser exibido através de um checkbox\. O campo deve assumir os seguintes valores: “S”, quando marcado, e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__MFS1015800__

__RN63__

Devem ser exibidos somente os estabelecimentos que atenderem as seguintes premissas:

- Que estejam licenciados;
- Que o usuário possua direito de acesso na ferramenta PowerLock;
- Que pertença ao estado do Tocantins\.

__OS2447__

__RN64__

__A1 – Segmento:__ Preencher com o texto fixo “A”\.

__OS2447__

__RN65__

__A2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para a empresa e o estabelecimento que estão sendo gerados\.

__OS2447__

__RN66__

Preencher com brancos\.

__OS2447__

__RN67__

__A3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN68__

__A4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.  Caso não esteja informado, preencher com zeros\.

__OS2447__

__RN69__

__A5 – Atividade econômica principal:__ Recuperar o campo COD\_ATIVIDADE da tabela ESTABELECIMENTO para a empresa e o estabelecimento que estão sendo gerados\.

__OS2447__

__RN70__

__A6 – Tipo de Estabelecimento:__ Recuperar o campo IND\_MATRIZ\_FILIAL da tabela ESTABELECIMENTO para o estabelecimento que está sendo gerado e gravar:

- “M”, se o conteúdo do campo for M\.
- “F”, se o conteúdo do campo for F\.

__OS2447__

__RN71__

__A7 – Portador da TARE:__ Preencher com o valor informado no campo “Portador de TARE” da tela Parâmetros – Dados Iniciais\. Gravar “S”, quando marcado e “N”, quando desmarcado\.

__OS2447__

__RN72__

__A8 – Tipo de Escrituração:__  Preencher com o valor informado no campo “Tipo de Escrituração” da tela Parâmetros – Dados Iniciais\.

- Caso o campo possua a opção “Fiscal” selecionada, gravar “F”\.
- Caso o campo possua a opção “Contábil” selecionada, gravar “C”\.

__OS2447__

__RN73__

__A9 – Saldo Inicial de Caixa:__ Preencher com o valor contido no campo “Saldo Inicial de Caixa” da tela Obrigações – Dados Mensais da Declaração\.

__OS2447__

__RN74__

__A10 – Saldo Final de Caixa: __Preencher com o valor contido no campo “Saldo Final de Caixa” da tela Obrigações – Dados Mensais da Declaração\.

__OS2447__

__RN75__

__A11 – Usuário de ECF: __Preencher com o valor informado no campo “Usuário de ECF” da tela Parâmetros – Dados Iniciais\. Gravar “S”, quando marcado e “N”, quando desmarcado\.

__OS2447__

__RN76__

__A12 – CPF Declarante: __ Recuperar o campo NUM\_CPF da tabela RESP\_INFORMACAO referente ao declarante escolhido no campo “Declarante” da tela Parâmetros – Dados Iniciais\. 

__OS2447__

__RN77__

__A13 – Nome Declarante:__ Recuperar o campo NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO referente ao declarante escolhido no campo “Declarante” da tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN78__

__A14 – Nº CRC Contabilista:__ Recuperar o campo NUM\_CRC da tabela RESP\_CONTADOR referente ao contabilista escolhido no campo “Contabilista” da tela Parâmetros – Dados Iniciais\.

__\[ALTERADO CH18241\_2013\]__

“Quando o valor do campo NUM\_CRC contiver menos do que 10 caracteres, a geração deverá ser alinhada à direita e completado o campo com espaços \.”

__\[ALTERADO MFS10301\]__

“Quando o valor do campo NUM\_CRC contiver menos do que 10 caracteres, a geração deverá ser alinhada à direita e completado o campo com Zeros \.”

__OS2447__

__MFS10301__

__RN79__

__A15 – UF CRC Contabilista:__ Recuperar a UF correspondente ao campo IDENT\_ESTADO\_CRC da tabela RESP\_CONTADOR  referente ao contabilista escolhido no campo “Contabilista” da tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN80__

__A16 – Nome Contabilista:__ Recuperar o campo NOM\_RESPONSAVEL da tabela RESP\_INFORMACAO referente ao contabilista escolhido no campo “Contabilista” da tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN81__

__A17 – Telefone Contabilista:__ Recuperar o campo DDD\_TELEFONE concatenado com o campo NUM\_TELEFONE da tabela RESP\_INFORMACAO referente ao contabilista escolhido no campo “Contabilista” da tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN82__

__A18 – Saída/prestações com débito de imposto: __

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘611’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\. 

__OS2447/__

__OS3091__

__RN83__

__A19 – Outros débitos:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘585’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero, quando o período de referência for posterior a 06/2012\.

Ex\.: 00000000000000

__OS2447/__

__OS3091/ OS3758__

__RN84__

__A20 – Estorno de créditos \(incluir os créditos transferidos\):__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘579’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN85__

__A21 – Entradas/aquisições com crédito do imposto: __Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘612’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN86__

__A22 – Outros créditos \(incluir os créditos recebidos por transferência\): __Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘584’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

__OS2447/__

__OS3091/__

__OS3758__

__RN87__

__A23 – Estornos de Débito:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘581’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN88__

__A24 – Saldo credor do período anterior:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘613’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

__OS2447/__

__OS3091/ OS3758__

__RN89__

__A25 – Deduções:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘616’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

__OS2447/__

__OS3091/ OS3758__

__RN90__

__A26 – Diferencia de Alíquota a recolher:__ Preencher com o resultado da soma do diferencial de alíquota do período e do diferencial de alíquota do período anterior\. Esse campo só deverá ser preenchido quando o valor for maior que 50,00\.

Cálculo: A26 = A35 \+ A36

__OS2447__

__RN91__

__A27 – Valor dos produtos: __ Verificar se o parâmetro = 48, está parametrizado na tela de Parâmetros por UF\. Recuperar o somatório do campo VLR\_TOT\_NOTA, no caso de Nota Fiscal sem item e VLR\_CONTAB\_ITEM, no caso de Nota Fiscal com item das tabelas de documento fiscal, utilizando os mesmos critérios do livro de apuração do ICMS\-ST, identificando as operações internas e interestaduais através dos CFOPs começados com 1 \(entrada interna\), 5 \(saída interna\) e 2 \(entrada interestadual\)\.

__OS2447__

__RN92__

__A28 – Base de Cálculo:__ Verificar se o parâmetro = 48, está parametrizado na tela de Parâmetros por UF\. Recuperar o somatório do campo VLR\_BASE\_ICMSS, no caso de Nota Fiscal com e sem item das tabelas de documento fiscal, utilizando os mesmos critérios do livro de apuração do ICMS\-ST, identificando as operações internas e interestaduais através dos CFOPs começados com 1 \(entrada interna\), 5 \(saída interna\) e 2 \(entrada interestadual\)\.

__OS2447__

__RN93__

__A29 – ICMS Substituição Tributária:__  Recuperar o somatório do campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘631’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘632’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘633’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Somar 631 \+ 632 \+ 633\.

__OS2447__

__RN94__

__A30 – Crédito de ICMS:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘635’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

__OS2447__

__RN95__

__A31 – Outros créditos:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘636’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘637’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_CLASSE = ‘639’ para a empresa, estabelecimento, data da apuração dentro do período geração e UF\.

Somar 636 \+ 637 \+ 639\.

__OS2447__

__RN96__

__A32 – Número da TARE:__ Preencher com o valor informado no campo “Nº do TARE” na tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN97__

__A33 – Versão do arquivo:__ Preencher o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher com 9\.4\.0

Alteração da __MFS6415__: Este campo é preenchido com o conteúdo informado no campo “Versão” da tela de geração\.

__OS2447/__

__OS3091/__

__CH81269__

__CH99437__

__MFS6415__

__RN98__

__A34 – Data Vencimento do TARE:__ Preencher com o valor informado no campo “Vencimento do TARE” na tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN99__

__A35 – Diferencial de Alíquota do Período:__ Recuperar o campo VLR\_DIF\_ALIQ\_PER da tabela EST\_TO\_DIF\_ALIQ referente ao período de referência\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

__OS2447/ OS3758__

__RN100__

__A36 – Diferencial de Alíquota a Recolher Transportado do Período Anterior:__ Preencher com o valor informado no campo “Diferencial de Alíquota a recolher do período anterior” na tela Obrigações – Dados Mensais da Declaração\. Recuperar o campo VLR\_DIF\_ALIQ\_ANT da tabela EST\_TO\_DIF\_ALIQ referente ao período de referência\.

__\[ALTERADA – OS3758\]__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

__OS2447/ OS3758__

__RN101__

__A37 – Tipo de Encerrante considerado na Escrituração de LMC__: Preencher com brancos\.

__OS2447__

__RN102__

__A38 – Observações sobre os Encerrantes informados no seguimento G__: Preencher com brancos\.

__OS2447__

__RN103__

__A39 – Houve Mudança de domicílio:__ Preencher com o valor informado do campo “Houve Mudança de Domicílio” da tela Obrigações – Meio Magnético\. Gravar “S”, quando marcado e “N”, quando desmarcado\.

__\[ALTERADA – OS3758\]__

__A39 – Complementação de Alíquota do Período__

Este campo deve ser preenchido com zero\.

Ex\.: 00000000000000

 

__OS2447/ OS3758__

__RN103\-A__

Alteração da __MFS6415 __\(inclusão do campo A40__\-__Diferencial de alíquota consumidor final \(saídas\) do período\):

__A40 \- Diferencial de alíquota consumidor final \(saídas\) do período:__

A geração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à este campo *não* existe, e o campo A40 é o campo descrito na “__RN104__”

Na versão 10\.0 à este campo é gerado normalmente com a numeração A40;

Conforme manual de orientação da vsr 10\.0, este campo deve ser preenchido com zeros\.

__MFS6415__

__RN104__

__A40 – Município Anterior:__ Preencher com o valor informado no campo “Município Anterior” da tela Obrigações – Meio Magnético\. 

__\[ALTERADA – OS3758\]__

__A40 – Houve Mudança de domicílio:__ Preencher com o valor informado do campo “Houve Mudança de Domicílio” da tela Obrigações – Meio Magnético\. Gravar “S”, quando marcado e “N”, quando desmarcado\.

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A40__;

Na versão 10\.0 à a numeração deste campo é = __A41__;

__OS2447/ OS3758__

__MSF6415__

__RN105__

__A41 – Data Inicial da cidade atual:__ Preencher com o valor informado no campo “Data Inicial” referente ao Município Atual da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

__\[ALTERADA – OS3758\]__

__A41 – Município Anterior:__ Preencher com o valor informado no campo “Município Anterior” da tela Obrigações – Meio Magnético\. 

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A41__;

Na versão 10\.0 à a numeração deste campo é = __A42__;

__OS2447/ OS3758__

__MFS6415__

__RN106__

__A42 – Data Final da cidade atual:__ Preencher com o valor informado no campo “Data Final” referente ao Município Atual da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

__\[ALTERADA – OS3758\]__

__A42 – Data Inicial da cidade atual:__ Preencher com o valor informado no campo “Data Inicial” referente ao Município Atual da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A42__;

Na versão 10\.0 à a numeração deste campo é = __A43__;

__OS2447/ OS3758__

__MFS6415__

__RN107__

__A43 – Data Inicial da cidade anterior:__ Preencher com o valor informado no campo “Data Inicial” referente ao Município Anterior da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

__\[ALTERADA – OS3758\]__

__A43 – Data Final da cidade atual:__ Preencher com o valor informado no campo “Data Final” referente ao Município Atual da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A43__;

Na versão 10\.0 à a numeração deste campo é = __A44__;

__OS2447/ OS3758__

__MFS6415__

__RN108__

__A44 – Data Final da cidade anterior: __ Preencher com o valor informado no campo “Data Final” referente ao Município Anterior da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

__\[ALTERADA – OS3758\]__

__A44 – Data Inicial da cidade anterior:__ Preencher com o valor informado no campo “Data Inicial” referente ao Município Anterior da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A44__;

Na versão 10\.0 à a numeração deste campo é = __A45__;

__OS2447/ OS3758__

__MFS6415__

__RGB\-01__

__Segmento B – Entradas e Saídas de Mercadorias, Bens e/ou Serviços no Estabelecimento do Contribuinte:__

__\[ALTERAÇÃO \- MFS59925__\] Inclusão de regra para considerar Notas Fiscais de Serviço no Segmento B\.

Incluir na regra para considerar as Notas Fiscais de Serviço, conforme informações recuperadas da Tabela “EST\_RES\_CFO\_UF\_01”, pela Procedure “SAF\_EST\_RES\_CFO\_UF” \(Resumo Por UF/CFOP\), o CFOP deverá ser parametrizado na tela Parâmetros – Segmento M → Por CFOP no módulo da GIAM\-TO\.

#### Além das informações já tratadas para geração do Segmento B, após inclusão da opção “Considerar Notas de Serviço com CFOP’s do Ajuste SINIEF 03/04”, na tela do menu Parâmetros – Parâmetros p/ Dados Acessórios, considerar também a Notas Fiscais de Serviços de Entradas\.

#### Documentos Fiscais de Entrada: 

Tratamento:

#### Parâmetros de Registros de Entrada → Por CFOP 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Campo 11 \- DATA\_FISCAL deve ser pertinente ao período de geração da obrigação;
- Campo 03 \- MOVTO\_E\_S <> “9”;
- Campo 12 \- COD\_CLASS\_DOC\_FIS deve ser = “1” e “3”; __OR__ 

                              COD\_CLASS\_DOC\_FIS = '2' se parâmetro P\_IND\_CONSID\_NF\_SERV = __'S'__

__Observação:__ Conforme inclusão da opção__ __“Considerar Notas de Serviço com CFOP’s do Ajuste SINIEF 03/04”, conforme menu Parâmetros – Parâmetros p/ Dados Acessórios, __a__proveitar a regra do parâmetro “P\_IND\_CONSID\_NF\_SERV”\.

#### Documentos Fiscais de Saídas: 

#### Parâmetros de Registros de Entrada → Por CFOP 

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Campo 11 \- DATA\_FISCAL deve ser pertinente ao período de geração da obrigação;
- Campo 03 \- MOVTO\_E\_S = “9”;
- Campo 12 \- COD\_CLASS\_DOC\_FIS deve ser = “1”, “3” e “4”\.

__ __

__MFS59925__

__RN109__

__B1 – Segmento:__ Preencher com o texto fixo “B”\.

__OS2447__

__RN110__

__B2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN111__

__B3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN112__

__B4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN113__

__B5 – Indica se entrada ou saída: __Recuperar o COD\_CFO referente ao campo IDENT\_CFO da tabela EST\_RES\_CFO\_UF\_01 e gravar:

- “0”, quando o cfop começar com 1, 2 ou 3
- “1”, quando o cfop começar com 5, 6 ou 7

__OS2447__

__RN114__

__B6 – Código Fiscal de Operações e de Prestações: __ Recuperar o COD\_CFOP referente ao campo IDENT\_CFO a tabela EST\_RES\_CFO\_UF\_01\.

__OS2447__

__RN115__

__B7 – Base de Cálculo:__ Recuperar  o campo VLR\_BASE\_ICMS referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN116__

__B8 – Isentas / Não Tributadas:__ Recuperar o campo VLR\_BASE\_ISENTAS referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN117__

__\[ALTERAÇÃO – MFS910409__\] Alteração da regra de preenchimento do campo de acordo com o novo parâmetro\.

__B9 – Outras:__

Se o parâmetro “Desconsiderar Valor IPI p/ Base Outras – Segmento B” estiver marcado na tela 

     Recuperar o campo VLR\_BASE\_OUTRAS referente a tabela EST\_RES\_CFO\_UF\_01

Senão

     Recuperar o campo VLR\_BASE\_OUTRAS \+ VLR\_OUTR\_IMPOSTOS referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091/__

__CH81269/__

__MFS31566__

__MFS910409__

__RN118__

__B10 – Substituição Tributária: __

__\[MFS31278\]__

Se o campo VLR\_ICMS\_S estiver preenchido

     Recuperar o campo VLR\_ICMS\_S referente a tabela EST\_RES\_CFO\_UF\_01

Senão

     Recuperar o campo VLR\_BASE\_ICMS\_ST referente a tabela EST\_RES\_CFO\_UF\_01\.

__OS2447/__

__MFS31278__

__RN119__

__B11 – Valor Contábil: __Recuperar o campo VLR\_CONTABIL referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, esse campo deve ser igual ao campo B10\.

__OS2447/__

__OS3091__

__RN120__

__B12 – Crédito do Imposto no caso de entrada e débito do imposto no caso de saída:  __Recuperar o campo VLR\_ICMS referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN121__

__B13 – Domicílio Fiscal: __

Gravar “B”\. Se o campo DAT\_APURAC da tabela EST\_RES\_CFO\_UF\_01 for igual ao campo DATA\_FIM\_ANT da tabela EST\_TO\_DADOS\_MENSAIS\.

Gravar “A”\. Se o campo DAT\_APURAC da tabela EST\_RES\_CFO\_UF\_01 for igual ao campo DATA\_FIM\_ATUAL da tabela EST\_TO\_DADOS\_MENSAIS\.

__OS2447__

__RN122__

__C1 – Segmento:__ Preencher com o texto fixo “C”\.

__OS2447__

__RN123__

__C2 – Inscrição Estadual:__ Recupera o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN124__

__C3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN125__

__C4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN126__

__C5 – Tributadas: __ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

__OS2447__

__RN127__

__C6 – Isentas e/ou tributadas:  __Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ISENTO da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ISENTO da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN128__

__C7 – Outras:__ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_OUTRAS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_OUTRAS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento 

__OS2447/__

__OS3091/__

__CH81269__

__RN129__

__C8 – Substituição Tributária: __ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Inicial do Inventário” da tela de geração\.

__OS2447__

__RN130__

__C9 – Valor Total:__ Preencher com o resultado da somatória dos campos C5, C6, C7 e C8\.

Cálculo: C9 = C5 \+ C6 \+ C7 \+ C8

__OS2447__

__RN131__

__C10 – Tributadas:__ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

__OS2447__

__RN132__

__C11 – Isentas e/ou tributadas: __ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ISENTO da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ISENTO da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN133__

__C12 – Outras:__ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_OUTRAS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_OUTRAS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

__OS2447/__

__OS3091/__

__CH81269__

__RN134__

__C13 – Substituição Tributária:__ Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “Produto”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela X52\_INVENT\_PRODUTO para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

Se o campo “Tipo de Inventário“ da tela Obrigações – Meio Magnético estiver marcado com “NBM”:

Recuperar o somatório do campo VLR\_BASE\_ICMSS da tabela X62\_INVENTARIO\_NBM para a empresa, estabelecimento e data do inventário igual à data informada no campo “Data Final do Inventário” da tela de geração\.

__OS2447__

__RN135__

__C14 – Valor Total:__ Preencher com o resultado da somatória dos campos C10, C11, C12 e C13\.

Cálculo: C14 = C10 \+ C11 \+ C12 \+ C13

__OS2447__

__RN136__

__D1 – Segmento:__ Preencher com o texto fixo “D”\.

__OS2447__

__RN137__

__D2 – Inscrição Estadual: __Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN138__

__D3 – Período de Referencia: __ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN139__

__D4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN140__

__D5 – Indica se entrada ou saída__ Recuperar o COD\_CFO referente ao campo IDENT\_CFO da tabela EST\_RES\_CFO\_UF\_01 e gravar:

- “0”, quando o cfop começar com 1, 2 ou 3
- “1”, quando o cfop começar com 5, 6 ou 7

Devem ser gerados registros do tipo “D” tantos quanto forem necessários para cada operação de Entrada ou Saída existente na apuração do ICMS\.

__OS2447__

__RN141__

__D6 – Código da UF: __ Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF referente ao IDENT\_ESTADO cadastrado na tabela EST\_RES\_CFO\_UF\_01\.

__OS2447__

__RN142__

__D7 – Base de Cálculo ou base de cálculo contribuinte em caso de saída: __

Em caso de entrada: 

Recuperar o campo VLR\_BASE\_ICMS referente a tabela EST\_RES\_CFO\_UF\_01\.

Em caso de saída:

Preencher o campo com o resultado da diferença: VLR\_BASE\_ICMS\_NC \- VLR\_BASE\_ICMS\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN143__

__D8 – Base de cálculo não contribuinte em caso de saída:__ 

Em caso de entrada: 

Preencher com zeros\.

Em caso de saída:

Recuperar o campo VLR\_BASE\_ICMS\_NC referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__\[ALTERADA – CH8820\_2012\]__

Se o parâmetro \(Parâmetros > Parâmetros para Dados Acessórios\) estiver com “pelo CFOP” selecionado, considerar os CFOP’s: ‘618', '619','645','653','663','5258','5307','5357','6107','6108', '6258','6307','6357', caso contrário, preencher com zeros\.

Essa regra deve contemplar a geração centralizada e a não centralizada\.

__OS2447/__

__OS3091/ CH8820\_2012 __

__RN144__

__D9 – Isentas/Não Tributadas:__ Recuperar o campo VLR\_BASE\_ISENTAS referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN145__

__\[ALTERAÇÃO \- MFS1015800\] __Alteração da regra de preenchimento do campo de acordo com o novo parâmetro

__D10 – Outras:__

Se o parâmetro “Desconsiderar Valor IPI p/ Base Outras – Segmento D” estiver marcado na tela

        Recuperar o campo VLR\_BASE\_OUTRAS referente à tabela EST\_RES\_CFO\_UF\_01\.

Senão

        Recuperar o campo VLR\_BASE\_OUTRAS \+ VLR\_OUTR\_IMPOSTOS referente à tabela EST\_RES\_CFO\_UF\_01\.

__OS2447/__

__OS3091/__

__CH81269/__

__MFS31566__

__MFS1015800__

__RN146__

__D11 – Substituição Tributária:__

__\[MFS31469\]__

Se o campo VLR\_ICMS\_S estiver preenchido

     Recuperar o campo VLR\_ICMS\_S referente a tabela EST\_RES\_CFO\_UF\_01

Senão

     Recuperar o campo VLR\_BASE\_ICMS\_ST referente a tabela EST\_RES\_CFO\_UF\_01\.

__OS2447/__

__MFS31469__

__RN147__

__D12 – Valor contábil quando entrada / Valor Contábil contribuinte quando saída:  __

Em caso de entrada: 

Recuperar o campo VLR\_CONTABIL referente a tabela EST\_RES\_CFO\_UF\_01\.

Em caso de saída:

Preencher o campo com o resultado da diferença: VLR\_CONTABIL\_NC \- VLR\_CONTABIL\.

__OS2447__

__RN148__

__D13 – Valor contábil não contribuinte: __

Em caso de entrada: 

Preencher com zeros\.

Em caso de saída:

Recuperar o campo VLR\_CONTABIL\_NC referente a tabela EST\_RES\_CFO\_UF\_01\.

__OS2447__

__RN149__

__D14 – Crédito do Imposto no caso de Entrada e Débito do Imposto contribuinte no caso de saída: __

Em caso de entrada: 

Recuperar o campo VLR\_ICMS referente a tabela EST\_RES\_CFO\_UF\_01\.

Em caso de saída:

Preencher o campo com o resultado da diferença: VLR\_ICMS\_NC \- VLR\_ICMS\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN150__

__D15 – Débito do Imposto não contribuinte: __

Em caso de entrada: 

Preencher com zeros\.

Em caso de saída:

Recuperar o campo VLR\_ICMS\_NC referente a tabela EST\_RES\_CFO\_UF\_01\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais, preencher com zeros\.

__OS2447/__

__OS3091__

__RN151__

__D16 – Domicílio Fiscal: __

Gravar “B”\. Se o campo DAT\_APURAC da tabela EST\_RES\_CFO\_UF\_01 for igual ao campo DATA\_FIM\_ANT da tabela EST\_TO\_DADOS\_MENSAIS\.

Gravar “A”\. Se o campo DAT\_APURAC da tabela EST\_RES\_CFO\_UF\_01 for igual ao campo DATA\_FIM\_ATUAL da tabela EST\_TO\_DADOS\_MENSAIS\.

__OS2447__

__RN152__

__E1 – Segmento:__ Preencher com o texto fixo “E”\.

__OS2447__

__RN153__

__E2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN154__

__E3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN155__

__E4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN156__

__E5 – Tipo de ICMS:__ Preencher com o valor informado no campo “Tipo de ICMS” da tela de ICMS a Recolher \(Obrigações – ICMS a Recolher\)\.

- Caso a opção selecionada na tela seja “Normal”, gravar “N”\.
- Caso a opção selecionada na tela seja “Diferencial de Alíquota”, gravar “D”\.
- Caso a opção selecionada na tela seja “Substituição Tributária”, gravar “S”\.

__\[ALTERADA – OS3758\]__

Inclusão da opção __Complementação de Alíquota__, na geração deste campo:

- Caso a opção selecionada na tela seja “Complementação de Alíquota”, gravar “C”\.

Alteração da __MFS6415__:

Inclusão de duas novas opções:

- Caso a opção selecionada na tela seja “Diferencial de Alíquota \(saídas\)”, gravar “F”\.
- Caso a opção selecionada na tela seja “Fundo combate a Pobreza”, gravar “P”\.

__OS2447/ OS3758__

__MFS6415__

__RN157__

__E6 – Data de Vencimento:__ Preencher com o valor informado no campo “Data de Vencimento” da tela de ICMS a Recolher \(Obrigações – ICMS a Recolher\)\. Gravar no formato DDMMAAAA\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais e o campo E5 for igual a “N”, preencher com brancos\.

__OS2447/__

__OS3091__

__RN158__

__E7 – Valor do ICMS a Recolher:__ Preencher com o valor informado no campo “Valor do ICMS a Recolher” da tela de ICMS a Recolher \(Obrigações – ICMS a Recolher\)\.

Se o parâmetro “Optante Simples Nacional” estiver marcado na tela Parâmetros – Dados Iniciais e o campo E5 for igual a “N”, preencher com zeros\.

__OS2447/__

__OS3091__

__RN159__

__J1 – Segmento:__ Preencher com o texto fixo “J”\.

__OS2447__

__RN160__

__J2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN161__

__J3 – Período de Referencia:__ Preencher o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN162__

__J4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN163__

__J5 – Número da TARE:__ Preencher com o valor informado no campo “Nº do TARE” na tela Parâmetros – Dados Iniciais\.

__OS2447__

__RN164__

__J6 – Data Vencimento do TARE:__ Preencher com o valor informado no campo “Vencimento do TARE” na tela Parâmetros – Dados Iniciais\. Gravar no formato DDMMAAAA\.

__OS2447__

__RN165__

__K1 – Segmento:__ Preencher com o texto fixo “K”\.

__OS2447__

__RN166__

__K2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN167__

__K3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN168__

__K4 – Retificação:__ Preencher o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN169__

__K5 – Código da Base Legal:__ Recuperar o campo COD\_AMPARO\_LEGAL da tabela EST\_GIA\_INFO, quando o campo COD\_AMPARO\_LEGAL começar com “OCR” \. Gravar no arquivo somente a parte numérica\.

__OS2447__

__RN170__

__K6 – Valor do Crédito:__ Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_AMPARO\_LEGAL começar com “OCR”

__OS2447__

__RN171__

__L1 – Segmento:__ Preencher com o texto fixo “L”\.

__OS2447__

__RN172__

__L2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN173__

__L3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN174__

__L4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN175__

__L5 – Código da Base Legal:__ Recuperar o campo COD\_AMPARO\_LEGAL da tabela EST\_GIA\_INFO, quando o campo COD\_AMPARO\_LEGAL começar com “DED”\. Gravar no arquivo somente a parte numérica\.

__OS2447__

__RN176__

__L6 – ICMS Devido__: Preencher com zeros\.

__OS2447__

__RN177__

__L7 – Média do ICMS__: Preencher com zeros\.

__OS2447__

__RN178__

__L8 – Valor da Dedução: __Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_AMPARO\_LEGAL começar com “DED”

__OS2447__

__RGM\-01__

__Segmento M – Saídas e/ou Prestações e Entradas e/ou Aquisições do Estabelecimento do Contribuinte por Município de Origem:__

Recuperar documentos fiscais \(SAFX07, SAFX08\) de saída que possuam CFOP parametrizado na tela Parâmetros – Segmento M → Por CFOP no módulo da GIAM\-TO\.

__Documentos Fiscais de Saída:__

#### Parâmetros de Registros de Saída → Por CFOP

- Código da empresa = passado como parâmetro
- Código estabelecimento  = passado como parâmetro
- Campo 11 \- DATA\_EMISSAO deve ser pertinente ao período de geração da obrigação;
- Campo 03 \- MOVTO\_E\_S = “9”;
- Campo 12 \- COD\_CLASS\_DOC\_FIS deve ser  = “1”, “3” e “4”;
- Código do Município \(município\) e UF do estabelecimento gerador pertencente a Tocantins;
- Campo 74 \- IND\_TRANSF\_CRED = “0”;
- Campo 125 \- IND\_SITUACAO\_ESP <> “1”, “2” e “8”;
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar somente as notas fiscais com CFOP iniciados com “5” \(somente operações internas\)\.  __\[MFS31589\]__
- As notas canceladas de compras devem ser consideradas\. 
- Quando Prestação de Serviço de Transporte \[\(COD\_PARAM = 158\], o Código do Município que tem que estar preenchido é o código do município origem \(campo 182 \- COD\_MUNICIPIO\_ORIG\), da capa do documento para recuperação\.

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração do Meio Magnético estiver __marcado__, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\.

__OS3735__

__MFS31589__

__RGM\-02__

__Segmento M – Saídas e/ou Prestações e Entradas e/ou Aquisições do Estabelecimento do Contribuinte por Município de Origem:__

Recuperar documentos fiscais \(SAFX07, SAFX08\) de entrada que possuam CFOP parametrizado na tela Parâmetros – Segmento M → Por CFOP no módulo da GIAM\-TO\.

#### Documentos Fiscais de Entrada: 

#### Parâmetros de <a id="_Toc319078198"></a>Registros de Entrada → Por CFOP 

- Código da empresa = passado como parâmetro
- Código estabelecimento  = passado como parâmetro
- Campo 11 \- DATA\_EMISSAO deve ser pertinente ao período de geração da obrigação;
- Campo 03 \- MOVTO\_E\_S <> “9”;
- Campo 12 \- COD\_CLASS\_DOC\_FIS deve ser  = “1” e “3”;
- Código do Município \(município\) e UF pertencente a Tocantins 
- Campo 74 \- IND\_TRANSF\_CRED = “0”;
- Campo 125 \- IND\_SITUACAO\_ESP <> “1”, “2” e “8”;
- Recuperar as notas fiscais com itens e as notas fiscais sem itens\.
- Recuperar as notas fiscais com CFOP\.

         \-   COD\_PARAM = 424 \(receber como parâmetro\)

- As notas canceladas de vendas devem ser consideradas\. 

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração do Meio Magnético estiver __marcado__, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\.

__OS3735__

__RGM\-03__

#### Documentos Fiscais de Energia e Comunicação: 

Recuperar documentos fiscais \(SAFX42 e SAFX43\) de utilities que possuam CFOP parametrizado na tela Parâmetros – Segmento M → Por CFOP no módulo da GIAM –TO:

- Código da empresa = passado como parâmetro
- Código estabelecimento = passado como parâmetro
- Campo 03 \- DAT\_FISCAL deve ser pertinente ao período de geração da obrigação;
- Campo 13 \- COD\_MODELO deve ser = “06”, “21” ou “22”;
- Campo 50 \- COD\_CLASS\_DOC\_FIS deve ser  = “1” e “3”;
- Estado deve ser igual ao do estabelecimento;
- Recuperar as notas fiscais com itens e as notas fiscais sem itens;
- Recuperar somente as notas fiscais com CFOP iniciados com “5” \(somente operações internas\)\.  __\[MFS31589\]__
- Campo 75 \- UF\_CONSUMO deve estar devidamente preenchido\.
- COD\_PARAM = 423 e 157 \(receber como parâmetro\)

gSE

- Não considerar os documentos gerados pelo Mapa Resumo, 
- As notas canceladas de vendas devem ser consideradas\. 

Quando o parâmetro __“*Geração Centralizada por Inscrição Estadual Única”*__ da Geração do Meio Magnético estiver __marcado__, o somatório deverá considerar todos os estabelecimentos centralizados e o centralizador ao estabelecimento centralizador parametrizado no modulo controle das obrigações estaduais\. \(Inventário e Documentário Fiscal\)\. As parametrizações deverão ser feitas sempre em nome do estabelecimento centralizador\.

__OS3735__

__MFS31589__

__RN179__

__M1 – Segmento:__ Preencher com o texto fixo “M”\.

__OS2447__

__RN180__

__M2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN181__

__M3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN182__

__M4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN183__

__M5 – Município de Origem: __

__ \[ALTERADA – OS3735\]__

Neste campo devem ser informados os municípios do Estado do Tocantins \(com base nos códigos do IBGE\), que tiveram saídas de mercadorias, bens e/ou prestação de serviços, ou entradas de mercadorias, bens e/ou aquisições de serviços, por município de origem __\[ALTERADA – CH6481\_2014/ CH11196\_2018 \(MFS\-18435\)\], __ou seja, do declarante\.  

__\[MFS31589\]__

__Para as entradas:__

Se operação interna \(CFOP iniciado com “1”\)

     Se COD\_MUNICIPIO\_ORIG estiver preenchido

         Deve ser recuperada a informação do campo 182 \- COD\_MUNICIPIO\_ORIG 183 \- COD\_MUNICIPIO\_DEST da SAFX07

     Senão

         Deve ser recuperada a informação do campo COD\_MUNICIPIO do Estabelecimento

Senão \(CFOP iniciado com “2” ou “3”\)

     Deve ser recuperada a informação do campo COD\_MUNICIPIO do Estabelecimento

__\[MFS30712\]__

__Para as saídas:__ 

__Mercadorias__

Se operação interna \(CFOP iniciado com “5”\)

     Se COD\_MUNICIPIO\_DEST estiver preenchido

          Deve ser recuperada a informação do campo 183 \- COD\_MUNICIPIO\_DEST 182 \- COD\_MUNICIPIO\_ORIG da SAFX07

     Senão

         Deve ser recuperada a informação do campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

Senão \(CFOP iniciado com “6” ou “7”\)

         O Registro não deve ser gerado, pois não devem ser geradas operações p/ fora do estado \(vide tabela de CFOP do manual da GIAM\-TO\)\.

__Utilities__

Se operação interna \(CFOP iniciado com “5”\)

     Se COD\_MUNIC\_CONSUMO estiver preenchido

          Deve ser recuperada a informação do campo 76 \- COD\_MUNIC\_CONSUMO da SAFX42

     Senão

         Deve ser recuperada a informação do campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\.

Senão \(CFOP iniciado com “6” ou “7”\)

         O Registro não deve ser gerado, pois não devem ser geradas operações p/ fora do estado \(vide tabela de CFOP do manual da GIAM\-TO\)\.

Deve ser feito consolidação por código de município, caso o mesmo código seja gerado mais de uma vez, levando em consideração RN185 e RN186\.

Deve se concatenado o código da UF com o código do município\.

__OS2447/ CH88941/ OS3735/__

__CH6481\_2014__

__CH11196\_2018 \(MFS\-18435\)/__

__MFS30712/__

__MFS31589__

__RN184__

__M6 – Domicílio Fiscal: __Verificar se o campo “Houve Mudança de Domicílio” está marcado\. Se estiver não estiver marcado, gravar “A”\. Se estiver marcado, gravar “B” se a data fiscal da nota estiver dentro do período de validade para o município anterior informado na tela Obrigações – Dados Mensais da Obrigação e gravar “A” se a data fiscal da nota estiver dentro do período de validade para o município atual informado na tela Obrigações – Dados Mensais da Obrigação\.

__OS2447__

__RN185__

__M7 – Saídas e/ou Prestações: __Recuperar notas fiscais utilizando o mesmo critério do Resumo de UF/CFOP\. Verificar se o CFOP está parametrizado na tela Parâmetros – Parâmetros p/ Segmento M – por CFOP\. Recuperar o somatório do campo VALOR\_CONTABIL, se os CFOPs começarem com 5, 6 ou 7\.  Quando este campo for preenchido, o campo __M8 – Entradas e/ou Aquisições __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(M5\), os valores deste campo deverão ser somados\.

__\[ALTERADA – OS3735\]__

__M7 – Saídas e/ou Prestações: __Recuperar notas fiscais utilizando o critério da regra RGM\-01 e RGM\-03\. Verificar se o CFOP está parametrizado na tela Parâmetros – Parâmetros p/ Segmento M – por CFOP\. Recuperar o somatório do campo VALOR\_CONTABIL, se os CFOPs começarem com 5\.  

Quando este campo for preenchido, o campo __M8 – Entradas e/ou Aquisições __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(M5\), os valores deste campo deverão ser somados\.

__OS2447 / CH88941/ OS3735__

__RN186__

__M8 – Entradas e/ou Aquisições: __Recuperar notas fiscais utilizando o mesmo critério do Resumo de UF/CFOP\. Verificar se o CFOP está parametrizado na tela Parâmetros – Parâmetros p/ Segmento M – por CFOP\. Recuperar o somatório do campo VALOR\_CONTABIL, se os CFOPs começarem com 1, 2 ou 3\. Quando este campo for preenchido, o campo __M7 – Saídas e/ou Prestações __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(M5\), os valores deste campo deverão ser somados\.

__\[ALTERADA – OS3735\]__

__M8 – Entradas e/ou Aquisições: __Recuperar notas fiscais utilizando o mesmo critério da regra RGM\-02\. Verificar se o CFOP está parametrizado na tela Parâmetros – Parâmetros p/ Segmento M – por CFOP\. Recuperar o somatório do campo VALOR\_CONTABIL, se os CFOPs começarem com 1, 2 ou 3\. Quando este campo for preenchido, o campo __M7 – Saídas e/ou Prestações __deve ser preenchido com zeros\.

Caso haja consolidações de código de município semelhante \(M5\), os valores deste campo deverão ser somados\.

__OS2447 / CH88941/ OS3735__

__RN187\-G__

__Regra para Segmento N:__

Na geração do Segmento N, recuperar as Notas Fiscais \(com ou sem item\), independente se o campo 30 – SITUAÇÃO \(SAFX07\) = ‘S’ ou ‘N’\.

Os demais filtros, para recuperar as notas fiscais, não devem sofrer alterações\.

__Origem dos Dados__: SAFX07 \- Documentos Fiscais \(Capa\)

                            SAFX08 \- Documentos Fiscais \(Itens\)

Serão recuperadas as notas fiscais apenas de entrada, que atendam aos seguintes critérios:

\- Empresa – empresa da apuração;

\- Estabelecimento – estabelecimento da apuração, ou

\- Estabelecimento – quando se tratar de apuração centralizada por I\.E\.U\.serão recuperadas as notas fiscais de todos os

  estabelecimentos envolvidos na centralização \(estabelecimento centralizador e estabelecimentos centralizados\);

\- Data da nota – notas com data fiscal enquadrada no período de geração;

\- Classificação – notas de classificação 1 e 3 \(nota de mercadoria e nota mista\);

\- CFOP parametrizado para Aquisição com Diferimento de ICMS \(menu: Parâmetros > Aquisição c/ Diferimento de ICMS > Por CFOP/ Natureza de Operação\);

\- UF da pessoa fis/jur igual a Tocantins\.

__OS2447__

__MFS574911__

__RN187__

__N1 – Segmento:__ Preencher com o texto fixo “N”\. 

__OS2447__

__RN188__

__N2 – Inscrição Estadual:__ Preencher com o valor contido no campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN189__

__N3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN190__

__N4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN191__

__N5 – Identificação da Empresa: __Recuperar o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR cadastrada na Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2447__

__RN192__

__N6 – Domicílio Fiscal: __Verificar se o campo “Houve Mudança de Domicílio” está marcado\. Se estiver não estiver marcado, gravar “A”\. Se estiver marcado, gravar “B” se a data fiscal da nota estiver dentro do período de validade para o município anterior informado na tela Obrigações – Dados Mensais da Obrigação e gravar “A” se a data fiscal da nota estiver dentro do período de validade para o município atual informado na tela Obrigações – Dados Mensais da Obrigação\.

__OS2447__

__RN193__

__N7 – Município: __Recuperar o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR cadastrada na Nota Fiscal de Entrada , que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__\[MFS574911\] __Inclusão do código da UF no preenchimento do campo código do município

Este campo é preenchido com a concatenação do código da UF \+ código do município da Pessoa física/jurídica da nota\.

Recuperar o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR, referente ao IDENT\_FIS\_JUR cadastrado na tabela SAFX07\.

Recuperar o campo COD\_UF da tabela MUNICIPIO, referente ao COD\_MUNICIPIO cadastrado na tabela SAFX04\.

__Obs\.: __Se o campo código do município não tiver 5 caracteres, completar com zeros à esquerda\.

__OS2447__

__MFS574911__

__RN194__

__N8 – Valor Total das Notas informadas para a inscrição indicada no campo N5: __Recuperar o somatório do campo O8 para cada Inscrição estadual\.

__\[ALTERADA – CH4518\_2012\]:__

Nesse registro não deve haver distinção se a NF tem ou não item, ou seja, uma consolidação\. Deve haver um somatório, conforme a RN202\.

__OS2447/ CH4518\_2012__

__RN195__

__O1 – Segmento:__ Preencher com o texto fixo “O”\.

__OS2447__

__RN196__

__O2 – Inscrição Estadual:__ Preencher com o valor contido no campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN197__

__O3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN198__

__O4 – Retificação: __ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN199__

__O5 – Identificação da Empresa: __Recuperar o campo INSC\_ESTADUAL da tabela X04\_PESSOA\_FIS\_JUR cadastrada na Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2447__

RN200

__O6 – Domicílio Fiscal: __Verificar se o campo “Houve Mudança de Domicílio” está marcado\. Se estiver não estiver marcado, gravar “A”\. Se estiver marcado, gravar “B” se a data fiscal da nota estiver dentro do período de validade para o município anterior informado na tela Obrigações – Dados Mensais da Obrigação e gravar “A” se a data fiscal da nota estiver dentro do período de validade para o município atual informado na tela Obrigações – Dados Mensais da Obrigação\.

__OS2447__

__RN201__

__O7 – Número da Nota: __Recuperar o campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL para Nota Fiscal de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__\[MFS63174\] __Inclusão do parâmetro para definir a forma de gerar o número do documento fiscal

Se o parâmetro “Considerar 7 Últimas Posições da Nota Fiscal” da tela de geração estiver marcado

     Considerar as 7 últimas posições do campo

Senão

     Considerar as 7 primeiras posições do campo

__OS2447__

__MFS63174__

__RN202__

__O8 – Valor da Nota: __Recuperar o campo VLR\_TOT\_NOTA da tabela DWT\_DOCTO\_FISCAL, para notas sem item e o somatório do campo VLR\_CONTAB\_ITEM da tabela DWT\_ITENS\_MERC, para notas com itens de Entrada, que possua CFOP/Natureza de Operação parametrizados na tela Parâmetros – Aquisição com diferimento do ICMS, e cuja pessoa fis/jur seja de Tocantins e com município diferente do município do estabelecimento que está sendo gerado\.

__OS2447__

__RN203__

__P1 – Segmento__: Preencher com o texto fixo “P”\.

__OS2447__

__ RN204__

__P2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__ RN205__

__P3 – Período de Referencia: __ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN206__

__P4 – Retificação:__ Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN207__

__P5 – Domicílio Fiscal: __Recuperar o campo IND\_DOMICILIO\_FISCAL da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN208__

__P6 – Código da UF: __ Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF referente ao IDENT\_ESTADO cadastrado na tabela EST\_TO\_DIF\_ALIQ\_UF\. 

__OS2447__

__RN209__

__P7 – Valor Contábil: __ Recuperar o campo VLR\_CONTABIL da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN210__

__P8 – Base de Cálculo: __Recuperar o campo VLR\_BASE da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__ RN211__

__P9 – Diferencial de Alíquota: __Recuperar o campo VLR\_DIF\_ALIQ da tabela EST\_TO\_DIF\_ALIQ\_UF\.

__OS2447__

__RN211\-A__

__Alteração da MFS6415: __\(novo campo P10 criado na versão 10\.0 da GIAM\-TO\)

__P10\-Alíquota:__

Este campo compõe o segmento P *apenas* quando a versão informada na tela da geração for = 10\.0 \(ou superiores\)\. Para a versão 9\.6 o segmento P vai apenas até o campo P9\.

O campo será preenchido com a alíquota do diferencial da tabela EST\_TO\_DIF\_ALIQ\_UF\.

*\(a geração que alimenta a tabela EST\_TO\_DIF\_ALIQ\_UF \(Obrigações > Diferencial de Alíquota > Geração\) foi alterada na MFS6415 para passar a gerar esta informação, que corresponde a diferença entre as alíquotas origem x destino\)*

__MFS6415__

__RN212__

__Z1 – Segmento:__ Preencher com o texto fixo “Z”\.

__OS2447__

__RN213__

__Z2 – Inscrição Estadual:__ Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS2447__

__RN214__

__Z3 – Período de Referencia:__ Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS2447__

__RN215__

__Z4 – Retificação: __Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS2447__

__RN216__

__Z5 – Total de registro que compõe a declaração:__ Preencher com o total de registros gerados no arquivo, exceto o registro Z\.

__OS2447__

__RN217__

Os campos numéricos devem ser completados com zeros à esquerda\.

__OS2447__

__RN218__

O menu Parâmetros – Parâmetros p/ Segmento M – por CFOP deve chamar a janela genérica utilizada nas demais GIAS, para a tabela PRT\_CFO\_MSAF\. Utilizar as mesmas regras de tela\.

__OS2447__

__RN219__

O campo “Estabelecimento“ deve exibir os estabelecimentos pertencentes a Tocantins que estejam licenciados\.

__OS2447__

__RN220__

O campo “Tipo” deve exibir as opções “157 – Comunicação”, “158 \- Transporte”, “423 \- Demais Saídas/Prestações” e “424 \- Demais Entradas”\.

__OS2447__

__RN221__

O campo “CFOP” deve exibir os CFOPs de acordo com o tipo escolhido:

Se o tipo for “158 – Transporte”, “157 \- Comunicação” ou “423 – Demais saídas”, a tela deve exibir os CFOPs começados por 5, 6 ou 7\.

Se o tipo for “Demais entradas”, a tela deve exibir os CFOPs começados por 1, 2 ou 3\.

__OS2447__

__RN222__

__Regra p/ o campo Optante Simples Nacional__

O campo “Optante Simples Nacional” deve ser exibido através de uma chekbox\. O campo deve assumir os seguintes valores: “S”, quando marcado e “N”, quando desmarcado\. Por default o campo deve ser exibido desmarcado\.

__OS3091__

__RN223__

__Regra para campo A33, do Segmento A:__

__Módulo:__ Estadual → GIAM TO

__Menu:__ Obrigações → Geração do Meio Magnético

__A33 – Versão do arquivo:__ Preencher o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher com 9\.5\.0\.

__\[ALTERADA – OS3758\]__

__A33 – Versão do arquivo:__ Preencher o valor informado no campo “Versão” da tela Obrigações – Meio Magnético\.

Preencher com 9\.6\.0\.

Alteração da __MFS6415__: Este campo é preenchido com o conteúdo informado no campo “Versão” da tela de geração\.

__OS3544/ OS3758__

__MFS6415__

__RN224__

__Regra para Segmento O:__

Na geração do Segmento O, recuperar as Notas Fiscais \(com ou sem item\), independente se o campo 30 – SITUAÇÃO = ‘S’ ou ‘N’\.

Os demais filtros, para recuperar as notas fiscais, não devem sofrer alterações\. 

__CH4518\_2012__

__RN225__

__Regra para Segmento N:__

Na geração do Segmento N, recuperar as Notas Fiscais \(com ou sem item\), independente se o campo 30 – SITUAÇÃO \(SAFX07\) = ‘S’ ou ‘N’\.

Os demais filtros, para recuperar as notas fiscais, não devem sofrer alterações\.

__VIDE RN187\-G__

__CH4518\_2012__

__RGR\-01__

__Regra para Segmento R – Especificação de Outros Débitos:__

Os campos desse segmento devem ser recuperados da tabela EST\_GIA\_INFO para a empresa, estabelecimento e o mês/ ano informados na tela de geração do meio magnético, e quando no campo COD\_AMPARO\_LEGAL começar com “ODB”\.

__RN226__

__R1 – Segmento:__ Especificação de Outros Débitos

Preencher com o texto fixo “R”\.

__OS3758__

__RN227__

__R2 – Inscrição Estadual:__ 

Recuperar o campo INSCRICAO\_ESTADUAL da tabela REGISTRO\_ESTADUAL para o estabelecimento que está sendo gerado\.

__OS3758__

__RN228__

__R3 – Período de Referencia:__ 

Preencher com o valor informado no campo “Mês/Ano” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\. Gravar no formato MMAAAA\.

__OS3758__

__RN229__

__R4 – Retificação:__ 

Preencher com o valor informado no campo “Nº\. da Retificação” da tela de geração do meio magnético \(Estadual – GIAM TO – Obrigações – Meio Magnético\)\.

__OS3758__

__RN230__

__R5 – Código da Base Legal:__ 

Recuperar o campo COD\_AMPARO\_LEGAL da tabela EST\_GIA\_INFO, quando o código começar com “ODB”\.

Recuperar somente a parte numérica\.

__OS3758__

__RN231__

__R6 – Valor do Débito:__

Recuperar o campo VLR\_OUTROS da tabela EST\_GIA\_INFO, quando o campo COD\_AMPARO\_LEGAL começar com “ODB”\. 

__OS3758__

__RN232__

__A45 – Data Final da cidade anterior:__

Preencher com o valor informado no campo “Data Final” referente ao Município Anterior da tela Obrigações – Meio Magnético\. Gravar no formato DDMMAAAA\.

Alteração da __MFS6415 \(renumeração dos campos A40 ao A45 para a versão 10\.0\): __

A numeração deste campo depende da versão da GIAM\-TO informada na tela da geração, da seguinte forma:

Na versão 9\.6 à a numeração deste campo é = __A45__;

Na versão 10\.0 à a numeração deste campo é = __A46__;

__OS3758__

__MFS6415__

__RN233__

__Segmento S__

__Segmento S – Especificação do Diferencial de Alíquotas Consumidor Final \(Saídas\) por UF:           __\(criado pela __MFS6415__\)

Este segmento foi incluído na GIAM na vrs 10\.0 \(Port 748/16\), e será gerado *apenas* quando a versão informada na tela da geração for = 10\.0\.

Trata\-se dos valores referentes ao diferencial de alíquota da Emenda Constitucional 87/2015, cuja  apuração é feita no Módulo ICMS\. No entanto, como as informações solicitadas no Segmento S não têm o mesmo formato da EFD, será necessário recuperar as informações das notas fiscais\.

__Origem dos Dados__: SAFX07 \- Documentos Fiscais \(Capa\)

                            SAFX08 \- Documentos Fiscais \(Itens\)

Serão recuperadas as notas fiscais apenas de saída, das operações interestaduais, que atendam aos seguintes critérios:

\- Empresa – empresa da apuração;

\- Estabelecimento – estabelecimento da apuração, ou

\- Estabelecimento – quando se tratar de apuração centralizada por I\.E\.U\.serão recuperadas as notas fiscais de todos os

  estabelecimentos envolvidos na centralização \(estabelecimento centralizador e estabelecimentos centralizados\);

\- Data da nota – notas com data fiscal enquadrada no período de geração, ou, notas com data extemporânea enquadrada

   no período de geração;

\- Classificação – notas de classificação 1, 3 ou 4 \(nota de mercadoria, nota mista, ou transporte\);

\- CFOP – apenas as saídas interestaduais \(CFOP’s iniciados por “6”\);

\- Somente notas fiscais não canceladas;

\- Serão consideradas apenas as notas / itens que tenham ao menos algum destes campos preenchidos:

__Nas notas sem itens \(SAFX07\)__

__Nas notas com itens \(SAFX08\)__

   284\-Valor ICMS UF Destino

   222\-Valor ICMS UF Destino

   285\-Valor ICMS UF Origem

   223\-Valor ICMS UF Origem

Obs: O campo referente ao valor do FECEP da EC87 não será considerado, pois *não* é solicitado no Segmento S\.

Os dados recuperados serão agrupados por UF de destino, \(campo “122\-UF Destino” da SAFX07\), e para cada UF, serão totalizados os seguintes valores:

\- Valor Contábil do Documento;

\- Valor da Base Tributada do ICMS;

\- ICMS destino;

\- ICMS origem\.

Para cada UF totalizada, será gerada uma linha no Segmento S\. As regras sobre o preenchimento dos campos estão descritas a seguir \(__RN233\-1__ a __RN233\-12__\)\.

__MFS6415__

__RN233\-1__

__Segmento S, campo S1\-Segmento: __

Este campo será preenchido com “S”\. 

__MFS6415__

__RN233\-2__

__Segmento S, campo S2\-Inscrição Estadual: __

Este campo será preenchido com a inscrição estadual do estabelecimento \(cadastro das Inscrições Estaduais do Módulo Parâmetros\)\.

__MFS6415__

__RN233\-3__

__Segmento S, campo S3\-Período de Referência: __

Este campo será preenchido com o mês e ano do período informado na tela da geração do meio magnético, no formato MMAAAA\. 

__MFS6415__

__RN233\-4__

__Segmento S, campo S4\-Retificação: __

Este campo será preenchido com o número da retificação informado no campo “Nº\. da Retificação” da tela de geração do meio magnético\. Quando não preenchido, o campo será preenchido com zeros\.

Verificar se o campo “Houve Mudança de Domicílio” está marcado\. Se estiver não estiver marcado, gravar “A”\. Se estiver marcado, gravar “B” se a data fiscal da nota estiver dentro do período de validade para o município anterior informado na tela Obrigações – Dados Mensais da Obrigação e gravar “A” se a data fiscal da nota estiver dentro do período de validade para o município atual informado na tela Obrigações – Dados Mensais da Obrigação\.

__MFS6415__

__RN233\-5__

__Segmento S, campo S5\-Domicílio Fiscal: __

Este campo é preenchido a partir da informação do campo “*Houve Mudança de Domicílio*” das informações iniciais da declaração, no menu “Obrigações > Dados Mensais da Declaração”, da seguinte forma:

__Se__ estiver desmarcado, gravar “A”;

__Se__ estiver marcado:

    \- Gravar “A” se o período informado no campo 04 estiver dentro do período informado para o município atual informado no menu “Obrigações –

      Dados Mensais da Obrigação”;

    \- Gravar “B” se o período informado no campo 04 estiver dentro do período informado para o município anterior informado no menu

      “Obrigações – Dados Mensais da Obrigação”;

__MFS6415__

__RN233\-6__

__Segmento S, campo S6\-Código UF: __

__\[ALTERADA \- CH14704\_2017 \(MFS\-12589\)\]__

Este campo é preenchido com a UF da totalização, conforme o processamento de geração do Segmento S descrito na __RN233__\.

Recuperar o campo COD\_UF\_OBRIG da tabela PRT\_UF\_OBRIG\_MSAF referente ao IDENT\_ESTADO cadastrado na tabela EST\_TO\_DIF\_ALIQ\_UF\.

__MFS6415__

__CH14704\_2017 \(MFS\-12589\)__

__RN233\-7__

__Segmento S, campo S7\-Valor Contábil: __

Este campo é preenchido a partir do total do Valor Contábil apurado para a UF em questão, conforme totalização descrita na __RN233__\.

__MFS6415__

__RN233\-8__

__Segmento S, campo S8\-Base de Cálculo: __

Este campo é preenchido a partir do total da Base de Cálculo do ICMS apurado para a UF em questão, conforme totalização descrita na __RN233__\.

__MFS6415__

__RN233\-9__

__Segmento S, campo S9\-Diferencial de Alíquota: __

Este campo é preenchido com o total do ICMS Origem \+ ICMS Destino \(valores informados nos campos S11 e S12\)\.

Obs: A Portaria Sefaz 748/2016 não tem nenhuma orientação sobre o preenchimento deste campo\. A princípio, o campo será gerado com o total do diferencial de alíquota, considerando Origem \+ Destino\.

__MFS6415__

__RN233\-10__

__Segmento S, campo S10\-Alíquota Consumidor: __

Este campo é preenchido de acordo com a “Tabela de Alíquota para UF” divulgada pela Portaria Sefaz 748, de 17/08/2016 \(item 3\.18\.1\), considerando a UF em questão \(UF informada no campo S6\)\.

__MFS6415__

__RN233\-11__

__Segmento S, campo S11\-Origem: __

Este campo é preenchido a partir do total do ”*ICMS Origem*” apurado para a UF em questão, conforme totalização descrita na __RN233__\.

__MFS6415__

__RN233\-12__

__Segmento S, campo S12\-Destino: __

Este campo é preenchido a partir do total do ”*ICMS Destino*” apurado para a UF em questão, conforme totalização descrita na __RN233__\.

__MFS6415__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

