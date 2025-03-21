from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.common_register_access_point_provider_content_data import CommonRegisterAccessPointProviderContentData
from typing import Dict
from typing import cast
from ...models.register_access_point_response import RegisterAccessPointResponse
from ...models.exception_response import ExceptionResponse



def _get_kwargs(
    *,
    content: CommonRegisterAccessPointProviderContentData,

) -> Dict[str, Any]:
    

    cookies = {}


    

    

    

    return {
        "method": "post",
        "url": "/common/registerAccessPointProvider",
        "content": content.to_bytes(),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegisterAccessPointResponse.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content: CommonRegisterAccessPointProviderContentData,

) -> Response[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    """ Metoda umożliwia rejestrację w KSeF nowego dostawcę usług Peppol, który posiada aktywny certyfikat
    Peppol

     Rejerstracja w KSeF nowego dostawcę usług Peppol

    Args:
        content_data (CommonRegisterAccessPointProviderContentData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, RegisterAccessPointResponse]]
     """


    kwargs = _get_kwargs(
        content=content,

    )

    print("*"*20, "/common/registerAccessPointProvider")
    print(kwargs)
    response = client.get_httpx_client().request(
        **kwargs,
    )
    print("*"*20, "//common/registerAccessPointProvider")
    print(response, response.content)

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    content: CommonRegisterAccessPointProviderContentData,

) -> Optional[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    """ Metoda umożliwia rejestrację w KSeF nowego dostawcę usług Peppol, który posiada aktywny certyfikat
    Peppol

     Rejerstracja w KSeF nowego dostawcę usług Peppol

    Args:
        content_data (CommonRegisterAccessPointProviderContentData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, RegisterAccessPointResponse]
     """


    return sync_detailed(
        client=client,
content=content,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content: CommonRegisterAccessPointProviderContentData,

) -> Response[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    """ Metoda umożliwia rejestrację w KSeF nowego dostawcę usług Peppol, który posiada aktywny certyfikat
    Peppol

     Rejerstracja w KSeF nowego dostawcę usług Peppol

    Args:
        content_data (CommonRegisterAccessPointProviderContentData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponse, RegisterAccessPointResponse]]
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
    content: CommonRegisterAccessPointProviderContentData,

) -> Optional[Union[ExceptionResponse, RegisterAccessPointResponse]]:
    """ Metoda umożliwia rejestrację w KSeF nowego dostawcę usług Peppol, który posiada aktywny certyfikat
    Peppol

     Rejerstracja w KSeF nowego dostawcę usług Peppol

    Args:
        content_data (CommonRegisterAccessPointProviderContentData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponse, RegisterAccessPointResponse]
     """


    return (await asyncio_detailed(
        client=client,
content=content,

    )).parsed
