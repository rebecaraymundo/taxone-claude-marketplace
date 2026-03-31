# MTZ_OTF_DIRF-2012

- **Fonte:** MTZ_OTF_DIRF-2012.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 97 KB

---

# Obrigações de Tributos Federais \- DIRF 2012

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3528

Obrigações de Tributos Federais \- DIRF 2012

<a id="_Toc281404230"></a>Atualização da DIRF – Leiaute 2012 – Ano\-Calendário 2011 e 2012 \( no caso de situação especial\)\.

## Módulo: Obrigações de Tributos Federais

- Alteração dos campos “Ano Calendário” e “Ano Referência DIRF” do menu DIRF >> Geração DIRF para permitir a geração do arquivo no formato correto\.
- Quando o parâmetro “Extinção” da tela da Geração da DIRF for selecionado, o default dos campos Ano\-Calendário e Ano Referência\-DIRF serão “2012”,”2012”, caso contrário preencher com “2011”, “2012” respectivamente\.
- Inclusão do botão para pesquisar os estabelecimentos na tela ‘Geração DIRF\.
- Alterado o campo  “Valor Anual Mínimo de Rendimentos” para o valor default 23\.499,15\.
- Inclusão dos campos 5 – Indicador de beneficiário dispensado do Número de Identificação Fiscal – NIF e 6 \- Identificador de que o país não exige Número de Identificação Fiscal \- NIF no registro BRPDE
- Criação da Rendimentos Recebidos Acumuladamente, no Menu: DIRF
- Geração dos Registros RRA, BPFRRA, QTMESES e DAJUD na DIRF 2012\.

OS3267\-D

Obrigações de Tributos Federais – Geração da DIRF a partir dos Tributos Ajustados

Será desenvolvida uma rotina para que a geração da DIRF passe a considerar as novas tabelas da solução dada para a família de OS’s 3267\.

OS3753\-B

Obrigações de Tributos Federais \- DIRF 2012

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

A solução proposta foi a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”\. Esses campos identificam a retenção estornada e não permitem que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema\. Vale salientar que esses campos citados anteriormente foram criados na OS3753\. As rotinas do sistema que deverão ser alteradas são:

- __Obrigações Acessórias__
	- DARF
	- DCTF
	- __DIRF – OS3753\-B__
	- Informe de Rendimentos
- Relatórios Gerenciais
	- Relatório de Tributos Federais
	- Relatório de Rastreabilidade

Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago\. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente\. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido\.

Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:

- __Retenção sem DARF Gerado:__ nesse caso a retenção será atualizada sem maiores ônus\. 
- __Retenção com DARF Gerado e Não Pago:__ nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75\_DCTF apagar esse DARF\. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”\. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados\.
- __Retenção com DARF Pago:__ nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema\. 

É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais\. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento \(R11\) sem uma Ficha de Débito vinculada\.

O escopo da OS3753\-B é permitir que a obrigação acessória DIRF desconsidere as retenções da tabela de Controle de Tributos que estejam estornadas\.

#### Cód\.

### Descrição

### DR

# RNG\-01

Ao gerar os registros de retificações contidos na OS3267\-D, ou seja, quando as retenções a serem recuperadas serão da tabela X530\_RETIFICACAO\_IRRF mais recente e não da X53\_RETENCAO\_IRRF, vale salientar que independente da Data de Retificação da Retenção informada na tabela X530\_RETIFICACAO\_IRRF, os valores serão informados nos respectivos registros da DIRF __do mês da retenção da X53\_RETENCAO\_IRRF e não do mês da retificação__\. Nesse caso em que a retificação for recuperada, serão considerados somente os valores da retificação mais recente, sendo que as outras informações, serão consideradas da retenção original \(SAFX53\)\.

Caso a retificação mais recente possua uma Data de Retificação cujo ano seja subseqüente ao Ano\-Calendário da Retenção original, a mesma será recuperada e gerada na DIRF do ano\-calendário da retenção\.

Essa regra é existente devido à competência ser referente ao Pagamento Original que ocorreu para o Prestador\.

OS3267\-D

# RN00

Alterar na tela da ‘Geração DIRF ‘o valor default do campo “Ano Referência\-DIRF” de “2011” para “2012”\. Esse campo poderá ser alterado\.

OS3528

# RN01

Na tela da ‘Geração DIRF’ quando o parâmetro ‘Extinção’ for selecionado, o default dos campos Ano\-Calendário e Ano Referência\-DIRF serão “2012” e ”2012”, caso contrário preencher com “2011”, “2012” respectivamente\.

OS3528

# RN02

Incluir o botão para pesquisar os estabelecimentos na tela da ‘Geração DIRF’\. Os campos que estarão disponíveis para a pesquisa são Cod\_Estab e Descrição\.

OS3528

# RN03

Gravar no campo 1 – Identificador do Registro o valor fixo “Dirf”\.

OS3528

# RN04

Gravar no campo 2 – Ano referência a informação do campo “Ano\-Referência” da tela de geração da DIRF \(módulo: Obrigações de Tributos Federais, menu DIRF >> Geração DIRF\)\. 

OBS: as regras contidas nesse documento devem ser referentes ao ano referência “2012”\. Os outros ano\-referência devem ser gerados através dos outros layouts\.

OS3528

# RN05

Gravar no campo 3 – Ano\-calendário a informação do campo “Ano\-Calendário” da tela de geração da DIRF \(módulo: Obrigações de Tributos Federais, menu DIRF >> Geração DIRF\)\. Para tanto a informação deve estar preenchida com as opções “2011” ou “2012”\. 

OS3528

# RN06

Gravar no campo 4 – Indicador de Retificadora se a declaração é retificadora ou não\. Para identificar seguir a seguinte regra:

- Gravar “N” caso o campo “Tipo de Declaração” do menu DIRF >> Geração DIRF estiver selecionado com a opção “Original”\.
- Gravar “S” caso o campo “Tipo de Declaração” do menu DIRF >> Geração DIRF estiver selecionado com a opção “Retificadora”\.

OS3528

# RN07

Gravar no campo 5 – Número do Recibo a informação de acordo com as regras abaixo:

- Recuperar a informação do campo “Núm\. Recibo Última Declaração” do menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais\.

OS3528

# RN08

Gravar no campo 6 – Identificador de Estrutura do leiaute o valor fixo “1A4MA1R”\.

OS3528

# RN09

Gravar no campo 1 – Identificador do Registro o valor fixo “RESPO”\.

OS3528

# RN10

Gravar no campo 2 – CPF a informação que estiver contida no campo NUM\_CPF da tabela RESP\_INFORMACAO de acordo com o Representante Legal da Empresa informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN11

Gravar no campo 3 – Nome a informação que estiver contida no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN12

Gravar no campo 4 – DDD a informação que estiver contida no campo NUM\_DDD da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN13

Gravar no campo 5 – Telefone a informação que estiver contida NUM\_TELEFONE da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN14

Gravar no campo 6 – Ramal a informação que estiver contida NUM\_RAMAL da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais\.

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN15

Gravar no campo 7 – Fax a informação que estiver contida NUM\_FAX da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN16

Gravar no campo 8 – Correio Eletrônico a informação que estiver contida E\_MAIL da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN17

Gravar no campo 1 – Identificador do Registro o valor fixo “DECPJ”\.

OS3528

# RN18

Gravar no campo 2 – CNPJ a informação que estiver contida no campo CGC da tabela ESTABELECIMENTO de acordo com o\(s\) estabelecimento\(s\) selecionado\(s\) para a geração\.

OS3528

# RN19

Gravar no campo 3 – Nome empresarial a informação que estiver contida no campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO de acordo com o\(s\) estabelecimento\(s\) selecionado\(s\) para a geração\.

OS3528

# RN20

Gravar no campo 4 – Natureza do Declarante  a informação que estiver contida no campo “Natureza do Declarante” da tela de Formatação das Mídias da DIRF no menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídias\. As informações contidas devem ser gravadas da seguinte forma:

- Caso a opção selecionada seja “0 \- Pessoa jurídica de direito privado”, gravar “0”\.
- Caso a opção selecionada seja “1 \- Órgãos, autarquias e fundações da administração pública federal”, gravar “1”\.
- Caso a opção selecionada seja “2 \- Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal”, gravar “2”\.
- Caso a opção selecionada seja “3 – Empresa pública ou sociedade de economia mista federal”, gravar “3”\.
- Caso a opção selecionada seja “4 \- Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal”, gravar “4”\.
- Caso a opção selecionada seja “8 – Entidade com alteração de natureza jurídica \(uso restrito\)”, gravar “8”\.

