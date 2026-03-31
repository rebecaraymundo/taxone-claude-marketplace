# MTZ_EFD_Tela_Pre_Geracao_Registro_E115

> Fonte: MTZ_EFD_Tela_Pre_Geracao_Registro_E115.docx






THOMSON REUTERS

Tela de Pré-Geração do Registro E115
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Pré-Geração\ Registro E115\ Geral

Título da tela: Geração para Informações Adicionais da Apuração – Valores Declaratórios

Regra Geral Botões (procedimento padrão Mastersaf DW):

Abre – Será demonstrado um ícone para opção de abrir novamente a tela de geração.

Gera PDF – Será habilitado nas abas Log e Pré-Geração, abre tela para inserção do Diretório e o campo Nome do Arquivo para digitação do nome do arquivo a ser salvo (é necessária a instalação do Acrobat Writer, caso contrário será gerado um aviso na tela “Não foi possível salvar em PDF, Verifique se o Acrobat Writer está disponível!”).

Imprime – Será habilitado nas abas Log e Pré-Geração, abre tela para inserção de parâmetros para impressão, como nº de cópias, intervalo de páginas (todo relatório, páginas, etc.).

Pág - – Permite avançar para página inicial.

Pág -- – Permite avançar página a página sentido a página inicial.

Pág + – Permite avançar para página final.

Pág ++ – Permite avançar página a página sentido a página final.

FECHA – Permite sair da tela.



## Sugestão de Layout






| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-13074 | Julyana Perrucini | Essa MFS tem como objetivo criar a rotina de geração do Registro E115 para alimentar a tabela de Valores Declaratórios. |
| MFS-24916 | Liliane Assaf | Reestruturação de Menu (Específico RS) |
| MFS-67999 | Rogério Ohashi | Inclusão do Parâmetro “Geração p/Inscrição Estadual Única” na tela de Pré-Geração do Registro E115 no menu “Geral”. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Texto | S | S | Formato:  DD/MM/AAAA  Default:  Desbloqueado | Permite o usuário preencher a data inicial para o processamento dos dados a serem gerados na manutenção dos valores declaratórios.  Tratamento: Caso o usuário não preencha o campo, emitir a mensagem na tela: “Informar Data Inicial”. | MFS-13074 |
| Data Final | Texto | S | S | Formato:  DD/MM/AAAA  Default:  Desbloqueado | Permite o usuário preencher a data final para o processamento dos dados a serem gerados na manutenção dos valores declaratórios.  Tratamento: Caso o usuário não preencha o campo, emitir a mensagem na tela: “Informar Data Final”; Fazer a verificação padrão quando este campo for preenchido com uma data inferior a data inicial e emitir a mensagem. Permitir preenchimento mensal. | MFS-13074 |
| Geração p/Inscrição Estadual Única | Texto | N | S | Formato: Radio Button Group  Default: Habilitado Desmarcado | Este campo apresenta duas opções:   - Sim - Não  As opções são alternativas.  A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica. | MFS-67999 |
| Estabelecimentos | Texto | S | S | Formato: Checkbox  Default: Habilitado | Permite o usuário selecionar o estabelecimento a ser entregue a obrigação acessória.  Tratamento: Listar apenas os estabelecimentos com UF igual a RS (Rio Grande do Sul); Permitir marcar mais de um estabelecimento; Caso nenhum estabelecimento seja selecionado, emitir a mensagem na tela: “Selecione pelo menos um Estabelecimento.”; Caso o usuário entre com um estabelecimento no Login, entrar como default com o estabelecimento marcado, caso contrário não marcar nenhum estabelecimento. | MFS-13074 |
