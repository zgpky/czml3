from __future__ import annotations

import datetime as dt
from typing import Any

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_serializer,
    model_validator,
)
from w3lib.url import is_url, parse_data_uri

from .base import BaseCZMLObject
from .common import Deletable, Interpolatable
from .enums import (
    ArcTypes,
    ClassificationTypes,
    ClockRanges,
    ClockSteps,
    ColorBlendModes,
    CornerTypes,
    HeightReferences,
    HorizontalOrigins,
    LabelStyles,
    ShadowModes,
    StripeOrientations,
    VerticalOrigins,
)
from .types import (
    Cartesian2Value,
    Cartesian3ListOfListsValue,
    Cartesian3ListValue,
    Cartesian3Value,
    Cartesian3VelocityValue,
    CartographicDegreesListOfListsValue,
    CartographicDegreesListValue,
    CartographicDegreesValue,
    CartographicRadiansListOfListsValue,
    CartographicRadiansListValue,
    CartographicRadiansValue,
    DistanceDisplayConditionValue,
    NearFarScalarValue,
    ReferenceListOfListsValue,
    ReferenceListValue,
    ReferenceValue,
    RgbafValue,
    RgbaValue,
    TimeInterval,
    TimeIntervalCollection,
    UnitQuaternionValue,
    format_datetime_like,
)


class HasAlignment(BaseModel):
    """A property that can be horizontally or vertically aligned."""

    horizontalOrigin: None | HorizontalOrigins | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HorizontalOrigins>`__ for it's definition.",
    )
    verticalOrigin: None | VerticalOrigins | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/VerticalOrigins>`__ for it's definition.",
    )


class Material(BaseCZMLObject):
    """A definition of how a surface is colored or shaded.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.
    """

    solidColor: None | SolidColorMaterial | str | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the surface with a solid color, which may be translucent. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/SolidColorMaterial>`__ for it's definition.",
    )
    image: None | ImageMaterial | str | Uri | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the surface with an image. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ImageMaterial>`__ for it's definition.",
    )
    grid: None | GridMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the surface with a grid. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/GridMaterial>`__ for it's definition.",
    )
    stripe: None | StripeMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the surface with alternating colors. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/StripeMaterial>`__ for it's definition.",
    )
    checkerboard: None | CheckerboardMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the surface with a checkerboard pattern. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CheckerboardMaterial>`__ for it's definition.",
    )
    polylineOutline: (
        None | PolylineMaterial | PolylineOutline | TimeIntervalCollection
    ) = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineMaterial>`__ for it's definition.",
    )  # NOTE: Not present in documentation


class PolylineOutline(BaseCZMLObject):
    """A definition of how a surface is colored or shaded.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineOutlineMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the surface. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the surface outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description="The width of the outline."
    )


class PolylineOutlineMaterial(BaseCZMLObject):
    """A definition of the material wrapper for a polyline outline.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineOutlineMaterial>`__ for it's definition."""

    polylineOutline: None | PolylineOutline | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineOutline>`__ for it's definition.",
    )


class PolylineGlow(BaseCZMLObject):
    """A definition of how a glowing polyline appears.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineGlowMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    glowPower: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    taperPower: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )


class PolylineGlowMaterial(BaseCZMLObject):
    """A material that fills the surface of a line with a glowing color.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineGlowMaterial>`__ for it's definition."""

    polylineGlow: None | PolylineGlow | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineGlow>`__ for it's definition.",
    )


class PolylineArrow(BaseCZMLObject):
    """A definition of how a polyline arrow appears.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineArrowMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the surface. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )


class PolylineArrowMaterial(BaseCZMLObject):
    """A material that fills the surface of a line with an arrow.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineArrowMaterial>`__ for it's definition."""

    polylineArrow: None | PolylineArrow | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineArrow>`__ for it's definition.",
    )


class PolylineDash(BaseCZMLObject):
    """A definition of how a polyline should be dashed with two colors.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineDashMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the dashes on the line. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    gapColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the gaps between dashes on the line. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    dashLength: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The length in screen-space pixels of a single dash and gap pattern. ",
    )
    dashPattern: None | int | TimeIntervalCollection = Field(
        default=None,
        description="A 16-bit bitfield representing which portions along a single dashLength are the dash (1) and which are the gap (0). The default value, 255 (0000000011111111), indicates 50% gap followed by 50% dash.",
    )


class PolylineDashMaterial(BaseCZMLObject):
    """A material that provides a how a polyline should be dashed.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineDashMaterial>`__ for it's definition."""

    polylineDash: None | PolylineDash | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineDash>`__ for it's definition.",
    )


