# MTZ_SAICS_Parametrização_Ajustes_Cálculo_Alíquota_Média_ICMS

> Fonte: MTZ_SAICS_Parametrização_Ajustes_Cálculo_Alíquota_Média_ICMS.docx






THOMSON REUTERS

Módulo SAICS

Parametrização do Ajuste da Apuração p/ Cálculo da Alíquota Média ICMS


Localização: Módulo Estadual >> SAICS – Sistema de Apuração do ICMS - Custos
Menu:    Parâmetros >> Parametrização do Ajuste da Apuração p/ Cálculo da Alíquota Média ICMS



DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4
























## Regras Gerais


Esta é uma parametrização dos Códigos de Ajustes do Sped Fiscal, presentes nos Lançamentos Complementares da Apuração do ICMS, como forma de identificação dos lançamentos que serão considerados no Cálculo da Alíquota Média ICMS, executado na Geração do Meio Magnético (Menu: Obrigações > Geração Meio Magnético).
.


## Layout da Tela


Tela do tipo formulário simples.








Tabela: SAICS_PAR_CALC_ALIQ
Campos que fazem parte da PK: Estabelecimento, Código do Ajuste Sped Fiscal.


Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MF5619349 | Liliane Videira Assaf | Criação da Tela | 20/03/2024 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


| NOVO | Ao clicar nesta opção os dados da tela serão limpos, e o usuário poderá cadastrar a parametrização para um novo estabelecimento. |
| --- | --- |
| ABRE | Exibe janela de pesquisa dos dados já parametrizados, para que o usuário selecione a parametrização desejada a ser exibida em tela. |
| EXCLUI | Opção para excluir a parametrização de um estabelecimento |
| CONFIRMA | Opção para salvar os dados da parametrização incluída / alterada. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Listbox | Este campo é uma lista dos estabelecimentos da empresa para seleção do usuário.  Caso o estabelecimento seja informado no login do Manager, este campo deve ser apresentado bloqueado.  Caso contrário, apresentar uma lista contendo todos os estabelecimentos da empresa de login. Ao salvar o registro fazer as seguintes validações: 1) Caso o campo “Estabelecimento” não esteja preenchido, então exibir a seguinte mensagem e não salvar registro:    “Campo "Estabelecimento" deve ser preenchido.” |
| Código do Ajuste Sped Fiscal | Alfanumérico | S | S | Pastinha + Código + Descrição | Este campo tem como origem o Cadastro do Código de Ajuste Sped Fiscal – tabela ICT_AJUSTE_ICMS.  A pastinha de seleção dos códigos de ajuste somente pode apresentar os códigos que obedeçam a seguinte regra de formação:  Primeiro e Segundo caracter = UF do Estabelecimento selecionado  Caso seja digitado um código que não atenda a regra acima, exibir a seguinte mensagem:  “Código Ajuste inválido ou não cadastrado”.  Ao salvar o registro fazer as seguintes validações: 1) Caso o campo “Estabelecimento” não esteja preenchido, então exibir a seguinte mensagem e não salvar registro:    “Campo "Código do Ajuste Sped Fiscal" deve ser preenchido.”  Obs: Esse código é criado via tela de manutenção disponível do módulo ICMS (menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Código de Ajuste Sped Fiscal). |
| Replicar para os Estabelecimentos |  |  |  | Checkbox  Default: desmarcado | Opção para permitir que a parametrização seja replicada para outros estabelecimentos no momento de salvar a operação.  A lista dos estabelecimentos para replicação só será habilitada para seleção do usuário, quando esta opção estiver marcada. Caso contrário, a lista permanece desabilitada, e não será possível selecionar nenhum estabelecimento. |
| Estabelecimentos | Alfanumérico | N | N |  | Este campo exibe a lista dos estabelecimentos da empresa para seleção do usuário (exceto o estabelecimento informado no campo “Estabelecimento”). |
| Selecionar todos | Alfanumérico | N | N |  | Opção para marcar / desmarcar todos os estabelecimentos simultaneamente. |
