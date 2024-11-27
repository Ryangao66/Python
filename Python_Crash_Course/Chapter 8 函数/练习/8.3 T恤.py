# Owner: Ryan
# Date: 04-Sep-2024/27-Nov-24

def make_shirts(size, logo):
    print(f"\nCan I please order a {size.upper()} T-shirt?")
    print(f"Print {logo.title()} on my {size.upper()} T-shirt.")


make_shirts("xl", "Danny")


def piano_practice(composer, work):
    print(f"I'm practicing {work} from {composer.title()}.")
    print()


piano_practice("mozart", "k311")