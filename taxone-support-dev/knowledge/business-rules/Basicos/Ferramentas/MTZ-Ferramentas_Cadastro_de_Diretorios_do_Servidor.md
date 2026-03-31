# MTZ-Ferramentas_Cadastro_de_Diretorios_do_Servidor

- **Fonte:** MTZ-Ferramentas_Cadastro_de_Diretorios_do_Servidor.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

# Ferramentas – Cadastro de Diretórios do Servidor 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3888\-A1

O objetivo da OS é criar um cadastro de diretório do servidor, para melhorar o uso do upload no módulo Gerenciador de ISS\.

OS3743\-K

Cadastro do Diretorio do Servidor

A tela “Cadastro do Diretorio do Servidor” receberá os registros importados da SAFX196:

Importação Batch

Importção Online \.\.\.\.\.\.

OS4514\-B

Cadastro do Diretórios do Servidor

A tela “Cadastro de Diretórios do Servidor” nova opção de Módulo\.

OS4302\-G

Cadastro do Diretórios do Servidor

A tela “Cadastro de Diretórios do Servidor” nova opção de Módulo\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Criação de Novo Menu

Deverá ser criado o seguinte menu no módulo Básicos – Ferramentas:

Parâmetros do Sistema > Cadastro de Diretórios do Servidor

OS3888\-A1

__RN01__

Regra p/ tela Ferramentas – Parâmetros do Sistema > Cadastro de Diretórios do Servidor

A tela deve exibir as seguintes opções:

Novo: permite ao usuário criar um novo cadastro\.

Excluir: permite ao usuário excluir um cadastro\.

Confirmar: permite ao usuário gravar as informações do cadastro\.

Ordem: permite ao usuário ordenar as linhas apresentadas no cadastro\.

Imprime: permite ao usuário imprimir o cadastro\.

Relatório: permite ao usuário gerar o relatório do cadastro\.

Fechar: permite ao usuário fechar a tela de cadastro\.

OS3888\-A1

__RN02__

Regra p/ tela Cadastro de Diretórios do Servidor \- campo Módulo 

Campo do tipo combobox\. Deve listar o nome de todos os módulos disponíveis para a parametrização\. 

Inicialmente será disponibilizado somente o módulo Gerenciador de ISS\.

No campo “Módulo”, tela “Cadastro de Diretorios do Servidor”, será incluido a opção: “Job\_Servidor”, “Integrador Onesource eSocial”, “Integrador Onesource ECF” e Monitor de Tributos a Pagar

OS3888\-A1

OS3743\-K

OS4514\-B

OS4302\-G

MFS\-1689

__RN03__

Regra p/ tela Cadastro de Diretórios do Servidor \- campo Identificador do Diretório no Servidor \(Directory\) 

Campo do tipo combobox\. Deve listar todos os diretórios do servidor disponíveis ao usuário\.

Ao selecionar um diretório do servidor, será verificado se existem permissões no banco de dados\.

Se não existir permissão para um determinado diretório, sistema vai montar um script no campo de observação da tela\. O script gerado deve ser copiado e enviado ao DBA, para que o mesmo realize as permissões necessárias\.

OS3888\-A1

__RN04__

Regra p/ tela Cadastro de Diretórios do Servidor – campo Caminho do Diretório

Campo do tipo textbox desabilitado por default\. Deve demonstrar o caminho do diretório do servidor selecionado\.

OS3888\-A1

__RN04__

__Regra p/ tela Cadastro de Diretórios do Servidor – campo Directory Criado__

Campo somente informativo\. Deve mostrar “Sim” ou “Não”\.

OS3888\-A1

__RN05__

__Regra p/ tela Cadastro de Diretórios do Servidor – campo Permissão Java__

Campo somente informativo\. Deve mostrar “Sim” ou “Não”\.

OS3888\-A1

__RN07__

__Regra p/ tela Cadastro de Diretórios do Servidor – Campo do script__

Campo do tipo textbox desabilitado para edição\. Deve demonstrar o script a ser copiado para envio ao DBA\. O script deve ser copiado através do botão “Copiar p/ área transferência”\.

OS3888\-A1

__RN08__

Na tela “Cadastro de Diretorio do Servidor” os campos “Identificador do Diretorio no Servidor” e o campo “ Caminho do Diretorio” não poderão ser definidos pelo usuário\.

Esses campos estarão sujeitos a mudanças mediante a permissão de um DBA\.

OS3743\-K

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

