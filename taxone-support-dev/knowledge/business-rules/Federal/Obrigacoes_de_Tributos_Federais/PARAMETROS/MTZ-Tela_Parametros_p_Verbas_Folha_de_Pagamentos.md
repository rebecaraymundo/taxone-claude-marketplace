# MTZ-Tela_Parametros_p_Verbas_Folha_de_Pagamentos

- **Fonte:** MTZ-Tela_Parametros_p_Verbas_Folha_de_Pagamentos.docx
- **Modificado:** 2022-09-26
- **Tamanho:** 38 KB

---

## <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>Tela Parâmetro para Verba \(Folha de Pagamentos\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3832\-A

Alteração de Tela

Inclusão de classes para DIRF\.

 

OS4409

Obrigações de Tributos Federais – Gerar Rendimentos de PLR da SAFX21 com o Código de Receita 3952

O cliente Raízen utiliza a Folha de Pagamento do MasterSAF DW \(tabela: SAFX21\) para a geração das informações da DIRF\. Ocorre que o cliente observou uma situação legal que o sistema hoje não comporta\.

Conforme IN 1\.297 de 2012, os rendimentos tributáveis e de imposto de renda retido na fonte referentes ao PLR – Pagamento de Participação nos Lucros ou Resultados deverão ser gerados sob o código de receita 3562 e não mais sob o código de receita 0561\. Ocorre que ao gerar as informações de um funcionário com suas verbas parametrizadas, todas elas são geradas sob o código 0561 e não sob o código 3562\. Para visualizar essa situação, basta ver a exigência do validador\.

OS4647

Inclusão de Classe para DIRF

Inclusão da Classe: Isentos \- Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995\.

MFS8800

Alteração de Classe para DIRF

Alterado de “Deduções \(Previdência Privada/FAPI\) para “Deduções \(Previdência Complementar\)\.

MFS\-90689

Elisabete Costa

Inclusão da classe: Isentos \(Resgate de previdência complementar por portador de moléstia grave\)

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Na tela de Parametrização das Verbas por Folha de Pagamento \(módulo: Obrigações de Tributos Federais, menu: Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\), deverão ser acrescentadas 9 \(nove\) novas opções no campo “Classe para DIRF”\. As opções são:

- Isentos \(Diária e Ajuda de Custo\)
- Isentos \(Indenizações por Contrato de Trabalho\)
- Isentos \(Abono Pecuniário\)
- Isentos \(Pensão, Aposentadoria ou Reforma por Moléstia Grave\)
- Isentos \(Parcela Isenta de Aposentadoria para Maiores de 65 anos\)
- Isentos Anuais \(Lucros e Dividendos\)
- Isentos Anuais \(Valores pagos a titular ou sócio de empresa\)
- Isentos Anuais \(Outros\)
- Pagamento ao Plano Privado de Assistência à Saúde

0 – Não considerado p/ DIRF

1 – Rendimentos Tributáveis

2 – Deduções \(Previdência Privada\)

3 – Imposto de Renda Retido

4 – Deduções \(Dependentes\)

5 – Deduções \(Pensão Alimentícia\)

6 – Deduções \(Previdência Complementar\)

A – Isentos \(Diária e Ajuda de Custo\)

B – Isentos \(Indenizações por Contrato de Trabalho\)

C – Isentos \(Abono Pecuniário\)

J – Isentos \(Bolsa de Estudo Recebida por Médico Residente\)

K – Isentos \(Benefícios Indiretos e Reembolso de Despesa – Voluntário da Copa\)

D – Isentos \(Pensão, Aposentadoria ou Reforma por Moléstia Grave\)

E – Isentos \(Parcela Isenta de Aposentadoria para Maiores de 65 anos\)

F – Isentos Anuais \(Lucros de Dividendos\)

G – Isentos Anuais \(Valores pagos a titular ou sócio de empresa\)

H – Isentos Anuais \(Outros\)

I – Pagamentos para Plano Privado de Assistência à Saúde

L – Isentos \(Complementação de aposentaria de previdência complementar correspondente às contribuições efetuadas no período de 01 de janeiro de 1989 a31 de dezembro de 1995\.

M – Isentos Anuais \(Juros de Mora Recebidos\)

N – Isentos \(Resgate de Previdência Complementar\)

Essas novas opções deverão ser incluídas após a opção “Deduções \(Previdência Privada/FAPI\)\.

Caso a opção “Isentos Anuais \(Outros\)” seja selecionada, o sistema deverá habilitar embaixo desse campo, um novo campo chamado “Descrição”\. Trata\-se da descrição dos rendimentos isentos – outros e será informada na DIRF por funcionário\. Esse campo deverá ser alfanumérico de 60 \(sessenta\) posições\.

OS3171

MFS\-90689

__RN01__

 Inclusão das opções Isentos \(Bolsa deEstudo Recebida por Médico Residente\)  e Isentos \(Benefícios Indiretos e Reembolso de despesa – Voluntário da Copa\) no Parâmetro da DIRF:Classe p/ DIRF\.

OS3832\-A

__RN02__

Deverá ser criado na tela de “Parâmetros por Verba” do módulo Obrigações de Tributos Federais, o parâmetro “Incide PLR”\. Ao abrir a tela, esse parâmetro será do tipo check\-box e por default ficará desmarcado\. 

Ele deverá ficar localizado antes do parâmetro “Classe p/ DIRF”\.

Ao marcar o parâmetro “Incide PLR”, o campo “Classe p/ DIRF” só ficará com as seguintes opções habilitadas: “Rendimentos Tributáveis”, “Deduções \(Pensão Alimentícia\)” e “Imposto de Renda Retido”\. As outras opções do campo “Classe p/ DIRF” não ficarão habilitadas ou não poderão ser visualizadas\.

OS4409

__RN03__

O relatório de conferência da tela de “Parâmetros por Verba deverá ser alterado para contemplar o novo campo “Incide PLR”\.

OS4409

__RN04__

Deverá incluir na lista de classe para DIRF a opção Isento \(Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995\)

OS4677

__RN05__

A opção “Deduções \(Previdência Privada/FAPI\) do campo Classe para Dirf deverá ser alterado para “Deduções \(Previdência Complementar\)”\.

MFS8800

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

