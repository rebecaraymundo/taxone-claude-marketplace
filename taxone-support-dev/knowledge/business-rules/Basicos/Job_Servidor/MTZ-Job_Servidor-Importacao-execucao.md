# MTZ-Job_Servidor-Importacao-execucao

- **Fonte:** MTZ-Job_Servidor-Importacao-execucao.docx
- **Modificado:** 2026-01-20
- **Tamanho:** 46 KB

---

# Módulo – Job Servidor – Importação Batch – execução

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

###### OS4757

###### Geração Multiempresa

Inclusão de novas tabelas no tratamento multiempresa

CH56743

Incluir novo código de situação no processo

Na tabela safx08 foi incluído novo código  de situação tributária de PIS e de Cofins\.

CH68023

Preencher campo ind\_tp\_registro quando nulo

Abastecer o campo ind\_tp\_registro com valor um quando o mesmo não for informado pelo usuário na carga\.

MFS\-92054

Alessandra Cristina Navatta

Inclusão de mensagem, __APENAS__ __no produto TAXONE, quando o parâmetro __IND\_VALID\_IMPORT__’ da tabela __PRT\_PAR\_MSAF__, estiver marcado com ‘S’ e__ ao tentar executar uma importação com os mesmos dados \(informação de empresa, estabelecimento, data inicial, data final e arquivo\) de uma importação que ainda não foi finalizada\. \(RN04\)

__Atenção: Esta solução é apenas no produto TAXONE e apenas para o cliente PROFARMA__

432792

Rogério Ohashi

Inclusão de tratamento na regra de importação para considerar o parâmetro “Usuário DB – Alternativo”, caso no processo de importação o campo de “__*table\_owner\_w*__” for diferente do Owner do Banco de Dados, o sistema deverá consultar o campo DB\_OWNER da tabela PRT\_PAR\_MSAF\. 

MFS1017722/MFS1024894

Lyene Benvenutti e Andrea Rocha

Inclusão da funcionalidade de “geração multiempresa” para a tabela SAFX2064\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No processo de execução  da Importação Batch, o sistema deve realizar a importação  considerando o novo item 05  incluído na lista do campo 175 \-  Código de situação tributária do PIS e no campo 178 do Código de Situação Tributária  Cofins na tabela SAFX08\.

CH56743

__RN01__

# Quando houver uma crítica dos campos “Código Situação Tributária PIS” e “Código Situação Tributária COFINS” da tabela de Itens de Mercadoria \(SAFX08 / X08\_ITENS\_MERC\) sejam corretamente exibidas para os códigos 01, 02, 03, 04, 05, 06, 07, 08, 09 e 99 e não mais 1, 2, 3, 4, 6, 7, 8, 9 e 99, exibindo mensagens de erro caso os códigos sejam diferentes 

CH56743

__RN02__

Na importação de dados para a tabela X42\_CAPA\_TELECOM, preencher o campo ind\_tp\_registro com o valor “1” quando este estiver nulo\.

CH68023

__RN03__

# Geração Multiempresa:

# A importação foi alterada na OS3255 para permitir a geração multiempresa para as seguintes tabelas:

\-SAFX01

\-SAFX02

\-SAFX07

\-SAFX08

\-SAFX09

\-SAFX53

\-SAFX147

\-SAFX148

\-SAFX183

\-SAFX187

\-SAFX2064 \- \[ALTERAÇÃO MFS1017722/MFS1024894\]

Quando na programação da importação, for selecionada a opção multiempresa para estas tabelas, a importação irá considerar todas as empresas e seus respectivos estabelecimentos, aos quais o usuário tenha permissão de acesso\.

#   

__Alteração OS4757__: Nesta OS foram incluídas as seguintes tabelas no tratamento multiempresa:

SAFX03

SAFX48

SAFX114

SAFX125

SAFX300

SAFX49

SAFX115

SAFX130

SAFX301

SAFX50

SAFX116

SAFX138

SAFX05

SAFX51

SAFX117

SAFX155

SAFX500

SAFX110

SAFX118

SAFX158

SAFX501

SAFX112

SAFX119

SAFX159

SAFX44

SAFX113

SAFX120

SAFX701

SAFX702

OS3255

OS4757

MFS1017722/MFS1024894

__RN04__

# Para o Produto TAXONE:

# Quando o cliente for PROFARMA e o parâmetro ‘<a id="_Hlk112162286"></a>IND\_VALID\_IMPORT’ da tabela <a id="_Hlk112162340"></a>PRT\_PAR\_MSAF, estiver marcado com ‘S’, ao selecionar o botão executar, se existir uma importação com os mesmos dados \(para os parâmetros: Empresa, Estabelecimento, Data inicial, Data final e Arquivo\) que está em andamento \(status = ‘E’\), não permitir a execução da nova importação e exibir a mensagem: “Já existe uma importação com os mesmos dados \(Empresa, Estabelecimento, Data Inicial, Data Final e Arquivo\) que ainda não foi finalizada\. Favor aguardar este processamento” 

Se o parâmetro estiver com ‘N’, a validação acima não será realizada\. 

__Atenção: Os clientes terão este parâmetro setado com ‘N’, apenas a PROFARMA estará com ele setado com ‘S’\. Esta definição do parâmetro será feita via sistema \(definido em código\), ou seja, os clientes não terão acesso/permissão para ajustar o parâmetro\.__

MFS\-92054

__RN05__

# Inclusão de tratamento para o parâmetro “Usuário DB – Alternativo”

Na execução do processo de importação __se__ o campo de “__*table\_owner\_w*__” for diferente do Owner do Banco de Dados \(Owner padrão\), o sistema deverá consultar o campo table\_owner da tabela prt\_par\_msaf\. 

__Se__ o campo “*table\_owner\_w*” for igual ao campo “*db\_owner*” \(parâmetro “Usuário DB – Alternativo”\)

   O sistema deverá considerar o Owner alternativo parametrizado na tela de Preferências do módulo de Ferramentas e seguir com o processo de importação\.

 __ Senão __deverá ser desconsiderado no processo de importação\.

  

__Obs\.:__ Tratamento incluído para o cliente Lasa, e __somente para o Mastersaf DW\.__

432792

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

