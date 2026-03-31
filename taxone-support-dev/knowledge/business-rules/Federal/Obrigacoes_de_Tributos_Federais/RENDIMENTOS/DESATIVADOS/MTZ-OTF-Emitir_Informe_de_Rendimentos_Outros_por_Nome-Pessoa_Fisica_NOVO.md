# MTZ-OTF-Emitir_Informe_de_Rendimentos_Outros_por_Nome-Pessoa_Fisica_NOVO

- **Fonte:** MTZ-OTF-Emitir_Informe_de_Rendimentos_Outros_por_Nome-Pessoa_Fisica_NOVO.docx
- **Modificado:** 2023-03-20
- **Tamanho:** 57 KB

---

# Módulo – Obrigações de Tributos Federais\.

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3579

Obrigações de Tributos Federais – Gerar Informes de Rendimento Outros por Nome de acordo com a IN RFB nº 1\.215, de 15/12/2011 \(Rendimentos Recebidos Acumuladamente\) criados a partir da DIRF 2012

De acordo com a IN 1\.215/2011, o modelo do Informe de Rendimentos para Pessoas Físicas foi alterado para contemplar as novas informações de Rendimentos Recebidos Acumuladamente\. Para essa demanda havia sido criada a OS3532\.

De acordo com o setor de Informação, essa alteração somente era válida para os Informes de Rendimentos dos Empregados \(Funcionários\)\. Em virtude desse entendimento, o escopo não contemplava os Informes de Rendimentos de Terceiros \(Outros\) para Pessoas Físicas\. Esse mesmo entendimento foi alterado após solicitação do cliente Klabin e após uma nova consulta ao setor de Informação que forneceu o seguinte parecer:

  
__*“Sim, o modelo de Informes deve obedecer exatamente ao layout publicado pela IN 1\.215, independente de haver valor declarado\.”*__

Logo os Informes de Rendimentos nas visões – CPF e Nome – deverão ser alterados para contemplar o novo quadro 6 – Rendimentos Recebidos Acumuladamente\.

CH107\_2013

Nome do arquivo pdf

Para os Informes de Rendimentos Outros \(quando utilizado a funcionalidade Enviar e\-mail\), o sistema deve considerar no momento em que o arquivo é salvo a seguinte estrutura: ‘CNPJ da pessoa beneficiária\_Sequencial’\.pdf

OS3996

Obrigações de Tributos Federais – Alteração da cor de fundo dos Informes de Rendimento

Essa OS tem por objetivo, alterar a cor de fundo dos Informes de Rendimento\. Conforme documento de visão da OS3996, foram solicitados os seguintes itens, porém conforme alinhamento com o Sr\. Marcos Paula em 08/10/2013, só será desenvolvido na OS\-3996 a alteração da cor de fundo\.

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

2

PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.

Será tratado na OS\-4000\.

3

Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável

Será tratado na OS\-3997\.

__4__

__Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.__

__Será tratado na OS\-3996\.__

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

Vale salientar que o controle de margem solicitado no item 4, já foi solicitado por outros clientes \(vide OS\-3956\) e há dificuldade técnica para implementação dessa demanda\. Logo esse item não será desenvolvido nessa OS\-3996 \(ver e\-mail sobre a margem anexo junto à demanda\)\.

OS4000

Obrigações de Tributos Federais \- Geração dos Informes de Rendimento Individualizados

Essa OS tem por objetivo, permitir a geração dos informes de rendimento individualizados, ou seja, que para cada informe de rendimento seja gerado um arquivo PDF diferente\. Além disso, será permitido que o usuário parametrize a forma como o nome do informe será disponibilizado\. Para essa OS foram solicitados diversos itens nos documentos de visão, que por sua vez foram segregados em diversas OS’s\. Abaixo seguem essas divisões:

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

__2__

__PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.__

__Será tratado na OS\-4000\.__

3

Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável

Será tratado na OS\-3997\.

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

OS3997

Obrigações de Tributos Federais – Inclusão de logotipo nos Informes de Rendimento

Essa OS tem por objetivo, permitir a inclusão do logotipo da empresa nos Informes de Rendimento\. Conforme documento de visão da OS3996, foram solicitados os seguintes itens, porém conforme alinhamento com o Sr\. Marcos Paula em 08/10/2013, só será desenvolvido na OS\-3997 a inclusão do logotipo nos informes de rendimento\.

