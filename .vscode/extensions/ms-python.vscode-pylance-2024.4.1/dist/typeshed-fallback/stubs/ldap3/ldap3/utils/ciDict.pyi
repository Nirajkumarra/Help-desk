from _typeshed import Incomplete
from collections.abc import MutableMapping
from typing import TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class CaseInsensitiveDict(MutableMapping[_KT, _VT]):
    def __init__(self, other: Incomplete | None = None, **kwargs) -> None: ...
    def __contains__(self, item): ...
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, item) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def __eq__(self, other): ...
    def copy(self): ...

class CaseInsensitiveWithAliasDict(CaseInsensitiveDict[_KT, _VT]):
    def __init__(self, other: Incomplete | None = None, **kwargs) -> None: ...
    def aliases(self): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def set_alias(self, key, alias, ignore_duplicates: bool = False) -> None: ...
    def remove_alias(self, alias) -> None: ...
    def __getitem__(self, key): ...
    def copy(self): ...
