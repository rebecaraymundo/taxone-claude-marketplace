# MTZ-DIMP_Regras_Bloco_1

- **Fonte:** MTZ-DIMP_Regras_Bloco_1.docx
- **Modificado:** 2025-10-11
- **Tamanho:** 105 KB

---

THOMSON REUTERS

DIMP \- Declaração de Informações de Meios de Pagamentos

Geração do Meio Magnético 

Bloco 1

__Localização__: Menu Estadual, módulo DIMP, menu Geração 🡪 Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS436281__

Aline Melo

Criação do documento\.

Ajuste na geração do registro 1100 e 1200\.

16/02/2023

__MFS436196__

Liliane Assaf

Ajuste no registro 1115 para inclusão dos campos 11 \- IND\_NAT\_JUR e 12\- IND\_TP\_PIX válidos para versão 09 e superiores\. Ver DIMP\_DEPARA\.xlsx\.

22/02/2023

__MFS436198__

Liliane Assaf

Ajuste no registro 1120 para inclusão do campo 11 – ID\_PEDIDO válido para versão 09 e superiores\. Ver DIMP\_DEPARA\.xlsx\.

22/02/2023

__MFS516559__

Aline Melo

Ajuste na geração do 1100 conforme parametrização da tela de Dados Iniciais

23/02/2023

__MFS436200__

Aline Melo

Criação do registro 1500 e alteração nos registros 1100 e 1200\.

27/02/2023

__MFS436202__

Liliane Assaf

Criação do registro 1600 – versão 09 DIMP

01/03/2023

__MFS528771__

Aline Melo

Ajuste na geração do registro 1100 e seus filhos em atendimento ao cenário UF Cliente x Uf de Destino\.

14/04/2023

__MFS532335__

Aline Melo

Ajuste na geração do registro 1500\.

27/04/2023

__MFS520144__

Aline Melo

Ajuste na geração do registro 1100 e 1500\.

20/06/2023

__MFS748247__

Graciela Soares

Inclisão de Novos Campos nos registros 1120, 1200 , 1220 e 1600

18/02/2025

__MFS710763                      __

Graciela Soares

Ajustes em Regras da Geração do Meio Magnético para atendimento a versão 10 da DIMP nos registros 1100, 1115, 1200, 1220, 1500

20/03/2025

__MFS878928__

Andréa Rocha

Ajuste na geração dos registros 1200 e 1220 que não devem ser gerados, quando o campo 03\-COD\_FIN do registro 0000 for diferente de “1\-Remessa de arquivo Normal”\.

05/08/2025

Sumário

