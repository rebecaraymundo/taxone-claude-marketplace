# MTZ_EFD_Tela_Pre_Geracao_Registro_1400_Convenio_52

> Fonte: MTZ_EFD_Tela_Pre_Geracao_Registro_1400_Convenio_52.docx






THOMSON REUTERS

Tela de Pré-Geração do Registro 1400 – Convênio 52/05
EFD-Escrituração Fiscal Digital


Localização: Menu SPED, módulo EFD-Escrituração Fiscal Digital, menu Pré-Geração à Registro 1400 – Conv. ICMS 52/05


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Pré-Geração\ Registro 1400 – Conv. ICMS 52/05

Título da tela: Registro 1400 – Conv. ICMS 52/05

Regra Geral (procedimento padrão Mastersaf DW):

O sistema deve exibir os estabelecimentos que estejam licenciados e que o usuário possua acesso no PowerLock;
A pré-geração deve ser feita no padrão Framework;
Essa tela será composta pelas seguintes abas:
Parâmetros: o sistema deve exibir os parâmetros de entrada da geração.
Processos: o sistema deve exibir os processos já executados para essa geração.
Log de Processo: o sistema deve exibir o log gerado durante a geração (a regra será composta no documento matriz de geração).

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





| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-15153 | Julyana Perrucini | Criação da pré-geração do Registro 1400 para atender o Convênio ICMS 52/05. |  |
| MFS20218 | Vânia Mattos | Inclusão de mensagem na tela da geração (alerta sobre os códigos de periodicidade  anual); | 23/01/2019 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período (Mês/Ano) | Data | S | S | Formato:  Text Input MM/AAAA  Default:  Desbloqueado | Permite o usuário preencher o mês e o ano a ser apurado o Registro 1400 para compor o arquivo magnético de acordo com o Convênio 52/05.  Tratamento: Caso o usuário não preencha o campo, emitir a mensagem na tela: “Informar Período”.  Alteração MFS20218: Incluída mensagem de alertar sobre a geração dos códigos anuais.   Quando o mês do período informado for = 12 (Dezembro), ao clicar no botão <Executar> será exibida a seguinte mensagem na tela:  Atenção: Para o mês de dezembro também serão gerados os códigos específicos com periodicidade anual, quando for o caso. Para estes códigos é feita a totalização das notas fiscais do ano todo, e por isso o processo pode demandar mais tempo para conclusão. Consultar detalhes no help. Deseja continuar mesmo assim?                             < Sim>     <Não> | MFS-15153 MFS20218 |
| Estabelecimento | Texto | S | S | Formato: Checkbox  Default: Habilitado | Permite o usuário selecionar o estabelecimento no qual necessita entregar o Registro 1400 da EFD-ICMS/IPI de acordo com o Convênio 52/05.  Tratamento: Listar todos os estabelecimentos licenciados; Permitir marcar mais de um estabelecimento; Caso nenhum estabelecimento seja selecionado, emitir a mensagem na tela: “Selecione pelo menos um Estabelecimento.”; Caso o usuário entre com um estabelecimento no Login, entrar como default com o estabelecimento marcado, caso contrário não marcar nenhum estabelecimento.  Incluir botão “Selecionar” para seleção de estabelecimento e o botão “Marcar Todos” caso o usuário queira marcar todos os estabelecimentos. | MFS-15153 |
