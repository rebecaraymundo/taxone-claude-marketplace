# MTZ_eSocial_Tela_Geracao_Evento_S1250

- **Fonte:** MTZ_eSocial_Tela_Geracao_Evento_S1250.docx
- **Modificado:** 2022-06-07
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Tela de Geração do Evento S\-1250

Informações para o eSocial

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS20750

Lara Aline

Definição das regras da tela de Geração do Evento S\-1250

\-

MFS24243

Eduardo Cruz

Estabelecimento Centralizador gerando todos os centralizados quando for acionado

\-

__MFS\-87543__

__Elisabete Costa__

__Exclusão do Evento S\-1250 \- Para versão S\-1\.0__

__06/06/2022__

Sumário

[1\.	Regras dos Campos	3](#_Toc525042709)

__A partir da versão S\-1\.0 não deve ser gerado o evento S\-1250__

__\[MFS\-87543\]__

# <a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc525042709"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: SPED >> Informações para o eSocial

Menu: Geração >> Geração do Evento S\-1250

__Título da tela: __Geração do Evento S\-1250

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Período \(MM/AAAA\)

Data

S

S

Formato: MM/AAAA

Mês e ano para a geração dos movimentos\.

Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Informe a Período”

MFS20750

Versão

Alfanumérico 

S

N

Listbox

Este campo é uma lista, que a princípio terá apenas uma opção: \[2\.5\.00\]

Esse evento não será gerado a partir da versão S1\.0\.

MFS20750

MFS\-63139

Geração Multiempresa

Checkbox

N

S

Default: não selecionado

Quando selecionado pelo usuário, a geração será multiempresa\.

Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”\.

MFS20750

Geração através de Estabelecimento Centralizador

Checkbox

N

S

Default: não selecionado

Quando selecionado pelo usuário, a geração será por estabelecimento centralizador\.

Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”\.

Ele marcado irá gerar todos os estabelecimentos centralizados dele\. 

Mensagem no log:

Erro:

'Estabelecimento \- xxx com erro na geração do evento S1250\.'

Não achar o estabelecimento:

' Estabelecimento \- xxx não existem dados para geração do evento S1250\.'

Finalizado o estabelecimento com sucesso:

' Estabelecimento \- xxx com geração do evento S1250 finalizada com sucesso\.'

MFS20750

MFS24243

__*Empresa/Estabelecimento*__

Selecionar

Pasta de Seleção

N

S

Pasta padrão que permite seleção de um estabelecimento específico\.

MFS20750

Marcar Todos

Checkbox

N

S

Default: não selecionado

Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”\.

MFS20750

Relação de estabelecimentos\*

Checkbox

N

S

Default: não selecionado

__Se parâmetro “Geração Multiempresa” e “Geração através de Estabelecimento Centralizador” estiverem desmarcados:__

Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo E somente os estabelecimentos centralizados\*\* ou centralizadores\*, ou seja, o estabelecimento precisa estar centralizado em algum centralizador ou ser um estabelecimento centralizador\. Não iremos demonstrar estabelecimento Descentralizados:

XXX / XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. empresa \+ cód\. e razão social do estabelecimento*

__Se parâmetro “Geração Multiempresa” estiver marcado e o parâmetro “Geração através de Estabelecimento Centralizador” estiver desmarcado:__

Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento \(Centralizados\*\* e Centralizadores\*\), mas neste caso serão demonstradas todas as empresas:

XXX / XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. empresa \+ cód\. e razão social do estabelecimento\)*

__Se parâmetro “Geração Multiempresa” estiver desmarcado e o parâmetro “Geração através de Estabelecimento Centralizador” estiver marcado:__

Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento centralizador\*, somente da empresa que acessou o módulo, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador”:

XXX / Centralizador \- XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. empresa \+ Centralizador \+ cód\. e razão social do estabelecimento\)*

__Se parâmetro “Geração Multiempresa” e o parâmetro “Geração através de Estabelecimento Centralizador” estiverem marcados:__

Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento centralizador\*, mas neste caso serão demonstradas todas as empresas, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador”:

XXX / Centralizador \- XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. empresa \+ Centralizador \+ cód\. e razão social do estabelecimento\)*

__Obs__: No caso da geração multiempresa, as regras da geração do arquivo não se modificam\. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas\.

\* Entende\-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares\. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa \(ou empresas, no caso de geração multiempresa\), não serão demonstrados nenhum estabelecimento\.

\*\* Entende\-se Estabelecimento Centralizado aquele que foi associado a um estabelecimento centralizador na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares\. Caso não exista nenhum estabelecimento cadastrado como centralizado ou centralizador nesta tela para a empresa \(ou empresas, no caso de geração multiempresa\), não serão demonstrados nenhum estabelecimento\.

MFS20750

*\* Descrição não disponível em tela*