As regras para a geração da DIRF cujo Ano\-Referência seja igual ou inferior a 2010, continuam iguais, ou seja, recuperam a informação do campo “Natureza da Informação” de acordo com o menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias\.

OS3528

# RN21

Gravar no campo 5 – CPF Responsável perante o CNPJ a informação que estiver contida no campo NUM\_CPF da tabela RESP\_INFORMACAO de acordo com o Responsável Legal informado no campo “Responsável Legal” dos seguintes menus:

- Caso o Ano\-Referência seja igual ou inferior a 2010 
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência até 2010 >> Formatação Mídias do módulo Obrigações de Tributos Federais\.
- Caso o Ano\-Referência seja 2011 em diante
	- Recuperar a informação pelo menu DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais

A regra é variável de acordo com o Ano\-Referência, visto que os layout’s são diferentes\.

OS3528

# RN22

Gravar no campo 6 – Indicador de Sócio Ostensivo responsável por sociedade em conta de participação – SCP a informação do campo “Sócio Ostensivo” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “N”\.
- Caso a opção selecionada seja “Sim”, gravar “S”\.

OS3528

# RN23

Gravar no campo 7 – Indicador de declarante depositário de crédito decorrente de decisão judicial a informação do campo “Declarante depositário de crédito decorrente de decisão judicial” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “N”\.
- Caso a opção selecionada seja “Sim”, gravar “S”\.

OS3528

# RN24

Gravar no campo 8 – Indicador de declarante de instituição administradora ou intermediadora de fundo ou clube de investimento a informação do campo “Declarante de instituição administradora ou intermediadora de fundo ou clube de investimento” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “N”\.
- Caso a opção selecionada seja “Sim”, gravar “S”\.

OS3528

# RN25

Gravar no campo 9 – Indicador de declarante de rendimentos pagos a residentes ou domiciliados no exterior a informação do campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “N”\.
- Caso a opção selecionada seja “Sim”, gravar “S”\.

OS3528

# RN26

Gravar no campo 10 – Indicador de plano privado de assistência à saúde – coletivo empresarial a informação do campo “Plano privado de assistência à saúde – coletivo empresarial” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso a opção selecionada seja “Não”, gravar “N”\.
- Caso a opção selecionada seja “Sim”, gravar “S”\.

OS3528

# RN27

Gravar no campo 11 – Indicador de situação especial da declaração a informação do campo “Extinção” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

- Caso o campo esteja marcado, gravar “S”\.
- Caso o campo esteja desmarcado, gravar “N”\.

OS3528

# RN28

Gravar no campo 12 – Data do evento a informação do campo “Data do evento” da tela de geração da DIRF – menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. A informação deve ser gravada no formato AAAAMMDD\.

OS3528

# RN29

Gravar no campo 1 – Identificador do Registro o valor fixo “IDREC”\.

OS3528

# RN30

Gravar no campo 2 – Código de Receita os códigos de receita de acordo com a regra abaixo:

