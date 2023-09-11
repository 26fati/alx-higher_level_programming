#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return super().__eq__(value)
