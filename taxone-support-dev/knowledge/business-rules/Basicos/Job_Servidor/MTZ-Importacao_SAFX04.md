# MTZ-Importacao_SAFX04

- **Fonte:** MTZ-Importacao_SAFX04.docx
- **Modificado:** 2026-03-13
- **Tamanho:** 62 KB

---

#  SAFX04

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga à Execução

\- Importação à Execução

\- Importação Batch à Programação à Execução

\- Exportação Dados à Execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3464

 novo campo Alvará

Esta OS tem como objetivo criar o novo campo Alvará na SAFX04, referente ao cadastro de Alvará do Estabelecimento\.

OS3405

DW \- BASICOS \- JOB SERVIDOR \- Inclusão de Rotina de validação de Inscrição Estadual no momento da importação das SAFX

O objetivo deste requisito é permitir que a importação as SAFX04 possa realizar a validação do campo Inscrição Estadual\. A tela de manutenção de pessoas físicas/jurídicas também deve realizar essa validação\.

CH394\_2012

Prefixo de arquivo

Correção do tratamento com prefixo de arquivo na importação batch

OS3537\-B

DW \- MUNICIPAL \- ISS \- PORTO ALEGRE \- Ajuste da regra do campo Matricula da obra de Serviços Tomados e atendimento a situação de CPOM\.

Incluir o campo CPOM – Cadastro de Prestadores de Serviços de Outros Municípios no processo de importação da SAFX04\.

OS\-3704

SAFX04 – Validação do campo CEP\.

Regra para o novo parâmetro criado para inibir a crítica de validação do campo CEP\.

OS2706

DW \- ESPECÍFICOS \- Atendimento a Resolução ANP n° 17 \- DPMP \- Modelo de Dados

Incluir o campo Código de Instalação 2 em atendimento a obrigação ISIMP\.

OS4296

DW \- ESPECIFICOS \- I\-SIMP \- Melhoria para atualização do campo Código de Instalação 02 do cadastro de Pessoa Fisica/Juridica\.

Ajuste do campo Código de Instalação 2\.

OS4514

Atualizações para atender às necessidade do e\-Social

Criação de novos campos que serão utilizados para atender às necessidades do e\-Social\.

OS4665

Inclusão de novo campo data para atender às necessidades do NFTS\.

Criação de novo campo data, que será utilizado para atender às necessidades do NFTS, referente a prestadores novos\.

OS4682

Inclusão de nova opção no campo Classe de Pessoa Física Jurídica

Este documento tem como objetivo incluir nova opção “Exig\. Suspensa/Proced Adm” no campo Classe de Pessoa Física Jurídica\.

CH5445\_2015

Tratamento Importação Batch

Este documento tem como objetivo incluir tratamento para variações na nomenclatura do arquivo a ser importado via batch\.

MFS1650

Inclusão do novo campo Pessoa Fís/Jur – Perfil Seguradoras

Este documento tem como objetivo incluir novo campo chamado “Indicação de Inclusão no Processo Conciliação de NFS de Corretores no Gerenciador de ISS”, para utilizar no processo do Gerenciador de ISS\.

MFS8789

Ajuste no tamanho do campo CEI para atender ao REINF

Para atender o REINF, foi ajustado o tamanho do campo CEI\.

MFS614

Criação de novo campo Bairro 

Alteração da SAFX04 para criação de novo campo Bairro com 60 posições, a ser utilizado nas obrigações fiscais do SPED\.

MFS11786

Inclusão de valores no campo Classe de Pessoa Física Jurídica

Esse alteração consiste em atualizar os valores do campo Classe de Pessoa Física Jurídica\.

MFS11593

Atendimento à Portaria CAT 156/2010

Criação de novos campos p/atendimento à Portaria CAT 156/2010 \(campos CONTATO e ENDEREÇO NA WEB\)\.

MFS15147

Alterações p/o eSocial \(07/12/2017\)

Criação dos campos 66, 67 e 68 \(ver __RN66, RN67__ e __RN68__\)\.

