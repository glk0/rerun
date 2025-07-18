# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/components/tensor_dimension_selection.fbs".

# You can extend this class by creating a "TensorHeightDimensionExt" class in "tensor_height_dimension_ext.py".

from __future__ import annotations

from .. import datatypes
from .._baseclasses import (
    ComponentBatchMixin,
    ComponentMixin,
)

__all__ = ["TensorHeightDimension", "TensorHeightDimensionBatch"]


class TensorHeightDimension(datatypes.TensorDimensionSelection, ComponentMixin):
    """**Component**: Specifies which dimension to use for height."""

    _BATCH_TYPE = None
    # You can define your own __init__ function as a member of TensorHeightDimensionExt in tensor_height_dimension_ext.py

    # Note: there are no fields here because TensorHeightDimension delegates to datatypes.TensorDimensionSelection


class TensorHeightDimensionBatch(datatypes.TensorDimensionSelectionBatch, ComponentBatchMixin):
    _COMPONENT_TYPE: str = "rerun.components.TensorHeightDimension"


# This is patched in late to avoid circular dependencies.
TensorHeightDimension._BATCH_TYPE = TensorHeightDimensionBatch  # type: ignore[assignment]