[1\.	Registro 1001 – Abertura do Bloco 1	1](#_Toc128596029)

[2\.	Registro 1100 – Resumo Mensal das Operações de Pagamento	1](#_Toc128596030)

[3\.	Registro 1110 – Operações Diárias de Pagamento por Meio de Captura	1](#_Toc128596031)

[4\.	Registro 1115 – Operações por Comprovante de Transação	1](#_Toc128596032)

[5\.	Registro 1120 – Intermediador de Serviços e Negócios	1](#_Toc128596033)

[6\.	Registro 1200 – Cancelamento Extemporâneo	1](#_Toc128596034)

[7\.	Registro 1220 – Cancelamento Transação de Intermediador	1](#_Toc128596035)

[8\.	Registro 1500 – Resumo Mensal Das Operações Financeiras	1](#_Toc128596036)

[9\.	Registro 1600 – Cancelamento Extemporâneo Consolidado	1](#_Toc128596037)

# <a id="_Toc128596029"></a>Registro 1001 – Abertura do Bloco 1

__RN1001__

Registro obrigatório e deve ser gerado para abertura do bloco 1, indicando se há informações sobre as operações de crédito e débito\.

Nível hierárquico \- 1

Ocorrência \- um \(por arquivo\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

<a id="OLE_LINK30"></a>

# <a id="_Toc128596030"></a>Registro 1100 – Resumo Mensal das Operações de Pagamento

<a id="_Hlk126759640"></a>__RN1100__

Este registro deve ser gerado para informar as transações mensais totalizadas por:

COD\_CLIENTE, por IP\_PAR e por IND\_COMEX \(Indicador de transação de pagamento ao exterior\)

Dessa forma, caso o COD\_CLIENTE tenha transações nacionais e internacionais, serão iniciados dois registros 1100 para ele\. 

Caso o COD\_CLIENTE tenha transações reportadas em nome de uma Instituição Parceira \(Campo 02 do Registro 1100\)

e tenha transações que não foram realizadas via Instituição Parceira, deverão ser gerados registros 1100 distintos para cada caso\. 

O registro 1100 de um COD\_CLIENTE deve ser seguido pelos seus respectivos registros 1110\.

Este registro admite o lançamento de operações extemporâneas apenas em arquivos com a finalidade do tipo 01, no campo 03 do registro 0000\. Deve ser criado um registro 1100 e seus filhos para cada mês em que ocorreu transação\.

Caso o registro 1100 se refira a uma transação com UF de destino diferente da UF do COD\_CLIENTE, deverá ser informado também no arquivo DIMP da UF de destino\. 

O registro 1100 é gerado a partir da tela de Movimentação Financeira \(SAFX313\)\.

__\[MFS436281/MFS516559\] Ajuste na geração do registro 1100, conforme regra abaixo:__

As informações geradas no registro, são recuperadas a partir da SAFX313 – Movimentação Financeira, seguindo os critérios abaixo:

__Critério de Seleção:__

\- Código da empresa = código da empresa da geração 

\- Código do estabelecimento = código do estabelecimento da geração 

\- Data de Operação \(campo DT\_OP\) pertencente ao período da geração

\- Situação da Operação \(campo SITUACAO\) = ‘N’

\- Indicador para Não Gerar Registros 1100 e 1500 \(campo ind\_não\_gera\_1100\_1500\) <> ‘S’ __\[MFS436281\]__

__\[MFS528771\] UF Cliente x UF Destinatário: __

UF do cliente __= __UF Destinatário \(regra atual\)

\-Deve ser gerado os registros com a UF relacionada ao Código do Cliente \(campo COD\_CLIENTE\) = UF informado no campo UF da tela de geração

UF do cliente __DIFERENTE__ da UF Destinatário

\-Deve ser gerado os registros com a UF relacionada ao Código do Cliente \(campo COD\_CLIENTE\) = UF informado no campo UF da tela de geração

\-Deve ser gerado os registros com a UF Destinatário \(campo UF\_DESTINO\) = UF informada no campo UF da tela de geração\.

<a id="_Hlk132364434"></a>__Obs\.: __No cenário de UF Cliente __DIFERENTE__ da UF do Destinatário os registros 1100 e seus filhos \(1110, 1115 e 1120\) devem ser informados

no arquivo para as 2 UF’s relacionadas na mesma transação, por exemplo:

Em uma transação, o código do cliente informado pertence a UF de SP e a UF Destinatário pertence a RS\.

\- Quando o usuário solicitar a geração do arquivo para a UF de SP, serão gerados nesse arquivo, o registro 1100 referente a essa transação, com seus registros 

Filhos \(1110, 1115 e 1120\), 0100 e 0200\.

\- Quando o usuário solicitar a geração do arquivo para a UF de RS, serão gerados os mesmos registros informados na situação acima\.

__\[MFS436200\]__

__Quanto ao parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” da Tela de Geração: __

  \- Se o parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” for __MARCADO__, então:

    As transações de Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) igual a 3, 4, 6, 8 não devem ser consideradas no registro 1100\.

  

  \- Se o parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” for __DESMARCADO__, então:

    As transações de Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) igual a 3, 4, 6, 8 devem ser consideradas no registro 1100\.

  

As demais Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) devem ser consideradas, independente do parâmetro marcado ou desmarcado\. 

__Verificação se o Cliente da transação é Pessoa Física ou Jurídica:__

Se for Pessoa Física, deve atender aos dois critérios a seguir:

   \- Valor Total de todas as transações do cliente \(mesmo CFP\) deve ser __IGUAL__ ou __SUPERIOR__ ao valor informado no campo Valor Total Mensal 

   da tela de Parâmetros > Dados Iniciais\. __\[MFS516559__: substituir o valor fixo ‘3\.375,00’ pelo valor informado no campo\]\. 

 __\[MFS710763\] – __Nos casos da finalidade 3 \(Remessa de arquivo para atender intimação\) e informações extemporâneas o limite mínimo de valores não se aplica\. 

Desconsiderar a Regra acima quando:

Quando a opção de seleção da finalidade for igual à 03 

__OU__ quando o campo campo IND\_EXTEMP da tabela SAFX313 for igual a “1” 

Deve\-se enviar o valor da transação sem limite\.

    __E__

   \- Quantidade total das Transações do cliente \(mesmo CPF\) deve ser __IGUAL__ ou __SUPERIOR__ ao valor informado no campo Quantidade de Transações 

da tela de Parâmetros > Dados Iniciais\. __\[MFS516559__: substituir o valor fixo ‘30’ pelo valor informado no campo\]\.

__\[MFS710763\] – __Nos casos da finalidade 3 \(Remessa de arquivo para atender intimação\) e informações extemporâneas o limite mínimo de quantidade não se aplica\. 

Desconsiderar a Regra acima quando:

Quando a opção de seleção da finalidade for igual à 03 

OU quando o campo campo IND\_EXTEMP da tabela SAFX313 for igual a “1” 

Deve\-se enviar o valor da transação sem limite\.

  

Se for Pessoa Jurídica, as transações devem ser consideradas independente dos totais de valores e quantidades\.

__\[MFS520144\]__

__Cenário de intimação \(campo Finalidade do arquivo = ‘3’\)__

Na geração do arquivo com finalidade = ‘3’, além dos critérios acima também devem ser considerados os critérios informados abaixo:

\- Versão do Layout” igual ou superior a 09;

\- Processo Admin/Fiscal da Intimação” preenchido;

\- Código do Cliente \(campo COD\_CLIENTE\) = código informado no campo Código do Cliente;

\- Deve ser gerado registro , e seus filhos para cada transação ocorrida no período informado;

\- Para o mês em que __NÃO__ ocorrer transação, deve ser gerado UM registro 1100 com os campos de valor e quantidade = ZERO e os registros filhos 1110, 1115 e 1120 __NÃO__ devem ser gerados\.

Nível hierárquico – 2

Ocorrência – 1:N \(1 por CNPJ ou CPF\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

# <a id="_Toc128596031"></a>Registro 1110 – Operações Diárias de Pagamento por Meio de Captura

<a id="_Hlk126759664"></a>__RN1110__

O preenchimento do registro 1110 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras, com os critérios de seleção especificados na regra do registro 1100\.

\[__MFS86995__\] Alteração da regra de agrupamento na geração do 1110 \(*Totalizador com operação de dois meios de pagamentos\.*

Regras campo 11 \- VLR\_TOT 

I – Uma única operação:

Agrupar por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex\.

*II – Totalizador com operação de dois meios de pagamentos:*

*Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ ID trasação complementar quando os códigos são iguais\.*

*III – Totalização por *dia:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ data operação\.

Regra campo 12 QTD\_TOT

I – Uma única operação:

Agrupar por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex\.

II – Totalizador com operação de dois meios de pagamentos:

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ ID trasação complementar quando os códigos são iguais:

III – Totalização por dia\.

Agrupa por empresa, estabelecimento, ident da instituição parceira, ident cliente e indicador comex \+ data operação\.

Nível hierárquico \- 3

Ocorrência \- 1:N \(1 por DT\_OP, COD\_MCAPT e CNPJ\_ADQUI\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

# <a id="_Toc128596032"></a>Registro 1115 – Operações por Comprovante de Transação

__RN1115__

O preenchimento do registro 1115 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras, com os critérios de seleção especificados na regra do registro 1100\.

Nível hierárquico \- 4

Ocorrência \- 1:N \(1 por comprovante\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN1115\-01__

__\[MFS710763\] Campo obrigatório e ajuste para receber em caso de campo em branco a informação do campo 04 ID\_TRANSAC__

__A partir da Versão do Layout 10 inserir mensagem de log, campo obrigatório\.__

__Campo 03 – COD\_AUT__

Preencher com o campo 15 \- COD\_AUT da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Caso o campo esteja vazio emitir a mensagem de Log:__

*“O Campo COD\_AUT \(Código de Autorização\) do Registro 1115 é de preenchimento obrigatório, e não foi informado\.”*

__Inserir na a seguinte condição:__ Quando o campo estiver em branco, incluir a informação do campo 16 – ID\_TRANSAC da tabela X313\_DIMP\_MOV \(SAFX313\)

__RN1115\-02__

__\[MFS710763\] Campo obrigatório__

__A partir da Versão do Layout 10 inserir mensagem de log, campo obrigatório\.__

__Campo 04 – ID\_TRANSAC__

Preencher com o campo 16 \- ID\_TRANSAC da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Caso o campo esteja vazio emitir a mensagem de Log:__

*“O Campo ID\_TRANSAC \(Identificação da Transação\) do Registro 1115 é de preenchimento obrigatório, e não foi informado\.”*

# <a id="_Toc128596033"></a>Registro 1120 – Intermediador de Serviços e Negócios

__RN1120__

O preenchimento do registro 1120 será preenchido de acordo com os dados informados na tabela safx313 Movimentação Financeiras, com os critérios de seleção especificados na regra do registro 1100\.

Nível hierárquico \- 5

Ocorrência – 1:N

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN1120\-01__

__Campo 10 \- CNPJ\_ORIGEM__

Preencher com o campo 34 \- CNPJ\_ORIGEM da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não Obrigatório

__\[MFS748247\] __Tratamento do campo para atender os registros com 14 posições\.

Incluir os registros referentes ao CNPJ quando for o caso, na SAFX313 utiliza o mesmo campo para inserir informações de CPF campo 12, carregar as informações dos registros contendo 14 posições\.

__RN1120\-02__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 12 \- CPF\_ORIGEM__

Preencher com o campo 34 \- CNPJ\_ORIGEM da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não Obrigatório

Incluir os registros referentes ao CPF quando for o caso, na SAFX313 utiliza o mesmo campo para inserir informações de CNPJ campo 10, carregar as informações dos registros contendo 11 posições\.

__RN1120\-03__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 13 \- ID\_SELLER__

Preencher com o campo 45 \- ID\_SELLER da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

*“O Campo *__*ID\_SELLER do registro 1120*__* é de preenchimento obrigatório, e não foi informado\.”*

# <a id="_Toc128596034"></a>Registro 1200 – Cancelamento Extemporâneo

__RN1200__

__\[MFS878928\] __Alteração da regra da geração do registro de acordo com o campo 03\-COD\_FIN do registro 0000

Este registro deve ser gerado para informar as transações de períodos anteriores, que foram canceladas no período e que o campo “Finalidade do Arquivo” da tela de geração,  for igual a “1 \- Remessa de arquivo Normal”\.  Para os demais tipos de finalidade, o registro não deve ser gerado\.

As informações geradas no registro, são recuperadas a partir da SAFX313 – Movimentação Financeira, seguindo os critérios abaixo:

__Critério de Seleção:__

\- Código da empresa = código da empresa da geração 

\- Código do estabelecimento = código do estabelecimento da geração 

\- Data de Cancelamento pertencente ao período da geração

\- Data de Operação \(campo DT\_OP\) anterior ao período da geração

\- Situação da Operação \(campo SITUACAO\) = ‘S’ – Cancelada

\- Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) <> 9 e 10

\- Indicador para Não Gerar Registros 1100 e 1500 \(campo ind\_não\_gera\_1100\_1500\) <> ‘S’ __\[MFS436281\]__

__\[MFS436200\]__

\- Quanto ao parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” da Tela de Geração: 

  Se o parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” for marcado, então:

    As transações de Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) igual a 3, 4, 6, 8 não devem ser consideradas nesse registro\.

  Se o parâmetro “Gerar as Naturezas 3, 4, 6, 88 nos registros 1500 e 1600” for desmarcado, então:

    As transações de Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) igual a 3, 4, 6, 8 devem ser consideradas nesse registro\.

  As demais Natureza de Operação de Pagamento \(IND\_OPER\_NAT\_PAG\) devem ser consideradas, independente do parâmetro marcado ou desmarcado\. 

__Regra de Consolidação: __

__\[MFS710763\]  Ajuste na Regra de Consolidação__

Recuperar os movimentos da SAFX313 segundo os critérios acima, agrupar os movimentos gerando um registro 1200 para o conjunto de campos a seguir:

\- Campo 02 – COD\_IP\_PAR

\- Campo 03 – COD\_CLIENTE

\- Campo 04 – COD\_MCAPT

\- Campo 05 – NSU

\- Campo 06 – COD\_AUT

\- Campo 07 – ID\_TRANSC

\- Campo 08 – DT\_OP

\- Campo 09 – DT\_CANC

\- Campo 10 – TIPO\_CANC

\- Campo 13 – NAT\_OPER

\- Campo 14 \- IND\_NAT\_JUR

\- Campo 15 \- IND\_TP\_PIX

Somar os campos de Valor

\- Campo 11 \- VL\_ORIG 

\- Campo 12 \- VL\_CANC 

 

Nível hierárquico – 2

Ocorrência – 1:N \(1 por cancelamento\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN1200\-01__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 13 \- NAT\_OPER__

Preencher com o campo 21 \- IND\_OPER\_NAT\_PAG da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__RN1200\-02__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 14 \- IND\_NAT\_JUR__

Preencher com o campo 36 \- IND\_NAT\_JUR da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não Obrigatório

__RN1200\-03__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 15 \- IND\_TP\_PIX__

Preencher com o campo 37 \- IND\_TP\_PIX da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não Obrigatório

__RN1200\-04__

__\[MFS710763\] Campo obrigatório e ajuste para receber em caso de campo em branco a informação do campo 04 ID\_TRANSAC__

__A partir da Versão do Layout 10 inserir mensagem de log, campo obrigatório\.__

__Campo 06 – COD\_AUT__

Preencher com o campo 15 \- COD\_AUT da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Caso o campo esteja vazio emitir a mensagem de Log:__

*“O Campo COD\_AUT \(Código de Autorização\) do Registro 1115 é de preenchimento obrigatório, e não foi informado\.”*

__Inserir na a seguinte condição:__ Quando o campo estiver em branco, incluir a informação do campo 16 – ID\_TRANSAC da tabela X313\_DIMP\_MOV \(SAFX313\)

__RN1200\-05__

__\[MFS710763\] Campo obrigatório__

__A partir da Versão do Layout 10 inserir mensagem de log, campo obrigatório\.__

__Campo 07 – ID\_TRANSAC__

Preencher com o campo 16 \- ID\_TRANSAC da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Caso o campo esteja vazio emitir a mensagem de Log:__

*“O Campo ID\_TRANSAC \(Identificação da Transação\) do Registro 1115 é de preenchimento obrigatório, e não foi informado\.”*

# <a id="_Toc128596035"></a><a id="OLE_LINK1"></a>Registro 1220 – Cancelamento Transação de Intermediador

__RN1220__

__\[MFS878928\] __Alteração da regra da geração do registro de acordo com o campo 03\-COD\_FIN do registro 0000

O preenchimento do registro 1220 será preenchido de acordo com os dados informados na tabela SAFX313 \- Movimentação Financeiras, com os critérios de seleção especificados na regra do registro 1200\.  Este registro somente deve ser gerado quando o campo “Finalidade do Arquivo” da tela de geração, for igual a “1 \- Remessa de arquivo Normal”\.  Para os demais tipos de finalidade, o registro não deve ser gerado\.

  


__\[MFS710763\] __O registro 1220 passou de 1:1 para 1:N

__Regra de Consolidação:__

Recuperar os movimentos da SAFX313 e agrupá\-los segundo o registro pai \(1200\), mais os conjuntos de campos a seguir:

\- Campo 02 – UF\_DEST

\- Campo 03 – CHAVE\_NF

\- Campo 04 – CNPJ\_DEST

\- Campo 05 – CPF\_DEST

\- Campo 06 – ID\_DEST

\- Campo 07 – ID\_PEDIDO

Nível hierárquico \- 3

Ocorrência – 1:N \(1 por campo ID\_PEDIDO\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN1220\-01__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 07 \- ID\_PEDIDO __Preencher com o campo 38 \- ID\_PEDIDO da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

__Inclusão de Mensagem de Log   \- Caso o campo esteja vazio emitir a mensagem de Log:__

*“O Campo *__*ID\_PEDIDO do registro 1220*__* é de preenchimento obrigatório, e não foi informado\.”*

__RN1220\-02__

__\[ALTERAÇÃO\-__ __MFS877404\]__

__Recupera a UF do cadastro da SAFX04__

__Recuperar a informação do campo 25 – UF\_DESTINO da tabela safx313__

# <a id="_Toc128596036"></a>Registro 1500 – Resumo Mensal Das Operações Financeiras

__RN1500__

__\[MFS436200\] Criação do registro em atendimento ao ATO COTEPE 81/22 que altera ATO COTEPE 65/18, válido a partir do layout versão 09 \(Abril/2023\)\. __

Este registro deve ser gerado para informar as transações mensais totalizadas por COD\_IP\_PAR \+ COD\_CLIENTE \+ IND\_COMEX \+

IND\_EXTEMP \+ PERIODO \+ COD\_MCAPT \+ NAT\_OPER\+ IND\_NAT\_JUR \+ IND\_TP\_PIX\.

Deve ser gerado a partir do layout versão 09 \(válido a partir de Abril de 2023\)\. 

As informações geradas no registro, são recuperadas a partir da SAFX313 – Movimentação Financeira, seguindo os critérios abaixo:

__\[MFS532335\] __

Não podem ser informados dois ou mais registros com a mesma combinação de valores dos campos:

COD\_IP\_PAR \+ COD\_CLIENTE \+ IND\_COMEX \+ IND\_EXTEMP \+ PERIODO \+ COD\_MCAPT \+ NAT\_OPER\+ IND\_NAT\_JUR \+ IND\_TP\_PIX\.

__Critério de Seleção:__

\- Código da empresa = código da empresa da geração 

\- Código do estabelecimento = código do estabelecimento da geração 

\- Data de liquidação \(DT\_LIQUIDACAO\) no período da geração

\- Para transações ocorridas no período da geração:

- Data de operação \(campo data\_oper\) no período da geração __E__
- Finalidade do Arquivo = qualquer opção __E __
- Indicador de Informação Extemporânea \(campo IND\_EXTEMP\) = ‘0’ – não  

\- Para transações ocorridas no período anterior da geração:

- Data de operação \(campo data\_oper\) < período informado na geração __E__
- Finalidade do Arquivo = ‘01’ \(Normal\) __E__ 
- Indicador de Informação Extemporânea \(campo IND\_EXTEMP\) = ‘1’ \- sim  

\- Situação da Operação \(campo SITUACAO\) = ‘N’

\- Indicador para Não Gerar Registros 1100 e 1500 \(campo ind\_não\_gera\_1100\_1500\) <> ‘S’ 

\- Natureza de operação de pagamento \(campo ind\_oper\_nat\_pag\) = 3, 4, 6, 8

\- Parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” da Tela de Geração = ‘S’ \(marcado\)

__Verificação se o Cliente da transação é Pessoa Física ou Jurídica:__

Se for Pessoa Física, deve atender aos dois critérios a seguir:

  

 \- Valor Total de todas as transações do cliente \(mesmo CFP\) deve ser __IGUAL__ ou __SUPERIOR__ a 3\.375,00\.  

      __\[MFS516559__: substituir o valor fixo 3\.375,00 pelo campo Valor Total Mensal da tela de Parâmetros > Dados Iniciais\]

__\[MFS710763\] – __Nos casos da finalidade 3 \(Remessa de arquivo para atender intimação\) e informações extemporâneas o limite mínimo de valores não se aplica\. 

Desconsiderar a Regra acima quando:

Quando a opção de seleção da finalidade for igual à 03 

__OU__ quando o campo campo IND\_EXTEMP da tabela SAFX313 for igual a “1” 

Deve\-se enviar o valor da transação sem limite\.

    __E__

   \- Quantidade total das Transações do cliente \(mesmo CPF\) deve ser __IGUAL__ ou __SUPERIOR__ a 30\.

      __\[MFS516559__: substituir o valor fixo 30 pelo campo Quantidade de Transações da tela de Parâmetros > Dados Iniciais\] 

__\[MFS710763\] – __Nos casos da finalidade 3 \(Remessa de arquivo para atender intimação\) e informações extemporâneas o limite mínimo de quantidade não se aplica\. 

Desconsiderar a Regra acima quando:

Quando a opção de seleção da finalidade for igual à 03 

__OU__ quando o campo campo IND\_EXTEMP da tabela SAFX313 for igual a “1” 

Deve\-se enviar o valor da transação sem limite\.

  

Se for Pessoa Jurídica, as transações devem ser consideradas independente dos totais de valores e quantidades\.

__Geração dos campos de valores:__

Para os campos Valor total das operações \(campo 11\-VLR\_TOT\) e Quantidade de operações \(campo 12\-QTD\_TOT\) 

deve ser feita a somatória de todas as transações conforme o critério informado\.

__\[MFS520144\]__

__Cenário de intimação \(campo Finalidade do arquivo = ‘3’\)__

Na geração do arquivo com finalidade = ‘3’, além dos critérios acima também devem ser considerados os critérios informados abaixo:

\- Versão do Layout” igual ou superior a 09;

\- Processo Admin/Fiscal da Intimação” preenchido;

\- Código do Cliente \(campo COD\_CLIENTE\) = código informado no campo Código do Cliente;

\- Deve ser gerado registro 1500 para cada transação ocorrida no período informado conforme regra já existente;

\- Para o mês em que __NÃO__ ocorrer transação, deve ser gerado UM registro 1500 com os campos de valor e quantidade = ZERO\.

Nível hierárquico \- 2

Ocorrência \- 1:N

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

# <a id="_Toc128596037"></a>Registro 1600 – Cancelamento Extemporâneo Consolidado

__RN1600__

__\[MFS436202\] Criação do registro em atendimento ao ATO COTEPE 81/22 que altera ATO COTEPE 65/18, válido a partir do layout versão 09 \(Abril/2023\)\. __

Este registro deve ser gerado para informar as transações canceladas em períodos anteriores, que foram liquidadas no período, totalizando\-as por COD\_IP\_PAR \+ COD\_CLIENTE \+ PERIODO \+ COD\_MCAPT \+ NAT\_OPER\.

Deve ser gerado a partir do layout versão 09 \(válido a partir de Abril de 2023\)\. 

As informações geradas no registro, são recuperadas a partir da SAFX313 – Movimentação Financeira, seguindo os critérios abaixo:

__Critério de Seleção:__

\- Código da empresa = código da empresa da geração 

\- Código do estabelecimento = código do estabelecimento da geração 

\- Data de Cancelamento pertencente ao período da geração

\- Data de liquidação \(DT\_LIQUIDACAO\) anterior ao período da geração 

\- Situação da Operação \(campo SITUACAO\) = ‘S’ \- Cancelada

\- Indicador para Não Gerar Registros 1100 e 1500 \(campo ind\_não\_gera\_1100\_1500\) <> ‘S’ 

\- Natureza de operação de pagamento \(campo ind\_oper\_nat\_pag\) = 3, 4, 6, 8

\- Parâmetro “Gerar as Naturezas 3, 4, 6, 8 nos registros 1500 e 1600” da Tela de Geração = ‘S’ \(marcado\)

\- Finalidade do Arquivo = ‘1’ – Normal

Nível hierárquico – 2

Ocorrência – 1:N \(1 por cancelamento\)

Para consultar as regras dos campos, verificar o documento DIMP\_DEPARA\.xlsx\.

__RN1600\-01__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 08 \- QTD __Preencher com o campo 46 \- QTD\_CANCELAMENTO da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Obrigatório

*“O Campo *__*QTD \(Quantidade do Cancelamento\) do registro 1600*__* é de preenchimento obrigatório, e não foi informado\.”*

__RN1600\-02__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 09 \- IND\_NAT\_JUR __Preencher com o campo 36 \- IND\_NAT\_JUR da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não Obrigatório

__RN1600\-03__

__\[MFS748247\] Inclusão de novo campo__

__Este campo deve ser gerado a partir da Versão do Layout 10\.__

__Campo 10 \- IND\_TP\_PIX __Preencher com o campo 37 \- IND\_TP\_PIX da tabela X313\_DIMP\_MOV \(SAFX313\)

Campo Não  Obrigatório

= = = = = =

