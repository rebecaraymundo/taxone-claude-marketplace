# MTZ-OTF-Gerar_Meio_Magnetico

- **Fonte:** MTZ-OTF-Gerar_Meio_Magnetico.docx
- **Modificado:** 2026-01-15
- **Tamanho:** 71 KB

---

# Obrigações de Tributos Federais \- Gerar Meio Magnético da DCTF

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3267\-B1

Obrigações de Tributos Federais \- Gerar DCTF

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

OS3267\-B2

Obrigações de Tributos Federais \- Geração da DCTF a partir das Retenções e Retificações das Retenções – Registros de Compensação R12 e R13

Será desenvolvida uma rotina para que a Sul América informe automaticamente na DCTF o respectivo valor dos créditos que estão sendo compensados na obrigação acessória\.

CH18020\_2012

Obrigações de Tributos Federais – Gerar campo 17 do registro R03 a partir do campo CRC UF do Responsável Legal

O objetivo deste documento de alteração de regra de negócio é gerar no campo 17 – UF do CRC Responsável a UF do Responsável Legal\. Hoje essa informação não está sendo gerada e por isso, está sendo solicitada a geração dessa informação\.

OS3699

Obrigações de Tributos Federais \- Atualização Legal da DCTF para a versão 2\.4

Trata\-se da atualização legal da DCTF para a versão 2\.4\.

CH24960\_2013

Obrigações de Tributos Federais – Correção do campo Ordem do Estabelecimento do registro R11

O objetivo deste documento de requisito é corrigir a geração do campo 12 – Ordem do Estabelecimento do registro R11 da DCTF, pois a geração desse campo está ocorrendo na posição incorreta\. 

CH4182\_2014

Obrigações de Tributos Federais – Tratamento nos campos 12 e 13 dos registros R10 e R11

O objetivo deste documento é colocar um tratamento na geração dos campos 12 – Ordem do Estabelecimento e 13 – CNPJ da Incorporação dos registros tipo R10 e R11 quando se aplicar códigos de receita dentro do grupo IPI, CIDE e RET\.

CH21391\_2014

Ajuste na regra do campo 19 do registro R10

Ajustar para considerar parametrização de “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” na tela parametrização de Dados Iniciais da DCTF\.

MFS43100

DCTF versão 3\.5

Atualização da DCTF para versão 3\.5, em substituição a 3\.4, para declarações com períodos a partir de 1º agosto de 2014\.

Até 1º agosto de 2014 a versão 2\.5 está mantida\.

MFS58858

Ajuste na Regra do Campo 17 do Registro Tipo R02 e Campo 11 do Registro Tipo R03\.  __\(RN92 e RN93\)__

O objetivo deste documento é corrigir a geração do Meio Magnético do Registro Tipo R02 do Campo 17 \- DDD do Fax e do Registro Tipo R03 do Campo 11 – DDD do Fax – Representado, que __NÃO __devem ser preenchidos se __não houver__ o número de FAX\. 

MFS616327

DCTF versão 3\.7

Atualização da DCTF para versão 3\.7, em substituição a 3\.5, para declarações com períodos a partir de 1º agosto de 2014\.

Até 1º agosto de 2014 a versão 2\.5 está mantida\.

MFS\-758230

Alteração do Menu e Título de tela

Alteração do Menu e do título da tela\. \(RN94\)

A partir de geração de 2025, será gerado o arquivo da DCTF e o arquivo JSON do MIT \(RN95\)

MFS\-779065

Não gerar o arquivo DCTF

A partir das gerações de 2025, não será gerado o arquivo da DCTF \(RN95\)\.

Inclusão de validações \(RN96\)

# Cód\.

__Descrição__

__DR__

# RN00

__Versões da DCTF Mensal__

Para declarações de períodos anteriores a 1º agosto de 2014, a versão da DCTF válida é a 2\.5\.

Para declarações de períodos a partir de 1º agosto de 2014, a versão da DCTF válida é a 3\.5 \(subtituiu a versão 3\.4\)\.

Para declarações de períodos a partir de 1º agosto de 2014, a versão da DCTF válida é a 3\.7 \(subtituiu a versão 3\.5\)\.

Segundo consulta à área da informação em agosto/2020, a versão 2\.5 já está prescrita, pois já passou o período de 5 anos\.  Mas ela pode ser exigida no caso de clientes que tiveram algum litigio com a RFB, que estejam em processo judicial que tenham suspendido o efeito prescricional de entrega da declaração\.

MFS43100

MFS616327

# RN01

__Informações das Fichas de Débito – Tipo R10__

__Campo 01 – Tipo__

Deverá ser gravado nas posições 1 a 3 o texto “R10”\.

OS3267\-B1

# RN02

__Informações das Fichas de Débito – Tipo R10__

__Campo 02 – CNPJ do Contribuinte__

Deverá ser gravado nas posições 4 a 17 o CNPJ do Contribuinte\. Essa informação deverá ser recuperada a partir do campo CNPJ da tabela ESTABELECIMENTO do estabelecimento informado no campo “Estabelecimento” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN03

__Informações das Fichas de Débito – Tipo R10__

__Campo 03 – MOFG – Mês de Ocorrência do Fato Gerador__

Deverá ser gravado nas posições 18 a 23 o Mês de Ocorrência do Fato Gerador\. Essa informação deverá ser recuperada a partir dos campos “Ano” e “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN04

__Informações das Fichas de Débito – Tipo R10__

__Campo 04 – Situação__

Deverá ser gravada nas posições 24 a 24 a Situação da DCTF\. A Situação da DCTF deverá ser recuperada a partir do campo “Tipo Situação” da tela de Dados Iniciais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Estabelecimento\.

- Gravar “0”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Não se aplica \(normal\)”\.
- Gravar “1”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Extinção”\.
- Gravar “2”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Fusão”\.
- Gravar “3”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporada”
- Gravar “4”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporadora”\.
- Gravar “5”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão total”\. 
- Gravar “6”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão parcial”\. 