class PolylineMaterial(BaseCZMLObject):
    """A definition of how a surface is colored or shaded.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineMaterial>`__ for it's definition."""

    solidColor: None | SolidColorMaterial | str | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a solid color, which may be translucent. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/SolidColorMaterial>`__ for it's definition.",
    )
    image: None | ImageMaterial | str | Uri | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with an image. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ImageMaterial>`__ for it's definition.",
    )
    grid: None | GridMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a grid. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/GridMaterial>`__ for it's definition.",
    )
    stripe: None | StripeMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with alternating colors. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/StripeMaterial>`__ for it's definition.",
    )
    checkerboard: None | CheckerboardMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a checkerboard pattern. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CheckerboardMaterial>`__ for it's definition.",
    )
    polylineDash: None | PolylineDashMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a pattern of dashes. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineDashMaterial>`__ for it's definition.",
    )
    polylineOutline: None | PolylineOutlineMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a color and outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineOutlineMaterial>`__ for it's definition.",
    )
    polylineArrow: None | PolylineArrowMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with an arrow. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineArrowMaterial>`__ for it's definition.",
    )
    polylineGlow: None | PolylineGlowMaterial | TimeIntervalCollection = Field(
        default=None,
        description="A material that fills the line with a glowing color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PolylineGlowMaterial>`__ for it's definition.",
    )


class SolidColorMaterial(BaseCZMLObject):
    """A material that fills the surface with a solid color.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/SolidColorMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the surface. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )


class GridMaterial(BaseCZMLObject):
    """A material that fills the surface with a two-dimensional grid.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/GridMaterial>`__ for it's definition."""

    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the surface. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    cellAlpha: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The alpha value for the space between grid lines. This will be combined with the color alpha.",
    )
    lineCount: None | list[int] | TimeIntervalCollection = Field(
        default=None,
        description="The number of grid lines along each axis. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/LineCount>`__ for it's definition.",
    )
    lineThickness: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The thickness of grid lines along each axis, in pixels. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/LineThickness>`__ for it's definition.",
    )
    lineOffset: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The offset of grid lines along each axis, as a percentage from 0 to 1. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/LineOffset>`__ for it's definition.",
    )


class StripeMaterial(BaseCZMLObject):
    """A material that fills the surface with alternating colors.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/StripeMaterial>`__ for it's definition."""

    orientation: None | StripeOrientations | str | TimeIntervalCollection = Field(
        default=None,
        description="The value indicating if the stripes are horizontal or vertical. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/StripeOrientations>`__ for it's definition.",
    )
    evenColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The even color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    oddColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The odd color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    offset: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The value indicating where in the pattern to begin drawing, with 0.0 being the beginning of the even color, 1.0 the beginning of the odd color, 2.0 being the even color again, and any multiple or fractional values being in between.",
    )
    repeat: None | float | TimeIntervalCollection = Field(
        default=None, description="The number of times the stripes repeat."
    )


class CheckerboardMaterial(BaseCZMLObject):
    """A material that fills the surface with alternating colors.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CheckerboardMaterial>`__ for it's definition."""

    evenColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The even color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    oddColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The odd color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    repeat: None | list[int] | TimeIntervalCollection = Field(
        default=None,
        description="The number of times the tiles repeat along each axis.",
    )


class ImageMaterial(BaseCZMLObject):
    """A material that fills the surface with an image.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ImageMaterial>`__ for it's definition."""

    image: None | Uri | TimeIntervalCollection = Field(
        default=None,
        description="The image to display on the surface. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ImageMaterial>`__ for it's definition.",
    )
    repeat: None | list[int] | TimeIntervalCollection = Field(
        default=None,
        description="The number of times the image repeats along each axis. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Repeat>`__ for it's definition.",
    )
    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the image. This color value is multiplied with the image to produce the final color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    transparent: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the image has transparency."
    )


class Color(BaseCZMLObject, Interpolatable, Deletable):
    """A color. The color can optionally vary over time.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition."""

    rgba: None | RgbaValue | str | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The color specified as an array of color components [Red, Green, Blue, Alpha] where each component is an integer in the range 0-255. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/RgbaValue>`__ for it's definition.",
    )
    rgbaf: None | RgbafValue | str | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The color specified as an array of color components [Red, Green, Blue, Alpha] where each component is a double in the range 0.0-1.0. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/RgbafValue>`__ for it's definition.",
    )
    reference: None | ReferenceValue = Field(
        default=None,
        description="The color specified as a reference to another property. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ReferenceValue>`__ for it's definition.",
    )

    @field_validator("rgba")
    @classmethod
    def validate_rgba(cls, c):
        if isinstance(c, list):
            return RgbaValue(values=c)
        return c

    @field_validator("rgbaf")
    @classmethod
    def validate_rgbaf(cls, c):
        if isinstance(c, list):
            return RgbafValue(values=c)
        return c


