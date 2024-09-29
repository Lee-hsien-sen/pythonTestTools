from H100 import sever_dev, sever_uae, sever_prod
from H100.calories import Calories
from H100.heartRate import HeartRate
from H100.walkSteps import WalkSteps
from H100.sportTime import SportTime
from H100.sleepAdd import SleepTime
from H100.waterIntake_addRecord import WaterIntake

host = sever_prod


def main():

    print("======================walkSteps============================================================")
    my_walkSteps = WalkSteps()
    w_walkSteps = my_walkSteps.walkSteps(host)

    print("======================heartRate============================================================")
    my_heartRate = HeartRate()
    w_walkSteps = my_heartRate.heartRate(host)

    print("=====================calories==============================================================")
    my_calories = Calories()
    my_calories.calories(host)

    print("======================sportTime============================================================")
    my_sportTime = SportTime()
    my_sportTime.sportTime(host)

    print("=======================sleep===============================================================")
    my_sleep = SleepTime()
    my_sleep.sleepAdd(host)

    print("=======================waterIntake===========================================================")
    my_waterIntake = WaterIntake()
    my_waterIntake.waterIntake(host)


if __name__ == "__main__":
    main()
