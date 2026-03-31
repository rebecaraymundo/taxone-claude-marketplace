---
source: "MTZ-PowerLock-Palavras_nao_permitidas.doc"
category: Seguranca
converted: auto
---

Power Lock - Controle de Segurança - Palavras não permitidas

Localização:
Powerlock > File > Controle de Segurança > Palavras não permitidas


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3894
DW - BASICOS - SEGURANÇA - Tratamento para utilização de password
O objetivo da OS é criar novas regras para a criação/alteração de senhas no PowerLock.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Regra geral da tela
Essa tela deve ser multi-registro e quando a mesma for aberta devem ser exibidos todos os registros já cadastrados nela. Os registros devem ser exibidos em ordem alfabética.

Botões de ação:
Novo: Esse botão permite que um novo registro seja incluído
Excluir: Esse botão permite que o registro selecionado seja excluído
Confirmar: Esse botão permite que os registros alterados sejam salvos
Ordernar: Esse botão permite que os registros sejam ordenados de A -> Z ou de Z -> A.
Sair: Esse botão permite que a tela seja fechada
OS3894
RN01
Regra p/ campo Palavra
Esse campo deve ser um textbox e deve conter 20 posições.
OS3894


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN


