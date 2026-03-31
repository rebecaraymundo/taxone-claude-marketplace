# MTZ_Tela_Manutenção_Bloco F_Creditos_Decorrentes_Incorporacao_Fusao_Cisao_F800

> Fonte: MTZ_Tela_Manutenção_Bloco F_Creditos_Decorrentes_Incorporacao_Fusao_Cisao_F800.docx






THOMSON REUTERS

Matriz da tela Créditos Decorrentes de Incorporação Fusão ou Cisão



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Layout da Tela:	4


## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco F >> Créditos Decorrentes de Incorporação Fusão ou Cisão (F800)


* Descrição não disponível em tela



## Layout da Tela:





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-B | Marcos G. de Paula | Criação do campo Código da SCP. |
| MFS-22180 | João Henrique de Araujo | Essa demanda tem como finalidade a criação do parâmetro “Período Apropriação Crédito” em atendimento ao cliente Claro para a geração dos registros F800 (Créditos Decorrentes de Eventos de Incorporação, Fusão e Cisão)e M100/M500 (Crédito do PIS Pasep/COFINS) da obrigação EFD – Contribuições. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Código da SCP | Editbox | N | S |  | Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código. Deverá acessar as informações da tabela SAFX2057.  Este campo deverá ser chave, mas não obrigatório. | OS4316-B |
| Período Apropriação Crédito | Data | S | S | MM/AAAA | Incluir na tela o campo DAT_APROP_CRED para digitação, na tabela Interna: EPC_CRED_INC_FUS_CIS.  Nesta tabela a data será considerada com o primeiro dia do mês por questões técnicas.  Regras:  O campo exibe a mensagem de preenchimento obrigatório para os novos cadastros ao salvar.  A tela permite que o usuário possa informar e/ ou editar o parâmetro “Período Apropriação Crédito” para os cadastros posteriores a criação desse campo. | MFS-22180 |
