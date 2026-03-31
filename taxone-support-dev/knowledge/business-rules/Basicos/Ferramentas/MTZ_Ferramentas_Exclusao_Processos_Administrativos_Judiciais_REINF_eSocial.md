# MTZ_Ferramentas_Exclusao_Processos_Administrativos_Judiciais_REINF_eSocial

- **Fonte:** MTZ_Ferramentas_Exclusao_Processos_Administrativos_Judiciais_REINF_eSocial.docx
- **Modificado:** 2021-05-04
- **Tamanho:** 64 KB

---

THOMSON REUTERS

Ferramentas

Exclusão Processo Administrativo Judicial \(REINF/eSocial\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS10287

Lara Aline

Inclusão da exclusão dos registros das tabelas de Processos Administrativos/Judiciais \(SAFX2058\) e seus itens filhos  de Suspensão de Exigibilidade de Tributos \(SAFX2059\)\. 

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Regras Gerais__

A tela deve ser do tipo FrameWork, com as abas Parâmetros, Processo e Log\.

Funcionamento: O usuário deve informar a data inicial e final e o estabelecimento\. Essa execução deve excluir as informações da SAFX2058 \- Cadastro de Processos Administrativos/Judiciais \(X2058\_PROC\_ADJ\) e de todas as tabelas que são dependentes desta como no caso a SAFX2059 \- Informação de Suspensão de Exigibilidade de Tributos \(X2059\_SUSP\_TBT\)\. Será excluído todas as informações de processos que possuem a mesma Data Inicial selecionada em tela, verificando campo VALID\_PROC\_ADJ\_INI da SAFX2058\.

Na aba de Log deve ser exibida a mensagem: “Foram excluídos” \+ número de registros excluídos \+ “da tabela” \+ nome da tabela\.

Somente será efetuada a exclusão se o Processo Administrativo/Judicial \(SAFX2058\) que não estiver relacionado em nenhuma outra tabela, ou seja, o processo selecionado através da data de início e estabelecimento informado em tela não poderá estar sendo usado em nenhuma nota ou cadastro no momento da exclusão\.

Abaixo segue as tabelas que deverão ser verificados o relacionamento:

SAFX03 \- Arquivo de Fornecedores \(Contas a Pagar\)

SAFX08 \- Itens Notas Fiscais Mercadorias e Produtos

SAFX09 \- Itens Notas Fiscais de Serviços

SAFX248 \- Demonstrativo de Pagamento dos Autônomos – Rubricas

SAFX263 \- Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte

SAFX531\- Rendimentos de Decisão Judicial

SAFX2037 \- Tabela de Setor 

SAFX2113 \- Processos relacionados à Suspensão da CPRB

SAFX2114 \- Tabela de Cadastro das Rubricas \(eSocial\)

esocial\_inf\_estab \- Parametrização “Informações do Estabelecimento” do Módulo eSocial

Caso seja encontrado relacionamento em alguma dessas tabelas na aba de Log deve ser exibida a mensagem: “Não foi possível efetuar a exclusão pois o processo está referenciado em outra tabela”\.

Processo Administrativo/Judicial: <numero\-do\-processo> 

MFS10287

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

