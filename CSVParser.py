import csv
import RowCheckController as Controller
data_delim = ','

newCsvFileFormat = ['ReportFiledDate', 'CandidateFirstName', 'CandidateLastName', 'PeriodBegining', 'PeriodEnding', 'TransactionID', 'TransactionType', 'TransactionAmount']
fileFormatDataPositions = []
rowChecker = Controller.RowCheckController()
fileHandle = open("converted_transactions.txt", "a") #append to the end of the file
data_list = [] #data after CandidateorcomitteeCheck

with open('transactions.csv', 'r') as file:
    reader = csv.reader(file)
    rowDataList = (next(reader))
    fileFormatDataPositions = rowChecker.FindDataPositionsForNewFormat(rowDataList, newCsvFileFormat)
    for row in reader:
        rowDataList = list(csv.reader(row))
        if len(rowDataList[1]) != 0:
            if rowChecker.IsCandidateOrCommitteeCOH(rowDataList[1][0]):
                if fileFormatDataPositions[len(fileFormatDataPositions)-1] < len(rowDataList)-1:
                    newRow = rowChecker.GenerateNewRow(rowDataList, fileFormatDataPositions, newCsvFileFormat)
                    data_list.append(newRow)

file.close()

with open("converted_transactions.csv", "w", newline='') as fp:
    wr = csv.writer(fp, dialect='excel', lineterminator='\n')
    wr.writerows(data_list)
    #wr.writerow(list1)
fileHandle.close()