- Caso a informação componha o registro BPFDEC – ou seja, seja originária da tabela X21\_FICHA\_FINANC, gravar a informação contida no campo “c/ Vínculo Empregatício” da tela de geração do meio magnético \(menu: DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.
- Caso a informação componha os registros BPFDEC ou BPJDEC – ou seja, seja originária da tabela X53\_RETENCAO\_IRRF e o Participante seja uma Pessoa Física ou Jurídica \(o que caracteriza uma retenção referente à uma prestação de serviço\), gravar o conteúdo do campo 11 \(COD\_DARF\) da mesma tabela X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF caso exista um registro nessa tabela, sendo o mais recente\.

OS3528

OS3267\-B

# RN31

Gravar no campo 1 – Identificador de Registro o valor fixo “BPFDEC”\.

As informações desse registro serão recuperadas das tabelas SAFX21 \(Ficha Financeira do Funcionário\) e SAFX53 \(Controle de Tributos – Retenções\)\. Para que as informações sejam recuperadas da SAFX53, serão recuperadas somente as retenções que pertençam a uma Pessoa Física\. Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente dessa tabela\.

Serão recuperados os Beneficiários a partir da SAFX21 cujo valor total de rendimentos anuais seja igual ou superior ao valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Caso os beneficiários recuperados sejam da SAFX53 \(o que caracteriza trabalho sem vínculo empregatício, de aluguéis ou royalties – ver o código de Retenção a partir do campo “s/ Vínculo Empregatício” – e também os Códigos de Retenção da SAFX53 \(campo 11 da SAFX53 = 3208\), considerar somente os valores pagos acima de R$ 6\.000,00 \(OBS: essa regra já existe na DIRF 2010\)\.

OS3528

OS3267\-D

# RN32

Gravar no campo 2 – CPF o CPF do Beneficiário\.

- SAFX21
	- Recuperar o CPF do Funcionário a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo 12 \(CPF\) da tabela SAFX15 e gravar a informação\.
- SAFX53
	- Recuperar o CPF da Pessoa Física a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da X530\_RETIFICACAO\_IRRF\. Com essa informação, recuperar o campo 06 \(CPF\_CGC\) da tabela SAFX04 e gravar a informação\.

OS3528

OS3267\-D

# RN33

Gravar no campo 3 – Nome o nome do beneficiário pessoa física\.

Caso a informação seja da SAFX53, 

- SAFX21
	- Recuperar o Nome do Funcionário a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo 05 \(NOME\) da tabela SAFX15 e gravar a informação\.
- SAFX53
	- Recuperar o Nome da Pessoa Física a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da X530\_RETIFICACAO\_IRRF\. Com essa informação, recuperar o campo 05 \(RAZAO\_SOCIAL\) da tabela SAFX04 e gravar a informação\.

OS3528

OS3267\-D

# RN34

Gravar no campo 4 – Data atribuída pelo laudo da moléstia grave a informação da Data de afastamento do funcionário\.

- SAFX21
	- Recuperar a Data atribuída pelo laudo da moléstia grave a partir do campo 03 \(COD\_FUNC\) da SAFX21\. Com essa informação, recuperar o campo “Data atribuída pelo laudo da moléstia grave” da tabela SAFX15 e gravar a informação\.
- SAFX53
	- Recuperar o Data atribuída pelo laudo da moléstia grave a partir dos campos 04 \(IND\_FIS\_JUR\) e 05 \(COD\_FIS\_JUR\) da SAFX53 ou IND\_FIS\_JUR/COD\_FIS\_JUR da X530\_RETIFICACAO\_IRRF\. Com essa informação, recuperar o campo “Data atribuída pelo laudo da moléstia grave” da tabela SAFX04 e gravar a informação\.

OS3528

OS3267\-D

# RN35

Devem ser recuperados os controles de tributos existentes na tabela X53\_RETENCAO\_IRRF desde que os mesmos sejam de Pessoas Jurídicas \(ver campos 04 e 05 da SAFX53 e verificar na tabela SAFX04 o campo CPF\_CGC que tenha 14 posições\)\. O campo “Tipo Lançamento” dessa tabela deve estar preenchido com a opção “Informações dos Beneficiários”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente dessa tabela\.

Deverão ser recuperados somente os beneficiários que forem PESSOA JURÍDICA\.

Gravar no campo 1 – Identificador do Registro o valor fixo “BPJDEC”\.

OS3528

OS3267\-D

# RN36

Gravar no campo 2 – CNPJ o CNPJ da Pessoa Jurídica \(ver campo 06 da tabela SAFX04\) de acordo com o campo de Pessoa Física/Jurídica do Controle de Tributos \(ver campos 04 e 05 da tabela SAFX53\)\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperado o CNPJ da Pessoa Jurídica referente ao registro mais recente dessa tabela\.

OS3528

OS3267\-D

# RN37

Gravar no campo 3 – Nome Empresarial a Razão Social da Pessoa Jurídica \(ver campo 05 da SAFX04\) de acordo com o campo de Pessoa Física/Jurídica do Controle de Tributos \(ver campos 04 e 05 da tabela SAFX53\)\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperada a Razão Social referente ao registro mais recente dessa tabela\.

OS3528

OS3267\-D

# RN38

Devem ser recuperados as fichas financeiras \(tabela X21\_FICHA\_FINANC\) e as retenções \(X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF\) dos funcionários e dos prestadores que estejam no período informado para a geração\. 

O campo “Tipo Lançamento” \(campo 11 da SAFX21 e 40 da SAFX53 ou X530\_RETIFICACAO\_IRRF\) deve estar selecionado com a opção “Informações dos Beneficiários”\.

No caso da SAFX53/X530\_RETIFICACAO\_IRRF deverão ser recuperados somente os beneficiários que forem PESSOA FÍSICA\.

As retenções da tabela X53\_RETENCAO\_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração da DIRF\. Vale salientar que essas retenções não possuem registros de retificação\.

Caso um funcionário ou prestador de serviços não possua valores para retenção de Imposto de Renda no período para nenhum mês ou Décimo Terceiro Salário, o mesmo não deverá ser informado\.

Gravar no campo 1 – Identificador do Registro a informação de acordo com as regras abaixo:

- Gravar o valor fixo “RTRT” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\. No caso da SAFX53, recuperar a informação a partir da somatória dos campos VLR\_BRUTO e VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “RTPO” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Oficial\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_INSS\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “RTPP” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Privada/FAPI\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PREV\_PRIVADA da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “RTDP” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Dependentes\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_DEP\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “RTPA” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Pensão Alimentícia\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PENS\_ALIMENT da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “RTIRF” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha na verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\. No caso da SAFX53, recuperar a informação do campo VLR\_IR\_RETIDO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.

OS3528

OS3267\-D

# RN39

Gravar no campo 2 – Janeiro o valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN40

Gravar no campo 3 – Fevereiro o valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN41

Gravar no campo 4 – Março o valor contido no campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN42

Gravar no campo 5 – Abril o valor contido no campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN43

Gravar no campo 6 – Maio o valor contido no campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN44

Gravar no campo 7 – Junho o valor contido no campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN45

Gravar no campo 8 – Julho o valor contido no campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN46

Gravar no campo 9 – Agosto o valor contido no campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN47

Gravar no campo 10 – Setembro o valor contido no campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN48

Gravar no campo 11 – Outubro o valor contido no campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN49

Gravar no campo 12 – Novembro o valor contido no campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN50

Gravar no campo 13 – Dezembro o valor contido no campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo 14 \(VLR\_BRUTO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo 15 \(VLR\_IR\_RETIDO\) da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN51

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 09 da SAFX21\. Para identificar o Décimo Terceiro Salário, o campo “Indicador Folha” da SAFX21 deve estar preenchido com a opção “Pagamento de 13º\. Salário”\. No caso da SAFX53/X530\_RETIFICACAO\_IRRF a informação deve ser recuperada da seguinte maneira:

- Para o registro RTRT: ver campo “Valor 13º\. Salário” da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
- Para os registros RTPO, RTPP, RTDP e RTPA ver os seguintes campos da SAFX53 ou X530\_RETIFICACAO\_IRRF\.
	- RTPO: campo VLR\_DED\_INSS\_TERC
	- RTPP: campo VLR\_PREV\_PRIVADA
	- RTDP: campo VLR\_DED\_DEP\_TERC
	- RTPA: campo VLR\_PENS\_ALIMENT
- Para o registro RTIRF: ver campo “Valor Tributo 13º\. Salário” da SAFX53 ou X530\_RETIFICACAO\_IRRF\.

OS3528

OS3267\-D

# RN52

Gravar no campo 1 – Identificador do Registro o valor fixo “RIL96”\.

OS3528

# RN53

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 09 da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Lucros e Dividendos\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

# RN54

Gravar no campo 1 – Identificador do Registro o valor fixo “RIO”\.

  
Este registro tem como origem de informação da tabela SAFX21 e SAFX53, podendo ser recuperados o conteúdo dos campos das duas tabelas\.

OS3528

# RN55

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 09 da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Outros\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Se a origem da informação for da tabela SAFX53/X530\_RETIFICACAO\_IRRF, o sistema deverá recuperar as informações da SAFX53 e somente nos casos em que o registro da SAFX53 possua uma ou mais retificações na X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente\. Após essa verificação, deverá ser recuperado do Valor de Outros Dirf \(campo 38 \- VLR\_OUTROS\_DIRF\), quando o Beneficiário for Pessoa Física e o valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

Porém, se o Beneficiário Pessoa Física não atinja o “Valor do Anual Mínimo de Rendimentos” e os demais registros possuam critério de geração, ou seja, são gerados no arquivo da DIRF, o registro RIO deverá ser apresentado com o valor que possui de rendimentos\.

OS3528

OS3267\-D

# RN56

Gravar no campo 3 – Descrição dos rendimentos isentos – outros a informação que estiver contida no campo “Descrição” do menu Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais\.

Se a origem da informação for da tabela SAFX53/X530\_RETIFICACAO\_IRRF, deverá ser recuperado a descrição dos rendimentos isentos – outros do campo 39 \- DSC\_OUTROS\_DIRF\.

Para recuperar as informações da SAFX53/X530\_RETIFICACAO\_IRRF, o sistema deverá recuperar as informações da SAFX53 e somente nos casos em que o registro da SAFX53 possua uma ou mais retificações na X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN57

Gravar no campo 1 – Identificador do Registro o valor fixo “RTRT”\.

OS3528

# RN58

Gravar no campo 2 – Janeiro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN59

Gravar no campo 3 – Fevereiro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN60

Gravar no campo 4 – Março o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN61

Gravar no campo 5 – Abril o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN62

Gravar no campo 6 – Maio o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN63

Gravar no campo 7 – Junho o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN64

Gravar no campo 8 – Julho o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN65

Gravar no campo 9 – Agosto o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN66

Gravar no campo 10 – Setembro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN67

Gravar no campo 11 – Outubro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN68

Gravar no campo 12 – Novembro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN69

Gravar no campo 13 – Dezembro o valor contido no campo VLR\_BRUTO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN70

Gravar no campo 14 – Décimo Terceiro o valor contido no campo “Valor 13º\. Salário” da SAFX53/X530\_RETIFICACAO\_IRRF\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN71

Gravar no campo 1 – Identificador do Registro o valor fixo “RTIRF”\.

OS3528 OS3267\-D

# RN72

Gravar no campo 2 – Janeiro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN73

Gravar no campo 3 – Fevereiro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN74

Gravar no campo 4 – Março o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN75

Gravar no campo 5 – Abril o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN76

Gravar no campo 6 – Maio o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN77

Gravar no campo 7 – Junho o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN78

Gravar no campo 8 – Julho o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN79

Gravar no campo 9 – Agosto o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN80

Gravar no campo 10 – Setembro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN81

Gravar no campo 11 – Outubro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN82

Gravar no campo 12 – Novembro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN83

Gravar no campo 13 – Dezembro o valor contido no campo VLR\_IR\_RETIDO da SAFX53/X530\_RETIFICACAO\_IRRF para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53/X530\_RETIFICACAO\_IRRF\)\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN84

Gravar no campo 14 – Décimo Terceiro o valor contido no campo “Valor Tributo 13º\. Salário” da SAFX53/X530\_RETIFICACAO\_IRRF\.

O campo “Tipo Lançamento” \(campo 40 = 0 da SAFX53/X530\_RETIFICACAO\_IRRF\) deverá estar selecionado com a opção “Informações dos Beneficiários”\.

OS3528

OS3267\-D

# RN85

Gravar no campo 1 – Identificador de Registro o valor fixo “INF”\.

OS3528

# RN86

Gravar no campo 2 – CPF o CPF do Beneficiário Pessoa Física presente no registro BPFDEC\. Deverá ser gravado apenas um registro para cada CPF informado no registro BPFDEC\.

OS3528

# RN87

Gravar no campo 3 – Informações Complementares a informação de forma concatenada separando cada campo com “\-“ a partir dos campos preenchidos na tabela X22\_INF\_COMPL\.

- Caso o campo IND\_TIPO = “2” da X22\_INF\_COMPL
	- NUM\_PROC\_JUD
	- DAT\_DECISAO
	- TRIB\_JUST
	- VARA\_JUDICIAL
- Caso o campo IND\_TIPO = “1” da X22\_INF\_COMPL
	- CPF
	- NOME
	- VLR\_PENSAO
	- VLR\_PENSAO\_13

OS3528

# RN88

Gravar no campo 1 – Identificador do Registro o valor fixo “FIMDirf”\.

OS3528

# RN89

Devem ser recuperados as fichas financeiras \(tabela X21\_FICHA\_FINANC\) e as retenções \(X53\_RETENCAO\_IRRF ou X530\_RETIFICACAO\_IRRF\) dos funcionários e dos prestadores que estejam no período informado para a geração\. 

Caso um funcionário não possua valores para retenção de Imposto de Renda no período para nenhum mês ou Décimo Terceiro Salário, o mesmo não deverá ser informado\.

No caso da SAFX53 ou X530\_RETIFICACAO\_IRRF deverão ser recuperados somente os beneficiários que forem PESSOA FÍSICA\.

As retenções da tabela X53\_RETENCAO\_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração da DIRF\. Vale salientar que essas retenções não possuem registros de retificação\.

Gravar no campo 1 – Identificador do Registro a informação de acordo com as regras abaixo:

- Gravar o valor fixo “ESRT” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa e quando a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\. No caso da SAFX53, recuperar a informação a partir da somatória dos campos VLR\_BRUTO e VLR\_OUTROS\_TRIB\_EXCL da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “ESPO” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa e quando a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Oficial\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_INSS\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “ESPP” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e quando o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Previdência Privada/FAPI\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PREV\_PRIVADA da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “ESDP” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Dependentes\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_DED\_DEP\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “ESPA” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Deduções \(Pensão Alimentícia\)”\. No caso da SAFX53, recuperar a informação do campo VLR\_PENS\_ALIMENT da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.
- Gravar o valor fixo “ESIR” caso a Ficha Financeira \(tabela SAFX21\) do período informado para geração tenha no campo 11 \(IND\_TP\_LANCTO\_DIRF\) a opção selecionada “Beneficiários com rendimento/imposto cuja tributação está sob exigibilidade suspensa” e caso a verba informada \(campo 07 da SAFX21\) o campo “Classe para DIRF” do menu Parâmetros >> Parâmetros para Verbas \(Folha de Pagamento\) do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\. No caso da SAFX53, recuperar a informação do campo VLR\_IR\_RETIDO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\.

OS3528

OS3267\-D

# RN90

Gravar no campo 1 – Identificador do Registro o valor fixo “RIPTS”\.

OS3528

# RN91

Gravar no campo 2 – Valor pago no ano o total de valores contido do ano calendário a partir do campo 09 da SAFX21, desde que a verba informada no campo 07 da SAFX21 possua na parametrização de Verba por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\) o campo “Classe para DIRF” preenchido com a opção “Isentos Anuais \(Valores pagos a titular ou sócio de empresa\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

# RN92

Gravar no campo 1 – Identificador do registro o valor fixo “PSE”\. Esse registro só será gerado caso o campo “Plano privado de assistência à saúde – coletivo empresarial” da tela de geração do meio magnético \(menu: DIRF >> Geração DIRF\) do módulo Obrigações de Tributos Federais esteja selecionado com a opção “Sim” e se existe informações na Ficha Financeira \(SAFX21\) desde que a verba esteja classificada como “Pagamento ao Plano Privado de Assistência à Saúde”

OS3528

# RN93

Gravar no campo 1 – Identificador do Registro o valor fixo “OPSE”\. Esse registro só será gerado caso existam registros TPSE existentes\. Só deve ser recuperado dos planos de saúde do movimento\.

OS3528

# RN94

Gravar no campo 2 – CNPJ da operadora de plano privado de assistência à saúde \- coletivo empresarial, o conteúdo do campo “CNPJ” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\.

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

# RN95

Gravar no campo 3 – Nome Empresarial, o conteúdo do campo “Nome Empresarial” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\.

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

# RN96

Gravar no campo 4 – Registro ANS, o conteúdo do campo “Registro ANS” da tela pertencente ao menu Manutenção >> Cadastros >> Assistência à Saúde >> Operadora de Plano Privado de Assistência à Saúde do módulo DW\. O campo possui 10 posições na tela de manutenção, porém no registro serão gravadas somente as 6 primeiras posições

Essa informação será recuperada de acordo com o Plano de Saúde informado no campo “Operadora de Plano Privado de Assist\. à Saúde” da tela Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) para a verba informada na SAFX21, desde que o campo “Operadora de Plano Privado de Assist\. a Saúde” da SAFX15 não esteja preenchido\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima será ignorada\.

OS3528

# RN97

Gravar no campo 1 – Identificador do Registro o valor fixo “TPSE”\.

Essa informação será recuperada a partir das fichas financeiras cadastradas na SAFX21 desde que a verba parametrizada na SAFX21 \(campo 07 – COD\_VERBA\) possua na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros para Verba \(Folha de Pagamento\) esteja com o campo “Classe DIRF” com a opção “Pagamento ao Plano Privado de Assistência à Saúde” e com o campo “Operadora de Plano Privado de Assist\. à Saúde” da mesma tela parametrizado para o Plano de Saúde\.

Caso o campo “Operadora de Plano Privado de Assist\. à Saúde” da SAFX15 esteja preenchido a regra acima de recuperar a partir da vinculação da Verba com o Plano de Saúde será ignorada\.

OS3528

# RN98

Gravar no campo 2 – CPF do Titular o CPF do Funcionário de acordo com o campo 03 \(COD\_FUNC\) da tabela SAFX21 preenchido\. Com o Funcionário identificado, gravar o CPF a partir do campo 12 \(CPF\) da tabela SAFX15\.

OS3528

# RN99

Gravar no campo 3 – Nome o Nome do Funcionário de acordo com o campo 03 \(COD\_FUNC\) da tabela SAFX21 preenchido\. Com o Funcionário identificado, gravar o Nome a partir do campo 05 \(NOME\) da tabela SAFX15\.

OS3528

# RN100

Gravar no campo 4 – Valor pago no ano o conteúdo do campo Valor Pago no Ano do Funcionário de acordo com o campo 09 \(VLR\_VERBA\) da tabela SAFX21\.

Caso o Funcionário possua Dependentes na SAFX212, será considerado o Valor Pago no Ano para o Titular o conteúdo do campo 09 \(VLR\_VERBA\) da tabela SAFX21 subtraindo o somatório do Valor da Verba da SAFX212 de cada um dos Dependentes\. 

__Valor Pago pelo Titular quando o mesmo tem Dependentes__ = SAFX21\.VLR\_VERBA – SAFX212\.VLR\_VERBA \(somatório de todos os dependentes\)\.

__OBS:__ para que essa solução funcione corretamente, o cliente deverá carregar para o Valor da Verba do titular o somatório do Titular e dos Dependentes\.

Caso o Funcionário não possua Dependentes na SAFX212, gravar o valor nesse campo\.

OS3528

# RN101

Gravar no campo 1 – Identificador do registro o valor fixo “DTPSE”\.

OS3528

# RN102

Gravar no campo 2 – CPF do Dependente a informação do CPF do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\)\. Com o Dependente identificado, gravar o CPF a partir do campo CPF do Dependente da SAFX55\.

