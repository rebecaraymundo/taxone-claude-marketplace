# MTZ-SEFII-Parametrizacao_dos_Perfis

- **Fonte:** MTZ-SEFII-Parametrizacao_dos_Perfis.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

                                                             __Módulo SEF II – Parametrização dos Perfis__

__ __

__ __

__Localização__: Menu Estadual, Módulo SEF II \- PE, item Parâmetros 🡪 Perfil

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4623

Atualização legal SEF II

Separação do arquivo “LA \+ Guias” em dois arquivos distintos \(ver RN01, RN03 e RN04\)

23/10/2014

\(criação do docto\)

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

__RN01__

__                                                        Campo “Leiaute”__

Campo __Leiaute__ 🡪  Este campo é uma lista dos layout’s existentes no SEF II, que engloba os diferentes arquivos:

Alteração da __OS4623:__ Com a separação do arquivo “LA\+Guias” em dois arquivos distintos, a lista teve as seguintes alterações:

\- Inclusão do item “GI\-Guias de Informação do ICMS”;

\- O item original “LA – Livros da Apuração \+ Guias” foi renomeado para “LA – Livros da Apuração”; 

EDoc – Extrato de Documentos Fiscais

GI – Guias de Informação do ICMS

LA – Livros da Apuração

LMC – Livro de Movimentação de Combustíveis

RI – Registro de Inventário

RIDF – Registro de Impressão de Documentos Fiscais

RV – Registro de Veículos

__RN02__

__                                                        Campo “Perfil”__

Campo __Perfil__ 🡪 Neste campo o usuário informará o código e uma descrição para o perfil\.

__RN03__

__                                                        Definição dos Blocos__

__Definição dos Blocos:__

Alteração da __OS4623:__ Com a separação do arquivo “LA\+Guias” em dois arquivos distintos, a definição dos blocos destes dois arquivos ficou da seguinte forma:

	

Para a opção de layout = “__LA – Livros da Apuração__” 🡪 Serão disponibilizados os blocos 0, E e 9;

Para a opção de layout = “__GI – Guias de Informação do ICMS__” 🡪 Serão disponibilizados os blocos 0, G, 8 e 9;

__RN04__

__                                                     Definição dos Registros__

__Definição dos Registros:__

Alteração da __OS4623:__ Com a separação do arquivo “LA\+Guias” em dois arquivos distintos, a definição dos registros destes dois arquivos ficou da seguinte forma:

Para a opção de layout = “__LA – Livros da Apuração__”:

   \- No Bloco 0 🡪 0000, 0001, 0005, 0025, 0030, 0100, 0150, 0400, 0450, 0455, 0460, 0465 e 0990

   \- No Bloco E 🡪 todos os registros do Bloco E \(\*\)

   \- No Bloco 9 🡪 todos os registros do Bloco 9 \(\*\)

\(\*\)conforme a planilha de layout do arquivo LA \(disponível no site da Sefaz\-PE\)

*\(são exatamente os mesmos registros que eram disponibilizados antes da separação dos arquivos, exceto pelos registros dos blocos G e 8, já que estes blocos não fazem mais parte deste arquivo\)*

Para a opção de layout = “__GI – Guias de Informação do ICMS__”

   \- No Bloco 0 🡪 0000, 0001, 0005, 0025, 0030, 0100, 0150 e 0990

   \- No Bloco G 🡪 todos os registros do Bloco G \(\*\)

   \- No Bloco 8 🡪 todos os registros do Bloco 8 \(\*\), sendo que o registro 8575 \(GIAF 2 Prodepe Importação – Crédito Presumido\) fica desabilitado 

   \- No Bloco 9 🡪 todos os registros do Bloco 9 \(\*\)

\(\*\)conforme a planilha de layout do arquivo GI \(disponível no site da Sefaz\-PE\)

*\(para os blocos G e 8, são exatamente os mesmos registros que eram disponibilizados antes da separação dos arquivos, já no bloco 0 saíram alguns registros não utilizados no arquivo “GI”\)*

= = = = = 

