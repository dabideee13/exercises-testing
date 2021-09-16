from typing import Optional


class Formatter:
    def format(self, string: str) -> str:
        pass


class UpperFormatter(Formatter):
    """Format a string in upper case.

    >>> text = "hello world"
    >>> formatter = UpperFormatter()
    >>> formatter.format(text)
    'HELLO WORLD'
    """

    def format(self, string: str) -> str:
        return str(string).upper()


class LowerFormatter(Formatter):
    """Format a string in lower case.

    >>> text = "hello world"
    >>> formatter = LowerFormatter()
    >>> formatter.format(text)
    'hello world'
    """

    def format(self, string: str) -> str:
        return str(string).lower()


class DefaultFormatter(Formatter):
    """Format a string in title case.

    >>> text = "hello world"
    >>> formatter = DefaultFormatter()
    >>> formatter.format(text)
    'Hello World'
    """

    def format(self, string: str) -> str:
        return str(string).title()


def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format a string using the formatter object, which
    is expected to have a format() method that accepts a string.
    """

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


if __name__ == '__main__':

    import doctest
    doctest.testmod()
