---
source: "MTZ-REPORT_FISCAL-ISS-Texto_Legal_p_Comprovacao_de_Retencao.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL => ISS => Texto Legal p/ Comprovação de Retenção


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3096-A3
Alteração na Comprovação de Retenções de ISSQN para gerar multi-empresa
Criar a opção de geração por Multi-empresa.


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00

O menu: REPORT FISCAL => ISS => Texto Legal p/ Comprovação de Retenções

Essa opção terá os mesmos filtros que a atualmente, com inclusão do campo EMPRESA.

OS3096-A3
RN01

O campo EMPRESA irá listar:

* Cada uma das Empresas cadastradas - Quando selecionada, caso tenha movimentação no período e demais filtros escolhidos será demonstrada no relatório.

Obs. Esse campo não terá a opção "TODAS", sendo obrigatório que o cliente selecione a EMPRESA que deseja realizar a manutenção. Caso não selecione, ao tentar salvar deverá ser exibida a mensagem:

"Falta valor obrigatório para 'Empresa'. Por favor, entre com o valor"

OS3096-A3
RN02

Ao definir a EMPRESA, o usuário também deverá definir o ESTABELECIMENTO, para inserir dados com sucesso.

OS3096-A3
RN03
O Relatório terá o mesmo layout que o atual, incluindo o Código da Empresa do lado esquerdo da descrição no Cabeçalho.

Os Estabelecimentos serão ordenados por EMPRESA.

OS3096-A3
RN04
Descrição da Regra de Negócio 01

RN05
Descrição da Regra de Negócio 00

RN06
Descrição da Regra de Negócio 01


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

