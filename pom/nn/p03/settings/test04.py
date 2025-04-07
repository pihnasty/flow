from pydantic import BaseModel, Field

class StringPromptValue(BaseModel):
    value: str

class DataDomainPromptTemplate(BaseModel):
    prompt_value: StringPromptValue

class ExtendedDataDomainPromptTemplate(BaseModel):
    data_domain_prompt: DataDomainPromptTemplate
    additional_field: StringPromptValue = None

# Создаем объект типа StringPromptValue
string_prompt_value = StringPromptValue(value="SomeValue")

# Приводим к типу ExtendedDataDomainPromptTemplate
extended_data_domain_prompt_template = ExtendedDataDomainPromptTemplate(data_domain_prompt=DataDomainPromptTemplate(prompt_value=string_prompt_value), additional_field=string_prompt_value)

# Выводим значения полей
print("ExtendedDataDomainPromptTemplate - Prompt Value:", extended_data_domain_prompt_template.data_domain_prompt.prompt_value)
print("ExtendedDataDomainPromptTemplate - Additional Field:", extended_data_domain_prompt_template.additional_field)