class Position(BaseCZMLObject, Interpolatable, Deletable):
    """Defines a position. The position can optionally vary over time.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Position>`__ for it's definition."""

    referenceFrame: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    cartesian: None | Cartesian3Value | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cartesian3Value>`__ for it's definition.",
    )
    cartographicRadians: (
        None | CartographicRadiansValue | list[float] | TimeIntervalCollection
    ) = Field(default=None, description="")
    cartographicDegrees: (
        None | CartographicDegreesValue | list[float] | TimeIntervalCollection
    ) = Field(default=None, description="")
    cartesianVelocity: (
        None | Cartesian3VelocityValue | list[float] | TimeIntervalCollection
    ) = Field(default=None, description="")
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    interval: None | TimeInterval | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/TimeInterval>`__ for it's definition.",
    )
    epoch: None | str | dt.datetime | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @model_validator(mode="after")
    def checks(self):
        if self.delete:
            return self
        if (
            sum(
                val is not None
                for val in (
                    self.cartesian,
                    self.cartographicDegrees,
                    self.cartographicRadians,
                    self.cartesianVelocity,
                )
            )
            != 1
        ):
            raise TypeError(
                "One of cartesian, cartographicDegrees, cartographicRadians or reference must be given"
            )
        return self

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3Value(values=r)
        return r

    @field_validator("cartographicRadians")
    @classmethod
    def validate_cartographicRadians(cls, r):
        if isinstance(r, list):
            return CartographicRadiansValue(values=r)
        return r

    @field_validator("cartographicDegrees")
    @classmethod
    def validate_cartographicDegrees(cls, r):
        if isinstance(r, list):
            return CartographicDegreesValue(values=r)
        return r

    @field_validator("cartesianVelocity")
    @classmethod
    def validate_cartesianVelocity(cls, r):
        if isinstance(r, list):
            return Cartesian3VelocityValue(values=r)
        return r

    @field_validator("epoch")
    @classmethod
    def validate_epoch(cls, e):
        return format_datetime_like(e)


class ViewFrom(BaseCZMLObject, Interpolatable, Deletable):
    """A suggested initial camera position offset when tracking this object, specified as a Cartesian position. Typically defined in the East (x), North (y), Up (z) reference frame relative to the object's position, but may use another frame depending on the object's velocity.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ViewFrom>`__ for it's definition."""

    cartesian: None | Cartesian3Value | list[float] | TimeIntervalCollection = Field(
        description="The offset specified as a three-dimensional Cartesian value [X, Y, Z].  See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cartesian3Value>`__ for it's definition."
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description="The offset specified as a reference to another property. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ReferenceValue>`__ for it's definition.",
    )

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3Value(values=r)
        return r

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Billboard(BaseCZMLObject, HasAlignment):
    """A billboard, or viewport-aligned image. The billboard is positioned in the scene by the position property. A billboard is sometimes called a marker.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Billboard>`__ for it's definition."""

    image: str | Uri | TimeIntervalCollection = Field(
        description="The URI of the image displayed on the billboard. For broadest client compatibility, the URI should be accessible via Cross-Origin Resource Sharing (CORS). The URI may also be a data URI. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Uri>`__ for it's definition."
    )
    show: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the billboard is shown."
    )
    scale: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The scale of the billboard. The scale is multiplied with the pixel size of the billboard's image. For example, if the scale is 2.0, the billboard will be rendered with twice the number of pixels, in each direction, of the image.",
    )
    pixelOffset: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The offset, in viewport pixels, of the billboard origin from the position. A pixel offset is the number of pixels up and to the right to place the billboard, relative to the position. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PixelOffset>`__ for it's definition.",
    )
    eyeOffset: None | EyeOffset | list[float] | TimeIntervalCollection = Field(
        default=None,
        description="The eye offset of the billboard, which is the offset in eye coordinates at which to place the billboard relative to the position property. Eye coordinates are a left-handed coordinate system where the X-axis points toward the viewer's right, the Y-axis points up, and the Z-axis points into the screen. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/EyeOffset>`__ for it's definition.",
    )
    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the billboard. This color value is multiplied with the values of the billboard's image to produce the final color. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )

    @field_validator("eyeOffset")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, list):
            return EyeOffset(cartesian=r)
        return r


