"""Planning and calculating a cozy tea party"""

__author__: str = "730474650"

# A function with a return of None, does not need to have a return statement


def main_planner(guests: int) -> None:
    """Number of guests attending the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats:" + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# To create a function: def function_name(<parameter list>) -> <return type>:


def tea_bags(people: int) -> int:
    """Calculate number of teabags needed for tea guests."""
    return 2 * people


# To create a function with arguement: function_name(<parameter0> = <arg0>, <parameter1> = <arg1>
# Convert result to an int before return


def treats(people: int) -> int:
    """Calculate number of treats needed for tea guests."""
    return int(tea_bags(people=people) * 3 / 2)


# Make sure the return is a float and not an integer: will give whole number instead of decimal


def cost(tea_count: int, treat_count: int) -> float:
    """The cost of teabags and treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party")))
