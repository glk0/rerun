// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/archetypes/line_strips3d.fbs".

#include "line_strips3d.hpp"

#include "../collection_adapter_builtins.hpp"

namespace rerun::archetypes {
    LineStrips3D LineStrips3D::clear_fields() {
        auto archetype = LineStrips3D();
        archetype.strips = ComponentBatch::empty<rerun::components::LineStrip3D>(Descriptor_strips)
                               .value_or_throw();
        archetype.radii =
            ComponentBatch::empty<rerun::components::Radius>(Descriptor_radii).value_or_throw();
        archetype.colors =
            ComponentBatch::empty<rerun::components::Color>(Descriptor_colors).value_or_throw();
        archetype.labels =
            ComponentBatch::empty<rerun::components::Text>(Descriptor_labels).value_or_throw();
        archetype.show_labels =
            ComponentBatch::empty<rerun::components::ShowLabels>(Descriptor_show_labels)
                .value_or_throw();
        archetype.class_ids =
            ComponentBatch::empty<rerun::components::ClassId>(Descriptor_class_ids)
                .value_or_throw();
        return archetype;
    }

    Collection<ComponentColumn> LineStrips3D::columns(const Collection<uint32_t>& lengths_) {
        std::vector<ComponentColumn> columns;
        columns.reserve(6);
        if (strips.has_value()) {
            columns.push_back(strips.value().partitioned(lengths_).value_or_throw());
        }
        if (radii.has_value()) {
            columns.push_back(radii.value().partitioned(lengths_).value_or_throw());
        }
        if (colors.has_value()) {
            columns.push_back(colors.value().partitioned(lengths_).value_or_throw());
        }
        if (labels.has_value()) {
            columns.push_back(labels.value().partitioned(lengths_).value_or_throw());
        }
        if (show_labels.has_value()) {
            columns.push_back(show_labels.value().partitioned(lengths_).value_or_throw());
        }
        if (class_ids.has_value()) {
            columns.push_back(class_ids.value().partitioned(lengths_).value_or_throw());
        }
        return columns;
    }

    Collection<ComponentColumn> LineStrips3D::columns() {
        if (strips.has_value()) {
            return columns(std::vector<uint32_t>(strips.value().length(), 1));
        }
        if (radii.has_value()) {
            return columns(std::vector<uint32_t>(radii.value().length(), 1));
        }
        if (colors.has_value()) {
            return columns(std::vector<uint32_t>(colors.value().length(), 1));
        }
        if (labels.has_value()) {
            return columns(std::vector<uint32_t>(labels.value().length(), 1));
        }
        if (show_labels.has_value()) {
            return columns(std::vector<uint32_t>(show_labels.value().length(), 1));
        }
        if (class_ids.has_value()) {
            return columns(std::vector<uint32_t>(class_ids.value().length(), 1));
        }
        return Collection<ComponentColumn>();
    }
} // namespace rerun::archetypes

namespace rerun {

    Result<Collection<ComponentBatch>> AsComponents<archetypes::LineStrips3D>::as_batches(
        const archetypes::LineStrips3D& archetype
    ) {
        using namespace archetypes;
        std::vector<ComponentBatch> cells;
        cells.reserve(6);

        if (archetype.strips.has_value()) {
            cells.push_back(archetype.strips.value());
        }
        if (archetype.radii.has_value()) {
            cells.push_back(archetype.radii.value());
        }
        if (archetype.colors.has_value()) {
            cells.push_back(archetype.colors.value());
        }
        if (archetype.labels.has_value()) {
            cells.push_back(archetype.labels.value());
        }
        if (archetype.show_labels.has_value()) {
            cells.push_back(archetype.show_labels.value());
        }
        if (archetype.class_ids.has_value()) {
            cells.push_back(archetype.class_ids.value());
        }

        return rerun::take_ownership(std::move(cells));
    }
} // namespace rerun
