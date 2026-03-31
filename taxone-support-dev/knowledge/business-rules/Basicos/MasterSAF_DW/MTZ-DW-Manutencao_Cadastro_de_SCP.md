# MTZ-DW-Manutencao_Cadastro_de_SCP

- **Fonte:** MTZ-DW-Manutencao_Cadastro_de_SCP.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Módulo DW – Tela Cadastro de SCP

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

MFS8291

Lara Aline

Inclusão do campo Incide DIRF\.

10/01/2017

Sumário

[1\.	Regras dos Campos	3](#_Toc471826356)

# <a id="_Toc350763252"></a><a id="_Toc471826356"></a>Regras dos Campos 

__Localização da tela:__ Menu Básicos,  Módulo: Mastersaf DW, item de menu Manutenção  Cadastros  Cadastro de SCP

__Título da tela: __Cadastro de SCP

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Incide DIRF

Checkbox

N

S

Default: Habilitado

Se o campo “Incide DIRF” estiver marcado, o sistema deve verificar se o campo Código da SCP corresponde a um CNPJ válido, caso o formato seja inválido exibir a seguinte mensagem:

‘Código da SCP não corresponde a um CNPJ válido, favor verificar ou desmarcar o campo “Incide DIRF” para esse código de SCP\.’

MFS8291