OS3267\-B1

# RN05

__Informações das Fichas de Débito – Tipo R10__

__Campo 05 – Data do Evento__

Deverá ser gravada nas posições 25 a 32 a Data do Evento\. Essa informação deverá ser recuperada a partir do campo “Data do Evento” da parametrização de Dados Iniciais do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento de acordo com o Estabelecimento informado na tela de Pagamento de Débitos\.

A Data deverá ser gravada no formato AAAAMMDD\.

OS3267\-B1

# RN06

__Informações das Fichas de Débito – Tipo R10__

__Campo 06 – Grupo de Tributo__

Deverá ser gravado nas posições 33 a 34 o Grupo de Tributo da DCTF\. Essa informação deverá ser recuperada a partir do campo “Grupo Tributo” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN07

__Informações das Fichas de Débito – Tipo R10__

__Campo 07 – Código da Receita__

Deverá ser gravado nas posições 35 a 40 o Código de Receita da DCTF\. Essa informação deverá ser recuperada a partir do campo “Receita” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN08

__Informações das Fichas de Débito – Tipo R10__

__Campo 08 – Periodicidade__

Deverá ser gravada nas posições 41 a 41 a Periodicidade da Retenção\. Essa informação deve ser recuperada de acordo com o campo “Periodicidade” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN09

__Informações das Fichas de Débito – Tipo R10__

__Campo 09 – Ano do Período da Apuração__

Deverá ser gravado nas posições 42 a 45 o Ano do Período da Apuração\. Essa informação deve ser recuperada de acordo com o campo “Ano” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN10

__Informações das Fichas de Débito – Tipo R10__

__Campo 10 – Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração__

Deverá ser gravado nas posições 46 a 47 o Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração\. Essa informação deve ser recuperada do campo “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN11

__Informações das Fichas de Débito – Tipo R10__

__Campo 11 – Dia/Semana/Quinzena/Decêndio do Período de Apuração__

Deverá ser gravado nas posições 48 a 49 o Dia/Semana/Quinzena/Decêndio do Período de Apuração\. Esse campo deve ser recuperado a partir do campo “Dia” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN12

__Informações das Fichas de Débito – Tipo R10__

__Campo 12 – Ordem do Estabelecimento__

Deverá ser gravada nas posições 50 a 55 a Ordem do Estabelecimento\. 

__\[ALTERADA – CH4182\_2014\]__

__Tratamento:__

Aplica\-se somente ao IPI e CIDE, ou seja, quando o campo Grupo Tributo da Ficha de Débito \(campo grp\_tributo da tabela dct\_ficha\_deb\), localizado no módulo OTF, no menu Outras Obrigações\\ DCTF\\ DCTF Mensal \(a partir de 01/01/2006\)\\ Digitação da Ficha de Débito, for igual a 03 ou 29, caso contrário preencher com zeros para os demais\.

OS3267\-B1

CH4182\_2014

# RN13

__Informações das Fichas de Débito – Tipo R10__

__Campo 13 – CNPJ da Incorporação__

Deverá ser gravado nas posições 56 a 69 o CNPJ da Incorporação\. 

__\[ALTERADA – CH4182\_2014\]__

__Tratamento:__

Aplica\-se somente ao RET, ou seja, quando o campo Grupo Tributo da Ficha de Débito \(campo grp\_tributo da tabela dct\_ficha\_deb\), localizado no módulo OTF, no menu Outras Obrigações\\ DCTF\\ DCTF Mensal \(a partir de 01/01/2006\)\\ Digitação da Ficha de Débito, for igual a 10, caso contrário preencher com zeros para os demais\.

OS3267\-B1

CH4182\_2014

# RN14

__Informações das Fichas de Débito – Tipo R10__

__Campo 14 – Reservado__

Deverá ser gravado nas posições 70 a 70 o valor “0”\.

OS3267\-B1

# RN15

__Informações das Fichas de Débito – Tipo R10__

__Campo 15 – Valor do Débito__

Deverá ser gravado nas posições 71 a 84 o Valor do Débito da Retenção\. Essa informação deve ser recuperada do campo “Valor Débito” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN16

__Informações das Fichas de Débito – Tipo R10__

__Campo 16 – Balanço de Redução__

Deverá ser gravado nas posições 85 a 85 o Balanço de Redução\. Essa informação deve ser recuperada de acordo com a opção informada no campo “Com Balanço de Redução” da tela de Geração da DCTF ou por Empresa ou por Estabelecimento \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento de acordo com o Estabelecimento informado na tela de Pagamento de Débitos 

A regra para gravação é a seguinte:

- Caso a opção selecionada seja “Sem Balanço de Redução”, gravar “0”
- Caso a opção selecionada seja “Com Balanço de Redução”, gravar “1”

OS3267\-B1

# RN17

__Informações das Fichas de Débito – Tipo R10__

__Campo 17 – O saldo desse débito será dividido em quotas__

Deverá ser gravado nas posições 86 a 86 se o saldo do débito será dividido em quotas\. Essa informação deve ser recuperada de acordo com a opção informada no campo “Saldo Dividido” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

A regra para gravação é a seguinte:

- Caso a opção selecionada seja “Sem Divisão em Quotas”, gravar “0”
- Caso a opção selecionada seja “Com Divisão em Quotas”, gravar “0” também\.

__OBS:__ Será necessário que mesmo que o usuário selecione a opção “Com Divisão em Quotas” seja gravado “0” ao invés de “1” porque a solução não contempla divisão em quotas\. 

OS3267\-B1

# RN18

__Informações das Fichas de Débito – Tipo R10__

__Campo 18 – Reservado__

Deverá ser gravado nas posições 87 a 87 deverá ser gravado “0”\.

OS3267\-B1

# RN19

__Informações das Fichas de Débito – Tipo R10__

