# MTZ-Parametrizacao-GIA-MG

- **Fonte:** MTZ-Parametrizacao-GIA-MG.docx
- **Modificado:** 2022-05-04
- **Tamanho:** 33 KB

---

# Parametrização \- GIA – MG 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3346  

Desmembramento CNAE\-F para o código de atividade 1052000

Ao gerar o arquivo da DAPI o sistema gera automaticamente o desmembramento como “00”, porém ao validar o arquivo ocorre a critica que este campo não é valido, conforme validação do arquivo do cliente\.

Para que seja importado corretamente este arquivo com o código de atividade “1052000” o desmembramento deve ser “01, 02 ou 03” conforme o validado da DAPI\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para criação do parâmetro “Desmembramento CNAE\-F”:__

__Módulo: __Estadual → GIA MG

__Menu:__ Parâmetros

Incluir o novo item no menu parametrização __“Desmembramento CNAE\-F”\.__

Este parâmetro não será obrigatório para a geração da GIA, porém tem algumas atividades que possuem esse desmembramento\.

__OS3346__

__RN01__

__Regra para criação de tela “Desmembramento CNAE\-F”:__

Esta nova tela de parametrização deve conter os seguintes campos:

Estabelecimento

Código de Atividade

Desmembramento do CNAE

__OS3346__

__RN02__

__Regra para campo Estabelecimento:__

Caso o usuário selecione o estabelecimento na tela de login do sistema, não deverá ter outra opção de escolha para outro estabelecimento\.

Caso o usuário não selecione o estabelecimento na tela do login, deverá apresentar todos os estabelecimentos da empresa selecionada pelo usuário, e que este tenha o devido acesso no Powerlook\.

__OS3346__

__RN03__

__Regra para campo Código de Atividade:__

Deve ser um campo tipo pasta\.

Deve trazer informações da TACES01\.txt – Atividade Economica\.

O preenchimento deste campo será automático no momento que o usuário selecionar o estabelecimento, ou seja, a informação deve vir do campo Atividade Economica da tela de cadastro de Empresas/ Estabelecimentos\.

Caso não haja nenhuma atividade econômica cadastrada para o estabelecimento, o sistema __NÃO__ deve permitir gravação na parametrização, mas sim sinalizar que o CNAE não está devidamente cadastrado e parametrizado\.

__OS3346__

__RN04__

__Regra para campo Desmembramento do CNAE:__

Deve ser um radiobutton group com 4 itens: 00 \( por default selecionado\),01, 02 e 03\.

Este campo deve estar por default desmarcado\.

__OS3346__

__RN05__

__Regra para funcionamento da nova parametrização:__

__Módulo: __Estadual → GIA MG

__Menu:__ Obrigações → DAPI → Geração → Geração dos Registros

Quando o usuário efetuar essa parametrização, no arquivo txt deverá ser incluída a informação do campo __Desmembramento do CNAE,__ na linha 00, posição 59 \(após o código de atividade\), o tamanho é 02\.

__OS3346__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

