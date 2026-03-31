# MTZ_Tela_Atribuicao_Natureza_Rendimento

> Fonte: MTZ_Tela_Atribuicao_Natureza_Rendimento.docx



THOMSON REUTERS

REINF
Atribuição da Natureza de Rendimento



DOCUMENTO DE REQUISITO



Sumário

1.	TELA	3
2.	Regras dos Campos	3

## TELA


DW



TAXONE




## Regras dos Campos


Localização da tela: Módulo: SPED>> SPED >> EFD – REINF
Menu: REINF >>Atribuição da Natureza de Rendimento

Título da tela: Atribuição da Natureza de Rendimento




#### Abas que podem ser geradas:




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-97021 | Alessandra Cristina Navatta | Criação do Documento |
| MFS-863016 | Alessandra Cristina Navatta | Permitir a geração Multiempresa. Ajustada a regra do componente Estabelecimento(apenas para produto TAXONE) |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Lista | S | N | Código – Razão Social | Exibe o estabelecimento que foi logado no sistema. | MFS-97021 |
| Período | Data | S | S | MM/AAAA | Só é permito indicar o mês e ano.  Período a partir de janeiro/2022 | MFS-97021 |
| Excluir Natureza de Rendimento Atribuída pelo Sistema | Check-box | N | S | Default: Não selecionado | Permite excluir natureza de rendimento que foi atribuída pelo sistema, se selecionado este parâmetro. | MFS-97021 |
| Multiempresas | CheckBox |  |  | Default: não selecionado | Quando o usuário selecionar esta opção, será exibido no campo Estabelecimento, os estabelecimentos de todas as empresas que o usuário tem acesso. Se o parâmetro estiver desmarcado, apenas os estabelecimentos da empresa logada serão demonstrados. | MFS-863016 |
| Estabelecimentos | Check-box | N | S | cód. Estab + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX    [ALTERAÇÃO MFS-863016] produto TAXONE XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento centralizador) ou  XXX / XXXXX-XXXXXXXXXXXXXXXXX  (cód. empresa + cód. e razão social do estabelecimento descentralizado), quando o campo multiempresa for selecionado   Default: não selecionado | Serão apresentados no componente, todos os estabelecimentos da empresa que está logada. Neste caso, poderá ser selecionado um ou mais estabelecimentos.  [ALTERAÇÃO MFS-863016] Para TAXONE: - Caso o parâmetro “Multiempresas” estiver desmarcado: Na lista será demonstrado os estabelecimentos da empresa que acessou o módulo.      - Caso o parâmetro “Multiempresas” estiver marcado: Na lista será demonstrado o estabelecimento de todas as empresas que o usuário tem acesso:          O usuário deverá escolher obrigatoriamente ao menos um estabelecimento. Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”  Como facilitador, poderá ser utilizada a opção “Marcar todos”. Por default, a opção será desmarcada. | MFS-97021 MFS-863016 |
| Selecionar | Botão |  |  |  | Permite pesquisar/selecionar um estabelecimento específico. | MFS-97021 |
| Marcar Todos | Botão |  |  |  | Permite Marcar todos os estabelecimentos que estão listados na grid de estabelecimentos. Caso todos os estabelecimentos estejam marcados, se selecionar novamente este botão, os estabelecimentos serão desmarcados. | MFS-97021 |
| Executar | Botão |  |  |  | Os campos Estabelecimento e Período são de preenchimento obrigatório, caso não estejam preenchidos exibir a mensagem: “Campo <<nome funcional no campo>> deve ser informado!”  Se o parâmetro ‘Excluir Natureza de Rendimento Atribuída pelo Sistema’ estiver desmarcado:  - Ao executar o processo, o sistema deve recuperar todos os registros da X53 (Arquivo de Controle de Tributos), do estabelecimento e período indicados no processamento, que estão com o campo ‘Natureza de Rendimento’ sem preenchimento e se for encontrado uma parametrização criada na tela “Identificação da Natureza de Rendimento”, localizada em Módulo: SPED>> SPED >> EFD – REINF, Menu: Parâmetros >>, que se enquadre nos critérios definido, atribuir a natureza de rendimento definida na parametrização na tabela de controle de tributo, no respectivo campo. Neste caso, o campo Natureza de Rendimento, da X53, será gravado com a natureza de rendimento indicada pela parametrização em questão.  Este passo, deve ser feito para cada registro da X53, que foi recuperado.  Todos os registros da tabela de Arquivo de Controle de Tributos (X53) que passarem pelo processo de atribuição da natureza de rendimento, terão o campo ‘Natureza de Rendimento’ gravado e ficarão identificados na tabela que foram alterados pelo sistema (este campo não será apresentado em tela). Sugestão: usar o campo ind_gravacao, com a opção 6 - Gerado pelo Sistema  Caso o registro seja alterado pela importação ou digitação, após a atribuição do campo ‘Natureza de Rendimento’ pelo sistema (ind_gravacao = ‘6’), o registro perderá as referencias, pois não temos o controle por campo. Neste cenários, os status passam a ser 2- Atualizado por Importação ou 5.  Incluído por Digitação / Atualizado por Digitação  Se o parâmetro ‘Excluir Natureza de Rendimento Atribuída pelo Sistema’ estiver marcado:  O sistema deve apagar todas as naturezas de rendimento que foram geradas pelo sistema (ind_gravacao = ‘6’), para o período, estabelecimento em questão e ajustar o campo ind_gravação para ‘9 - Atualizado pelo Sistema’   Priorização da Execução das Parametrizações:  Serviço para Atribuição da Natureza de Rendimento; Código de Receita e Pessoa Física/Jurídica  Serão executadas as parametrizações que possuem todos os critérios definidos primeiro (sempre respeitando a ordem alfabética dos conteúdos dos filtros), até chegar nas parametrizações menos específicas (sem todos os filtros estarem definidos). | MFS-97021 |


| Parâmetros | Esta aba apresenta as colunas da tela de geração do processamento, definidas no tópico 2. Regras dos Campos, deste documento. | MFS-97021 |
| --- | --- | --- |
| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-97021 |
| Logs | Esta aba deve demonstrar os logs do processo.   Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração, seguindo o formato abaixo: | MFS-97021 |