__Campo 19 – Débito de SCP/INC__

Deverá ser gravado nas posições 88 a 88 se há débito de SCP/INC\. Essa informação deve ser recuperada de acordo com a parametrização de Dados Iniciais da DCTF \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa __OU__ Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento\) de acordo com o Estabelecimento informado na tela de Pagamento de Débitos\.

A regra para gravação é a seguinte:

- Caso o campo “PJ com Débitos de SCP a serem Declarados” esteja selecionado e o campo “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” __NÃO__ esteja selecionado, gravar “1”;
- Caso o campo “PJ com Débitos de INC a serem Declarados” esteja selecionado e o campo “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” __NÃO__ esteja selecionado, gravar “2”;
- Caso nenhuma das opções anteriores esteja selecionada, gravar “0
- Caso o campo “PJ com Débitos de SCP a serem Declarados” __NÃO __esteja selecionado __E__ o campo “PJ com Débitos de INC a serem Declarados” __NÃO__ esteja selecionado __E__ o campo “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” __NÃO__ esteja selecionado, gravar “0”\.

Caso o parâmetro “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” esteja selecionado, o sistema irá gravar o campo 19 de acordo com a Parametrização de SCP/INC, por Código de Receita\.

O sistema irá verificar o Código de Receita da Ficha R10 \(ver RN07\) e irá verificar o campo “Débito de SCP/INC” da tela de Parametrização de SCP/INC\. 

A regra para gravação é a seguinte:

- Caso o campo “Débito de SCP/INC” esteja selecionado com a opção “SCP”, gravar “1”;
- Caso o campo “Débito de SCP/INC” esteja selecionado com a opção “INC”, gravar “2”;
- Caso o campo “Débito de SCP/INC” esteja selecionado com a opção “Não é SCP nem INC”, gravar “0”;

OS3267\-B1

OS4259

CH21391\_2014

# RN20

__Informações das Fichas de Débito – Tipo R10__

__Campo 20 – Reservado__

Deverá ser gravado nas posições 89 a 98 deverá ser gravados espaços em branco\.

OS3267\-B1

# RN21

__Informações das Fichas de Débito – Tipo R10__

__Campo 21 – Delimitador de Registro__

Deverá ser gravado nas posições 99 a 100 o delimitador do registro \(EOL – End of Line\)\.

OS3267\-B1

# RN22

__Pagamentos com DARF – R11__

__Campo 01 – Tipo__

Deverá ser gravado nas posições 1 a 3 o texto “R11”\.

OS3267\-B1

# RN23

__Pagamentos com DARF – R11__

__Campo 02 – CNPJ do Contribuinte__

Deverá ser gravado nas posições 4 a 17 o CNPJ do Contribuinte\. Essa informação deverá ser recuperada a partir do campo CNPJ da tabela ESTABELECIMENTO do estabelecimento informado no campo “Estabelecimento” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN24

__Pagamentos com DARF – R11__

__Campo 03 – MOFG – Mês de Ocorrência do Fato Gerador__

Deverá ser gravado nas posições 18 a 23 o Mês de Ocorrência do Fato Gerador\. Essa informação deverá ser recuperada a partir dos campos “Ano” e “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN25

__Pagamentos com DARF – R11__

__Campo 04 – Situação__

Deverá ser gravada nas posições 24 a 24 a Situação da DCTF\. A Situação da DCTF deverá ser recuperada a partir do campo “Tipo Situação” da tela de Dados Iniciais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Estabelecimento\.

- Gravar “0”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Não se aplica \(normal\)”\.
- Gravar “1”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Extinção”\.
- Gravar “2”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Fusão”\.
- Gravar “3”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporada”
- Gravar “4”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporadora”\.
- Gravar “5”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão total”\. 
- Gravar “6”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão parcial”\. 

OS3267\-B1

# RN26

__Pagamentos com DARF – R11__

__Campo 05 – Data do Evento__

Deverá ser gravada nas posições 25 a 32 a Data do Evento\. Essa informação deverá ser recuperada a partir do campo “Data do Evento” da parametrização de Dados Iniciais do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento de acordo com o Estabelecimento informado na tela de Pagamento de Débitos\.

A Data deverá ser gravada no formato AAAAMMDD\.

OS3267\-B1

# RN27

__Pagamentos com DARF – R11__

__Campo 06 – Grupo de Tributo__

Deverá ser gravado nas posições 33 a 34 o Grupo de Tributo da DCTF\. Essa informação deverá ser recuperada a partir do campo “Grupo Tributo” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN28

__Pagamentos com DARF – R11__

__Campo 07 – Código da Receita__

Deverá ser gravado nas posições 35 a 40 o Código de Receita da DCTF\. Essa informação deverá ser recuperada a partir do campo “Receita” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN29

__Pagamentos com DARF – R11__

__Campo 08 – Periodicidade__

Deverá ser gravada nas posições 41 a 41 a Periodicidade da Retenção\. Essa informação deve ser recuperada de acordo com o campo “Periodicidade” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN30

__Pagamentos com DARF – R11__

__Campo 09 – Ano do Período da Apuração__

Deverá ser gravado nas posições 42 a 45 o Ano do Período da Apuração\. Essa informação deve ser recuperada de acordo com o campo “Ano” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN31

__Pagamentos com DARF – R11__

__Campo 10 – Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração__

Deverá ser gravado nas posições 46 a 47 o Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração\. Essa informação deve ser recuperada do campo “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN32

__Pagamentos com DARF – R11__

__Campo 11 – Dia/Semana/Quinzena/Decêndio do Período de Apuração__

Deverá ser gravado nas posições 48 a 49 o Dia/Semana/Quinzena/Decêndio do Período de Apuração\. Esse campo deve ser recuperado a partir do campo “Dia” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B1

# RN33

__Pagamentos com DARF – R11__

__Campo 12 – Ordem do Estabelecimento__

