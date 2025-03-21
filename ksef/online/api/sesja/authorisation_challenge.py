from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.authorisation_challenge_request import AuthorisationChallengeRequest
from typing import cast
from ...models.exception_response import ExceptionResponse
from ...models.authorisation_challenge_response import AuthorisationChallengeResponse



def _get_kwargs(
    *,
    json_body: AuthorisationChallengeRequest,

) -> Dict[str, Any]:
    

    cookies = {}


    

    json_json_body = json_body.to_dict()



    

    return {
        "method": "post",
        "url": "/online/Session/AuthorisationChallenge",
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AuthorisationChallengeResponse.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AuthorisationChallengeRequest,

) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """ Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
     """


    kwargs = _get_kwargs(
        json_body=json_body,

    )

    print("*"*20, "/online/Session/AuthorisationChallenge")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//online/Session/AuthorisationChallenge")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AuthorisationChallengeRequest,

) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """ Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthorisationChallengeResponse, ExceptionResponse]
     """


    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AuthorisationChallengeRequest,

) -> Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """ Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthorisationChallengeResponse, ExceptionResponse]]
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
    json_body: AuthorisationChallengeRequest,

) -> Optional[Union[AuthorisationChallengeResponse, ExceptionResponse]]:
    """ Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji

     Inicjalizacja mechanizmu uwierzytelnienia i autoryzacji.

    Args:
        json_body (AuthorisationChallengeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthorisationChallengeResponse, ExceptionResponse]
     """


    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
