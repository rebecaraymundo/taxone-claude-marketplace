# Tela_Geracao_ECF

> Fonte: Tela_Geracao_ECF.docx






THOMSON REUTERS

Tela de Geração da ECF




DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÂO	3
2.	DOCUMENTOS DE REFERÊNCIAS	3
2.1.	Regras dos Campos	4

## INTRODUÇÂO


Objetivo desta especificação é permitir a geração dos arquivos texto da ECF

## DOCUMENTOS DE REFERÊNCIAS


Regras de Negócio Gerais:
Regras_Gerais_DWECF.docx

Mensagens do Sistema
Mensagens_Sistema_DWECF.xlsx

Geração do bloco 0
MTZ_ECF_Bloco0.doc

Geração do bloco C
MTZ_ECF_BlocoC.doc

Geração do bloco E
MTZ_ECF_BlocoE.doc

Geração do bloco J
MTZ_ECF_BlocoJ.doc

Geração do bloco L
MTZ_ECF_BlocoL.doc

Geração do bloco M
MTZ_ECF_BlocoM.doc

Geração do bloco N
MTZ_ECF_BlocoN.doc


Geração do bloco P
MTZ_ECF_BlocoP.doc

Geração do bloco Q
MTZ_ECF_BlocoQ.doc

Geração do bloco T
MTZ_ECF_BlocoT.doc

Geração do bloco U
MTZ_ECF_BlocoU.doc

Geração do bloco X
MTZ_ECF_BlocoX.doc

Geração do bloco Y
MTZ_ECF_BlocoY.doc

Geração do bloco W
MTZ_ECF_BlocoW.doc

#### Regras dos Campos


Localização da tela: ECF - Escrituração Contábil Fiscal >> Gerações >> ECF


Título da tela: Geração da ECF




(*) Não exibir a descrição na tela.

| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 09/03/2018 | MFS-12684 | Criação da documentação | Alessandra Cristina Navatta |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS | MFS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Executar | Botão | - | - | Default desabilitado- | Botão que permite submeter as escriturações para processamento do arquivo magnético.   Tratamentos:  Validações que impedem a geração do arquivo:  -Se no componente Informações ECF dos Estabelecimentos não tiver registros selecionados, exibir a mensagem DW00057.   -Permitir exercício a partir de 2014. Caso o usuário informe um exercício anterior a 2014, exibir a mensagem DW00027.  - Aplicar RNG000010 – Campo Obrigatório  - A data Inicial deve ser a partir de 01/01/2014. Caso o usuário informe uma data inicial anterior a 01/01/2014, exibir a mensagem DW00028  - Aplicar RNG00053 -Data Inicial x Exercício  - Aplicar RNG00052 - Validação do campo data inicial/data final.   - Se o campo Data Final for menor que o campo Data Inicial, exibir a mensagem DW00212  Para cada escrituração selecionada, verificar: -Se na tela de “Informações ECF”, o campo “Perfil de Geração do Arquivo” está preenchido. Se não existir informação no campo, não gerar o arquivo desta escrituração e exibir a mensagem DW00189.  Caso, o perfil esteja indicado na Informação ECF e a validação acima for satisfatória, para cada escrituração, recuperar os dados de acordo com o período indicado nos campos Data Inicial e Data final.   -Para todas as Informações ECF selecionada, verificar na Informação ECF imediatamente anterior, (considerando a data inicial da tela Informações ECF imediatamente anterior da Informação ECF selecionada, para o mesmo estabelecimento), se possui na última abertura da apuração, o campo situação especial igual a ‘Desenquadramento de Imune/Isenta’, se sim, verificar se o campo ‘Indicador de Início de Período’ está igual a ‘4 – Início de obrigatoriedade da entrega no curso do ano calendário’ (informação cadastrada na tela de Geração da ECF), caso o indicador esteja diferente, exibir a mensagem DW00188 (impedindo a geração do arquivo para a o estabelecimento em questão), se não, o arquivo é processado sem problemas.   Validações que não impedem a geração do arquivo:   -Se não forem encontrados nenhum registro de abertura de apuração, para a escrituração selecionada, exibir a mensagem DW00190 e gerar apenas os registros cadastrais (Bloco 0) e os Blocos que não precisam passar pelo processamento.  -Se o campo Indicador de Início de Período for “0 – Regular (início no primeiro dia do ano)” e for selecionada escriturações que possuam data inicial da primeira abertura recuperada diferente de 01/01/AAAA, exibir a mensagem DW00269.   - Se o conteúdo do campo Indicador de Início de Período selecionado for “1 – Abertura (início de atividades no ano calendário)”, e for selecionadas escriturações com data inicial da apuração recuperada igual a  01/01/AAAA, exibir a mensagem DW00269.    Regras de Geração do Arquivo:  Realizar a geração do arquivo ECF, seguindo as regras de agrupamento contidas nas respectivas especificações considerando para seleção das informações somente os registros correspondentes às aberturas de apuração selecionadas:  MTZ_ECF_Bloco0.doc MTZ_ECF_BlocoC.doc MTZ_ECF_BlocoE.doc 	MTZ_ECF_BlocoJ.doc MTZ_ECF_BlocoK.doc MTZ_ECF_BlocoL.doc MTZ_ECF_BlocoM.doc MTZ_ECF_BlocoN.doc MTZ_ECF_BlocoP.doc MTZ_ECF_BlocoQ.doc MTZ_ECF_BlocoT.doc MTZ_ECF_BlocoW.doc MTZ_ECF_BlocoX.doc MTZ_ECF_BlocoY.doc MTZ_ECF_Bloco9.doc  Nomenclatura dos Registros: Gerar um arquivo para cada escrituração processada. O nome do arquivo deverá ser composto conforme a formatação “ECF” + “-“ + “CNPJ” + “DDMMAAAA (do campo Data Inicial do grid de seleção de empresas e escriturações) ”. Exemplo: ECF-12345678901234-01112014.txt | MFS-12684 | MFS-12684 |
| Exercício | Texto | S | S | AAAA | Permite que o usuário informe o exercício para processamento. | MFS-12684 | MFS-12684 |
| Data Inicial | Data | S | S |  | Permite que o usuário informe a data inicial para seleção dos registros de abertura da apuração. | MFS-12684 | MFS-12684 |
| Data Final | Data | S | S |  | Permite que o usuário informe a data final para seleção dos registros de abertura da apuração. | MFS-12684 | MFS-12684 |
| Indicador de Início de Período | Lista | S | S | Código - Descrição | Permite que o usuário informe o indicador de início de período que será utilizado no campo correspondente do layout da ECF  Conteúdos Válidos:  0 – Regular (início no primeiro dia do ano) 1 – Abertura (início de atividades no ano calendário) 2 – Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação 3 – Resultante de Transformação 4 – Início de obrigatoriedade da entrega no curso do ano calendário | MFS-12684 | MFS-12684 |
| Plano de Contas e Centro de Custos | Radio Button | S | N | Movimentado no Período | Permite que o usuário selecione a opção que as contas e centros de custos serão recuperadas na geração da ECF.  Opções Válidas:  Movimentado no Período Completo  Tratamento: Quando selecionado “Completo”, o sistema deve recuperar e exibir no arquivo todos os cadastros de contas e de centros de custo que estiverem cadastrados na tabela.  Quando selecionado “Movimentado no Período”, o sistema deve recuperar e exibir no arquivo somente os cadastros de contas e de centros de custo que estiverem dentro do período informado na data inicial e data final e que possuem saldos. | MFS-12684 | MFS-12684 |
| Retificadora | Lista | S | S | N – ECF original | Permite que o usuário informe se o arquivo gerado é normal ou retificação.  Tratamentos:  Conteúdos Válidos:  S – ECF retificadora N – ECF original F–ECF original com mudança de forma de tributação (Art. 5o da Instrução Normativa no 166/1999) | MFS-12684 | MFS-12684 |
| Número do Recibo Anterior | Texto | S | N | Default: Desabilitado | Permite que o usuário informe o número do recibo do arquivo da ECF que será retificado  Tratamentos:  Habilitar este campo para edição somente se o campo “RETIFICADORA” for igual a “S – ECF retificadora” ou “F – ECF original com mudança de forma de tributação (Art. 5o da Instrução Normativa no 166/1999) ”. | MFS-12684 | MFS-12684 |
| Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos |
| Selecionar | Botão |  |  |  | Permite que o usuário selecione os registros de Informações ECF para processamento  Tratamentos:  Exibir todos as escriturações de acordo com os filtros que foram preenchidos na tela.    Apresentar os conteúdos, conforme descrito abaixo:  Campos de Pesquisa do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos: Descrição' Botões do Modal 'Selecionar Períodos de Apuração dos Estabelecimentos': Critério, Cancelar, OK e Salvar  - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem DW00053. - Ao selecionar o botão 'Cancelar', nada será feito e o modal será fechado.  - Ao selecionar o botão 'Critério', as escriturações que foram recuperadas poderão ser filtradas.  -Ao confirmar a seleção dos registros, apresentá-los no componente “ Informações ECF dos Estabelecimentos” da tela Principal -Ao selecionar o botão salvar, o sistema salva as informações recuperadas das apurações em formato txt (no diretório local que o usuário informar). | MFS-12684 | MFS-12684 |
| Marcar Todos | Check-box |  |  | Desmarcado | Permite ao usuário selecionar ou desmarcar todos os registros da grid Período de Apuração dos Estabelecimentos. | MFS-12684 | MFS-12684 |
| Escriturações (*) | Texto | S | N | Código Estab - CGC - Exercício -  Data Inicial da Escrituração  (076 - XXXXXXXXXXXXXX -  01/03/2017) | Permite que o usuário visualize e selecione as escriturações que serão processadas. | MFS-12684 | MFS-12684 |
