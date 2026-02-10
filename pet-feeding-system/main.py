#!/usr/bin/env python3
"""
Pet Feeding System - Main Control Script
"""

import time
from datetime import datetime

class PetFeedingSystem:
    def __init__(self, pet_name):
        self.pet_name = pet_name
        self.feeding_times = []
        self.last_fed = None
        
    def set_feeding_schedule(self, times):
        """Set feeding times (list of 'HH:MM' strings)"""
        self.feeding_times = times
        print(f"Feeding schedule set for {self.pet_name}: {times}")
        
    def feed_now(self, portion_size="medium"):
        """Trigger immediate feeding"""
        self.last_fed = datetime.now()
        print(f"[{self.last_fed.strftime('%Y-%m-%d %H:%M:%S')}] "
              f"Feeding {self.pet_name} - Portion: {portion_size}")
        self._activate_feeder()
        
    def _activate_feeder(self):
        """Simulate feeder activation"""
        print("🔄 Activating feeder motor...")
        time.sleep(2)   # simulate motor running
        print("✅ Feeding complete!")
        
    def check_schedule(self):
        """Check if it's time to feed (safe from double-feeding)"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time in self.feeding_times:
            # Feed only once per scheduled minute
            if self.last_fed is None or self.last_fed.strftime("%H:%M") != current_time:
                self.feed_now()

def main():
    print("=" * 50)
    print("🐕 Pet Feeding System Initializing...")
    print("=" * 50)
    
    feeder = PetFeedingSystem("Buddy")
    
    # Feeding times: 8 AM, 1 PM, 7 PM
    feeder.set_feeding_schedule(["08:00", "13:00", "19:00"])
    
    print("\n🧪 Test feeding...")
    feeder.feed_now("small")
    
    print("\n✅ System ready!")
    print("Press Ctrl+C to exit\n")
    
    try:
        while True:
            feeder.check_schedule()
            time.sleep(60)   # check once per minute
    except KeyboardInterrupt:
        print("\n👋 System shutdown")

if __name__ == "__main__":
    main()
