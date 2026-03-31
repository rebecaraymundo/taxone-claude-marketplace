# MTZ_Tela_Detalhamento_Ajustes_Contribuicao_Pis_Apurado_M225

> Fonte: MTZ_Tela_Detalhamento_Ajustes_Contribuicao_Pis_Apurado_M225.docx






THOMSON REUTERS

Matriz da tela Detalhamento dos Ajustes da Contribuição de Pis/Pasep Apurado - M225



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Obrigações >> Manutenção >> Apuração PIS/PASEP

Deverá ser criada a tela “Detalhamento dos Ajustes da Contribuição de Pis/Pasep Apurado - M225” para que seja possível realizar a geração do registro M225 da EFD-Contribuições.

Esta tela será acessada através de nova aba inserida na tela de Apuração PIS/PASEP. Estará em um nível abaixo do nível das abas de Contribuição Diferida em Períodos Anteriores – M300, Sociedades Cooperativas – Composição da Base de Cálculo – PIS/Pasep – M211, Ajustes da Contribuição para o PIS/PASEP Apurada – M220 e Informações Adicionais de Diferimento – M230. Na estrutura dos registros da EFD-Contribuições este é um registro filho do M220 – Ajustes da Contribuição para o PIS/PASEP Apurada.

Deverá ser criada a tela de lista, permitindo a visualização das informações gravadas e a tela de detalhe, que será acessada na inserção de novas informações ou a partir de uma linha da tela de listagem.


* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4316-D | Marcos G. de Paula | Criação da tela de Ajustes da Contribuição de Pis/Pasep Apurado - M225. |
|  |  |  |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Detalhamento do Valor | Editbox | S | S | Formato: “,00” | Por ser um campo obrigatório, se não for informado ou for informado um valor igual a zero, retornar a mensagem: “Detalhamento do Valor não informado”. | OS4316-D |
| CST | Editbox | N | S | - | Campo padrão do Mastersaf com pasta de seleção, campo de código e descrição.  Através da pasta será possível acessar o conteúdo da TACES65. | OS4316-D |
| Detalhamento da BC | Editbox | N | S | Formato: “,000” |  | OS4316-D |
| Detalhamento da Alíquota | Editbox | N | S | Formato: “,0000” |  | OS4316-D |
| Data da Operação | Editbox | S | S | Formato: DD/MM/AAAA | Por ser um campo obrigatório, se não for informado, retornar a mensagem: “Data da Operação não informada”. | OS4316-D |
| Descrição da Operação | Editbox | N | S | - |  | OS4316-D |
| Conta Contábil | Editbox | N | S | - | Campo padrão do Mastersaf com pasta de seleção, campo de grupo, campo de código, campo de data de validade e descrição.  Através da pasta será possível acessar o conteúdo da SAFX2002. | OS4316-D |
| Informação Complementar | Editbox | N | S | - |  | OS4316-D |