Os itens solicitados no documento de visão foram:

__Item__

__Descrição__

__Solução__

1

Criação de uma tabela auxiliar no cadastro de pessoas onde será informado para cada CPF ou CNPJ a suas respectivas classificações\. Exemplo:1 – corretor, 2\- prestador, 3 \- beneficiário\), lembrando que o CPF/CNPJ poderá ter mais de uma classificação\. Tratar e disponibilizar ao usuário a seleção das classificações em tempo de geração dos informes\.

O cliente poderá tratar pelo Código de Operação, conforme informações do Marcos Paula\.

2

PDF Individual: Necessidade de que os informes sejam gerados em PDF individualmente  por CPF/CNPJ, e que o nome do arquivo seja parametrizável\.

Será tratado na OS\-4000\.

__3__

__Logotipo nos informes: Ter funcionalidade de inserir a imagem do logotipo de cada empresa nos informes de forma parametrizável__

__Será tratado na OS\-3997\.__

4

Configuração do Envelope: Ter funcionalidade de definir a cor do fundo do envelope, de forma a não deixar transparecer nenhuma informação sigilosa e também possibilitar a configuração das dobras do envelope, pois dependendo a impressora, a dobra poderá sofrer ajustes\.

Será tratado na OS\-3996\.

5

Informação de Isenção: Alguns beneficiários possuem Isenção em parte da tributação do IRRF a ser apresentado no Informe e Dirf, para composição do valor a ser demonstrado, é preciso ter campos específicos nas retenções para que o tratamento seja feito\.

Tipos de Isenção: Aposentado maior de 65 anos, beneficiário associado a cooperativa de transporte \(Taxi\) e beneficiário portador de moléstia grave\. Este item aplica\-se somente ao Informe de Rendimentos de terceiros \(Pessoa Física\) e aos Registros da Dirf especificos para estas informações\.

Será tratado na OS\-3999\.

Vale salientar que o controle de margem solicitado no item 4, já foi solicitado por outros clientes \(vide OS\-3956\) e há dificuldade técnica para implementação dessa demanda\. Logo esse item não será desenvolvido nessa OS\-3996 \(ver e\-mail sobre a margem anexo junto à demanda\)\.

CH26320\_2013

Gravação da linha 02 do Quadro 03

Tratamento para seleção da linha 02 do Quadro 03 quando a origem for da SAFX53 – Terceiros\.

OS4700

Inclusão da Linha 2 no Quadro 05

“ Imposto sobre a renda retido na fonte sobre 13° salário\.

OS4700

Alteração rodapé referente à Instrução Normativa 1\.522, de 05 de dezembro de 2014\.

Alteração do rodapé referente à Instrução Normativa para seguinte descrição 2014:

Aprovado pela Instrução Normativa RFB nº 1\.522, de 05 de dezembro de 2014, para Rendimentos Outros e Empregados\.

OS4700

Campo “Valor 13° salário”

As informações passam a ser recuperadas da SAFX53

MFS8975

Informe de Rendimento DIRF2017

Alteração do Rodapé\.

MFS7081

Inclusão de parametrização para verso do informe de rendimentos

Inclusão de nova parametrização para o verso do Informe de Rendimentos\.

MFS9876

Informe de Rendimento DIRF2017

Inclusão do Exercício no cabeçalho do informe de rendimento

MFS\-9872

Incluir beneficiários do exterior

Este documento tem como objetivo corrigir a geração dos Informes de Rendimento Outros para considerar beneficiários do exterior\.

MFS\-74070

Esta funcionalidade não estará disponível no Taxone

Não disponibilizar no produto TAXONE, o item de menu Emissão de Declaração de Rendimentos’ e suas respectivas funcionalidades, no módulo Federal / OTF/Rendimentos / Outros 

Este item já estava implementado, apenas refere\-se a atualização de documentação funcional\.

MFS\-77523

Informe de Rendimento 

Alterações realizadas de acordo com a Instrução Normativa n° 2\.060/21, dispondo sobre o Comprovante de Rendimentos Pagos e de Imposto sobre a Renda Retido na Fonte\.

Alterada a RN01, RN04, RN14, RN23, RN24, RN25\. Criada a RN09\.01 e RN32

MFS\-79687

Esta funcionalidade não estará disponível no DW