OS3528

# RN103

Gravar no campo 3 – Data de Nascimento a informação da Data de Nascimento do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar a Data de Nascimento a partir do campo 08 \(DATA\_NASC\) da SAFX55\.

OS3528

# RN104

Gravar no campo 4 – Nome o Nome do Dependente de acordo com o campo “Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar o Nome a partir do campo 07 \(NOME\) da tabela SAFX55\.

OS3528

# RN105

Gravar no campo 5 – Relação de dependência a Relação de Dependência do Dependente em relação ao Funcionário, de acordo com o campo “Código Dependente” da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\. Com o Dependente identificado, gravar o código do Dependente – conforme relação abaixo – de acordo com o campo 06 \(COD\_TIPO\_DEPEND\) da tabela SAFX55\.

- Caso a opção selecionada seja “03 – Cônjuge/Companheiro\(a\)”, gravar “03”\.
- Caso a opção selecionada seja “04 – Filho\(a\)”, gravar “04”\.
- Caso a opção selecionada seja “06 – Enteado\(a\)”, gravar “06”\.
- Caso a opção selecionada seja “08 – Pai/Mãe”, gravar “08”\.
- Caso a opção selecionada seja “10 – Agregado/Outros”, gravar “10”\.

Caso o campo 06 \(COD\_TIPO\_DEPEND\) da tabela SAFX55 esteja com outra opção selecionada, a opção será gravada, porém isso poderá causar crítica no PGD da DIRF 2011\.

OS3528

# RN106

Gravar no campo 6 – Valor pago no ano o conteúdo do campo “Valor pago no ano” do dependente da tela Manutenção >> Folha de Pagamento >> Ficha Financeira Segregada por Dependente \(SAFX212\) do módulo DW\.

Cada Dependente deve ser gerado em um registro do tipo DTPSE separado\.

OS3528

# RN107

Gravar no campo 1 – Identificador do Registro o valor fixo “RIDAC”\. Essa informação poderá ser recuperada a partir da Ficha Financeira \(SAFX21\) ou das Retenções \(SAFX53/X530\_RETIFICACAO\_IRRF\)\.

