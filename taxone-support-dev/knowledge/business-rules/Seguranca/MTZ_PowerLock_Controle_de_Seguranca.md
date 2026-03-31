---
source: "MTZ_PowerLock_Controle de Seguranca.docx"
category: Seguranca
converted: auto
---

# Power Lock – Controle de Segurança – Parâmetros

**Localização:**
Powerlock > File > Controle de Segurança > Parâmetros



DOCUMENTO DE REQUISITO



## REGRAS DE NEGÓCIO





Considerações deste modelo:

**Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**


**Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:**



---

| DR | Nome | Descrição |
| --- | --- | --- |
| OS3894 | DW - BASICOS - SEGURANÇA - Tratamento para utilização de password | O objetivo da OS é criar novas regras para a criação/alteração de senhas no PowerLock. |
| OS4381 | DW - BASICOS - Powerlock - USUÁRIOS SIMULTANEOS | Criação de parâmetro para Bloquear acessos Simultâneos |


---

| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Regra p/ campo Não permitir senha derivada do login do usuário Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado (default). | OS3894 |
| RN01 | Regra p/ campo Não permitir senha composta por sequencias do mesmo caracter 4 vezes ou mais Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado (default). | OS3894 |
| RN02 | Regra p/ campo Não permitir senha composta pelas palavras parametrizadas aqui Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado (default). | OS3894 |
| RN03 | Regra p/ campo Bloquear Acessos Simultâneos (frame Acessos Simultâneos) Esse campo deve ser um checkbox e deve ter as seguintes opções: “S” – marcado e “N” – desmarcado (default). | OS4381 |


---

| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |



---

| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

