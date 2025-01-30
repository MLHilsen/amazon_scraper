import requests

def get_data(low, high):
    pass

def main():
    while True: # Get user input
        p_range_l, p_range_h = 0, 0

        p_range_l = input("Enter lower price bound $")
        if not p_range_l.isdigit():
            print("Must be a digit.")
            continue
        else:
            p_range_l = int(p_range_l)

        p_range_h = input("Enter upper price bound $")
        if not p_range_h.isdigit():
            print("Must be a digit.")
            continue
        else:
            p_range_h = int(p_range_h)

        if p_range_h <= p_range_l:
            print("Lower bound must be less than upper bound.")
            continue

        break

    get_data(p_range_l, p_range_h)

main()