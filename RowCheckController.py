import datetime
import CommonFunctions
class RowCheckController:
    def IsCandidateOrCommitteeCOH(self, candidateOrCommiteCSV):
        if candidateOrCommiteCSV == 'COH':
            return True
        else:
            return False

    def FindDataPositionsForNewFormat(self, currentDataRow, NewDataFormat):
        PositionsList = []
        for format in NewDataFormat:
            if format in currentDataRow:
                PositionsList.append(currentDataRow.index(format))
        return PositionsList

    def GenerateNewRow(self, currentRow, DataPositions, fileFormat):
        newLine = []
        idx = 0;
        for i in DataPositions:
            if fileFormat[idx] == 'CandidateFirstName':
                newLine.append(currentRow[i] + currentRow[i+1])
                i+=1
            elif fileFormat[idx] == 'CandidateLastName':
                pass
            elif fileFormat[idx] == 'ReportFiledDate':
                if str(currentRow[i][0][:-3]).find('.') != -1:
                    cus_date = datetime.datetime.strptime(currentRow[i][0][:-3], "%Y-%m-%d %H:%M:%S.%f").timestamp()
                    newLine.append(cus_date)
                else:
                    cus_date = datetime.datetime.strptime(currentRow[i][0], "%Y-%m-%d %H:%M:%S").timestamp()
                    newLine.append(cus_date)
            elif (fileFormat[idx] == 'PeriodBegining' or fileFormat[idx] == 'PeriodEnding') and CommonFunctions.IsDateFormatValid(currentRow[i]):
                cus_date = datetime.datetime.strptime(currentRow[i][0], "%m/%d/%Y").date().isoformat()
                newLine.append(cus_date)
            else:
                newLine.append(currentRow[i])
            idx += 1;
        return newLine;
