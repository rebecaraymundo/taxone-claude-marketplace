# MTZ_ICMS_Transf_Cred_CompensacaoRJ_Geracao_Apuracao_Estab_Cred_x_Estab_Dev

- **Fonte:** MTZ_ICMS_Transf_Cred_CompensacaoRJ_Geracao_Apuracao_Estab_Cred_x_Estab_Dev.docx
- **Modificado:** 2024-02-15
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo ICMS

Transferência de Crédito \(Compensação Padrão RJ\) – Apuração Estab Credores X Estab Devedores

<a id="OLE_LINK20"></a><a id="OLE_LINK21"></a><a id="OLE_LINK22"></a>

<a id="OLE_LINK51"></a><a id="OLE_LINK52"></a>__Localização__: Menu Estadual, Módulo ICMS, item Datamart <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>🡪 Transferência de Débito/Crédito Automática 🡪 <a id="OLE_LINK28"></a><a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a>Transferência de Crédito \(Compensação – RJ\)  🡪 Apuração Estab\. Credores x Estab\. Devedores

 

__Localização__: Menu Estadual, Módulo ICMS, item Datamart🡪Transferência de Débito/Crédito Automática🡪Transferência de Crédito __\(Compensação – Padrão RJ\)__<a id="OLE_LINK56"></a><a id="OLE_LINK57"></a><a id="OLE_LINK58"></a>  🡪 Apuração Estab\. Credores x Estab\. Devedores

