# MFS19177_EVIDENCIA_QA_TESTE

> Fonte: MFS19177_EVIDENCIA_QA_TESTE.docx


Processamento PAT






- Estamos exibindo a mensagem DW00066, indevidamente no processamento em lote.










- Apaguei todas as aberturas de apuração e ao pesquisar novamente a abertura, o sistema está preenchendo no cabeçalho a data final do último dia da escrituração, como sendo fevereiro


- Não está mais aparecendo o ícone de lápis (vermelho ou verde) na entrada manual. Faço uma entrada manual na linha, o valor é salvo, mas não exibe o lápis vermelho. Incluo a justificativa, o sistema salva, mas não exibe o lápis verde.



Esta situação não era erro. Apenas não estava arualizado no diretório as imagens do produto.

- Ao processar o período de março, o sistema retorna o erro na transcrição de valores (mas não indica o problema). Se o processamento é refeito, o processo é executado sem problemas.



- Não está sendo possível adicionar uma abertura com situação especial , com data do evento no ultimo dia do mês.


6.
O valor do PAT de períodos anteriores do registro N630 não está correto.







Erros encontrados por A&D


ECF_PAT:

(1) Erro na inicialização de variáveis (ECF023 -2018 – 01/01/2018  - A03 - MARÇO) .(OK)

(2) Na apuração de Abril não gravou a tabela CLOSED (ECF023 – 2018 – 01/04/2018 – A04).
- Abril é a primeira apuração da escrituração.

(3) Não está legal o CUR_PREV_TUSE (22/06) .(OK)


O erro está na view:


(4) Gerar_lancamento_parte_b:  (20/06) .(OK)
- Depois da modificação de hoje, não está gerando nem lançamento a Dédito nem a Crédito.
(5) Correção na view .(OK)



Transcrição de Valores:
ECF_PRESET – função Limpeza
(6)  ECF_PRESET : NÃO ESTAVA DEVOLVENDO O N630 DO PERÍODO ANTERIOR. (ok)
(7) ECF_PRESET (Limpeza): devolução e limpeza do N630 de PERÍODO ANTERIOR dentro da mesma escrituração. Fez devolução e limpeza com apuração anterior de uma escrituração anterior. (OK)

Cálculo das Formulas do PAT
(8)  Mensagem DW00249 sem a DW00250. (ok)
(9)  IND_BALANCE_DETAIL (ok)
(10)  CÓPIA PARA O A00 do campo novo (ECF_PREV_TUSE) (ok)


| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 25/06/2018 | MFS-19177 | Criação do documento | Alessandra Cristina Navatta |
| 02/07/2018 | MFS-19177 | Erros encontrados por A&D | Alessandra Cristina Navatta |