class EllipsoidRadii(BaseCZMLObject, Interpolatable, Deletable):
    """The radii of an ellipsoid.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/EllipsoidRadii>`__ for it's definition."""

    cartesian: Cartesian3Value | list[float] | TimeIntervalCollection = Field(
        description="The radii specified as a three-dimensional Cartesian value [X, Y, Z], in world coordinates in meters. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cartesian3Value>`__ for it's definition."
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ReferenceValue>`__ for it's definition.",
    )

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3Value(values=r)
        return r

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Corridor(BaseCZMLObject):
    """A corridor , which is a shape defined by a centerline and width that conforms to the curvature of the body shape. It can can optionally be extruded into a volume.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Corridor>`__ for it's definition."""

    positions: PositionList | TimeIntervalCollection = Field(
        description="The array of positions defining the centerline of the corridor. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PositionList>`__ for it's definition."
    )
    show: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the corridor is shown."
    )
    width: float = Field(
        description="The width of the corridor, which is the distance between the edges of the corridor."
    )
    height: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The height of the corridor, which is the altitude of the corridor relative to the surface.",
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The height reference of the corridor, which indicates if height is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    extrudedHeight: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The extruded height of the corridor, which is the altitude of the corridor's extruded face relative to the surface.",
    )
    extrudedHeightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The extruded height reference of the corridor, which indicates if extrudedHeight is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    cornerType: None | CornerType | TimeIntervalCollection = Field(
        default=None,
        description="The style of the corners of the corridor. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CornerType>`__ for it's definition.",
    )
    granularity: None | float | TimeIntervalCollection = Field(
        default=None, description="The sampling distance, in radians."
    )
    fill: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the corridor is filled."
    )
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description="The material to display on the surface of the corridor. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(
        default=None,
        description="Whether or not the corridor is outlined. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the corridor outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description="The width of the corridor outline."
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description="Whether or not the corridor casts or receives shadows. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(
        default=None,
        description="The display condition specifying the distance from the camera at which this corridor will be displayed. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/DistanceDisplayCondition>`__ for it's definition.",
    )
    classificationType: None | ClassificationType | TimeIntervalCollection = Field(
        default=None,
        description="Whether a classification affects terrain, 3D Tiles, or both. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationType>`__ for it's definition.",
    )
    zIndex: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The z-index of the corridor, used for ordering ground geometry. Only has an effect if the corridor is constant, and height and extrudedHeight are not specified.",
    )


class Cylinder(BaseCZMLObject):
    """A cylinder, which is a special cone defined by length, top and bottom radius.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cylinder>`__ for it's definition."""

    length: float | TimeIntervalCollection = Field(
        description="The length of the cylinder."
    )
    show: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the cylinder is shown."
    )
    topRadius: float | TimeIntervalCollection = Field(
        description="The radius of the top of the cylinder."
    )
    bottomRadius: float | TimeIntervalCollection = Field(
        description="The radius of the bottom of the cylinder."
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The height reference of the cylinder, which indicates if the position is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    fill: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the cylinder is filled."
    )
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description="The material to display on the surface of the cylinder. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the cylinder is outlined."
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the cylinder outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description="The width of the cylinder outline."
    )
    numberOfVerticalLines: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The number of vertical lines to draw along the perimeter for the outline.",
    )
    slices: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The number of edges around the perimeter of the cylinder.",
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description="Whether or not the cylinder casts or receives shadows. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(
        default=None,
        description="The display condition specifying the distance from the camera at which this cylinder will be displayed. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/DistanceDisplayCondition>`__ for it's definition.",
    )


class Ellipse(BaseCZMLObject):
    """An ellipse, which is a close curve, on or above Earth's surface.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Ellipse>`__ for it's definition."""

    semiMajorAxis: float | TimeIntervalCollection = Field(
        description="The length of the ellipse's semi-major axis in meters."
    )
    semiMinorAxis: float | TimeIntervalCollection = Field(
        description="The length of the ellipse's semi-minor axis in meters."
    )
    show: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the ellipse is shown."
    )
    height: None | float | TimeIntervalCollection = Field(
        default=None, description="The altitude of the ellipse relative to the surface."
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The height reference of the ellipse, which indicates if height is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    extrudedHeight: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The altitude of the ellipse's extruded face relative to the surface.",
    )
    extrudedHeightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The extruded height reference of the ellipse, which indicates if extrudedHeight is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    rotation: None | float | TimeIntervalCollection = Field(
        default=None, description="The angle from north (counter-clockwise) in radians."
    )
    stRotation: None | float | TimeIntervalCollection = Field(
        default=None, description="The rotation of any applied texture coordinates."
    )
    granularity: None | float | TimeIntervalCollection = Field(
        default=None, description="The sampling distance, in radians."
    )
    fill: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the ellipse is filled."
    )
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description="The material to use to fill the ellipse. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the ellipse is outlined."
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the ellipse outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description="The width of the ellipse outline."
    )
    numberOfVerticalLines: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The number of vertical lines to use when outlining an extruded ellipse.",
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description="Whether or not the ellipse casts or receives shadows. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(
        default=None,
        description="The display condition specifying at what distance from the camera this ellipse will be displayed. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/DistanceDisplayCondition>`__ for it's definition.",
    )
    classificationType: None | ClassificationType | TimeIntervalCollection = Field(
        default=None,
        description="Whether a classification affects terrain, 3D Tiles, or both. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationType>`__ for it's definition.",
    )
    zIndex: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The z-index of the ellipse, used for ordering ground geometry. Only has an effect if the ellipse is constant, and height and extrudedHeight are not specified.",
    )


