# Owner: Ryan
# Date: 04-Sep-2024

def make_shirts(size, logo="I love Python"):
    print(f"\nPrint {logo.title()} on my {size.upper()} T-shirt.")


# 默认字样的大号T恤
make_shirts("l")
# 默认字样的中号T恤
make_shirts("m")
# 一件印有其他字样的T恤
make_shirts("6xl", "We have all the size you want")