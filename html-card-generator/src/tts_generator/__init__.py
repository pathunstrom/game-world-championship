import jinjax

from . import templates

catalog = jinjax.Catalog()
catalog.add_module(templates)


