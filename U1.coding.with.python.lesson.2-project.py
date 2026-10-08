# module import
import math
import time


# user defined function
def convert_and_estimate_materials():
    # built in function 1, print
    print("trade measurement and material estimator")

    # loop using a while loop to handle repeated calculations
    while True:
        # built in function 2, input combined with float type casting
        length_feet = float(input("\nEnter wall length in feet (0 to exit): "))

        # decision making, using if-elif-else ladder
        if length_feet == 0:
            print("Exiting tool. Good luck with the job!")
            break
        elif length_feet < 0:
            print("Invalid measurement! Length must be a positive number.")
            time.sleep(1) # using time module pause
        else:
            # metric conversion, feet to meters
            length_meters = length_feet * 0.3048

            # built in function 3, str for string concatenation
            print(
                "Converted length: "
                + str(round(length_meters, 2))
                + " meters."
            )

            # module usage, math.ceil to round up brick/block estimates
            # assuming standard wall height requiring 60 bricks per linear meter
            bricks_needed = math.ceil(length_meters * 60)

            # built in function 4, len to inspect character count of summary text
            summary_text = "Total estimated bricks required: " + str(
                bricks_needed
            )
            print(summary_text)
            print(
                "Summary note character count: "
                + str(len(summary_text))
                + " chars."
            )

            time.sleep(1)


# calling the user defined function
convert_and_estimate_materials()
