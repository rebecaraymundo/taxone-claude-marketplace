# MTZ-OTF-Emitir_Informe_de_Rendimentos_Outros_por_CNPJ

- **Fonte:** MTZ-OTF-Emitir_Informe_de_Rendimentos_Outros_por_CNPJ.docx
- **Modificado:** 2022-02-08
- **Tamanho:** 48 KB

---

# Módulo: Obrigações de Tributos Federais

# Emissão de Informe de Rendimento Outros por CNPJ 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3226

Obrigações de Tributos Federais \- Emitir Informes de Rendimento Outros com Filtro por Empresa

O cliente Sul América necessita que no momento da emissão dos Informes de Rendimentos Outros, seja possível que o Beneficiário seja selecionado com um filtro para TODAS AS EMPRESAS de um determinado grupo\. Isso é necessário, visto que o cliente possui um Beneficiário em mais de uma Empresa e esse tipo de filtro facilita a geração das informações\.

CH31887

Imprimir o tipo de logradouro no Informe de Rendimentos outros por CNPJ

Imprimir o tipo de logradouro no campo 01 – Fonte Pagadora do Informe de Rendimentos outros por CNPJ\.

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

CH1766\_2015

Alteração no preenchimento do item 2 – Pessoa Jurídica Beneficiária dos Rendimentos

Este documento tem como objetivo alterar a geração dos relatórios de Informe de Rendimentos Outros por CNPJ, e Por Nome, localizados no módulo Federal >> Obrigações de Tributos Federais, para considerar sempre o cadastro da pessoa jurídica beneficiária dos rendimentos \(SAFX04\) de maior validade\.

MFS7081

Inclusão de parametrização para verso do informe de rendimentos

Inclusão de nova parametrização para o verso do Informe de Rendimentos\.

MFS\-9872

Incluir beneficiários do exterior

Este documento tem como objetivo corrigir a geração dos Informes de Rendimento Outros para considerar beneficiários do exterior\.

MFS\-74070

Esta funcionalidade não estará disponível no Taxone

Não disponibilizar no produto TAXONE, o item de menu Emissão de Declaração de Rendimentos’ e suas respectivas funcionalidades, no módulo Federal / OTF/Rendimentos / Outros 

Este item já estava implementado, apenas refere\-se a atualização de documentação funcional\.

MFS\-79687

Esta funcionalidade não estará disponível no DW

Não disponibilizar no produto DW, o item de menu Emissão de Declaração de Rendimentos’ e suas respectivas funcionalidades, no módulo Federal / OTF/Rendimentos / Outros 

Este item já estava implementado, apenas refere\-se a atualização de documentação funcional\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Caso o usuário selecione nos campos “Empresa” e “Estabelecimento” a opção “Todos” o sistema deverá permitir que o usuário selecione o Beneficiário Inicial e Final para a emissão do Informe de Rendimentos\.

Caso o usuário faça isso, o sistema deverá gerar o\(s\) Informe\(s\) de Rendimento\(s\) desse\(s\) Beneficiário\(s\) para todas as Empresas e Estabelecimentos em que o mesmo possuir informação\. 

__OS3226__

__RN02__

Caso o usuário selecione no campo “Empresa” uma Empresa específica e selecione no campo “Estabelecimento” um Estabelecimento específico, o sistema deverá permitir que o usuário selecione o Beneficiário Inicial e Final para a emissão do Informe de Rendimentos\.

Caso o usuário faça isso, o sistema deverá gerar o\(s\) Informe\(s\) de Rendimento\(s\) desse\(s\) Beneficiário\(s\) para a Empresa e Estabelecimento informados\.

__OS3226__

__RN03__

Caso o usuário selecione no campo “Empresa” uma Empresa específica e selecione no campo “Estabelecimento” a opção “Todos”, o sistema deverá permitir que o usuário selecione o Beneficiário Inicial e Final para a emissão do Informe de Rendimentos\.

Caso o usuário faça isso, o sistema deverá gerar o\(s\) Informe\(s\) de Rendimento\(s\) desse\(s\) Beneficiário\(s\) para a Empresa informada e para todos os Estabelecimentos  em que o mesmo possuir informação\.

__OS3226__

__RN04__

