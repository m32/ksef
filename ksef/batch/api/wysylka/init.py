from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.init_response import InitResponse
from typing import cast
from ...models.exception_response import ExceptionResponse
from ...types import File, FileJsonType
from io import BytesIO
from typing import Dict



def _get_kwargs(
    *,
    content: File,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "post",
        "url": "/batch/Init",
        "content": content.to_bytes(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, InitResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = InitResponse.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, InitResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Response[Union[ExceptionResponse, InitResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - inicjalizacja

     Inicjalizacja wysyłki wsadowej paczki faktur. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001/InitRequest

    Args:
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, InitResponse]]
     """


    kwargs = _get_kwargs(
        content=content,

    )

    print("*"*20, "/batch/Init")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//batch/Init")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Optional[Union[ExceptionResponse, InitResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - inicjalizacja

     Inicjalizacja wysyłki wsadowej paczki faktur. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001/InitRequest

    Args:
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, InitResponse]
     """


    return sync_detailed(
        client=client,
content=content,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Response[Union[ExceptionResponse, InitResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - inicjalizacja

     Inicjalizacja wysyłki wsadowej paczki faktur. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001/InitRequest

    Args:
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, InitResponse]]
     """


    kwargs = _get_kwargs(
        content=content,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    content: File,

) -> Optional[Union[ExceptionResponse, InitResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - inicjalizacja

     Inicjalizacja wysyłki wsadowej paczki faktur. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001/InitRequest

    Args:
        content_data (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, InitResponse]
     """


    return (await asyncio_detailed(
        client=client,
content=content,

    )).parsed
