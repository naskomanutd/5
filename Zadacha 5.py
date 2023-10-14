def find_max_number(numbers):
  """
  Намира най-голямото число в списък от числа.

  Args:
    numbers: Списъкът с числа, в който да се намери най-голямото число.

  Returns:
    Най-голямото число в списъка.
  """

  max_number = numbers[0]
  for number in numbers:
    if number > max_number:
      max_number = number
  return max_number


def main():
  """
  Точка на влизане в програмата.
  """

  numbers = [5, 2, 3, 1, 4]
  max_number = find_max_number(numbers)
  print(f"Най-голямото число в списъка е {max_number}")


if __name__ == "__main__":
  main()