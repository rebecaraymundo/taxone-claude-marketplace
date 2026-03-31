---
source: "MTZ_REPORT_FISCAL_Tela_Relatorio_Conferencia_dos_Documentos_Fiscais_ICMS_IPI_PIS_COFINS.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS

Conferência dos Documentos Fiscais (ICMS/IPI/PIS/COFINS)
Tela do Relatório Conferência dos Documentos Fiscais (ICMS/IPI/PIS/COFINS)



DOCUMENTO DE REQUISITO


Sumário

**1.	Regras dos Campos	3**
2.	Sugestão de Layout	4

# Regras dos Campos

Localização da tela: Básicos\ Report Fiscal\ Gerenciais\ Documentos Fiscais\ Analíticos\ Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS)

Título da tela: Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS)



# Sugestão de Layout




---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| CH6894_2015 | Julyana Perrucini | Esse documento tem como objetivo incluir os botões “Marcar Todos” e “Desmarcar Todos” para os Estabelecimentos da tela de geração do relatório “Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS)” do módulo Básicos >> Report Fiscal. |
| OS4808 | Julyana Perrucini | Este documento tem como objetivo incluir novo parâmetro no relatório de Conferência de Documentos Fiscais (ICMS/IPI/PIS/COFINS), módulo Básicos – Report Fiscal, para apresentação da coluna “Descrição” por código do produto/ serviço ou pela descrição complementar do documento fiscal. |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimentos | Texto | N | S | Formato:  Check Box  Default:  Habilitado | Permite que o usuário selecione um ou mais estabelecimentos para realizar a geração do relatório.  [ALTERADA – CH6894_2015] Tratamento: Deverá vir em forma de lista e não será obrigatório informar estabelecimento, mas caso não seja marcado o relatório virá em branco sem movimentação dos documentos; Opção de ‘Marcar Todos e “Desmarcar Todos”. | CH6894_2015 |
| Exibir Código Produto/Serviço | Texto | N | S | Formato:  Check Box  Default:  Habilitado e Desmarcado | Permite que o usuário marque a opção caso desejar gerar o relatório apresentando na coluna Descrição o código de produto e/ ou serviço destacado no documento fiscal.  Observação: Gerar Descrição Complementar como default. | OS4808 |
