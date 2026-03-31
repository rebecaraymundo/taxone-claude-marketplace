---
source: "MTZ-RF-ObrigAcessorias-DM-Relatorio_de_NFs_por_CFOP.docx"
category: Report_Fiscal
converted: auto
---

# Report Fiscal – RF – DM – Relatório de Notas p/CFOP


Localização: Módulo Report Fiscal, item Obrigações Acessórias > ICMS/IPI por DataMart > Relatório de NF p/ CFOP


DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO




---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS2484 | Inclusão do Parâmetro "UF" na Emissão de Relatórios | Incluir o parâmetro “UF” na emissão dos relatórios. |
| Chamado 478-A/15 | Correção no tratamento das NF’s de entrada extemporânea | Correção no tratamento das NF’s de entrada extemporânea (ver RN06) |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | O cursor deverá apontar para o 1º campo da tela de parametrização, ou seja, para o parâmetro “UF”. | OS2484 |
| RN01 | O conteúdo do campo “Estabelecimento” será de acordo com o estado selecionado no campo “UF”, sendo apenas apresentado(s) o(s) estabelecimento(s) pertinente(s) àquele estado. Dessa forma o usuário poderá emitir o relatório para apenas um estabelecimento do estado selecionado ou todos os estabelecimentos do mesmo estado. | OS2484 |
| RN02 | Se o campo “UF” estiver em branco, o campo “Estabelecimento” deve apresentar todos os estabelecimentos cadastrados para a empresa em questão, deixando a critério do o usuário a emissão do relatório para apenas um estabelecimento ou todos os estabelecimentos separados por estado. | OS2484 |
| RN03 | O parâmetro “UF” deve conter as siglas dos estados da tabela TFIX04 (Tabela de Estados). | OS2484 |
| RN04 | O campo “UF” do relatório deve apresentar a sigla do estado selecionado na parametrização da emissão do relatório. | OS2484 |
| RN05 | Se o modo de emissão for apenas para um estabelecimento específico, o campo “UF” deve apresentar a sigla do estado do estabelecimento. | OS2484 |
| RN06 | Tratamento das notas de entrada extemporâneas:  Na recuperação das notas a serem exibidas no relatório, serão consideradas as notas fiscais de entrada extemporâneas, seguindo o mesmo conceito da Apuração do ICMS, ou seja:  Serão recuperadas as notas de entrada extemporânea cuja data extemporânea (campo DAT_ESCR_EXTEMP da SAFX07) se enquadre no período solicitado para a emissão do relatório.   Obs: Esta regra foi documentada em Jan/2016 (chamado 478-A/2015), com objetivo apenas de registrar o funcionamento do relatório, de acordo com testes realizados. Ou seja, os testes realizados demonstraram que o relatório já tratava as notas extemporâneas, mas apresentava problemas nos casos em que a diferença de dias entre a data de emissão e a data extemporânea fosse superior a 60 dias. . |  |