<a id="OLE_LINK146"></a><a id="OLE_LINK147"></a><a id="OLE_LINK148"></a><a id="OLE_LINK162"></a>Obs: A descrição deste menu foi alterada pela MFS6326 \(ver RN00\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

CH26343\_2015

Julyana Perrucini

Este documento tem como objetivo alterar a rotina de apuração dos estabelecimentos credores para os devedores na transferência de crédito de compensação do estado do Rio de Janeiro, para desconsiderar o valor de dedução da apuração do ICMS no saldo devedor\.

MFS6326

Vânia Mattos

<a id="OLE_LINK149"></a><a id="OLE_LINK150"></a><a id="OLE_LINK151"></a><a id="OLE_LINK163"></a><a id="OLE_LINK164"></a>Alteração <a id="OLE_LINK63"></a><a id="OLE_LINK64"></a><a id="OLE_LINK65"></a>nas rotinas de Transferência de Crédito Automática da modalidade “Compensação – RJ” para serem utilizadas por outros estados \(ver RN00 e RN02\)\. 

04/08/2017

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

<a id="OLE_LINK174"></a><a id="OLE_LINK175"></a><a id="OLE_LINK176"></a>

Alteração da __MFS6326__: Criação do campo UF para possibilitar que as rotinas de Transferência de Crédito Automática da modalidade <a id="OLE_LINK66"></a><a id="OLE_LINK67"></a><a id="OLE_LINK68"></a><a id="OLE_LINK69"></a>“Compensação – RJ” possam ser utilizadas por outros estados\. Para isso, o título “Compensação – RJ” foi alterado para “Compensação – Padrão RJI”\.

__Parâmetros da tela:__

__Obrigação Fiscal__ – Neste campo é exibido o código e a descrição da obrigação fiscal referente ao Livro de Apuração do ICMS \(o campo é apenas informativo, e *não* fica habilitado para alteração\):  “108 Registro de Apuração do ICMS – P9”\.

<a id="OLE_LINK180"></a><a id="OLE_LINK181"></a>__UF__ –<a id="OLE_LINK185"></a><a id="OLE_LINK186"></a><a id="OLE_LINK187"></a><a id="OLE_LINK188"></a>\. Este campo exibe a lista dos estados da tabela ESTADOS, para seleção do usuário\. Campo de preenchimento obrigatório\.

__Data da Apuração__ – Neste campo o usuário informa a data da apuração desejada\. Campo de preenchimento obrigatório\.

__Funcionamento da tela:__

O usuário informa a UF e uma data de apuração, e o sistema identifica <a id="OLE_LINK34"></a><a id="OLE_LINK35"></a><a id="OLE_LINK36"></a>todos os estabelecimentos __do RJ__ da UF informada que tenham apuração gerada para a data informada\. Então, exibe em tela estes estabelecimentos\. Os credores na coluna à esquerda, e os devedores à direita\.  Em cada coluna, os estabelecimentos são apresentados em ordem decrescente de valor\. 

Os estabelecimentos com saldo zero não são apresentados\.

__MFS6326__

RN01

Campo Valor do Débito do item Estabelecimentos Devedores:

__\[ALTERADA – CH26343\_2015\]__

Esse valor deve ser preenchido com o valor total do débito deduzindo nele o valor da Dedução \(item 012\) do Resumo da Apuração do Imposto da Apuração do ICMS do módulo ICMS, item de menu DATA MART >> Apuração do ICMS >> Ajuste SINIEF\.

CH26343\_2015

RN02

__Regras da Geração__:

<a id="OLE_LINK78"></a><a id="OLE_LINK79"></a>Ao clicar na opção <Geração>, será executado o processo de apuração das transferências de crédito a serem realizadas, com base nos dados demonstrados em tela\.

As transferências são dos estabelecimentos credores para os devedores, com objetivo de compensar os estabelecimentos em débito\.

As transferências são feitas a partir dos estabelecimentos de maior saldo credor, para os estabelecimentos de maior saldo devedor\.

Os valores de créditos a serem transferidos serão apenas os valores suficientes para zerar o saldo dos estabelecimentos em débito\. 

O processo se encerra ao acabarem os créditos, ou, quando não tiver mais estabelecimentos devedores\.

Exemplo:

<a id="_Hlk489622261"></a>    __Estabelecimentos Credores__

__Estabelecimentos Devedores__

WB\-2

2\.662\.010,89

WB\-1

2\.792\.595,17

WB\-4

1\.269\.546,65

WB\-3

1\.058,34

Para este cenário, teríamos as seguintes transferências a serem realizadas:

     \- o WB\-2 transfere crédito de 2\.662\.010,89 para o WB\-1;

          \(o WB\-2 fica zerado, pois transferiu todo o seu crédito\)

          \(o WB\-1 ainda fica devedor em 130,584,28\)

     \- o WB\-4 transfere crédito de 130\.584,28 para o WB\-1;

       \(o WB\-4 fica ainda com crédito de 1\.138\.962,37, pois transferiu só parte do seu crédito\)

       \(o WB\-1 fica zerado\)

Após identificar todas as transferências a serem realizadas, conforme a regra descrita acima, os dados de cada transferência são gravados na tabela __ICT\_TC\_ESTAB\_RJ\.__

Alteração __MFS6326:__ Como a UF foi inserida na tabela, ao gravar os dados processados, a geração passa a gravar também a UF informada\.

Para cada transferência serão armazenadas as seguintes informações:

\- Código da Empresa;

\- UF;

\- Data da Apuração;

<a id="OLE_LINK124"></a><a id="OLE_LINK125"></a>\- Código do Estabelecimento Credor;

\- Código do Estabelecimento Devedor;

\- Valor da Transferência;

<a id="OLE_LINK126"></a><a id="OLE_LINK127"></a><a id="OLE_LINK128"></a><a id="OLE_LINK129"></a>\- Valor do Saldo Inicial do Estabelecimento Credor \(antes da transferência\);

\- Valor do Saldo Final do Estabelecimento Credor \(após a transferência\);

\- Valor do Saldo Inicial do Estabelecimento Devedor \(antes da transferência\);

\- Valor do Saldo Final do Estabelecimento Devedor \(após a transferência\)<a id="OLE_LINK130"></a><a id="OLE_LINK131"></a>;

\- IND\_TRANSF\_CREDOR: <a id="OLE_LINK135"></a><a id="OLE_LINK136"></a><a id="OLE_LINK137"></a>Indica se o crédito transferido foi total \(T\) ou parcial<a id="OLE_LINK132"></a><a id="OLE_LINK133"></a><a id="OLE_LINK134"></a> \(P\);

<a id="OLE_LINK138"></a><a id="OLE_LINK139"></a>                                            \(se = “T”, significa que o estabelecimento credor ficou zerado após a transferência\)

                                            \(se = “P”, significa que o estabelecimento credor *não* ficou zerado após a transferência\) 

\- IND\_TRANSF\_DEVEDOR: Indica se o crédito recebido cobriu todo o saldo devedor \(T\) ou não \(P\);\-

                                            \(se = “T”, significa que o estabelecimento devedor ficou zerado após a transferência\)

                                            \(se = “P”, significa que o estabelecimento devedor *não* ficou zerado após a transferência\) 

\- Indicador de GERAÇÃO = “N” \(IND\_GERACAO\);

 

__MFS6326__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

