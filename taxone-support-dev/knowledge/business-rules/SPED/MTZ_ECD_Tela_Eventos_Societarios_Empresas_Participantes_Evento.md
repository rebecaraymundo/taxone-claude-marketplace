# MTZ_ECD_Tela_Eventos_Societarios_Empresas_Participantes_Evento

> Fonte: MTZ_ECD_Tela_Eventos_Societarios_Empresas_Participantes_Evento.docx






THOMSON REUTERS

Eventos Societários / Empresas Participantes do Evento
Bloco K – Sped Contábil



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
Menu: Manutenção >> Bloco K  >> Eventos Societários/Empresas Participantes do Evento

Título da tela: Eventos Societários/Empresas Participantes do Evento












Sugestão de Tela




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-9667 | Tela Eventos Societários/Empresas Participantes do Evento | Criação da Tela “Eventos Societários/Empresas Participantes do Evento” |
| MFS30647 | Andréa Rocha | Alteração da regra do campo data do evento societário |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento Controlador | Text Box | S | S | Default: Habilitado | Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário. Quando o estabelecimento for informado no login do sistema, o campo mostrará fixo o estabelecimento do login, e o usuário não poderá alterá-lo.   Demonstrar na frente do código e nome do estabelecimento se o mesmo é centralizado ou descentralizado. | MFS9667 |
| Data Inicial (Período da Consolidação) | Text Box | S | S | Default: Desabilitado | Neste campo será demonstrado o período inicial da consolidação de acordo com o Código/Nome da Empresa Participante selecionado. | MFS9667 |
| Data Final (Período da Consolidação) | Text Box | S | S | Default: Desabilitado | Neste campo será demonstrado o período final da consolidação de acordo com o Código/Nome da Empresa Participante selecionado. | MFS9667 |
| Código/Nome da Empresa Participante | Text Box | S | S | Default: Habilitado | Este campo trabalha com janela de seleção da tabela SAFX240 – Relação das Empresas Consolidadas. Filtrando para que sejam demostrados apenas as informações cujo campo Evento Ocorrido no Período contenha o valor = S - Sim da SAFX240 e que correspondam ao Estabelecimento Controlador selecionado. De acordo com o código selecionado na SAFX240 será demostrados também os respectivos campos Data Inicial e Final do Período de Consolidação.  Caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Participante é obrigatório - deve ser preenchido”. | MFS9667 |
| Evento Ocorrido no Período | Text Box | S | S | Default: Habilitado | Campo para informar o evento societário que ocorreu no período.  Opções: 1 – Aquisição  2 – Alienação  3 – Fusão  4 – Cisão Parcial  5 – Cisão Total  6 – Incorporação  7 – Extinção  8 – Constituição   Caso não preenchido exibir a seguinte mensagem: “O Campo Evento Societário ocorrido no período é obrigatório - deve ser preenchido”.   Tratamento:  Caso o usuário selecionar as opções: 7 – Extinção OU 8 – Constituição   Os campos Código/Nome da Empresa Envolvida, Condição da Empresa relacionada à Operação e % da Empresa Envolvida na Operação serão desabilitados. Esses campos serão habilitados apenas quando as opções escolhidas forem do 1 à 6. | MFS9667 |
| Data do Evento | Text Box | S | S | Default: Habilitado | Neste campo o usuário informará à data que ocorreu o evento societário.  [MFS30647] Verificar se a data informada neste campo corresponde ao período informado nos campos Data Inicial do período consolidado e Data Final do período. Ou que a data seja do ano anterior, do mesmo ano ou do ano posterior do período consolidado.  Caso esteja fora desses períodos, retornar mensagem de erro: “A Data do Evento Societário não pode ser diferente da data do período consolidado, ou do ano anterior ou do ano posterior deste período”.   Caso não preenchido exibir a seguinte mensagem: “O Campo Data do Evento é obrigatória - deve ser preenchida”. | MFS9667 MFS30647 |
| Código/Nome da Empresa Envolvida | Text Box | S | S |  | Este campo trabalha com janela de seleção da tabela SAFX240 – Relação das Empresas Consolidadas. Filtrando apenas as empresas que pertençam ao mesmo período de consolidação selecionado, com exceção do código de empresa informado no campo Código da Empresa Participante.   Se o campo “Evento Societário ocorrido no período” estiver preenchido com “1” (Aquisição), “2” (Alienação), “3” (Fusão), “4” (Cisão Parcial), “5” (Cisão Total) ou “6” (Incorporação), esse campo é de preenchimento obrigatório e se não estiver preenchido exibir a seguinte mensagem: “O Campo Código da Empresa envolvida na operação é obrigatório quando o campo “Evento Societário ocorrido no período” estiver preenchido com “1” (Aquisição), “2” (Alienação), “3” (Fusão), “4” (Cisão Parcial), “5” (Cisão Total) ou “6” (Incorporação) - deve ser preenchido”.   Caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Envolvida é obrigatório - deve ser preenchido”. | MFS9667 |
| Condição da Empresa relacionada à Operação | Text Box | S | S |  | Opções: 1 – Sucessora;  2 – Adquirente;  3 – Alienante.  Esse campo será preenchido de acordo com a informação selecionada no campo Evento Ocorrido no Período, conforme:  Se a opção selecionada for igual à “3” (Fusão), “4” (Cisão Parcial), “5” (Cisão Total) ou “6” (Incorporação) nesse campo será preenchido a opção 1 – Sucessora.  Se a opção selecionada for igual à “1” (Aquisição) nesse campo será preenchido a opção 2 – Adquirente.  Se a opção selecionada for igual à “2” (Alienação) nesse campo será preenchido a opção 3 – Alienante.  Sem possibilidade de alteração. | MFS9667 |
| % da Empresa Envolvida na Operação | Text Box | S | S |  | Neste campo o usuário informará percentual da empresa envolvida na operação.  Se o campo “Evento Societário ocorrido no período” estiver preenchido com “1” (Aquisição), “2” (Alienação), “3” (Fusão), “4” (Cisão Parcial), “5” (Cisão Total) ou “6” (Incorporação), esse campo é de preenchimento obrigatório e se não estiver preenchido exibir a seguinte mensagem: “O Campo Percentual da empresa participante envolvido é obrigatório quando o campo “Evento Societário ocorrido no período” estiver preenchido com “1”, “2”, “3”, “4”, “5” ou “6” - deve ser preenchido”. | MFS9667 |
