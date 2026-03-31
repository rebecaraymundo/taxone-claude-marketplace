# MTZ-PowerLock-Relatorio_de_Log_de_Acesso-Powerlock

- **Fonte:** MTZ-PowerLock-Relatorio_de_Log_de_Acesso-Powerlock.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

# Segurança – Relatório de Log de Acesso \- PowerLock

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3893

DW \- BASICOS \- SEGURANÇA \- Tratamento para controle de acessos e armazenamento dos logs 

O objetivo da OS é criar o relatório de log de acesso para o usuário PowerLock\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Regra p/ tela de critério de seleção

A tela deve conter os campos Período e Acesso\. E os botões Ok e Cancel\.

Quando o botão Ok for acionado, o sistema deve gerar o relatório de acordo com os critérios escolhidos anteriormente\.

Quando o botão Cancel for acionado, o sistema deve fechar a tela de critério de seleção\.

OS3893

__RN01__

Regra geral do relatório

Recuperar as informações gravadas na tabela PL\_AUD com as seguintes características:

\- Data Início e Data Fim dentro do período informado na tela de critério de seleção

\- __Acesso de acordo com o escolhido na tela de critério de seleção\.__

  \- Quando selecionada a opção CONFIRMADO, deverão ser recuperadas as informações que contiverem o status “S” no campo ACESSO\_OK da tabela PL\_AUD\.

  \- Quando selecionada a opção NEGADO, deverão ser recuperadas as informações que contiverem o status “N” no campo ACESSO\_OK da tabela PL\_AUD\.

  \- Quando selecionada a opção TODOS, ambas as condições \(tanto “S” quanto “N”\) deverão ser consideradas na geração do relatório\.

OS3893

__RN02__

Regra p/ campo Emissão \(Cabeçalho\)

Preencher com o dia e hora em que o relatório foi gerado\. Utilizar SYSDATE\. Formato: DD/MM/AAAA HH:MM:SS\.

OS3893

__RN03__

Regra p/ campo Período \(Cabeçalho\)

Preencher com o período informado na tela de critério de seleção\. Formato: DD/MM/AAAA\.

O campo deve conter um textbox \+ “a” \+ textox\. Mascara de data para o textbox: DD/MM/AAAA\.

OS3893

__RN04__

Regra p/ campo Acesso \(Cabeçalho\)

Preencher com o Acesso informado na tela de critério de seleção, podendo ser: Confirmado, Negado ou Todos\.

Por default, deve\-se manter a opção Todos marcada\.

OS3893

__RN05__

Regra p/ campo Módulo \(Cabeçalho\)

Preencher com “PowerLock”\.

OS3893

__RN06__

Regra p/ campo Usuário \(Cabeçalho\)

Preencher com o campo “ADM\_NAME” da tabela PL\_ADMIN, de acordo com o usuário que realizou o login no módulo Power Lock

OS3893

__RN07__

Regra p/ campo Data Inicio

Preencher com o campo AUD\_START\_TIME da tabela PL\_AUD\.

OS3893

__RN08__

Regra p/ campo Data Fim

O Preencher com o campo AUD\_END\_TIME da tabela PL\_AUD\.

OS3893

__RN09__

Regra p/ campo Acesso

Preencher com o campo ACESSO\_OK da tabela PL\_AUD\. 

Se o campo estiver preenchido com “S”, o relatório deve exibir “SIM”\.

Se o campo estiver preenchido com “N”, o relatório deve exibir “NÃO”\.

OS3893

__RN10__

Regra p/ campo Login do Windows

Preencher com o campo USUARIO\_WINDOWS da tabela PL\_AUD\.

OS3893

__RN11__

Regra p/ campo Máquina

Preencher com o campo NOME\_MAQUINA da tabela PL\_AUD\.

OS3893

__RN12__

As informações demonstrada no relatório “Access Log Report – PowerLock” devem demonstrar as informações de acesso do usuário admin ao módulo do Powerlock\. A informação apresentada deve refletir as tentativas e acesso ao Powerlock independente do acesso ao DW\.

Estas informações devem ser armazenadas por, no mínimo, três meses\.

OS4079

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

