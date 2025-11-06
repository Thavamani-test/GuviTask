# Find all ways to make Rs.10 using Rs.1, Rs.2, Rs.5, and Rs.10 coins

total_amount = 10
Numberofways = 0 # count combinations

print("Combinations of coins to make Rs.10:\n")

# Loop through all possibilities
for coin1 in range(total_amount + 1): # Rs.1 coins
    for coin2 in range(total_amount // 2 + 1): # Rs.2 coins
        for coin5 in range(total_amount // 5 + 1): # Rs.5 coins
            for coin10 in range(total_amount // 10 + 1): # Rs.10 coins
                if coin1 * 1 + coin2 * 2 + coin5 * 5 + coin10 * 10 == total_amount:
                    print(f"1₹ x {coin1}, 2₹ x {coin2}, 5₹ x {coin5}, 10₹ x {coin10}")
                    Numberofways += 1

print(f"\nTotal number of ways = {Numberofways}")
