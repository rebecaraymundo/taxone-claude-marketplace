---
source: "MTZ_PowerLock_Troca_de_Senha.doc"
category: Seguranca
converted: auto
---

Power Lock - Troca de Senha

Localização:
Powerlock 


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3894
DW - BASICOS - SEGURANÇA - Tratamento para utilização de password
O objetivo da OS é criar novas regras para a criação/alteração de senhas no PowerLock.

OS4079
DW - BASICOS - SEGURANÇA - Tratamento para utilização de password
Ajustes nas regras definidas pela OS3894

 
REGRAS DE NEGÓCIO

Cód.
 Descrição
 DR
RN00
Regra p/ validação das senhas - Não permitir senha derivada do login do usuário
Quando esse campo estiver marcado na tela de Controle de Segurança, o sistema deverá verificar se existe alguma palavra na senha que tenha referencia com o login do usuário. Ou seja, se o login do usuário for "teste", a senha não pode conter a palavra "teste" em nenhuma posição, lembrando que esta regra se aplica ao login como um todo, como o exemplo citado acima.
No caso de o login ser "teste" e a senha utilizada ser "TEST123", esta será aceita.
Quando o parâmetro "Não permitir senha derivada do login do usuário" a senha informada pelo usuário não pode derivar de uma sequência de três letras de palavras informadas no login, realizando esta validação por palavra, considerando como palavra a expressão separada por um dos caracteres especiais: "!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "<", ">", ".", ":", ";", "?", "/", "\", "|", "ç" e "Ç".

Exemplo:
login = vanessa.paula.mella
Neste caso, a senha não poderia conter as palavras vanessa, paula e melo e nem uma sequência de três letras que estejam contidas nestas palavras, como van, pau, mel, ane, aul, etc

Neste caso, também seria inválida a senha colocada com letra maiúscula. Ex.: Van.
 
OS3894
OS4079
RN01
Regra p/ validação das senhas - Não permitir senha composta por sequenciais do mesmo caractere 4 vezes ou mais
Quando esse campo estiver marcado na tela de Controle de Segurança, o sistema deverá verificar se existe alguma palavra na senha que tenha o mesmo caractere repetido SEQUENCIALMENTE 4 vezes ou mais. Por exemplo: tesssssssssste, não é permitido. 
Quando o parâmetro "Não permitir senha composta por sequenciais do mesmo caractere 4 vezes ou mais", na senha escolhida pelo usuário não podem ser repetidos em uma sequência de quatro caracteres, considerando letras, números, caracteres especiais, considerando na relação de caracteres especiais: "!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "<", ">", ".", ":", ";", "?", "/", "\", "|", "ç" e "Ç".

Para letras, não pode haver distinção de maiúsculas e minúsculas.

Exemplo: Aaaa, 9999, @@@@, tessssste seria inválido.

OS3894
OS4079
RN02
Regra p/ validação das senhas - Não permitir senha composta pelas palavras parametrizadas aqui
Quando esse campo estiver marcado na tela de Controle de Segurança, Se a senha cadastrada consta dentro do banco de dados das palavras inseridas. A verificação deverá realizar a consulta a partir do número de caracteres utilizados na senha e a partir deste, realizar uma busca por palavras com a mesma quantidade ou quantidade menor de caracteres e caso a palavra esteja contida dentro da senha esta deverá ser vetada. Não deverão ser verificadas divergências entre caracteres Maiúsculas e Minúsculas.

Exemplificando: Palavra cadastrada "MASTERS" e senha "MASTERSAF" esta será recusada. Caso a senha seja "MSAF" esta será aceita, pelo motivo de a sequencia utilizada na senha estar abaixo da QTDE de caracteres utilizados na palavra chave
OS3894


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN


