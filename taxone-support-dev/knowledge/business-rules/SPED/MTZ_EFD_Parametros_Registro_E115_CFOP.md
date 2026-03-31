# MTZ_EFD_Parametros_Registro_E115_CFOP

> Fonte: MTZ_EFD_Parametros_Registro_E115_CFOP.docx






THOMSON REUTERS

Parâmetros p/ Geração do Registro E115 por CFOP
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registros E115/1925\ Registro E115(Específico RS)\ CFOP

Título da tela: Parâmetros por CFOP – Informações Adicionais da Apuração (Registro E115)

Tratamentos:

[MFS57858] Regra para Bloquear parametrização de um CFOP, para códigos adicionais diferentes.
[MFS80289] Regra para Desbloquear Geração de um CFOP, para códigos adicionais diferentes e adicionar Log de Aviso


A opção do item de menu Registro E115 – CFOP só será habilitada quando o estabelecimento iniciado tiver a UF cadastrada igual a “RS”;
Se houver o mesmo CFOP para códigos adicionais diferentes para o mesmo Anexo, deverá ser utilizado o Parâmetro de CFOP/Natureza de Operação. Exemplo:
O mesmo CFOP pode ter códigos adicionais diferentes para o mesmo Anexo. Exemplo:

GIA – Anexos: Anexo I.C
Código: RS013001
CFOP: 1101

GIA – Anexos: Anexo I.C
Código: RS013091
CFOP: 1101


Verificar se o CFOP está parametrizado para mais de um código adicional para os Anexos V.A e V.B
SE sim criar log de aviso:

Aviso: CFOP “XXXX” parametrizado para códigos adicionais diferentes, para o Anexo V.A ou V.B, para evitar duplicidades preencher o Campo 255 - COD_BENEFICIO da Tabela SAFX08 ou utilizar o Parâmetro de CFOP/Natureza de Operação.

Verificar se o CFOP já está sendo utilizado para um código adicional.
SE sim bloquear nova parametrização.


Regra Geral Botões:

-- EXCLUI – Permite excluir registro ao desmarcar o CFOP.

CONFIRMA – Permite salvar registro.

RELATÓRIO – Permite emitir relatório listando todos os registros existentes na base de dados ou de acordo com a Empresa e Estabelecimento selecionados na tela de login (mostrar todos os campos como critério de busca).

FECHA – Permite sair da tela.



## Sugestão de Layout




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-13074 | Julyana Perrucini | Essa MFS tem como objetivo criar parametrização para geração do Registro E115. |
| MFS-24916 | Liliane Assaf | Reestruturação de Menu (Específico RS) |
| MFS-57858 | Rogério Ohashi | Regra para bloquear parametrização de um CFOP para mais de um Código de Informação Adicional, para evitar duplicidade na geração dos Registros E115. |
| MFS-80289 | Rogério Ohashi | Regra para desbloquear parametrização de um CFOP para mais de um Código de Informação Adicional, e incluir Log de Mensagem para evitar duplicidade na geração dos Registros E115. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato:  Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir mostrar estabelecimento a ser parametrizado para geração dos registros. Inicialmente serão considerados apenas os estabelecidos no Rio Grande do Sul.  Tratamento: O campo será apresentado de forma desbloqueada e caso o usuário entre com um estabelecimento no Login, somente este será apresentado e bloqueado; O campo será apresentado de forma desbloqueada e caso o usuário não entre com um estabelecimento no Login, deverá apresentar a lista dos estabelecimentos de UF igual a RS; Se o campo não for preenchido, emitir a mensagem na tela: “Estabelecimento deve ser preenchido”. | MFS-13074 |
| GIA – Anexos | Texto | S | N | Formato: Combo Box  Default: Habilitado/Desabilitado (ver tratamento) | Permitir demonstrar Quadros/ Anexos/ Registros da GIA relacionados ao Registro E115.  Conteúdo: Para estabelecidos na UF do Rio Grande do Sul serão apresentados:  Anexo I.C Anexo V.A Anexo V.B Anexo V.C  Tratamento: O campo será apresentado de forma desbloqueada e depois que salvar o registro deverá ser bloqueado; Se o campo não for preenchido, emitir a mensagem na tela: “GIA Anexos deve ser preenchido”. | MFS-13074 |
| Código | Texto | S | S | Formato: Pesquisar Pasta – Seleção da Manutenção Informações Adicionais da Apuração (Registro E115/ 1925)  Default: Habilitado | Permitir seleção da tabela dos códigos parametrizados na Manutenção Informações Adicionais da Apuração (Registro E115/ 1925), item de menu Parâmetros – Registros E115 e 1925.  Tratamento: Bloquear a entrada dos códigos RS013006 e RS053006 na seleção, eles se tratam de Exclusões Parciais que já não eram geradas de forma automática na GIA-RS; Se o campo não for preenchido, emitir a mensagem na tela: “Código deve ser preenchido”. | MFS-13074 |
| CFOP’s | Texto | S | S | Formato: Check Box  Default: Habilitado | Permitir demonstrar os CFOP cadastrados na SAFX2012.  Tratamento: Se o campo GIA – Anexos for igual a I.C, listar apenas CFOP iniciados com 1,2,3; Se o campo GIA – Anexos for igual a V.A, V.B ou V.C, listar apenas CFOP iniciados com 5,6,7.  Como facilitador, poderão ser utilizados os botões “Selecionar todos” e “Desmarcar todos”. | MFS-13074 |
| Replicar para Estabelecimentos | Texto | N | S | Formato: Check Box  Default: Habilitado | Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos.  Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento” e apenas aos estabelecidos na UF do Rio Grande do Sul.  Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação.   Como facilitador, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”. | MFS-13074 |