- SAFX21
	- Deverão ser recuperadas as Fichas Financeiras \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Diária e Ajuda de Custo\)”\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Deverão ser recuperadas as Retenções \(SAFX53\) do período que pertençam à Pessoas Físicas \(campos 04 e 05 da SAFX53, desde que o campo 05 pela SAFX04 tenha 11 posições\) e que possuam o Valor de Ajuda de Custo preenchido \(campo VLR\_AJUDA\_CUSTO da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN108

Gravar no campo 2 – Janeiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Janeiro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN109

Gravar no campo 3 – Fevereiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Fevereiro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN110

Gravar no campo 4 – Março:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Março \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN111

Gravar no campo 5 – Abril:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Abril \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN112

Gravar no campo 6 – Maio:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Maio \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN113

Gravar no campo 7 – Junho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Junho \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN114

Gravar no campo 8 – Julho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Julho \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN115

Gravar no campo 9 – Agosto:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Agosto \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN116

Gravar no campo 10 – Setembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Setembro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN117

Gravar no campo 11 – Outubro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Outubro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN118

Gravar no campo 12 – Novembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Novembro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN119

Gravar no campo 13 – Dezembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_AJUDA\_CUSTO da SAFX53 para a competência de Dezembro \(ver campos 12 e 13 da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528 OS3267\-D

# RN120

Gravar no campo 14 – Décimo Terceiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo “Valor 13º\. Salário”\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528 OS3267\-D

# RN121

Gravar no campo 1 – Identificador do Registro o valor fixo “RIIRP”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Indenizações por Contrato de Trabalho\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

# RN122

Gravar no campo 2 – Janeiro o valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN123

Gravar no campo 3 – Fevereiro o valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN124

Gravar no campo 4 – Março o valor contido no campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN125

Gravar no campo 5 – Abril o valor contido no campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN126

Gravar no campo 6 – Maio o valor contido no campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN127

Gravar no campo 7 – Junho o valor contido no campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN128

Gravar no campo 8 – Julho o valor contido no campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN129

Gravar no campo 9 – Agosto o valor contido no campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN130

Gravar no campo 10 – Setembro o valor contido no campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN131

Gravar no campo 11 – Outubro o valor contido no campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN132

Gravar no campo 12 – Novembro o valor contido no campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN133

Gravar no campo 13 – Dezembro o valor contido no campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN134

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 09 da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

# RN135

Gravar no campo 1 – Identificador do Registro o valor fixo “RIAP”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Abono Pecuniário\)”\.

OS3528

# RN136

Gravar no campo 2 – Janeiro o valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN137

Gravar no campo 3 – Fevereiro o valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN138

Gravar no campo 4 – Março o valor contido no campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN139

Gravar no campo 5 – Abril o valor contido no campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN140

Gravar no campo 6 – Maio o valor contido no campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN141

Gravar no campo 7 – Junho o valor contido no campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN142

Gravar no campo 8 – Julho o valor contido no campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN143

Gravar no campo 9 – Agosto o valor contido no campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN144

Gravar no campo 10 – Setembro o valor contido no campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN145

Gravar no campo 11 – Outubro o valor contido no campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN146

Gravar no campo 12 – Novembro o valor contido no campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN147

Gravar no campo 13 – Dezembro o valor contido no campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN148

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 09 da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

# RN149

Gravar no campo 1 – Identificador do Registro o valor fixo “RIMOG”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Pensão, Aposentadoria ou Reforma por Moléstia Grave\)”\.

Serão recuperados os Beneficiários cujo valor total de rendimentos anuais seja igual ou superior a 3 \(três\) vezes o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\.

OS3528

# RN150

Gravar no campo 2 – Janeiro o valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN151

Gravar no campo 3 – Fevereiro o valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN152

Gravar no campo 4 – Março o valor contido no campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN153

Gravar no campo 5 – Abril o valor contido no campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN154

Gravar no campo 6 – Maio o valor contido no campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN155

Gravar no campo 7 – Junho o valor contido no campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN156

Gravar no campo 8 – Julho o valor contido no campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN157

Gravar no campo 9 – Agosto o valor contido no campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN158

Gravar no campo 10 – Setembro o valor contido no campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN159

Gravar no campo 11 – Outubro o valor contido no campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN160

Gravar no campo 12 – Novembro o valor contido no campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN161

Gravar no campo 13 – Dezembro o valor contido no campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN162

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 09 da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

# RN163

Gravar no campo 1 – Identificador do Registro o valor fixo “RIP65”\.

Essa informação deverá ser recuperada a partir da Ficha Financeira \(SAFX21\) do período cuja verba \(campo 07 da SAFX21\) esteja parametrizado na Parametrização de Verbas do módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\) = “Isentos \(Parcela Isenta de Aposentadoria para Maiores de 65 anos\)”\.

OS3528

# RN164

Gravar no campo 2 – Janeiro o valor contido no campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN165

Gravar no campo 3 – Fevereiro o valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN166

Gravar no campo 4 – Março o valor contido no campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN167

Gravar no campo 5 – Abril o valor contido no campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN168

Gravar no campo 6 – Maio o valor contido no campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN169

Gravar no campo 7 – Junho o valor contido no campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN170

Gravar no campo 8 – Julho o valor contido no campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN171

Gravar no campo 9 – Agosto o valor contido no campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN172

Gravar no campo 10 – Setembro o valor contido no campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN173

Gravar no campo 11 – Outubro o valor contido no campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN174

Gravar no campo 12 – Novembro o valor contido no campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN175

Gravar no campo 13 – Dezembro o valor contido no campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)\.

OS3528

# RN176

Gravar no campo 14 – Décimo Terceiro o valor contido no campo 09 da SAFX21 desde que o campo 06 da SAFX21 = 02 \(Pagamento de 13º\. Salário\)\.

OS3528

# RN177

Deverá ser alterado na tela de Geração da DIRF, o campo “Valor Anual Mínimo de Rendimentos”, o valor 

default é 23\.499,15\.

OS3528

# RN178

Vale salientar que os registros de plano de saúde – PSE, OPSE, TPSE e DTPSE – só serão gerados quando um funcionário possuir mais de um plano de saúde – independente se o mesmo for de assistência médica ou odontológica – caso o campo “Operadora de Plano Privado de Assist\. à Saúde” não esteja preenchido na SAFX15\. As regras para planos múltiplos só serão atendidas caso esse campo não esteja preenchido\. Caso o campo esteja preenchido, as regras de geração atuais serão mantidas\.

OS3528

# RN179

Gravar no campo 1 – Identificador do Registro o valor fixo “CJAC”\.

O registro CJAC corresponde a um registro BPFDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53/X530\_RETIFICACAO\_IRRF\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – ano calendário\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente dessa tabela\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto que as verbas classificadas como “Proventos” deverão ser somadas\.

OS3528

OS3267\-D

# RN178

Gravar no campo 2 – Janeiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN179

Gravar no campo 3 – Fevereiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN180

Gravar no campo 4 – Março:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN181

Gravar no campo 5 – Abril:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN182

Gravar no campo 6 – Maio:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN183

Gravar no campo 7 – Junho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN184

Gravar no campo 8 – Julho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN185

Gravar no campo 9 – Agosto:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN186

Gravar no campo 10 – Setembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN187

Gravar no campo 11 – Outubro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN188

Gravar no campo 12 – Novembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN189

Gravar no campo 13 – Dezembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN190

Gravar no campo 14 – Décimo Terceiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 desde que o campo “Indicador da Folha” \(campo 06 da SAFX21\) seja “Pagamento de 13º\. Salário”\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo “Valor Tributo 13º\. Salário” da SAFX53\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN191

Gravar no campo 1 – Identificador do Registro o valor fixo “CJAA”\.

O registro CJAA corresponde a um registro BPFDEC correspondente, logo deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53/X530\_RETIFICACAO\_IRRF\) dos Beneficiários – pessoas físicas – cujo campo Tipo Lançamento = Beneficiários com valores de imposto compensados em virtude de decisão judicial – anos anteriores\. Nos casos em que a informação for oriunda da SAFX21, verificar o código da verba \(campo 07\) e verificar se na Parametrização por Verba \(menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\) o campo “Classe DIRF” = “Imposto de Renda Retido”\.

Caso o registro da SAFX53 possua uma ou mais retificações na tabela X530\_RETIFICACAO\_IRRF, deverá ser recuperado o registro mais recente dessa tabela\.

O valor compensado em virtude da decisão judicial já vai ser informado nesse registro além do campo respectivo ao mesmo Beneficiário no registro RTIRF também já vir com a informação correta\.

*Exemplo*: caso se tenha um valor a ser compensado de R$ 1\.000,00 e o valor retido no mês foi de R$ 1\.000,00, o registro RTIRF será informado com o valor R$ 0,00 e o registro CJAC com valor R$ 1\.000,00\. Caso o valor da compensação seja maior, o valor do imposto retido RTIRF será zerado e a sobra do crédito \(a ser utilizado no CJAC\) deverá ser utilizada em outro mês\. Caso o valor da compensação seja menor, o valor do RTIRF será diminuído até o valor máximo da compensação, e o CJAC será informado com o valor creditado\.

