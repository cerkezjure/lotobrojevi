import random
from twilio.rest import Client
import schedule
import time




def generate_lottery_numbers():
    main_numbers = sorted(random.sample(range(1, 51), 5))
    extra_numbers = sorted(random.sample(range(1, 13), 2))
    main_str = ",".join(str(n) for n in main_numbers)
    extra_str = ",".join(str(n) for n in extra_numbers)
    numbers_str = main_str + " / " + extra_str
    return numbers_str

lottery_numbers = generate_lottery_numbers()

print(lottery_numbers)