MFS22135

Alterações p/o eSocial

Criação do Campo CPF do Proprietário da Fazenda SP \(São Paulo\) para atender o evento S\-1250 do eSocial

MFS16653

Criação de novos campos reservados

Criação de 8 novos campos Reservados\.

MFS\-26563

Criação de campo 

Criação do campo “Informações sobre Isenção e Imunidade”, para atender o evento R\-4020 do REINF

MFS\-29334

Alteração no tamanho de campo

Alteração do tamanho \(de 50 para 60\) do campo Endereço Eletrônico \(campo 40 \- E\_MAIL da SAFX04\)\.

Esta alteração impacta as funcionalidades de carga, importações e exportação da SAFX04\.

MFS31253

Criação de campo

Criação do campo Contribuinte ICMS\.

MFS36731

Andréa Rocha/Liliane Assaf

Alteração da validação do campo CEP

MFS72456

Andréa Rocha

Incluir nova opção “CEPOM” no campo Classe de Pessoa Física Jurídica\.

MFS\-79890

Alessandra Cristina Navatta

Criação do campo Sociedade Civil \(atendimento ao REINF versão 2\.1\)

MFS\-90001

Alessandra Cristina Navatta

Exclusão do campo Sociedade Civil \(atendimento ao REINF versão 2\.1\.1\)

MFS525312

Andréa Rocha

Alteração da validação dos campos CEP quando a UF=”EX”

MFS591904

Graciela Soares

Inclusão de Novos Campos – Atendimento Claro \- NFCom 

MFS741454

Liliane Assaf

Inclusão da validação do CNPJ Alfanumérico “MTZ\-Regra de Validação do CNPJ\.docx”

MFS981990

Liliane Assaf

Novos campos \(itens 94 a 98\) para atendimento ao Ato Cotepe ICMS 52/15\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para Importação Programada e Batch:__

__Tratamento Geral:__

- O arquivo deve ter a extensão TXT\-txt\.
- O arquivo SAFX04ot deve ser considerado tanto na importação programada, quanto na importação batch, assim como é realizada a importação da SAFX04\.

__\[ALTERADA – CH5445\_2015\]__

__Tratamento Importação Batch:__

- Para verificação da nomenclatura do arquivo no diretório parametrizado na programação da importação, deve considerar o seguinte: PREFIXO \+ Nº SAFX ou PREFIXO \+ Nº SAFX \+ DATA;
- Para verificação da nomenclatura do arquivo no diretório parametrizado na programação da importação quando o Nº da SAFX for igual a 04, deve considerar o seguinte: PREFIXO \+ Nº SAFX \+ OT ou PREFIXO \+ Nº SAFX \+ OT \+ DATA\.

*Exemplo:*

j01804\.txt

j01804ot\.txt

j0180420050827\.txt

j01804\_20050827\.txt

j01804ot20050827\.txt

j01804ot\_20050827\.txt

__Atenção: __Nesse caso o underline “\_” não se aplica para importação batch, pois existe o parâmetro na tela de Execução chamado “Nome do Arquivo com Data” para verificar essa variação\.

__CH26930\_2012__

__CH5445\_2015__

__RN00__

__Prefixo de arquivo Importação Batch__

__Origem: __Básicos >> Job Servidor >> Importação Batch >> Prefixo de Arquivos\.

__\[ALTERADA – CH5445\_2015\]__

Quando existe prefixo de arquivo parametrizado para o estabelecimento em “Importação batch à Prefixos de Arquivos”, o sistema deve primeiramente procurar pelo arquivo com o nome do prefixo parametrizado, concatenado com o número da SAFX e no caso da SAFX04 considerar também se houver a variação “ot”\.

*Exemplos: *