OBS: vale salientar que as verbas informadas no campo 07 da SAFX21 deverão seguir a regra previamente existente de que as verbas classificadas como “Desconto” deverão ser subtraídas, enquanto que as verbas classificadas como “Proventos” deverão ser somadas\.

OS3528

OS3267\-D

# RN192

Gravar no campo 2 – Janeiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Janeiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN193

Gravar no campo 3 – Fevereiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Fevereiro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN194

Gravar no campo 4 – Março:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Março \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN195

Gravar no campo 5 – Abril:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Abril \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN196

Gravar no campo 6 – Maio:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Maio \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN197

Gravar no campo 7 – Junho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Junho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN198

Gravar no campo 8 – Julho:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Julho \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN199

Gravar no campo 9 – Agosto:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Agosto \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN200

Gravar no campo 10 – Setembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Setembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN201

Gravar no campo 11 – Outubro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Outubro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN202

Gravar no campo 12 – Novembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Novembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN203

Gravar no campo 13 – Dezembro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 para a competência de Dezembro \(campos 04 e 05 da SAFX21\)\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo VLR\_IR\_RETIDO da SAFX53 para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA da SAFX53\)\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN204

Gravar no campo 14 – Décimo Terceiro:

- SAFX21
	- O valor contido no campo 09 da SAFX21 desde que o campo “Indicador da Folha” \(campo 06 da SAFX21\) seja “Pagamento de 13º\. Salário”\. 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- O valor contido no campo “Valor Tributo 13º\. Salário” da SAFX53\. Caso a retenção possua uma ou mais retificações, deverá ser recuperada a retificação da tabela X530\_RETIFICACAO\_IRRF mais recente\. Os campos são os mesmos da SAFX53\.

OS3528

OS3267\-D

# RN205

Gravar no campo 1 – Identificador do Registro o texto fixo “RPDE”\.

As informações a serem gravadas serão recuperadas das tabelas SAFX21 e SAFX53/X530\_RETIFICACAO\_IRRF\. Caso não existam registros nessas tabelas, os registros RPDE, BRPDE e VRPDE não deverão ser gerados\. O critério para recuperar as informações dos beneficiários domiciliados no exterior é o seguinte:

- SAFX21
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores do período informado nos campos “Mês/Ano da Saída do País” e “Mês/Ano do Retorno ao País” \(campos 68 e 69 da SAFX21\) __OU__ com valores de IR retido na fonte – ver campo 07 da SAFX21 cuja campo “Classe DIRF” = Imposto de Renda Retido na tela de Parâmetros por Verba \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros por Verba \(Folha de Pagamento\)\) – e com o campo 09 da SAFX21 preenchido para o período\. 
- SAFX53
	- Campo “Declarante de rendimentos pagos a residentes ou domiciliados no exterior” = Sim no menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais;
	- Total de Rendimentos anuais igual ou superior a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” do menu DIRF >> Geração DIRF do módulo Obrigações de Tributos Federais\. Deverão ser considerados como Total de Rendimentos anuais os valores durante o período quando a Pessoa Física/Jurídica possuir a UF = EX __OU__ com valores de IR retido na fonte – ver campo VLR\_IR\_RETIDO da SAFX53 para o período informado\.Caso a retenção da SAFX53 possua um ou mais registros na X530\_RETIFICACAO\_IRRF, o sistema deverá recuperar o registro mais recente dessa tabela\.

O total de rendimentos do ano calendário que estiverem fora do período informado nos campos 68 e 69 da SAFX21 serão considerados nos registros\-filhos da família BPFDEC \(porque os mesmos serão pagos para o funcionário residente no Brasil\)\. Só serão considerados nos registros\-filhos da família RPDE os que estiverem dentro do período informado nos campos 68 e 69 da SAFX21\.

Nos casos em que o prestador de serviço \(pessoa física ou jurídica\) estiver parte do ano prestando serviço no Brasil e na outra parte do ano fora do país, o cliente deverá criar dois cadastros desse prestador \(SAFX04\) com data de validade distinta\. Só será considerada nos registros da família RPDE os que estiverem com UF = EX\. O cadastro do prestador que estiver no Brasil \(UF <> EX\) será considerado nos registros da família BPJDEC\.

Caso um mesmo funcionário \(SAFX21\) ou prestador \(SAFX53/X530\_RETIFICACAO\_IRRF\) possuam informações para os respectivos registros dentro do país \(BPFDEC ou BPJDEC e filhos\) ou fora do país \(RPDE, BRPDE e VRPDE\) o sistema não deverá considerar o somatório de dentro e fora do país para definir se o funcionário ou prestador é elegível para ser considerado na DIRF\. As informações devem ser consideradas de forma separada\. Caso em ambas as situações os valores não sejam iguais ou superiores a 1x o valor informado no campo “Valor Anual Mínimo de Rendimentos” da tela de Geração da DIRF, o funcionário ou prestador __NÃO SERÁ INFORMADO__ no meio magnético\. Porém se em um dos casos o mesmo for elegível, __TODAS__ as informações pertinentes ao funcionário ou prestador serão geradas no arquivo\.

OS3528

OS3267\-D

# RN206

Gravar no campo 1 – Identificador de Registro o valor fixo “BRPDE”\.

OS3528

# RN207

Gravar no campo 2 – Beneficiário a informação de acordo com as regras abaixo:

- SAFX21
	- Gravar o valor “1”
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Caso o Beneficiário seja uma Pessoa Física \(campo 04 da SAFX53\), gravar “1”\.
	- Caso o Beneficiário seja uma Pessoa Jurídica \(campo 04 da SAFX53\), gravar “2”\.

No caso da SAFX53, para identificar uma Pessoa Física de uma Jurídica, verificar o identificador do campo 04 da SAFX53 e procurar o campo 06 da SAFX04\. Caso o campo 06 da SAFX04 possua 11 posições é uma Pessoa Física\. Caso possua 14 posições é uma Pessoa Jurídica\.

Caso o campo 06 da SAFX04 não esteja preenchido – o que caracteriza que o beneficiário não possui CPF ou CNPJ – verificar o campo 26 da SAFX04\. Caso o mesmo esteja preenchido com “1”, gravar “1”\. Caso esteja preenchido com qualquer outra informação, gravar “2”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN208

Gravar no campo 3 – Código do País a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor de acordo com o campo “País”\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 21 da SAFX04\.

No caso em que o Código do País não for preenchido na SAFX21, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Funcionário residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro do Funcionário\.*__”\.

No caso em que o Código do País não for preenchido na SAFX53, deverá ser exibida a seguinte mensagem no log de geração da DIRF: “__*Retenção de Terceiro residente no exterior sem preenchimento do campo Código do País\. Por gentileza, verificar o cadastro da Pessoa Física/Jurídica*__”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN209

Gravar no campo 4 \- Número de identificação fiscal – NIF a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo “Número de Identificação Fiscal” da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN210

Gravar no campo 5 – Indicador de beneficiário dispensado do Número de Identificação Fiscal – NIF, seguindo as regras abaixo:

- SAFX21
- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, verificar se existe informação no campo 73\- “NUM\_ID\_FISCAL” da SAFX15, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’
- SAFX53/X530\_RETIFICACAO\_IRRF
- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, verificar se existe informação no campo 53\- “NUM\_ID\_FISCAL” da SAFX04, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN211

Gravar no campo 6 – Identificador de que o país não exige Número de Identificação Fiscal – NIF

- SAFX21
- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, verificar se existe informação no campo 76\- “DSC\_PROVINCIA\_EX” da SAFX15, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’
- SAFX53/X530\_RETIFICACAO\_IRRF
- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, verificar se existe informação no campo 55\- “DSC\_PROVINCIA\_EX” da SAFX04, em caso afirmativo o campo deve ser preenchido com ‘N’, caso contrário ‘S’

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN212

Gravar no campo 7 – CPF/CNPJ a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 12 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 06 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN213

Gravar no campo 8 – Nome/Nome Empresarial a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 05 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 05 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN214

Gravar no campo 9 – Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica a informação de acordo com as regras abaixo:

- SAFX21
	- Não será gravada nessa situação, visto que essa informação é pertinente somente para Pessoas Jurídicas\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo “Relação Fonte Pagadora/Beneficiário” da SAFX04\. Essa informação só será gravada caso a Pessoa Física/Jurídica da SAFX04 seja uma __Pessoa Jurídica__, neste caso o preenchimento do campo é obrigatório\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN215

