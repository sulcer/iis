## Serve
To start the server, run the following command:

```shell
poetry run poe serve
```

## Process data
To process data, run the following command:

```shell
poetry run poe process_data
```

## Validate with custom script
To start the script validation, run the following command:

```shell
poetry run poe validate
```

## Validate with evidently
To start the evidently validation, run the following command:

```shell
poetry run poe data_drift
```

Comment:
Nisem zaznal nobenega znatnega odstopanja podatkov v nobenem od stolpcev, glede na podane p-vrednosti. To pomeni, da ni prišlo do opaznih sprememb ali premikov v statističnih lastnostih nabora podatkov glede na teste, ki so se izvedli.
Ker ni bilo zaznano nobeno odstopanje, kaže, da porazdelitev podatkov ostaja stabilna v času glede na kriterije in pragove.