- Procedimento padrão: Para o Prefixo: “001\_”, o nome do arquivo deverá ser: “001\_04\.txt”, onde “001\_” corresponde ao prefixo parametrizado pelo usuário e “04” corresponde ao número da SAFX\.
- Procedimento específico: No caso do número da SAFX = 04, pode aceitar a variação “ot” na nomenclatura, então para o Prefixo: “001\_”, o nome do arquivo deverá ser: “001\_04\.txt”, onde “001\_” corresponde ao prefixo parametrizado pelo usuário e “04” corresponde ao número da SAFX\.

Caso o sistema não encontre o arquivo com o nome do prefixo, então deve procurar pelo arquivo com nome padrão do sistema “safx04\.txt” e considerar este para a importação, no caso específico citado no exemplo anterior, aceitar também a variação “ot” que seria a “safx04ot\.txt”\.

__CH394\_2012__

__CH5445\_2015__

__RN06__

__Campo CPF\-CGC__

Nome: CPF\_CGC

Tipo Alfanumérico

Tamanho: 14

Validar o CNPJ podendo ser numérico ou alfanumérico de acordo com o Cálculo do Dígito Verificador, definido na matriz “MTZ\-Regra de Validação do CNPJ\.docx”

__MFS741454__

__RN32__

__Campo CPF/CNPJ \(Convênio ICMS 115\)__

Nome: CPF\_CNPJ\_INV

Tipo Alfanumérico

Tamanho: 14

Validar o CNPJ podendo ser numérico ou alfanumérico de acordo com o Cálculo do Dígito Verificador, definido na matriz “MTZ\-Regra de Validação do CNPJ\.docx”

__MFS741454__

__RN08__

__Regra p/ campo Inscrição Estadual__

Esse campo deve ser validado através da procedure VALIDA\_INSC\_ESTADUAL\.

__OS3405__

__RN20__

__Regra p/ importação on line e bacth da SAFX04__

__\[MFS525312\] __Alteração da regra do campo CEP para preeencher quando a UF = “EX”

Realizar as seguintes validações:

- 
	- Conversão de campo do tipo data
	- Conversão de campo do tipo numérico
	- Conversão de @ em nulo
	- Permitir preencher o campo CEP quando a UF= ‘EX’

\[OS\-3704 \- Alteração\]

__Parâmetro “Validar CEP\(X04\):”:__

__Se marcado \(default\) e o campo UF <> “EX”:__

               Validar se os 5 primeiros dígitos do CEP informado na SAFX04, Campo 20, existe na tabela de cadastro do Mastersaf \(TACES12\)\. Caso não exista apresentar seguintes mensagens:

- Para CEP inexistente na TACES12: *90666 \- CEP Inexistente\.*

 __\[MFS36731\] __: Melhoria na mensagem 91475

 Se a UF informada no campo 19 da SAFX04 for diferente da referenciada pelo Cep na Tabela de Cadastro do Mastersaf \(TACES12\), então:

*91475: CEP pertencente a Unidade da Federacao diferente da informada\.*

*Nº / Desc\. Campo Manual Layout = CEP \(Item 20\) \- UF \(item 19\)*

*Solução: Favor verificar se CEP informado no campo 20 da SAFX04 está completo com 8 dígitos e se a UF informada no campo 19 está compatível com CEP\.*

__Se desmarcado ou campo UF = “EX”::__ Não realizar a validação de CEP \(Campo 20 da SAFX04\), deixando assim de exibir a crítica citada acima, 90666\.

__\[MFS36731\] Observação sobre tamanho do campo CEP__

     Oficialmente o CEP possui tamanho igual a 8\.

__     __Mas o DW aceita que o CEP seja importado com menos de 8 dígitos\. Ou seja, o cliente pode informar apenas os 5 primeiros dígitos \(denominado aqui por “radical do CEP”\) ou o CEP completo com 8 dígitos \(radical \+ 3 dígitos finais\)\.

    A TACES12 contém os 5 primeiros digitos do CEP \(“radical do CEP”\)\.  

   Como existem CEPs iniciados por zeros, ao importar a TACES os zeros à esquerda não são gravados na tabela de Cadastro do CEP \(DWT\_CEP\)\. Exemplo: o código 07900 na TACES12 é gravado com 7900\. 

         

  Na importação da SAFX04 fazemos dois tratamentos para validação do CEP na tabela de cadastro do CEP \(TACES12\):

