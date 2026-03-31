# MTZ-Geracao_Meio_Magnetico_Anexos_Grupo_III-Policia_Federal

- **Fonte:** MTZ-Geracao_Meio_Magnetico_Anexos_Grupo_III-Policia_Federal.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 40 KB

---

# Módulo Substâncias Controladas  

# Atendimento – Polícia Federal – Geração Meio Magnético \- Anexos Grupo III

__Localização__: Menu Específicos, Módulo Substâncias Controladas, item Atendimento 🡪Polícia Federal 🡪 Geração em Meio Magnético – Anexos Grupo III

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data de Alteração__

OS3976\-G

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS \- Correção na geração do Polícia Federal onde registro MR que deve ser considerada pela Data Emissão

Este documento tem como objetivo permitir a geração para atendimento à Polícia Federal através da Data de Emissão da nota fiscal\.

04/04/2013

CH27589\-A\_2013

DW \- ESPECÍFICOS \- SUBSTÂNCIAS CONTROLADAS – Gravação do CAMPO DIA dos registros MV e MR

Tratamento na gravação do campo DIA dos registros MV e MR\.

11/11/2013

OS4532

Alteração na geração dos saldos iniciais

Incluído parâmetro na tela da geração para possibilitar que os saldos iniciais sejam transportados dos resultados do mês anterior \(vide RN01, RN04 e RN05\)\. 

20/08/2014

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra para tela de geração do Meio Magnético – Anexos Grupo III:__

Ao clicar no menu Atendimento > Polícia Federal > Geração Meio Magnético – Anexos Grupo III, o sistema deve exibir a tela de seleção conforme abaixo, com o seguinte campo, além dos campos já existentes: 

Recuperar informações por: 

Exibir campo no formato radio Button com as seguinte opções: Data Movimento e Data Emissão\. A opção Data Movimento deve estar marcada por default\.

Alteração da __OS4532__ \(inclusão do parâmetro SALDO INICIAL\)

__Saldo Inicial__ – Este campo apresenta duas opções para o usuário escolher como gerar os saldos iniciais: 

                                                 \(  \)  __Transportar saldo final do mês anterior__

                                                 \(  \)  __Apurar saldos a partir da SAFX72__

A opção “Transportar saldo final do mês anterior” sempre aparecerá marcada por default\.

As duas opções são alternativas, e desta forma, somente uma pode ser selecionada\. Ao selecionar uma das opções, a outra será automaticamente desmarcada\. 

Quando a opção escolhida for = “Transportar saldo final do mês anterior” o campo “__Data dos Saldos__” será automaticamente limpo e permanecerá desabilitado\.

Quando a opção escolhida for = “Apurar saldos a partir da SAFX72”, o campo “__Data dos Saldos__” será habilitado para alteração do usuário\.

__Data dos Saldos __– Este campo será habilitado *apenas* quando a opção escolhida para o saldo inicial for = “Apurar saldos a partir da SAFX72”, e neste caso o usuário informará a data para a recuperação dos saldos na tabela\.

 

Sempre que a opção escolhida para o saldo inicial for = “Transportar saldo final do mês anterior” este campo será limpo e permanecerá desabilitado\.

OS3976\-G

OS4532

__RN02__

__Regra Geral para recuperação dos dados:__

A geração deve recuperar as informações da tabela X70\_MOV\_SUBST\_CONT através da seguintes informações:

- Se o campo Recuperar informações por estiver marcado como Data Movimento:

        O campo DATA\_MOVTO deve estar dentro do mês/ano referencia informado na tela de geração\.

Se o campo Recuperar informações por estiver marcado como Data Emissão:

        O campo DATA\_EMISSAO deve estar dentro do mês/ano referencia informado na tela de geração\.

- Tipo de Obrigação = “PF“
- Empresa igual a selecionado na Manager
- Estabelecimento igual ao escolhido na tela de geração

OS3976\-G

__RN03__

__Registro MV/MR: CAMPO DIA__

