from typing import Sequence, Any, Callable, Iterator


class FilterIter:
    """
    An iterator that filters items from a given sequence based on a specified function.

    Attributes:
        sequence (Sequence[Any]): The sequence of items to filter.
        func (Callable[[Any], bool]): The function used to determine if an item should be included.
        index (int): The current index in the sequence.
    """
    def __init__(self, sequence: Sequence[Any], func: Callable[[Any], bool]) -> None:
        """
        Initializes the FilterIter instance with a sequence and a filtering function.

        Parameters:
            sequence (Sequence[Any]): The sequence of items to filter.
            func (Callable[[Any], bool]): The function used to determine if an item should be included.
        """
        self.sequence = sequence
        self.func = func
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        """
        Returns the iterator itself.

        Returns:
            Iterator[Any]: The iterator object.
        """
        return self

    def __next__(self) -> Any:
        """
        Returns the next item in the sequence that satisfies the filtering function.

        Returns:
            Any: The next item in the sequence that passes the filter.

        Raises:
            StopIteration: If no further items satisfy the condition.
        """
        while True:
            if self.index == len(self.sequence):
                raise StopIteration
            value = self.sequence[self.index]
            self.index += 1
            if self.func(value):
                return value


def main() -> None:
    """
    Demonstrates the usage of FilterIter by filtering a list of mixed types.
    """
    f_iter = FilterIter([1, 2, 3, 4, 6, 0, None, 33, "fkj"], lambda x: x)
    while True:
        try:
            print(next(f_iter))
        except StopIteration:
            break


if __name__ == "__main__":
    main()
