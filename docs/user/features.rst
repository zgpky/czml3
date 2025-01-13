Features
========

The goal of czml3 is to make the process of writing CZML files in Python easy. This page details the features that allow czml3 to achieve this goal.

Type Checking
-------------

All classes enforces type checking on the inputs. This ensures that the data is in the correct format before it is written to the CZML file.

Cooercion of Data
-----------------

czml3 `coerces data to their right type <https://docs.pydantic.dev/latest/why/#json-schema>`_. See Example 2 in  :ref:`examples-label`.

Forbid Unrecognised Properties
------------------------------

czml3 raises an error if a model (class) receives an unrecognised input.

Minimal CZML File Creation
--------------------------

czml3 will remove all fields that are not set (i.e. ``None``). This ensures that the CZML file is as small as possible.
