#Hello Wolrd

A simple Python function to greet someone with "Hello" or "Goodbye" multiple times.

## Functionality

The `say_hello` function prints a greeting message to the standard output. You can customize the message with the person's name, the number of times the message is repeated, and whether to say "Goodbye" instead of "Hello".

## Parameters

- `name` (str): The name of the person or thing you want to greet.
- `repeat` (int, optional): The number of times to repeat the greeting message. Defaults to 1.
- `goodbye` (bool, optional): If set to True, the message changes to "Goodbye". Defaults to False.

## Returns

The function returns `None`. It prints the greeting message to the standard output (`stdout`).

## Examples

To greet the world once with "Hello":

```python
say_hello('World')

