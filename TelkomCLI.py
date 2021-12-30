import sys
# from typing import List

FUNCTIONLIST=[
    {
        "Function":'help',
        "Alternate":'-h',
        "Description":"fungsi untuk menampilkan bantuan format: '-h' atau 'help'"
    },
    {
        "Function":'trans',
        "Alternate":'-t',
        "Description":"fungsi untuk mengubah file log menjadi txt atau json format: '{filepath} -t json'"
    },
    {
        "Function":'output',
        "Alternate":'-o',
        "Description":"fungsi untuk mengubah file log menjadi txt atau json format: '{filepath} -t json -o {outputpath}'"
    }
]
HElPFUNCTIONPOSITIONNUMBER = 0 #Help dictionary posituion order base on FUNCTIONLIST
TRANSPOSEFUNCTIONPOSITIONNUMBER = 1 #TRANSPOSE dictionary posituion order base on FUNCTIONLIST

def ReadArgs(Args, FunctionList):
    try:
        ReqFunction = []
        for Function in FunctionList:
            if Function['Alternate'] in str(Args).lower() or Function['Function'] in str(Args).lower():
                ReqFunction.append(Function['Function'])
            else:
                None
    except:
        print("Tidak ada input atau input salah, tulis help atau -h untuk mencari tau")
        exit()
    return ReqFunction

def Help(AllFunctionNames):
    print(f'Fungsi Nama\tAlternative\tFungsi Deskripsi \n')
    for Function in AllFunctionNames:
        print(f'{Function["Function"]}\t\t{Function["Alternate"]}\t\t{Function["Description"]}')
    print("keterangan tambahan:")
    print("untuk format lebih detail mengikuti contoh di file pdf, jadi contoh dipdf bisa dilakukan juga disini")
    return None

def ConvertToJson(FilePath, FileOutPut = None):
    try:
        File = open(FilePath,"r")
        NewFileName = FilePath[:-4]
        NewFile = open(f'{NewFileName}.json', "w") if FileOutPut == None else open(FileOutPut,"w")
        for line in File:
            NewFile.writelines(f'{str(line)}')
        File.close()
        NewFile.close()
        print("proses selesai")
    except:
        print("something wrong")
        exit()
    return None

def ConvertToPlain(FilePath, FileOutPut = None):
    try:
        File = open(FilePath,"r")
        NewFileName = FilePath[:-3]
        NewFile = open(f'{NewFileName}.txt', "w") if FileOutPut == None else open(FileOutPut,"w")
        for line in File:
            NewFile.writelines(f'{str(line)}')
        File.close()
        NewFile.close()
        print("proses selesai")
    except:
        print("something wrong")
        exit()
    return None

def Transpose(Args):
    try:
        FilePath =  Args[0]
        TransposeType = None if len(Args)<3 else str(Args[2]).lower()
        if TransposeType == "json":
            ConvertToJson(FilePath)
        else:
            ConvertToPlain(FilePath)
    except:
        print("Argumen yang dimasukkan tidak lengkap atau salah")
        exit()
    return None

def Output(Args):
    try:
        FilePath =  Args[0]
        FileOutput = Args[-1]
        TransposeType = None if len(Args)<5 else str(Args[2]).lower()
        if TransposeType == 'json' and TransposeType != str(FileOutput[-4:]):
            raise ValueError("format transpose berbeda dengan otput path")
        elif TransposeType == 'txt' and TransposeType != str(FileOutput[-3:]):
            raise ValueError("format transpose berbeda dengan otput path")
        
        if TransposeType == "json":
            ConvertToJson(FilePath, FileOutput)
        else:
            ConvertToPlain(FilePath, FileOutput)
    except:
        print("format transpose berbeda dengan otput path atau Argumen yang dimasukkan tidak lengkap atau salah")
        exit()
    return None
    
def Exe(FunctionLists, Args, ListOfAllFunctionNames, HelpFunctionOrder, TransposeFunctionOrder):
    try:
        if len(FunctionLists)<2 and FunctionLists[0] == ListOfAllFunctionNames[HelpFunctionOrder]["Function"]:
            Help(ListOfAllFunctionNames)
        elif len(FunctionLists)<2 and FunctionLists[0] == ListOfAllFunctionNames[TransposeFunctionOrder]["Function"]:
            Transpose(Args)
        elif ListOfAllFunctionNames[HelpFunctionOrder]["Function"] not in FunctionLists:
            Output(Args)
        else:
            raise ValueError
    except:
        print("fungsi tidak terbaca atau kombinasi fungsi salah")
        exit()
    return None

if __name__ == "__main__":
    # Args:List[str] = sys.argv
    Args = []
    for Counter, Arg in enumerate(sys.argv):
        if Counter>0:
            # Args.append(str(Arg).lower())
            Args.append(str(Arg))
    # print(Args)
    Functions = ReadArgs(Args, FUNCTIONLIST)
    # print(Functions)
    Exe(Functions, Args, FUNCTIONLIST, HElPFUNCTIONPOSITIONNUMBER, TRANSPOSEFUNCTIONPOSITIONNUMBER)