Deverá ser gravada nas posições 50 a 55 a Ordem do Estabelecimento\.

__\[ALTERADA – CH4182\_2014\]__

__Tratamento:__

Aplica\-se somente ao IPI e CIDE, ou seja, quando o campo Grupo Tributo da Ficha de Débito \(campo grp\_tributo da tabela dct\_ficha\_deb\), localizado no módulo OTF, no menu Outras Obrigações\\ DCTF\\ DCTF Mensal \(a partir de 01/01/2006\)\\ Digitação da Ficha de Débito, for igual a 03 ou 29, caso contrário preencher com zeros para os demais\.

OS3267\-B1

CH24960\_2013

CH4182\_2014

# RN34

__Pagamentos com DARF – R11__

__Campo 13 – CNPJ da Incorporação__

Deverá ser gravado nas posições 56 a 69 o CNPJ da Incorporação\. 

__\[ALTERADA – CH4182\_2014\]__

__Tratamento:__

Aplica\-se somente ao RET, ou seja, quando o campo Grupo Tributo da Ficha de Débito \(campo grp\_tributo da tabela dct\_ficha\_deb\), localizado no módulo OTF, no menu Outras Obrigações\\ DCTF\\ DCTF Mensal \(a partir de 01/01/2006\)\\ Digitação da Ficha de Débito, for igual a 10, caso contrário preencher com zeros para os demais\.

OS3267\-B1

CH4182\_2014

# RN35

__Pagamentos com DARF – R11__

__Campo 14 – Reservado__

Deverá ser gravado nas posições 70 a 70 o valor “0”\.

OS3267\-B1

# RN36

__Pagamentos com DARF – R11__

__Campo 15 – Período de Apuração__

Deverá ser gravado nas posições 71 a 78 o Período de Apuração do DARF\. Essa informação deverá ser recuperada do campo ”Data Apuração” da tela de Pagamento de Débitos, quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total\. A data deve ser gravada no formato DDMMAAAA\.

OS3267\-B1

# RN37

__Pagamentos com DARF – R11__

__Campo 16 – CNPJ do DARF__

Deverá ser gravado nas posições 79 a 92 o CNPJ do DARF\. Essa informação deverá ser recuperada a partir do campo CNPJ da tabela ESTABELECIMENTO de acordo com o Estabelecimento informado na tela de Pagamento dos Débitos\.

OS3267\-B1

# RN38

__Pagamentos com DARF – R11__

__Campo 17 – Código da Receita do DARF__

Deverá ser gravado nas posições 93 a 96 o Código da Receita do DARF\. Essa informação deverá ser recuperada a partir do campo “Darf” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN39

__Pagamentos com DARF – R11__

__Campo 18 – Data de Vencimento__

Deverá ser gravada nas posições 97 a 104 a Data de Vencimento do DARF\. Essa informação deverá ser recuperada a partir do campo “Data Vencimento” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN40

__Pagamentos com DARF – R11__

__Campo 19 – Nº de Referência__

Deverá ser gravado nas posições 105 a 121 o Nº de Referência do DARF\. Essa informação deverá ser recuperada a partir do campo “Número Referência” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN41

__Pagamentos com DARF – R11__

__Campo 20 – Valor do Principal__

Deverá ser gravado nas posições 122 a 135 o Valor do Principal do DARF\. Essa informação deverá ser recuperada a partir do campo “Valor Principal” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN42

__Pagamentos com DARF – R11__

__Campo 21 – Valor da Multa__

Deverá ser gravado nas posições 136 a 149 o Valor da Multa do DARF\. Essa informação deverá ser recuperada a partir do campo “Valor Multa” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN43

__Pagamentos com DARF – R11__

__Campo 22 – Valor dos Juros__

Deverá ser gravado nas posições 150 a 163 o Valor dos Juros\. Essa informação deverá ser recuperada do campo “Valor Juros” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN44

__Pagamentos com DARF – R11__

__Campo 23 – Valor pago do Débito__

Deverá ser gravado nas posições 167 a 177 o Valor pago do Débito\. Essa informação deverá ser recuperada do campo “Valor Pagamento” da tela de Pagamento dos Débitos quando o campo “Selecionar Pagamento” = “Pagamento do Débito Total”\.

OS3267\-B1

# RN45

__Pagamentos com DARF – R11__

__Campo 24 – Reservado__

Deverá ser gravado nas posições 178 a 187 deverá ser gravados espaços em branco\.

OS3267\-B1

# RN46

__Pagamentos com DARF – R11__

__Campo 25 – Delimitador de Registro__

Deverá ser gravado nas posições 188 a 189 o delimitador do registro \(EOL – End of Line\)\.

OS3267\-B1

# RN47

__Compensação de Pagamento Indevido ou a Maior – R12__

__Compensação de Pagamento Indevido ou a Maior – Tipo R12__

__Campo 1 – Tipo__

Deverá ser gravado nas posições 1 a 3 o texto “R12”\.

OS3267\-B2

# RN48

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 02 – CNPJ do Contribuinte__

Deverá ser gravado nas posições 4 a 17 o CNPJ do Contribuinte\. Essa informação deverá ser recuperada a partir do campo CNPJ da tabela ESTABELECIMENTO do estabelecimento informado no campo “Estabelecimento” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN49

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 03 – MOFG – Mês de Ocorrência do Fato Gerador__

Deverá ser gravado nas posições 18 a 23 o Mês de Ocorrência do Fato Gerador\. Essa informação deverá ser recuperada a partir dos campos “Ano” e “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN50

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 04 – Situação__

Deverá ser gravada nas posições 24 a 24 a Situação da DCTF\. A Situação da DCTF deverá ser recuperada a partir do campo “Tipo Situação” da tela de Dados Iniciais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Estabelecimento\.