class Polygon(BaseCZMLObject):
    """A polygon, which is a closed figure on the surface of the Earth.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Polygon>`__ for it's definition."""

    positions: PositionList | TimeIntervalCollection = Field(
        description="The array of positions defining a simple polygon. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PositionList>`__ for it's definition."
    )
    show: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the polygon is shown."
    )
    arcType: None | ArcType | TimeIntervalCollection = Field(
        default=None,
        description="The type of arc that should connect the positions of the polygon. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ArcType>`__ for it's definition.",
    )
    granularity: None | float | TimeIntervalCollection = Field(
        default=None, description="The sampling distance, in radians."
    )
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description="The material to use to fill the polygon. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description="Whether or not the polygon casts or receives shadows. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(
        default=None,
        description="The display condition specifying the distance from the camera at which this polygon will be displayed. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/DistanceDisplayCondition>`__ for it's definition.",
    )
    classificationType: None | ClassificationType | TimeIntervalCollection = Field(
        default=None,
        description="Whether a classification affects terrain, 3D Tiles, or both. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationType>`__ for it's definition.",
    )
    zIndex: None | int | TimeIntervalCollection = Field(
        default=None,
        description="The z-index of the polygon, used for ordering ground geometry. Only has an effect if the polygon is constant, and height and extrudedHeight are not specified.",
    )
    holes: None | PositionListOfLists | TimeIntervalCollection = Field(
        default=None,
        description="The array of arrays of positions defining holes in the polygon. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PositionListOfLists>`__ for it's definition.",
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description="The color of the polygon outline. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the polygon is outlined."
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description="The width of the polygon outline."
    )
    extrudedHeight: None | float | TimeIntervalCollection = Field(
        default=None, description="The extruded height of the polygon."
    )
    extrudedHeightReference: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The extruded height reference of the polygon, which indicates if extrudedHeight is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    perPositionHeight: None | bool | TimeIntervalCollection = Field(
        default=None,
        description="Whether to use the height of each position to define the polygon or to use height as a constant height above the surface.",
    )
    height: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The height of the polygon when perPositionHeight is false.",
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description="The height reference of the polygon, which indicates if height is relative to terrain or not. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    stRotation: None | float | TimeIntervalCollection = Field(
        default=None,
        description="The rotation of any applied texture. A positive rotation is counter-clockwise.",
    )
    fill: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether or not the polygon is filled."
    )
    closeTop: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether to close the top of the polygon."
    )
    closeBottom: None | bool | TimeIntervalCollection = Field(
        default=None, description="Whether to close the bottom of the polygon."
    )


