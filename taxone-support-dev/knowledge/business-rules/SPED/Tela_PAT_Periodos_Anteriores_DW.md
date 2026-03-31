# Tela_PAT_Periodos_Anteriores_DW

> Fonte: Tela_PAT_Periodos_Anteriores_DW.docx








THOMSON REUTERS

PAT – Períodos Anteriores ao ONESOURCE
ECF - Escrituração Contábil Fiscal (DW)







DOCUMENTO DE REQUISITO











Sumário

1.	INTRODUÇÂO	3
2.	DOCUMENTOS DE REFERÊNCIAS	3
3.	TELAS	3
3.1.	Pesquisa de Registros	3
3.2.	Regras dos Campos da Tela Principal	5




## INTRODUÇÂO


O objetivo desta especificação é criar a tela de PAT – Períodos Anteriores ao DW possibilitando a entrada manual dos valores (sobras a serem utilizadas para abater o valor do IRPJ) do PAT controlados em sistemas anteriores ao ONESOURCE DW.

## DOCUMENTOS DE REFERÊNCIAS


Mensagens_Sistema_DWECF.xlsx

Regras_Gerais_DWECF.docx

Tela_Informacoes_ECF.doc

Tela_Programa_de_Alimentação_do_Trabalhador.doc

## TELAS


### Pesquisa de Registros


Localização da tela:
ECF - Escrituração Contábil Fiscal >> Manutenção >>PAT – Períodos Anteriores ao DW

Título da tela: PAT – Períodos Anteriores ao DW

Condições Gerais:
Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de as escriturações (Informações ECF) cadastradas no sistema que não possuem outras escriturações com datas anteriores.








Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.






### Regras dos Campos da Tela Principal


Localização da tela:
ECF - Escrituração Contábil Fiscal >> Manutenção>> PAT -  Períodos Anteriores ao DW
Título da tela: PAT -  Períodos Anteriores ao DW

Condições Gerais: Quando o usuário acessar a tela de consulta, apresentar todos os registros da tela Informações ECF.
Desabilitar os botões “Novo”, “Excluir” e “Copiar” na toolbar.
Botão Editar: Habilitar quando o status da abertura da apuração for “Em Aberto”, “Reapurar” ou não houver dados na tela de Abertura da Apuração (status da primeira abertura).







| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 05/06/2018 | MFS-18710 | Criação do documento | Alessandra Cristina Navatta |


| Campo | Tipo | Regra |
| --- | --- | --- |
| Estabelecimento | LOV (Tipo - Código – Descrição) | Permite que o usuário busque o registro pelo Código do Estabelecimento. |
| Exercício | Texto AAAA | O usuário poderá informar o exercício. |
| Data Inicial | Data DD/MM/AAAA | O usuário poderá informar a data inicial da Informação ECF. |
| Versão | Lista (Código -Descrição) | Aplicar a RNG00004-Versão de Layout |
| Forma de Tributação | Lista (Código -Descrição) | Exibe as opções abaixo:  -Lucro Real, Lucro Presumido, Lucro Arbitrado -Imune de IRPJ  -Isento do IRPJ |
| Apuração | Lista (Código -Descrição) | Exibe as opções abaixo:  - Anual - Trimestral |


| Campo | Tipo | Tipo | Obrig | Ed | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Confirma | Botão | Botão |  |  |  |  | Aplicar a RNG00012 – Salvar | MFS-18710 |
| DADOS GERAIS | DADOS GERAIS |  |  |  |  |  |  |  |
| Estabelecimento | Texto | Texto | S | N | N | Tipo - Código - Descrição | Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF. | MFS-18710 |
| Exercício | Texto | Texto | S | N | N | AAAA | Permite que o usuário visualize o ano correspondente ao registro selecionado na tabela de Informações ECF. | MFS-18710 |
| Data Inicial | Texto | Texto | S | N | N | DD/MM/AAAA | Permite que o usuário visualize a data inicial, referente ao registro selecionado na tabela das Informações ECF. | MFS-18710 |
| Versão | Texto | Texto | S | N | N | Código - Descrição | Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro, referente ao registro selecionado na tabela de Informações ECF. | MFS-18710 |
| Forma de Tributação | Texto | Texto | S | N | N | Descrição | Permite que o usuário visualize a forma de tributação, referente ao registro selecionado na tabela das Informações ECF. | MFS-18710 |
| Apuração | Texto | Texto | S | N | N | Descrição | Permite que o usuário visualize a apuração, referente ao registro selecionado na tabela das Informações ECF. | MFS-18710 |
| Data Final do Último Período da Escrituração | Texto | Texto | S | N | N | DD/MM/AAAA | Permite que o usuário visualize a data final do último período da escrituração | MFS-18710 |
| PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW | PAT – PERÍODOS ANTERIORES AO DW |
| Ano(*) | Texto | Texto | S | N | N | AAAA | Tratamento: Exibir automaticamente os 2 anos imediatamente anterior ao da escrituração selecionada (considerando o ano da Data Inicial da Informação ECF).    O label do campo será dinâmico. Deve ser exibido de acordo com a informação ECF recuperada.  AAAA será os dois anos imediatamente anterior ao ano da Informação ECF recuperada. Exemplo: recuperada a informação ECF de 2014, os campos exibidos serão Ano 2012 e Ano 2013. | MFS-18710 |
| Valor | Texto | Texto | S | S | S | 0,00 | Tratamentos:  Será habilitado para preenchimento com a ação no botão editar.  O valor total exibido na tela não será exibido na conta da parte B corresponde ao PAT. Pelo fato da tela Lançamento da Parte B (M410) possuir modo edição, se necessário, o valor da parte B poderá ser ajustado manualmente.  O valor informado nesta tela será utilizado no cálculo do PAT . Quando o valor tiver o prazo expirado para utilização, ou seja, o período de dois anos-calendários for excedido, o valor será desconsiderado. Neste cenário, não será gerado lançamento da Parte B realizando a baixa do valor utilizado. | MFS-18710 |
