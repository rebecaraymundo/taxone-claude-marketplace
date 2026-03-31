# MTZ_EFD_Tela_Pre_Geracao_Registro_B440

> Fonte: MTZ_EFD_Tela_Pre_Geracao_Registro_B440.docx






THOMSON REUTERS

Pré-Geração da Totalização dos Valores Retidos
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos para Tela de Geração	3
2.	Sugestão de Layout da Tela de Geração	6

## Regras dos Campos para Tela de Geração


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Pré-Geração\ Registro B440\ Geração

Título da tela: Pré Geração – Registro B440

Regra Geral (procedimento padrão Mastersaf DW):

O sistema deve exibir os estabelecimentos que estejam licenciados e que o usuário possua acesso no PowerLock;
A pré-geração deve ser feita no padrão Framework;
Essa tela será composta pelas seguintes abas:
Parâmetros: o sistema deve exibir os parâmetros de entrada da geração.
Processos: o sistema deve exibir os processos já executados para essa geração.
Log de Processo: o sistema deve exibir o log gerado durante a geração (a regra será composta no documento matriz de geração).
Relatório: o sistema deve exibir o relatório demonstrando as informações geradas (a regra será composta no documento matriz de geração).

Regra Geral Botões (procedimento padrão Mastersaf DW):

Imprime – Será habilitado nas abas Log e Pré-Geração, abre tela para inserção de parâmetros para impressão, como nº de cópias, intervalo de páginas (todo relatório, páginas, etc.).

Pág - – Permite avançar para página inicial.

Pág -- – Permite avançar página a página sentido a página inicial.

Pág + – Permite avançar para página final.

Pág ++ – Permite avançar página a página sentido a página final.

FECHA – Permite sair da tela.



## Sugestão de Layout da Tela de Geração








| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20990 | Julyana Perrucini | Essa MFS tem como objetivo atender o Ato COTEPE Nº 44/2018, em que será criada uma rotina para gerar a totalização dos valores do Registro B440, e após reaproveitada para geração do relatório de conferência e arquivo magnético. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S | Formato:  DD/MM/AAAA  Default: Não informado  Desbloqueado | Permite o usuário preencher o período inicial para apurar a totalização do Registro B440.  Tratamento: Caso o usuário não preencha o campo, emitir a mensagem na tela: “Informar Data inicial”. | MFS-20990 |
| Data Final | Data | S | S | Formato:  DD/MM/AAAA  Default:  Não informado  Desbloqueado | Permite o usuário preencher o período final para apurar a totalização do Registro B440.  Tratamento: Caso o usuário não preencha o campo, emitir a mensagem na tela: “Informar Data Final”. | MFS-20990 |
| Geração p/Inscrição Estadual Única | Texto | N | S | Formato: Radio Button Group  Default: Habilitado Desmarcado | Este campo apresenta duas opções:   - Sim - Não  As opções são alternativas.  A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica. | MFS-20990 |
| Estabelecimento | Texto | S | S | Formato: Checkbox  Default: Habilitado Desmarcado | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  A exibição dos estabelecimentos depende da opção informada no campo “Geração p/Inscrição Estadual Única”, da seguinte forma:  Se = “Sim”  Neste caso, serão exibidos apenas os estabelecimentos centralizadores, conforme a parametrização da Inscrição Estadual Única no módulo de Controle das Obrigações Estaduais;   Se = “Não”  Neste caso serão exibidos todos os estabelecimentos da empresa;  Sempre que a opção do campo “Geração p/Inscrição Estadual Única” for alterada, esta lista será refeita dinamicamente, considerando a nova opção.  Incluir botão “Selecionar” para seleção de estabelecimento e o botão “Marcar Todos” caso o usuário queira marcar todos os estabelecimentos. | MFS-20990 |
