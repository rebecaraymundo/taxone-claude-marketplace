# MTZ_ECD_Geracao_Por_Centro_de_Custo

> Fonte: MTZ_ECD_Geracao_Por_Centro_de_Custo.docx






THOMSON REUTERS

ECD – Escrituração Contábil Digital / Geração de Saldos por Centro de Custo


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3


## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Escrituração Contábil Digital
Menu: Geração >> Saldos por centro de custo
Título da tela: 	Geração de saldos por centro de custo

Obs.: Devido necessidade de geração de ECD de Situação Especial, a tela foi alterada, sendo incluído os Campo de Data Inicial e Data Final, que permitirá ao usuário definir as datas dos Campos de Saldo por Centro de Custo Inicial e Saldo final, conforme necessidade do cliente.











Sugestão de Tela:


Especificação:

Quando o usuário clicar no botão executar, o processo deverá:
- Consultar o saldo anterior por centro de custo conforme regra, RN1;
- Consultar os lançamentos contábeis do período selecionado agrupando por conta, centro de custo e agrupando os valores de lançamento conforme regra, RN2;
- Calcular o saldo atual por centro de custo com base no saldo anterior e a soma dos lançamentos conforme regra, RN3;
- Apresentar no log a quantidade de registros que serão inseridos ou atualizados regra, RN4;
- Gerar um relatório apresentando as informações do registro que será inserido/alterado e a respectiva operação regra, RN5;
- Se a opção apenas simular estiver desmarcada, o processo deverá realizar a gravação de saldos por centro de custo, conforme regra, RN6.

| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-46979 | ECD – Escrituração Contábil Digital/Geração de saldos por centro de custo | Criação da funcionalidade da geração de saldos por centro de custos a partir dos lançamentos contábeis |
| MFS890185 | Rogério Ohashi | Este documento tem por objetivo de alterar o campo de Período, que agora possibilita o usuário inserir as informações dos campos de Data Inicial e Data Final do da tabela x80, caso o parâmetro de Situação Especial estiver marcado. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Empresa | Combo Box | S | S | Default: Código da empresa informada no login | Este campo exibe a lista de empresas para seleção do usuário.  Demonstrar na frente o código e nome de empresa. Deverão ser demonstradas apenas as empresas que o usuário tem acesso. | MFS46979 |
| Data Inicial | Data | S | S | Formato: DD/MM/AAAA | Informar o período para a geração/consulta dos saldos por centro de custo.  O sistema deve apresentar o dia/mês/ano da data do campo de Saldo Inicial. | MFS46979 MFS890185 |
| Data Final | Data | S | S | Formato: DD/MM/AAAA | O sistema deve apresentar o dia/mês/ano da data do campo de Saldo Final. | MFS890185 |
| Situação Especial | Checkbox | N | S | Default: Desmarcado | Caso a entrega se referir a uma Entrega de Situação Especial, a geração respeitará a data inicial e data final conforme preenchido na tela | MFS890185 |
| Apenas simulação/Conferência | Check Box | S | S | Default: Marcado | Neste campo o usuário indicara se é somente simulação ou geração real dos dados. | MFS46979 |
| Estabelecimento | Multi Select | S | S | Default: Habilitado | Irá listar todos os estabelecimentos da empresa selecionada. | MFS46979 |
