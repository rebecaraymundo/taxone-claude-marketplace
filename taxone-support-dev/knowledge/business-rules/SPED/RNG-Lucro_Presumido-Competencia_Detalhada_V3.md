# RNG-Lucro_Presumido-Competencia_Detalhada_V3

> Fonte: RNG-Lucro_Presumido-Competencia_Detalhada_V3.doc

Regras de Recuperação para os registros
Regime Competência – Detalhada
RNG	Para as empresas do Lucro Presumido e com Regime de Competência Detalhada (conforme parametrização feita na tela de Dados Inicias), a recuperação dos dados utilizará os mesmos critérios utilizados na geração dos registros A100/A110/A111/A170,C100/C110/C111/C170/C180/C181/ C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/C600/C601/
C605/C609/D200/D201/D205/D209/D300/D309/D350/D359/D600/D601/D605/D609, F100/F111/F200/F211/ F600/F700,(gerados no Lucro Real), porém, deverão ser filtrados apenas os documentos de Saída (Geradores de Receita). 

Quanto à exibição dos registros, (na geração dos arquivos), será considerado o mesmo formato dos registros gerados no Lucro Real. As informações serão geradas normalmente nos registros dos blocos A, C, D e F (considerando inclusive os registros de abertura e encerramento).Não deverão ser gerados os registros  F500,509,510,519,525,550,559,560,569 e nem o 1900.
Com relação ao bloco 0, apenas os registros 0000, 0001, 0100, 0110, 0140, 0150, 0190, 0200, 0205, 0206, 0400, 0450,0500,0600 e 0990 devem ser gerados (quando existir informações pertinentes a cada registros).

Verifique a RNG3-EFD
	OS3169-GE25B