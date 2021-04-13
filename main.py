import csv
import traceback

class FileModules():
    def __init__(self):
        self.nameOfColumns = ['BMI Category', 'BMI Range', 'Health Risk']

    def writeDataToCsvFile(self, fileName, data):
        with open(fileName + '.csv', '+w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([self.nameOfColumns])
            for row in data:
                writer.writerows([row])

    def readDataFromCsvFile(self, fileName, dataToRead):
        count = 0
        with open(fileName + '.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if dataToRead in row:
                    count = count + 1
        return count


class BMI():
    def __init__(self):
        self.fileModules = FileModules()
        self.fileName = "FileData"          # File for CSV file
        self.Category = ''                  # Category = Underweight Normal weight Overweight Moderately obese Severely obese Very severely obese
        self.HealthRisk = ''                # HealthRisk = Malnutrition risk Low risk Enhanced risk Medium risk High risk Very high risk
        self.dataToRead = 'Overweight'      # To find out total


    def calculateBMI(self, data):
        BMIList = []
        for data in data:
            # BMI(kg/m ) = mass(kg) / height(m)
            BMI = round(data['WeightKg'] / (data['HeightCm'] / 100), 1)
            self.Category, self.HealthRisk = self.BMICategoryAndHealthRisk(BMI)
            BMIList.append((self.Category, BMI, self.HealthRisk))
        self.fileModules.writeDataToCsvFile(self.fileName, BMIList)
        count = self.fileModules.readDataFromCsvFile(self.fileName, self.dataToRead)
        print('the total number of {} people are: {}'.format(self.dataToRead, count))

    # BMI Category and Health Risk
    def BMICategoryAndHealthRisk(self, BMI):
        if BMI <= 18.4:
            self.Category = 'Underweight'
            self.HealthRisk = 'Malnutrition risk'
        elif BMI >= 18.5 and BMI <=24.9:
            self.Category = 'Normal weight'
            self.HealthRisk = 'Low risk'
        elif BMI >= 25.0 and BMI <=29.9:
            self.Category = 'Overweight'
            self.HealthRisk = 'Enhanced risk'
        elif BMI >= 30.0 and BMI <=34.9:
            self.Category = 'Moderately obese'
            self.HealthRisk = 'Medium risk'
        elif BMI >= 35.0 and BMI <=39.9:
            self.Category = 'Severely obese'
            self.HealthRisk = 'High risk'
        elif BMI >= 40.0:
            self.Category = 'Very severely obese'
            self.HealthRisk = 'Very high risk'

        return self.Category, self.HealthRisk


def main():
    Data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}, {"Gender": "Male", "HeightCm": 161, "WeightKg":
        85}, {"Gender": "Male", "HeightCm": 180, "WeightKg": 77}, {"Gender": "Female", "HeightCm": 166,"WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]

    bmi = BMI()

    bmi.calculateBMI(Data)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(traceback.format_exc())
        print("Exception: ", e)
