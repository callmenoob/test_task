from enum import Enum
import os
import sys

from alttester import AltObject

sys.path.append(os.path.dirname(__file__))


class BaseComponent:
    component_name = None
    component_assembly = None

    @classmethod
    def get_component_property(cls, component: AltObject, property_name):
        if isinstance(property_name, Enum):
            property_name = property_name.value
        return component.get_component_property(cls.component_name, property_name, cls.component_assembly)

    @classmethod
    def wait_for_component_property(cls, component: AltObject, property_name, value,
                                    interval=0.1, timeout=5):
        if isinstance(property_name, Enum):
            property_name = property_name.value
        return component.wait_for_component_property(cls.component_name, property_name, value,
                                                     cls.component_assembly, interval=interval,
                                                     timeout=timeout)

    @classmethod
    def call_component_method(cls, component: AltObject, method_name, params=None, params_type=None):
        if isinstance(method_name, Enum):
            method_name = method_name.value
        return component.call_component_method(cls.component_name, method_name,
                                               cls.component_assembly, params, params_type)
