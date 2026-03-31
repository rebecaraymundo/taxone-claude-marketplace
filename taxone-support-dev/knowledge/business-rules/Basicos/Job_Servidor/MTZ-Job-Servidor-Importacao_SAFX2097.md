# MTZ-Job-Servidor-Importacao_SAFX2097

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2097.docx
- **Modificado:** 2025-04-25
- **Tamanho:** 65 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2097

Tabela de Municípios

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS38942

Andréa Rocha

Alteração da regra do campo 53 \- Código Formato Específico\.

MFS\-769159

Alessandra Cristina Navatta

Criação do campo 59 – Feriado

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX2097 🡪 vide manual de layout

Campo que compõe a chave da tabela:

__   Código do Município ISS__

A manutenção desta tabela é feita no Módulo Data Warehouse, menu Manutenção 🡪 Cadastros 🡪 Municípios ISS 🡪 Manutenção

Tabela de Destino:

A SAFX2097 alimenta a tabela definitiva x2097\_munic\_iss

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campo chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS38942

__RN53__

__Campo 53 \-  Código Formato Específico__

Campo de preenchimento não obrigatório\.

Quando o código estiver preenchido com zeros, o conteúdo não deve ser considerado, deve\-se tratar como se o campo estivesse nulo\.  Este tratamento se faz necessário porque o campo foi criado como numérico na tabela quando deveria ter sido criado como alfanumérico\.

Crítica da existência da código na tabela de Código de Layout do Livro de ISS \(TFIX37\):

Quando o código estiver preenchido, deve\-se verificar se está cadastrado na tabela de Código de Layout do Livro de ISS\. Caso o código não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

*“Codigo de Formato Especifico nao esta relacionado a nenhum registro da tabela de Formato de livro ISSQN \- TFIX37”*

MFS38942

__RN59__

__Campo 59 \-  Feriado__

Campo de preenchimento não obrigatório\.

Informar para o município, se há antecipação ou postergação de pagamento, em caso do dia de vencimento ser feriado\. 

Lista de Valores Válidos:

@ \-Indefinido;

A\-Antecipa;

P\-Posterga

Formato: A

Tamanho: 001

Validação:

Se não for informado uma opção válida, exibir a mensagem de erro 93774: “O campo Feriado, deve ser preenchido com nulo, <@>, <A> ou <P>\.”

MFS\-769159

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

