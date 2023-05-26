# nexus_sdk.model.docker_group_api_repository.DockerGroupApiRepository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**online** | bool,  | BoolClass,  | Whether this repository accepts incoming requests | 
**storage** | [**StorageAttributes**](StorageAttributes.md) | [**StorageAttributes**](StorageAttributes.md) |  | 
**docker** | [**DockerAttributes**](DockerAttributes.md) | [**DockerAttributes**](DockerAttributes.md) |  | 
**group** | [**GroupDeployAttributes**](GroupDeployAttributes.md) | [**GroupDeployAttributes**](GroupDeployAttributes.md) |  | 
**name** | str,  | str,  | A unique identifier for this repository | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
