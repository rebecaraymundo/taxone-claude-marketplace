# MTZ-DIMP_Regras_Bloco_0

- **Fonte:** MTZ-DIMP_Regras_Bloco_0.docx
- **Modificado:** 2025-10-11
- **Tamanho:** 97 KB

---

THOMSON REUTERS

DIMP \- Declaração de Informações de Meios de Pagamentos

Geração do Meio Magnético 

Bloco 0

__Localização__: Menu Estadual, módulo DIMP, menu Geração 🡪 Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS91838__

Aline Melo

09/08/2022

\(criação do documento\)

__MFS92288__

Aline Melo

15/08/2022

__MFS436204__

Aline Melo

Criação do registro 0006 e ajuste na geração do registro 0005\.

03/02/2023

__MFS436206__

Aline Melo

Criação do registro 0201\.

14/02/2023

__MFS436210__

Liliane Assaf

Criação do registro 0700

22/02/2023

__MFS525364__

Aline Melo

Ajuste nos registros 0100 e 0201

24/03/2023

__MFS520144__

Aline Melo

Ajuste na geração do registro 0700\.

20/06/2023

__MFS748247__

Graciela Soares

Inclisão do Registro 0002 e campos novos nos registros 0105 e 0200

18/02/2025

Sumário

[1\.	Regras Gerais do Bloco 0	1](#_Toc127982865)

[2\.	Registro 0000 – ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA INSTITUIÇÃO DE PAGAMENTO, FINANCEIRA OU DO INTERMEDIADOR	1](#_Toc127982866)

[3\.	Registro 0001 – Abertura do Bloco 0	1](#_Toc127982867)

4\.      Registro 0002 – IDENTIFICAÇÃO DE LIQUIDANTES DIVERSOS

[5\.	Registro 0005 – Dados Complementares do Autor do Arquivo	1](#_Toc127982868)

[6\.	Registro 0006 – Dados Complementares do Técnico Responsável	1](#_Toc127982869)

[7\.	Registro 0100 – Tabela de Cadastro do Cliente	1](#_Toc127982870)

[8\.	Registro 0105 – Tabela de Van do Cliente	1](#_Toc127982871)

[9\.	Registro 0200 – Tabela de Cadastro do Meio de Captura	1](#_Toc127982872)

[10\.	Registro 0201 – Identificação de Titulares de Conta Conjunta	1](#_Toc127982873)

[11\.	Registro 0300 – Dados da Instituição Parceira	1](#_Toc127982874)

[12\.	Registro 0600 – Autorização para Instituição Parceira	1](#_Toc127982875)

[13\.	Registro 0700 – Identificação da Intimação para Informações Específicas	1](#_Toc127982876)

[14\.	Registro 0990 – Encerramento do Bloco 0	1](#_Toc127982877)

# <a id="_Toc127982865"></a>Regras Gerais do Bloco 0

# <a id="_Toc127982866"></a>Registro 0000 – ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DA INSTITUIÇÃO DE PAGAMENTO, FINANCEIRA OU DO INTERMEDIADOR

__RN0000__

Registro obrigatório e corresponde ao primeiro registro do arquivo, gerado a partir dos dados da tela de geração e do Parâmetro de Empresa/Estabelecimento

Para o preenchimento do Registro 0000, o programa irá buscar os dados da tela de geração e do Parâmetro de Empresa/Estabelecimento\. 

Para os campos 05 \- CNPJ e 06 \- Nome do Layout DIMP é preenchido através das informações contidas no parâmetro Estabelecimento\.  


Os demais campos serão preenchidos conforme tela de Parâmetros de Geração do arquivo Dimp\.  


Observação: Quando a indicação for código 6 \- Autorização para Instituição Parceira no campo 03, deverá ter o cadastro da Autorização da Instituição Parceira SAFX314 para que seja gerado o Registro 0600\.

Para as Federações sem movimento o programa já irá gerar com finalidade 4 – Arquivo zerado para que não tenha que gerar novamente um a um\.

Nível hierárquico \- 2

Ocorrência \- um \(por arquivo\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0000\-02__

COD\_VER

Código da versão do layout\. Deve ser preenchido automaticamente no campo “Versão do Layout”:

06 – vigência de 01/01/2021 a 31/10/2021 \[MFS\-79177\]

07 \- vigência de 01/11/2021 a 31/12/2022 

08 – vigência a partir de 01/01/2023 \(substituída pela versão 09\)

09 – vigência a partir de 01/04/2023

10 \- vigência a partir de 01/06/2025

# <a id="_Toc127982867"></a><a id="OLE_LINK30"></a>Registro 0001 – Abertura do Bloco 0

__RN0000__

Registro obrigatório e deve ser gerado para abertura do bloco 0 e indica se há informações previstas para este bloco\.

Nível hierárquico \- 1

Ocorrência \- um \(por arquivo\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

# Registro 0002 – Identificação de Liquidantes Diversos

__RN0002__

__\[MFS748247\] inclusão do novo registro__

__Gerar este registro a partir da versão de Layout 10\.__

Nível hierárquico – 2 

Ocorrência – 1:N

Registro obrigatório caso seja informado no campo 06 do Registro 1110 \(CNPJ\_LIQ\) um CNPJ com raiz diferente da raiz do CNPJ do autor do arquivo ou da instituição parceira informada no campo 05 do registro 0000 \(quando estiver preenchido\)\.

Gerar um registro 0002 para cada  CNPJ\_ADQUI campo \(13 da SAFX313\) que foi gerado no campo 06 do registro 1110 que atenda a um dos seguintes critéiros:

1. Quando o CNPJ\_ADQUI do campo 13 da SAFX 313 for diferente do CNPJ do Estabelecimento, presente no registro 0000 campo 05\.

ou

1. Quando o CNPJ\_ADQUI do campo 13 da SAFX 313 for diferente do CNPJ de TODAS as Instiuições Parceira geradas no Registro 0300 campo 03\.

OBS: CNPJ da instituição parceira campo 03 do registro 0300, foi gerado com base nos campos 04 \- IND\_IP\_PAR e 05 \- COD\_IP\_PAR da SAFX313\. 

__RN0002\-01__

__Campo REG__

Preencher com o Texto fixo contendo "0002"

__RN0002\-02__

__Campo LIQ\_TERC__

Preencher com o campo 13 \- CNPJ\_ADQUI da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__RN0002\-03__

__Campo TP\_REL__

Preencher com o campo 43 \- IND\_TP\_REL da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Verificar como a mensagem é gerada no log, se precisa de cadastro na TFIX de código de erro?__

*“O Campo *__*Tipo de Relacionamento do Liquidante*__* é obrigatório\.”*

__ __

__RN0002\-04__

__Campo INFO\_SELLER__

Preencher com o campo 44 \- IND\_INFO\_SELLER da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log \- Verificar como a mensagem é gerada no log, se precisa de cadastro na TFIX de código de erro?__

*“O Campo *__*Indicador de detenção da informação do seller/vendedor*__* é obrigatório\.”*

# <a id="_Toc127982868"></a>Registro 0005 – Dados Complementares do Autor do Arquivo

<a id="_Hlk126759640"></a>__RN0005__

__\[MFS436204\] Ajuste na geração do registro\.__

Registro obrigatório, utilizado para complementar as informações de identificação do informante do arquivo\.

Nível hierárquico \- 2

Ocorrência \- um \(por arquivo\)

Para a geração do registro, deve ser recuperada a informação do campo “Responsável para Contato”, da tela de geração do meio magnético da DIMP\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0005\-08__

__Campo FONE__

Preencher com o campo NUM\_DDD \+ NUM\_TELEFONE da tabela RESP\_INFORMAÇÃO\. 

Se não estiver preenchido, preencher com o campo TELEFONE da tabela ESTABELECIMENTO e no log deve ser exibida mensagem informando que foi considerado o campo da tabela ESTABELECIMENTO\. 

__RN0005\-09__

__Campo EMAIL__

Preencher com o campo E\_MAIL__ __da tabela RESP\_INFORMAÇÃO\.

Se não estiver__ __preenchido, preencher com o campo E\_MAIL da tabela ESTABELECIMENTO e no log deve ser exibida mensagem informando que foi considerado o campo da tabela ESTABELECIMENTO\. 

# <a id="_Toc127982869"></a>Registro 0006 – Dados Complementares do Técnico Responsável

<a id="_Hlk126759664"></a>__RN0006__

__\[MFS436204\] Criação do registro em atendimento ao ATO COTEPE 81/22 que altera ATO COTEPE 65/18, válido a partir de Abril/2023\.__

Registro facultativo utilizado para complementar as informações de contato dos responsáveis pela geração do arquivo\. Caso a Instituição não pretenda informar o contato do técnico responsável, não é obrigatório informar este registro\. Se a instituição optar por informar o registro, todos os campos são obrigatórios\.

Deve ser gerado a partir do layout versão 09 \(válido a partir de Abril de 2023\)\.

Nível hierárquico – 3

Ocorrência – 1:N

Para a geração do registro, deve ser recuperada a informação do campo “Responsável Técnico para Contato”, da tela de geração do meio magnético da DIMP\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0006\-03__

__Campo FONE__

Preencher com o campo NUM\_DDD \+ NUM\_TELEFONE da tabela RESP\_INFORMAÇÃO\. 

Se não estiver preenchido, preencher com o campo TELEFONE da tabela ESTABELECIMENTO e no log deve ser exibida mensagem informando que foi considerado o campo da tabela ESTABELECIMENTO\. 

Campo obrigatório somente quando o campo__ “__Responsável Técnico para Contato”, for informado na tela de geração da DIMP\.

__RN0006\-04__

__Campo EMAIL__

Preencher com o campo E\_MAIL__ __da tabela RESP\_INFORMAÇÃO\.

Se não estiver__ __preenchido, preencher com o campo E\_MAIL da tabela ESTABELECIMENTO e no log deve ser exibida mensagem informando que foi considerado o campo da tabela ESTABELECIMENTO\. 

Campo obrigatório somente quando o campo__ “__Responsável Técnico para Contato”, for informado na tela de geração da DIMP\.

# <a id="_Toc127982870"></a>Registro 0100 – Tabela de Cadastro do Cliente

__RN0100__

Este registro tem por objetivo identificar os clientes do intermediador, que comercializam produtos ou prestam serviços, ou da Instituição de Pagamento ou Financeira, que recebem os pagamentos, depósitos ou transferências de recursos\. Devem ser informados somente os clientes com informações no arquivo\. O código do cliente a ser utilizado é único por arquivo e de livre atribuição pelo remetente do arquivo\. Sugere\-se guardar relação com o código do estabelecimento mostrado no comprovante da transação\. 

Caso o cliente tenha transação destinada a UF, campo 02 do registro 1120, diferente da sua UF o seu registro 0100 deverá ser informado no arquivo DIMP gerado para a UF de destino da transação\. 

Em contas conjuntas as transações deverão ser atribuídas ao CPF do primeiro titular\.

Nível hierárquico – 2 

Ocorrência – 1:1

O registro 0100 é gerado a partir da tela de Movimentação Financeira, através do Código do Cliente \(campo 02\-COD\_CLIENTE da SAFX313\) e as demais informações relacionadas são recuperadas da SAFX04\.

\[__MFS525364\]__

Para as movimentações financeiras \(SAFX313\) cujo o campo Tipo de Tecnologia = 09, deve ser gerado um registro 0100 para cada titular pertencente a mesma conta conjunta, relacionado ao código cliente informado no campo Código do Cliente \(campo 02\-COD\_CLIENTE da SAFX313\)\.

Os titulares da conta conjunta, devem ser recuperados através da tela “Titulares de Conta Conjunta”, através do botão X, na barra de menu da tela de Meio de Captura\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

# <a id="_Toc127982871"></a>Registro 0105 – Tabela de Van do Cliente

__RN0105__

Este registro tem por objetivo identificar as instituições que atuam no cliente informado no registro 0100 e que utilizaram a estrutura de tecnologia do declarante do arquivo \(VAN\) para captura de transações, sendo a liquidação do pagamento efetuada pelo CNPJ informado nesse registro\. 

Obrigatório apenas para as instituições de pagamento que tenham contrato ativo para utilização do serviço\. Caso a prestadora do serviço de VAN tenha conhecimento dos detalhes da transação, poderá enviar tais transações utilizando\-se do registro 0300\.

Este registro só deverá ser informado se existirem transações de VAN, neste caso todos os campos são de preenchimento obrigatório\.

Nível hierárquico – 3

Ocorrência – 1:N

O registro 0105 é gerado a partir do Código do Cliente VAN, cadastrado na tela de Cadastrado de Cliente VAN \(SAFX315\), associado na tela de Cadastro de Transações Cliente VAN \(SAFX316\)\. 

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0105\-05__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo VALOR__

Preencher com o campo 06 \- VLR\_TRANS da tabela X316\_DIMP\_TRANSACOES\_VAN \(SAFX316\)

Campo Obrigatório

# <a id="_Toc127982872"></a>Registro 0200 – Tabela de Cadastro do Meio de Captura

__RN0200__

Este registro tem por objetivo identificar os meios e modos de captura de pagamentos e transações no período ou em períodos anteriores\. O código do Meio de Captura, campo 02, a ser utilizado é único por arquivo e de livre atribuição pelo autor do arquivo, devendo ser utilizado no Registro 1110 e/ou no Registro 1200\. 

As instituições de pagamento ou financeiras que enviam informações em nome de intermediadores devem informar no campo 06 o nome ou URL do intermediador\. Sugere\-se guardar relação com o código do meio de captura mostrado no comprovante da transação\.

As instituições financeiras que atuam por meio de uma instituição financeira centralizadora, com CNPJ diferente, terão suas transações enviadas pela instituição centralizadora e o CNPJ da instituição responsável pela conta do cliente deverá ser informado no campo

NUM\_LOG antes dos dados da agência e conta\.

As instituições financeiras devem agrupar as transações conforme as “Contas” em que ocorrerem os créditos, sendo cada conta atribuída a um Registro 0200\. Não há diferenciação se ocorreu via mobile, Internet Banking, caixa ou outra forma de captura\.

Nível hierárquico – 2

Ocorrência – 1:N

Registro 0200 é obrigatório e gerado a partir da tela de Cadastro de Meio de Captura \(SAFX312\)\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0200\-07__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo SMARTPOS__

Preencher com o campo 08 \- IND\_SMARTPOS da tabela X312\_DIMP\_MCAPT \(SAFX312\)

Campo Não Obrigatório

<a id="OLE_LINK27"></a>

# <a id="_Toc127982873"></a>Registro 0201 – Identificação de Titulares de Conta Conjunta

Registro de preenchimento obrigatório caso seja informado o tipo de tecnologia “9” no campo 04 do Registro 0200\.

__RN0201__

__\[MFS436206\] Criação do registro em atendimento ao ATO COTEPE 81/22 que altera ATO COTEPE 65/18, válido a partir de Abril/2023\.__

Registro de preenchimento obrigatório caso seja informado o tipo de tecnologia “9” no campo 04 do Registro 0200\.

Deve ser gerado a partir do layout versão 09 \(Abril/2023\)\.

Nível hierárquico – 3

Ocorrência – 1:N

O registro deve ser gerado na seguinte situação:

Para cada registro de Movimentação Financeira \(SAFX313\), se o Tipo de Tecnologia \(campo 04\-TIPO\_TECN\) = ‘9’ \(Conta Conjunta\):

\- Deve ser gerado um registro 0201, para cada titular da conta, para cada titular pertencente a mesma conta conjunta, informado através do Código do Cliente na tela de Movimentação Financeira \(campo 07\-COD\_CLIENTE da SAFX313\)\. O código do cliente de todos os titulares da mesma conta conjunta, devem ser referenciados no registro 0100 \(campo 02\-COD\_CLIENTE\)\.

\- Os titulares da conta conjunta, devem ser recuperados através da tela “Titulares de Conta Conjunta”, através do botão X, na barra de menu da tela de Meio de Captura\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

#  <a id="_Toc127982874"></a>Registro 0300 – Dados da Instituição Parceira

Este registro tem por objetivo identificar as instituições cujas transações de seus clientes estejam sendo reportadas no arquivo\. Quando o remetente do arquivo tiver acesso à identificação dos beneficiários do pagamento/vendedores/prestadores de serviços deverá reportar as transações da “Instituição Parceira”\. Os clientes da “Instituição Parceira” deverão ser declarados no Registro 0100 e suas transações deverão conter o COD\_IP\_PAR, cadastrado no registro Campo 02 do 0300, informado no campo 02 do Registro 1100\. Todos os registros 0300 informados deverão ser utilizados no campo 02 do registro 1100\. 

Para reportar as transações das instituições parceiras não deverá ser criado registro 0100 com os dados da instituição parceira\. Deverá ser criado registro 0100 com os dados dos clientes da instituição parceira e este Código do Cliente que será informado no Registro 1100 ou 1500\.

<a id="OLE_LINK1"></a>

__ITEM__

__CAMPO__

__CONTEÚDO__

__MFS__

1

REG

Conteúdo fixo = “__0300__”

2

COD\_IP\_PAR 

Ver DExPARA

3

CNPJ 

Ver DExPARA

4

NOME 

Ver DExPARA

5

END

Ver DExPARA

6

CEP 

Ver DExPARA

7

COD\_MUN 

Ver DExPARA

8

UF 

Ver DExPARA

9

NOME\_RESP 

Ver DExPARA

10

FONE\_CONT 

Ver DExPARA

11

EMAIL\_CONT 

Ver DExPARA

# <a id="_Toc127982875"></a>Registro 0600 – Autorização para Instituição Parceira

O preenchimento do Registro 0600 será preenchido através da tabela safx314 \- Cadastro de Autorização Para Instituição Parceira\. OBS: O arquivo irá preencher o registro 0600 quando a finalidade no Registro 0000 campo 3 for do tipo 6\.   
A partir da data da emissão de autorização, a outorgante não poderá mais enviar arquivos com suas transações, concedendo essa autonomia as parceiras\.   
No arquivo de autorização deve ser informado, obrigatoriamente, os registros 0000,0001,0005,0600,0990,1001,1990,9001,9990,9900 e 9999\.   
O Uso da Finalidade 6 é exclusivo para uma instituição de pagamento ou Marketplace\. 

__ITEM__

__CAMPO__

__CONTEÚDO__

__MFS__

1

REG

Conteúdo fixo = “__0600__”

2

TP\_AUTORIZ 

Ver DExPARA

3

CNPJ 

Ver DExPARA

4

TP\_TRANSAC 

Ver DExPARA

5

N\_FANT 

Ver DExPARA

6

END 

Ver DExPARA

7

CEP 

Ver DExPARA

8

COD\_MUN 

Ver DExPARA

9

UF 

Ver DExPARA

10

NOME\_RESP 

Ver DExPARA

11

FONE\_CONT 

Ver DExPARA

12

EMAIL\_CONT 

Ver DExPARA

13

DT\_INI\_AUT 

Ver DExPARA

14

DT\_FIM\_AUT 

Ver DExPARA

# <a id="_Toc127982876"></a>Registro 0700 – Identificação da Intimação para Informações Específicas

__RN0700__

__\[MFS436210\] Criação do registro em atendimento ao ATO COTEPE 81/22 que altera ATO COTEPE 65/18, válido a partir de Abril/2023\.__

Registro facultativo utilizado informar o número do processo apenas em caso de intimação\.

Deve ser gerado a partir do layout versão 09 \(válido a partir de Abril de 2023\)\.

Nível hierárquico – 2

Ocorrência – 1:1

Ao acionar a execução da geração, verificar se as três condições a seguir estão atendidas:

1. Campo “Finalidade do Arquivo” preenchido com 3 – Remessa de arquivo para atender intimação;
2. Campo “Versão do Layout” igual ou superior a 09;
3. Campo “Processo Admin/Fiscal da Intimação” preenchido;
4. Campo “Código do Cliente” preenchido;

Caso todas as quatro condições forem atendidas, então gerar o registro 0700\.

Caso a primeira, segunda e a quarta condição forem atendidas, mas o campo “Processo Admin/Fiscal da Intimação” não preenchido, então não gerar o registro 0700 e exibir a seguinte mensagem de erro no log da geração:

<a id="_Hlk128489981"></a>*“Preencher o campo Processo Admin/Fiscal da Intimação para geração do registro 0700 em arquivo com Finalidade = 3\.”*

Todas essas informações estão presentes na Tela de Geração da DIMP\.

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN0700\-02__

__Campo ID\_PROC__

Preencher com o campo “Processo Admin/Fiscal da Intimação” informado na Tela de Geração da DIMP\.

# <a id="_Toc127982877"></a>Registro 0990 – Encerramento do Bloco 0

Este registro tem por objetivo identificar o encerramento do bloco 0 e informar a quantidade de linhas existentes no bloco\.

__ITEM__

__CAMPO__

__CONTEÚDO__

__MFS__

1

REG

Conteúdo fixo = “__0990__”

2

QTD\_LIN\_0

Quantidade total de linhas informadas no Bloco 0, incluindo os registros de abertura e fechamento do Bloco\.

= = = = = =

