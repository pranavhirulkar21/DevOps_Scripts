
import random

class CouponCollector:
    @staticmethod
    def generate_random_number(n):
        return random.randint(1,n)
    
    @staticmethod
    def collect_coupons(n):
        distinct_coupons = set()
        count = 0
        while len(distinct_coupons) <n:
            count += 1
            coupon = CouponCollector.generate_random_number(n)
            distinct_coupons.add(coupon)
        return count
    
def main():
        n = int(input("Enter the no. of distinct coupon numbers : "))
        count = CouponCollector.collect_coupons(n)
        print(f"Total random numbers nedded to have all distinct numbers: {count}")
        
if __name__ == "__main__":
        main()
   