- Se o cliente escolheu informar apenas o radical do CEP, o código carregado no campo 20 \(CEP\) da SAFX04 possui até 5 digitos, então: 

Consultamos a tabela de cadastro do CEP \(TACES12\) com o código carregado no campo 20\.

- Se o cliente escolheu informar o CEP completo \(campo 20 com mais de 5 dígitos\), então:

Consultamos a tabela de cadastro do CEP \(TACES12\) com as 5 primeiras posições do código carregado no campo 20, tendo o cuidado de primeiro completar as 8 posições com zeros a esquerda\. 

__OS3464 / OS3704__

__MFS36731__

__MFS525312__

__RN57__

__Regra p/ campo CPOM – Cadastro de Prestadores de Serviços de Outros Municípios__

Incluir o campo CPOM – Cadastro de Prestadores de Serviços de Outros Municípios no processo de importação online e batch da tabela SAFX04\.

Se valor informado = ‘S’, marcar o flag\.

Se valor informado = ‘N’, desmarcar o flag\.

__OS3537\-B__

__RN57__

__Regra p/ campo Código da Instalação 2__

Preencher com o Código de Instalação 2 da Pessoa Física/Jurídica\. Deve ser preenchido de acordo com as informações da coluna COD\_INSTALACAO da TFIX86\.

__OS42__

__OS4296__

__RN05__

__Criação de campo__

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Indicador do Nº de Identificação Fiscal

Nome do Campo: A ser definido por A&D

Comentário: Indicativo do Número de Identificação Fiscal:

1 \- Beneficiário com NIF;

2 \- Beneficiário dispensado do NIF;

3 \- País não exige NIF

Tamanho: 001

Tipo: A

Validação do campo: o conteúdo informado deve ser igual a <1>, <2> ou <3>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador do Nº de Identificação Fiscal inválido\. Informe <1>, <2> ou <3>”\.

__OS4514__

__RN06__

__Criação de campo__

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: CAEPF

Nome do Campo: A ser definido por A&D

Comentário: CAEPF do Contribuinte

Tamanho: 015

Tipo: A

__OS4514__

__RN07__

__Criação de campo__

Obrigatoriedade: Não obrigatório

Item: A ser definido por A&D

Descrição: Data Início da Prestação do Serviço

Nome do Campo: A ser definido por A&D

Comentário:Indica a data de início da prestação de serviços de Novos Prestadores

Tamanho: 008

Tipo: A

__OS4665__

__RN08__

__Criação de campo__

Obrigatoriedade: Não obrigatório

Item: 26

Descrição: Classe de Pessoa Física Jurídica

Nome do Campo: IND\_CLASSE\_PFJ

__\[ALTERADA – OS4682\]__

Comentário: Informar de acordo com:

01 \- Pessoa Física

02 \- Cooperativa

03 \- Empresa Pública

04 \- Empresa Privada

05 \- Cooperativa de Transporte

06 \- Sociedade Profissional

07 \- Imune

08 \- Regime de Estimativa

09 \- Depósito/Decisão Judicial

10 \- Isento

11 \- Exig\. Suspensa/Proced Adm

12 – Empr\. da Adm\. Pública Direta/Indireta

13 – Inscrito no PRODEVAL

14 \- Inscrito no CEPOM

Tamanho: 002

Tipo: A

__OS4682__

__MFS11786__

__MFS72456__

__RN09__

__Campo Indicação de Inclusão no Processo Conciliação de NFS de Corretores no Gerenciador de ISS__

Campo de preenchimento *não* obrigatório\.

Quando informada, deve conter um dos seguintes valores: S ou N\. Caso contrário, o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*“Campo Indicação de Inclusão no Processo Conciliação de NFS de Corretores no Gerenciador de ISS”*

Quando não informado, será gravado o valor default = “N”\.