class Polyline(BaseCZMLObject):
    """A polyline, which is a line in the scene composed of multiple segments.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Polyline>`__ for it's definition."""

    positions: PositionList | TimeIntervalCollection
    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    arcType: None | ArcType | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ArcType>`__ for it's definition.",
    )
    width: None | float | TimeIntervalCollection = Field(default=None, description="")
    granularity: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    material: (
        None
        | PolylineMaterial
        | PolylineDashMaterial
        | PolylineArrowMaterial
        | PolylineGlowMaterial
        | PolylineOutlineMaterial
        | str
    ) | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Field>`__ for it's definition.",
    )
    followSurface: None | bool | TimeIntervalCollection = Field(
        default=None, description=""
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    depthFailMaterial: (
        None
        | PolylineMaterial
        | PolylineDashMaterial
        | PolylineArrowMaterial
        | PolylineGlowMaterial
        | PolylineOutlineMaterial
        | str
    ) | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Field>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")
    clampToGround: None | bool | TimeIntervalCollection = Field(
        default=None, description=""
    )
    classificationType: None | ClassificationType | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationType>`__ for it's definition.",
    )
    zIndex: None | int | TimeIntervalCollection = Field(default=None, description="")


class ArcType(BaseCZMLObject, Deletable):
    """The type of an arc.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ArcType>`__ for it's definition."""

    arcType: None | ArcTypes | str | TimeIntervalCollection = Field(
        default=None,
        description="The arc type. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ArcTypes>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description="The arc type specified as a reference to another property. See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class ShadowMode(BaseCZMLObject, Deletable):
    """Whether or not an object casts or receives shadows from each light source when shadows are enabled.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition."""

    shadowMode: None | ShadowModes | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowModes>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class ClassificationType(BaseCZMLObject, Deletable):
    """Whether a classification affects terrain, 3D Tiles, or both.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationType>`__ for it's definition."""

    classificationType: None | ClassificationTypes | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClassificationTypes>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class DistanceDisplayCondition(BaseCZMLObject, Interpolatable, Deletable):
    """Indicates the visibility of an object based on the distance to the camera.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/DistanceDisplayCondition>`__ for it's definition."""

    distanceDisplayCondition: (
        None | DistanceDisplayConditionValue | TimeIntervalCollection
    ) = Field(default=None, description="")
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class PositionListOfLists(BaseCZMLObject, Deletable):
    """A list of positions.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PositionListOfLists>`__ for it's definition."""

    referenceFrame: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    cartesian: (
        None | Cartesian3ListOfListsValue | list[list[float]] | TimeIntervalCollection
    ) = Field(default=None, description="")
    cartographicRadians: (
        None
        | CartographicRadiansListOfListsValue
        | list[list[float]]
        | TimeIntervalCollection
    ) = Field(default=None, description="")
    cartographicDegrees: (
        None
        | CartographicDegreesListOfListsValue
        | list[list[float]]
        | TimeIntervalCollection
    ) = Field(default=None, description="")
    references: (
        None | ReferenceListOfListsValue | list[list[str]] | TimeIntervalCollection
    ) = Field(default=None, description="")

    @model_validator(mode="after")
    def checks(self):
        if self.delete:
            return self
        if (
            sum(
                val is not None
                for val in (
                    self.cartesian,
                    self.cartographicDegrees,
                    self.cartographicRadians,
                )
            )
            != 1
        ):
            raise TypeError(
                "One of cartesian, cartographicDegrees, cartographicRadians or reference must be given"
            )
        if isinstance(self.references, ReferenceListOfListsValue):
            if isinstance(self.cartesian, Cartesian3ListOfListsValue):
                v = self.cartesian.values
            elif isinstance(
                self.cartographicDegrees, CartographicDegreesListOfListsValue
            ):
                v = self.cartographicDegrees.values
            elif isinstance(
                self.cartographicRadians, CartographicRadiansListOfListsValue
            ):
                v = self.cartographicRadians.values
            else:
                raise TypeError
            if len(self.references.values) != len(v):
                raise TypeError("Number of references must equal number of coordinates")
            for r, v1 in zip(self.references.values, v, strict=False):
                if len(r) != len(v1) // 3:
                    raise TypeError(
                        "Number of references must equal number of coordinates in each list"
                    )

        return self

    @field_validator("references")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, list):
            return ReferenceListOfListsValue(values=r)
        return r

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3ListOfListsValue(values=r)
        return r

    @field_validator("cartographicRadians")
    @classmethod
    def validate_cartographicRadians(cls, r):
        if isinstance(r, list):
            return CartographicRadiansListOfListsValue(values=r)
        return r

    @field_validator("cartographicDegrees")
    @classmethod
    def validate_cartographicDegrees(cls, r):
        if isinstance(r, list):
            return CartographicDegreesListOfListsValue(values=r)
        return r


class PositionList(BaseCZMLObject, Interpolatable, Deletable):
    """A list of positions.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/PositionList>`__ for it's definition."""

    referenceFrame: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    cartesian: None | Cartesian3ListValue | list[float] | TimeIntervalCollection = (
        Field(default=None, description="")
    )
    cartographicRadians: (
        None | CartographicRadiansListValue | list[float] | TimeIntervalCollection
    ) = Field(default=None, description="")
    cartographicDegrees: (
        None | CartographicDegreesListValue | list[float] | TimeIntervalCollection
    ) = Field(default=None, description="")
    references: None | ReferenceListValue | list[str] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ReferenceListValue>`__ for it's definition.",
    )
    interval: None | TimeInterval | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/TimeInterval>`__ for it's definition.",
    )
    epoch: None | str | dt.datetime | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )  # note: not documented

    @model_validator(mode="after")
    def checks(self):
        if self.delete:
            return self
        if (
            sum(
                val is not None
                for val in (
                    self.cartesian,
                    self.cartographicDegrees,
                    self.cartographicRadians,
                )
            )
            != 1
        ):
            raise TypeError(
                "One of cartesian, cartographicDegrees, cartographicRadians or reference must be given"
            )
        if isinstance(self.references, ReferenceListValue):
            if isinstance(self.cartesian, Cartesian3ListValue):
                v = self.cartesian.values
            elif isinstance(self.cartographicDegrees, CartographicDegreesListValue):
                v = self.cartographicDegrees.values
            elif isinstance(self.cartographicRadians, CartographicRadiansListValue):
                v = self.cartographicRadians.values
            else:
                raise TypeError
            if len(self.references.values) != len(v) // 3:
                raise TypeError("Number of references must equal number of coordinates")
        return self

    @field_validator("references")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, list):
            return ReferenceListValue(values=r)
        return r

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3ListValue(values=r)
        return r

    @field_validator("cartographicRadians")
    @classmethod
    def validate_cartographicRadians(cls, r):
        if isinstance(r, list):
            return CartographicRadiansListValue(values=r)
        return r

    @field_validator("cartographicDegrees")
    @classmethod
    def validate_cartographicDegrees(cls, r):
        if isinstance(r, list):
            return CartographicDegreesListValue(values=r)
        return r

    @field_validator("epoch")
    @classmethod
    def check(cls, e):
        return format_datetime_like(e)


