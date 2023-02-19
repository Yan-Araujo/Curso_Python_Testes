# Informações adicionais:

## Pytest:
    Como instalar: No terminal, digitar pip install pytest

    Obs: Após a instalação do pytest, digitar no terminal o comando
    pip freeze > requirements.txt para criar um arquivo de texto com
    todos os plugins utilizados no projeto

    - Instalando: Criar 2 diretórios no projeto sendo um onde sera alocado
    o arquivo.py que deveremos testar e outro, com o nome de tests onde serão
    alocados o iniciador do pytest, __init__.py, e o arquivo.py onde serão
    escritos os testes que deve ter o nome "test_" seguido donome do arquivo

    Esse Framework possui métodos próprios, como é o caso do "raises" e
    do "mark". O "raises" permite o uso de exceções nos testes desenvolvidos
    enquando o "mark" permite que seja criado um marcador em um ou mais 
    testes que facilita à executar testes específicos.

    Exemplo do uso do raises: "with pytest.raises(Exception):"
    Exemplo do uso do mark: "@pytest.mark.nomeParaBusca"

    O método "mark" já possui marcadores pré definidos, como é o caso do
    @pytest.mark.skip ou @pytest.mark.skipif. Caso seja criado um mark
    customizado, sera gerado um Warning. Para resolve-lo, basta criar no
    projeto um arquivo chamado "pytest.ini" e colocar o seguinte comando
    nele: 

        [pytest]
        markers =
            calcular_bonus: Teste para método calcular_bonus

    Note que esse comando deve estar escrito e identado exatamente
    como no exemplo.

    Comandos:
        - pytest: Executa os testes sem exibir detalhes sobre os mesmos

        - pytest -v: Executa os testes exibindo detalhes sobre os mesmos

        - pytest -k parametro: Executa os testes que tenham o parametro
        passado em seu nome de forma resumida

        - pytest -v -k parametro: Executa os testes que tenham o parametro
        passado em seu nome exibindo detalhes sobre o teste

        - pytest --junitxml report.xml: Cria um arquivo xml com os 
        resultados dos testes

        - pytest --cov-report xml: Cria um relatório xml do coverage

        

## Pytest --cov:
    Extensão do Pytest usada para que possamos averiguar se todo o nosso
    código está sendo testado. Nos exemplos, considere que o arquivo que 
    será testado está no diretório "codigos" e o arquivo dos testes no 
    diretório "tests'

    Como instalar: No terminal, digitar pip install pytest-cov

    Obs: Após a instalação do pytest --cov, digitar no terminal o comando
    pip freeze > requirements.txt para criar um arquivo de texto com
    todos os plugins utilizados no projeto

    Comandos:
        - pytest --cov: Executa todos os testes e exibe uma tabela com o 
        percentual de cobertura de cada arquivo no Projeto

        - pytest --cov=codigos tests: Exibe uma tabela com o percentual 
        de cobertura e com itens não testados

        - pytest --cov=codigos tests/ --cov-report term-missing: Exibe
        uma tabela que inclui as linhas faltam serem testadas.

        - pytest --cov=codigos tests/ --cov-report html: Gera um diretório
        chamado "htmlcov" onde possui um arquivo index.html com todos os
        detalhes sobre testes não executados no código. 

    O pytest-cov nativamente retorna qualquer função não testada no
    percentual da tabela e isso inclui as funções built-in do python
    como é o caso da __str__ ou __eq__. Para que não sejam contadas
    nesse percentual, é necessário criar um novo arquivo chamado 
    ".coveragerc" que deverá conter:

        [run]

        [report]
        exclude_lines=
            def __str__
            def __eq__            

    Nesse exemplo, as funções str e eq serão ignoradas na hora da contagem
    de testes em falta.

    No arquivo ".coveragerc", tambem podemos definir a fonte que será 
    usada para os teste. Dessa forma, podemos utilizar apenas o comando 
    "pytest --cov" para checarmos falta algo a ser testado. Para isso,
    precisamos inserir no arquivo a seguinte linha de código:

        source = ./codigos

    Dessa forma, configuramos nosso --cov para apenas checar no diretório
    codigos. O código final ficará:

        [run]
        source = ./codigos

        [report]
        exclude_lines=
            def __str__
            def __eq__

    Tambem podemos configurar o nome do diretório html que será criado
    ao utilizar o comando "pytest --cov=codigos tests/ --cov-report html".
    Para isso, basta adicionarmos ao ".coveragerc" o seguinte código:

        [html]
        directory = nome_do_diretorio_html

    Assim, nosso ficará da seguinte forma:

        [run]
        source = ./codigos

        [html]
        directory = coverage_relatorio_html

        [report]
        exclude_lines=
            def __str__
            def __eq__
        