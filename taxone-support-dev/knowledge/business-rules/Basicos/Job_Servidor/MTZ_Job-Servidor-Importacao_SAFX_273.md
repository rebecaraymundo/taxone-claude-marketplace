# MTZ_Job-Servidor-Importacao_SAFX_273

- **Fonte:** MTZ_Job-Servidor-Importacao_SAFX_273.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX273  

Cadastro de Inscrições Estaduais

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-26173

Aline Melo

Criação da SAFX273 para a tela de Cadastro de Inscrições Estaduais

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

Estrutura da tabela SAFX273 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__Código da Empresa \+ Código do Estabelecimento \+ UF __

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

MFS\-26173

RN01

__Campo 01 – Código da Empresa __

Campo de preenchimento __*obrigatório*__\. Caso o campo não esteja preenchido, deve ser demonstrada a seguinte mensagem:

__*“Codigo de Empresa nao esta preenchido\.”*__

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)\.*

MFS\-26173

RN02

__Campo 02 – Código do Estabelecimento __

Campo de preenchimento __*obrigatório*__\. Caso o campo não esteja preenchido, deve ser demonstrada a seguinte mensagem:

__*“Codigo de Estabelecimento deve ser preenchido\.”   *__

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-26173

RN03

__Campo 03 – UF __

Campo de preenchimento __*obrigatório*__\.

Caso o campo não esteja preenchido, deve ser demonstrada a seguinte mensagem:

__*“A UF deve ser preenchida\.”*__

MFS\-26173

RN04

__Campo 04 – Inscrição Estadual__

Campo de preenchimento __*obrigatório*__\.

Caso o campo não esteja preenchido, deve ser demonstrada a seguinte mensagem:

__“*A Inscrição Estadual deve ser preenchida*\.”__

MFS\-26173

RN05

__Campo 05 – NIRE__

Campo de preenchimento __*não obrigatório\.*__

MFS\-26173

RN06

__Campo 06 – Nº Junta Comercial__

Campo de preenchimento __*não obrigatório\.*__

MFS\-26173

RN07

__Campo 07 – Data Despacho__

Campo de preenchimento __*não obrigatório*__\. Se o campo estiver preenchido e formato estiver diferente de dd/mm/aaaa, deve ser demonstrada a seguinte mensagem:

__*“O campo Data de Despacho com formato inválido\.“      *__

MFS\-26173

RN08

__Campo 08 – Situação__

Campo de preenchimento __não obrigatório__\. 

Situação da Inscrição:

1 – Normal

2 – Suspensa

Se o campo vier com preenchimento diferente de @, 1 ou 2 , deve ser demonstrada a seguinte mensagem: 

__*“O Tipo da Situacao deve ser preenchido com <1> ou  <2>\.”*__

No caso de não preenchimento ou @ o default = ‘1’\.

MFS\-26173

RN09

__Campo 09 – Inscrição Estadual Especial \(ICMS\-ST\)__

Campo de preenchimento __obrigatório__, somente para UF = ‘PR’\.

Se o campo UF <> ‘PR’ e campo Inscrição Estadual Especial \(ICMS\-ST\) estiver preenchido

OU

Campo UF = ‘PR’ e e campo Inscrição Estadual Especial \(ICMS\-ST\) não estiver preenchido, deve ser demonstrada a seguinte mensagem: 

__*“A Inscrição Estadual especial – GIA\-ICMS\-ST deve ser informada apenas quando o codigo do estado for = 'PR'\.”    *__

MFS\-26173

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

