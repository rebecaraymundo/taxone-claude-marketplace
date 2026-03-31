---
source: "MTZ-REPORT_FISCAL-ISS-Recolhimento_de_ISSQN.doc"
category: Report_Fiscal
converted: auto
---

REPORT FISCAL - ISS - Recolhimento de ISSQN


DOCUMENTO DE REQUISITO

DR
Nome
Descrição


OS2920


Report Fiscal - ISSQN - Recolhimento de ISSQN


Melhoria no relatório no Report Fiscal ? Obrigações Acessórias ? ISS ? Recolhimento de ISSQN. Ele pede que o relatório tenha a opção de gerar separadamente as notas que tenha retenção de ISSQN daquelas notas que tiveram ISSQN com valor menor que 0.

MFS-769155
Alessandra Navatta
Apenas no produto TAXONE:
* Incluir colunas no relatório de Recolhimento de ISSQN (por empresa) (RN03) 
*  Migração do relatório para o Servidor de Relatórios. RN04
* Criação do formato em Excel (RN05)
* Layouts dos relatórios, dos formatos em PDF e Excel (RN06)

Não foi realizada a reversa do relatório

MFS-769159
Alessandra Navatta
Apenas no produto TAXONE:

Inclusão da coluna Feriado (RN03), nos formatos PDF e Excel. Inclusão da coluna no layout (RN06)

MFS-840902
Alessandra Navatta
Transformar o parâmetro Com Retenção e Sem Retenção em check-box e não radio-button. Criar um título/agrupamento para o parâmetro (Notas a Considerar) (RN00, RN01 e RN02). Este ajuste deve ser feito apenas no produto TAXONE.
MFS-838425
Alessandra Navatta
Inclusão do parâmetro Tipo de Relatório com as opções Analítico e Sintético. Definição dos layouts (formato pdf e Excel)  do tipo Sintético. Este ajuste deve ser feito apenas para o TAXONE
MFS-923058
Rafael Fabiano
Apenas no produto TAXONE:
* Incluir colunas no relatório analítico de Recolhimento de ISSQN nos formatos Excel e PDF: "Descrição de município", (RN03) e (RN06).
* Alteração na regra campo parâmetros notas a considerar no relatório do Report fiscal das notas com e sem retenção, (RN00, RN01).
* Incluir no relatório de Recolhimento de ISSQN a opção de geração por multiempresa, (RN08).

Não foi realizada a reversa do relatório.


MFS-922949
Rafael Fabiano
Apenas no produto TAXONE:

* Alteração na regra do relatório Sintético de Recolhimento de ISSQN no formato de visão guia de pagamento em Excel.xslx e PDF. (RN07)


MFS-928571

Alessandra Navatta
Rafael Fabiano
Apenas no Produto TAXONE:

Criação da Data Vencimento Feriado nos relatórios Analitico e Sintético. (RN03) e (RN07).
REGRAS DE NEGÓCIO

Cód.
Descrição
DR


RN00


Criação de dois novos flegs COM RETENÇÃO e SEM RETENÇÃO, no relatório:

Módulo: Estadual ? Report Fiscal 
Menu: Obrigações Acessórias ? ISS ? Recolhimento de ISSQN.

Caso nenhum dos dois novos flegs seja selecionado pelo usuário, o relatório deverá ser gerado normalmente.

Os novos flegs devem ser criados nas duas opções Por Empresa e Por Estabelecimento.


[EXCLUSÃO MFS-923058] [ALTERAÇÃO MFS-840902]

Na opção por Empresa:

* Criação do agrupamento Notas a Considerar.
* Transformar as opções Com Retenção e Sem Retenção, em check-box e não radio button conforme mockup, por default a opção 'Com Retenção', deve ser marcada, mas, pode ser desmarcada pelo usuário, se necessário. 
* Pelo menos uma das opções deve ser marcada, caso contrário, exibir a mensagem: "Favor informar pelo menos uma opção de Notas a ser Considerada na geração do relatório!"


OS2920
MFS-840902
MFS-838425
MFS-923058


[ALTERAÇÃO MFS-838425] Produto TAXONE:
Criação da Opção Tipo de Relatório, com as opções Analítico e Sintético, por default a opção analítica será marcada, mas, pode ser alterada.

Observação: devem ter como opções os formatos em Excel.XSLX e PDF.


RN01

Regra para o fleg COM RETENÇÃO:

Caso esse novo fleg seja selecionado, deverão trazer no relatório somente as notas que tiverem retenção de ISSQN, ou seja, valores > 0.