- Gravar “0”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Não se aplica \(normal\)”\.
- Gravar “1”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Extinção”\.
- Gravar “2”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Fusão”\.
- Gravar “3”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporada”
- Gravar “4”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporadora”\.
- Gravar “5”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão total”\. 
- Gravar “6”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão parcial”\. 

OS3267\-B2

# RN51

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 05 – Data do Evento__

Deverá ser gravada nas posições 25 a 32 a Data do Evento\. Essa informação deverá ser recuperada a partir do campo “Data do Evento” da parametrização de Dados Iniciais do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento de acordo com o Estabelecimento informado na tela de Pagamento de Débitos\.

A Data deverá ser gravada no formato AAAAMMDD\.

OS3267\-B2

# RN52

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 06 – Grupo de Tributo__

Deverá ser gravado nas posições 33 a 34 o Grupo de Tributo da DCTF\. Essa informação deverá ser recuperada a partir do campo “Grupo Tributo” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN53

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 07 – Código da Receita__

Deverá ser gravado nas posições 35 a 40 o Código de Receita da DCTF\. Essa informação deverá ser recuperada a partir do campo “Receita” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN54

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 08 – Periodicidade__

Deverá ser gravada nas posições 41 a 41 a Periodicidade da Retenção\. Essa informação deve ser recuperada de acordo com o campo “Periodicidade” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN55

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 09 – Ano do Período da Apuração__

Deverá ser gravado nas posições 42 a 45 o Ano do Período da Apuração\. Essa informação deve ser recuperada de acordo com o campo “Ano” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN56

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 10 – Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração__

Deverá ser gravado nas posições 46 a 47 o Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração\. Essa informação deve ser recuperada do campo “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN57

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 11 – Dia/Semana/Quinzena/Decêndio do Período de Apuração__

Deverá ser gravado nas posições 48 a 49 o Dia/Semana/Quinzena/Decêndio do Período de Apuração\. Esse campo deve ser recuperado a partir do campo “Dia” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN58

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 12 – Ordem do Estabelecimento__

Deverá ser gravada nas posições 48 a 49 a Ordem do Estabelecimento\. 

OS3267\-B2

# RN59

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 13 – CNPJ da Incorporação__

Deverá ser gravado nas posições 56 a 69 o CNPJ da Incorporação\. 

OS3267\-B2

# RN60

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 14 – Reservado__

Deverá ser gravado nas posições 70 a 70 o valor “0”\.

OS3267\-B2

# RN61

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 15 – Valor Compensado do Débito__

Deverá ser gravado nas posições 71 a 84 o Valor Compensado do Débito\. Essa informação deverá ser recuperada do campo “Vlr Compensação” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\) quando o campo “Selecionar Pagamento” = “Compensação de Pagamento Indevido ou a Maior”\.

Essa informação deverá ser recuperada do campo “Valor Utilizado” da aba de Compensação do DARF \(X75\_DCTF\) ou DARF Complementar \(X751\_DCTF\_COMPL\) na tela de Manutenção dos DARF’s \(menu: Outras Obrigações >> DARF’s >> Manutenção\)\. O campo a ser recuperado é o VLR\_PRINC\_DEVIDO\_COMP da tabela CTRL\_COMPENSACAO\_CRED\.

Essa informação deverá ser gravada também no campo “Vlr\. Compensação” quando a opção Selecionar Pagamento = Compensação de Pagamento Indevido ou a Maior na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

OS3267\-B2

# RN62

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 16 – Formalização do Pedido__

Deverá ser gravada nas posições 85 a 85 a Formalização do Pedido\. Essa informação deve ser recuperada a partir do campo “Formalização Pedido” quando a opção Selecionar Pagamento = Compensação de Pagamento Indevido ou a Maior na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

A informação deverá ser gravada da seguinte forma:

- Gravar “1” caso a opção selecionada seja “Processo Administrativo”
- Gravar “3” caso a opção selecionada seja “Dcomp”
- Gravar “4” caso a opção selecionada seja “Dcomp com Direito Creditório Reconhecido em Processo”

OS3267\-B2

# RN63

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 17 – Número do PERDCOMP ou Processo__

Deverá ser gravado nas posições 86 a 109 o Número do PERDCOMP ou Processo\. Essa informação deve ser recuperada a partir do campo “Nº Processo/Dcomp” quando a opção Selecionar Pagamento = Compensação de Pagamento Indevido ou a Maior na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

OS3267\-B2

# RN64

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 18 – Reservado__

Deverá ser gravado nas posições 110 a 119 espaços em branco\.

OS3267\-B2

# RN65

__Compensação de Pagamento Indevido ou a Maior – R12__

__Campo 19 – Delimitador de Registro__

Deverá ser gravado nas posições 120 a 121 o delimitador do registro \(EOL – End of Line\)\.

OS3267\-B2

# RN66

__Outras Compensações – Tipo R13__

__Campo 01 – Tipo__

Deverá ser gravado nas posições 1 a 3 o texto “R13”\.

OS3267\-B2

# RN67

__Outras Compensações – Tipo R13__

__Campo 02 – CNPJ do Contribuinte__

Deverá ser gravado nas posições 4 a 17 o CNPJ do Contribuinte\. Essa informação deverá ser recuperada a partir do campo CNPJ da tabela ESTABELECIMENTO do estabelecimento informado no campo “Estabelecimento” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN68

__Outras Compensações – Tipo R13__

__Campo 03 – MOFG – Mês de Ocorrência do Fato Gerador__

Deverá ser gravado nas posições 18 a 23 o Mês de Ocorrência do Fato Gerador\. Essa informação deverá ser recuperada a partir dos campos “Ano” e “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN69

__Outras Compensações – Tipo R13__

__Campo 04 – Situação__

Deverá ser gravada nas posições 24 a 24 a Situação da DCTF\. A Situação da DCTF deverá ser recuperada a partir do campo “Tipo Situação” da tela de Dados Iniciais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Estabelecimento\.

