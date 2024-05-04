import re
from typing import Any, Dict
from src.drivers.mongodb_handler import DatabaseQuery
from src.errors.http_bad_request_error import HttpBadRequestError


def cep_factory(data: Dict[str, Any]):
    normalized_query = normalize_query(data)
    if not normalized_query:
        raise HttpBadRequestError(
            'Formato inválido'
        )
    query = DatabaseQuery()
    collection = query.handle_collection('cep')
    result = query.query_find_one(collection, normalized_query)
    return result


def normalize_query(query_dict: Dict[str, Any]):
    if query_dict.get("CEP"):
        cep_value = query_dict["CEP"]
        cep_value = re.sub(r'\D', '', cep_value)
        cep_value = cep_value.zfill(8)
        cep_value = f"{cep_value[:5]}-{cep_value[5:]}"
        return {"CEP": cep_value}
    return None
