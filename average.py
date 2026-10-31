def avg(nums):
    if not nums:
        raise ValueError("avg() requires at least one number.")
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(avg([1, 2, 3]))
