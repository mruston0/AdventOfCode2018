from dataclasses import dataclass
from typing import Any, List
import re
import arrow
import operator

words = open('inputs/day_4.txt', 'r')
lines = words.read().splitlines()       # Prevents trailing newline characters

# Let's try out Python's dataclasses feature.

@dataclass
class Sleep:
    start: int = 0
    end: int = 0 

    def total_time(self):
        return self.end - self.start

@dataclass
class Guard:
    id: str
    sleep_times: List[Sleep]

    def __repr__(self):
        return f"Guard {self.id}: Total Sleep Time = {self.total_sleep_time()}. Most Asleep Minute {self.most_asleep_minute()} over {self.volume_of_most_asleep_minute()} times."
    
    def total_sleep_time(self):
        return sum(map(lambda x: x.total_time(), self.sleep_times))
    
    def most_asleep_minute(self):
        minutes = [0] * 60
        for s in self.sleep_times:
            for x in range(s.start, s.end):
                minutes[x] += 1
        return minutes.index(max(minutes))

    def volume_of_most_asleep_minute(self):
        minutes = [0] * 60
        for s in self.sleep_times:
            for x in range(s.start, s.end):
                minutes[x] += 1
        return max(minutes)

@dataclass
class GuardRotation:
    guards = []

    def get_guard(self, id):
        if len([g for g in self.guards if g.id == id]) == 0:
            guard = Guard(id=id, sleep_times=[])
            self.guards.append(guard)
            return guard;
        else:
            return next(g for g in self.guards if g.id == id)
    
    def get_guard_highest_sleep_time(self):
        return sorted(self.guards, key=operator.methodcaller("total_sleep_time"))[-1]
    
    def get_guard_most_frequently_asleep_minute(self):
        s =  sorted(self.guards, key=operator.methodcaller("volume_of_most_asleep_minute"))
        for p in s:
            print(p)
        return s[-1]

def get_data(lines): 
    result = {}
    for line in lines:
        parts = re.split('\[| |\]', line)
        time = arrow.get(parts[1] + " " + parts[2])
        data = parts[4:]
        result[time] = data
    return sorted(result.items())

def build_guard_rotation(data):
    rotation = GuardRotation()

    for time, value in data:
        if value[0] == 'Guard':
            guard = rotation.get_guard(id=value[1])
        elif value[0] == 'falls':
            guard.sleep_times.append(Sleep(start=0, end=0)) 
            guard.sleep_times[-1].start = int(time.format('mm'))
        elif value[0] == 'wakes':
            guard.sleep_times[-1].end = int(time.format('mm'))
    return rotation
        


data = get_data(lines)

rotation = build_guard_rotation(data) 
for g in rotation.guards:
    print(g.id, len(g.sleep_times), "total sleep time", g.total_sleep_time(), "most asleep minute", g.most_asleep_minute())
highest_guard = rotation.get_guard_highest_sleep_time();
print(f"Guard with the highest sleep time is {highest_guard.id} time = {highest_guard.total_sleep_time()} fav minute = {highest_guard.most_asleep_minute()}")
print(f"Answer is {int(highest_guard.id[1:])*int(highest_guard.most_asleep_minute())}")

print("Part Two")
most_frequent_sleep_same_minute = rotation.get_guard_most_frequently_asleep_minute()
print(f"Guard is most frequently asleep on the same minute: {most_frequent_sleep_same_minute.id} Minute: {most_frequent_sleep_same_minute.most_asleep_minute()}")
print(f"Answer is {int(most_frequent_sleep_same_minute.id[1:])*int(most_frequent_sleep_same_minute.most_asleep_minute())}")

# 4345: too low.