class Ellipsoid(BaseCZMLObject):
    """A closed quadric surface that is a three-dimensional analogue of an ellipse.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Ellipsoid>`__ for it's definition."""

    radii: EllipsoidRadii | TimeIntervalCollection
    innerRadii: None | EllipsoidRadii | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/EllipsoidRadii>`__ for it's definition.",
    )
    minimumClock: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    maximumClock: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    minimumCone: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    maximumCone: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    fill: None | bool | TimeIntervalCollection = Field(default=None, description="")
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(default=None, description="")
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    stackPartitions: None | int | TimeIntervalCollection = Field(
        default=None, description=""
    )
    slicePartitions: None | int | TimeIntervalCollection = Field(
        default=None, description=""
    )
    subdivisions: None | int | TimeIntervalCollection = Field(
        default=None, description=""
    )


class Box(BaseCZMLObject):
    """A box, which is a closed rectangular cuboid.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Box>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    dimensions: None | BoxDimensions | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/BoxDimensions>`__ for it's definition.",
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    fill: None | bool | TimeIntervalCollection = Field(default=None, description="")
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(default=None, description="")
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")


class BoxDimensions(BaseCZMLObject, Interpolatable):
    """The width, depth, and height of a box.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/BoxDimensions>`__ for it's definition."""

    cartesian: None | Cartesian3Value | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cartesian3Value>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3Value(values=r)
        return r

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Rectangle(BaseCZMLObject, Interpolatable, Deletable):
    """A cartographic rectangle, which conforms to the curvature of the globe and can be placed on the surface or at altitude and can optionally be extruded into a volume.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Rectangle>`__ for it's definition."""

    coordinates: None | RectangleCoordinates | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/RectangleCoordinates>`__ for it's definition.",
    )
    fill: None | bool | TimeIntervalCollection = Field(default=None, description="")
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )


class RectangleCoordinates(BaseCZMLObject, Interpolatable, Deletable):
    """A set of coordinates describing a cartographic rectangle on the surface of the ellipsoid.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/RectangleCoordinates>`__ for it's definition."""

    wsen: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/list>`__ for it's definition.",
    )
    wsenDegrees: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/list>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @model_validator(mode="after")
    def checks(self):
        if self.delete:
            return self
        if sum(val is not None for val in (self.wsen, self.wsenDegrees)) != 1:
            raise TypeError("One of wsen or wsenDegrees must be given")
        return self

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class EyeOffset(BaseCZMLObject, Deletable):
    """An offset in eye coordinates which can optionally vary over time. Eye coordinates are a left-handed coordinate system where the X-axis points toward the viewer's right, the Y-axis poitns up, and the Z-axis points into the screen.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/EyeOffset>`__ for it's definition."""

    cartesian: None | Cartesian3Value | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Cartesian3Value>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("cartesian")
    @classmethod
    def validate_cartesian(cls, r):
        if isinstance(r, list):
            return Cartesian3Value(values=r)
        return r

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class HeightReference(BaseCZMLObject, Deletable):
    """The height reference of an object, which indicates if the object's position is relative to terrain or not.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition."""

    heightReference: None | HeightReferences | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReferences>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class ColorBlendMode(BaseCZMLObject, Deletable):
    """The height reference of an object, which indicates if the object's position is relative to terrain or not.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ColorBlendMode>`__ for it's definition."""

    colorBlendMode: None | ColorBlendModes | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ColorBlendModes>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class CornerType(BaseCZMLObject, Deletable):
    """The height reference of an object, which indicates if the object's position is relative to terrain or not.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CornerType>`__ for it's definition."""

    cornerType: None | CornerTypes | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CornerTypes>`__ for it's definition.",
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Clock(BaseCZMLObject):
    """Initial settings for a simulated clock when a document is loaded. The start and stop time are configured using the interval property.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Clock>`__ for it's definition."""

    currentTime: None | str | dt.datetime | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    multiplier: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    range: None | ClockRanges | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClockRanges>`__ for it's definition.",
    )
    step: None | ClockSteps | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ClockSteps>`__ for it's definition.",
    )

    @field_validator("currentTime")
    @classmethod
    def format_time(cls, time):
        return format_datetime_like(time)