Se o fleg COM RETENÇÂO for selecionado, o outro deve ser desabilitado, impedindo que os dois flegs sejam selecionados simultaneamente.

[ALTERAÇÃO MFS-840902] Produto TAXONE

Regra para o flag COM RETENÇÃO:

Caso esse flag seja selecionado, deverão trazer no relatório somente as notas que tiverem retenção de ISSQN, ou seja, valores > 0.

Se o flag 'Com Retenção' for selecionada, a outra opção pode ou não ser selecionada.

Parametros notas a considerar:


1. Quando o parâmetro estiver marcado com retenção: 
Com retenção, deverão trazer no relatório somente as notas que tiverem retenção de ISSQN, ou seja, valores > 0, ou seja, as notas que tiverem retenção, recuperar campo 58 VLR_ISS_RETIDO, SAFX09.

2. Quando o parametro estiver marcado sem retenção
Sem retenção, deverão trazer no trazer no relatório somente as notas que tiverem  sem a retenção de ISSQN, ou seja, valores = 0, ou seja, as notas que tiverem retenção, recuperar campo 58 VLR_ISS_RETIDO, SAFX09.

3. Quando o paramentro estiver marcado ambos:
Ambos, Deverão trazer no relatório todas as notas que tiverem com e sem retenção de ISSQN, ou seja valores >, e, ou = 0, recuperar campo 58 VLR_ISS_RETIDO, SAFX09.


OS2920
MFS-840902
MFS-923058
RN02

Regra para o fleg SEM RETENÇÃO:

Caso esse novo fleg seja selecionado, deverão trazer no relatório somente as notas com o valor de retenção de ISSQN = 0, ou seja, as notas fiscais que não tiveram retenção.

Se o fleg SEM RETENÇÂO for selecionado, o outro deve ser desabilitado, impedindo que os dois flegs sejam selecionados simultaneamente.

[ALTERAÇÃO MFS-840902] Regra para o flag SEM RETENÇÃO:

Caso esse novo flag seja selecionado, deverão trazer no relatório somente as notas com o valor de retenção de ISSQN = 0, ou seja, as notas fiscais que não tiveram retenção.

[ALTERAÇÃO MFS-840902,] Se o flag 'Sem Retenção' for selecionada, a outra opção pode ou não ser selecionada.


OS2920
MFS-840902

RN03


Apenas para o Produto TAXONE, quando Tipo de Relatório for Analítico:

Inserir no Relatório Analítico de Recolhimento de ISSQN (por Empresa) as colunas:

* Mês/Ano Fiscal: Recuperar o campo, DATA_FISCAL, da tabela IST_RECOLHIM_ISSQN (Formato MM/AAAA)
* Mês/Ano Emissão: Recuperar o campo DAT_EMISSAO, da tabela IST_RECOLHIM_ISSQN (Formato MM/AAAA)
* Situação: Recuperar o campo 30 - SITUACAO, da SAFX07. Se 'N', exibir 'Normal'. Se 'S', exibir 'Cancelada'
* Movto. E/S: Recuperar o campo 03-MOVTO_E_S, da SAFX07. Se 9 = Saída, se diferente de 9 = Entrada.
* Número de Controle: Recuperar o campo 69 -NUM_CONTROLE_DOCTO, da SAFX07
* Valor Multa: Recuperar o campo VLR_MULTA da tabela IST_RECOLHIM_ISSQN
* Valor Juros: Recuperar o campo VLR_JUROS da tabela IST_RECOLHIM_ISSQN
* Serviço: Recuperar o campo COD_SERV_LEI116, da tabela IST_RECOLHIM_ISSQN
* Valor Total Nota: Recuperar o campo 23 - VLR_TOT_NOTA, da SAFX07
* Dia Vencimento: Recuperar o campo 10 - DIA_VENCTO, da SAFX2097
* Observações: Recuperar o campo 18 - OBS_ISS2, da SAFX2097
* Inscrição Municipal:  Recuperar o campo 7 - INSC_MUNICIPAL, da SAFX2064
* Munícipio (do Estabelecimento): Recuperar o campo 37 - COD_MUNICIPIO_ISS, da SAFX2064

[ALTERAÇÃO MFS-769159] Inclusão da coluna

* Feriado: Recuperar o campo 59 - IND_VENC_FERIADO, da SAFX2097

[ALTERAÇÃO MFS-923058] Inclusão da coluna

* Descrição do município estabelecimento:Recuperar o campo 15 - CIDADE, da SAFX2064.

[ALTERAÇÃO MFS-928571] Criação da data  vencimento feriado

