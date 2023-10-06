from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.exception_response import ExceptionResponse
from ...models.terminate_session_response import TerminateSessionResponse
from typing import cast



def _get_kwargs(
    
) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "get",
        "url": "/online/Session/Terminate",
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TerminateSessionResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    """ Wymuszenie zamknięcia aktywnej sesji

     Wymuszenie zamknięcia aktywnej sesji interaktywnej

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
     """


    kwargs = _get_kwargs(
        
    )

    print("*"*20, "/online/Session/Terminate")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Session/Terminate")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    """ Wymuszenie zamknięcia aktywnej sesji

     Wymuszenie zamknięcia aktywnej sesji interaktywnej

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, TerminateSessionResponse]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[ExceptionResponse, TerminateSessionResponse]]:
    """ Wymuszenie zamknięcia aktywnej sesji

     Wymuszenie zamknięcia aktywnej sesji interaktywnej

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, TerminateSessionResponse]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ExceptionResponse, TerminateSessionResponse]]:
    """ Wymuszenie zamknięcia aktywnej sesji

     Wymuszenie zamknięcia aktywnej sesji interaktywnej

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, TerminateSessionResponse]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
