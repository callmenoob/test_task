from alttester import AltDriver

from components.base import BaseComponent


class StaticBaseComponent(BaseComponent):
    def __init__(self, altdriver: AltDriver):
        self.altdriver = altdriver

    def get_static_property(self, static_property: str):
        return self.altdriver.get_static_property(self.component_name, static_property,
                                                  self.component_assembly)

    def set_static_property(self, static_property: str, value: any):
        self.altdriver.set_static_property(self.component_name, static_property,
                                           self.component_assembly, value)

    def call_static_method(self, method_name, params=[], params_type=None):
        self.altdriver.call_static_method(self.component_name, method_name, self.component_assembly, params,
                                          params_type)
