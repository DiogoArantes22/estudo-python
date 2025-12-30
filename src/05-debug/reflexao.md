● O que você conseguiu enxergar no debugger que não ficava tão claro apenas executando o programa normalmente (sem depuração)? 
Resp:Executando normalmente, eu só via a entrada e a saída final. Com o debugger, consegui enxergar o momento exato em que os dados mudam de tipo.
Exmp: No exercício do IMC (ex05), consegui ver o dicionário sendo montado passo a passo e confirmar se as chaves ('peso', 'altura') estavam escritas corretamente antes de serem usadas no cálculo.

● Em quais situações você acha mais prático usar o pdb pela linha de comando e em quais prefere o debugger visual do VS Code? 
Resp: Linha de comando acho mais prático para testes muito rápidos ou quando estou rodando scripts simples no terminal e quero apenas inspecionar uma variável específica. Já o debugger visual prefiro para a maioria dos casos, especialmente em programas como o do Aquário (ex06) e IMC (ex05). É muito mais fácil ver a lista de variáveis locais e globais na barra lateral e expandir os dicionários visualmente do que ficar digitando comndos repetidamente no consle pdb


● Houve algum erro ou comportamento inesperado nos seus exercícios que você só percebeu por causa da depuração? Descreva brevemente. 
Resp: Não teve nenhum erro, mas com o debbuger consegui visualizar melhor todo o "caminho" do código e entender melhor o porque de cada etapa. Ex: Percebi o quão importante é converter as variáveis logo na entrada dos dados para evittar TypeError.
