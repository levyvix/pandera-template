# pandera-template


## Pandera

### Links


- [Tipos de dados](https://pandera.readthedocs.io/en/stable/reference/dtypes.html#api-dtypes)
- [Decoradores](https://pandera.readthedocs.io/en/stable/reference/decorators.html)
- [pa.Check](https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.checks.Check.html#pandera.api.checks.Check)
- [pa.Field](https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.dataframe.model_components.Field.html)
- [class Config](https://pandera.readthedocs.io/en/stable/dataframe_models.html#config)

### Criando os Contratos 
 
#### DataFrame Schemas
```python
import pandera as pa

from pandera import Column, DataFrameSchema, Check, Index

schema = DataFrameSchema(
    {
        "column1": Column(int),
        "column2": Column(float, Check(lambda s: s < -1.2)),
        # you can provide a list of validators
        "column3": Column(str, [
            Check(lambda s: s.str.startswith("value")),
            Check(lambda s: s.str.split("_", expand=True).shape[1] == 2)
        ]),
    },
    index=Index(int),
    strict=True,
    coerce=True,
)
```

#### DataFrame Models

- [Custom Checks](https://pandera.readthedocs.io/en/stable/dataframe_models.html#custom-checks)

### Aplicando as validações de Contrato

-  Com Decoradores:

    - `@pa.check_input(<CONTRATO_ENTRADA>)`: Checa os dados na entrada da função.
    - `@pa.check_output(<CONTRATO_SAÍDA>)`: Checa os dados na saída da função.
    - `@pa.check_io(df1 =<CONTRATO_ENTRADA> , df2 = <CONTRATO_ENTRADA>,  output = <CONTRATO_SAÍDA>)`: Checa os dados na entrada e na saida da função.