class Path(BaseCZMLObject):
    """A path, which is a polyline defined by the motion of an object over time. The possible vertices of the path are specified by the position property. Note that because clients cannot render a truly infinite path, the path must be limited, either by defining availability for this object, or by using the leadTime and trailTime properties.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Path>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    leadTime: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    trailTime: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    width: None | float | TimeIntervalCollection = Field(default=None, description="")
    resolution: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")


class Point(BaseCZMLObject):
    """A point, or viewport-aligned circle.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Point>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    pixelSize: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    scaleByDistance: None | NearFarScalar | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/NearFarScalar>`__ for it's definition.",
    )
    translucencyByDistance: None | NearFarScalar | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/NearFarScalar>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")
    disableDepthTestDistance: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )


class Tileset(BaseCZMLObject):
    """A 3D Tiles tileset.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Tileset>`__ for it's definition."""

    uri: str | Uri | TimeIntervalCollection
    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    maximumScreenSpaceError: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )


class Wall(BaseCZMLObject):
    """A two-dimensional wall defined as a line strip and optional maximum and minimum heights. It conforms to the curvature of the globe and can be placed along the surface or at altitude.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Wall>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    positions: PositionList | TimeIntervalCollection
    minimumHeights: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/list>`__ for it's definition.",
    )
    maximumHeights: None | list[float] | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/list>`__ for it's definition.",
    )
    granularity: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    fill: None | bool | TimeIntervalCollection = Field(default=None, description="")
    material: None | Material | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Material>`__ for it's definition.",
    )
    outline: None | bool | TimeIntervalCollection = Field(default=None, description="")
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")


class NearFarScalar(BaseCZMLObject, Interpolatable, Deletable):
    """A numeric value which will be linearly interpolated between two values based on an object's distance from the camera, in eye coordinates. The computed value will interpolate between the near value and the far value while the camera distance falls between the near distance and the far distance, and will be clamped to the near or far value while the distance is less than the near distance or greater than the far distance, respectively.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/NearFarScalar>`__ for it's definition."""

    nearFarScalar: None | list[float] | NearFarScalarValue | TimeIntervalCollection = (
        Field(default=None, description="")
    )
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Label(BaseCZMLObject, HasAlignment):
    """A string of text.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Label>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    text: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    font: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    style: None | LabelStyles | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/LabelStyles>`__ for it's definition.",
    )
    scale: None | float | TimeIntervalCollection = Field(default=None, description="")
    showBackground: None | bool | TimeIntervalCollection = Field(
        default=None, description=""
    )
    backgroundColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    fillColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    outlineWidth: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    pixelOffset: None | float | Cartesian2Value | TimeIntervalCollection = Field(
        default=None, description=""
    )


class Orientation(BaseCZMLObject, Interpolatable, Deletable):
    """Defines an orientation.  An orientation is a rotation that takes a vector expressed in the "body" axes of the object and transforms it to the Earth fixed axes.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Orientation>`__ for it's definition."""

    unitQuaternion: (
        None | list[float] | UnitQuaternionValue | TimeIntervalCollection
    ) = Field(default=None, description="")
    reference: None | str | ReferenceValue | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )
    velocityReference: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("reference")
    @classmethod
    def validate_reference(cls, r):
        if isinstance(r, str):
            return ReferenceValue(value=r)
        return r


class Model(BaseCZMLObject):
    """A 3D model.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Model>`__ for it's definition."""

    show: None | bool | TimeIntervalCollection = Field(default=None, description="")
    gltf: str | TimeIntervalCollection
    scale: None | float | TimeIntervalCollection = Field(default=None, description="")
    minimumPixelSize: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    maximumScale: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    incrementallyLoadTextures: None | bool | TimeIntervalCollection = Field(
        default=None, description=""
    )
    runAnimations: None | bool | TimeIntervalCollection = Field(
        default=None, description=""
    )
    shadows: None | ShadowMode | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ShadowMode>`__ for it's definition.",
    )
    heightReference: None | HeightReference | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/HeightReference>`__ for it's definition.",
    )
    silhouetteColor: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    silhouetteSize: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    color: None | Color | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Color>`__ for it's definition.",
    )
    colorBlendMode: None | ColorBlendMode | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/ColorBlendMode>`__ for it's definition.",
    )
    colorBlendAmount: None | float | TimeIntervalCollection = Field(
        default=None, description=""
    )
    distanceDisplayCondition: (
        None | DistanceDisplayCondition | TimeIntervalCollection
    ) = Field(default=None, description="")
    nodeTransformations: None | Any | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Any>`__ for it's definition.",
    )
    articulations: None | Any | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Any>`__ for it's definition.",
    )


class Uri(BaseCZMLObject, Deletable):
    """A URI value. The URI can optionally vary with time.

    See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/Uri>`__ for it's definition."""

    uri: None | str | TimeIntervalCollection = Field(
        default=None,
        description=" See `here <https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/str>`__ for it's definition.",
    )

    @field_validator("uri")
    @classmethod
    def _check_uri(cls, value: str):
        if is_url(value):
            return value
        try:
            parse_data_uri(value)
        except ValueError:
            raise TypeError("uri must be a URL or a data URI") from None
        return value

    @model_serializer
    def custom_serializer(self) -> None | str | TimeIntervalCollection:
        return self.uri
