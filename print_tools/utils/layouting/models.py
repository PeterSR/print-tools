import abc
from typing import Any
from pydantic import BaseModel


class CustomFieldsMixin(BaseModel):
    """
    Mixin for custom fields in Pydantic models.
    This allows for additional fields that are not defined in the model.
    """

    custom_fields: dict[str, Any] = {}


class Container(CustomFieldsMixin):
    width: float
    height: float


class ContainerSpec(BaseModel):
    container: Container
    max_amount: int

    def generate_containers(self) -> list[Container]:
        """
        Generate a list of containers based on the specification.
        """
        return [self.container.model_copy() for i in range(self.max_amount)]


class Box(CustomFieldsMixin):
    width: float
    height: float


class AppliedBox(BaseModel):
    """
    A box that has been applied to a layout.
    This can include additional information such as position, rotation, etc.
    """

    box_index: int  # Index of the box in the original list
    container_index: int  # Index in used_containers where this box is applied
    position: tuple[float, float] = (0.0, 0.0)  # x, y coordinates
    scale: float = 1.0  # scale factor
    rotation: float = 0.0  # rotation in degrees
    mirror_horizontal: bool = False
    mirror_vertical: bool = False


class LayoutResult(CustomFieldsMixin):
    used_containers: list[Container]
    applied_boxes: list[AppliedBox]


class BaseLayouter(abc.ABC):
    @abc.abstractmethod
    def perform_layout(
        self, available_containers: list[Container] | ContainerSpec, boxes: list[Box]
    ) -> LayoutResult:
        """
        Perform layout on the given boxes using the available containers.

        Args:
            available_containers: List of containers or a container specification.
            boxes: List of boxes to be laid out.

        Returns:
            LayoutResult containing the layout information.
        """
        raise NotImplementedError("Subclasses must implement this method.")