Não disponibilizar no produto DW, o item de menu Emissão de Declaração de Rendimentos’ e suas respectivas funcionalidades, no módulo Federal / OTF/Rendimentos / Outros 

Este item já estava implementado, apenas refere\-se a atualização de documentação funcional\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

O layout do Informe de Rendimentos Outros deverá ser alterado para que fique igual ao layout proposto pela RFB através da IN RFB 1\.215, de 15 de Dezembro de 2011\.

O layout está disponibilizado no documento de requisito da OS3579\.

__\[ALTERAÇÃO MFS\-77523\]__ Adequação do layout

A Receita Federal do Brasil publicou a Instrução Normativa n° 2\.060/21, dispondo sobre o Comprovante de Rendimentos Pagos e de Imposto sobre a Renda Retido na Fonte\. O Layout está disponível na MFS\-77523\.

__OS3579__

__MFS\-77523__

__RN02__

No logotipo do Ministério da Fazenda – Secretaria da Receita Federal, o texto “SECRETARIA DA RECEITA FEDERAL” deverá ser alterado para “SECRETARIA DA RECEITA FEDERAL DO BRASIL”\.

Abaixo do novo texto – SECRETARIA DA RECEITA FEDERAL DO BRASIL – deverá ser incluído o texto “Imposto sobre a Renda da Pessoa Física”\.

No logotipo – MINISTÉRIO DA FAZENDA e o texto abaixo SECRETARIA DA RECEITA FEDERAL DO BRASIL, deverá ser alterado para: __“MINISTÉRIO DA ECONOMIA”__ e o texto abaixo __“Secretária Especial da Receita Federal do Brasil”__

__OS3579__

__MFS\-77523__

__RN03__

No lado direito ao logo, o texto “COMPROVANTE DE RENDIMENTOS PAGOS E DE RETENÇÃO DE IMPOSTO DE RENDA NA FONTE” deverá ser alterado para “COMPROVANTE DE RENDIMENTOS PAGOS E DE IMPOSTO SOBRE A RENDA RETIDO NA FONTE”\.

__OS3579__

__RN04__

Antes do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, deverá ser incluída uma mensagem no Informe de Rendimentos com a seguinte informação:

__“Verifique as condições e o prazo para a apresentação da Declaração do Imposto sobre a Renda da Pessoa Física para este ano\-calendário no sítio da Secretaria da Receita Federal do Brasil na Internet, no endereço <__[__www\.receita\.fazenda\.gov\.br__](http://www.receita.fazenda.gov.br)__>\.”__

__\[ALTERAÇÃO MFS\-77523\]__ Adequação do layout

__“Verifique as condições e o prazo para a apresentação da Declaração do Imposto sobre a Renda da Pessoa Física para este ano\-calendário no sítio da Secretaria Especial da Receita Federal do Brasil na Internet, no endereço <https://www\.gov\.br/receitafederal/pt\-br>\.”__

__OS3579__

__MFS\-77523__

__RN05__

No quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, o campo “Nome Empresarial/Nome” deverá ser alterado para “Nome Empresarial/Nome Completo”\.

__OS3579__

__RN06__

Os campos “CNPJ/CPF” e “Nome Empresarial/Nome Completo” do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, deverão ser invertidos de ordem\.

__OS3579__

__RN07__

Os campos “Endereço”, “Cidade”, “UF” e “Telefone”, deverão ser excluídos do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física\.

__OS3579__

__RN08__

O campo “Descrição do Rendimento” do quadro 2 – Pessoa Física Beneficiária dos Rendimentos deverá ter sua descrição alterada para “Natureza do Rendimento”\.

__OS3579__

__RN09__

O quadro “3 – Rendimentos Tributáveis, Deduções e Imposto Retido na Fonte” deverá ter sua descrição alterada para “3 – Rendimentos Tributáveis, Deduções e Imposto sobre a Renda Retido na Fonte”\.

__OS3579__

__RN09\.01__

No Quadro 3, alterações de descrições das linhas:

linha 03, alterar a descrição de “Contribuição à Previdência Privada e ao Fundo de Aposentadoria Programada Individual” para “Contribuição a entidades de previdência complementar, pública ou privada, e a Fundo de Aposentadoria Programada Individual \(Fapi\) \(preencher também o Quadro 7\)”\.

linha 04, alterar a descrição de “Pensão Alimentícia \(informar o beneficiário no campo 6\)” para “Pensão alimentícia \(preencher também o Quadro 7\)”\.

linha 05, alterar a descrição de “Imposto de Renda Retido” para “Imposto sobre a Renda Retido na Fonte \(IRRF\)”\.

__MFS\-77523__

__RN10__

Os quadros “Informações Complementares” e “Responsável pelas Informações” deverão ter suas numerações alteradas, devido à entrada do quadro “6 – Rendimentos Recebidos Acumuladamente”\.

__OS3579__

__RN11__

Deverá ser criado o quadro 6 – Rendimentos Recebidos Acumuladamente, logo após o quadro 5 – Rendimentos sujeitos à Tributação exclusiva \(rendimento líquido\)\.

__OS3579__

__RN12__

O quadro “6 – Rendimentos Recebidos Acumuladamente” será um quadro cujas informações de rendimentos não serão parametrizáveis como o restante do Informe de Rendimentos – vide parametrização por Verba do módulo Obrigações de Tributos Federais\. 

__OS3579__

__RN13__

Para que as informações do quadro 6 – Rendimentos Recebidos Acumuladamente sejam gerados e exibidos, o seguinte critério de filtro deverá ser realizado:

1. Ao gerar os Informes de Rendimento através dos seguintes menus de Geração dos Dados:
	1.  Geração dos Dados
		1.  Rendimentos >> Rendimentos Outros >> Geração dos Dados >> Empresa
		2.  Rendimentos >> Rendimentos Outros >> Geração dos Dados >> Estabelecimento
	2. Geração dos Dados por Pessoa Física/Jurídica
		1.  Rendimentos >> Rendimentos Outros >> Geração dos Dados por Pessoa Fís/Jur >> Empresa
		2.  Rendimentos >> Rendimentos Outros >> Geração dos Dados por Pessoa Fís/Jur >> Estabelecimento

Na rotina de geração citada no item 1 e filhos, o sistema irá gerar as informações dos Beneficiários \(Terceiros\) para o Ano Calendário informado\. Ao verificar o Nome informado para geração, deverá ser validado se esse nome está vinculado à um CPF\. Caso seja um CPF a informação deverá ser gerada no Informe de Rendimento, caso o Nome esteja vinculado à um CNPJ, a informação não deverá ser gerada no Informe de Rendimento\.

__OS3579__

__RN14__

As informações dos rendimentos pertencentes ao quadro 6 – Rendimentos Recebidos Acumuladamente não serão recuperadas, pois não é possível realizar um vínculo entre as tabelas SAFX04 \(PF/PJ onde fica o Beneficiário\) e a SAFX181\. Logo esse quadro será gerado no Informe, porém sem informações ou zerado\. Os campos que devem ser informados são os seguintes:

- __6\.1 Número do Processo:__ esse campo deverá ser informado em branco\.
- __Quantidade de Meses:__ esse campo deverá ser informado com o valor “0,0”\. 
- __Natureza do Rendimento:__ esse campo deverá ser informado em branco\.

Após exibir as informações básicas dos rendimentos recebidos acumuladamente, deverão ser informadas as informações pertinentes aos rendimentos recebidos acumuladamente:

- __1 – Total dos rendimentos tributáveis \(inclusive férias e décimo terceiro salário\): __esse campo deverá ser informado com o valor “0,00”\.
- __2 – Exclusão: despesas com ação judicial:__ esse campo deverá ser informado com o valor “0,00”\.
- __3 – Dedução: Contribuição previdenciária oficial:__ esse campo deverá ser informado com o valor “0,00”\.
- __4 – Dedução: Pensão alimentícia \(preencher também o quadro 7\): __esse campo deverá ser informado com o valor “0,00”\.
- __5 – Imposto sobre a renda retido na fonte: __esse campo deverá ser informado com o valor “0,00”\.
- __6 – Rendimentos isentos de pensão, proventos de aposentadoria ou reforma por moléstia grave ou aposentadoria ou reforma por acidente em serviço: __esse campo deverá ser informado com o valor “0,00”\.

__\[ALTERAÇÃO – MFS\-77523\]__

Alteração da descrição da linha 5, de “__Imposto sobre a renda retido na fonte__” para “__Imposto sobre a Renda Retido na fonte \(IRRF\)__”\.

__OS3579__

__MFS\-77523__

__RN15__

O rodapé do quadro 8 – Responsável pelas Informações deverá ser preenchido com o seguinte texto, caso o campo “Ano Base” seja igual a 2011:

“Aprovado pela IN RFB nº 1\.215, de 15 de novembro de 2011\.”

__OS3579__

__RN16__

Caso o Ano Calendário seja a partir de 2011, as informações relacionadas ao Logradouro \(Endereço, Cidade, UF e CEP\) do Quadro 2 – Pessoa Física Beneficiária dos Rendimentos não deverão ser exibidas, visto que o layout da IN 1\.215 que altera o Informe de Rendimentos não solicita essas informações\.

As informações não serão exibidas independente do parâmetro “Imprime Pessoa Fis/Jur” estar selecionado ou não\.

__OS3579__

__RN17__

Caso o Ano Calendário seja anterior a 2011, as informações relacionadas ao Logradouro \(Endereço, Cidade, UF e CEP\) do Quadro 2 – Pessoa Física Beneficiária dos Rendimentos deverão ser exibidas de acordo com o parâmetro “Imprime Endereço Fis/Jur”:

- Caso o parâmetro “Imprime Endereço Fis/Jur” esteja marcado:
	- Os campos Endereço, Cidade, UF e CEP do Quadro 2 – Pessoa Física Beneficiária dos Rendimentos deverão ser exibidos\.
- Caso o parâmetro “Imprime Endereço Fis/Jur” esteja desmarcado:
	- Os campos Endereço, Cidade, UF e CEP do Quadro 2 – Pessoa Física Beneficiária dos Rendimentos não deverão ser exibidos\.

Caso no campo “Ano\-Calendário” seja informado o ano de “2011” em diante, o flag “Imprime Endereço Fis/Jur” ficará oculto\. Para anos anteriores a “2011” o flag continuará disponível\.

__OS3579__

__RN18__

Para os Informes de Rendimentos Outros \(quando utilizado a funcionalidade Enviar e\-mail\), o sistema deve considerar no momento em que o arquivo é salvo a seguinte estrutura: ‘CNPJ da pessoa beneficiária\_Sequencial’\.pdf

Onde: 

O sequencial é baseado na apresentação dos informes na tela, considerando o código da empresa, do estabelecimento e CPF/CNPJ\.

__CH107\_2013__

__RN19__

__\[ALTERADO MFS7081\]__

Após a MFS7081 foi incluída uma parametrização onde será possível o usuário escolher o texto de fundo do informe de rendimentos e também qual a cor de fundo do quadro de Endereço do Remetente e Destinatário\. 

Nesse caso:

Ao emitir o Informe de Rendimentos, será verificado se existe parametrização no caminho: OTF > Parâmetros > Parâmetros p/ Verso do Informe de Rendimentos:

Campo: ‘Texto para impressão no fundo da folha’, caso houver informação o fundo do Informe deverá ser gerado com o texto informado, caso não houver parametrização o fundo do Informe deverá ser o padrão com caracteres especiais para impedir a visualização dos dados do beneficiário e dos rendimentos ao ser dobrado\.

Campo: ‘Cor de fundo do Endereço do Remetente e Destinatário’ no verso nas partes que se destinam a informar o “Remetente” e o “Destinatário” caso a opção escolhida seja Preto deverão possuir fundo preto e fonte branca, caso a opção escolhida seja Branco deverão possuir fundo branco e fonte preto\. Por padrão caso não parametrizado deverão possuir fundo preto e fonte branca também para dificultar a leitura do informe de rendimentos ao ser dobrado e jogado contra a luz\.

Ao emitir o Informe de Rendimentos, o fundo do Informe deverá ficar com caracteres especiais para impedir a visualização dos dados do beneficiário e dos rendimentos ao ser dobrado\.

Além disso, no verso nas partes que se destinam a informar o “Remetente” e o “Destinatário” deverão possuir fundo preto e fonte branca também para dificultar a leitura do informe de rendimentos ao ser dobrado e jogado contra a luz\.

Ver arquivo “Verso Informe de Rendimentos\.png”\.

__OS3996__

__MFS7081__

__RN20__

Ao emitir o Informe de Rendimentos e clicar no botão “Gera PDF”, o sistema irá salvar o arquivo PDF na pasta que o usuário informou no campo “Diretório” e com o nome parametrizado de acordo com o campo “Nomenclatura do Arquivo” da tela de Emissão do Informe de Rendimentos do módulo Obrigações de Tributos Federais\.

Para cada informe de rendimento, existirá um arquivo PDF diferente\.

__OS4000__

__RN21__

Caso na emissão do Informe de Rendimentos exista parametrização para a Empresa/Estabelecimento contendo o logotipo na tela “Logotipo para Emissão do Informe de Rendimentos” – menu: Parâmetros >> Logotipo para Emissão do Informe de Rendimentos – do módulo Obrigações de Tributos Federais, o sistema deverá recuperar a imagem do logotipo no campo “Logotipo” e deverá gerar essa informação na parte superior do informe e no verso também na parte de Remetente, caso o usuário opte por gerar o verso contendo as informações do endereço do remetente e do destinatário\.

__OS3997__

__RN22__

Serão criados na tela de emissão do informe de rendimentos os seguintes campos:

- __Nomenclatura do Arquivo:__ nesse campo, o usuário irá definir de que forma a nomenclatura \(nome\) do arquivo será definido\. Esse campo não é obrigatório de preenchimento\. Serão exibidas para o usuário, as seguintes opções:
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF \+ Ano Calendário
- __Diretório: __nesse campo, o usuário irá informar o diretório para a geração dos arquivos PDF\. Esse campo não é obrigatório de preenchimento\. O campo só será obrigatório caso o campo Nomenclatura do Arquivo seja informado\. Caso o mesmo não seja informado, deverá ser exibida mensagem de erro\.

Ao gerar o informe de rendimento com uma das nomenclaturas selecionadas, o sistema irá montar o informe de rendimento no formato PDF com as informações separadas por underline\.

__OS4000__

__RN23__

Bloco 5 – \(Rendimento Sujeitos à Tributação Exclusiva\) 

Obs: Para gerar o informe de rendimento se faz necessário a geração dos dados no caminho Módulo: Federal 🡪 Obrigações de Tributos Federais 🡪 Rendimentos 🡪 Rendimentos Outros 🡪 Geração dos Dados ou por FIS/JUR\.

Deverá ser incluído a linha “2 – Imposto sobre a renda retido na fonte sobre 13° Salário”, as informações para popular este, serão recuperadas da SAFX53 seguindo a seguinte regra:

SAFX53 – Para que as informações sejam recuperadas da SAFX53 o campo “Valor Tributo 13° Salário” localizado no Módulo: Básicos 🡪 MasterSAF DW 🡪 Manutenção 🡪 Controle de Tributos deverá estar preenchido\.

__\[ALTERAÇÃO – MFS\-77523\]__

Alteração da descrição da linha 2, de “Impostos spbre a renda retido na fonte sobre 13º salário” para ““Impostos spbre a Renda Retido na fonte sobre 13º \(décimo terceiro\) salário”\.

__OS4700__

__MFS\-77523__

__RN24__

Bloco 5 – \(Rendimento Sujeitos à Tributação Exclusiva\)\. 

Obs: Para gerar o informe de rendimento se faz necessário a geração dos dados no caminho Módulo: Federal 🡪 Obrigações de Tributos Federais 🡪 Rendimentos 🡪 Rendimentos Outros 🡪 Geração dos Dados ou por FIS/JUR\.

Linha 01 – Décimo 13° salário, as informações para popular este serão recuperadas da SAFX53/530 seguindo a seguinte regra:

SAFX53 – Para que as informações sejam recuperadas da SAFX53 o campo “Valor 13° Salário” localizado no Módulo: Básicos 🡪 MasterSAF DW 🡪 Manutenção 🡪 Controle de Tributos deverá estar preenchido\.

__\[ALTERAÇÃO – MFS\-77523\]__

Alteração da descrição da linha 1, de “Décimo Terceiro Salário” para “13º \(décimo terceiro\) salário”\.

__OS4700__

__MFS\-77523__

__RN25__

O rodapé do quadro 8 – Responsável pelas Informações deverá ser preenchido com o seguinte texto, caso o campo “Ano Base” seja igual a 2014:

“Aprovado pela IN RFB nº 1\.522, de 05 de dezembro de 2014”

\[MFS8975\]

Caso ano base for igual a 2016:

“Aprovado pela Instrução Normativa RFB n° 1682, de dezembro de 2016”

__\[ALTERAÇÃO MFS\-77523\] – Adequação da descrição__

Caso ano base for igual a 2021:

“Aprovado pela Instrução Normativa RFB n° 2060, de 13 de dezembro de 2021\.”

__OS4700__

__MFS8975__

__MFS\-77523__

__RN29__

\[MFS9876\]

Inclusão do ano do exercício no cabeçalho do informe de rendimento\.

O exercício deverá ser o ano calendário mais “1”, ou seja, caso o ano calendário = 2016 o exercício será igual a 2017\.

Como será demonstrado no informe: “Exercício de XXXX”

__MFS9876__

__RN30__

Com a alteração feita para gerar os beneficiários do exterior, consequentemente no item 2 – Pessoa Física Beneficiária dos Rendimentos, o campo CNPJ será preenchido com o campo “06\-CPF\-CGC” ou com o campo “53\-Número de Identificação Fiscal”, o relatório deverá ser alterado para contemplar 30 posições\.

__MFS\-9872__

__RN31__

Não disponibilizar no produto TAXONE, o item de menu Emissão de Declaração de Rendimentos' e suas respectivas funcionalidades \(módulo Federal / OTF/Rendimentos / Outros\)\.

 

__MFS\-74070__

__RN32__

__Quadro 4__

Alterar a ordenação e descrição das linhas do quadro 4, criar duas linhas e suas respectivas regras de recuperação, conforme indicado abaixo, as demais regras de recuperação das linhas já existentes, devem se manter:

Ajuste na descrição da “Linha 01\- Parcela Isenta dos Proventos de Aposentadoria, Reserva, Reforma e pensão \(65 anos ou mais\)” para: “Linha 1 \- Parcela isenta dos proventos de aposentadoria, reserva remunerada, reforma e pensão \(65 anos ou mais\), exceto a parcela isenta do 13º \(décimo terceiro\) salário\.”

Mantém a regra: Considerar a informação do Campo 33 \- VLR\_APOSENT\_ISENTA da SAFX53 

CRIAR LINHA: Linha 2 \- Parcela isenta do 13º \(décimo terceiro\) salário de aposentadoria, reserva remunerada, reforma e pensão \(65 anos ou mais\)\.

Regra: Considerar a informação do Campo 99 \- VLR\_APOSENT\_ISENTA\_13 da SAFX53 

Alterar a ordem da “Linha 02\- Diárias e Ajudas de Custo” para “Linha 3 \- Diárias e ajudas de custo\.”

Alterar a ordem e a descrição da “Linha 03 \- Pensão, Proventos de Aposentadoria ou Reforma por Moléstia Grave e  Aposentadoria ou Reforma por Acidente em Serviço” para “Linha 4 \- Pensão e proventos de aposentadoria ou reforma por moléstia grave; proventos de aposentadoria ou reforma por acidente em serviço\.”

 Alterar a descrição e a ordem da “Linha 4 \- Lucro e Dividendo, Apurado a partir de 1996, pagos por PJ \(Lucro Real, Presumido ou Arbitrado\)\.” para “Linha 5 \- Lucros e dividendos, apurados a partir de 1996, pagos por pessoa jurídica \(lucro real, presumido ou arbitrado\)\.”

Alterar a ordem da “Linha 5 \- Valores Pagos ao Titular ou Sócio da Microempresa ou Empresa de Pequeno Porte, exceto Pró\-labore, Aluguéis ou Serviços Prestados” para “Linha 6 \- Valores pagos ao titular ou sócio da microempresa ou empresa de pequeno porte, exceto pró\-labore, aluguéis ou serviços prestados\.”

Alterar a ordem da “Linha 6 \- Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV e por acidente de trabalho\.” Para “Linha 7 \- Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV e por acidente de trabalho\.”

Mantém a regra: Gerar fixo 0,00

CRIAR LINHA: Linha 8 \- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função\.

Regra gerar fixo 0,00

Alterar a ordem e a descrição da “Linha 7 – Outros” para “Linha 9 \- Outros \(especificar\)”\.

__MFS\-77523__

__RN33__

Não disponibilizar no produto DW, o item de menu Emissão de Declaração de Rendimentos' e suas respectivas funcionalidades \(módulo Federal / OTF/Rendimentos / Outros\)\.

 

__MFS\-79687__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

