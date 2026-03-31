# MTZ-Tela_de_Perfil

> Fonte: MTZ-Tela_de_Perfil.docx


Tela de Cadastro do Perfil – ECD



Módulo: SPED >> ECD – Escrituração Contábil Digital
Menu: Parâmetros >> Perfil





### REGRAS DE NEGÓCIO




| DR | Nome | Descrição |
| --- | --- | --- |
| OS3835-C1 | ECD – Tela de Perfil de Geração do Meio Magnético. | Este documento tem por objetivo especificar as alterações para que o mastersaf possa contemplar o layout da ECD 2013. |
| OS4123 | ECD – Tela de Perfil de Geração do Meio Magnético. | Habilitar para geração o Registro I020 – Campos Adicionais. |
| OS4745 | ECD – Tela de Perfil de Geração do Meio Magnético. | Criação do Tipo de Livro “S – Escrituração SCP Mantida pelo Sócio Ostensivo” e inclusão dos registros “0035”, “I053” e “J935”. |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN01 | Campo Tipo de Livro  Campo do tipo lista com as opções:  G - Livro Diário (Completa sem Escrituração Auxiliar) R - Livro Diário com Escrituração Resumida (com Escrituração Auxiliar) A - Livro Diário Auxiliar ao Diário com Escrituração Resumida B - Livro Balancetes Diários e Balanços (Matriz) Z - Razão Auxiliar (Livro Contábil conforme Leiaute definido nos Registros I500 e I555) S - Escrituração SCP Mantida pelo Sócio Ostensivo | OS3835-C1 OS4745 |
| RN02 | Campo Perfil  Campo do tipo texto, com a possibilidade de indicação do código e descrição do Perfil. | OS3835-C1 |
| RN03 | Quadro Definição dos Blocos  Serão exibidas as opções:  0 Abertura, Identificação e Referências I Lançamentos Contábeis J Demonstrações Contábeis 9 Controle e Encerramento do Arquivo Digital | OS3835-C1 |
| RN04 | Quadro Definição dos Registros  No quadro de definição dos registros serão demonstrados os registros conforme Tipo de Livro e Bloco de Registros indicado pelo usuário.   Considerar as seguintes regras para seleção dos registros:  Os registros Indicados como "O" para o Tipo de Livro indicado pelo usuário serão demonstrados já selecionados para geração e não será possível remover a sua seleção.  Os registros Indicados como "N" para o Tipo de Livro indicado pelo usuário não serão demonstrados para seleção.  Os registros Indicados como "F" para o Tipo de Livro indicado pelo usuário serão demonstrados não selecionados para geração e será possível a sua seleção por parte do usuário. | OS3835-C1 OS4123 OS4745 |
