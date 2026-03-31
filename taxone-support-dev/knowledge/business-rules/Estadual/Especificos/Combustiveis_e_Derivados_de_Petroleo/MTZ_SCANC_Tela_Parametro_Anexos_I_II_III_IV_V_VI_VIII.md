# MTZ_SCANC_Tela_Parametro_Anexos_I_II_III_IV_V_VI_VIII

- **Fonte:** MTZ_SCANC_Tela_Parametro_Anexos_I_II_III_IV_V_VI_VIII.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Anexos I, II, III, IV, V, VI e VIII – Por CFOP ou Por Extensão de CFOP

Módulo Combustível e Derivados de Petróleo \(SCANC\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-11111

Julyana Perrucini

Este documento tem como objetivo alterar a tela de parametrização dos Anexos I, II, III, IV, V, VI e VIII – Por CFOP ou Por Extensão de CFOP, para inclusão da opção 687\-Remessa em Bonificação, Doação e Brinde e da opção 688\-Empréstimos\.

Sumário

[1\.	Regras dos Campos	3](#_Toc494454507)

# <a id="_Toc350763252"></a><a id="_Toc494454507"></a>Regras dos Campos 

__Localização da tela:__ Específicos\\ Combustível e Derivados de Petróleo\\ Parâmetros\\ Anexos I, II, III, IV, V, VI e VIII – Por CFOP e Por Extensão de CFOP

__Título da tela: __Anexos I, II, III, IV, V, VI e VIII – Por CFOP

      Anexos I, II, III, IV, V, VI e VIII – Por Extensão de CFOP

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Texto

S

N

Formato: 

Combo Box

Default: 

Desbloqueado

Permitir mostrar estabelecimento a ser parametrizado para geração dos registros\.

__Tratamento:__

- O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, este será apresentado;
- O campo será apresentado de forma desbloqueada e caso o usuário não entre com um estabelecimento no Login, deverá apresentar a lista dos estabelecimentos licenciados;
- Se o campo não for preenchido, emitir a mensagem na tela: “Estabelecimento deve ser preenchido”\.

MFS\-11111

Tipo

Texto

S

N

Formato: 

Combo Box

Default: 

Habilitado

Neste campo o usuário deverá selecionar o tipo de operação que será relacionado a uma CFOP\. É indicado que se parametrize apenas as operações relacionadas a entradas, saídas, devolução, bonificação, empréstimos e ressarcimento autorizado conforme tabela apresentada a seguir:

__\[ALTERADA – MFS\-11111\]__

__Tipo de Operação x Anexos e Quadros__

__088 \- Saídas de combustível e derivados__

Anexo II Quadro 2

Anexo I Quadro 4 

Anexo VIII Quadro 2 e 6

__089 \- Entrada de combustível e derivados__

Anexo I Quadro 3

Anexo IV Quadro 2 

Anexo VIII Quadro 2 e 6

__090 \- Devolução de venda de combustível e derivados__

Anexo I Quadro 4

Anexo II Quadro 2 

Anexo VIII Quadro 2 e 6

__091 \- Devolução de compra de combustível e derivados__

Anexo I Quadro 3

Anexo IV Quadro 2

Anexo VIII Quadro 4 e 5

__092 \- Saída para consumidor final__

Anexo I Quadro 4

Anexo VIII Quadro 2 e 6

__093 \- Devolução de venda para consumidor final __

Anexo II Quadro 2

__108 \- Ressarcimento Autorizados de ICMS\-ST__

Anexo VI Quadro 10, 11, 12 e 13

__687 \- Remessa em Bonificação, Doação ou Brinde__

Anexo I Quadro 3

__688 \- Empréstimos__

Anexo I Quadro 3

__Tratamento:__

- Se o campo não for preenchido, emitir a mensagem na tela: “Tipo deve ser preenchido”\.

MFS\-11111

CFOP’s

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado

Lista todos os CFOP's cadastrados, para que o usuário selecione quais os CFOP's deseja fazer parametrização\. 

*Observação: *Para correta seleção deste código, o usuário deverá ter importado a tabela SAFX2012, através do Módulo Job Servidor ou cadastrar manualmente\.

Dentro dessa seleção de CFOP terá um campo Destinação nele o usuário poderá informar em alguns casos o destino de um determinado CFOP, podendo ser:

1 \- Remessa p/ comercialização;

2 \- Remessa p/ transferência; ou

3 \- Remessa p/ consumo\.

MFS\-11111

Replicar para Estabelecimentos

Texto

N

S

Formato:

Check Box

Default:

Habilitado

Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos\.

Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”\.

Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação\. 

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

MFS\-11111

