# MTZ-Ferramentas-Status-Concorrencia

- **Fonte:** MTZ-Ferramentas-Status-Concorrencia.docx
- **Modificado:** 2020-07-13
- **Tamanho:** 66 KB

---

THOMSON REUTERS

                                                                                     __Módulo Job Servidor__

__  __

__Tela de Status de Concorrência__

__Localização__: Menu Básicos, Módulo Ferramentas, item Parâmetros do Sistema 🡪 Status de Concorrência

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS35999

Andréa Rocha

Este documento tem como objetivo incluir um quadro para replicar os estabelecimentos\.

09/07/2020

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

  A tela recupera os dados da tabela de Concorrência do Data Mart \(PRT\_IDENT\_DMART\) por tabela e estabelecimento\.  O objetivo é o usuário poder trocar o status da concorrência por tabela do Data Mart \(DWT\_DOCTO\_FISCAL, DWT\_ITENS\_MERC e DWT\_ITENS\_SERV\), para cada estabelecimento selecionado\.

__RN01__

__                                                        Parâmetros de Tela__

__Estabelecimentos__ – Neste campo serão disponibilizados para seleção do usuário todos os estabelecimentos da Empresa do login\.

__Nome Tabela __– Este campo é uma lista com as opções: DWT\_DOCTO\_FISCAL, DWT\_ITENS\_MERC e DWT\_ITENS\_SERV\.

__Status Concorrência__ –__ __Este campo é uma lista com as opções: Sim e Não\.

__Replicar para os Estabelecimentos – __Este campo é um checkbox, default desmarcado\.

__Quadro de Estabelecimentos\- __Quadro dos estabelecimentos da Empresa do login, com a opções de marcar/desmarcar todos os estabelecimentos\. Somente será habilitado quando for marcada a opção “Replicar para os Estabelecimentos”__\.                  __

__RN02__

__                                                         Processamento __

Os dados serão recuperados da tabela de Concorrência do Data Mart \(PRT\_IDENT\_DMART\) e será atualizado o campo Status da Concorrência, de acordo com a opção escolhida \(Sim/Não\), para a tabela e os estabelecimentos selecionados\.  Quando a opção “Replicar para os Estabelecimentos__” __estiver marcada, deve ser replicado o Status da Concorrência para todos os estabelecimentos selecionados\.     