Comentário: Indica se a pessoa física / Jurídica cadastrada no sistema, possui perfil de Seguradoras ou não\. Selecionado indica que o cadastro é perfil de seguradoras e desabilitado indica que é um cadastro de outros segmentos\.

__MFS1650__

__RN10__

__Campo Alvará__

Preencher com o código do Alvará do estabelecimento

__OS3464__

__RN11__

__Campo CEI__

Obrigatoriedade: Não obrigatório

Tamanho: 015

Tipo: A

__MFS8789__

__RN12__

__Campo Bairro \(II\):__

__MFS614: __ Devido ao impacto em aumentar o tamanho do campo “15\-Bairro”, foi criado este novo campo com 60 posições, para ser utilizado, se preenchido, na geração das obrigações fiscais do SPED\.

Campo *não* obrigatório\.

__MFS614__

__RN13__

__Campo 64\-Contato:__

\(campo criado na MFS11593 p/a geração do meio magnético da Portaria CAT 156/2010\)

Campo não obrigatório\.

__MFS11593__

__RN14__

__Campo 65\-Endereço na web:__

\(campo criado na MFS11593 p/a geração do meio magnético da Portaria CAT 156/2010\)

Campo não obrigatório\.

__MFS11593__

__RN40__

__Campo Endereço Eletrônico__

Alterar a rotina de importação para contemplar a alteração do tamanho deste campo

Tabela: SAFX04

Item: 40

Nome do Campo: E\_MAIL

Descrição: Endereço Eletrônico

Tipo: A

Tamanho: 60

Não obrigatório\.

__MFS\-29334__

__RN66__

__Campo 66\-Código da Categoria do Trabalhador__:               \(campo criado na MFS15147\)

Campo de preenchimento *não* obrigatório\.

Quando preenchido, o conteúdo informado deve ser um código existente na “*Tabela de Categoria de Trabalhador – eSocial*”  __\(TACES66\)__\.

Caso o código informado não exista na TACES66, será gravada mensagem de erro padrão e o registro não será importado\.

__MFS15147__

__RN67__

__Campo 67\-Natureza da Atividade__:                                         \(campo criado na MFS15147\)

Campo de preenchimento *não* obrigatório\.

Quando preenchido, o conteúdo deve ser  = “1” ou “2”, conforme as opções abaixo:

1 \- Trabalho Urbano

2 \- Trabalho Rural

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão e o registro não será importado\.

__MFS15147__

__RN68__

__Campo 68\-Setor__:                                                                      \(campo criado na MFS15147\)

Campo de preenchimento *não* obrigatório\.

Quando preenchido, o conteúdo informado deve ser um código existente na Tabela de Setor \(SAFX2037\), considerando apenas os códigos do Grupo a ser utilizado \(Relacionamento Tabela x Grupo\), que é o mesmo Grupo utilizado p/a pessoa fis/jur a ser importada / alterada\. Além disso, o Setor precisa ser compatível com a validade da pessoa fis/jur\.

Assim, o Setor deve atender as seguintes condições:

\-Grupo – O Grupo a ser utilizado é o mesmo Grupo da Pessoa/Fis/Jur;

\- Validade Inicial <= Validade inicial da pessoa fis/jur;

\- Validade final nula ou >= validade inicial da pessoa fis/jur;

Caso o código informado não exista na SAFX2037, ou não seja válido em relação às datas de validade,  será gravada mensagem de erro padrão e o registro não será importado \(exemplo: “*Setor não existente ou inválido para a Pessoa Fis/Jur*”\)\.

__MFS15147__

__RN69__

__Campo CPF do Proprietário da Fazenda SP \(São Paulo\)__

Obrigatoriedade: Não obrigatório

Tamanho: 011

Tipo: A

Se informado o CPF, deve ser um CPF válido, caso o código informado não seja válido será gravada mensagem de erro e o registro não será importado: CPF do campo ‘CPF do Proprietário da Fazenda SP \(São Paulo\)’ inválido\.

__MFS22135__

__RN70__

