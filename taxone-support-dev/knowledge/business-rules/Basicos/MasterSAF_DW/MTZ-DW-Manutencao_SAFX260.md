# MTZ-DW-Manutencao_SAFX260

- **Fonte:** MTZ-DW-Manutencao_SAFX260.docx
- **Modificado:** 2025-12-01
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Itens Fatura de Serviços de Comunicação e de Telecomunicações

Manutenção SAFX260

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-15570

Julyana Perrucini

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de manutenção para a SAFX260\.

MFS\-22679

Julyana Perrucini

Essa MFS tem como objetivo alterar o campo Modelo da Nota Fiscal para aceitar o modelo “55”\.

MFS21354

Lara Aline

Inclusão de 8 novos campos reservados

MFS23990

Andréa Rocha

Inclusão do modelo 65

MFS38312

Andréa Rocha

Retirar o campo PFJ do usuário da chave primária da tabela e incluir o campo para a manutenção

MFS992323

Andréa Rocha

Incluir o código de modelo 62 para a recuperação das notas fiscais\.

Sumário

[1\.	Regras dos Campos	3](#_Toc42697449)

# <a id="_Toc350763252"></a><a id="_Toc42697449"></a>Regras dos Campos 

__Localização da tela:__ Básicos\\ MasterSAF DW\\ <a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Manutenção\\ Telecom\\ Fatura Comunicação/Telecomunicações \(Aba __Item__\)

__Título da tela: __Fatura de Serviços de Comunicação/Telecomunicações

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__ABRE – __Permite abrir seleção de registros inseridos\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__IMPRIME – __Permite imprimir os dados do registro\.

__PÁG \- – __Permite avançar para página inicial\.

__PÁG \-\- – __Permite avançar página a página sentido a página inicial\.

__PÁG \+ –__ Permite avançar para página final\.

__PÁG \+\+ –__ Permite avançar página a página sentido a página final\.

__RELATÓRIO – __Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login \(mostrar apenas os campos obrigatórios como critério de busca\)\.

__FECHA – __Permite sair da tela\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Item

Numérico

S

N

Formato: 

Text Input

Default:

Habilitado

Nesse campo o usuário deverá informar o número de ordem do item da fatura comercial\.

__Tratamento:__

- Ao salvar o registro esse campo não poderá ser alterado;
- Se o campo não for preenchido, emitir a mensagem de tela: *“Item da Nota Fiscal deve ser preenchido”*\.

MFS\-15570

Origem do Item

Texto

S

S

Formato:

Combo Box

Default:

Habilitado

Nesse campo o usuário deverá informar “1” para receita/desconto próprio e “2” para receita/desconto de terceiros\.

__Tratamento:__

- Se o campo não for preenchido, emitir a mensagem na tela: *“Origem do item deve ser preenchida”*\.

MFS\-15570

Produto

Texto

N

S

Formato:

Text Input/ Pasta de Seleção SAFX2013

Default:

Habilitado

Nesse campo o usuário deverá informar o código do item da fatura comercial atribuído pela empresa\.

__Tratamento:__

- Demonstrar indicador, código e descrição do produto;
- Se a informação for digitada manualmente e o produto não estiver cadastrado na SAFX2013 demonstrar a mensagem padrão no campo: “*Produto Não Encontrado”*\.

MFS\-15570

Fís/Jur Usuário

Texto

S

S

Formato:

Text Input/ Pasta de Seleção SAFX04

Default:

Habilitado

Nesse campo o usuário deverá informar qual a Pessoa Física ou Jurídica cadastrada na SAFX04 do usuário relativo à fatura comercial\.

__Tratamento:__

- Demonstrar indicador, código e razão social;
- Se a informação for digitada manualmente e o usuário não estiver cadastrado na SAFX04 demonstrar a mensagem padrão no campo: “*Pessoa/Física Jurídica Não Encontrada*”\.
- Se o campo não for preenchido, emitir a mensagem na tela: *“Fís/Jur do usuário deve ser preenchido”\.*

MFS\-38312

Fís/Jur Terceiro

Texto

N

S

Formato:

Text Input/ Pasta de Seleção SAFX04

Default:

Habilitado

Nesse campo o usuário deverá informar qual a Pessoa Física ou Jurídica cadastrada na SAFX04 do terceiro relativo à fatura comercial\.

__Tratamento:__

- Demonstrar indicador, código e razão social;
- Se a informação for digitada manualmente e o usuário não estiver cadastrado na SAFX04 demonstrar a mensagem padrão no campo: “*Pessoa/Física Jurídica Não Encontrada*”\.

MFS\-15570

Valor do Item

Numérico

S

S

Formato:

Text Input 0,00

Default:

Habilitado

Nesse campo o usuário deverá informar o valor do item da fatura\. __*Atenção:*__ Item de desconto deverá ter sinal negativo na primeira posição do campo\.

MFS\-15570

Dados da Nota Fiscal \(Group\)

Modelo

Texto

N

S

Formato:

Text Input/ Pasta de Seleção SAFX2024

Default:

Habilitado

__\[ALTERADA – MFS\-22679\]__

__\[MFS992323\] __Inclusão do modelo 62

Nesse campo o usuário deverá informar o modelo do documento fiscal relativo à fatura comercial\. Serão aceitos apenas os modelos 21, 22, 55, 62 e 65, e se não houver informação o mesmo deverá ser deixado em branco\.

__Tratamento:__

- Demonstrar código e descrição do modelo;
- Se a informação for digitada manualmente e o modelo não estiver cadastrado na SAFX2024 demonstrar a mensagem padrão no campo: “*Modelo Não Encontrado*”;
- Caso o conteúdo não corresponda a nulo, a 21 ou a 22 ou a 55 ou 62 ou a 65, deve ser exibida a mensagem na tela: *“O Campo Modelo do Documento deve ser: <nulo, 21, 22, 55, 62 ou 65>*\.

MFS\-15570

MFS\-22679

MFS\-23990

MFS992323

Nº NF/ Série

Texto

N

S

Formato:

Text Input

Default:

Habilitado

Nesse campo o usuário deverá informar o número e a série do documento fiscal relativo à fatura comercial\.

MFS\-15570

Data Emissão

Data

N

S

Formato:

Text Input DD/MM/AAAA

Default:

Habilitado

Nesse campo o usuário deverá informar a data de emissão do documento fiscal relativo à fatura comercial\.

MFS\-15570

Vlr\. Total NF

Numérico

N

S

Formato:

Text Input 0,00

Default:

Habilitado

Nesse campo o usuário deverá informar o valor total do documento fiscal relativo à fatura comercial

MFS\-15570

Reservado 1

Numérico

N

S

Formato:

Text Input 0,00

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 2

Numérico

N

S

Formato:

Text Input 0,00

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 3

Numérico

N

S

Formato:

Text Input 0,00

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 4

Texto

N

N

Formato:

Text Input

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 5

Texto

N

N

Formato:

Text Input

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 6

Texto

N

N

Formato:

Text Input

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 7

Texto

N

N

Formato:

Text Input

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

Reservado 8

Texto

N

N

Formato:

Text Input

Default:

Habilitado

Campo tipo reservado \(FLEXFIELD\), para uso exclusivo dos clientes em processos customizados\. Não serão utilizados em nenhum processo dentro dos produtos Mastersaf\.

MFS21354

#  

