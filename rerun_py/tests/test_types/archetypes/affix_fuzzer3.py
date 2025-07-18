# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/testing/archetypes/fuzzy.fbs".

# You can extend this class by creating a "AffixFuzzer3Ext" class in "affix_fuzzer3_ext.py".

from __future__ import annotations

from typing import Any

import numpy as np
import pyarrow as pa
from attrs import define, field
from rerun._baseclasses import (
    Archetype,
    ComponentColumnList,
)
from rerun.error_utils import catch_and_log_exceptions

from .. import components, datatypes

__all__ = ["AffixFuzzer3"]


@define(str=False, repr=False, init=False)
class AffixFuzzer3(Archetype):
    def __init__(
        self: Any,
        *,
        fuzz2001: datatypes.AffixFuzzer1Like | None = None,
        fuzz2002: datatypes.AffixFuzzer1Like | None = None,
        fuzz2003: datatypes.AffixFuzzer1Like | None = None,
        fuzz2004: datatypes.AffixFuzzer1Like | None = None,
        fuzz2005: datatypes.AffixFuzzer1Like | None = None,
        fuzz2006: datatypes.AffixFuzzer1Like | None = None,
        fuzz2007: components.AffixFuzzer7Like | None = None,
        fuzz2008: components.AffixFuzzer8Like | None = None,
        fuzz2009: components.AffixFuzzer9Like | None = None,
        fuzz2010: components.AffixFuzzer10Like | None = None,
        fuzz2011: components.AffixFuzzer11Like | None = None,
        fuzz2012: components.AffixFuzzer12Like | None = None,
        fuzz2013: components.AffixFuzzer13Like | None = None,
        fuzz2014: datatypes.AffixFuzzer3Like | None = None,
        fuzz2015: datatypes.AffixFuzzer3Like | None = None,
        fuzz2016: components.AffixFuzzer16Like | None = None,
        fuzz2017: components.AffixFuzzer17Like | None = None,
        fuzz2018: components.AffixFuzzer18Like | None = None,
    ) -> None:
        """Create a new instance of the AffixFuzzer3 archetype."""

        # You can define your own __init__ function as a member of AffixFuzzer3Ext in affix_fuzzer3_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                fuzz2001=fuzz2001,
                fuzz2002=fuzz2002,
                fuzz2003=fuzz2003,
                fuzz2004=fuzz2004,
                fuzz2005=fuzz2005,
                fuzz2006=fuzz2006,
                fuzz2007=fuzz2007,
                fuzz2008=fuzz2008,
                fuzz2009=fuzz2009,
                fuzz2010=fuzz2010,
                fuzz2011=fuzz2011,
                fuzz2012=fuzz2012,
                fuzz2013=fuzz2013,
                fuzz2014=fuzz2014,
                fuzz2015=fuzz2015,
                fuzz2016=fuzz2016,
                fuzz2017=fuzz2017,
                fuzz2018=fuzz2018,
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            fuzz2001=None,
            fuzz2002=None,
            fuzz2003=None,
            fuzz2004=None,
            fuzz2005=None,
            fuzz2006=None,
            fuzz2007=None,
            fuzz2008=None,
            fuzz2009=None,
            fuzz2010=None,
            fuzz2011=None,
            fuzz2012=None,
            fuzz2013=None,
            fuzz2014=None,
            fuzz2015=None,
            fuzz2016=None,
            fuzz2017=None,
            fuzz2018=None,
        )

    @classmethod
    def _clear(cls) -> AffixFuzzer3:
        """Produce an empty AffixFuzzer3, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    @classmethod
    def from_fields(
        cls,
        *,
        clear_unset: bool = False,
        fuzz2001: datatypes.AffixFuzzer1Like | None = None,
        fuzz2002: datatypes.AffixFuzzer1Like | None = None,
        fuzz2003: datatypes.AffixFuzzer1Like | None = None,
        fuzz2004: datatypes.AffixFuzzer1Like | None = None,
        fuzz2005: datatypes.AffixFuzzer1Like | None = None,
        fuzz2006: datatypes.AffixFuzzer1Like | None = None,
        fuzz2007: components.AffixFuzzer7Like | None = None,
        fuzz2008: components.AffixFuzzer8Like | None = None,
        fuzz2009: components.AffixFuzzer9Like | None = None,
        fuzz2010: components.AffixFuzzer10Like | None = None,
        fuzz2011: components.AffixFuzzer11Like | None = None,
        fuzz2012: components.AffixFuzzer12Like | None = None,
        fuzz2013: components.AffixFuzzer13Like | None = None,
        fuzz2014: datatypes.AffixFuzzer3Like | None = None,
        fuzz2015: datatypes.AffixFuzzer3Like | None = None,
        fuzz2016: components.AffixFuzzer16Like | None = None,
        fuzz2017: components.AffixFuzzer17Like | None = None,
        fuzz2018: components.AffixFuzzer18Like | None = None,
    ) -> AffixFuzzer3:
        """Update only some specific fields of a `AffixFuzzer3`."""

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            kwargs = {
                "fuzz2001": fuzz2001,
                "fuzz2002": fuzz2002,
                "fuzz2003": fuzz2003,
                "fuzz2004": fuzz2004,
                "fuzz2005": fuzz2005,
                "fuzz2006": fuzz2006,
                "fuzz2007": fuzz2007,
                "fuzz2008": fuzz2008,
                "fuzz2009": fuzz2009,
                "fuzz2010": fuzz2010,
                "fuzz2011": fuzz2011,
                "fuzz2012": fuzz2012,
                "fuzz2013": fuzz2013,
                "fuzz2014": fuzz2014,
                "fuzz2015": fuzz2015,
                "fuzz2016": fuzz2016,
                "fuzz2017": fuzz2017,
                "fuzz2018": fuzz2018,
            }

            if clear_unset:
                kwargs = {k: v if v is not None else [] for k, v in kwargs.items()}  # type: ignore[misc]

            inst.__attrs_init__(**kwargs)
            return inst

        inst.__attrs_clear__()
        return inst

    @classmethod
    def cleared(cls) -> AffixFuzzer3:
        """Clear all the fields of a `AffixFuzzer3`."""
        return cls.from_fields(clear_unset=True)

    @classmethod
    def columns(
        cls,
        *,
        fuzz2001: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2002: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2003: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2004: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2005: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2006: datatypes.AffixFuzzer1ArrayLike | None = None,
        fuzz2007: components.AffixFuzzer7ArrayLike | None = None,
        fuzz2008: components.AffixFuzzer8ArrayLike | None = None,
        fuzz2009: components.AffixFuzzer9ArrayLike | None = None,
        fuzz2010: components.AffixFuzzer10ArrayLike | None = None,
        fuzz2011: components.AffixFuzzer11ArrayLike | None = None,
        fuzz2012: components.AffixFuzzer12ArrayLike | None = None,
        fuzz2013: components.AffixFuzzer13ArrayLike | None = None,
        fuzz2014: datatypes.AffixFuzzer3ArrayLike | None = None,
        fuzz2015: datatypes.AffixFuzzer3ArrayLike | None = None,
        fuzz2016: components.AffixFuzzer16ArrayLike | None = None,
        fuzz2017: components.AffixFuzzer17ArrayLike | None = None,
        fuzz2018: components.AffixFuzzer18ArrayLike | None = None,
    ) -> ComponentColumnList:
        """
        Construct a new column-oriented component bundle.

        This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.

        The returned columns will be partitioned into unit-length sub-batches by default.
        Use `ComponentColumnList.partition` to repartition the data as needed.
        """

        inst = cls.__new__(cls)
        with catch_and_log_exceptions(context=cls.__name__):
            inst.__attrs_init__(
                fuzz2001=fuzz2001,
                fuzz2002=fuzz2002,
                fuzz2003=fuzz2003,
                fuzz2004=fuzz2004,
                fuzz2005=fuzz2005,
                fuzz2006=fuzz2006,
                fuzz2007=fuzz2007,
                fuzz2008=fuzz2008,
                fuzz2009=fuzz2009,
                fuzz2010=fuzz2010,
                fuzz2011=fuzz2011,
                fuzz2012=fuzz2012,
                fuzz2013=fuzz2013,
                fuzz2014=fuzz2014,
                fuzz2015=fuzz2015,
                fuzz2016=fuzz2016,
                fuzz2017=fuzz2017,
                fuzz2018=fuzz2018,
            )

        batches = inst.as_component_batches()
        if len(batches) == 0:
            return ComponentColumnList([])

        kwargs = {
            "AffixFuzzer3:fuzz2001": fuzz2001,
            "AffixFuzzer3:fuzz2002": fuzz2002,
            "AffixFuzzer3:fuzz2003": fuzz2003,
            "AffixFuzzer3:fuzz2004": fuzz2004,
            "AffixFuzzer3:fuzz2005": fuzz2005,
            "AffixFuzzer3:fuzz2006": fuzz2006,
            "AffixFuzzer3:fuzz2007": fuzz2007,
            "AffixFuzzer3:fuzz2008": fuzz2008,
            "AffixFuzzer3:fuzz2009": fuzz2009,
            "AffixFuzzer3:fuzz2010": fuzz2010,
            "AffixFuzzer3:fuzz2011": fuzz2011,
            "AffixFuzzer3:fuzz2012": fuzz2012,
            "AffixFuzzer3:fuzz2013": fuzz2013,
            "AffixFuzzer3:fuzz2014": fuzz2014,
            "AffixFuzzer3:fuzz2015": fuzz2015,
            "AffixFuzzer3:fuzz2016": fuzz2016,
            "AffixFuzzer3:fuzz2017": fuzz2017,
            "AffixFuzzer3:fuzz2018": fuzz2018,
        }
        columns = []

        for batch in batches:
            arrow_array = batch.as_arrow_array()

            # For primitive arrays and fixed size list arrays, we infer partition size from the input shape.
            if pa.types.is_primitive(arrow_array.type) or pa.types.is_fixed_size_list(arrow_array.type):
                param = kwargs[batch.component_descriptor().component]  # type: ignore[index]
                shape = np.shape(param)  # type: ignore[arg-type]
                elem_flat_len = int(np.prod(shape[1:])) if len(shape) > 1 else 1  # type: ignore[redundant-expr,misc]

                if pa.types.is_fixed_size_list(arrow_array.type) and arrow_array.type.list_size == elem_flat_len:
                    # If the product of the last dimensions of the shape are equal to the size of the fixed size list array,
                    # we have `num_rows` single element batches (each element is a fixed sized list).
                    # (This should have been already validated by conversion to the arrow_array)
                    batch_length = 1
                else:
                    batch_length = shape[1] if len(shape) > 1 else 1  # type: ignore[redundant-expr,misc]

                num_rows = shape[0] if len(shape) >= 1 else 1  # type: ignore[redundant-expr,misc]
                sizes = batch_length * np.ones(num_rows)
            else:
                # For non-primitive types, default to partitioning each element separately.
                sizes = np.ones(len(arrow_array))

            columns.append(batch.partition(sizes))

        return ComponentColumnList(columns)

    fuzz2001: components.AffixFuzzer1Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer1Batch._converter,  # type: ignore[misc]
    )
    fuzz2002: components.AffixFuzzer2Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer2Batch._converter,  # type: ignore[misc]
    )
    fuzz2003: components.AffixFuzzer3Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer3Batch._converter,  # type: ignore[misc]
    )
    fuzz2004: components.AffixFuzzer4Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer4Batch._converter,  # type: ignore[misc]
    )
    fuzz2005: components.AffixFuzzer5Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer5Batch._converter,  # type: ignore[misc]
    )
    fuzz2006: components.AffixFuzzer6Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer6Batch._converter,  # type: ignore[misc]
    )
    fuzz2007: components.AffixFuzzer7Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer7Batch._converter,  # type: ignore[misc]
    )
    fuzz2008: components.AffixFuzzer8Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer8Batch._converter,  # type: ignore[misc]
    )
    fuzz2009: components.AffixFuzzer9Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer9Batch._converter,  # type: ignore[misc]
    )
    fuzz2010: components.AffixFuzzer10Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer10Batch._converter,  # type: ignore[misc]
    )
    fuzz2011: components.AffixFuzzer11Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer11Batch._converter,  # type: ignore[misc]
    )
    fuzz2012: components.AffixFuzzer12Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer12Batch._converter,  # type: ignore[misc]
    )
    fuzz2013: components.AffixFuzzer13Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer13Batch._converter,  # type: ignore[misc]
    )
    fuzz2014: components.AffixFuzzer14Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer14Batch._converter,  # type: ignore[misc]
    )
    fuzz2015: components.AffixFuzzer15Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer15Batch._converter,  # type: ignore[misc]
    )
    fuzz2016: components.AffixFuzzer16Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer16Batch._converter,  # type: ignore[misc]
    )
    fuzz2017: components.AffixFuzzer17Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer17Batch._converter,  # type: ignore[misc]
    )
    fuzz2018: components.AffixFuzzer18Batch | None = field(
        metadata={"component": True},
        default=None,
        converter=components.AffixFuzzer18Batch._converter,  # type: ignore[misc]
    )
    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