- Gravar “0”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Não se aplica \(normal\)”\.
- Gravar “1”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Extinção”\.
- Gravar “2”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Fusão”\.
- Gravar “3”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporada”
- Gravar “4”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Incorporação/Incorporadora”\.
- Gravar “5”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão total”\. 
- Gravar “6”, caso o parâmetro “Tipo Situação” esteja preenchido com a informação “Cisão parcial”\. 

OS3267\-B2

# RN70

__Outras Compensações – Tipo R13__

__Campo 05 – Data do Evento__

Deverá ser gravada nas posições 25 a 32 a Data do Evento\. Essa informação deverá ser recuperada a partir do campo “Data do Evento” da parametrização de Dados Iniciais do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento de acordo com o Estabelecimento informado na tela de Pagamento de Débitos\.

A Data deverá ser gravada no formato AAAAMMDD\.

OS3267\-B2

# RN71

__Outras Compensações – Tipo R13__

__Campo 06 – Grupo de Tributo__

Deverá ser gravado nas posições 33 a 34 o Grupo de Tributo da DCTF\. Essa informação deverá ser recuperada a partir do campo “Grupo Tributo” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN72

__Outras Compensações – Tipo R13__

__Campo 07 – Código da Receita__

Deverá ser gravado nas posições 35 a 40 o Código de Receita da DCTF\. Essa informação deverá ser recuperada a partir do campo “Receita” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN73

__Outras Compensações – Tipo R13__

__Campo 08 – Periodicidade__

Deverá ser gravada nas posições 41 a 41 a Periodicidade da Retenção\. Essa informação deve ser recuperada de acordo com o campo “Periodicidade” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN74

__Outras Compensações – Tipo R13__

__Campo 09 – Ano do Período da Apuração__

Deverá ser gravado nas posições 42 a 45 o Ano do Período da Apuração\. Essa informação deve ser recuperada de acordo com o campo “Ano” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN75

__Outras Compensações – Tipo R13__

__Campo 10 – Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração__

Deverá ser gravado nas posições 46 a 47 o Mês/Bimestre/Trimestre/Quadrimestre/Semestre do Período de Apuração\. Essa informação deve ser recuperada do campo “Mês” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN76

__Outras Compensações – Tipo R13__

__Campo 11 – Dia/Semana/Quinzena/Decêndio do Período de Apuração__

Deverá ser gravado nas posições 48 a 49 o Dia/Semana/Quinzena/Decêndio do Período de Apuração\. Esse campo deve ser recuperado a partir do campo “Dia” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

OS3267\-B2

# RN77

__Outras Compensações – Tipo R13__

__Campo 12 – Ordem do Estabelecimento__

Deverá ser gravada nas posições 48 a 49 a Ordem do Estabelecimento\. 

OS3267\-B2

# RN78

__Outras Compensações – Tipo R13__

__Campo 13 – CNPJ da Incorporação__

Deverá ser gravado nas posições 56 a 69 o CNPJ da Incorporação\. 

OS3267\-B2

# RN79

__Outras Compensações – Tipo R13__

__Campo 14 – Reservado__

Deverá ser gravado nas posições 70 a 70 o valor “0”\.

OS3267\-B2

# RN80

__Outras Compensações – Tipo R13__

__Campo 15 – Tipo de Crédito__

Deverá ser gravado nas posições 71 a 72 o Tipo de Crédito de acordo com a opção informada no campo “Tipo de Crédito” de acordo com a opção “Outras Compensações” do campo “Selecionar Pagamento” da tela de Pagamento de Débitos – menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos do módulo Obrigações de Tributos Federais\.

Essa informação é gravada de acordo com a opção selecionada no campo “Tipo do Crédito” da tela de manutenção do Saldo Credor \(menu: Outras Obrigações >> DARF’s >> Saldo Credor para Compensação dos Tributos Federais\)\. Caso o DARF gerado no R11 tenha sido compensado com um crédito oriundo dessa tela de manutenção citada anteriormente, a compensação será gerada no R13 e não no R12\.

De acordo com o DE/PARA abaixo, a informação será gravada nesse campo:

- Gravar “01”, caso a opção seja “Ressarcimento de IPI”
- Gravar “02”, caso a opção seja “IRPJ Saldo Negativo Per\. Anteriores – Próprio”
- Gravar “03”, caso a opção seja “IRPJ Saldo Negativo Per\. Anteriores – Sucedida”
- Gravar “04”, caso a opção seja “CSLL Saldo Negativo Per\. Anteriores – Próprio”
- Gravar “05”, caso a opção seja “CSLL Saldo Negativo Per\. Anteriores – Sucedida”
- Gravar “06”, caso a opção seja “IRRF Cooperativas de Trabalho”
- Gravar “07”, caso a opção seja “IRRF Juros sobre o Capital Próprio”
- Gravar “11”, caso a opção seja “Outros”
- Gravar “12”, caso a opção seja “PIS/PASEP Não\-Cumulativo – Exportação”
- Gravar “13”, caso a opção seja “Cofins Não\-Cumulativa – Exportação”
- Gravar “14”, caso a opção seja “PIS/PASEP Não\-Cumulativo \- Mercado Interno”
- Gravar “15”, caso a opção seja “Cofins Não\-Cumulativa \- Mercado Interno”
- Gravar “16”, caso a opção seja “PIS/PASEP Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)”
- Gravar “17”, caso a opção seja “Cofins Embalagens \(§4º do art\. 51 da Lei nº 10\.833/03\)”

Deverá ser exibido o registro para que o usuário possa realizar a manutenção do mesmo\. O registro “Outras Compensações – R13” não será gerado\.

OS3267\-B2

# RN81

__Outras Compensações – Tipo R13__

__Campo 16 – Valor Compensado do Débito__

Deverá ser gravado nas posições 73 a 86 o Valor Compensado do Débito\. Essa informação deverá ser recuperada do campo “Vlr Compensação” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\) quando o campo “Selecionar Pagamento” = “Outras Compensações”\.

