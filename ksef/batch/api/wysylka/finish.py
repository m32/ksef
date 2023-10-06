from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.finish_response import FinishResponse
from ...models.finish_request import FinishRequest
from ...models.exception_response import ExceptionResponse
from typing import Dict



def _get_kwargs(
    *,
    json_body: FinishRequest,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/batch/Finish",
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, FinishResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FinishResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, FinishResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: FinishRequest,

) -> Response[Union[ExceptionResponse, FinishResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - finalizacja

     Finalizacja wysyłki wsadowej paczki faktur

    Args:
        json_body (FinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, FinishResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    print("*"*20, "/batch/Finish")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//batch/Finish")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: FinishRequest,

) -> Optional[Union[ExceptionResponse, FinishResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - finalizacja

     Finalizacja wysyłki wsadowej paczki faktur

    Args:
        json_body (FinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, FinishResponse]
     """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: FinishRequest,

) -> Response[Union[ExceptionResponse, FinishResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - finalizacja

     Finalizacja wysyłki wsadowej paczki faktur

    Args:
        json_body (FinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, FinishResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: FinishRequest,

) -> Optional[Union[ExceptionResponse, FinishResponse]]:
    """ Wysyłka wsadowa paczki faktur do KSeF - finalizacja

     Finalizacja wysyłki wsadowej paczki faktur

    Args:
        json_body (FinishRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, FinishResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