Gravar no campo 10 – Logradouro a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 35 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 12 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN216

Gravar no campo 11 – Número a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 36 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 13 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN217

Gravar no campo 12 – Complemento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 37 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 14 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN218

Gravar no campo 13 – Bairro/Distrito a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 38 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 15 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN219

Gravar no campo 14 – Código Postal a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 40 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 20 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN220

Gravar no campo 15 – Cidade a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 39 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 16 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN221

Gravar no campo 16 – Estado/Província a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido no campo 76 da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido no campo 55 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN222

Gravar no campo 17 – Telefone a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação de acordo com o Funcionário \(campo 03 da SAFX21\)\. Com essa informação, gravar o valor contido nos campos “DDD” e “Telefone” da SAFX15\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação de acordo com o campo 04 da SAFX53\. Com essa informação, gravar o valor contido nos campos 22 e 23 da SAFX04\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN223

Gravar no campo 1 – Identificador do Registro o valor fixo “VRPDE”\.

OS3528

# RN224

Gravar no campo 2 – Data do Pagamento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo 08 da SAFX21\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação do campo “Data Pagamento” da SAFX53\. Caso o campo “Data Pagamento” não esteja preenchido, gravar a informação contida no campo 03 \(DATA\_MOVTO\) da SAFX53\.

Nesse caso em que a Data do Pagamento não esteja preenchida para a SAFX53/X530\_RETIFICACAO\_IRRF e seja gerada no arquivo a Data do Movimento deverá ser exibido no log de geração da DIRF a seguinte mensagem: __*“Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos”*__

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN225

Gravar no campo 3 – Código de Receita a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo “Residente no Exterior” da tela de geração da DIRF – módulo: Obrigações de Tributos Federais, menu: DIRF >> Geração DIRF\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação do campo 11 da SAFX53\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN226

Gravar no campo 4 – Tipo de Rendimento a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Tipo Rendimento” 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação do campo “Tipo Rendimento”\.

No caso em que o Tipo Rendimento não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que o Tipo Rendimento não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN227

Gravar no campo 5 – Rendimento Pago a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Rendimentos Tributáveis”\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação a partir do campo 14 da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser somadas, enquanto que as verbas classificadas como “Descontos” devem ser subtraídas\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN228

Gravar no campo 6 – Imposto Retido a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação a partir do campo 09 da SAFX21, desde que a verba informada \(campo 07 da SAFX21\) esteja parametrizada no menu Parâmetros >> Parâmetros p/ Verba do módulo Obrigações de Tributos Federais com a opção “Imposto de Renda Retido”\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação a partir do campo 15 da SAFX53

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto que as verbas classificadas como “Descontos” devem ser somadas\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN229

Gravar no campo 7 – Forma de Tributação a informação de acordo com as regras abaixo:

- SAFX21
	- Recuperar a informação do campo “Forma Tributação” 
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Recuperar a informação do campo “Forma Tributação” 

No caso em que a Forma de Tributação não esteja preenchido na SAFX21, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Funcionário residente no exterior sem preenchimento de algum dos campos: Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção da Ficha Financeira\.*__”

No caso em que a Forma de Tributação não esteja preenchido na SAFX53, deverá ser exibido no log de geração da DIRF a seguinte mensagem: “__*Retenção de Terceiro residente no exterior sem preenchimento de algum dos campos: Data Pagamento, Tipo Rendimento e/ou Forma Tributação\. Por gentileza, verificar a manutenção do Controle de Tributos\.*__”

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN230

Gravar no campo 1 – Identificador do Registro o valor fixo “ESDJ”\.

- Deverão ser recuperadas as Fichas Financeiras \(SAFX21\) e as Retenções do período \(SAFX53\) – somente para pessoas físicas – cujo campo Tipo Lançamento = Beneficiários do Imposto de Renda retido na fonte com depósito judicial\.
- Quando as informações forem recuperadas das Fichas Financeiras \(SAFX21\), o código da verba \(campo 07 da SAFX21\) deverá estar parametrizado no módulo Obrigações de Tributos Federais \(menu: Parâmetros >> Parâmetros p/ Verba\) com o campo “Classe DIRF” = “Imposto de Renda Retido”\.

OBS: as verbas oriundas da tabela SAFX21 que estiverem classificadas como “Proventos” devem ser subtraídas, enquanto que as verbas classificadas como “Descontos” devem ser somadas\.

OS3528

# RN231

Gravar no campo 2 – Janeiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Janeiro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Janeiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN232

Gravar no campo 3 – Fevereiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Fevereiro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Fevereiro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN233

Gravar no campo 4 – Março de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Março \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Março \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN234

Gravar no campo 5 – Abril de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Abril \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Abril \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN235

Gravar no campo 6 – Maio de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Maio \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Maio \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN236

Gravar no campo 7 – Junho de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Junho \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Junho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN237

Gravar no campo 8 – Julho de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Julho \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Julho \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN238

Gravar no campo 9 – Agosto de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Agosto \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Agosto \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN239

Gravar no campo 10 – Setembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Setembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Setembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN240

Gravar no campo 11 – Outubro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Outubro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Outubro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN241

Gravar no campo 12 – Novembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Novembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Novembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN242

Gravar no campo 13 – Dezembro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21 para a competência de Dezembro \(ver campos 04 e 05 da SAFX21\)
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo VLR\_IR\_RETIDO da SAFX53 para a competência de Dezembro \(ver campos ANO\_COMPETENCIA e MÊS\_COMPETENCIA\)

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN243

Gravar no campo 14 – Décimo Terceiro de acordo com as regras abaixo:

- SAFX21
	- Gravar o campo 09 da SAFX21, desde que o campo 06 \(IND\_FOLHA\) da SAFX21 esteja com a opção “Pagamento de 13º\. Salário”\.
- SAFX53/X530\_RETIFICACAO\_IRRF
	- Gravar o campo “Valor Tributo 13º\. Salário”\.

Será considerado o registro da SAFX53, caso a mesma não possua uma retificação na X530\_RETIFICACAO\_IRRF\. Caso a mesma possua uma ou mais retificações nessa tabela, deverá ser recuperado o registro mais recente\.

OS3528

OS3267\-D

# RN244

Caso durante a geração do arquivo o campo “Relação Fonte Pagadora/Beneficiário” do registro BRPDE seja informado para uma Pessoa Física, deve ser exibida a seguinte mensagem de erro no log de geração\.

“Não pode ser informado para uma Pessoa Física a Relação de Fonte Pagadora com o Beneficiário, pois a mesma é pertinente apenas para Pessoa Jurídica”\.

Embora seja exibida a mensagem de erro, a geração do arquivo não será impedida\.

OS3528

# RN245

Criação da tela Rendimentos Recebidos Acumuladamente, no Menu: DIRF	

OS3528

# RN246

Registros Recebido Acumuladamente:

#### Deverão ser recuperado as informações da tela “Rendimentos Recebidos Acumuladamente” localizada no Menu: DIRF do módulo Federal / Obrigações de Tributos Federais, com base nos campos Ano Referência\-DIRF e Processo \- Ano Base \- Dt Geração, da tela de Formatação das Mídias \(Menu: DIRF / Geração do Meio Magnético / Ano Referência a partir de 2011\) seguindo as seguintes regras:

\- Serão considerados no txt da DIRF\-2012, os registros de RRA que estiverem cadastrados com Ano\-Calendário 2011, Ano Referência\-DIRF2012, uma vez que na tela de Formatação das Mídias, o usuário informe o Ano Referência\-DIRF2012  e escolha um processo que tenha sido gerado com o Ano\-Calendário 2011\.

\- Serão considerados no txt da DIRF\-2012, os registros de RRA que estiverem cadastrados com Ano\-Calendário 2012, Ano Referência\-DIRF2012, uma vez que na tela de Formatação das Mídias, o usuário informe o Ano Referência\-DIRF2012  e escolha um processo que tenha sido gerado com o Ano\-Calendário 2012\.

Estrutura completa:

RRA \- Rendimentos recebidos acumuladamente

IDREC \- Identificação do código de receita

BPFRRA \- Beneficiário pessoa física do rendimento recebido acumuladamente

RTRT \- Rendimentos Tributáveis \- Rendimento Tributável

RTPO \- Rendimentos Tributáveis \- Dedução \- Previdência Oficial

RTPA \- Rendimentos Tributáveis \- Dedução \- Pensão Alimentícia

RTIRF \- Rendimentos Tributáveis \- Imposto de Renda Retido na Fonte

RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave

DAJUD \- Despesa com ação judicial

QTMESES \- Quantidade de meses

OS3528

# RN247

Registro de rendimentos recebidos acumuladamente