Essa informação deverá ser recuperada do campo “Valor Utilizado” da aba de Compensação do DARF \(X75\_DCTF\) ou DARF Complementar \(X751\_DCTF\_COMPL\) na tela de Manutenção dos DARF’s \(menu: Outras Obrigações >> DARF’s >> Manutenção\)\.

Essa informação deverá ser gravada também no campo “Vlr\. Compensação” quando a opção Selecionar Pagamento = Outras Compensações na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

OS3267\-B2

# RN82

__Outras Compensações – Tipo R13__

__Campo 17 – Formalização do Pedido__

Deverá ser gravado nas posições 87 a 87 a Formalização do Pedido\. Essa informação será recuperada do campo “Formalização Pedido” quando a opção Selecionar Pagamento = Outras Compensações na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

A informação será gravada da seguinte maneira:

- Gravar “1” caso a opção seja “Processo Administrativo”
- Gravar “3” caso a opção seja “DComp

Por default ao gerar a DCTF e existir ficha para “Outras Compensações”, gravar “DComp”\.

OS3267\-B2

# RN83

__Outras Compensações – Tipo R13__

__Campo 18 – Número do PERDCOMP ou Processo__

Deverá ser gravado nas posições 88 a 111 o Número do PERDCOMP ou Processo\. Essa informação será recuperada do campo “Nº Processo/Dcomp” quando a opção Selecionar Pagamento = Outras Compensações na tela de Pagamento de Débitos, localizado no menu: Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Pagamento de Débitos\.

Para que esse campo acima citado seja gravado com sucesso, essa informação será recuperada quando o DARF gerado no registro de Pagamentos com DARF – R11 imediatamente anterior tenha sido compensado com um crédito oriundo da tela de manutenção de Saldo Credor \(menu: Outras Obrigações >> DARF’s >> Saldo Credor para Compensação de Tributos Federais\)\. Para que o campo seja recuperado a informação deverá ser recuperada do campo “Número do Processo” da tela de manutenção do Saldo Credor\.

OS3267\-B2

# RN84

__Outras Compensações – Tipo R13__

__Campo 19 – Reservado__

Deverá ser gravado nas posições 112 a 121 espaços em branco\.

OS3267\-B2

# RN85

__Outras Compensações – Tipo R13__

__Campo 20 – Delimitador de Registro__

Deverá ser gravado nas posições 122 a 123 o delimitador de registro EOL – End Of Line\.

OS3267\-B2

# RN86

Sempre que o usuário abrir a tela de Geração da Declaração dos Débitos e Créditos \(geração do Meio Magnético\), irá visualizar a seguinte mensagem:

“Antes de iniciar a geração do Meio Magnético da DCTF, por gentileza verificar se o Número do Processo e/ou Tipo de Crédito referente às Compensações das fichas “Compensações de Pagamentos Indevidos ou a Maior” e/ou “Outras Compensações” foram preenchidos na tela de Pagamento de Débitos\. Caso essas informações não estejam preenchidas, o arquivo pode não ser validado com sucesso no programa da Receita Federal\.”

Essa mensagem será sempre exibida para o usuário na abertura da tela\. Essa condição não irá fazer nenhuma verificação se essas informações existem ou não\. A única opção disponível da mensagem deverá ser o botão “OK”\.

OS3267\-B2

# RN87

__Dados dos Responsáveis pela Pessoa Jurídica – Tipo R03__

__Campo 17 – UF do CRC – Responsável__

Deverá ser gravado nas posições 259 a 260 a UF do CRC do Responsável Legal\. Essa informação deve ser recuperada a partir do campo “Responsável Contador” da tela de Dados Iniciais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Dados Iniciais >> Por Empresa OU Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Dados Iniciais >> Por Estabelecimento\) do módulo Obrigações de Tributos Federais\.

Com o responsável informado, deve\-se recuperar o mesmo na tela de Responsável Legal \(menu: Requisitos Legais >> Responsável pelas Informações\) do módulo Parâmetros\.

A partir do Responsável Legal deve\-se gravar nesse campo 17 do registro R03 da DCTF a informação contida no campo “CRC UF”\.

CH18020\_2012

# RN88

__Parcelamento – Tipo R15__

__Regra Geral:__

No registro R15 são gerados os Parcelamentos de Débito pertencentes às fichas de débito do mês da declaração\. 

Não são consideradas os parcelamentos das fichas de débito com Código de Receita de periodicidade Trimestral\. Pois tais parcelamentos são apresentados no R25, da declaração do último mês do trimestre seguinte\. Vide RN89\.

Os Parcelamentos de Débito são inseridos manualmente vide menu: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débito\.

MFS43100

# RN89

__Débito Apurado e Creditos Vinculados do Trimestre Anterior – Tipo R20__

__Regra Geral:__

Esse registro é gerado apenas para as declarações de meses de competência 03 \- março, 06 \- junho, 09 \- setembro ou 12 \-dezembro\.

As fichas de débito, cuja localização de menu é Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Digitação das Fichas de Débito,  do trimestre anterior, que atendam aos critérios abaixo serão apresentadas no R20:

\- Mes da Declaração = último mês do trimestre anterior ao mes da declaração que está sendo entregue\. Exemplo, se a declaração é de dezembro, as fichas de débito de setembro são consideradas\.

 \- Grupo Tributo = 01 – IRPJ ou 05 – CSLL

 \- Código de Receita = qualquer receita que tenha periodicidade trimestral\. Exemplo 208901\.

 \- Saldo Dividido = com divisão de quotas

 \- Valor do Débito > 2\.000,00

A ficha de débito deve possuir um Pagamento de Débito Total o Parcial, vide menu: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débito\.

MFS43100

# RN90

__Parcelamento – Tipo R25__

__Regra Geral:__

Esse registro é gerado apenas para as declarações de meses de competência 03 \- março, 06 \- junho, 09 \- setembro ou 12 \-dezembro\.

