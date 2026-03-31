# Tela_Geracao_ECF

- **Fonte:** Tela_Geracao_ECF.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 85 KB

---

 

THOMSON REUTERS

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Tela de Geração da ECF 

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

09/03/2018

MFS\-12684

Criação da documentação 

Alessandra Cristina Navatta

<a id="OLE_LINK28"></a><a id="OLE_LINK29"></a><a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a>

Sumário

[1\.	INTRODUÇÂO	3](#_Toc519170184)

[2\.	DOCUMENTOS DE REFERÊNCIAS	3](#_Toc519170185)

[2\.1\.	Regras dos Campos	4](#_Toc519170186)

# <a id="_Toc519170184"></a>INTRODUÇÂO

Objetivo desta especificação é permitir a geração dos arquivos texto da ECF

# <a id="_Toc519170185"></a>DOCUMENTOS DE REFERÊNCIAS

- __Regras de Negócio Gerais: __

 Regras\_Gerais\_DWECF\.docx

- __Mensagens do Sistema__

 Mensagens\_Sistema\_DWECF\.xlsx

- __Geração do bloco 0__

MTZ\_ECF\_Bloco0\.doc

- __Geração do bloco C__

MTZ\_ECF\_BlocoC\.doc

- __Geração do bloco E__

MTZ\_ECF\_BlocoE\.doc

- __Geração do bloco J__

MTZ\_ECF\_BlocoJ\.doc

- __Geração do bloco L__

MTZ\_ECF\_BlocoL\.doc

- __Geração do bloco M__
- MTZ\_ECF\_BlocoM\.doc
- __Geração do bloco N__

MTZ\_ECF\_BlocoN\.doc

- __Geração do bloco P__
- MTZ\_ECF\_BlocoP\.doc__ __
- __Geração do bloco Q__
- MTZ\_ECF\_BlocoQ\.doc__ __
- __Geração do bloco T__
- MTZ\_ECF\_BlocoT\.doc__ __
- __Geração do bloco U__
- MTZ\_ECF\_BlocoU\.doc__ __
- __Geração do bloco X__

MTZ\_ECF\_BlocoX\.doc

- __Geração do bloco Y__

MTZ\_ECF\_BlocoY\.doc

- __Geração do bloco W__

MTZ\_ECF\_BlocoW\.doc

### <a id="_Toc350763252"></a><a id="_Toc360443175"></a><a id="_Toc519170186"></a>Regras dos Campos 

__Localização da tela:__ ECF \- Escrituração Contábil Fiscal >> Gerações >> ECF

__Título da tela: __Geração da ECF

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS__

Executar

Botão

\-

\-

Default desabilitado\-

Botão que permite submeter as escriturações para processamento do arquivo magnético\.

__Tratamentos:__

__Validações que impedem a geração do arquivo:__

\-Se no componente Informações ECF dos Estabelecimentos não tiver registros selecionados, exibir a mensagem

DW00057\.

* *

\-Permitir exercício a partir de 2014\. Caso o usuário informe um exercício anterior a 2014, exibir a mensagem DW00027\.

\- Aplicar RNG000010 – Campo Obrigatório

\- A data Inicial deve ser a partir de 01/01/2014\. Caso o usuário informe uma data inicial anterior a 01/01/2014, exibir a mensagem DW00028

\- Aplicar RNG00053 \-Data Inicial x Exercício

\- Aplicar RNG00052 \- Validação do campo data inicial/data final\. 

\- Se o campo Data Final for menor que o campo Data Inicial, exibir a mensagem DW00212

Para cada escrituração selecionada, verificar:

\-Se na tela de “Informações ECF”, o campo “Perfil de Geração do Arquivo” está preenchido\. Se não existir informação no campo, não gerar o arquivo desta escrituração e exibir a mensagem DW00189\. 

Caso, o perfil esteja indicado na Informação ECF e a validação acima for satisfatória, para cada escrituração, recuperar os dados de acordo com o período indicado nos campos Data Inicial e Data final\. 

\-Para todas as Informações ECF selecionada, verificar na Informação ECF imediatamente anterior, \(considerando a data inicial da tela Informações ECF imediatamente anterior da Informação ECF selecionada, para o mesmo estabelecimento\), se possui na última abertura da apuração, o campo situação especial igual a ‘Desenquadramento de Imune/Isenta’, se sim, verificar se o campo ‘__Indicador de Início de Período__’ está igual a ‘4 – Início de obrigatoriedade da entrega no curso do ano calendário’ \(informação cadastrada na tela de Geração da ECF\), caso o indicador esteja diferente, exibir a mensagem DW00188 \(impedindo a geração do arquivo para a o estabelecimento em questão\), se não, o arquivo é processado sem problemas\. 

__Validações que não impedem a geração do arquivo: __

\-Se não forem encontrados nenhum registro de abertura de apuração, para a escrituração selecionada, exibir a mensagem DW00190 e gerar apenas os registros cadastrais \(Bloco 0\) e os Blocos que não precisam passar pelo processamento\.

\-Se o campo __Indicador de Início de Período__ for “0 – Regular \(início no primeiro dia do ano\)” e for selecionada escriturações que possuam data inicial da primeira abertura recuperada diferente de 01/01/AAAA, exibir a mensagem DW00269\. 

\- Se o conteúdo do campo __Indicador de Início de Período__ selecionado for “1 – Abertura \(início de atividades no ano calendário\)”, e for selecionadas escriturações com data inicial da apuração recuperada igual a  01/01/AAAA, exibir a mensagem DW00269\. 

__Regras de Geração do Arquivo:__

Realizar a geração do arquivo ECF, seguindo as regras de agrupamento contidas nas respectivas especificações considerando para seleção das informações somente os registros correspondentes às aberturas de apuração selecionadas:

MTZ\_ECF\_Bloco0\.doc

MTZ\_ECF\_BlocoC\.doc

MTZ\_ECF\_BlocoE\.doc

	MTZ\_ECF\_BlocoJ\.doc

MTZ\_ECF\_BlocoK\.doc

MTZ\_ECF\_BlocoL\.doc

MTZ\_ECF\_BlocoM\.doc

MTZ\_ECF\_BlocoN\.doc

MTZ\_ECF\_BlocoP\.doc

MTZ\_ECF\_BlocoQ\.doc

MTZ\_ECF\_BlocoT\.doc

MTZ\_ECF\_BlocoW\.doc

MTZ\_ECF\_BlocoX\.doc

MTZ\_ECF\_BlocoY\.doc

MTZ\_ECF\_Bloco9\.doc

__Nomenclatura dos Registros:__

Gerar um arquivo para cada escrituração processada\. O nome do arquivo deverá ser composto conforme a formatação “ECF” \+ “\-“ \+ “CNPJ” \+ “DDMMAAAA \(do campo Data Inicial do grid de seleção de empresas e escriturações\) ”\. Exemplo: ECF\-12345678901234\-01112014\.txt

MFS\-12684

Exercício

Texto

S

S

AAAA

Permite que o usuário informe o exercício para processamento\.

MFS\-12684

Data Inicial

Data

S

S

Permite que o usuário informe a data inicial para seleção dos registros de abertura da apuração\.

MFS\-12684

Data Final

Data

S

S

Permite que o usuário informe a data final para seleção dos registros de abertura da apuração\.

MFS\-12684

Indicador de Início de Período

Lista

S

S

Código \- Descrição

Permite que o usuário informe o indicador de início de período que será utilizado no campo correspondente do layout da ECF

__Conteúdos Válidos:__

0 – Regular \(início no primeiro dia do ano\)

1 – Abertura \(início de atividades no ano calendário\)

2 – Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação

3 – Resultante de Transformação

4 – Início de obrigatoriedade da entrega no curso do ano calendário

MFS\-12684

Plano de Contas e Centro de Custos

Radio Button

S

N

Movimentado no Período

Permite que o usuário selecione a opção que as contas e centros de custos serão recuperadas na geração da ECF\.

__Opções Válidas:__

Movimentado no Período

Completo

__Tratamento:__

Quando selecionado “Completo”, o sistema deve recuperar e exibir no arquivo todos os cadastros de contas e de centros de custo que estiverem cadastrados na tabela\.

Quando selecionado “Movimentado no Período”, o sistema deve recuperar e exibir no arquivo somente os cadastros de contas e de centros de custo que estiverem dentro do período informado na data inicial e data final e que possuem saldos\.

MFS\-12684

Retificadora

Lista

S

S

N – ECF original

Permite que o usuário informe se o arquivo gerado é normal ou retificação\.

__Tratamentos:__

__Conteúdos Válidos:__

S – ECF retificadora

N – ECF original

F–ECF original com mudança de forma de tributação \(Art\. 5o da Instrução Normativa no 166/1999\)

MFS\-12684

Número do Recibo Anterior 

Texto

S

N

Default: Desabilitado

Permite que o usuário informe o número do recibo do arquivo da ECF que será retificado

__Tratamentos:__

Habilitar este campo para edição somente se o campo “RETIFICADORA” for igual a “S – ECF retificadora” ou “F – ECF original com mudança de forma de tributação \(Art\. 5o da Instrução Normativa no 166/1999\) ”\. 

MFS\-12684

__Informações ECF dos Estabelecimentos__

Selecionar

Botão

Permite que o usuário selecione os registros de Informações ECF para processamento

__Tratamentos:__

Exibir todos as escriturações de acordo com os filtros que foram preenchidos na tela\. 

Apresentar os conteúdos, conforme descrito abaixo:  
  
Campos de Pesquisa do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos:  
Descrição'  
Botões do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos': Critério, Cancelar, OK e Salvar  
  
\- Permite a seleção de vários registros por vez\.  
\- Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem DW00053\.  
\- Ao selecionar o botão 'Cancelar', nada será feito e o modal será fechado\.   
\- Ao selecionar o botão 'Critério', as escriturações que foram recuperadas poderão ser filtradas\. 

\-Ao confirmar a seleção dos registros, apresentá\-los no componente “ Informações ECF dos Estabelecimentos” da tela Principal  
\-Ao selecionar o botão salvar, o sistema salva as informações recuperadas das apurações em formato txt \(no diretório local que o usuário informar\)\.

MFS\-12684

Marcar Todos

Check\-box

Desmarcado

Permite ao usuário selecionar ou desmarcar todos os registros da grid Período de Apuração dos Estabelecimentos\.

MFS\-12684

Escriturações \(\*\)

Texto

S

N

Código Estab \- CGC \- Exercício \-  Data Inicial da Escrituração   
\(076 \- XXXXXXXXXXXXXX \-  01/03/2017\)

Permite que o usuário visualize e selecione as escriturações que serão processadas\.

MFS\-12684

\(\*\) Não exibir a descrição na tela\.