- Este registro deve ser classificado em ordem crescente por:

                 \- Indicador de rendimento recebido acumuladamente e 

                 \-  Número do processo

Gravar no campo 1 – Identificador do Registro o valor fixo “RRA”\.

OS3528

# RN248

Gravar no campo 2 – Identificador de rendimento recebido acumuladamente, a informação do campo “Identificador de rendimento recebido acumuladamente”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN249

Gravar no campo 3 – Número do Processo/Requerimento, a  informação do campo “Número do Processo / Requerimento”, da tela “Rendimentos Recebidos Acumuladamente”\.

Obs\. Este campo será obrigatório se o campo 2– Identificador de rendimento recebido acumuladamente, for igual a “2”

OS3528

# RN250

Gravar no campo 4 – Advogado/escritório de advocacia, de acordo com as regras abaixo:

- 
	- Se o campo “CPF/CNPJ” da tela “Rendimentos Recebidos Acumuladamente” estiver preenchido com 11 posições gravar “1”, caso seja 14 posições gravar “2”

OS3528

# RN251

Gravar no campo 5 – CPF Advogado/CNPJ escritório de advocacia, a  informação do campo “CPF/CNPJ”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN252

Gravar no campo 6 – Advogado/escritório de advocacia, a  informação do campo “Nome do Advogado / Escritório de Advocacia”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN253

- Deve ser apresentado com os códigos de receita em ordem crescente
- Deve estar associado ao registro do tipo RRA

Gravar no campo 1 – Identificador do Registro o valor fixo “IDREC”\.

OS3528

# RN254

Gravar no campo 2 – Código de Receita de acordo com a regra abaixo:

- Preencher com a informação do campo “Código de Receita” da tela “Rendimentos Recebidos Acumuladamente”, Atualmente no layout de 2012 este campo é fixo “1889”\.

OS3528

# RN255

Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente 

- Este registro deve ser classificado em ordem crescente por:

                 \- CPF

                \- Natureza do RRA

- Deve ser associado ao registro do tipo IDREC

Gravar no campo 1 – Identificador do Registro o valor fixo “BPFRRA”\.

OS3528

# RN256

Gravar no campo 2 – CPF, a  informação do campo “CPF”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN257

Gravar no campo 3 – Nome, a  informação do campo “Beneficiário”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN258

Gravar no campo 4 – Natureza do RRA, a  informação do campo “Natureza do rendimento recebido acumuladamente”, da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN259

Gravar no campo 5 – Data atribuída pelo laudo da moléstia grave, a  informação do campo “Data atribuída pelo laudo”, da tela “Rendimentos Recebidos Acumuladamente”

Formato do campo: AAAAMMDD

OS3528

# RN260

Gravar no campo 1 – Identificador do Registro a informação de acordo com as regras abaixo:

- Gravar o valor fixo “RTRT” 
- Gravar o valor fixo “RTPO” 
- Gravar o valor fixo “RTPA” 
- Gravar o valor fixo “RTIRF” 
- Gravar o valor fixo “RIMOG”

OS3528

# RN261

Gravar no campo 2 – Janeiro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Janeiro , conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN262

Gravar no campo 3 – Fevereiro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Fevereiro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN263

Gravar no campo 4 – Março o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Março, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN264

Gravar no campo 5 – Abril o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Abril, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN265

Gravar no campo 6 – Maio o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Maio, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN266

Gravar no campo 7 – Junho o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Junho, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN267

Gravar no campo 8 – Julho o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Julho, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN268

Gravar no campo 9 – Agosto o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Agosto, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN269

Gravar no campo 10 – Setembro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Setembro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN270

Gravar no campo 11 – Outubro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Outubro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN271

Gravar no campo 12 – Novembro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Novembro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN272

Gravar no campo 13 – Dezembro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Dezembro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

OS3528

# RN273

Gravar no campo 14 – Décimo Terceiro o valor contido na tela “Rendimentos Recebidos Acumuladamente” referente à linha de Décimo Terceiro, conforme regras abaixo:

- Para o registro RTRT: campo Rendimento Tributável
- Para o registro RTPO: campo  Previdência Oficial
- Para o registro RTPA: campo Pensão Alimentícia
- Para o registro RTIRF: campo Imposto Retido
- Para o registro RIMOG: campo Rend Isento Moléstia Grave

ATENÇÃO: Até recebermos definição da Receita sobre a existência ou não do campo de 13º, o campo deve ser gerado com ‘||’, mesmo possuindo valor correspondente na tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN274

Registro de Despesas de Ação Judicial

Gravar no campo 1 – Identificador do Registro o valor fixo “DAJUD”\.

#### Deverão ser recuperado as informações da tela <a id="_Toc313347822"></a>“Rendimentos Recebidos Acumuladamente” localizada no Menu: DIRF do módulo Federal / Obrigações de Tributos Federais, com base no campo Ano Referência\-DIRF \(neste caso 2012\)\.

OS3528

# RN275

Gravar no campo 2 – Janeiro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Janeiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN276

Gravar no campo 3 – Fevereiro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Fevereiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN277

Gravar no campo 4 – Março de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Março da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN278

Gravar no campo 5 – Abril de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Abril da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN279

Gravar no campo 6 – Maio de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Maio da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN280

Gravar no campo 7 – Junho de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Junho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN281

Gravar no campo 8 – Julho de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Julho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN282

Gravar no campo 9 – Agosto de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Agosto da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN283

Gravar no campo 10 – Setembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Setembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN284

Gravar no campo 11 – Outubro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Outubro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN285

Gravar no campo 12 – Novembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de Novembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN286

Gravar no campo 13 – Dezembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha Dezembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN287

Gravar no campo 14 – Décimo Terceiro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Despesas Ação Judicial”, referente à linha de 13º da tela “Rendimentos Recebidos Acumuladamente”

ATENÇÃO: Até recebermos definição da Receita sobre a existência ou não do campo de 13º, o campo deve ser gerado com ‘||’, mesmo possuindo valor correspondente na tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN288

Registro de quantidade de meses 

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário
- Deve ser associado ao registro do tipo BPFRRA

Gravar no campo 1 – Identificador do Registro o valor fixo “QTMESES”\.

OS3528

# RN289

Gravar no campo 2 – Quantidade meses \- Janeiro com a informação do campo “Quantidade de Meses” referente à linha de Janeiro da  tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN290

Gravar no campo 3 – Quantidade meses \- Fevereiro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Fevereiro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN291

Gravar no campo 4 – Quantidade meses \-  Março de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Março da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN292

Gravar no campo 5 – Quantidade meses \- Abril de acordo com as regras abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Abril da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN293

Gravar no campo 6 – Quantidade meses \- Maio de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Maio da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN294

Gravar no campo 7 – Quantidade meses \- Junho de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Junho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN295

Gravar no campo 8 – Quantidade meses \- Julho de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Julho da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN296

Gravar no campo 9 – Quantidade meses \- Agosto de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Agosto da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN297

Gravar no campo 10 – Quantidade meses \- Setembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Setembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN298

Gravar no campo 11 – Quantidade meses \-  Outubro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Outubro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN299

Gravar no campo 12 – Quantidade meses \- Novembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha de Novembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN300

Gravar no campo 13 – Quantidade meses \- Dezembro de acordo com a regra abaixo:

- 
	- Gravar o valor do campo “Quantidade de Meses”, referente à linha Dezembro da tela “Rendimentos Recebidos Acumuladamente”

OS3528

# RN300\.1

Se o Beneficiário Pessoa Física não atingiu o “Valor do Anual Mínimo de Rendimentos”, porém existem informações no período de RRA,  todos os registros da DIRF deverão ser apresentados, independente do valor que possui de rendimentos por registros\.

OS3528

# RN301

Alterar o default do campo Ano Referencia\-DIRF para 2012 na tela de Formatação Mídia, localizada no Menu: DIRF / Geração do Meio Magnético / Ano Referência a partir de 2011

OS3528

# RN302

Este layout é valido, apenas quando o cliente informar na tela da Geração da DIRF, no campo Ano Referencia\-DIRF um ano a partir de 2012 , caso contrário manter o layout compatível com os anos anteriores\.

OS3528

# RN303

Não deverão ser recuperados os registros da tabela de Controle de Tributos \(X53\_RETENCAO\_IRRF\) cujo campo 52 – DATA\_CANCELAMENTO esteja preenchido e cujo campo 53 – IND\_CANCELAMENTO = “S”\.

Essas retenções não deverão ser recuperadas para a DIRF, pois as mesmas foram retidas indevidamente e a partir do seu cancelamento o valor das mesmas será considerado como crédito para futura recuperação\.

OS3267\-D

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

