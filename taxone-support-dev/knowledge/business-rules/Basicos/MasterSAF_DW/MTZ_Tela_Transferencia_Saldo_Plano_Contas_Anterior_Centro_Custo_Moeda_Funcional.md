# MTZ_Tela_Transferencia_Saldo_Plano_Contas_Anterior_Centro_Custo_Moeda_Funcional

- **Fonte:** MTZ_Tela_Transferencia_Saldo_Plano_Contas_Anterior_Centro_Custo_Moeda_Funcional.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional 

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-2631

Criação de Tela

Criação da tela Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc355275051"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc355275052"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc355275053"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

\[Quem executará o evento\. Ex\.: Usuário do sistema\]\.

__Pré\- Condições__

\[Condições necessárias para execução\. Ex\.: Estabelecimento cadastrado\]

__Pós\-Condições__

\[Resultado após executar caso de uso\. Ex\.: Informação armazenada no banco de dados\]

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc355275054"></a>Fluxo Principal 

\[Descrever a ação principal que será realizada na tela especificada\.

 Ex\.: O usuário deseja realizar o cadastro de uma estrutura padrão\.

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc355275055"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ 

__                     Módulo__: MasterSAF\-DW >> Básicos >> MasterSAF DW

__                        Menu__: Manutenção >> Contabilidade >> Movimentos em Moeda Funcional >> Diário Geral >> Saldo Contábil por Centro de Custo em Moeda Funcional

__Título da tela: __Transferência de Saldos de Plano de Contas Anterior por Centro de Custo em Moeda Funcional

__Funcionamento da tela__: o acesso a esta tela será realizado através do botão do menu da tela de Saldos p/ Centro de Custo 

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAZCAIAAACpVwlNAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOwgAADsYBcUSPhAAAAZhJREFUSEtj/P//PwNtAOOVCydoYzIDE43MXbNhB62MBrp4eBv9cosfEJEUMUQFCNBQx8qbJJlLVFg/2+gLMfff3//PN/o+30is2wmk68frfJ2y6pk4FOBO/vbq/PElE2WCtuD3BOHE9+fPP4avzxh+voIjLn5py9D4x0diCIYPgbBWDNu6fcaMf08OMnx9vrW3ZEtPCZDNxS304+F7ko3GTAYq0ds2L9n87/2t378ZVEHsTUD23z+ESx4sroabDk9wGvHbNizc+PcvyDiN+O3rF2768/cfya4GagCmB7jpcLZ20g6dpO0Q44AMfjURko2GOM08acazjX5//4K0Q9hoBsnaLCHZ6D9//v9+Noedi80xfx4Q/f18FMg2j8x9tNaHoFloCtDDWi54y86pHf/eHkNOcBzM3//8JhxvaEZjzzI3FnsxMPxn+M/on1P87+vDLfPXqMdtI8nVOLOMRuw2jdjtf//8A5q7YfZqUs2FOAJflgFG49oZq7RhCYMkVwMV06puJFyGkOpSZPVEldfkWUCrAAG6BgADkckV1b46dQAAAABJRU5ErkJggg==)__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Conta do Plano de Contas Anterior \(Gr\./Cód\./Data Val\.\)

Editbox

S

N

Campo do tipo texto com as informações do Grupo, Código da Conta, Data de Validade e Descrição, acompanhado da pasta de seleção do Código da Conta\. 

Caso o usuário informe um código da Conta do Plano de Contas Anterior que não tem cadastro correspondente, retornar mensagem: “Conta Não Encontrada”\.

MFS\-2631

Centro de Custo do Plano de Contas Anterior \(Gr\./Cód\./Data Val\.\)

Editbox

N

S

Campo do tipo texto com as informações do Grupo, Código do Centro de Custo, Data de Validade e Descrição, acompanhado da pasta de seleção do Código do Centro de Custo\.

Caso o usuário informe um código de Centro de Custo que não tem cadastro correspondente, retornar mensagem: “Centro de Custo Não Encontrado”\.

MFS\-2631

Saldo Inicial

Editbox

N

S

Default: “,00”

MFS\-2631

Débito/Crédito

Radiobutton

N

S

Default: “Crédito”

Campo do tipo radiobutton com as opções:

- Débito
- Crédito

MFS\-2631

Novo

Botão

N

S

Botão que, no momento que for acionado, possibilita a inserção de um novo registro na tela\.

MFS\-2631

Excluí

Botão

N

S

Botão que, no momento que for acionado, possibilita a exclusão de um registro lido na tela\. O sistema deverá retornar a seguinte mensagem: “Confirma exclusão deste registro?”\.

Se o usuário modificar algum registro lido e tentar excluir, retornar a seguinte mensagem: “Existem modificações não confirmadas\. Deseja excluir o registro original?”\.

MFS\-2631

Confirma

Botão

N

S

Botão que, no momento que for acionado, gravará a inclusão/alteração do registro lido\.

MFS\-2631

Fecha

Botão

N

S

Botão que, no momento que for acionado, possibilita o fechamento da tela\.

MFS\-2631

