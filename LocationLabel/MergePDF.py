#win32com.client 모듈 임포트 
# import win32com.client 

# #엑셀을 실행할 객체 생성 
# excel = win32com.client.Dispatch("Excel.Application") 

# #pdf로 변환할 파일명 선택 
# # wb = excel.Workbooks.Open("C:/Users/Zinus_user/Desktop/Zinus_RPA_project/LocationLabel/Location Label_012122.xlsx") 

# # #워크북의 시트명 설정 
# # ws_sht = wb.Worksheets("Lv4") 

# # #설정한 시트 선택 
# # ws_sht.Select() 

# # #PDF파일을 저장할 경로 및 파일명 지정 
# # savepath = "C:/Users/Zinus_user/Desktop/Zinus_RPA_project/LocationLabel/pdf/sample_pdf.pdf"

# # #활성화된 시트를 pdf 저장 
# # wb.ActiveSheet.ExportAsFixedFormat(0, savepath) 

# # 엑셀 워크북 및 프로그램 종료 
# # # 종료를 제대로 해주어야 다음 실행시 에러 안생김 
# # wb.Close(False)
# excel.Quit()

from glob import glob
from PyPDF2 import PdfFileMerger
class merge_all_pdf_class:

    def merge_all_pdf(self):

        BOOK = 'total_location_label'

        merger = PdfFileMerger()

        for f in glob('./LocationLabel/pdf/*.pdf'):
            merger.append(f)

        merger.write("./LocationLabel/"+BOOK + ".pdf")
        merger.close()