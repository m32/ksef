from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.common_session_status import CommonSessionStatus
from ...models.exception_response import ExceptionResponse
from ...models.session_type import SessionType
from ...models.sessions_query_response import SessionsQueryResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime



def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 10,
    session_type: SessionType,
    reference_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    date_closed_from: Union[Unset, datetime.datetime] = UNSET,
    date_closed_to: Union[Unset, datetime.datetime] = UNSET,
    date_modified_from: Union[Unset, datetime.datetime] = UNSET,
    date_modified_to: Union[Unset, datetime.datetime] = UNSET,
    statuses: Union[Unset, list[CommonSessionStatus]] = UNSET,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_continuation_token, Unset):
        headers["x-continuation-token"] = x_continuation_token



    

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    json_session_type = session_type.value
    params["sessionType"] = json_session_type

    params["referenceNumber"] = reference_number

    json_date_created_from: Union[Unset, str] = UNSET
    if not isinstance(date_created_from, Unset):
        json_date_created_from = date_created_from.isoformat()
    params["dateCreatedFrom"] = json_date_created_from

    json_date_created_to: Union[Unset, str] = UNSET
    if not isinstance(date_created_to, Unset):
        json_date_created_to = date_created_to.isoformat()
    params["dateCreatedTo"] = json_date_created_to

    json_date_closed_from: Union[Unset, str] = UNSET
    if not isinstance(date_closed_from, Unset):
        json_date_closed_from = date_closed_from.isoformat()
    params["dateClosedFrom"] = json_date_closed_from

    json_date_closed_to: Union[Unset, str] = UNSET
    if not isinstance(date_closed_to, Unset):
        json_date_closed_to = date_closed_to.isoformat()
    params["dateClosedTo"] = json_date_closed_to

    json_date_modified_from: Union[Unset, str] = UNSET
    if not isinstance(date_modified_from, Unset):
        json_date_modified_from = date_modified_from.isoformat()
    params["dateModifiedFrom"] = json_date_modified_from

    json_date_modified_to: Union[Unset, str] = UNSET
    if not isinstance(date_modified_to, Unset):
        json_date_modified_to = date_modified_to.isoformat()
    params["dateModifiedTo"] = json_date_modified_to

    json_statuses: Union[Unset, list[str]] = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = []
        for statuses_item_data in statuses:
            statuses_item = statuses_item_data.value
            json_statuses.append(statuses_item)


    params["statuses"] = json_statuses


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/sessions",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    if response.status_code == 200:
        response_200 = SessionsQueryResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    session_type: SessionType,
    reference_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    date_closed_from: Union[Unset, datetime.datetime] = UNSET,
    date_closed_to: Union[Unset, datetime.datetime] = UNSET,
    date_modified_from: Union[Unset, datetime.datetime] = UNSET,
    date_modified_to: Union[Unset, datetime.datetime] = UNSET,
    statuses: Union[Unset, list[CommonSessionStatus]] = UNSET,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    """ Pobranie listy sesji

     Zwraca listę sesji spełniających podane kryteria wyszukiwania.



    **Sortowanie:**

    - dateCreated (Desc)


    **Wymagane uprawnienia**:
    - `Introspection` – pozwala pobrać wszystkie sesje w bieżącym kontekście uwierzytelnienia
    `(ContextIdentifier)`.
    - `InvoiceWrite` – pozwala pobrać wyłącznie sesje utworzone przez podmiot uwierzytelniający, czyli
    podmiot inicjujący uwierzytelnienie.

    Args:
        page_size (Union[Unset, int]):  Default: 10.
        session_type (SessionType): | Wartość | Opis |
            | --- | --- |
            | Online | Wysyłka interaktywna (pojedyncze faktury). |
            | Batch | Wysyłka wsadowa (paczka faktur). |
        reference_number (Union[Unset, str]): Numer referencyjny.
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        date_closed_from (Union[Unset, datetime.datetime]):
        date_closed_to (Union[Unset, datetime.datetime]):
        date_modified_from (Union[Unset, datetime.datetime]):
        date_modified_to (Union[Unset, datetime.datetime]):
        statuses (Union[Unset, list[CommonSessionStatus]]):
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, SessionsQueryResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
session_type=session_type,
reference_number=reference_number,
date_created_from=date_created_from,
date_created_to=date_created_to,
date_closed_from=date_closed_from,
date_closed_to=date_closed_to,
date_modified_from=date_modified_from,
date_modified_to=date_modified_to,
statuses=statuses,
x_continuation_token=x_continuation_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    session_type: SessionType,
    reference_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    date_closed_from: Union[Unset, datetime.datetime] = UNSET,
    date_closed_to: Union[Unset, datetime.datetime] = UNSET,
    date_modified_from: Union[Unset, datetime.datetime] = UNSET,
    date_modified_to: Union[Unset, datetime.datetime] = UNSET,
    statuses: Union[Unset, list[CommonSessionStatus]] = UNSET,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    """ Pobranie listy sesji

     Zwraca listę sesji spełniających podane kryteria wyszukiwania.



    **Sortowanie:**

    - dateCreated (Desc)


    **Wymagane uprawnienia**:
    - `Introspection` – pozwala pobrać wszystkie sesje w bieżącym kontekście uwierzytelnienia
    `(ContextIdentifier)`.
    - `InvoiceWrite` – pozwala pobrać wyłącznie sesje utworzone przez podmiot uwierzytelniający, czyli
    podmiot inicjujący uwierzytelnienie.

    Args:
        page_size (Union[Unset, int]):  Default: 10.
        session_type (SessionType): | Wartość | Opis |
            | --- | --- |
            | Online | Wysyłka interaktywna (pojedyncze faktury). |
            | Batch | Wysyłka wsadowa (paczka faktur). |
        reference_number (Union[Unset, str]): Numer referencyjny.
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        date_closed_from (Union[Unset, datetime.datetime]):
        date_closed_to (Union[Unset, datetime.datetime]):
        date_modified_from (Union[Unset, datetime.datetime]):
        date_modified_to (Union[Unset, datetime.datetime]):
        statuses (Union[Unset, list[CommonSessionStatus]]):
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, SessionsQueryResponse]
     """


    return sync_detailed(
        client=client,
page_size=page_size,
session_type=session_type,
reference_number=reference_number,
date_created_from=date_created_from,
date_created_to=date_created_to,
date_closed_from=date_closed_from,
date_closed_to=date_closed_to,
date_modified_from=date_modified_from,
date_modified_to=date_modified_to,
statuses=statuses,
x_continuation_token=x_continuation_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    session_type: SessionType,
    reference_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    date_closed_from: Union[Unset, datetime.datetime] = UNSET,
    date_closed_to: Union[Unset, datetime.datetime] = UNSET,
    date_modified_from: Union[Unset, datetime.datetime] = UNSET,
    date_modified_to: Union[Unset, datetime.datetime] = UNSET,
    statuses: Union[Unset, list[CommonSessionStatus]] = UNSET,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    """ Pobranie listy sesji

     Zwraca listę sesji spełniających podane kryteria wyszukiwania.



    **Sortowanie:**

    - dateCreated (Desc)


    **Wymagane uprawnienia**:
    - `Introspection` – pozwala pobrać wszystkie sesje w bieżącym kontekście uwierzytelnienia
    `(ContextIdentifier)`.
    - `InvoiceWrite` – pozwala pobrać wyłącznie sesje utworzone przez podmiot uwierzytelniający, czyli
    podmiot inicjujący uwierzytelnienie.

    Args:
        page_size (Union[Unset, int]):  Default: 10.
        session_type (SessionType): | Wartość | Opis |
            | --- | --- |
            | Online | Wysyłka interaktywna (pojedyncze faktury). |
            | Batch | Wysyłka wsadowa (paczka faktur). |
        reference_number (Union[Unset, str]): Numer referencyjny.
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        date_closed_from (Union[Unset, datetime.datetime]):
        date_closed_to (Union[Unset, datetime.datetime]):
        date_modified_from (Union[Unset, datetime.datetime]):
        date_modified_to (Union[Unset, datetime.datetime]):
        statuses (Union[Unset, list[CommonSessionStatus]]):
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionResponse, SessionsQueryResponse]]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
session_type=session_type,
reference_number=reference_number,
date_created_from=date_created_from,
date_created_to=date_created_to,
date_closed_from=date_closed_from,
date_closed_to=date_closed_to,
date_modified_from=date_modified_from,
date_modified_to=date_modified_to,
statuses=statuses,
x_continuation_token=x_continuation_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = 10,
    session_type: SessionType,
    reference_number: Union[Unset, str] = UNSET,
    date_created_from: Union[Unset, datetime.datetime] = UNSET,
    date_created_to: Union[Unset, datetime.datetime] = UNSET,
    date_closed_from: Union[Unset, datetime.datetime] = UNSET,
    date_closed_to: Union[Unset, datetime.datetime] = UNSET,
    date_modified_from: Union[Unset, datetime.datetime] = UNSET,
    date_modified_to: Union[Unset, datetime.datetime] = UNSET,
    statuses: Union[Unset, list[CommonSessionStatus]] = UNSET,
    x_continuation_token: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ExceptionResponse, SessionsQueryResponse]]:
    """ Pobranie listy sesji

     Zwraca listę sesji spełniających podane kryteria wyszukiwania.



    **Sortowanie:**

    - dateCreated (Desc)


    **Wymagane uprawnienia**:
    - `Introspection` – pozwala pobrać wszystkie sesje w bieżącym kontekście uwierzytelnienia
    `(ContextIdentifier)`.
    - `InvoiceWrite` – pozwala pobrać wyłącznie sesje utworzone przez podmiot uwierzytelniający, czyli
    podmiot inicjujący uwierzytelnienie.

    Args:
        page_size (Union[Unset, int]):  Default: 10.
        session_type (SessionType): | Wartość | Opis |
            | --- | --- |
            | Online | Wysyłka interaktywna (pojedyncze faktury). |
            | Batch | Wysyłka wsadowa (paczka faktur). |
        reference_number (Union[Unset, str]): Numer referencyjny.
        date_created_from (Union[Unset, datetime.datetime]):
        date_created_to (Union[Unset, datetime.datetime]):
        date_closed_from (Union[Unset, datetime.datetime]):
        date_closed_to (Union[Unset, datetime.datetime]):
        date_modified_from (Union[Unset, datetime.datetime]):
        date_modified_to (Union[Unset, datetime.datetime]):
        statuses (Union[Unset, list[CommonSessionStatus]]):
        x_continuation_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionResponse, SessionsQueryResponse]
     """


    return (await asyncio_detailed(
        client=client,
page_size=page_size,
session_type=session_type,
reference_number=reference_number,
date_created_from=date_created_from,
date_created_to=date_created_to,
date_closed_from=date_closed_from,
date_closed_to=date_closed_to,
date_modified_from=date_modified_from,
date_modified_to=date_modified_to,
statuses=statuses,
x_continuation_token=x_continuation_token,

    )).parsed