* Data vencimento feriado:  O campo 'Data Vencimento Feriado' deve ser preenchido somente quando a data de vencimento do município for um dia não útil, ou seja:Sábado, Domingo ou Feriado (federal, estadual ou municipal)

Identificação de dia não útil:
Considerando o campo 10 - DIA_VENCTO da tabela x2097, verificar se essa data é um sábado, domingo ou um feriado para o município em questão. 
Considerar feriado, os registros da tela Feriado (Básico ? Data Warehouse  ?Manutenção ? Cadastros ? Feriados), indepentende se for um feriado federal, estadual ou municipal.

Quando preencher:
o Caso seja um dia útil (não é feriado, não é sábado e nem domingo), o  campo data vencimento feriado, deve ser preenchido com a mesma data do campo 10 - DIA_VENCTO

o Se a data de vencimento for um dia não útil, então: 
* Consultar o campo 59 - IND_VENC_FERIADO da tabela SAFX2097:
Básico ? Data Warehouse ? Manutenção ? Cadastros ? Município ISS ? Manutenção.
* Se IND_VENC_FERIADO estiver vazio:
o Preencher Data Vencimento Feriado com a mesma data do campo Data de Vencimento (campo 10 - DIA_VENCTO).
* Se IND_VENC_FERIADO = "Antecipa":
o Preencher Data Vencimento Feriado com a data do dia útil imediatamente anterior à data original de vencimento.
* Se IND_VENC_FERIADO = "Posterga":
o Preencher Data Vencimento Feriado com a data do dia útil imediatamente posterior à data original de vencimento.

MFS-769155
MFS-769159
MFS-838425
MFS-923058
MFS-928571

RN04


Apenas para Produto TAXONE


Migrar o relatório para o servidor de relatórios.


Incluir o campo Tipo de Geração na tela Relatório de Recolhimento de ISSQN (por Empresa).


Permite escolher a opção de geração.
Lista de valores válidos:
* Arquivo PDF
* Excel (XLSX)


A opção default é "Arquivo PDF"
 


   MFS-769155

RN05
Formato Excel, no produto TAXONE

Criar a versão em excel, com as mesmas colunas apresentadas no formato em PDF.
MFS-769155
RN06
Layout dos relatórios, no produto TAXONE [ALTERAÇÃO MFS-923058]


Estão disponíveis no arquivo 'Layout_Relatorio_Recolhimento_ISSQN_Por_Empresa.xlsx' (as planilhas PDF e EXCEL), conforme a opção do tipo de relatório selecionada (analítico ou sintético).

Houve inclusão de colunas e atualização do header (renomeado o label Filial para Estabelecimento), no formato PDF e Excel.

MFS-769155
MFS-769159
MFS-838425
MFS-923058


RN07
Apenas para Produto TAXONE [ALTERAÇÃO MFS-923058]

Quando a opção 'Sintético' do Campo Tipo de Relatório estiver selecionada, apresentar todos os campos do tipo analítico, exceto: 
* Nº, Série e Subsérie do documento fiscal
* Data fiscal
* Data Emissão
* Mês/Ano Emissão
* Número de Controle
* Alíq. ISS

A recuperação dos dados será a mesma que a do tipo analítico, porém, o agrupamento será por Fornecedor, Município, Mês/ano fiscal, Situação, Mov. E/ e Serviço.

Quando a opção "Sintético" do campo Tipo de Relatório estiver selecionada devem ser sumarizados os campos do tipo analíticos abaixo:

* Cod. Empresa;
* Cod. Estab.;
* Data fiscal;
* Mês/ ano fiscal;
* Município;
* Valor total nota;
* Valor Base ISS;
* Valor ISS;
* Data vencimento;
* Vencimento feriado.

[INLCUSÃO DE REGRA MFS-928571] Criação da coluna Data Vencimento Feriado, considerar a mesma regra indicada na RN03


MFS-838425
MFS-922949
MFS-923058
MFS-928571
RN08
Apenas para Produto TAXONE

Permitir a geração do relatório Recolhimento ISSQN por Multiempresa. Devera ser disponibilizado o componente de empresa. 


No componente deve ser apresentado todas as empresas que o usuario tem acesso. Pelo menos uma das empresas devem estar marcadas, caso contrário, exibir a mensagem: "Favor informar pelo menos uma empresa!"
Disponibilizar os botões selecionar todos e desmarcar todos. 
* Selecionar todos: Permite selecionar automaticamente todos os registros do componente. 
* Desmarcar todos: Permite desmarcar todos os registros selecionados.


MFS-923058


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

