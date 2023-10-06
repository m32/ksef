from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.internal_identifier_generated_response import InternalIdentifierGeneratedResponse
from typing import cast
from typing import Dict



def _get_kwargs(
    input_digits_sequence: str,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/online/Session/GenerateInternalIdentifier/{inputDigitsSequence}".format(inputDigitsSequence=input_digits_sequence,),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InternalIdentifierGeneratedResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExceptionResponse.from_dict(response.json())



        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    input_digits_sequence: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    """ Wygenerowanie identyfikatora wewnetrznego

     Wygenerowanie identyfikatora wewnetrznego na podstawie nip i 4 cyfr

    Args:
        input_digits_sequence (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]
     """


    kwargs = _get_kwargs(
        input_digits_sequence=input_digits_sequence,

    )

    print("*"*20, "/online/Session/GenerateInternalIdentifier/{inputDigitsSequence}")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Session/GenerateInternalIdentifier/{inputDigitsSequence}")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    input_digits_sequence: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    """ Wygenerowanie identyfikatora wewnetrznego

     Wygenerowanie identyfikatora wewnetrznego na podstawie nip i 4 cyfr

    Args:
        input_digits_sequence (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, InternalIdentifierGeneratedResponse]
     """


    return sync_detailed(
        input_digits_sequence=input_digits_sequence,
client=client,

    ).parsed

async def asyncio_detailed(
    input_digits_sequence: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    """ Wygenerowanie identyfikatora wewnetrznego

     Wygenerowanie identyfikatora wewnetrznego na podstawie nip i 4 cyfr

    Args:
        input_digits_sequence (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]
     """


    kwargs = _get_kwargs(
        input_digits_sequence=input_digits_sequence,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    input_digits_sequence: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, InternalIdentifierGeneratedResponse]]:
    """ Wygenerowanie identyfikatora wewnetrznego

     Wygenerowanie identyfikatora wewnetrznego na podstawie nip i 4 cyfr

    Args:
        input_digits_sequence (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, InternalIdentifierGeneratedResponse]
     """


    return (await asyncio_detailed(
        input_digits_sequence=input_digits_sequence,
client=client,

    )).parsed
