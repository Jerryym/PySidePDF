# -*- coding: utf-8 -*-

import pdf2docx
import pdfplumber
import pandas as pd
from action import Action
from office import Office

class Converter:
    @staticmethod
    def convert(src_file, dst_file, action):
        if action == Action.Pdf2Word:
            Converter.do_pdf2word(src_file, dst_file)
        elif action == Action.Pdf2Excel:
            Converter.do_pdf2excel(src_file, dst_file)
        elif action == Action.Pdf2PPT:
            Converter.do_pdf2ppt(src_file, dst_file)
        elif action == Action.Pdf2Image:
            Converter.do_pdf2image(src_file, dst_file)
        elif action == Action.Word2Pdf:
            Converter.do_word2pdf(src_file, dst_file)
        elif action == Action.Excel2Pdf:
            Converter.do_excel2pdf(src_file, dst_file)
        elif action == Action.PPT2Pdf:
            Converter.do_ppt2pdf(src_file, dst_file)
        elif action == Action.PDFSplit:
            Converter.do_pdfsplit(src_file, dst_file)
        elif action == Action.PDFMerge:
            Converter.do_pdfmerge(src_file, dst_file)

    @staticmethod
    def do_pdf2word(src_file, dst_file):
        converter = pdf2docx.Converter(pdf_file = src_file)
        converter.convert(docx_filename=dst_file)
        converter.close()

    @staticmethod
    def do_pdf2excel(src_file, dst_file):
        print(src_file)
        # 读取pdf文件
        pdf = pdfplumber.open(src_file)
        if not pdf:
            print ("NULL")
            return 
        # 访问第一页
        first_page = pdf.pages[0]
        # 读取表格数据
        table = first_page.extract_table()
        table_data = pd.DataFrame(table[1:], columns = table[0])
        # 保存为excel
        table_data.to_excel(dst_file, index = False)
        pdf.close()

    @staticmethod
    def do_pdf2ppt(src_file, dst_file):
        pass

    @staticmethod
    def do_pdf2image(src_file, dst_file):
        pass

    @staticmethod
    def do_word2pdf(src_file, dst_file):
        Office.word2pdf(src_file, dst_file)

    @staticmethod
    def do_excel2pdf(src_file, dst_file):
        Office.excel2pdf(src_file, dst_file)

    @staticmethod
    def do_ppt2pdf(src_file, dst_file):
        Office.ppt2pdf(src_file, dst_file)

    @staticmethod
    def do_pdfsplit(src_file, dst_file):
        pass

    @staticmethod
    def do_pdfmerge(src_file, dst_file):
        pass