__Campo Reservado 1__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 1

Descrição: DSC\_RESERVADO1

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN71__

__Campo Reservado 2__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 2

Descrição: DSC\_RESERVADO2

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN72__

__Campo Reservado 3__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 3

Descrição: DSC\_RESERVADO3

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN73__

__Campo Reservado 4__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 4

Descrição: DSC\_RESERVADO4

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN74__

__Campo Reservado 5__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 5

Descrição: DSC\_RESERVADO5

Tipo: A

Tamanho 50

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN75__

__Campo Reservado 6__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 6

Descrição: DSC\_RESERVADO6

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN76__

__Campo Reservado 7__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 7

Descrição: DSC\_RESERVADO7

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN77__

__Campo Reservado 8__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX07

Item: A ser agendado pelo A&D

Nome do Campo: Reservado 8

Descrição: DSC\_RESERVADO8

Tipo: N

Tamanho: 015V002

Comentário: Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

Não obrigatório\.

__MFS16653__

__RN78__

__Campo Informações sobre Isenção e Imunidade__

Alterar a rotina de importação para contemplar este campo

Tabela: SAFX04

__Tamanho:__ 1

__Tipo:__ N

Campo Não obrigatório

__Valores Válidos:__

1 \- Não isenta/não imune;

2\- Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art\. 12 da Lei nº 9\.532, de 10 de dezembro de 1997;

3\- Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art\. 15 da Lei nº 9\.532, de 1997\.

__MFS\-26563__

__RN79__

__Campo Contribuinte ICMS__

Campo *não* obrigatório\.

Quando preenchido, seu conteúdo deve ser:

\- 1 \(Contribuinte do ICMS\), 

\- 2 \(Contribuinte Isento de Inscrição no Cadastro de Contribuintes do ICMS\),

\- 9 \(Não Contribuinte\)\. 

Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*Campo Contribuinte ICMS inválido\. Preencher com 1, 2 ou 9*”\)\.

__MFS31253__

__RN81__

__\[EXCLUSÃO MFS\-90001\] Campo Excluído na versão do REINF 2\.1\.1 __

__Campo Sociedade Civil__

Campo *não* obrigatório\.

Tamanho: 1

Tipo: Alfanumérico

Quando preenchido, seu conteúdo deve ser:

\-1 \(Por pessoas físicas que sejam diretores, gerentes ou controladores da pessoa jurídica que pagar ou creditar os rendimentos \(contribuinte declarante\); 

\- 2 \(Por cônjuge ou por parente de primeiro grau das pessoas físicas a que se refere o item 1 acima\)

Caso contrário, o registro não será importado e será gravada uma mensagem de erro no log \(“*Campo Sociedade Civil inválido\. Preencher com 1 ou 2*”\)\.

__3__

__MFS\-79890__

__MFS\-90001__

__RN81__

__Campo 81 – Identificação do Destinatário Outros__

Obrigatoriedade: Não obrigatório

Descrição: Identificação do Destinatário Outros 

Nome do Campo: NUM\_ID\_OUTROS

Tamanho: 020

Tipo: A

Edita: Sim

__MFS591904__

__RN82__

__Campo 82 – Identificação do Assinante__

Obrigatoriedade: Não obrigatório

Descrição: Identificação do Assinante

Nome do Campo: COD\_ID\_ASSINANTE

Tamanho: 015

Tipo: A

Edita: Sim

__MFS591904__

__RN83__

__Campo 83 \- Tipo de Assinante__

Obrigatoriedade: Não obrigatório

Descrição: Tipo de Assinante

Nome do Campo: IND\_TP\_ASSINANTE

Tamanho: 002

Tipo: A

Edita: Não

Validação: Quando for preenchido, seu conteúdo deve ser:

1\-Comercial; 

2\-Industrial; 

3\-Residencial/Pessoa Física; 

4\-Produtor Rural; 

5\-Órgão da administração pública estadual e fundações e autarquias; 

6\-Prestador de serviço de telecomunicação;

7\-Missões Diplomáticas, Repartições Consulares e Organismos Internacionais; 

8\-Igrejas e Templos de qualquer natureza ; 

99\-Outros não especificados anteriormente

Ou estar em branco

Se o campo for preenchido com algum valor diferente, será gravada mensagem de erro padrão \(Verificar mensagem padrão\) e o registro não será importado\.

Validação do campo: o conteúdo informado deve ser igual a < Nulo >, <1> , <2>, <3>, <4>, <5>, <6>, <7>,  <8> ou <99>\. Caso seja informado um código diferente, retornar a mensagem: “Indicador do Tipo de Assinante inválido\. Informe <1> , <2>, <3>, <4>, <5>, <6>, <7>,  <8> , <99> ou deixar em branco\.

__MFS591904__

__RN84__

__Campo 84 \- Endereço de Entrega__

Obrigatoriedade: Não obrigatório

Descrição: Endereço de Entrega

Nome do Campo: ENDERECO\_ENTREGA

Tamanho: 060

Tipo: A

Edita: Sim

__MFS591904__

__RN85__

__Campo 85 – Número Entrega__

Obrigatoriedade: Não obrigatório

Descrição: Número Entrega

Nome do Campo: NUM\_ENDERECO\_ENTREGA

Tamanho: 060

Tipo: A

Edita: Sim

__MFS591904__

__RN86__

__Campo 86 – Complemento Entrega__

Obrigatoriedade: Não obrigatório

Descrição: Complemento Entrega

Nome do Campo: COMPL\_ENDERECO\_ENTREGA

Tamanho: 060

Tipo: A

Edita: Sim

__MFS591904__

__RN87__

__Campo 87 – Bairro Entrega__

Obrigatoriedade: Não obrigatório

Descrição: Bairro Entrega

Nome do Campo: BAIRRO\_ENTREGA

Tamanho: 060

Tipo: A

Edita: Sim

__MFS591904__

__RN88__

__Campo 88 \- Município Entrega__

Obrigatoriedade: Não obrigatório

Descrição: Município Entrega

Nome do Campo: COD\_MUNICIPIO\_ENTREGA

Tamanho: 005

Tipo: N

Edita: Não

Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela MUNICIPIO\. Se o código não existir na tabela, gravar a seguinte mensagem no log de importação e não gravar o registro: 90549 \- O Código do Município não está cadastrado ou com informação alfanumérica no código\.

__MFS591904__

__RN89__

__Campo 89 – CEP Entrega__

Obrigatoriedade: Não obrigatório

Descrição: CEP Entrega

Nome do Campo: CEP\_ENTREGA

Tamanho: 008

Tipo: N

Formatação do campo: Máscara de CEP

Edita: Sim

__MFS591904__

__RN90__

__Campo 90 \- UF Entrega __

Obrigatoriedade: Não obrigatório

Descrição: UF Entrega

Nome do Campo: UF\_ENTREGA

Tamanho: 002

Tipo: A

Edita: Não

Caso o campo esteja preenchido no arquivo, validar seu conteúdo na tabela ESTADO\. Se o código não existir na tabela Campo “COD\_ESTADO”, gravar a seguinte mensagem no log de importação e não gravar o registro: 90027 \- O Codigo da Unidade da Federacao é invalido

__MFS591904__

__RN91__

__Campo 91 \- DDD Tel\. Entrega__

Obrigatoriedade: Não obrigatório

Descrição: DDD Tel\. Entrega

Nome do Campo: DDD\_ENTREGA

Tamanho: 005

Tipo: A

Edita: Sim

__MFS591904__

__RN92__

__Campo 92 \- Telefone Entrega __

Obrigatoriedade: Não obrigatório

Descrição: Telefone Entrega

Nome do Campo: TELEFONE\_ENTREGA

Tamanho: 010

Tipo: A

Edita: Sim

__MFS591904__

__RN93__

__Campo 93 – E\-mail Entrega__

Obrigatoriedade: Não obrigatório

Descrição: E\-mail Entrega

Nome do Campo: EMAIL\_ENTREGA

Tamanho: 060

Tipo: A

Edita: Sim

__MFS591904__

__RN94__

__Campo 94 \- Tipo de Unidade \(Injetora ou apenas Consumidora de Energia Elétrica\)__

Obrigatoriedade: Não obrigatório

Descrição: Tipo de Unidade \(Injetora ou apenas Consumidora de Energia Elétrica\)

Nome do Campo: IND\_TP\_UNID\_EE

Tamanho: 001

Tipo: A

__Lista de Valores Válidos:__

C – Consumidora

I \- Injetora

Validação do campo:

O campo IND\_TP\_UNID\_EE não é obrigatório, mas quando preenchido, deve ser um dos valores da lista\. 

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__93808 \- O campo Tipo de Unidade \(Injetora ou apenas Consumidora de Energia Elétrica\) deve ser preenchido com um valor valido\. Valores Validos: C, I\.__

MFS981990

__RN95__

__Campo 95 \- Código do Grupo do Titular \(Energia Elétrica\)__

Obrigatoriedade: Não obrigatório

Descrição: Código do Grupo do Titular \(Energia Elétrica\)

Nome do Campo: COD\_GRP\_TITULAR\_EEE

Tamanho: 014

Tipo: A

Sem validação

MFS981990

__RN96__

__Campo 96 \- Ordem de Prioridade de Compensação \(Energia Elétrica\)__

Obrigatoriedade: Não obrigatório

Descrição: Ordem de Prioridade de Compensação \(Energia Elétrica\)

Nome do Campo: NUM\_ORD\_COMP\_EE

Tamanho: 007

Tipo: N

Validação do campo:

O campo NUM\_ORD\_COMP\_EE não é obrigatório, mas quando preenchido, deve ser um valor numérico\. 

Quando o campo for preenchido com valor inválido, o registro não será importado e será gravada no log de erros: 

__90994 \- Erro na conversao de dados para numerico__\.

MFS981990

__RN97__

__Campo 97 \- Período de Referência de Entrada no Sistema de Compensação \(Energia Elétrica\)__

Obrigatoriedade: Não obrigatório

Descrição: Período de Referência de Entrada no Sistema de Compensação \(Energia Elétrica\)

Nome do Campo: DAT\_REF\_ENT\_EE

Tamanho: 008

Tipo: N

Validação do campo:

O campo DAT\_REF\_ENT\_EE deve ser uma data válida no formato AAAAMMDD\. 

Quando o campo for preenchido com informação que não é uma data válida, o registro não será importado e será gravada no log de erros: 

__93809 – Período de Referência de Entrada no Sistema de Compensação invalido__

O campo DAT\_REF\_ENT\_EE deve ser igual ao último dia do mês\. 

Quando o campo não corresponder ao último dia do mês, o registro não será importado e será gravada no log de erros: 

__93810 – Período de Referência de Entrada no Sistema de Compensação deve ser igual ao ultimo dia do mês__

MFS981990

__RN98__

__Campo 98 \- Período de Referência da Saída do Sistema de Compensação \(Energia Elétrica\)__

Obrigatoriedade: Não obrigatório

Descrição: Período de Referência da Saída do Sistema de Compensação \(Energia Elétrica\)

Nome do Campo: DAT\_REF\_SAI\_EE

Tamanho: 008

Tipo: N

Validação do campo:

O campo DAT\_REF\_SAI\_EE deve ser uma data válida no formato AAAAMMDD\. 

Quando o campo for preenchido com informação que não é uma data válida, o registro não será importado e será gravada no log de erros: 

__93811 – Período de Referência de Saída no Sistema de Compensação invalido__

O campo DAT\_REF\_SAI\_EE deve ser igual ao último dia do mês\. 

Quando o campo não corresponder ao último dia do mês, o registro não será importado e será gravada no log de erros: 

__93812 – Período de Referência de Saída no Sistema de Compensação deve ser igual ao ultimo dia do mês__

MFS981990

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

