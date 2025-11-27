from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.exception_response import ExceptionResponse
from ...models.permissions_operation_response import PermissionsOperationResponse
from typing import cast



def _get_kwargs(
    permission_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2/permissions/common/grants/{permission_id}".format(permission_id=permission_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    if response.status_code == 202:
        response_202 = PermissionsOperationResponse.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    permission_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Odebranie uprawnień

     Metoda pozwala na odebranie uprawnienia o wskazanym identyfikatorze.
    Wymagane jest wcześniejsze odczytanie uprawnień w celu uzyskania
    identyfikatora uprawnienia, które ma zostać odebrane.

    > Więcej informacji:
    > - [Odbieranie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#odebranie-
    uprawnie%C5%84)

    **Wymagane uprawnienia**: `CredentialsManage`, `VatUeManage`, `SubunitManage`.

    Args:
        permission_id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy
            operacjach odbierania.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]
     """


    kwargs = _get_kwargs(
        permission_id=permission_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    permission_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Odebranie uprawnień

     Metoda pozwala na odebranie uprawnienia o wskazanym identyfikatorze.
    Wymagane jest wcześniejsze odczytanie uprawnień w celu uzyskania
    identyfikatora uprawnienia, które ma zostać odebrane.

    > Więcej informacji:
    > - [Odbieranie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#odebranie-
    uprawnie%C5%84)

    **Wymagane uprawnienia**: `CredentialsManage`, `VatUeManage`, `SubunitManage`.

    Args:
        permission_id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy
            operacjach odbierania.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse]
     """


    return sync_detailed(
        permission_id=permission_id,
client=client,

    ).parsed

async def asyncio_detailed(
    permission_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Odebranie uprawnień

     Metoda pozwala na odebranie uprawnienia o wskazanym identyfikatorze.
    Wymagane jest wcześniejsze odczytanie uprawnień w celu uzyskania
    identyfikatora uprawnienia, które ma zostać odebrane.

    > Więcej informacji:
    > - [Odbieranie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#odebranie-
    uprawnie%C5%84)

    **Wymagane uprawnienia**: `CredentialsManage`, `VatUeManage`, `SubunitManage`.

    Args:
        permission_id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy
            operacjach odbierania.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, PermissionsOperationResponse]]
     """


    kwargs = _get_kwargs(
        permission_id=permission_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    permission_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, ExceptionResponse, PermissionsOperationResponse]]:
    """ Odebranie uprawnień

     Metoda pozwala na odebranie uprawnienia o wskazanym identyfikatorze.
    Wymagane jest wcześniejsze odczytanie uprawnień w celu uzyskania
    identyfikatora uprawnienia, które ma zostać odebrane.

    > Więcej informacji:
    > - [Odbieranie uprawnień](https://github.com/CIRFMF/ksef-docs/blob/main/uprawnienia.md#odebranie-
    uprawnie%C5%84)

    **Wymagane uprawnienia**: `CredentialsManage`, `VatUeManage`, `SubunitManage`.

    Args:
        permission_id (str): Techniczny identyfikator nadanego uprawnienia – wymagany m.in. przy
            operacjach odbierania.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, PermissionsOperationResponse]
     """


    return (await asyncio_detailed(
        permission_id=permission_id,
client=client,

    )).parsed