Os parâmetros de “Emissão por Pessoa” – Jurídica, Física e Ambas – da tela de Emissão do Informe de Rendimentos Outros por CNPJ deverá ser inibida, visto que nesse tipo de Informe, Pessoas Físicas não devem ser informes já que existe o Informe de Rendimentos Outros por CPF e por Nome\.

__OS3579__

__RN05__

No campo 01\(Fonte Pagadora\) do Informe de Rendimentos deve ser impresso o Tipo de Logradouro \(ex: Avenida, Rua\.\.\)

__CH31887__

__RN06__

O tipo de logradouro será recuperado da tabela ESTABELECIMENTO, o campo a ser recuperado será o:

\[ESTABELECIMENTO, TP\_LOGRADOURO\]

__CH31887__

__RN07__

Para os Informes de Rendimentos Outros \(quando utilizado a funcionalidade Enviar e\-mail\), o sistema deve considerar no momento em que o arquivo é salvo a seguinte estrutura: ‘CNPJ da pessoa beneficiária\_Sequencial’\.pdf

Onde: 

O sequencial é baseado na apresentação dos informes na tela, considerando o código da empresa, do estabelecimento e CPF/CNPJ\.

__CH107\_2013__

__RN08__

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

__RN09__

Ao emitir o Informe de Rendimentos e clicar no botão “Gera PDF”, o sistema irá salvar o arquivo PDF na pasta que o usuário informou no campo “Diretório” e com o nome parametrizado de acordo com o campo “Nomenclatura do Arquivo” da tela de Emissão do Informe de Rendimentos do módulo Obrigações de Tributos Federais\.

Para cada informe de rendimento, existirá um arquivo PDF diferente\.

__OS4000__

__RN10__

Caso na emissão do Informe de Rendimentos exista parametrização para a Empresa/Estabelecimento contendo o logotipo na tela “Logotipo para Emissão do Informe de Rendimentos” – menu: Parâmetros >> Logotipo para Emissão do Informe de Rendimentos – do módulo Obrigações de Tributos Federais, o sistema deverá recuperar a imagem do logotipo no campo “Logotipo” e deverá gerar essa informação na parte superior do informe e no verso também na parte de Remetente, caso o usuário opte por gerar o verso contendo as informações do endereço do remetente e do destinatário\.

__OS3997__

__RN11__

Serão criados na tela de emissão do informe de rendimentos os seguintes campos:

- __Nomenclatura do Arquivo:__ nesse campo, o usuário irá definir de que forma a nomenclatura \(nome\) do arquivo será definido\. Esse campo não é obrigatório de preenchimento\. Serão exibidas para o usuário, as seguintes opções:
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF
	- CNPJ da Pessoa Física/Jurídica \+ CNPJ do Estabelecimento \+ Código DARF \+ Ano Calendário
- __Diretório: __nesse campo, o usuário irá informar o diretório para a geração dos arquivos PDF\. Esse campo não é obrigatório de preenchimento\. O campo só será obrigatório caso o campo Nomenclatura do Arquivo seja informado\. Caso o mesmo não seja informado, deverá ser exibida mensagem de erro\.

Ao gerar o informe de rendimento com uma das nomenclaturas selecionadas, o sistema irá montar o informe de rendimento no formato PDF com as informações separadas por underline\.

__OS4000__

__RN12__

Para preenchimento do item 2 – Pessoa Jurídica Beneficiária dos Rendimentos deve ser considerado os dados do cadastro da pessoa jurídica \(SAFX04\) de maior validade\.

__CH1766\_2015__

__RN13__

Com a alteração feita para gerar os beneficiários do exterior, consequentemente no item 2 – Pessoa Jurídica Beneficiária dos Rendimentos, o campo CNPJ será preenchido com o campo “06\-CPF\-CGC” ou com o campo “53\-Número de Identificação Fiscal”, o relatório deverá ser alterado para contemplar 30 posições\.

__MFS\-9872__

__RN14__

Não disponibilizar no produto TAXONE, o item de menu Emissão de Declaração de Rendimentos' e suas respectivas funcionalidades \(módulo Federal / OTF/Rendimentos / Outros\)\.

__MFS\-74070__

__RN15__

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