Gravar a informação do campo DATA\_MOVTO de acordo com a parametrização prevista na RG00, ou seja, se o parâmetro estiver marcado como Data Movimento\.

OU

Gravar a informação do campo DATA\_EMISSAO de acordo com a parametrização prevista na RG00, ou seja, se o parâmetro estiver marcado como Data Emissão\.

CH27589\-A\_2013

__RN04__

__Tratamento dos Saldos Iniciais__

__OS4532__: Originalmente, os saldos iniciais eram sempre apurados na SAFX72, mas a partir da OS4532 foi criado o parâmetro “Saldo Inicial” para possibilitar que os saldos iniciais sejam transportados automaticamente dos resultados do mês anterior\.

Os saldos iniciais de cada classificação de produto \(campo “__Qt\. Est\. Ant”__\) são gerados dependendo do parâmetro “Saldo Inicial”, da seguinte forma:

 __Se__ parâmetro = __*“Transportar saldo final do mês anterior*”__:

       Neste caso, os saldos iniciais *de cada classificação de produto* serão transportados do mês anterior \(campo “__Qt\. Est\. Atual__”\)\.

       Para recuperar os saldos de cada classificação de produto armazenados na geração do mês anterior, considerar os seguintes

       critérios:

            \-Código da Empresa = código da Empresa do login

            \-Código do Estabelecimento = código do estabelecimento em processamento

            \-Mês e Ano de Referência = *deve ser o mês/ano anterior ao mês/ano da geração* 

            \-Tipo da Obrigação = “PF” \(Polícia Federal\)

            \-Classificação do Produto = código de classificação do produto

       No caso das classificações de produtos para as quais *não* seja identificado saldo no mês anterior, deve ser considerado saldo

       inicial = zero\.

        *IMPORTANTE*:

         \- As classificações que tiverem movimentação de produtos, mas *não* tiverem registro de saldo no mês anterior, serão gravadas

           com saldo inicial = zero \(*conforme procedimento já feito originalmente*\); 

         \- As classificações que tiverem registro de saldo no mês anterior, mas *não* tiverem movimentação de produtos, serão gravadas

           com o saldo inicial, e com todos os tipos de movimentação = zero \(*conforme procedimento já feito originalmente*\); 

__Se__ parâmetro = __*“Apurar saldos a partir da SAFX72*”__:

       Neste caso, os saldos iniciais *de cada classificação de produto* serão apurados com base na tabela SAFX72, considerando os

       produtos parametrizados para a classificação \(conforme o procedimento original da geração, onde os saldos são recuperados da

       tabela SAFX72 utilizando o parâmetro de tela “Data dos Saldos”\)\.

 

       No caso das classificações de produtos para as quais *não* exista saldo registrado na SAFX72, deve ser considerado saldo inicial =

       zero\.

        IMPORTANTE*:*

        \- As classificações que tiverem movimentação de produtos, mas *não* tiverem registro de saldo na SAFX72, serão gravadas com

           saldo inicial = zero \(*conforme procedimento já feito originalmente*\); 

        \- As classificações que tiverem registro de saldo na SAFX72, mas *não* tiverem movimentação de produtos, serão gravadas com o

          saldo inicial, e com todos os tipos de movimentação = zero \(*conforme procedimento já feito originalmente*\); 

OS4532

__RN05__

__Tratamento dos Saldos Finais: __

__OS4532__: A partir desta OS, os saldos finais calculados passaram a ser armazenados internamente, para possibilitar que sejam recuperados na geração do próximo mês, e transportados automaticamente\.

Os saldos finais apurados para cada classificação de produto \(campo “__Qt\. Est\. Atual__”\) serão armazenados internamente, considerando os critérios a seguir:

     \-Código da Empresa = código da Empresa do login 

     \-Código do Estabelecimento = código do estabelecimento em processamento 

     \-Mês e Ano de Referência = *mês e ano da geração* 

     \-Tipo da Obrigação = “PF” \(Polícia Federal\) 

     \-Classificação do Produto = código de classificação do produto

OS4532

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