No registro R25 são gerados os Parcelamentos de Débito pertencentes às fichas de débito do trimestre anterior, que atendam as regras de geração do Registro R20 \(vide RN88\)\.

Os Parcelamentos de Débito são inseridos manualmente vide menu: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débito\.

MFS43100

# RN91

__Header da Declaração__

Para declarações de períodos anteriores a 1º agosto de 2014, a versão da DCTF válida é a 2\.5\.

Para declarações de períodos a partir de 1º agosto de 2014, a versão da DCTF válida é a 3\.5 \(subtituiu a versão 3\.4\)\.

Para declarações de períodos a partir de 1º agosto de 2014, a versão da DCTF válida é a 3\.7 \(subtituiu a versão 3\.5\)\.

__Campo 09 – Versão__

Deverá ser gravado nas posições 37 a 39 a Versão da DCTF\.

Se mês/ano de competência da Declaração for anterior a 1º agosto de 2014, então:

   O valor a ser gravado deverá ser “250”\.

Se mês/ano de competência da Declaração for igual ou posterior a 1º agosto de 2014, então:

  O valor a ser gravado deverá ser “350”\.

Se mês/ano de competência da Declaração for igual ou posterior a 1º agosto de 2014, então:

  O valor a ser gravado deverá ser “370”\.

OS3699

MFS43100

MFS616327

# RN92

__Dados Cadastrais do Estabelecimento Matriz – Tipo R02__

__Campo 17 – DDD do Fax__

Se o campo “FAX” da tabela “ESTABELECIMENTO” __NÃO __estiver preenchido;

  __NÃO__ preencher o “Campo 17 – DDD do Fax” do Registro Tipo R02\.

MFS58858

# RN93

__Dados dos Responsáveis pela Pessoa Jurídica – Tipo R03__

__Campo 11 – DDD do Fax \- Representante__

Se o campo “NUM\_FAX” da tabela “RESP\_INFORMACAO” __NÃO __estiver preenchido;

  __NÃO__ preencher o “Campo 11 – DDD do Fax – Representante” do Registro Tipo R03\.

MFS58858

# RN94

__Alteração do menu e do título da tela__

__Menu: __

__Dê: __Outras Obrigações > DCTF > DCTF Mensal > Meio Magnético – Declaração de Débito e Crédito > Geração > Por Empresa

__Para: __Outras Obrigações > DCTF/MIT > DCTF Mensal/MIT > Meio Magnético – Declaração de Débito e Crédito e Módulo de Inclusão de Tributos > Geração > Por Empresa

__Dê: __Outras Obrigações > DCTF > DCTF Mensal > Meio Magnético – Declaração de Débito e Crédito > Geração > Por Estabelecimento

__Para: __Outras Obrigações > DCTF/MIT > DCTF Mensal/MIT > Meio Magnético – Declaração de Débito e Crédito e Módulo de Inclusão de Tributos > Geração > Por Estabelecimento

__Título: __

__Dê:__ Geração – Declaração de Débitos e Créditos__ __

__Para: __Geração – Declaração de Débitos e Créditos e Módulo de Inclusão de Tributos

MFS\-758230

# RN95

__Geração DCTF e MIT__

__\[Alteração MFS\-779065\] __A partir de gerações de 2025, será gerado os arquivos da DCTF \(conforme regras existente neste documento\) e apenas o arquivo em formato JSON do MIT, conforme as regras indicadas no arquivo: [https://trten\.sharepoint\.com/sites/REQ\_MTZ/Mastersaf%20DW%20TaxOne/Documento\_Matriz/Federal/Obrigacoes\_de\_Tributos\_Federais/OUTRAS%20OBRIGACOES/DCTF/MIT/MTZ\_OTF\_MIT\_leiaute\_JSON\.docx?web=1](https://trten.sharepoint.com/sites/REQ_MTZ/Mastersaf%20DW%20TaxOne/Documento_Matriz/Federal/Obrigacoes_de_Tributos_Federais/OUTRAS%20OBRIGACOES/DCTF_MIT/MTZ_OTF_MIT_leiaute_JSON.docx?web=1)

MFS\-758230

MFS\-779065

# RN96

__Botão Geração__

Validações:

- Quando o campo ‘VariacoesMonetarias’ preenchido com ‘0\-Não preenchido’ ou ‘4\-Não se Aplica’ ou ‘5\-Sem Alteração do Regime’, exibir a mensagem no log: “VariacoesMonetarias pode ser ‘1\-Regime de Caixa’, ‘2\-Regime de Competência’ ou ‘3\-Regime de Caixa \- Elevada oscilação da taxa de câmbio’\. Favor rever a informação\.”
- Quando o campo ‘RegimePisCofins’, estiver preenchido com ‘0\-Não preenchido’, exibir a mensagem no log: “RegimePisCofins pode ser ‘1\-Não\-cumulativa’; ‘2\- Cumulativa’;‘3\-Não\-cumulativa e Cumulativa ou ‘4\- Não se aplica’ Favor rever a informação\.”
- Se for encontrado algum tributo não aceito pela obrigação, \(tributo diferente de 01\-IRPJ; 02\-IRRF; 03\-IPI; 04\-IOF; 05\-CSLL; 06\-PIS/PASEP; 07\-COFINS; 08\- CPMF; 10\-RET/PA; 29\-CIDE ou 33\-CPSS\) exibir a mensagem no log:"O\(s\) tributo\(s\) "cod\_desc abreviada, cod\_desc abreviada", não é/são válido\(s\) para o MIT\. As opções aceitas são: 01\-IRPJ; 02\-IRRF; 03\-IPI; 04\-IOF; 05\-CSLL; 06\-PIS/PASEP; 07\-COFINS; 08\-CPMF; 10\-RET/PA; 29\-CIDE ou 33\-CPSS"\.

MFS\-779065

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

